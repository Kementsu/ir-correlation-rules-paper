# Functional groups a rule needs but `functional_groups_smarts.csv` does not have

Every rule in `rules/rules_draft.csv` needs a ground-truth definition: a SMARTS
that answers "does this molecule carry the group the rule is about". When the
rule speaks about a group that is not in `rules/functional_groups_smarts.csv`,
`truth_smarts_group` is left **blank** and the group is recorded here instead.

**No SMARTS has been invented for any of these.** Writing them is a separate,
deliberate decision, because a badly drawn substructure silently corrupts the
sensitivity and specificity of every rule attached to it.

## Missing groups

| Group needed | Rules that need it | Nearest existing group | Why the existing group is not enough |
| ------------ | ------------------ | ---------------------- | ------------------------------------- |
| `methylene` | `SMITH-BR4-CH2-ASYM`, `SMITH-BR4-CH2-SYM` | `alkane` = `[CX4;H0,H1,H2,H4]` | `alkane` matches any sp3 carbon with 0, 1, 2 or 4 hydrogens, so it lumps methine, methylene and quaternary carbon together and excludes methyl. A rule about the CH2 stretch needs CH2 alone. |
| `alcohol_primary` | `SMITH-BR5-ROH-PRIM-CO` | `alcohols` = `[#6][OX2H]` | `alcohols` does not distinguish the substitution degree of the carbon bearing the OH, which is exactly what the rule keys on. |
| `alcohol_secondary` | `SMITH-BR5-ROH-SEC-CO` | `alcohols` | As above. |
| `alcohol_tertiary` | `SMITH-BR5-ROH-TERT-CO` | `alcohols` | As above. |
| `alcohol_aromatic` (phenol) | `SMITH-BR5-AROH-CO` | `alcohols` | `[#6][OX2H]` already matches a phenol, because `#6` covers aromatic carbon, so it cannot separate phenols from aliphatic alcohols. |

## Qualifiers handled elsewhere, deliberately

These are **not** listed as missing groups. They are conjugation qualifiers that
`rules/README.md` assigns to `condition_notes`, not distinct substructures:

- saturated versus aromatic **ester** (`SMITH-BR7-EST-*`), truth group `esters`
- saturated **ether** (`SMITH-BR5-ETHER-SAT-CO`), truth group `ether`

The rules still cannot be evaluated exactly as stated until the dataset can be
split on that qualifier. The difference from the rows above is that the split is
a filter over an existing group rather than a new group. Flagged here so the
decision is visible rather than implied.

## Expected to appear once the sources are obtained

The reference articles could not be downloaded (see `docs/refs/PENDING.md`), so
the rules that would need these groups are not transcribed yet. Listed so the
gap is not rediscovered later: anhydride, isocyanate, thiol, sulfone, sulfoxide,
phenol as distinct from alcohol, primary versus secondary versus tertiary amine,
primary versus secondary amide, alkene substitution patterns (vinyl, vinylidene,
cis, trans, trisubstituted), and terminal versus internal alkyne.
