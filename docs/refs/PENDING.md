# Reference articles still to be obtained

`docs/refs/` holds the reference articles used to transcribe
`rules/rules_draft.csv`. Its contents are **not redistributed**: everything in
this directory except this file is excluded from version control.

## Status

Every automated download attempted on 2026-09-14 was refused with **HTTP 403
Forbidden**, both by a direct HTTP client and by the standard page fetcher. No
mirror, proxy or alternative route was tried, by instruction. The files below
have to be downloaded by hand into `docs/refs/` under the given file names.

| Target file name                | Status     | Source |
| ------------------------------- | ---------- | ------ |
| `coates_2000.pdf`               | 403, pending | Coates (a) below |
| `smith_big_review_iv.pdf`       | 403, pending | Smith IV |
| `smith_big_review_v.pdf`        | 403, pending | Smith V |
| `smith_big_review_vi.pdf`       | 403, pending | Smith VI |
| `smith_big_review_vii.pdf`      | 403, pending | Smith VII |
| `smith_big_review_viii.pdf`     | 403, pending | Smith VIII |

### a) Coates

Coates, J. "Interpretation of Infrared Spectra, A Practical Approach", in
*Encyclopedia of Analytical Chemistry*, Wiley, 2000, pp. 10815-10837.
DOI [10.1002/9780470027318.a5606](https://doi.org/10.1002/9780470027318.a5606)

Open copy at Wiley Analytical Science:
<https://analyticalscience.wiley.com/content/article-do/interpretation-infrared-spectra-practical-approach>

### b) Smith, "IR Spectral Interpretation Workshop", *Spectroscopy*

Brian C. Smith, series "The Big Review".

| Part | Title | Citation | URL |
| ---- | ----- | -------- | --- |
| IV   | Hydrocarbons | *Spectroscopy* 2025, **40**(1), 16-19 | <https://www.spectroscopyonline.com/view/the-big-review-iv-hydrocarbons> |
| V    | The C-O Bond | *Spectroscopy* 2025, **40**(3), 10-13 | <https://www.spectroscopyonline.com/view/the-big-review-v-the-c-o-bond> |
| VI   | Carbonyl Compounds | *Spectroscopy* 2025, **40**(4), 12-18 | <https://www.spectroscopyonline.com/view/the-big-review-vi-carbonyl-compounds> |
| VII  | More Carbonyl Compounds | *Spectroscopy* 2025 | <https://www.spectroscopyonline.com/view/the-big-review-vii-more-carbonyl-compounds> |
| VIII | Organic Nitrogen Compounds | *Spectroscopy* 2026, **41**(1), 20-26 | <https://www.spectroscopyonline.com/view/the-big-review-viii-organic-nitrogen-compounds> |

On the Spectroscopy web pages the correlation tables are published as images. If
only the HTML version can be obtained, save the table images into this directory
as `smith_big_review_<part>_table_<n>.png` so they can be read directly.

## What this blocks

`rules/rules_draft.csv` currently contains only the rows that could be cited
exactly. The gap against the intended coverage is listed in
`docs/rules_draft_notes.md`, section "Coverage not yet met".
