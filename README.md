# How diagnostic are classical infrared correlation rules?

A large-scale evaluation using experimental spectra.

## Objective

Classical infrared correlation tables (Pretsch, Silverstein, Socrates and the
teaching material derived from them) are the everyday tool for reading an IR
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
themselves are transcribed by hand from the printed correlation tables, with
book, edition, table and page recorded, and are frozen before any evaluation is
run, so that the measurement cannot be tuned to the data.

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
| `docs/`                          | Generated reports and download instructions.                   |
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

The independent replication will use **condensed-phase** spectra from the
**NIST Chemistry WebBook**, DOI:
[10.18434/T4D303](https://doi.org/10.18434/T4D303).

These spectra are **not redistributed** by this project. Only the following are
published here: the identifiers of the spectra used, the scripts that download
them, and the derived results (per-rule contingency tables and summary
statistics). Anyone wishing to reproduce the replication must obtain the spectra
from NIST directly, under the terms NIST sets.

### Code

All code in this repository is released under the **MIT License** (see
`LICENSE`), copyright Mol Insight.

### Competing interests

The authors declare a competing interest: they are the authors of a commercial
spectral interpretation software product. The rule set evaluated here is frozen
and documented before evaluation, the ground-truth SMARTS definitions are
published in `rules/`, and the analysis code and derived tables are released in
full, so that every number reported can be recomputed independently.
