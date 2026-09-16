# Pipeline notes (2026-09-14)

Status: the pipeline runs end to end on the Chemotion collection. It was
checked on the development split only. **The rules were frozen the same day
(see the Freeze section); no confirmatory number exists yet.**

## Scripts and what they produce

| Step | Script | Output |
| --- | --- | --- |
| 0 | `scripts/inventory.py` | `data/processed/inventory.csv`, `docs/inventory.md` |
| 1 | `scripts/preprocess.py` | `data/processed/spectra.npz` (gitignored, 84 MB), `spectra_meta.csv` |
| 2 | `scripts/bands.py` | `data/processed/bands.csv` |
| 3 | `scripts/evaluate_rules.py --split dev` | `data/processed/rule_metrics_dev.csv`, `docs/rule_metrics_dev.md` |

Fixed choices, all to be stated in the Methods section: absorbance
A = -log10(T) with T clipped at 1e-4; 2 cm-1 grid from 400 to 4000;
asymmetric least squares baseline (lam 1e6, p 0.001, 10 iterations);
normalisation to the strongest point in 650 to 3800; band = local maximum
with prominence >= 0.01 of the strongest band (candidates), evaluation
thresholds swept over 0.01, 0.02, 0.05 and 0.10; intensity classes strong
>= 0.60, medium >= 0.20 of the strongest band; shape classes by FWHM, sharp
< 30, broad 30 to 100, very broad > 100 cm-1.

## Development / confirmatory split

20 percent of the distinct InChIKeys (seed 20260914) form the development
split, 421 spectra; the other 1692 spectra are the confirmatory set and must
not be looked at until the rule table is frozen. Duplicates of one structure
never straddle the two sets. The main stratum (single fragment, no metals)
of the development split has 384 spectra.

## What the pipeline check showed (development split only)

These are observations about the pipeline and the data, not results.

1. **Sampling technique confirmed.** The JCAMP field `SAMPLING PROCEDURE`
   reads "Diamant-ATR" or "ATR platinum Diamond 1 Refl" in about 1850 of
   2113 spectra; 139 are blank and 116 carry a placeholder. Chemotion is an
   ATR collection. Every relative intensity in this dataset carries the ATR
   wavelength dependence (bands at high wavenumber look weaker than in
   transmission). Two consequences for the rules: intensity words such as
   "intense" in the sources were written for transmission spectra, and the
   NIST replication (transmission) is where that difference will show.
2. **The nitrile case, a worked example of why a rule fails.** 26 nitriles
   in the development stratum. The C-N triple bond band is present in all 26
   (apex between 2216 and 2246 cm-1), yet at prominence 0.05 the rule
   "2220-2240, intense" finds 1 of them. Two separate causes, both real:
   half of the nitriles belong to one family of large carbazole-substituted
   dicyanobenzenes from one project, where the C-N band is 2 to 3 percent of
   the strongest band; and several apexes sit at 2216 to 2220, just outside
   the source window. So the paper will need (a) the prominence sweep down
   to 0.01, and (b) a note that "intense" is relative to the molecule size
   in ATR.
3. **Clustering.** The 1923 spectra of the main stratum have 545 distinct
   Murcko scaffolds; the largest scaffold families hold 193, 93, 58, 58 and
   52 spectra. Spectra are not independent samples of chemistry. The
   confirmatory analysis should report metrics both per spectrum and per
   scaffold family (or with a cluster bootstrap), and this is another reason
   the NIST replication matters.
4. **Where the "intensity" clause helps and where it hurts.** With the
   intensity clause the ester C=O rule (1735-1755, strong) goes from LR+ 2.4
   to 20 on the development split, because the C=O of an ester is indeed
   among the strongest bands; the acid O-H envelope (2500-3500, strong and
   broad) goes from useless by position (LR+ 1.0, everything has something
   there) to LR+ 2.9. Conversely the same clause kills the nitrile rule (see
   2). The full-versus-position comparison is a result in itself.
5. **The failure analysis works.** For each rule with false positives the
   script lists the groups enriched among the false positives (odds ratio
   against the true negatives). Examples from the check: the saturated
   ketone C=O window (1705-1725) is fired by esters (OR 22) and methyl-rich
   molecules; the amide I window (1630-1680) by ketones (OR 7); the 690
   ring bend "meta" rule by monosubstituted rings (OR 8), as expected.
6. **Windows that most compounds satisfy.** Aromatic out-of-plane (700-1000),
   ring modes (1400-1620), saturated ether C-O (1070-1140) and the acid C-O
   (1210-1320) have specificity below 0.15 in this dataset: nearly every
   spectrum has a band there. They can only work in combination or with an
   intensity clause; on their own they are pattern-recognition windows, as
   the sources themselves say.

## Proposed SMARTS for the missing groups

`rules/groups_proposed_smarts.csv` holds 37 candidate definitions (status
"proposed, not adopted") with the number of matches in the main stratum, so
the review can see at once which rules would become evaluable and with what
n. Known problem inside it: the cis and trans alkene patterns match every
disubstituted alkene (134 each) because the match ignores the stereo marks;
they need `useChirality=True` in the matcher and SMILES that carry the
stereo, which many depositor SMILES do not. Nothing in this file is used by
`evaluate_rules.py` until it is moved into `functional_groups_smarts.csv`
by a deliberate decision.

## Freeze (same day, later)

The decisions are in `docs/decisions_freeze.md` and the plan in
`docs/preregistration.md`. `rules/rules_frozen.csv` has 106 rows (101
evaluable), the SMARTS table 60 groups, and `evaluate_rules.py` now scores
composite rules (`requires` / `forbids` windows), two strata, a primary
threshold of 0.02 and a scaffold-cluster bootstrap. The development split
was run once more as a final pipeline check.

## Next

1. Commit and tag `rules-frozen-v1`.
2. Run `python scripts/evaluate_rules.py --split confirm` once.
3. NIST condensed-phase replication with `scripts/nist_download.py` (all
   Index values, full JCAMP with metadata).
