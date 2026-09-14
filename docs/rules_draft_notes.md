# Notes on the draft correlation rule table

Companion to `rules/rules_draft.csv`. Nothing in that file is frozen: every row
carries `frozen = no` and the table is a draft for human review.

## 1. Provenance of what is in the table

**Read this first.** None of the 21 rows currently in `rules_draft.csv` was read
by the transcriber from the published article. Every automated attempt to
download the sources was refused (see section 2), so the rows transcribed are
exactly the values the project lead supplied as already verified against the
printed tables. They are recorded here with the citation the project lead gave.

The practical consequence: the `source_quote` column holds the numeric row as it
was handed over, not a character-for-character copy of the published table cell.
Before any row is frozen, it has to be checked against the article itself.

## 2. Sources obtained and not obtained

Attempted on 2026-09-14. Every URL returned **HTTP 403 Forbidden**, to a direct
HTTP client and to the standard page fetcher alike. By instruction, no mirror,
proxy or alternative route was tried.

| Source | Obtained | Rules transcribed |
| ------ | -------- | ----------------- |
| Coates, *Encyclopedia of Analytical Chemistry*, Wiley 2000, DOI 10.1002/9780470027318.a5606 | No, 403 | 0 |
| Smith, The Big Review IV: Hydrocarbons, *Spectroscopy* 2025, 40(1), 16-19 | No, 403 | 10 |
| Smith, The Big Review V: The C-O Bond, *Spectroscopy* 2025, 40(3), 10-13 | No, 403 | 5 |
| Smith, The Big Review VI: Carbonyl Compounds, *Spectroscopy* 2025, 40(4), 12-18 | No, 403 | 0 |
| Smith, The Big Review VII: More Carbonyl Compounds, *Spectroscopy* 2025 | No, 403 | 6 |
| Smith, The Big Review VIII: Organic Nitrogen Compounds, *Spectroscopy* 2026, 41(1), 20-26 | No, 403 | 0 |
| **Total** | | **21** |

The rules that were transcribed despite the failed downloads are the ones the
project lead had already verified by hand. `docs/refs/PENDING.md` lists the exact
URLs and the file names to save them under.

## 3. Discrepancies between Coates and Smith

**None can be reported yet.** Detecting a discrepancy requires two sources
stating a window for the same group, and Coates could not be obtained, so every
row in the table comes from a single author. This section is the reason the
table keeps one row per rule *and per source* rather than merging windows, and
it is expected to be the most informative part of the document once Coates is
available.

The comparison to run first, once Coates is in hand, is the set of groups the
current table already covers: methyl and methylene C-H stretch, benzene
substitution pattern bands, ester C=O and C-O, and alcohol C-O by substitution
degree.

## 4. Rules with no ground-truth group

Six rows carry a blank `truth_smarts_group`, needing five distinct groups that
are not in `rules/functional_groups_smarts.csv`. They are itemised, with the
nearest existing group and why it does not serve, in `rules/groups_missing.md`:

- `SMITH-BR4-CH2-ASYM`, `SMITH-BR4-CH2-SYM` need `methylene`
- `SMITH-BR5-ROH-PRIM-CO` needs `alcohol_primary`
- `SMITH-BR5-ROH-SEC-CO` needs `alcohol_secondary`
- `SMITH-BR5-ROH-TERT-CO` needs `alcohol_tertiary`
- `SMITH-BR5-AROH-CO` needs `alcohol_aromatic`

No SMARTS was invented for any of them.

Six further rows (`SMITH-BR7-EST-*`, `SMITH-BR5-ETHER-SAT-CO`) do carry a truth
group but state a qualifier the group cannot express, saturated versus aromatic.
That is recorded in their `condition_notes` and in `groups_missing.md` under
"Qualifiers handled elsewhere".

## 5. Transcription doubts to resolve

1. **`SMITH-BR5-*` table number is unknown.** The project lead cited The Big
   Review V without a table number, so `table` is blank for all five C-O rows.
2. **`SMITH-BR7-*` table assignment is unresolved.** The source was cited as
   "Tables I and II" for both the saturated and the aromatic ester block. Which
   block sits in which table is not known, so all six rows carry
   `Tables I and II` rather than a guess.
3. **`SMITH-BR7-*` page range is unknown.** The citation for The Big Review VII
   carried no page numbers, so `page` is blank for those six rows.
4. **The meta 690 window is inferred.** The monosubstituted entry states
   "690 plus or minus 10"; the meta entry states only "with 690". The window for
   `SMITH-BR4-BZ-META-690` was taken as 680 to 700 by analogy, which is an
   inference and is flagged in that row's `condition_notes`. If the source gives
   a different tolerance, this row must change.
5. **Negative conditions are not yet a testable form.** The ortho and para rules
   are stated partly as the *absence* of a band near 690. That is recorded in
   `condition_notes` as prose. How an absence is scored against a spectrum, and
   with what threshold, is an evaluation decision that is not made here.
6. **Intensity and shape are `any` wherever the source did not state them.** No
   value was supplied from the transcriber's own knowledge. This means `any`
   carries two different meanings at the moment, "the source says any" and "the
   source is silent", and the distinction is currently lost. Worth splitting
   into two values before freezing.

## 6. Coverage not yet met

The intended minimum coverage for this session is far from reached, because five
of the six sources could not be read. Covered so far:

- methyl and methylene C-H stretch
- benzene substitution patterns, mono, ortho, meta and para, including the 690 band
- ester C=O, C-C-O and O-C-C, saturated and aromatic
- alcohol C-O by substitution degree, and saturated ether C-O

Not covered, and needing the sources in `docs/refs/PENDING.md`:

- aromatic C-H stretch
- aromatic C=C ring stretch
- alkene C=C stretch and out-of-plane deformations
- alkyne C-H stretch and carbon-carbon triple bond stretch
- O-H stretch of alcohols and phenols
- ether C-O other than the saturated case
- ketone C=O
- aldehyde C=O and the C-H doublet near 2720
- carboxylic acid broad O-H and C=O
- amide I, amide II and amide N-H
- amine N-H and the number of N-H bands by substitution
- nitrile carbon-nitrogen triple bond stretch
- nitro symmetric and asymmetric stretch
- alkyl halide C-X

Most of these sit in The Big Review VI (carbonyls), VIII (nitrogen) and in
Coates, which is the broadest of the six and the only one giving a full
correlation table in one place.
