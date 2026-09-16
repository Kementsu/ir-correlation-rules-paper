# NIST replication: plan and selection rules (2026-09-15)

Written after the download finished and before `evaluate_rules.py` was run
on the NIST set. The rule table is the frozen one (`rules-frozen-v1`); no
rule, threshold, definition or statistic changed. The only additions are
the selection and handling rules below, which the Chemotion set did not
need.

## Source

NIST Chemistry WebBook, SRD 69 (DOI 10.18434/T4D303), IR spectra of every
species the formula search reports as having IR data: 14,391 species,
18,030 spectra (9,498 gas, 7,297 condensed by ##STATE, 1,235 without a
usable state, of which 809 are image-only records with no data points).
Download script and identifier list: `scripts/nist_download.py`,
`data/processed/nist_index.csv`. Raw files are not redistributed.

## Inclusion (per spectrum)

Data points present; X units 1/CM or MICROMETERS (converted as 10000/x);
Y units transmittance or absorbance (reflectance and "dispersion index"
records excluded); ##STATE condensed; at least 500 points; measured range
covering 700 to 3800 cm-1 after conversion; a structure parsable from the
WebBook 2D MOL file. Result: 5,894 spectra pass.

## One spectrum per species

NIST often holds several condensed spectra of one compound (KBr disc and
mull, or two Coblentz batches). One is kept per species, chosen by, in
order: X already in 1/CM (avoids the resampling of digitised micrometre
scans), preparation kbr > liquid/film > solution > mull > other (mulls
carry hydrocarbon bands of the oil; solutions have solvent gaps), lowest
spectrum index. Result: 5,522 primary spectra; main stratum (single
fragment, no metals) 5,124; salt stratum 314.

## Window coverage

Many prism-era spectra start at 650 to 700 cm-1. Instead of dropping them,
each rule is scored only on the spectra whose measured range covers every
window the rule uses (its own window, and the requires / forbids windows of
composite rules). The evaluator now does this for both datasets; on
Chemotion it changes nothing because every spectrum covers 374 to 3997.

## Preparation strata

`inventory_nist.csv` carries `prep` (kbr, mull, solution, liquid, other) so
that a secondary analysis can split rules by preparation; the primary
analysis pools them, as the rule sources do.

## What is compared

For every rule powered in both sets (at least 10 positives in each), LR+
at the primary threshold with the full definition, Chemotion (ATR,
synthesis laboratory, 2016 to 2024) against NIST (transmission, Coblentz
and NIST collections, mostly before 1990). Agreement is summarised by the
Spearman correlation of LR+ across rules and by the share of rules whose
LR+ agree within a factor of two. Disagreements are listed by rule.
