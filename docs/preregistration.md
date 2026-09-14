# Preregistered analysis plan

Title (working): How diagnostic are classical infrared correlation rules?
A large-scale evaluation using experimental spectra.

Date of freeze: 2026-09-14. Git tag to be applied on the commit that adds
this file and `rules/rules_frozen.csv`: `rules-frozen-v1`.

## Question

For each classical IR correlation rule (a wavenumber window, with the
intensity and shape qualifiers the source states), how much does observing
the band change the odds that the molecule carries the functional group the
rule is about, and how much does not observing it lower those odds? The
quantities of interest are LR+ and LR- per rule, with intervals, on
experimental spectra of compounds with known structure.

## Hypotheses (stated before the confirmatory run)

H1. Rules in the carbonyl region (1600 to 1900 cm-1) and the triple-bond
region (2100 to 2300 cm-1) will have LR+ above 5 when scored with their
intensity clause; rules in the fingerprint region below 1300 cm-1 scored by
position alone will have LR+ below 2 and specificity below 0.3, because
nearly every spectrum has a band in those windows.

H2. Adding the intensity clause will raise LR+ for strong-band groups
(esters, ketones, acids, nitro) and lower sensitivity for groups whose band
is weak relative to the strongest band in ATR spectra of large molecules
(nitriles, C-H stretches, O-H and N-H stretches).

H3. The composite benzene-substitution rules (C-H wag window plus presence
or absence of the 690 ring bend) will outperform either half alone, but
none of the four patterns will reach LR+ above 3 on a dataset that is 93
percent aromatic.

H4. The groups enriched among false positives will be chemically
interpretable in most cases (an ester in a ketone window, a ketone in an
amide window), not random.

## Data

Chemotion IR (RADAR4Chem, DOI 10.22000/OGoEQGlsZGElrgst, CC BY-SA 4.0).
2113 spectra pass QC; main stratum 1923; salt stratum 137. Ground truth is
the depositor's structure matched by SMARTS (`rules/functional_groups_smarts.csv`).
Confirmatory set: the 80 percent of InChIKeys not in the development split
(`data/processed/spectra_meta.csv`, column `split`).

## Rules

`rules/rules_frozen.csv`, 106 rows, 101 evaluable, all `frozen = yes`.
Sources: Brian C. Smith, Spectroscopy, "IR Spectral Interpretation
Workshop" (13 articles, listed in `docs/rules_draft_notes.md`), transcribed
as published. No window is adjusted after the freeze.

## Processing (fixed)

`scripts/preprocess.py`: A = -log10(T), T clipped at 1e-4; 2 cm-1 grid,
400 to 4000; asymmetric least squares baseline, lam 1e6, p 0.001, 10
iterations; normalisation to the strongest point in 650 to 3800.
`scripts/bands.py`: local maxima with prominence >= 0.01 (candidates);
height relative to the strongest band; FWHM at half prominence.

## Analysis (fixed)

`scripts/evaluate_rules.py --split confirm`. Primary threshold 0.02;
sweep 0.01, 0.02, 0.05, 0.10. Three nested definitions of "band present".
Composite rules use `requires` and `forbids` windows at the same threshold.
Metrics and intervals as in `docs/decisions_freeze.md`, D10. Rules with
fewer than 10 positives are reported as underpowered. Cluster bootstrap on
Murcko scaffold families, 500 resamples, seed 20260914.

## Reporting

Every evaluable rule is reported, whatever its result. The paper's main
table is the full-definition result at the primary threshold; the sweep and
the position-only and intensity-only columns go in the supplement. The
development-split numbers are not reported as results.

## Replication

NIST WebBook condensed-phase spectra (transmission), same frozen table,
same scripts, reported as an independent replication with the ATR versus
transmission difference as a pre-specified secondary analysis.

## Deviations

Any deviation from this plan will be listed in `docs/deviations.md` with
its date and reason.
