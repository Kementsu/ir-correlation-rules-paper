# Rule and ground-truth definitions

## `functional_groups_smarts.csv`

Ground truth for "this molecule carries this functional group". One row per
group, with columns `group`, `smarts`, `source`. A molecule is counted as
carrying the group when RDKit finds at least one substructure match of `smarts`
in the structure parsed from the sample SMILES.

### Rows 1 to 17: the Punjabi et al. group set

Transcribed verbatim from the reference implementation of Punjabi et al. 2025,
repository <https://github.com/ComPlat/ir_analysis> (MIT), which in turn adapts
the group set of Fine et al. 2020 (<https://github.com/chopralab/candiy_spectrum>).
The SMARTS strings are copied as they appear in that code; only the group names
were rewritten in snake_case so they can be used as column names. The original
names are `alkane`, `methyl`, `alkene`, `alkyne`, `alcohols`, `amines`,
`nitriles`, `aromatics`, `alkyl halides`, `esters`, `ketones`, `aldehydes`,
`carboxylic acids`, `ether`, `acyl halides`, `amides`, `nitro`.

**One discrepancy inside the source repository, resolved explicitly.** The
`ether` SMARTS differs between the two places the group table appears:

| Location                       | `ether` SMARTS                            |
| ------------------------------ | ----------------------------------------- |
| `utils/create_datasets.py`     | `[OD2]([#6])[#6]`                         |
| `data/data_preproc.ipynb`      | `[OD2]([#6;!$(C=O)])([#6;!$(C=O)])`       |

In the notebook, the first form is present but commented out immediately above
the second, so the notebook version supersedes it. The notebook is also the file
that actually labels the Chemotion dataset, so we take the notebook form. The
practical difference is that the stricter form does not count the C-O-C of an
ester as an ether.

No SMARTS was invented or repaired. Every string is byte-identical to the
source, and there are no TODO entries: all 17 groups are stated unambiguously in
the source code.

### Rows 18 to 21: aromatic substitution patterns

Added for this project (`source` = `Mol Insight`), because the out-of-plane C-H
bending region of 900 to 675 cm-1 is one of the classical correlation rules we
intend to evaluate, and it is a claim about the *substitution pattern* of the
ring, which the `aromatics` group above cannot express.

- `aromatic_mono` monosubstituted benzene ring
- `aromatic_ortho` 1,2-disubstituted benzene ring
- `aromatic_meta` 1,3-disubstituted benzene ring
- `aromatic_para` 1,4-disubstituted benzene ring

Each requires a six-membered aromatic ring (`R1`) with the stated arrangement of
substituted (`[!#1]`) and unsubstituted (`cH`) ring carbons.

## `rules_template.csv`

Header only, deliberately. This is the table of classical IR correlation rules
to be filled in by hand from the printed sources (Pretsch, Silverstein,
Socrates), and frozen before any evaluation is run.

| Column              | Meaning                                                        |
| ------------------- | -------------------------------------------------------------- |
| `rule_id`           | Stable identifier for the rule.                                 |
| `group`             | Functional group the rule is about, in prose.                   |
| `description`       | The rule as stated in the source.                               |
| `wn_min`, `wn_max`  | Wavenumber window in cm-1.                                      |
| `intensity`         | `strong`, `medium`, `weak` or `any`.                            |
| `shape`             | `sharp`, `broad` or `any`.                                      |
| `condition_notes`   | Qualifiers the source attaches (phase, conjugation, ring size). |
| `truth_smarts_group`| `group` value in `functional_groups_smarts.csv` used as truth.  |
| `source_book`       | Pretsch, Silverstein, Socrates.                                 |
| `edition`           | Edition of that book.                                           |
| `table`             | Table number within the edition.                                |
| `page`              | Page number.                                                    |
| `frozen`            | `yes` once the row is locked and must not be edited again.      |
