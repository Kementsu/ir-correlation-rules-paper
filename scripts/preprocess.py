"""
preprocess.py: turn the Chemotion JCAMP files into absorbance spectra on a
common grid, with a baseline estimate, ready for band detection.

Input:  data/processed/inventory.csv (from inventory.py)
Output: data/processed/spectra.npz
            grid        (G,)      wavenumber axis, cm-1, ascending
            absorbance  (N, G)    baseline corrected absorbance, max 1 in the
                                  evaluation window
            raw_abs     (N, G)    absorbance before baseline correction
            baseline    (N, G)    the estimated baseline that was subtracted
            ids         (N,)      file_id, aligned with inventory.csv
        data/processed/spectra_meta.csv   one row per spectrum with the
                                  sampling procedure and the split assignment

Steps, in order, all deterministic:
  1. keep one row per analysis (is_primary_export) that passes every QC flag
  2. read the JCAMP file; the X axis is rebuilt by the jcamp library from
     FIRSTX, LASTX and NPOINTS (see docs/inventory.md, section 9)
  3. transmittance to absorbance: A = -log10(T). T is stored as a fraction
     in this collection (0 to 1); values in percent are divided by 100 first.
     T is clipped to [1e-4, 1] before the log so a noisy 0 does not become
     infinity. Files already in absorbance are taken as they are.
  4. resample onto a 2 cm-1 grid from 400 to 4000 by linear interpolation;
     outside the measured range the spectrum is NaN
  5. baseline: asymmetric least squares (Eilers and Boelens 2005), which
     follows the underside of the spectrum without cutting into bands.
     Parameters lam and p are fixed here and reported in the paper.
  6. normalise so that the strongest point in the evaluation window
     (650 to 3800 cm-1) equals 1

Nothing here decides whether a band is "present"; that is bands.py.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import sparse
from scipy.sparse.linalg import spsolve

ROOT = Path(__file__).resolve().parent.parent
PROCESSED = ROOT / "data" / "processed"

GRID_MIN, GRID_MAX, GRID_STEP = 400.0, 4000.0, 2.0
EVAL_MIN, EVAL_MAX = 650.0, 3800.0
ALS_LAM = 1e6
ALS_P = 0.001
ALS_ITER = 10
T_FLOOR = 1e-4
DEV_FRACTION = 0.20
SPLIT_SEED = 20260914


def read_xy(path: str) -> tuple[np.ndarray, np.ndarray, str, str, str]:
    import jcamp

    with contextlib.redirect_stdout(io.StringIO()):
        rec = jcamp.readfile(path)
    if len(np.asarray(rec.get("y", []))) == 0 and rec.get("children"):
        # LINK file: the spectrum is the child block of data class XYDATA;
        # the other children are the depositor's peak assignment tables
        for child in rec["children"]:
            is_spectrum = str(child.get("data type", "")).upper() == "INFRARED SPECTRUM"
            if is_spectrum and len(child.get("y", [])) > 0:
                rec = child
                break
    x = np.asarray(rec["x"], dtype=float)
    y = np.asarray(rec["y"], dtype=float)
    yunits = str(rec.get("yunits", "")).strip().upper()
    xunits = str(rec.get("xunits", "")).strip().upper()
    sampling = str(rec.get("sampling procedure", "")).strip()
    return x, y, yunits, sampling, xunits


def to_absorbance(y: np.ndarray, yunits: str) -> np.ndarray:
    if yunits.startswith("ABSORBANCE"):
        return y
    t = y.copy()
    if np.nanmax(t) > 1.5:  # percent transmittance
        t = t / 100.0
    t = np.clip(t, T_FLOOR, 1.0)
    return -np.log10(t)


def als_baseline(y: np.ndarray, lam: float = ALS_LAM, p: float = ALS_P,
                 niter: int = ALS_ITER) -> np.ndarray:
    """Asymmetric least squares baseline (Eilers and Boelens 2005)."""
    n = len(y)
    d = sparse.diags([1.0, -2.0, 1.0], [0, -1, -2], shape=(n, n - 2))
    dtd = lam * d.dot(d.transpose())
    w = np.ones(n)
    z = y
    for _ in range(niter):
        wmat = sparse.spdiags(w, 0, n, n)
        z = spsolve((wmat + dtd).tocsc(), w * y)
        w = p * (y > z) + (1 - p) * (y < z)
    return np.asarray(z)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--dataset", choices=["chemotion", "nist"], default="chemotion",
                    help="chemotion: inventory.csv, dev/confirm split; nist: inventory_nist.csv, all 'confirm'")
    args = ap.parse_args()
    suf = "" if args.dataset == "chemotion" else f"_{args.dataset}"

    inv = pd.read_csv(PROCESSED / f"inventory{suf}.csv", low_memory=False)
    keep = inv[(inv.is_primary_export == True) & (inv.qc_pass == True)].copy()  # noqa: E712
    if args.limit:
        keep = keep.head(args.limit)
    keep = keep.reset_index(drop=True)
    print(f"[preprocess] {len(keep)} spectra to process")

    grid = np.arange(GRID_MIN, GRID_MAX + GRID_STEP, GRID_STEP)
    g = len(grid)
    raw = np.full((len(keep), g), np.nan)
    base = np.full((len(keep), g), np.nan)
    corr = np.full((len(keep), g), np.nan)
    sampling = []
    win = (grid >= EVAL_MIN) & (grid <= EVAL_MAX)

    for i, row in keep.iterrows():
        path = str(ROOT / row.file_path)
        x, y, yunits, samp, xunits = read_xy(path)
        sampling.append(samp)
        if xunits.startswith("MICROMETER"):
            x = 1e4 / x
        order = np.argsort(x)
        x, y = x[order], y[order]
        a = to_absorbance(y, yunits)
        inside = (grid >= x.min()) & (grid <= x.max())
        ai = np.interp(grid[inside], x, a)
        raw[i, inside] = ai
        b = als_baseline(ai)
        base[i, inside] = b
        c = ai - b
        c[c < 0] = 0.0
        peak = np.nanmax(c[win[inside]]) if np.any(win[inside]) else np.nanmax(c)
        corr[i, inside] = c / peak if peak > 0 else c
        if (i + 1) % 200 == 0:
            print(f"  {i + 1}/{len(keep)}")

    # development / confirmatory split, by structure so that duplicates of one
    # compound never straddle the two sets
    rng = np.random.default_rng(SPLIT_SEED)
    keys = keep.inchikey.fillna(keep.file_id).unique()
    rng.shuffle(keys)
    n_dev = int(round(DEV_FRACTION * len(keys)))
    dev_keys = set(keys[:n_dev])
    split = np.where(keep.inchikey.fillna(keep.file_id).isin(dev_keys), "dev", "confirm")
    if args.dataset != "chemotion":
        split = np.full(len(keep), "confirm")  # replication set: no development split, rules already frozen

    np.savez_compressed(PROCESSED / f"spectra{suf}.npz", grid=grid, absorbance=corr,
                        raw_abs=raw, baseline=base, ids=keep.file_id.values)
    meta = keep[["file_id", "analysis_id", "sample_id", "inchikey", "smiles_canonical",
                 "instrument", "x_min", "x_max", "n_points", "resolution",
                 "is_multifragment", "has_unusual_elements"]].copy()
    meta["sampling_procedure"] = sampling
    meta["split"] = split
    meta["x_min_cm"] = [float(np.nanmin(grid[~np.isnan(corr[i])])) for i in range(len(keep))]
    meta["x_max_cm"] = [float(np.nanmax(grid[~np.isnan(corr[i])])) for i in range(len(keep))]
    meta.to_csv(PROCESSED / f"spectra_meta{suf}.csv", index=False)
    print(f"[preprocess] wrote spectra{suf}.npz ({corr.shape}) and spectra_meta.csv")
    print(f"[preprocess] split: dev {int((split == 'dev').sum())}, confirm {int((split == 'confirm').sum())}")
    print("[preprocess] sampling procedure values:")
    print(pd.Series(sampling).replace("", "(missing)").value_counts().head(15).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
