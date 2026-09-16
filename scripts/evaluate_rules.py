"""
evaluate_rules.py: score correlation rules against the detected bands and the
structural ground truth, one 2x2 table per rule.

    python scripts/evaluate_rules.py --split dev       # pipeline check
    python scripts/evaluate_rules.py --split confirm   # ONLY after freezing

Inputs:  rules/rules_frozen.csv (or another table with --rules),
         rules/functional_groups_smarts.csv, data/processed/inventory.csv,
         data/processed/bands.csv, data/processed/spectra_meta.csv
Output:  data/processed/rule_metrics_<split>.csv and
         docs/rule_metrics_<split>.md

Rules without a truth_smarts_group or without a numeric window are listed as
"not evaluable" so nothing disappears silently.

Strata (column `stratum` of the rule table):
    main   spectra passing QC, single fragment, no element outside
           C H N O S P B Si and the halogens
    salt   spectra passing QC with more than one fragment (protonated amines
           and their counter-ions), no metals

"Band present" for a rule, three nested definitions, all reported:
    position   a detected band with prominence >= threshold has its apex
               inside [wn_min, wn_max]; if the rule carries a
               requires window, a band must also sit there; if it carries a
               forbids window, no band with prominence >= threshold may sit
               there (this is how "absence of the 690 band" is scored)
    +intensity as above and, when the rule states an intensity, the band's
               intensity_class matches (strong; medium accepts strong or
               medium; weak accepts anything)
    +shape     as above and, when the rule states a shape, the band's
               shape_class matches (broad accepts broad or very_broad)
The prominence threshold is swept over PROMINENCE_SWEEP; the pre-specified
primary threshold is DEFAULT_PROMINENCE.

Metrics per rule and definition: TP FP TN FN, sensitivity, specificity, PPV,
NPV, LR+ and LR- with 95 percent intervals (log scale, Altman), prevalence,
and, at the primary threshold, a cluster bootstrap interval for LR+ that
resamples Murcko scaffold families instead of spectra (spectra of one
scaffold family are not independent). Groups enriched among the false
positives are listed with their odds ratio against the true negatives.
"""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
PROCESSED = ROOT / "data" / "processed"
DOCS = ROOT / "docs"
RULES = ROOT / "rules"

PROMINENCE_SWEEP = (0.01, 0.02, 0.05, 0.10)
DEFAULT_PROMINENCE = 0.02
MIN_POSITIVES = 10
BOOT_N = 500
BOOT_SEED = 20260914
INTENSITY_OK = {"strong": {"strong"}, "medium": {"strong", "medium"},
                "weak": {"strong", "medium", "weak"}, "any": {"strong", "medium", "weak"}}
SHAPE_OK = {"sharp": {"sharp"}, "broad": {"broad", "very_broad"},
            "very_broad": {"very_broad"}, "any": {"sharp", "broad", "very_broad"}}


def lr_point(tp, fp, fn, tn, positive=True):
    a, b, c, d = (x + 0.5 if min(tp, fp, fn, tn) == 0 else x for x in (tp, fp, fn, tn))
    sens, spec = a / (a + c), d / (b + d)
    return sens / (1 - spec) if positive else (1 - sens) / spec


def lr_ci(tp, fp, fn, tn, positive=True):
    a, b, c, d = (x + 0.5 if min(tp, fp, fn, tn) == 0 else x for x in (tp, fp, fn, tn))
    sens, spec = a / (a + c), d / (b + d)
    if positive:
        lr = sens / (1 - spec); se = math.sqrt((1 - sens) / a + spec / b)
    else:
        lr = (1 - sens) / spec; se = math.sqrt(sens / c + (1 - spec) / d)
    return lr, lr * math.exp(-1.96 * se), lr * math.exp(1.96 * se)


def scaffold_of(smiles: str) -> str:
    try:
        from rdkit.Chem.Scaffolds import MurckoScaffold
        return MurckoScaffold.MurckoScaffoldSmiles(smiles=smiles) or "(acyclic)"
    except Exception:
        return "(unknown)"


def cluster_bootstrap_lr(pred: np.ndarray, y: np.ndarray, clusters: np.ndarray, rng) -> tuple[float, float]:
    uniq = np.unique(clusters)
    idx_by = {c: np.where(clusters == c)[0] for c in uniq}
    vals = []
    for _ in range(BOOT_N):
        pick = rng.choice(uniq, size=len(uniq), replace=True)
        idx = np.concatenate([idx_by[c] for c in pick])
        p, t = pred[idx], y[idx]
        tp = int((p & t).sum()); fp = int((p & ~t).sum()); fn = int((~p & t).sum()); tn = int((~p & ~t).sum())
        vals.append(lr_point(tp, fp, fn, tn))
    return float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", choices=["dev", "confirm", "all"], default="dev")
    ap.add_argument("--rules", default=str(RULES / "rules_frozen.csv"))
    ap.add_argument("--dataset", choices=["chemotion", "nist"], default="chemotion")
    args = ap.parse_args()
    suf = "" if args.dataset == "chemotion" else f"_{args.dataset}"
    tag = f"{args.dataset}_{args.split}" if args.dataset != "chemotion" else args.split

    rules = pd.read_csv(args.rules)
    inv = pd.read_csv(PROCESSED / f"inventory{suf}.csv", low_memory=False)
    meta = pd.read_csv(PROCESSED / f"spectra_meta{suf}.csv")
    bands_all = pd.read_csv(PROCESSED / f"bands{suf}.csv")
    groups = pd.read_csv(RULES / "functional_groups_smarts.csv")
    fg_cols = [f"fg_{g}" for g in groups.group]
    rng = np.random.default_rng(BOOT_SEED)

    if args.split != "all":
        meta = meta[meta.split == args.split]
    strata = {
        "main": set(meta[(meta.is_multifragment == False) & (meta.has_unusual_elements == False)].file_id),  # noqa: E712
        "salt": set(meta[(meta.is_multifragment == True) & (meta.has_unusual_elements == False)].file_id),  # noqa: E712
    }
    inv = inv.set_index("file_id")
    evaluable = rules[rules.truth_smarts_group.notna() & (rules.truth_smarts_group != "")
                      & rules.wn_min.notna() & rules.wn_max.notna()].copy()
    skipped = rules[~rules.index.isin(evaluable.index)]
    out = []
    for stratum, ids in strata.items():
        sub = evaluable[evaluable.stratum == stratum]
        if not len(ids) or not len(sub):
            continue
        truth_all = inv.loc[list(ids), fg_cols].astype(bool)
        rng_meta = meta.set_index("file_id").loc[truth_all.index]
        xlo_all = rng_meta["x_min_cm"].values if "x_min_cm" in rng_meta else np.full(len(truth_all), 0.0)
        xhi_all = rng_meta["x_max_cm"].values if "x_max_cm" in rng_meta else np.full(len(truth_all), 1e5)
        scaf_all = np.array([scaffold_of(s) for s in inv.loc[truth_all.index, "smiles_canonical"].fillna("")])
        bands = bands_all[bands_all.file_id.isin(ids)]
        print(f"[evaluate] split={args.split} stratum={stratum}: {len(truth_all)} spectra, {len(bands)} candidate bands, "
              f"{len(sub)} rules")
        for _, r in sub.iterrows():
            col = f"fg_{r.truth_smarts_group}"
            if col not in truth_all:
                print(f"  ! no truth column for {r.rule_id} ({col})"); continue
            # only spectra whose measured range covers every window of the rule
            lo = min(float(r.wn_min), float(r.get("requires_wn_min")) if pd.notna(r.get("requires_wn_min")) else 1e9,
                     float(r.get("forbids_wn_min")) if pd.notna(r.get("forbids_wn_min")) else 1e9)
            hi = max(float(r.wn_max), float(r.get("requires_wn_max")) if pd.notna(r.get("requires_wn_max")) else 0,
                     float(r.get("forbids_wn_max")) if pd.notna(r.get("forbids_wn_max")) else 0)
            cover = (xlo_all <= lo) & (xhi_all >= hi)
            truth = truth_all[cover]
            scaf = scaf_all[cover]
            n = len(truth)
            y = truth[col].values
            n_pos = int(y.sum())
            inwin = bands[(bands.position_cm >= float(r.wn_min)) & (bands.position_cm <= float(r.wn_max))]
            req = None
            if pd.notna(r.get("requires_wn_min")):
                req = bands[(bands.position_cm >= float(r.requires_wn_min)) & (bands.position_cm <= float(r.requires_wn_max))]
            forb = None
            if pd.notna(r.get("forbids_wn_min")):
                forb = bands[(bands.position_cm >= float(r.forbids_wn_min)) & (bands.position_cm <= float(r.forbids_wn_max))]
            inten = str(r.intensity) if isinstance(r.intensity, str) else "any"
            shape = str(r.shape) if isinstance(r.shape, str) else "any"
            for thr in PROMINENCE_SWEEP:
                b0 = inwin[inwin.prominence_rel >= thr]
                b1 = b0[b0.intensity_class.isin(INTENSITY_OK.get(inten, INTENSITY_OK["any"]))]
                b2 = b1[b1.shape_class.isin(SHAPE_OK.get(shape, SHAPE_OK["any"]))]
                req_ids = set(req[req.prominence_rel >= thr].file_id) if req is not None else None
                forb_ids = set(forb[forb.prominence_rel >= thr].file_id) if forb is not None else set()
                for defn, bb in (("position", b0), ("+intensity", b1), ("+shape", b2)):
                    hit = set(bb.file_id.unique())
                    if req_ids is not None:
                        hit &= req_ids
                    hit -= forb_ids
                    pred = truth.index.isin(hit)
                    tp = int((pred & y).sum()); fp = int((pred & ~y).sum())
                    fn = int((~pred & y).sum()); tn = int((~pred & ~y).sum())
                    sens = tp / (tp + fn) if tp + fn else float("nan")
                    spec = tn / (tn + fp) if tn + fp else float("nan")
                    ppv = tp / (tp + fp) if tp + fp else float("nan")
                    npv = tn / (tn + fn) if tn + fn else float("nan")
                    lrp, lrp_lo, lrp_hi = lr_ci(tp, fp, fn, tn, True)
                    lrn, lrn_lo, lrn_hi = lr_ci(tp, fp, fn, tn, False)
                    boot_lo = boot_hi = float("nan")
                    enriched = ""
                    if defn == "+shape" and thr == DEFAULT_PROMINENCE and n_pos >= MIN_POSITIVES:
                        boot_lo, boot_hi = cluster_bootstrap_lr(pred, y, scaf, rng)
                        if fp >= 5:
                            fp_m = pred & ~y; tn_m = ~pred & ~y
                            ors = []
                            for g in fg_cols:
                                if g == col:
                                    continue
                                gv = truth[g].values
                                a = int((gv & fp_m).sum()); c = int((gv & tn_m).sum())
                                if a >= 3:
                                    o = ((a + 0.5) / (fp - a + 0.5)) / ((c + 0.5) / (tn - c + 0.5))
                                    ors.append((g[3:], o, a))
                            ors.sort(key=lambda t: -t[1])
                            enriched = "; ".join(f"{g} OR={o:.1f} (n={k})" for g, o, k in ors[:3])
                    out.append(dict(rule_id=r.rule_id, stratum=stratum, tier=r.get("tier", "group"),
                                    group=r.group, truth_group=r.truth_smarts_group,
                                    wn_min=r.wn_min, wn_max=r.wn_max, rule_intensity=inten, rule_shape=shape,
                                    requires=f"{r.requires_wn_min:.0f}-{r.requires_wn_max:.0f}" if req is not None else "",
                                    forbids=f"{r.forbids_wn_min:.0f}-{r.forbids_wn_max:.0f}" if forb is not None else "",
                                    prominence=thr, definition=defn, n=n, n_pos=n_pos,
                                    prevalence=round(float(y.mean()), 3), TP=tp, FP=fp, FN=fn, TN=tn,
                                    sensitivity=round(sens, 3), specificity=round(spec, 3),
                                    PPV=round(ppv, 3), NPV=round(npv, 3),
                                    LR_pos=round(lrp, 2), LR_pos_lo=round(lrp_lo, 2), LR_pos_hi=round(lrp_hi, 2),
                                    LR_pos_boot_lo=round(boot_lo, 2), LR_pos_boot_hi=round(boot_hi, 2),
                                    LR_neg=round(lrn, 2), LR_neg_lo=round(lrn_lo, 2), LR_neg_hi=round(lrn_hi, 2),
                                    underpowered=n_pos < MIN_POSITIVES, fp_enriched_groups=enriched))
    res = pd.DataFrame(out)
    res.to_csv(PROCESSED / f"rule_metrics_{tag}.csv", index=False)

    main_tab = res[(res.prominence == DEFAULT_PROMINENCE) & (res.definition == "+shape")].copy()
    pos_tab = res[(res.prominence == DEFAULT_PROMINENCE) & (res.definition == "position")].set_index(["rule_id", "stratum"])
    status = ("**Status: pipeline check on the development split. These numbers are for "
              "debugging the pipeline, not for the paper.**" if args.split == "dev"
              else "**Confirmatory run on the frozen rule table.**")
    lines = [f"# Rule metrics, dataset = {args.dataset}, split = {args.split}", "", status, "",
             f"Primary prominence threshold {DEFAULT_PROMINENCE}; full definition (position, intensity, shape). "
             f"`LR+ [CI]` is the analytic 95 percent interval; `boot` is the scaffold-cluster bootstrap interval "
             f"({BOOT_N} resamples); `LR+ pos` is the same rule scored by position only. "
             f"Rules with fewer than {MIN_POSITIVES} positives are marked underpowered.", ""]
    for stratum in ("main", "salt"):
        t = main_tab[main_tab.stratum == stratum]
        if not len(t):
            continue
        lines += [f"## Stratum: {stratum} (n up to {int(t.n.max())}; each rule is scored on the spectra whose measured range covers its windows)", "",
                  "| rule | tier | truth group | window | n+ | sens | spec | LR+ [CI] | LR+ boot | LR- [CI] | LR+ pos | FP enriched in |",
                  "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for _, r in t.sort_values(["truth_group", "wn_min"]).iterrows():
            flag = " (underpowered)" if r.underpowered else ""
            win = f"{r.wn_min:.0f}-{r.wn_max:.0f}" + (f" +{r.requires}" if r.requires else "") + (f" no {r.forbids}" if r.forbids else "")
            boot = f"[{r.LR_pos_boot_lo:.1f}, {r.LR_pos_boot_hi:.1f}]" if not np.isnan(r.LR_pos_boot_lo) else ""
            lines.append(f"| {r.rule_id} | {r.tier} | {r.truth_group} | {win} | {r.n_pos}{flag} | {r.sensitivity:.2f} | {r.specificity:.2f} | "
                         f"{r.LR_pos:.1f} [{r.LR_pos_lo:.1f}, {r.LR_pos_hi:.1f}] | {boot} | "
                         f"{r.LR_neg:.2f} [{r.LR_neg_lo:.2f}, {r.LR_neg_hi:.2f}] | {pos_tab.loc[(r.rule_id, stratum), 'LR_pos']:.1f} | "
                         f"{r.fp_enriched_groups} |")
        lines.append("")
    lines += ["## Prominence sweep (LR+, full definition, main stratum)", "",
              "| rule | " + " | ".join(f"p>={t}" for t in PROMINENCE_SWEEP) + " |",
              "| --- | " + " | ".join("---" for _ in PROMINENCE_SWEEP) + " |"]
    sw = res[(res.definition == "+shape") & (res.stratum == "main")].pivot(index="rule_id", columns="prominence", values="LR_pos")
    for rid, row in sw.iterrows():
        lines.append(f"| {rid} | " + " | ".join(f"{row[t]:.1f}" for t in PROMINENCE_SWEEP) + " |")
    lines += ["", f"## Not evaluable ({len(skipped)} rules)", ""]
    lines += [f"- {r.rule_id}: {r.group}. {str(r.condition_notes)[:160]}" for _, r in skipped.iterrows()]
    (DOCS / f"rule_metrics_{tag}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[evaluate] {len(evaluable)} rules scored, {len(skipped)} not evaluable; wrote docs/rule_metrics_{tag}.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
