"""
bands.py: detect bands in the preprocessed spectra and describe each one by
position, relative intensity and width.

Input:  data/processed/spectra.npz, spectra_meta.csv (from preprocess.py)
Output: data/processed/bands.csv, one row per detected band:
            file_id, position_cm, height_rel, prominence_rel, fwhm_cm,
            left_cm, right_cm, intensity_class, shape_class

Definitions (these are the operational choices the paper has to state):
  * A band is a local maximum of the baseline corrected, max-normalised
    absorbance (scipy.signal.find_peaks) with prominence at least
    PROMINENCE_FLOOR. The floor is deliberately low (0.01 of the strongest
    band) so that the table keeps every candidate; the evaluation script
    applies the actual prominence threshold, and sweeps it.
  * height_rel is the band height relative to the strongest band of the
    spectrum in the evaluation window (650 to 3800 cm-1), so 1.0 is the
    strongest band.
  * intensity_class follows the usual three levels, relative to the
    strongest band:  strong >= 0.60,  medium >= 0.20,  weak otherwise.
    These cut points are also swept by the evaluation script.
  * fwhm_cm is the full width at half prominence (scipy peak_widths at
    rel_height 0.5), in cm-1. shape_class: sharp < 30, broad 30 to 100,
    very_broad > 100.
  * Bands whose apex lies outside 650 to 3800 cm-1 are dropped: below 650
    many Chemotion spectra end and ATR diamond absorbs; above 3800 there is
    nothing diagnostic and the noise grows.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.signal import find_peaks, peak_widths

ROOT = Path(__file__).resolve().parent.parent
PROCESSED = ROOT / "data" / "processed"

EVAL_MIN, EVAL_MAX = 650.0, 3800.0
PROMINENCE_FLOOR = 0.01
STRONG_MIN, MEDIUM_MIN = 0.60, 0.20
SHARP_MAX, BROAD_MAX = 30.0, 100.0


def classify_intensity(h: float) -> str:
    if h >= STRONG_MIN:
        return "strong"
    if h >= MEDIUM_MIN:
        return "medium"
    return "weak"


def classify_shape(w: float) -> str:
    if w < SHARP_MAX:
        return "sharp"
    if w <= BROAD_MAX:
        return "broad"
    return "very_broad"


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", choices=["chemotion", "nist"], default="chemotion")
    args = ap.parse_args()
    suf = "" if args.dataset == "chemotion" else f"_{args.dataset}"
    z = np.load(PROCESSED / f"spectra{suf}.npz", allow_pickle=True)
    grid, spectra, ids = z["grid"], z["absorbance"], z["ids"]
    step = float(grid[1] - grid[0])
    rows = []
    for i in range(spectra.shape[0]):
        y = spectra[i]
        ok = ~np.isnan(y)
        yy = np.where(ok, y, 0.0)
        peaks, props = find_peaks(yy, prominence=PROMINENCE_FLOOR)
        if len(peaks) == 0:
            continue
        widths, _, left_ips, right_ips = peak_widths(yy, peaks, rel_height=0.5)
        for k, p in enumerate(peaks):
            pos = float(grid[p])
            if pos < EVAL_MIN or pos > EVAL_MAX:
                continue
            h = float(yy[p])
            w = float(widths[k] * step)
            rows.append(dict(
                file_id=ids[i], position_cm=round(pos, 1), height_rel=round(h, 4),
                prominence_rel=round(float(props["prominences"][k]), 4),
                fwhm_cm=round(w, 1),
                left_cm=round(float(np.interp(left_ips[k], np.arange(len(grid)), grid)), 1),
                right_cm=round(float(np.interp(right_ips[k], np.arange(len(grid)), grid)), 1),
                intensity_class=classify_intensity(h), shape_class=classify_shape(w),
            ))
    bands = pd.DataFrame(rows)
    bands.to_csv(PROCESSED / f"bands{suf}.csv", index=False)
    per = bands.groupby("file_id").size()
    print(f"[bands] {len(bands)} candidate bands in {per.size} spectra; "
          f"median {per.median():.0f} per spectrum at prominence >= {PROMINENCE_FLOOR}")
    for thr in (0.02, 0.05, 0.10):
        sub = bands[bands.prominence_rel >= thr].groupby("file_id").size()
        print(f"  prominence >= {thr:.2f}: median {sub.median():.0f} bands per spectrum")
    print(bands.intensity_class.value_counts().to_string())
    print(bands.shape_class.value_counts().to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
