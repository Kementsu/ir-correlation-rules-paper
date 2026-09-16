"""
supplement.py: the Supplementary Information, generated from the result tables.

Output: results/supplement.tex (built with latexmk -pdf supplement.tex)

Contents
  S1  the 60 SMARTS definitions with their source and match counts
  S2  every evaluable rule (all tiers and strata): LR+ under the three nested
      definitions at the primary threshold, and under the full definition at
      the four thresholds of the sweep, in both collections
  S3  the four preregistered hypotheses and their outcome (text)
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
PROCESSED = ROOT / "data" / "processed"
RULES = ROOT / "rules"
OUT = ROOT / "results" / "supplement.tex"
PRIMARY = 0.02
SWEEP = (0.01, 0.02, 0.05, 0.10)


def tex(s: str) -> str:
    return (str(s).replace("\\", "\\textbackslash{}").replace("&", "\\&").replace("%", "\\%")
            .replace("_", "\\_").replace("#", "\\#").replace("$", "\\$").replace("^", "\\^{}")
            .replace("~", "\\textasciitilde{}"))


def fmt(v, under=False):
    if pd.isna(v):
        return "--"
    s = f"{v:.1f}" if v < 10 else f"{v:.0f}"
    return f"({s})" if under else s


def smarts_table() -> str:
    g = pd.read_csv(RULES / "functional_groups_smarts.csv")
    inv = pd.read_csv(PROCESSED / "inventory.csv", low_memory=False)
    meta = pd.read_csv(PROCESSED / "spectra_meta.csv")
    main = meta[(meta.split == "confirm") & (meta.is_multifragment == False) & (meta.has_unusual_elements == False)].file_id  # noqa: E712
    inv = inv[inv.file_id.isin(main)]
    ninv = pd.read_csv(PROCESSED / "inventory_nist.csv", low_memory=False)
    nmeta = pd.read_csv(PROCESSED / "spectra_meta_nist.csv")
    nmain = nmeta[(nmeta.is_multifragment == False) & (nmeta.has_unusual_elements == False)].file_id  # noqa: E712
    ninv = ninv[ninv.file_id.isin(nmain)]
    src_short = {"Punjabi et al. 2025, adapted from Fine et al. 2020": "Punjabi et al.", }
    lines = [
        "\\section*{S1. Ground-truth definitions}",
        "Table~S1 lists the 60 SMARTS patterns used as ground truth, their source, and the number of spectra "
        "in the main stratum of each collection whose structure matches (Chemotion confirmatory set, "
        f"$n$ = {len(inv):,}; NIST, $n$ = {len(ninv):,}). Patterns marked ``this work'' were written for this study "
        "following the wording of the rule source; the rest are those of Punjabi et al., adapted from Fine et al.",
        "\\begingroup\\footnotesize\\setlength{\\tabcolsep}{4pt}",
        "\\begin{longtable}{@{}>{\\raggedright\\arraybackslash}p{3.2cm}>{\\raggedright\\arraybackslash}p{7.6cm}lrr@{}}",
        "\\caption{Ground-truth SMARTS definitions and match counts.}\\label{tab:s1}\\\\",
        "\\toprule Group & SMARTS & Source & Chemotion & NIST \\\\ \\midrule \\endfirsthead",
        "\\toprule Group & SMARTS & Source & Chemotion & NIST \\\\ \\midrule \\endhead",
        "\\midrule \\multicolumn{5}{r}{\\small continued} \\\\ \\endfoot \\bottomrule \\endlastfoot",
    ]
    for _, r in g.iterrows():
        col = f"fg_{r.group}"
        c = int(inv[col].astype(bool).sum()) if col in inv else 0
        n = int(ninv[col].astype(bool).sum()) if col in ninv else 0
        src = "Punjabi et al." if r.source.startswith("Punjabi") else "this work"
        lines.append(f"{tex(r.group)} & {{\\scriptsize\\texttt{{{tex(r.smarts)}}}}} & {src} & {c} & {n} \\\\")
    lines += ["\\end{longtable}\\endgroup", ""]
    return "\n".join(lines)


def rule_table() -> str:
    rules = pd.read_csv(RULES / "rules_frozen.csv").set_index("rule_id")
    mc = pd.read_csv(PROCESSED / "rule_metrics_confirm.csv")
    mn = pd.read_csv(PROCESSED / "rule_metrics_nist_confirm.csv")

    def cell(m, rid, stratum, definition, prom):
        s = m[(m.rule_id == rid) & (m.stratum == stratum) & (m.definition == definition) & (m.prominence == prom)]
        if s.empty:
            return None, None, None
        s = s.iloc[0]
        return s.LR_pos, bool(s.underpowered), int(s.n_pos)

    order = [r for r in rules.index if r in set(mc.rule_id) | set(mn.rule_id)]
    lines = [
        "\\section*{S2. Every evaluable rule under every definition and threshold}",
        "Table~S2 gives, for each of the 101 evaluable rules, the positive likelihood ratio under the three nested "
        "definitions at the primary band threshold (prominence 0.02 of the strongest band), and under the full "
        "definition at the four thresholds of the sweep. Rules of tier ``class'' are the umbrella windows of the "
        "source (for example any carbonyl, 1600 to 1900~cm$^{-1}$); rules of stratum ``salt'' are scored on the salt "
        "stratum only (Chemotion confirmatory salt stratum $n$ = 35, NIST $n$ = 314). Values in parentheses rest on "
        "fewer than ten positive spectra. Where a rule states no intensity or shape the three definitions coincide.",
        "\\begin{landscape}",
        "\\begingroup\\scriptsize\\setlength{\\tabcolsep}{3pt}",
        "\\begin{longtable}{@{}>{\\raggedright\\arraybackslash}p{4.4cm}llr|rrrr|rrr|r|rrrr|rrr@{}}",
        "\\caption{LR$^+$ of every evaluable rule by definition and threshold.}\\label{tab:s2}\\\\",
        "\\toprule & & & & \\multicolumn{7}{c|}{Chemotion} & & \\multicolumn{7}{c}{NIST} \\\\",
        " & & & & \\multicolumn{4}{c|}{full definition, threshold} & \\multicolumn{3}{c|}{threshold 0.02} & & "
        "\\multicolumn{4}{c|}{full definition, threshold} & \\multicolumn{3}{c}{threshold 0.02} \\\\",
        "Rule & tier & stratum & $n_+$ & 0.01 & 0.02 & 0.05 & 0.10 & pos. & +int. & +shape & $n_+$ & 0.01 & 0.02 & 0.05 & 0.10 & pos. & +int. & +shape \\\\",
        "\\midrule \\endfirsthead",
        "\\toprule Rule & tier & stratum & $n_+$ & 0.01 & 0.02 & 0.05 & 0.10 & pos. & +int. & +shape & $n_+$ & 0.01 & 0.02 & 0.05 & 0.10 & pos. & +int. & +shape \\\\ \\midrule \\endhead",
        "\\midrule \\multicolumn{19}{r}{\\small continued} \\\\ \\endfoot \\bottomrule \\endlastfoot",
    ]
    for rid in order:
        rr = rules.loc[rid]
        stratum, tier = rr.stratum, rr.tier
        row = [f"{tex(rid.replace('SMITH-', ''))} {{\\tiny {tex(rr.description)}}}", tier, stratum]
        for m in (mc, mn):
            _, _, npos = cell(m, rid, stratum, "+shape", PRIMARY)
            row.append("--" if npos is None else str(npos))
            for prom in SWEEP:
                v, u, _ = cell(m, rid, stratum, "+shape", prom)
                row.append(fmt(v, bool(u)) if v is not None else "--")
            for d in ("position", "+intensity", "+shape"):
                v, u, _ = cell(m, rid, stratum, d, PRIMARY)
                row.append(fmt(v, bool(u)) if v is not None else "--")
        lines.append(" & ".join(row) + " \\\\")
    lines += ["\\end{longtable}\\endgroup", "\\end{landscape}", ""]
    return "\n".join(lines)


HYPOTHESES = r"""
\section*{S3. Preregistered hypotheses and their outcome}
The following four hypotheses were written down (\texttt{docs/preregistration.md}, tag \texttt{rules-frozen-v1})
before the confirmatory Chemotion set was examined. Each is quoted as written, followed by the outcome.

\paragraph{H1.} \emph{Rules in the carbonyl region (1600 to 1900~cm$^{-1}$) and the triple-bond region (2100 to 2300~cm$^{-1}$) will have LR$^+$ above 5 when scored with their intensity clause; rules in the fingerprint region below 1300~cm$^{-1}$ scored by position alone will have LR$^+$ below 2 and specificity below 0.3, because nearly every spectrum has a band in those windows.}
Supported in part. The fingerprint half holds almost without exception: 37 of the 38 powered Chemotion fingerprint rules have LR$^+$ below 2 by position (the exception is the narrow vinyl C-H wag at 985 to 995~cm$^{-1}$, 2.2), and 29 of 38 have specificity below 0.3; the nine above it are the narrow windows (vinyl wags, the 690~cm$^{-1}$ ring bend, the methylene rock) and the absence rules, whose specificity comes from the forbidden band rather than from the window. The carbonyl and triple-bond half holds for the strongest bands (saturated ester C=O 43, aromatic ester 6.1, saturated ketone 5.9, nitrile 189) but not for every rule in the region: the aromatic ketone (2.5), amide (3.1) and aromatic acid (4.8) carbonyls, and the alkyne C$\equiv$C stretches (2.7 and 3.4), stay below 5. The hypothesis overstated the uniformity of the upper region.

\paragraph{H2.} \emph{Adding the intensity clause will raise LR$^+$ for strong-band groups (esters, ketones, acids, nitro) and lower sensitivity for groups whose band is weak relative to the strongest band in ATR spectra of large molecules (nitriles, C-H stretches, O-H and N-H stretches).}
Supported (Section~3.2 of the article). The clause raises LR$^+$ in 16 of 20 Chemotion rules and 23 of 29 NIST rules, and halves sensitivity or worse in 8 of each. The nitrile is the extreme case (sensitivity 0.78 to 0.06). The part of the hypothesis that attributed the effect to ATR was not supported: the NIST transmission spectra show the same distribution of nitrile band heights.

\paragraph{H3.} \emph{The composite benzene-substitution rules (C-H wag window plus presence or absence of the 690 ring bend) will outperform either half alone, but none of the four patterns will reach LR$^+$ above 3 on a dataset that is 93 percent aromatic.}
Supported. Composite mono 1.96 against 1.05 (wag) and 1.88 (bend); composite meta 1.40 against 1.08 and 1.29. No pattern reaches 3 in Chemotion (in NIST the composite mono rule reaches 3.7, on a collection that is 66\% aromatic). The gain of the composite over the ring bend alone is small: the discriminating half is the bend.

\paragraph{H4.} \emph{The groups enriched among false positives will be chemically interpretable in most cases (an ester in a ketone window, a ketone in an amide window), not random.}
Supported. Across the rules with at least five false positives, the most enriched groups are neighbouring carbonyls in carbonyl windows (aromatic esters in the saturated ketone window, odds ratio 20; aromatic acids in the aromatic ketone window, 18), nitriles in the internal alkyne window (57), and aromatic C-H wags in the fingerprint bending windows (monosubstituted rings, 43; para rings, 64). Table~2 of the article summarises them by failure mode.
"""


def main() -> int:
    head = r"""% generated by scripts/supplement.py, do not edit by hand
\documentclass[10pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[margin=2cm]{geometry}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{pdflscape}
\usepackage[hidelinks]{hyperref}
\title{Supplementary Information\\[4pt]\large Classical infrared correlation rules as diagnostic tests:\\likelihood ratios from 6,663 experimental spectra}
\author{Kementsu Ibarguen Calvo\\\small Mol Insight S.L., Bilbao, Spain}
\date{}
\renewcommand{\thetable}{S\arabic{table}}
\begin{document}
\maketitle
\noindent All tables are generated by \texttt{scripts/supplement.py} from the result files in \texttt{data/processed/} of the repository \url{https://github.com/Kementsu/ir-correlation-rules-paper} (tag \texttt{rules-frozen-v1}). The per-rule contingency tables, confidence intervals and false-positive enrichment for every rule, definition and threshold are in \texttt{rule\_metrics\_confirm.csv} and \texttt{rule\_metrics\_nist\_confirm.csv}.

"""
    body = smarts_table() + rule_table() + HYPOTHESES + "\n\\end{document}\n"
    OUT.write_text(head + body, encoding="utf-8", newline="\n")
    print(f"[supplement] wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
