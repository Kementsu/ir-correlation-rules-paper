# Notes on the draft correlation rule table

Companion to `rules/rules_draft.csv`. Nothing in that file is frozen: every row
carries `frozen = no` and the table is a draft for human review.

## 1. Provenance (updated 2026-09-14, second pass)

The Smith articles are free to read on spectroscopyonline.com; only their PDF
export is blocked. In the second pass every Smith source below was read on the
web page itself, and every numbered table was read from the published table
image (the tables are served as PNG files on the publisher's CDN). So every row
whose `table` column is filled was transcribed from the table as printed, and
every row whose `table` column is empty was transcribed from a sentence of the
article text; that sentence is copied in `source_quote`.

Coates (Wiley) is still not obtained: the open copy on Wiley Analytical Science
is behind a login or paywall from this side. See `docs/refs/PENDING.md`.

## 2. Sources and rows

| Source (Smith, Spectroscopy) | Read | Rows |
| --- | --- | --- |
| The Big Review IV: Hydrocarbons, 2025, 40(1), 16-19 | Text + Tables I, III | 12 |
| The Big Review V: The C-O Bond, 2025, 40(3), 10-13 | Text + Tables I, II | 11 |
| The Big Review VI: Carbonyl Compounds, 2025, 40(4), 12-18 | Text + Tables I, II | 11 |
| The Big Review VII: More Carbonyl Compounds, 2025, 40(8), 27-30 | Text (Tables I-III restated in text) | 13 |
| The Big Review VIII: Organic Nitrogen Compounds, 2026, 41(1), 20-26 | Text + Tables 1-4 | 23 |
| The C=O Bond, Part II: Aldehydes, 2017, 32(11), 31-36 | Text | 4 |
| The Infrared Spectroscopy of Alkenes, 2016, 31(11) | Text (Table II restated in text) | 11 |
| Potpourri: Carbohydrates and Alkynes, 2017, 32(7) | Text | 4 |
| Organic Nitrogen Compounds IV: Nitriles, 2019, 34(7) | Text | 2 |
| Organic Nitrogen Compounds X: Nitro Groups, 2020, 35(9) | Text | 3 |
| Organic Nitrogen Compounds V: Amine Salts, 2019, 34(9) | Text | 7 |
| Group Wavenumbers and an Introduction to the Spectroscopy of Benzene Rings, 2016, 31(3) | Text | 3 |
| Coates, Encyclopedia of Analytical Chemistry, 2000 | Not obtained | 0 |
| **Total** | | **104** |

Page numbers are blank where the web page does not print them (alkenes,
alkynes, nitriles, nitro, amine salts, benzene rings). They must be added from
the issue PDF or the DOI landing page before freezing.

## 3. Discrepancies between sources

Coates is still missing, so no Coates versus Smith comparison exists yet.
Within Smith there is one internal point to settle:

- Big Review V, Table I prints the alcohol "O-H Bends" cell as
  "3350+-50, 650+-50". The text describes only one bend, the O-H wag at
  650+-50, and 3350 is the O-H stretch. The 3350 entry in the bends column is
  treated as a typesetting repeat and not transcribed as a bend
  (`SMITH-BR5-ROH-OH-WAG`, condition_notes).

## 4. Rules with no ground-truth group

61 of 104 rows carry a blank `truth_smarts_group`. The groups they need are
listed in `rules/groups_missing.md`. The main families are: methylene;
primary, secondary, tertiary alcohol and phenol; mixed and aryl ether; organic
carbonate; primary and secondary amide; primary and secondary amine, each split
saturated versus aromatic; alkene substitution patterns (vinyl, cis, trans,
trisubstituted); terminal versus internal alkyne; amine salts (protonated
amines); and the umbrella rules for any carbonyl, any C-O bond, and any N-H
bond. No SMARTS was invented for any of them.

## 5. Transcription doubts to resolve before freezing

1. `SMITH-BR4-BZ-META-690`: resolved. The +-10 tolerance sits in the column
   header of Table III and therefore applies to every row.
2. `SMITH-BR8-AMN2-AR-NH`: Table 4 gives only "~3400" for the aromatic
   secondary amine N-H stretch, with no range. wn_min and wn_max are left
   blank on purpose; a tolerance has to be chosen and justified, or the row
   dropped.
3. `SMITH-ALD17-CH-BEND`: the source says "around 1390"; the +-10 window is an
   editorial choice, flagged in condition_notes.
4. Negative conditions: the ortho and para rules require the ABSENCE of the
   690 band. How absence is scored is an evaluation decision, not made here.
5. `intensity = any` still carries two meanings (source silent, or source says
   any). Split before freezing.
6. Umbrella rules (`SMITH-BR6-CO-GENERAL`, `SMITH-BR5-CO-GENERAL`,
   `SMITH-BR8-NH-ANY`) are stated by the author as pattern-recognition windows,
   not as diagnostics for a single group. Decide whether they enter the
   evaluation as rules, or only as context.
7. Amine salt rules are the source of the "salt mimics alkyne or nitrile"
   trap that automated interpretation runs into (`SMITH-SALT19-COMB`, 2000-2800).
   They only make sense on the salt stratum of the dataset.

## 6. Coverage against the intended minimum

Covered: methyl and methylene C-H stretch and bends; aromatic C-H stretch,
ring stretches and out-of-plane bends; benzene substitution patterns including
the 690 band; alkene C-H, C=C and out-of-plane wags by substitution; alkyne C-H
and triple bond by substitution; O-H stretch and wag of alcohols and phenols;
C-O of alcohols by degree and of ethers by type; ketone C=O and C-C-C;
aldehyde C=O, C-H doublet and bend; carboxylic acid O-H, C=O, C-O and bends;
ester Rule of 3 (saturated and aromatic); organic carbonates; amide I and II,
N-H stretches, C-N and wags (primary and secondary); amine N-H stretches,
scissors, C-N and wags (primary and secondary, saturated and aromatic); amine
salts; nitrile; nitro.

Not covered by any Smith source read so far: alkyl halide C-X ranges (Smith's
halogen article, Spectroscopy 2023, 38(9), 12-15 and 42, gives example
positions and the overlap statement but its Table I could not be read from the
text; read the table image before adding rows), anhydrides, acid halides,
isocyanates, sulfur groups, imines. Coates is the source expected to cover
these in one place.
