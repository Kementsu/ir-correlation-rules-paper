"""
nist_inventory.py: inventory of the NIST WebBook condensed-phase replication
set, in the same shape as the Chemotion inventory so that preprocess.py,
bands.py and evaluate_rules.py run on it unchanged (with --dataset nist).

Input:  data/raw/nist/jdx/<ID>_<index>.jdx, data/raw/nist/mol/<ID>.mol,
        data/processed/nist_index.csv (from nist_download.py)
Output: data/processed/inventory_nist.csv, docs/inventory_nist.md

Selection rules (pre-specified for the replication, see
docs/nist_replication_plan.md):
  * usable = JCAMP with data points, X units in 1/CM or MICROMETERS, Y in
    transmittance or absorbance, phase condensed by ##STATE, at least 500
    points, covering 700 to 3800 cm-1 after unit conversion (many prism-era spectra start at 650 to 700; rules whose window reaches below a spectrum X range are scored only on spectra that cover the window), a valid
    structure from the WebBook MOL file
  * one spectrum per species (is_primary_export): X already in 1/CM
    preferred over micrometers, then preparation in the order
    kbr > liquid/film > solution > mull > other, then lowest index
  * preparation classes from ##STATE: kbr, mull, solution, liquid, other
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors

sys.path.insert(0, str(Path(__file__).resolve().parent))
from inventory import load_smarts, describe_structure  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "nist"
PROCESSED = ROOT / "data" / "processed"
DOCS = ROOT / "docs"
SMARTS = ROOT / "rules" / "functional_groups_smarts.csv"

PREP_ORDER = {"kbr": 0, "liquid": 1, "solution": 2, "mull": 3, "other": 4}


def header(text: str, key: str) -> str:
    m = re.search(r"##" + re.escape(key) + r"\s*=\s*(.+)", text, re.I)
    return m.group(1).strip() if m else ""


def prep_class(state: str) -> str:
    u = state.upper()
    if any(w in u for w in ("KBR", "DISC", "PELLET", "PRESSING")):
        return "kbr"
    if any(w in u for w in ("MULL", "NUJOL", "OIL", "FLUOROLUBE")):
        return "mull"
    if any(w in u for w in ("SOLUTION", "CCL4", "CS2", "CHCL3", "% IN")):
        return "solution"
    if any(w in u for w in ("LIQUID", "NEAT", "FILM", "CAPILLARY", "SMEAR", "MELT")):
        return "liquid"
    return "other"


def mol_to_smiles(path: Path) -> str:
    try:
        mol = Chem.MolFromMolFile(str(path), sanitize=True)
    except Exception:
        mol = None
    return Chem.MolToSmiles(mol) if mol is not None else ""


def main() -> int:
    idx = pd.read_csv(PROCESSED / "nist_index.csv")
    idx = idx[idx.status == "ok"]
    groups = load_smarts(SMARTS)
    cache: dict = {}
    rows = []
    for k, r in enumerate(idx.itertuples(), 1):
        fid = f"{r.id}_{r.index}"
        path = RAW / "jdx" / f"{fid}.jdx"
        if not path.exists():
            continue
        text = path.read_text(encoding="latin-1", errors="ignore")
        head = text[:6000]
        npts = int(float(header(head, "NPOINTS") or 0))
        xunits = header(head, "XUNITS").upper()
        yunits = header(head, "YUNITS").upper()
        state = header(head, "STATE")
        firstx = float(header(head, "FIRSTX") or "nan")
        lastx = float(header(head, "LASTX") or "nan")
        if xunits == "MICROMETERS" and firstx > 0 and lastx > 0:
            x_lo, x_hi = sorted((1e4 / firstx, 1e4 / lastx))
        else:
            x_lo, x_hi = sorted((firstx, lastx))
        mol_path = RAW / "mol" / f"{r.id}.mol"
        smiles = mol_to_smiles(mol_path) if mol_path.exists() else ""
        struct = describe_structure(smiles, groups, cache)
        row = dict(
            file_id=fid, species_id=r.id, spectrum_index=r.index,
            file_path=str(path.relative_to(ROOT)).replace("\\", "/"),
            analysis_id=fid, sample_id=r.id,
            title=header(head, "TITLE"), cas=header(head, "CAS REGISTRY NO"),
            source=header(head, "$NIST SOURCE"), instrument=header(head, "SPECTROMETER/DATA SYSTEM")[:60],
            date=header(head, "DATE"), resolution=header(head, "RESOLUTION"),
            state_text=state, phase=r.phase, prep=prep_class(state) if r.phase == "condensed" else "",
            sampling=header(head, "SAMPLING PROCEDURE"),
            x_units=xunits, y_units=yunits, n_points=npts, x_min=x_lo, x_max=x_hi,
            smiles_raw=smiles,
        )
        row.update(struct)
        flags = dict(
            flag_no_xy_data=npts == 0,
            flag_bad_x_units=xunits not in ("1/CM", "MICROMETERS"),
            flag_bad_y_units=not (yunits.startswith("TRANSMITTANCE") or yunits.startswith("ABSORBANCE")),
            flag_not_condensed=r.phase != "condensed",
            flag_few_points=0 < npts < 500,
            flag_range_incomplete=not (x_lo <= 700 and x_hi >= 3800) if npts else True,
            flag_no_structure=not struct["smiles_valid"],
        )
        row.update(flags)
        row["qc_pass"] = not any(flags.values())
        rows.append(row)
        if k % 1000 == 0:
            print(f"  {k}/{len(idx)}")
    df = pd.DataFrame(rows)
    # one spectrum per species
    df["_xrank"] = (df.x_units != "1/CM").astype(int)
    df["_prank"] = df.prep.map(PREP_ORDER).fillna(9)
    df = df.sort_values(["species_id", "qc_pass", "_xrank", "_prank", "spectrum_index"],
                        ascending=[True, False, True, True, True])
    df["is_primary_export"] = False
    df.loc[df[df.qc_pass].groupby("species_id").head(1).index, "is_primary_export"] = True
    df = df.drop(columns=["_xrank", "_prank"]).sort_values("file_id")
    df.to_csv(PROCESSED / "inventory_nist.csv", index=False)

    p = df[df.is_primary_export]
    main_stratum = p[(~p.is_multifragment) & (~p.has_unusual_elements)]
    lines = ["# NIST WebBook condensed-phase inventory", "",
             f"Spectra downloaded (condensed or unknown phase): {len(df)}. "
             f"Pass every filter: {int(df.qc_pass.sum())}. One per species (primary): {len(p)}. "
             f"Main stratum (single fragment, no metals): {len(main_stratum)}, "
             f"{main_stratum.inchikey.nunique()} distinct InChIKeys.", "",
             "## Filters", "", "| flag | files flagged |", "| --- | --- |"]
    for c in [c for c in df.columns if c.startswith("flag_")]:
        lines.append(f"| `{c}` | {int(df[c].sum())} |")
    lines += ["", "## Preparation (primary spectra)", "", "| prep | spectra |", "| --- | --- |"]
    lines += [f"| {k} | {v} |" for k, v in p.prep.value_counts().items()]
    lines += ["", "## X units (primary)", "", "| units | spectra |", "| --- | --- |"]
    lines += [f"| {k} | {v} |" for k, v in p.x_units.value_counts().items()]
    lines += ["", "## Instrument (primary, top 12)", "", "| instrument | spectra |", "| --- | --- |"]
    lines += [f"| {k} | {v} |" for k, v in p.instrument.value_counts().head(12).items()]
    lines += ["", "## Functional group coverage (main stratum)", "", "| group | spectra | share |", "| --- | --- | --- |"]
    for name, _, _ in groups:
        n = int(main_stratum[f"fg_{name}"].sum())
        lines.append(f"| {name} | {n} | {100 * n / max(len(main_stratum), 1):.1f}% |")
    (DOCS / "inventory_nist.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[nist_inventory] {len(df)} spectra, {int(df.qc_pass.sum())} pass QC, {len(p)} primary, "
          f"{len(main_stratum)} in main stratum")
    return 0


if __name__ == "__main__":
    sys.exit(main())
