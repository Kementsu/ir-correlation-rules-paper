# Functional groups a rule needed but `functional_groups_smarts.csv` did not have

**Update 2026-09-14 (freeze):** every group in the table below except the
cis/trans alkene pair was adopted into `functional_groups_smarts.csv` with
source "this work"; the definitions and the reasoning are in
`docs/decisions_freeze.md`, D2 and D6. This file is kept as the record of
why each group was needed.

Every rule in `rules/rules_draft.csv` needs a ground-truth definition: a SMARTS
that answers "does this molecule carry the group the rule is about". When the
rule speaks about a group that is not in `rules/functional_groups_smarts.csv`,
`truth_smarts_group` is left **blank** and the group is recorded here instead.

**No SMARTS has been invented for any of these.** Writing them is a separate,
deliberate decision, because a badly drawn substructure silently corrupts the
sensitivity and specificity of every rule attached to it.

## Missing groups (updated 2026-09-14, second pass; 61 rows affected)

| Group needed | Rules that need it | Nearest existing group | Why the existing group is not enough |
| --- | --- | --- | --- |
| `methylene` (CH2) | SMITH-BR4-CH2-* | `alkane` = `[CX4;H0,H1,H2,H4]` | Lumps CH, CH2 and quaternary carbon and excludes CH3; the CH2 rules need CH2 alone |
| `methylene_chain_4` ((CH2)n, n>=4) | SMITH-BR4-CH2-ROCK | none | The rock only appears with four or more CH2 in a row |
| `alcohol_primary`, `alcohol_secondary`, `alcohol_tertiary` | SMITH-BR5-ROH-*-CO | `alcohols` = `[#6][OX2H]` | Does not distinguish the substitution degree of the hydroxyl carbon |
| `phenol` | SMITH-BR5-PHENOL-CO | `alcohols` | `[#6]` already matches aromatic carbon, so phenols are not separable |
| `ether_mixed` (alkyl aryl), `ether_aryl` (diaryl) | SMITH-BR5-ETHER-MIX-*, SMITH-BR5-ETHER-ARYL-CO | `ether` | Does not split saturated, mixed and aryl ethers |
| `carbonate_organic` (saturated, mixed, aromatic) | SMITH-BR7-CARB-* | `esters` | An organic carbonate is not an ester; the ester SMARTS requires a carbon on the carbonyl |
| `amide_primary`, `amide_secondary` | SMITH-BR8-AMD1-*, SMITH-BR8-AMD2-* | `amides` = `[NX3][CX3](=[OX1])[#6]` | Does not count the N-H bonds |
| `amine_primary`, `amine_secondary`, each saturated versus aromatic | SMITH-BR8-AMN1-*, SMITH-BR8-AMN2-* | `amines` = `[NX3;H2,H1;!$(NC=O)]` | Does not count N-H bonds, nor whether an alpha carbon is aromatic |
| `alkene_vinyl`, `alkene_cis`, `alkene_trans`, `alkene_trisubstituted` | SMITH-ALK16-* | `alkene` = `[CX3]=[CX3]` | No substitution pattern; cis/trans also needs stereo in the SMILES |
| `alkyne_terminal`, `alkyne_internal` | SMITH-ALY17-* | `alkyne` = `[CX2]#C` | No terminal/internal split |
| `amine_salt_primary`, `amine_salt_secondary`, `amine_salt_tertiary` (protonated amines) | SMITH-SALT19-* | none | Needs [NH3+], [NH2+], [NH+] with a counter-ion; dataset has 137 multi-fragment SMILES |
| `carbonyl_any`, `c_o_single_any`, `n_h_any` | SMITH-BR6-CO-GENERAL, SMITH-BR5-CO-GENERAL, SMITH-BR8-NH-ANY | several | Umbrella windows; decide first whether they are evaluated at all |

## Qualifiers handled by a filter over an existing group, not a new group

Saturated versus aromatic for esters, ketones, acids, aldehydes and nitriles.
The truth group exists (`esters`, `ketones`, `carboxylic_acids`, `aldehydes`,
`nitriles`); the split is "is the alpha carbon aromatic", which is a second
SMARTS applied on top. Flagged in each row's `condition_notes`. Until that
filter exists, the saturated and aromatic rows of a group can only be
evaluated together, as the union of their windows.

## Still expected once Coates is obtained

Anhydride, acid halide (the dataset has 0 acyl halides anyway), isocyanate,
thiol, sulfone, sulfoxide, imine, alkyl halide C-X ranges.
