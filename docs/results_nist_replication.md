# NIST replication: first read (2026-09-15)

Frozen table `rules-frozen-v1`, same scripts, same thresholds. NIST main
stratum 5,124 spectra (1,737 non-aromatic, against 101 in Chemotion), salt
stratum 314. Sources: `data/processed/rule_metrics_nist_confirm.csv`,
`docs/rule_metrics_nist_confirm.md`, and the side-by-side table
`data/processed/rule_metrics_comparison.csv`.

## Does it replicate

Yes. Over the 71 group-tier rules powered in both sets, the Spearman
correlation of LR+ (full definition, primary threshold) between Chemotion
and NIST is 0.79, and 87 percent of the rules agree within a factor of
two. Two datasets that share nothing (ATR versus transmission, a 2016 to
2024 synthesis laboratory versus mostly pre-1990 reference collections,
93 percent versus 66 percent aromatic) rank the rules the same way.

The headline survives in the larger set. Of the 85 NIST-powered group
rules: LR+ >= 5 for 10, 2 to 5 for 31, 1.2 to 2 for 22, below 1.2 for 22.
Fingerprint rules (window at or below 1350 cm-1, 43 rules) have a median
LR+ of 1.21; rules at or above 1500 cm-1 a median of 3.03. NIST is a
little kinder to the fingerprint (Chemotion medians 1.07 and 2.8),
because with 34 percent non-aromatic compounds the fingerprint is less
crowded, but the conclusion is the same: position alone in the
fingerprint is close to uninformative.

## The nine rules that disagree by more than a factor of two

| rule | Chemotion LR+ | NIST LR+ | reading |
| --- | --- | --- | --- |
| ester saturated C=O 1735-1755 | 43 | 12 | both strong; in NIST more non-ester carbonyls (anhydrides, lactones, acids) share the window |
| aromatic nitrile 2220-2240 "intense" | 189 | 62 | both near-perfect specificity, both sensitivity 0.06: see below |
| terminal alkyne C=C 2100-2140 | 2.7 | 12 | 23 positives in each; Chemotion's alkynes are conjugated aryl alkynes whose band sits higher |
| primary amine saturated asym 3350-3380 | 8.7 | 2.3 | Chemotion n = 13, wide interval |
| primary amine aromatic asym 3420-3500 | 6.8 | 3.0 | NIST anilines in KBr and mull are more hydrogen bonded (broader, lower) |
| secondary amine saturated N-H 3280-3320 | 0.9 | 4.3 | Chemotion n = 24, band weak in ATR |
| saturated acid C=O 1700-1730 | 1.3 | 4.2 | Chemotion n = 10 |
| aromatic aldehyde C=O 1685-1710 | 1.5 | 3.0 | small n in both |
| ortho wag 735-770 without 690 | 0.8 | 1.7 | absence rule; fails in polyaromatic Chemotion, marginal in NIST |

Six of the nine involve a group with fewer than 30 positives in Chemotion;
the disagreements are mostly power, not chemistry. The two that are
chemistry (ester C=O, terminal alkyne) are explained by the composition
of each collection, and both keep the same sign.

## What NIST adds

1. Groups Chemotion could not test now have power: 94 saturated nitriles,
   211 saturated acids, 100 primary amides, 21 organic carbonates, 18
   saturated aldehydes, 94 tertiary alcohols. The carbonate C=O rules
   (mixed 1760-1790, aromatic 1775-1820) come out at LR+ 7 and 10, the
   saturated aldehyde C=O at 6.3.
2. Better specificity for aromatic rules. The monosubstituted ring bend at
   690 rises from LR+ 1.9 (Chemotion) to 3.1 (NIST), and the composite
   mono rule to 3.7, because there are now compounds without a ring to
   put a band there. Still, no substitution rule reaches LR+ 5.
3. Rule-out value is confirmed: terminal alkyne C-H 3250-3350 LR- 0.06,
   primary amide N-H 0.10, primary amine scissors 0.11, meta wag 0.14,
   mono 690 bend 0.15.

## The nitrile clause is not an ATR artefact

In NIST the C-N triple bond band is detected at prominence >= 0.02 in 92
percent of the 150 nitriles, but its height is a median of 0.18 of the
strongest band (first quartile 0.07, third 0.37). "Intense" in the sense
of the rule (at least 0.6 of the strongest band) holds for fewer than one
nitrile in ten, in transmission as in ATR. The clause reduces sensitivity
to 0.03 (saturated) and 0.06 (aromatic) in NIST, exactly as in Chemotion.
The correct wording of the rule is "sharp and unmistakable", not "intense",
and the failure analysis should say so. A second, smaller effect: apexes
spread from 2190 to 2280 and the two published 20 cm-1 windows catch only
about half of their own group by position alone (sensitivity 0.39 and
0.46).

## Preparation and instrument caveats (for the discussion)

Mulls (1,220 of the primary spectra) carry the C-H bands of the oil, which
inflates the methyl and methylene rules' false positives in that stratum;
solutions (1,177) have solvent gaps; 2,006 spectra are digitised
micrometre scans from prism or unspecified instruments. The pooled
analysis is what the rules' authors would have seen; the split by `prep`
is a secondary analysis to add.
