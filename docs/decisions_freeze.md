# Decisions taken to freeze the rule table (2026-09-14)

Taken on scientific and technical criteria, delegated by the project lead.
Each decision names the alternative that was rejected and why. Anything a
reviewer could call a degree of freedom is listed here so that it is fixed
before the confirmatory run.

## D1. Rules are transcribed as published, never adjusted to the data

Windows, intensities and shapes in `rules/rules_frozen.csv` are the source's
values. The development-split check showed, for instance, that several
aromatic nitrile bands sit at 2216 to 2220, just outside the published
2220 to 2240 window. The window is NOT widened. Adjusting windows to the data
would turn an audit of the rules into a re-fit of the rules; where a window
looks wrong, the paper says so in the failure analysis, with the data.

## D2. Ground truth for the 61 rules that had no SMARTS

39 substructure definitions were added to `rules/functional_groups_smarts.csv`
with source "this work". Principles: as literal as the source's own words
(a "primary alcohol" is an OH on a CH2, `[CH2X4][OX2H]`); "saturated" means
an sp3 alpha carbon and "aromatic" means an aromatic alpha carbon, so the two
are mutually exclusive and neither covers alpha,beta-unsaturated carbonyls,
which are left to the parent group only; amines and amides exclude N-N, N-O
and acyl nitrogen. Two of these groups have fewer than 5 examples in the
dataset (organic carbonate 2, saturated aldehyde 3); they stay in the table
and are reported as underpowered rather than dropped. The 17 published SMARTS
of Punjabi et al. are untouched.

## D3. Composite rules for benzene substitution are scored as published

Smith's Table III defines each pattern by a C-H wag window AND the presence
or absence of the 690 +- 10 ring bend. The table therefore carries both the
single-window rows (to see each half alone) and the composite rows:
`SMITH-BR4-BZ-MONO-BOTH` and `-META-BOTH` (both bands required, column
`requires_wn_*`), and the ortho and para rows carry `forbids_wn_* = 680-700`.
"Absent" is defined as no detected band with prominence at or above the same
threshold used for presence. Rejected alternative: a separate, looser
threshold for absence, which would be a second free parameter.

## D4. Primary prominence threshold 0.02, sweep 0.01 / 0.02 / 0.05 / 0.10

The development check showed that in this ATR collection of large molecules
diagnostically real bands (the C-N triple bond of the dicyanobenzene family)
can be 2 to 3 percent of the strongest band. 0.05 would declare them absent
for a reason that has nothing to do with the rule. 0.01 is at the noise
floor of some spectra. 0.02 is the primary value; the other three are
reported as a sensitivity analysis, always, for every rule.

## D5. Intensity and shape clauses: three nested definitions, all reported

"Position only", "position and intensity" and "position, intensity and
shape" are all computed and all appear in the results. The full definition
is the primary one because it is what the source states. Where the source
is silent on intensity or shape the clause is "any" and the three
definitions coincide. Rejected alternative: choosing per rule which clause
to keep, which is exactly the kind of choice this study should not make.
Intensity classes: strong >= 0.60, medium >= 0.20 of the strongest band in
650 to 3800 cm-1. Shape by FWHM: sharp < 30, broad 30 to 100, very broad
> 100 cm-1.

## D6. cis and trans alkene rules are not evaluable on this dataset

Most depositor SMILES carry no stereo marks, so "cis" and "trans" cannot be
established for most disubstituted alkenes. The four rows stay in the table,
marked not evaluable, rather than being scored against a `disubstituted`
group that would not test what the rule claims.

## D7. The one window the source gives without a range

Secondary aromatic amine N-H stretch, Table 4: "~3400". Window set to
3380 to 3420, the tolerance of the neighbouring N-H windows in the same
table (30 to 40 cm-1 wide). Flagged in `condition_notes`. Rejected: dropping
the rule (loses information) or a wider guess (arbitrary).

## D8. Umbrella rules are kept, tagged `tier = class`

"Any carbonyl 1600-1900", "any C-O 1000-1300", "any N-H 3300-3500", the
aromatic C-H, ring and out-of-plane windows and the generic alkene windows
are how the sources themselves describe the first pass of an interpretation.
They are scored against union ground-truth groups (`carbonyl_any`,
`c_o_single_any`, `n_h_any`, `aromatics`, `alkene`) and reported in their
own tier so they are not compared head to head with group-specific rules.

## D9. Strata

Main: QC pass, single fragment, no element outside C H N O S P B Si and the
halogens (1923 spectra). Salt: QC pass, more than one fragment, no metals
(the amine salt rules are scored only here). Metal complexes are excluded
from both. Rejected: scoring salts inside the main stratum, where a
protonated amine would count as a false positive for every N-H rule.

## D10. Statistics

Per rule and definition: 2x2 table, sensitivity, specificity, PPV, NPV, LR+
and LR- with 95 percent intervals on the log scale. Rules with fewer than 10
positives in the split are reported but marked underpowered. At the primary
threshold a cluster bootstrap (500 resamples of Murcko scaffold families)
gives a second interval for LR+, because the main stratum has 1923 spectra
in 545 scaffold families and spectra within a family are not independent.
Failure analysis: for each rule with at least 5 false positives, the groups
enriched among the false positives relative to the true negatives, by odds
ratio, top three. No multiple-testing correction is applied and none is
claimed: the LR intervals describe each rule; no rule is declared
"significant".

## D11. Development / confirmatory split

20 percent of distinct InChIKeys (seed 20260914) are the development split
used to build and check the pipeline. Everything above was decided after
looking at the development split only. The confirmatory 80 percent is run
once, with `scripts/evaluate_rules.py --split confirm`, after this table and
`rules/rules_frozen.csv` are committed and tagged. Development-split
numbers are not reported as results.

## D12. What is deliberately NOT decided here

Coates (Wiley 2000) could not be obtained; the source comparison chapter is
postponed, and adding Coates rows later will be a separate, dated addendum
to the frozen table, not an edit of it. The NIST condensed-phase replication
follows the same frozen table and the same script.
