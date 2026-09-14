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
| `smith_big_review_iv.pdf`       | PDF not offered; article and table images read on the web page 2026-09-14 | Smith IV |
| `smith_big_review_v.pdf`        | same | Smith V |
| `smith_big_review_vi.pdf`       | same | Smith VI |
| `smith_big_review_vii.pdf`      | same (tables restated in the text) | Smith VII |
| `smith_big_review_viii.pdf`     | same | Smith VIII |

Additional Smith articles read on the web page the same day (no PDF): The C=O
Bond, Part II: Aldehydes (2017, 32(11), 31-36); The Infrared Spectroscopy of
Alkenes (2016, 31(11)); Potpourri: Carbohydrates and Alkynes (2017, 32(7));
Organic Nitrogen Compounds IV: Nitriles (2019, 34(7)); X: Nitro Groups (2020,
35(9)); V: Amine Salts (2019, 34(9)); Group Wavenumbers and an Introduction to
the Spectroscopy of Benzene Rings (2016, 31(3)); Halogenated Organic Compounds
(2023, 38(9), 12-15 and 42, Table I not yet read).

The Spectroscopy articles are open on the web but the publisher does not
serve a PDF. The Big Review VII page has an audio version and a "Key
Takeaways" box; the numbered tables are PNG images on the publisher's CDN.

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
