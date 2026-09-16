# Classical infrared correlation rules as diagnostic tests

Likelihood ratios for 101 published IR correlation rules, measured on 6,663
experimental spectra with known structures (Chemotion, ATR; NIST WebBook,
transmission). Code, frozen rule set, ground-truth definitions, result tables
and manuscript sources.

## Objective

Classical infrared correlation tables are the everyday tool for reading an IR
spectrum: a carbonyl stretch near 1700 cm-1, a broad O-H band above 3200 cm-1,
a nitrile around 2250 cm-1. These rules are stated as qualitative heuristics and
are almost never accompanied by the numbers a diagnostic test is normally judged
by.

This project measures them. For each classical rule we compute, over a large set
of experimental spectra whose structures are known:

- sensitivity (fraction of molecules carrying the group whose spectrum shows the band),
- specificity (fraction of molecules without the group whose spectrum does not show it),
- positive and negative likelihood ratios (LR+ and LR-),
- and the associated confidence intervals.

The ground truth for "molecule carries the group" comes from substructure
matching (SMARTS) on the published structure of each sample. The rules
themselves are transcribed by hand from one published source (Brian C. Smith's
"IR Spectral Interpretation Workshop" column in *Spectroscopy*), with article,
table and page recorded, and are frozen before any evaluation is run, so that
the measurement cannot be tuned to the data.

The intended output is a single, citable answer to a question practising
chemists ask constantly and that the literature answers only by tradition: which
of these rules actually carry diagnostic weight, and how much.

### Repository layout

| Path                             | Contents                                                      |
| -------------------------------- | ------------------------------------------------------------- |
| `data/raw/`                      | Downloaded archives and unpacked spectra. Not tracked by git.  |
| `data/processed/`                | Derived tables produced by the scripts. Tracked.               |
| `scripts/`                       | Processing and analysis code.                                  |
| `rules/`                         | SMARTS ground-truth definitions and the frozen rule table.     |
| `docs/`                          | Generated reports, decisions and download instructions.        |
| `paper/`                         | Manuscript (LaTeX), figures and generated tables.              |
| `tools/`                         | Reference checkouts of third-party code. Not tracked by git.   |

### Getting started

```sh
python -m venv .venv
.venv/Scripts/activate        # Windows
pip install -r requirements.txt
python scripts/inventory.py
```

`scripts/inventory.py` reads the Chemotion IR archive under `data/raw/` and
writes `data/processed/inventory.csv` plus the human-readable summary
`docs/inventory.md`. See `docs/DOWNLOAD.md` for how to obtain the archive.

The full pipeline, in order:

```sh
python scripts/inventory.py                 # QC and ground truth per spectrum
python scripts/preprocess.py                # absorbance, baseline, grid, dev/confirm split
python scripts/bands.py                     # band detection (position, intensity, width)
python scripts/evaluate_rules.py --split dev     # pipeline check on the development split
python scripts/evaluate_rules.py --split confirm # confirmatory run, ONLY after the rules are frozen

python scripts/nist_download.py enumerate|spectra|structures|pack   # NIST replication set
python scripts/nist_inventory.py
python scripts/preprocess.py --dataset nist
python scripts/bands.py --dataset nist
python scripts/evaluate_rules.py --dataset nist --split confirm

python scripts/figures.py                  # manuscript figures
python scripts/tables.py                   # manuscript tables
```

`docs/pipeline_notes.md` records the fixed processing choices, the
development/confirmatory split and what the pipeline check showed.
`data/processed/spectra.npz` (84 MB) is not tracked; rebuild it with
`preprocess.py`.

## Reproducing the paper

Every number in the manuscript comes from a file in `data/processed/` that a
script in `scripts/` writes; nothing is typed by hand. The result tables are
tracked in git, so the figures and tables of the paper can be rebuilt without
the raw spectra:

```sh
python scripts/figures.py     # paper/figures/*.pdf and figure_numbers.md
python scripts/tables.py      # paper/tables/*.tex
cd paper && latexmk -pdf main.tex
```

To recompute the result tables themselves, obtain the spectra as described in
`docs/DOWNLOAD.md` and run the pipeline above. On a laptop the Chemotion run
takes minutes; the NIST download is rate-limited to one request per second and
takes several hours.

The analysis follows the plan in `docs/preregistration.md`. The rule table and
every processing choice were frozen at tag `rules-frozen-v1` before the
confirmatory data were examined; `docs/decisions_freeze.md` records each
choice and the alternative rejected. `data/processed/rule_metrics_dev.csv`
is the development-split run used to check the pipeline; it is kept for
transparency and is not reported in the paper.

## Provenance

The rule transcription and the ground-truth definitions grew out of the
author's earlier work encoding correlation tables for automated
interpretation, where the contradictions that motivated this study first
appeared. Everything in this repository was rebuilt from the published sources
for the paper, with the article, table and page of every rule recorded in
`rules/rules_frozen.csv`.

## Citing

See `CITATION.cff`. Until the article is published, cite the repository at tag
`rules-frozen-v1`.

## Data and licensing

### Primary dataset

The primary dataset is **"Chemotion Repository - Data collection: FT-IR
spectroscopy data (Chemotion IR)"**, published through **RADAR4Chem**:

- DOI: [10.22000/OGoEQGlsZGElrgst](https://doi.org/10.22000/OGoEQGlsZGElrgst)
- License: **CC BY-SA 4.0**
- Published alongside: Punjabi et al., *Journal of Cheminformatics* (2025) **17**:24,
  DOI: [10.1186/s13321-025-00960-2](https://doi.org/10.1186/s13321-025-00960-2)

The archive contains JCAMP-DX spectra exported from the Chemotion Repository
together with a `meta_data.json` file that carries the sample identifiers,
SMILES and instrument information. It is downloaded into `data/raw/`, which is
excluded from version control; `docs/DOWNLOAD.md` documents how to reproduce the
download.

Because the dataset is CC BY-SA 4.0, any redistribution of the spectra
themselves, or of derivative works that incorporate them, must carry the same
license and attribute the original authors. The code in this repository is
licensed separately (see below) and derived tables published here contain
aggregate statistics and identifiers rather than redistributed spectra.

### Independent replication set

The independent replication uses **condensed-phase** spectra from the
**NIST Chemistry WebBook**, DOI:
[10.18434/T4D303](https://doi.org/10.18434/T4D303).

These spectra are **not redistributed** by this project. Only the following are
published here: the identifiers of the spectra used, the scripts that download
them, and the derived results (per-rule contingency tables and summary
statistics). Anyone wishing to reproduce the replication must obtain the spectra
from NIST directly, under the terms NIST sets.

### Code

All code in this repository is released under the **MIT License** (see
`LICENSE`), copyright Kementsu Ibarguen Calvo.

### Competing interests

The author declares a competing interest: he is the founder of a company that
develops spectral interpretation software. The rule set evaluated here is frozen
and documented before evaluation, the ground-truth SMARTS definitions are
published in `rules/`, and the analysis code and derived tables are released in
full, so that every number reported can be recomputed independently.
