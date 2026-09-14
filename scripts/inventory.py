#!/usr/bin/env python3
"""Build a per-spectrum inventory of the Chemotion IR dataset.

Reads every JCAMP-DX file shipped in the Chemotion IR collection together with
the accompanying ``meta_data.json``, and writes

* ``data/processed/inventory.csv`` with one row per spectrum file, and
* ``docs/inventory.md`` with a human-readable summary.

See ``docs/DOWNLOAD.md`` for how to obtain the dataset and for the quirks of
this particular export (files without extension, a point counter written in the
X column of the XYDATA block).
"""

from __future__ import annotations

import argparse
import contextlib
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from rdkit import Chem, RDLogger
from rdkit.Chem import rdMolDescriptors

RDLogger.DisableLog("rdApp.*")

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATASET = REPO_ROOT / "data" / "raw" / "chemotion_ir" / "data" / "dataset"
DEFAULT_CSV = REPO_ROOT / "data" / "processed" / "inventory.csv"
DEFAULT_MD = REPO_ROOT / "docs" / "inventory.md"
DEFAULT_SMARTS = REPO_ROOT / "rules" / "functional_groups_smarts.csv"

# Quality thresholds.
MIN_POINTS = 500
REQUIRED_X_LOW = 650.0
REQUIRED_X_HIGH = 3800.0

# Elements considered ordinary for organic IR work. Anything else is reported.
COMMON_ELEMENTS = {"C", "H", "N", "O", "S", "F", "Cl", "Br", "I", "P", "B", "Si"}

QUALITY_FLAGS = [
    ("flag_unreadable", "file could not be parsed as JCAMP-DX"),
    ("flag_no_xy_data", "no XYDATA block (peak table only)"),
    ("flag_no_smiles", "no SMILES in the metadata"),
    ("flag_invalid_smiles", "SMILES does not parse with RDKit"),
    ("flag_few_points", f"fewer than {MIN_POINTS} points"),
    ("flag_range_incomplete",
     f"X range does not cover {REQUIRED_X_LOW:.0f} to {REQUIRED_X_HIGH:.0f} cm-1"),
    ("flag_constant_y", "Y values are constant"),
    ("flag_nan_y", "Y values contain NaN or infinity"),
]

# Chemotion exports the same measurement more than once per analysis: a raw
# attachment and a peak-picked one, both carrying the full XYDATA block. Rows
# are deduplicated down to one per analysis id before anything is counted, with
# this preference order over the attachment file name.
EXPORT_PREFERENCE = [".dx", ".jdx", "peak.jdx", "other"]


# --------------------------------------------------------------------------
# JCAMP-DX reading
# --------------------------------------------------------------------------

class _Discard:
    """Swallow the per-line X-check warnings the jcamp library prints."""

    def write(self, text):  # noqa: D102
        return len(text)

    def flush(self):  # noqa: D102
        pass


def read_jcamp(path):
    """Return (record, parser_name, error). ``record`` is None on failure."""
    try:
        import jcamp
    except ImportError:  # pragma: no cover - jcamp is a hard requirement
        jcamp = None

    if jcamp is not None:
        try:
            with contextlib.redirect_stdout(_Discard()):
                return jcamp.readfile(str(path)), "jcamp", ""
        except Exception as exc:  # noqa: BLE001 - any parse failure falls back
            error = f"{type(exc).__name__}: {exc}"
    else:
        error = "jcamp not installed"

    record = read_jcamp_headers(path)
    if record is None:
        return None, "none", error
    return record, "fallback_headers", error


LDR_RE = re.compile(r"^\s*##(\$?[^=]+)=(.*)$")


def read_jcamp_headers(path):
    """Minimal fallback: read the labelled data records, ignore the Y block.

    Used only when the jcamp library raises. It recovers the header metadata so
    that the file still appears in the inventory with a description of what it
    is, but it does not decode the compressed ordinates, so the row is flagged
    as unreadable.
    """
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    record = {}
    children = []
    current = record
    for line in text.splitlines():
        match = LDR_RE.match(line)
        if not match:
            continue
        key = match.group(1).strip().lower()
        value = match.group(2).strip()
        if key == "title" and "title" in current and current is record:
            current = {}
            children.append(current)
        if key in ("xydata", "peak table", "peaktable"):
            current[key] = value
            continue
        current[key] = value
    if children:
        record["children"] = children
    return record


def as_float(value):
    try:
        out = float(value)
    except (TypeError, ValueError):
        return None
    return out if np.isfinite(out) else None


def candidate_blocks(record):
    """Yield the record itself plus any child blocks, outermost first."""
    if record is None:
        return []
    blocks = [record]
    blocks.extend(record.get("children", []) or [])
    return blocks


def pick_spectrum_block(record):
    """Return the block holding the continuous IR spectrum, or None."""
    with_data = []
    for block in candidate_blocks(record):
        x = block.get("x")
        y = block.get("y")
        if x is None or y is None or len(x) == 0 or len(x) != len(y):
            continue
        with_data.append(block)
    if not with_data:
        return None
    for block in with_data:
        data_type = str(block.get("data type", "")).upper()
        data_class = str(block.get("data class", "")).upper()
        if "INFRARED" in data_type and "PEAK" not in data_type and "PEAK" not in data_class:
            return block
    return with_data[0]


def normalise_y_units(raw):
    text = str(raw or "").strip().upper()
    if not text:
        return "unknown"
    if "ABSORB" in text or text in ("A", "AU", "ABS"):
        return "absorbance"
    if "TRANSMIT" in text or "TRANSMISSION" in text or text in ("%T", "T"):
        return "transmittance"
    if "REFLECT" in text:
        return "reflectance"
    if "KUBELKA" in text:
        return "kubelka_munk"
    return "other"


def describe_spectrum(record):
    """Extract the spectral description from a parsed JCAMP record."""
    out = {
        "data_type": "",
        "data_class": "",
        "x_units": "",
        "y_units_raw": "",
        "y_units": "unknown",
        "n_points": 0,
        "x_min": None,
        "x_max": None,
        "x_step_mean": None,
        "resolution": "",
        "y_min": None,
        "y_max": None,
        "n_nan": 0,
        "has_xy_data": False,
        "jcamp_title": "",
        "jcamp_origin": "",
        "jcamp_owner": "",
        "jcamp_date": "",
        "jcamp_version": "",
        "n_blocks": 0,
    }
    if record is None:
        return out

    blocks = candidate_blocks(record)
    out["n_blocks"] = len(blocks)
    for key, field in (("title", "jcamp_title"), ("origin", "jcamp_origin"),
                       ("owner", "jcamp_owner"), ("date", "jcamp_date"),
                       ("jcamp-dx", "jcamp_version")):
        for block in blocks:
            value = block.get(key)
            if value not in (None, ""):
                out[field] = str(value).strip()
                break

    block = pick_spectrum_block(record)
    if block is None:
        return out

    out["has_xy_data"] = True
    out["data_type"] = str(block.get("data type", "")).strip()
    out["data_class"] = str(block.get("data class", "")).strip()
    out["x_units"] = str(block.get("xunits", "")).strip()
    out["y_units_raw"] = str(block.get("yunits", "")).strip()
    out["y_units"] = normalise_y_units(block.get("yunits"))
    out["resolution"] = str(block.get("resolution", "") or "").strip()

    x = np.asarray(block["x"], dtype=float)
    y = np.asarray(block["y"], dtype=float)
    out["n_points"] = int(x.size)
    finite_x = x[np.isfinite(x)]
    if finite_x.size:
        out["x_min"] = float(finite_x.min())
        out["x_max"] = float(finite_x.max())
        if finite_x.size > 1:
            span = float(finite_x.max() - finite_x.min())
            out["x_step_mean"] = span / (finite_x.size - 1)
    finite_y = y[np.isfinite(y)]
    out["n_nan"] = int(y.size - finite_y.size)
    if finite_y.size:
        out["y_min"] = float(finite_y.min())
        out["y_max"] = float(finite_y.max())
    return out


# --------------------------------------------------------------------------
# Metadata
# --------------------------------------------------------------------------

def quill_to_text(raw):
    """Flatten the Quill delta stored in the ``content`` field to plain text."""
    if not raw:
        return ""
    try:
        delta = json.loads(raw)
    except (TypeError, ValueError):
        return str(raw).strip()
    parts = []
    for op in delta.get("ops", []) if isinstance(delta, dict) else []:
        insert = op.get("insert") if isinstance(op, dict) else None
        if isinstance(insert, str):
            parts.append(insert)
    return " ".join("".join(parts).split())


def load_metadata(dataset_dir):
    """Map spectrum file id to the metadata of the sample it belongs to."""
    path = Path(dataset_dir) / "meta_data.json"
    with open(path, encoding="utf-8") as handle:
        entries = json.load(handle)

    by_file = {}
    for entry in entries:
        affiliations = entry.get("affiliations") or {}
        authors = entry.get("authors") or []
        author_names = "; ".join(
            str(a.get("name") or "").strip() for a in authors if a.get("name")
        )
        affiliation_names = "; ".join(
            str(v).strip() for v in affiliations.values() if v
        )
        orcids = "; ".join(str(a.get("ORCID")) for a in authors if a.get("ORCID"))
        common = {
            "sample_id": entry.get("sample_id"),
            "analysis_id": entry.get("analysis_id"),
            "analysis_kind": entry.get("kind") or "",
            "smiles_raw": entry.get("cano_smiles") or "",
            "authors": author_names,
            "author_orcids": orcids,
            "affiliations": affiliation_names,
            "reported_ir_text": quill_to_text(entry.get("content")),
        }
        for dataset in entry.get("datasets") or []:
            instrument = str(dataset.get("instrument") or "").strip()
            for attachment in dataset.get("attacments") or []:
                identifier = str(attachment.get("identifier") or "")
                file_id = identifier.rsplit("/", 1)[-1]
                if not file_id:
                    continue
                by_file[file_id] = dict(
                    common,
                    instrument=instrument,
                    attachment_id=attachment.get("id"),
                    attachment_filename=attachment.get("filename") or "",
                    attachment_identifier=identifier,
                )
    return by_file


# --------------------------------------------------------------------------
# Structures
# --------------------------------------------------------------------------

def load_smarts(path):
    """Read the ground-truth SMARTS table, keeping the file order."""
    groups = []
    with open(path, encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            name = (row.get("group") or "").strip()
            smarts = (row.get("smarts") or "").strip()
            if not name or not smarts or smarts.upper() == "TODO":
                continue
            pattern = Chem.MolFromSmarts(smarts)
            if pattern is None:
                print(f"warning: SMARTS for '{name}' does not compile, skipped",
                      file=sys.stderr)
                continue
            groups.append((name, smarts, pattern))
    return groups


def describe_structure(smiles, groups, cache):
    """Canonical SMILES, InChIKey, formula, element set and group membership."""
    if smiles in cache:
        return cache[smiles]

    out = {
        "smiles_canonical": "",
        "inchikey": "",
        "formula": "",
        "n_fragments": 0,
        "is_multifragment": False,
        "elements": "",
        "unusual_elements": "",
        "has_unusual_elements": False,
        "n_heavy_atoms": 0,
        "smiles_valid": False,
    }
    groups_out = {f"fg_{name}": False for name, _, _ in groups}

    mol = Chem.MolFromSmiles(smiles) if smiles else None
    if mol is not None:
        out["smiles_valid"] = True
        out["smiles_canonical"] = Chem.MolToSmiles(mol)
        out["formula"] = rdMolDescriptors.CalcMolFormula(mol)
        out["n_heavy_atoms"] = mol.GetNumHeavyAtoms()
        out["n_fragments"] = len(Chem.GetMolFrags(mol))
        out["is_multifragment"] = out["n_fragments"] > 1
        try:
            out["inchikey"] = Chem.MolToInchiKey(mol) or ""
        except Exception:  # noqa: BLE001 - InChI can fail on exotic valences
            out["inchikey"] = ""
        symbols = sorted({atom.GetSymbol() for atom in mol.GetAtoms()})
        if any(atom.GetTotalNumHs() for atom in mol.GetAtoms()) and "H" not in symbols:
            symbols = sorted(set(symbols) | {"H"})
        out["elements"] = " ".join(symbols)
        unusual = sorted(set(symbols) - COMMON_ELEMENTS)
        out["unusual_elements"] = " ".join(unusual)
        out["has_unusual_elements"] = bool(unusual)
        for name, _, pattern in groups:
            groups_out[f"fg_{name}"] = mol.HasSubstructMatch(pattern)

    out.update(groups_out)
    cache[smiles] = out
    return out


# --------------------------------------------------------------------------
# Inventory
# --------------------------------------------------------------------------

def build_inventory(dataset_dir, smarts_path):
    dataset_dir = Path(dataset_dir)
    spectra_dir = dataset_dir / "JCAMP-DX Files" / "exp"
    if not spectra_dir.is_dir():
        raise SystemExit(
            f"spectra directory not found: {spectra_dir}\n"
            "See docs/DOWNLOAD.md for how to obtain and unpack the dataset."
        )

    groups = load_smarts(smarts_path)
    metadata = load_metadata(dataset_dir)
    cache = {}

    files = sorted(p for p in spectra_dir.iterdir() if p.is_file())
    rows = []
    for index, path in enumerate(files, start=1):
        if index % 500 == 0 or index == len(files):
            print(f"  {index}/{len(files)} files", file=sys.stderr)

        file_id = path.name
        meta = metadata.get(file_id, {})
        record, parser, error = read_jcamp(path)
        spec = describe_spectrum(record)
        smiles = meta.get("smiles_raw", "")
        struct = describe_structure(smiles, groups, cache)

        row = {
            "file_id": file_id,
            "file_path": path.relative_to(REPO_ROOT).as_posix(),
            "file_size_bytes": path.stat().st_size,
            "in_metadata": bool(meta),
            "sample_id": meta.get("sample_id", ""),
            "analysis_id": meta.get("analysis_id", ""),
            "analysis_kind": meta.get("analysis_kind", ""),
            "attachment_id": meta.get("attachment_id", ""),
            "attachment_filename": meta.get("attachment_filename", ""),
            "attachment_identifier": meta.get("attachment_identifier", ""),
            "instrument": meta.get("instrument", ""),
            "authors": meta.get("authors", ""),
            "author_orcids": meta.get("author_orcids", ""),
            "affiliations": meta.get("affiliations", ""),
            "reported_ir_text": meta.get("reported_ir_text", ""),
            "smiles_raw": smiles,
            "parser": parser,
            "parse_error": error if parser != "jcamp" else "",
        }
        row.update(struct)
        row.update(spec)

        n_points = spec["n_points"]
        x_min, x_max = spec["x_min"], spec["x_max"]
        y_min, y_max = spec["y_min"], spec["y_max"]
        covers = (
            x_min is not None and x_max is not None
            and x_min <= REQUIRED_X_LOW and x_max >= REQUIRED_X_HIGH
        )
        row["flag_unreadable"] = record is None or parser != "jcamp"
        row["flag_no_xy_data"] = not spec["has_xy_data"]
        row["flag_no_smiles"] = not smiles
        row["flag_invalid_smiles"] = bool(smiles) and not struct["smiles_valid"]
        row["flag_few_points"] = n_points < MIN_POINTS
        row["flag_range_incomplete"] = not covers
        row["flag_constant_y"] = (
            spec["has_xy_data"]
            and y_min is not None and y_max is not None
            and y_max - y_min == 0.0
        )
        row["flag_nan_y"] = spec["n_nan"] > 0
        row["qc_pass"] = not any(row[name] for name, _ in QUALITY_FLAGS)
        row["attachment_kind"] = attachment_kind(row["attachment_filename"])
        rows.append(row)

    df = pd.DataFrame(rows)
    df["is_primary_export"] = mark_primary_exports(df)
    return df, groups


def attachment_kind(filename):
    """Classify the export by file name suffix."""
    name = str(filename or "").lower()
    if name.endswith(".peak.jdx"):
        return "peak.jdx"
    for suffix in (".dx", ".jdx"):
        if name.endswith(suffix):
            return suffix
    return "other"


def mark_primary_exports(df):
    """One row per analysis id: the preferred export, breaking ties on quality."""
    rank = {kind: index for index, kind in enumerate(EXPORT_PREFERENCE)}
    order = pd.DataFrame({
        "qc_rank": (~df["qc_pass"]).astype(int),
        "kind_rank": df["attachment_kind"].map(rank).fillna(len(rank)).astype(int),
        "points_rank": -pd.to_numeric(df["n_points"], errors="coerce").fillna(0),
        "file_id": df["file_id"],
    })
    # Files with no analysis id cannot be grouped; each one stands on its own.
    key = df["analysis_id"].astype(str).where(
        df["analysis_id"].astype(str) != "", "file:" + df["file_id"])
    order = order.assign(key=key)
    winners = (order.sort_values(["key", "qc_rank", "kind_rank", "points_rank", "file_id"])
               .groupby("key", sort=False)
               .head(1)
               .index)
    primary = pd.Series(False, index=df.index)
    primary.loc[winners] = True
    return primary


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------

def md_table(header, rows):
    lines = ["| " + " | ".join(header) + " |",
             "| " + " | ".join("---" for _ in header) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(lines)


def counts_table(series, header, limit=None, total=None):
    counts = series.fillna("").astype(str).replace("", "(missing)").value_counts()
    total = total if total is not None else int(counts.sum())
    rows = []
    for value, count in counts.items():
        share = 100.0 * count / total if total else 0.0
        rows.append([value, count, f"{share:.1f}%"])
    truncated = 0
    if limit is not None and len(rows) > limit:
        truncated = len(rows) - limit
        remainder = sum(int(r[1]) for r in rows[limit:])
        rows = rows[:limit]
        rows.append([f"(other, {truncated} distinct values)", remainder,
                     f"{100.0 * remainder / total:.1f}%" if total else "0.0%"])
    return md_table(header, rows)


def write_report(df, groups, path, dataset_dir):
    total = len(df)
    primary = df[df["is_primary_export"]]
    valid = df[df["qc_pass"] & df["is_primary_export"]]
    n_valid = len(valid)

    try:
        location = Path(dataset_dir).resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        location = Path(dataset_dir).as_posix()

    parts = []
    parts.append("# Chemotion IR inventory\n")
    parts.append(
        "Generated by `scripts/inventory.py` from the Chemotion IR collection\n"
        "(RADAR4Chem, DOI 10.22000/OGoEQGlsZGElrgst, CC BY-SA 4.0). One row per\n"
        "JCAMP-DX file in `data/processed/inventory.csv`; this file summarises it.\n"
    )
    parts.append(f"Dataset directory: `{location}`\n")
    parts.append(
        "**Unit of analysis.** Chemotion exports every measurement more than once:\n"
        "a raw attachment and a peak-picked one, and both carry the full XYDATA\n"
        "block, so the raw file count is close to twice the number of measurements.\n"
        "Every count below other than sections 1 and 2 is taken over one row per\n"
        "analysis id, selected by the `is_primary_export` column of the CSV.\n"
    )

    # 1. Totals
    parts.append("## 1. Totals\n")
    parts.append(md_table(
        ["Quantity", "Count"],
        [
            ["JCAMP-DX files found", total],
            ["Files referenced by `meta_data.json`", int(df["in_metadata"].sum())],
            ["Files parsed by the `jcamp` library", int((df["parser"] == "jcamp").sum())],
            ["Files with a continuous XYDATA block", int((~df["flag_no_xy_data"]).sum())],
            ["Distinct sample ids", df["sample_id"].replace("", pd.NA).nunique()],
            ["Distinct analysis ids", df["analysis_id"].replace("", pd.NA).nunique()],
            ["Rows kept as primary export (one per analysis)", len(primary)],
            ["Primary-export spectra passing every quality filter", n_valid],
        ],
    ))
    parts.append("")
    parts.append("Exports per analysis, and how the duplicates are named:\n")
    parts.append(counts_table(df["attachment_kind"], ["File name suffix", "Files", "Share"]))
    parts.append("")

    # 2. Filters
    parts.append("## 2. Quality filters\n")
    parts.append(
        "Each flag is raised independently; a file can raise several. "
        "`qc_pass` is true only when no flag is raised.\n"
    )
    rows = []
    for name, description in QUALITY_FLAGS:
        failed = int(df[name].sum())
        rows.append([f"`{name}`", description, failed, total - failed,
                     f"{100.0 * (total - failed) / total:.1f}%" if total else "0.0%"])
    parts.append(md_table(["Flag", "Meaning", "Files flagged", "Files passing", "Pass rate"], rows))
    parts.append("")
    n_pass_files = int(df["qc_pass"].sum())
    parts.append(
        f"**{n_pass_files} of {total} files pass every filter** "
        f"({100.0 * n_pass_files / total:.1f}%). After collapsing the duplicate "
        f"exports, that is **{n_valid} usable spectra**, one per analysis.\n"
        if total else "")

    combos = (df.loc[~df["qc_pass"], [name for name, _ in QUALITY_FLAGS]]
              .apply(lambda r: ", ".join(n for n in r.index if r[n]), axis=1))
    if len(combos):
        parts.append("Most common flag combinations among the rejected files:\n")
        rows = [[f"`{value}`", count]
                for value, count in combos.value_counts().head(10).items()]
        parts.append(md_table(["Flags raised", "Files"], rows))
        parts.append("")

    # 3. Instruments
    parts.append("## 3. Instruments\n")
    parts.append("All analyses:\n")
    parts.append(counts_table(primary["instrument"], ["Instrument", "Analyses", "Share"], limit=25))
    parts.append("")
    parts.append("Spectra passing every filter:\n")
    parts.append(counts_table(valid["instrument"], ["Instrument", "Spectra", "Share"], limit=25))
    parts.append("")

    # 4. Units
    parts.append("## 4. Y units\n")
    parts.append(counts_table(primary["y_units"], ["Y unit (normalised)", "Analyses", "Share"]))
    parts.append("")
    parts.append("Raw `##YUNITS` strings as written in the files:\n")
    parts.append(counts_table(primary["y_units_raw"], ["`##YUNITS`", "Analyses", "Share"], limit=15))
    parts.append("")
    parts.append("X units:\n")
    parts.append(counts_table(primary["x_units"], ["`##XUNITS`", "Analyses", "Share"], limit=10))
    parts.append("")

    # 5. Ranges
    parts.append("## 5. Spectral ranges and sampling\n")
    with_data = primary[~primary["flag_no_xy_data"]]
    if len(with_data):
        stats = []
        for column, label in (("x_min", "X min (cm-1)"), ("x_max", "X max (cm-1)"),
                              ("n_points", "Points"), ("x_step_mean", "Mean step (cm-1)")):
            series = pd.to_numeric(with_data[column], errors="coerce").dropna()
            if not len(series):
                continue
            stats.append([
                label, f"{series.min():.4g}", f"{series.quantile(0.25):.4g}",
                f"{series.median():.4g}", f"{series.quantile(0.75):.4g}",
                f"{series.max():.4g}",
            ])
        parts.append(md_table(["Quantity", "Min", "Q1", "Median", "Q3", "Max"], stats))
        parts.append("")
        ranges = with_data.apply(
            lambda r: f"{r['x_min']:.0f} to {r['x_max']:.0f}"
            if pd.notna(r["x_min"]) and pd.notna(r["x_max"]) else "(missing)",
            axis=1,
        )
        parts.append("Most common X ranges, rounded to 1 cm-1:\n")
        parts.append(counts_table(ranges, ["X range (cm-1)", "Analyses", "Share"], limit=15))
        parts.append("")
        covered = int((~with_data["flag_range_incomplete"]).sum())
        parts.append(
            f"{covered} of {len(with_data)} analyses with XYDATA cover the full "
            f"{REQUIRED_X_LOW:.0f} to {REQUIRED_X_HIGH:.0f} cm-1 window.\n"
        )
    else:
        parts.append("No file carries a continuous XYDATA block.\n")

    parts.append("### Declared resolution\n")
    parts.append(counts_table(primary["resolution"], ["`##RESOLUTION`", "Analyses", "Share"], limit=15))
    parts.append("")

    # 6. Duplicates
    parts.append("## 6. Duplicate structures\n")
    keys = valid.loc[valid["inchikey"] != "", "inchikey"]
    key_counts = keys.value_counts()
    repeated = key_counts[key_counts > 1]
    parts.append(md_table(
        ["Quantity", "Count"],
        [
            ["Spectra passing every filter", n_valid],
            ["With a computable InChIKey", int(len(keys))],
            ["Distinct InChIKeys", int(key_counts.size)],
            ["InChIKeys with more than one spectrum", int(repeated.size)],
            ["Spectra belonging to a repeated InChIKey", int(repeated.sum())],
            ["Largest number of spectra for one InChIKey",
             int(key_counts.max()) if key_counts.size else 0],
        ],
    ))
    parts.append("")
    if repeated.size:
        rows = []
        for key, count in repeated.head(10).items():
            subset = valid[valid["inchikey"] == key]
            formula = subset["formula"].iloc[0]
            rows.append([f"`{key}`", formula, count])
        parts.append("Most repeated structures:\n")
        parts.append(md_table(["InChIKey", "Formula", "Spectra"], rows))
        parts.append("")

    # 7. Composition
    parts.append("## 7. Composition of the valid set\n")
    multifragment = int(valid["is_multifragment"].sum())
    unusual = int(valid["has_unusual_elements"].sum())
    mf_molecules = valid.loc[valid["is_multifragment"], "inchikey"].nunique()
    ue_molecules = valid.loc[valid["has_unusual_elements"], "inchikey"].nunique()
    parts.append(md_table(
        ["Quantity", "Spectra", "Share of valid", "Distinct InChIKeys"],
        [
            ["Salts or multi-fragment SMILES (contain a dot)", multifragment,
             f"{100.0 * multifragment / n_valid:.1f}%" if n_valid else "0.0%",
             mf_molecules],
            ["Containing an element outside C H N O S F Cl Br I P B Si", unusual,
             f"{100.0 * unusual / n_valid:.1f}%" if n_valid else "0.0%",
             ue_molecules],
        ],
    ))
    parts.append("")
    element_counter = Counter()
    for value in valid.loc[valid["has_unusual_elements"], "unusual_elements"]:
        element_counter.update(value.split())
    if element_counter:
        parts.append("Unusual elements, by number of valid spectra:\n")
        parts.append(md_table(
            ["Element", "Spectra"],
            [[symbol, count] for symbol, count in element_counter.most_common()],
        ))
        parts.append("")
    parts.append("Number of fragments per valid spectrum:\n")
    parts.append(counts_table(valid["n_fragments"], ["Fragments", "Spectra", "Share"], limit=10))
    parts.append("")

    # 8. Functional groups
    parts.append("## 8. Functional group coverage\n")
    parts.append(
        "Ground truth from `rules/functional_groups_smarts.csv`, matched with RDKit\n"
        "against the structure of each sample. Counted over the spectra that pass\n"
        "every quality filter, and over the distinct structures behind them.\n"
    )
    rows = []
    for name, smarts, _ in groups:
        column = f"fg_{name}"
        if column not in valid.columns:
            continue
        hits = valid[valid[column]]
        n_hits = int(len(hits))
        molecules = hits["inchikey"].replace("", pd.NA).nunique()
        rows.append([
            name, f"`{smarts}`", n_hits,
            f"{100.0 * n_hits / n_valid:.1f}%" if n_valid else "0.0%",
            molecules,
        ])
    parts.append(md_table(
        ["Group", "SMARTS", "Valid spectra", "Share", "Distinct InChIKeys"], rows))
    parts.append("")
    counts_per_spectrum = valid[[f"fg_{n}" for n, _, _ in groups
                                 if f"fg_{n}" in valid.columns]].sum(axis=1)
    if len(counts_per_spectrum):
        parts.append(
            f"A valid spectrum matches {counts_per_spectrum.mean():.2f} of the "
            f"{len(groups)} patterns on average "
            f"(median {counts_per_spectrum.median():.0f}, "
            f"minimum {int(counts_per_spectrum.min())}, "
            f"maximum {int(counts_per_spectrum.max())}). "
            f"Spectra matching no pattern at all: "
            f"{int((counts_per_spectrum == 0).sum())}.\n"
        )
    empty = [name for name, _, _ in groups
             if f"fg_{name}" in valid.columns and not valid[f"fg_{name}"].any()]
    if empty:
        parts.append(
            "Groups with no example in the valid set, and therefore not "
            "evaluable on this dataset: " + ", ".join(f"`{n}`" for n in empty) + ".\n"
        )

    parts.append("## 9. Notes\n")
    parts.append(
        "- The spectrum files carry no extension and are named by the UUID that\n"
        "  closes the `identifier` field of each attachment in `meta_data.json`.\n"
        "- Chemotion writes a descending point counter in the X column of the\n"
        "  XYDATA block instead of the wavenumber, so the X axis is reconstructed\n"
        "  from `##FIRSTX`, `##LASTX` and `##NPOINTS`. The `jcamp` library does\n"
        "  this correctly but emits an X-check warning per line, suppressed here.\n"
        "- Most analyses appear twice, as a `.dx` and a `.jdx` attachment, and\n"
        "  both files carry the same XYDATA block. The `is_primary_export` column\n"
        "  marks one row per analysis id, preferring `.dx` over `.jdx` over\n"
        "  `.peak.jdx`, and preferring rows that pass the quality filters. No\n"
        "  analysis in this release disagrees between its exports on point count.\n"
        "- Files whose only data block is a peak table raise `flag_no_xy_data`.\n"
        "  They are kept in the inventory because they record the bands the\n"
        "  depositors themselves picked, which is a separate object of study.\n"
        "- `reported_ir_text` holds the IR band list written by the depositor in\n"
        "  the publication, flattened from the Quill delta in the `content` field.\n"
    )

    Path(path).write_text("\n".join(parts).rstrip() + "\n",
                          encoding="utf-8", newline="\n")


# --------------------------------------------------------------------------

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset-dir", default=str(DEFAULT_DATASET),
                        help="directory holding meta_data.json and 'JCAMP-DX Files'")
    parser.add_argument("--smarts", default=str(DEFAULT_SMARTS),
                        help="ground-truth SMARTS table")
    parser.add_argument("--out-csv", default=str(DEFAULT_CSV))
    parser.add_argument("--out-md", default=str(DEFAULT_MD))
    args = parser.parse_args(argv)

    print("reading spectra ...", file=sys.stderr)
    df, groups = build_inventory(args.dataset_dir, args.smarts)

    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_csv, index=False, lineterminator="\n", encoding="utf-8")
    print(f"wrote {out_csv} ({len(df)} rows, {len(df.columns)} columns)", file=sys.stderr)

    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    write_report(df, groups, out_md, args.dataset_dir)
    print(f"wrote {out_md}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
