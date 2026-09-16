"""
nist_download.py: polite, resumable download of the NIST Chemistry WebBook
infrared spectra (condensed phase) for the replication set.

    python scripts/nist_download.py enumerate --limit 5   # smoke test, 5 queries
    python scripts/nist_download.py enumerate     # ~1.5 h : which species have IR data
    python scripts/nist_download.py spectra       # ~3-4 h : every IR spectrum of those species
    python scripts/nist_download.py structures    # ~40 min: 2D MOL file of species with a condensed spectrum
    python scripts/nist_download.py pack          # seconds: one tar.gz with the condensed-phase files

Everything lands in data/raw/nist/, which is not tracked by git: NIST
WebBook data (SRD 69, DOI 10.18434/T4D303) may be used for scientific work
but not redistributed. What the repository will publish is the list of
species and spectrum indices used (data/processed/nist_index.csv, written by
the "spectra" phase) plus this script, which is enough to rebuild the set.

Politeness: one request per second, identifying User-Agent, resumable at
every phase (re-running skips what is already on disk), and a hard stop on
repeated HTTP errors so a blocked client never hammers the server.

How the set is built:
  enumerate  The WebBook formula search accepts "C7H?" with the option
             "allow other elements" and the flag "has IR spectrum" (cIR=on),
             and returns at most 400 species per query. We iterate carbon
             count 1..60 and hydrogen count 1..120 (and H absent), record
             every species ID, and log any query that hit the 400 cap so it
             can be split further by hand.
  spectra    For each species, JCAMP files are requested for Index 0, 1, 2,
             ... until the server answers with an HTML page instead of a
             JCAMP file. The phase (gas / condensed) is read from the
             ##STATE and ##SAMPLING PROCEDURE lines inside each file, which
             is more reliable than parsing the web page.
  structures For species with at least one condensed-phase spectrum, the
             WebBook's own 2D MOL file (Str2File) is downloaded. Using the
             WebBook structure avoids a second identifier resolution step.
  pack       Copies the condensed-phase JCAMP files and the MOL files into
             data/raw/nist/nist_condensed.tar.gz for transfer.
"""
from __future__ import annotations

import csv
import re
import sys
import tarfile
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "nist"
JDX = RAW / "jdx"
MOL = RAW / "mol"
PROCESSED = ROOT / "data" / "processed"
for p in (RAW, JDX, MOL, PROCESSED):
    p.mkdir(parents=True, exist_ok=True)

BASE = "https://webbook.nist.gov/cgi/cbook.cgi"
UA = "ir-correlation-rules-paper/1.0 (scientific use; contact: kementsuibarguen@gmail.com)"
RATE = 1.0            # seconds between requests
TIMEOUT = 30
MAX_ERRORS = 20       # consecutive HTTP/network errors before the script stops itself
C_MAX, H_MAX = 60, 120
CAP_TEXT = "only the first 400"

SPECIES_FILE = RAW / "species.csv"          # id, formula_query, name
INDEX_FILE = PROCESSED / "nist_index.csv"   # id, index, status, phase, state_text, bytes
STRUCT_FILE = RAW / "structures.csv"        # id, status, bytes

CONDENSED_WORDS = ("SOLID", "LIQUID", "SOLUTION", "MULL", "NUJOL", "KBR", "FILM", "NEAT",
                   "CCL4", "CHCL3", "CS2", "MELT", "PELLET", "ATR", "CAPILLARY", "SMEAR")


class Client:
    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({"User-Agent": UA})
        self.errors = 0
        self.last = 0.0

    def get(self, params: dict) -> requests.Response | None:
        wait = RATE - (time.time() - self.last)
        if wait > 0:
            time.sleep(wait)
        self.last = time.time()
        try:
            r = self.s.get(BASE, params=params, timeout=TIMEOUT)
        except requests.RequestException as e:
            self.errors += 1
            print(f"  network error ({self.errors}/{MAX_ERRORS}): {e}")
            if self.errors >= MAX_ERRORS:
                sys.exit("too many consecutive errors, stopping (re-run to resume)")
            time.sleep(5)
            return None
        if r.status_code >= 500 or r.status_code == 429:
            self.errors += 1
            print(f"  HTTP {r.status_code} ({self.errors}/{MAX_ERRORS})")
            if self.errors >= MAX_ERRORS:
                sys.exit("too many consecutive errors, stopping (re-run to resume)")
            time.sleep(10)
            return None
        self.errors = 0
        return r


def append_row(path: Path, header: list[str], row: dict) -> None:
    new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header, lineterminator="\n")
        if new:
            w.writeheader()
        w.writerow(row)


def read_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ---------------------------------------------------------------- enumerate
def enumerate_species(c: Client, limit: int | None = None) -> None:
    done_queries = {r["formula_query"] for r in read_rows(RAW / "queries.csv")}
    seen = {r["id"] for r in read_rows(SPECIES_FILE)}
    queries = []
    for nc in range(1, C_MAX + 1):
        queries.append(f"C{nc}")  # no hydrogen at all (rare, but exists)
        for nh in range(1, H_MAX + 1):
            queries.append(f"C{nc}H{nh}")
    todo = [q for q in queries if q not in done_queries][:limit]
    print(f"[enumerate] {len(todo)} formula queries to run ({len(done_queries)} done, {len(seen)} species so far)")
    for i, q in enumerate(todo, 1):
        r = c.get({"Formula": q, "AllowOther": "on", "NoIon": "on", "Units": "SI", "cIR": "on"})
        if r is None:
            continue
        html = r.text
        ids = []
        for m in re.finditer(r'cbook\.cgi\?ID=(C\d+)[^"]*"[^>]*>([^<]*)<', html):
            sid, name = m.group(1), m.group(2).strip()
            if sid not in seen:
                seen.add(sid)
                append_row(SPECIES_FILE, ["id", "formula_query", "name"], dict(id=sid, formula_query=q, name=name))
            ids.append(sid)
        # a single-species result redirects straight to the species page
        if not ids:
            m = re.search(r'name="ID" value="(C\d+)"', html) or re.search(r'cbook\.cgi\?ID=(C\d+)', html)
            if m and "IR Spectrum" in html and m.group(1) not in seen:
                seen.add(m.group(1))
                append_row(SPECIES_FILE, ["id", "formula_query", "name"], dict(id=m.group(1), formula_query=q, name=""))
                ids.append(m.group(1))
        capped = CAP_TEXT in html
        append_row(RAW / "queries.csv", ["formula_query", "n_ids", "capped"],
                   dict(formula_query=q, n_ids=len(ids), capped=capped))
        if capped:
            print(f"  ! {q}: hit the 400 cap, split this query by hand (add O/N counts)")
        if i % 50 == 0:
            print(f"  {i}/{len(todo)} queries, {len(seen)} species")
    print(f"[enumerate] done: {len(seen)} species with IR data")


# ---------------------------------------------------------------- spectra
def phase_of(text: str) -> tuple[str, str]:
    m = re.search(r"##STATE\s*=\s*(.+)", text, re.I) or re.search(r"##SAMPLING PROCEDURE\s*=\s*(.+)", text, re.I)
    state = m.group(1).strip() if m else ""
    up = state.upper()
    if "GAS" in up or "VAPOR" in up or "VAPOUR" in up:
        return "gas", state
    if any(w in up for w in CONDENSED_WORDS):
        return "condensed", state
    return "unknown", state


def download_spectra(c: Client, limit: int | None = None) -> None:
    species = read_rows(SPECIES_FILE)
    done = {(r["id"], r["index"]) for r in read_rows(INDEX_FILE)}
    finished_ids = {r["id"] for r in read_rows(INDEX_FILE) if r["status"] == "end"}
    todo = [s for s in species if s["id"] not in finished_ids][:limit]
    print(f"[spectra] {len(todo)} species to fetch ({len(finished_ids)} finished)")
    for n, s in enumerate(todo, 1):
        sid = s["id"]
        idx = 0
        while True:
            key = (sid, str(idx))
            if key in done:
                idx += 1
                continue
            r = c.get({"JCAMP": sid, "Type": "IR", "Index": idx})
            if r is None:
                break  # retry on the next run
            body = r.content
            is_jcamp = body[:20].lstrip().startswith(b"##")
            if r.status_code == 200 and is_jcamp:
                text = body.decode("latin-1", errors="ignore")
                phase, state = phase_of(text[:6000])
                (JDX / f"{sid}_{idx}.jdx").write_bytes(body)
                append_row(INDEX_FILE, ["id", "index", "status", "phase", "state_text", "bytes"],
                           dict(id=sid, index=idx, status="ok", phase=phase, state_text=state, bytes=len(body)))
                idx += 1
            else:
                append_row(INDEX_FILE, ["id", "index", "status", "phase", "state_text", "bytes"],
                           dict(id=sid, index=idx, status="end", phase="", state_text="", bytes=0))
                break
        if n % 100 == 0:
            rows = read_rows(INDEX_FILE)
            print(f"  {n}/{len(todo)} species; spectra so far: "
                  f"{sum(r['phase'] == 'condensed' for r in rows)} condensed, "
                  f"{sum(r['phase'] == 'gas' for r in rows)} gas, "
                  f"{sum(r['phase'] == 'unknown' for r in rows)} unknown")
    print("[spectra] done")


# ---------------------------------------------------------------- structures
def download_structures(c: Client) -> None:
    rows = read_rows(INDEX_FILE)
    want = sorted({r["id"] for r in rows if r["phase"] in ("condensed", "unknown")})
    done = {r["id"] for r in read_rows(STRUCT_FILE)}
    todo = [i for i in want if i not in done]
    print(f"[structures] {len(todo)} MOL files to fetch ({len(done)} done)")
    for n, sid in enumerate(todo, 1):
        r = c.get({"Str2File": sid})
        if r is None:
            continue
        body = r.content
        ok = r.status_code == 200 and b"M  END" in body
        if ok:
            (MOL / f"{sid}.mol").write_bytes(body)
        append_row(STRUCT_FILE, ["id", "status", "bytes"], dict(id=sid, status="ok" if ok else "missing", bytes=len(body) if ok else 0))
        if n % 100 == 0:
            print(f"  {n}/{len(todo)}")
    print("[structures] done")


# ---------------------------------------------------------------- pack
def pack() -> None:
    rows = read_rows(INDEX_FILE)
    keep = [r for r in rows if r["phase"] in ("condensed", "unknown")]
    out = RAW / "nist_condensed.tar.gz"
    with tarfile.open(out, "w:gz") as tar:
        for r in keep:
            p = JDX / f"{r['id']}_{r['index']}.jdx"
            if p.exists():
                tar.add(p, arcname=f"jdx/{p.name}")
        for p in MOL.glob("*.mol"):
            tar.add(p, arcname=f"mol/{p.name}")
        tar.add(INDEX_FILE, arcname="nist_index.csv")
        tar.add(SPECIES_FILE, arcname="species.csv")
    print(f"[pack] {len(keep)} condensed/unknown spectra + {len(list(MOL.glob('*.mol')))} MOL files -> {out} "
          f"({out.stat().st_size / 1e6:.1f} MB)")


def main() -> int:
    phase = sys.argv[1] if len(sys.argv) > 1 else ""
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    c = Client()
    if phase == "enumerate":
        enumerate_species(c, limit)
    elif phase == "spectra":
        download_spectra(c, limit)
    elif phase == "structures":
        download_structures(c)
    elif phase == "pack":
        pack()
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
