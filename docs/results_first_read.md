# Confirmatory run: first read (2026-09-14)

Run once, on the frozen table (`rules-frozen-v1`, commit 752e344), confirm
split, main stratum n = 1539 (salt stratum n = 35, 6 positives, not
informative and reported only in the CSV). Primary threshold 0.02, full
definition. Source of every number: `data/processed/rule_metrics_confirm.csv`
and `docs/rule_metrics_confirm.md`. These are the numbers of the paper; the
development split is not used anywhere below.

## Headline

Of the 73 group-tier rules with at least 10 positives:

| LR+ (full definition) | rules |
| --- | --- |
| >= 5 (strong evidence when the band is seen) | 7 |
| 2 to 5 (moderate) | 23 |
| 1.2 to 2 (weak) | 14 |
| < 1.2 (no diagnostic value on its own) | 29 |

The split by region is the cleanest single statement in the data: the 38
rules whose window lies at or below 1350 cm-1 (the fingerprint region) have
a median LR+ of 1.07 and a maximum of 4.4; the 31 rules at or above 1500
cm-1 have a median LR+ of 2.8. Position-only scoring of a fingerprint window
is, in this dataset, close to a coin toss for the group it claims to detect.

## Hypotheses (from docs/preregistration.md)

H1, supported. Carbonyl and triple-bond region rules with their intensity
clause: saturated ester C=O LR+ 43 (bootstrap 18 to 116), saturated ketone
C=O 5.9, aromatic ester C=O 6.1, aromatic acid C=O 4.8, nitro asymmetric
5.3. Fingerprint rules by position: alcohol C-O by degree 0.96 to 0.99,
phenol C-O 0.98, saturated ether C-O 0.92, acid C-O 0.96, amine C-N 0.97
to 1.05; specificity 0.02 to 0.15.

H2, supported, with the sharpest example being the one the check
predicted. Aromatic nitrile 2220-2240: by position alone LR+ 10 with
sensitivity 0.78; with the "intense" clause LR+ 189 but sensitivity 0.06.
The intensity clause turns the rule from a good detector into a near-perfect
but almost never firing confirmation, because in ATR spectra of large
molecules the C-N band is rarely 60 percent of the strongest band. Ester
C=O goes the other way: position 2.9, full 43.

H3, supported. Composite mono rule (wag 710-770 plus 690 bend) LR+ 1.96,
against 1.05 for the wag alone and 1.88 for the 690 bend alone: the
discriminating half is the ring bend, the wag adds nothing. Meta: 1.40
composite, 1.08 and 1.29 for the halves. Ortho with "no 690" 0.82 and para
with "no 690" 1.19: the absence rule does not work on a dataset where most
molecules carry several rings, because some other ring supplies the 690
band. No pattern reaches LR+ 3.

H4, supported. The false-positive enrichment is chemically readable in
every high-LR rule: the saturated ester C=O window is fired by ketones and
acids; the saturated ketone window by aromatic esters (OR 20); the internal
alkyne window 2190-2260 by nitriles (OR 57); the secondary amide N-H window
by terminal alkynes and primary amines; amide I by aromatic ketones; the
aromatic ketone C=O window by aromatic acids (OR 18).

## Rule-out value (LR-), which the sources never state

The rules that best exclude a group when the band is missing: secondary
amide N-H stretch LR- 0.08 (sensitivity 0.94), monosubstituted-ring 690
bend 0.17, terminal alkyne C-H 0.17, nitro asymmetric 0.21, nitro scissors
0.23, aromatic ester C-C-O 0.25. Several rules with useless LR+ are good
rule-outs (meta wag 750-810: LR+ 1.08, LR- 0.25). The correlation tables
only ever describe rules as evidence FOR a group; half of their value is the
other direction.

## Robustness

The prominence sweep moves the strong rules little (saturated ester C=O 44,
43, 46, 49 across 0.01 to 0.10; nitro asymmetric 5.3 throughout). Rules
that depend on weak bands move more (secondary amide N-H 2.4 to 5.6), which
is itself the ATR effect and goes in the discussion. The scaffold-cluster
bootstrap intervals are wider than the analytic ones for every rule with a
dominant scaffold family and are the intervals to report.

## Caveats to write down before anyone reads the table

1. The dataset is 93 percent aromatic and comes from one kind of laboratory;
   specificity for aromatic rules is estimated on 101 non-aromatic spectra.
   NIST transmission spectra are the replication that answers this.
2. All spectra are ATR. Every intensity clause was written for transmission.
   The nitrile result is the clearest demonstration, and the NIST run will
   show whether it reverses.
3. Underpowered groups (organic carbonate 2, saturated aldehyde 3, primary
   amide 5, tertiary alcohol 8) are in the table but carry no inference.
4. Ground truth is the depositor's structure; label noise is unquantified.
5. Window edges were not adjusted (D1); the nitrile apexes at 2216 to 2220
   are counted as misses of the published window, on purpose.
