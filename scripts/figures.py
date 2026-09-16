"""
figures.py: the five figures of the manuscript, built from the confirmatory
result tables only (never from the development split).

Inputs:  data/processed/rule_metrics_confirm.csv        Chemotion, confirmatory
         data/processed/rule_metrics_nist_confirm.csv   NIST replication
         data/processed/rule_metrics_comparison.csv     side by side
         data/processed/bands*.csv, inventory*.csv, spectra_meta*.csv
         rules/rules_frozen.csv
Output:  results/figures/fig1_lr_by_region.pdf  (and .png)
         results/figures/fig2_position_vs_full.pdf
         results/figures/fig3_nitrile.pdf
         results/figures/fig4_benzene.pdf
         results/figures/fig5_replication.pdf
         results/figures/figure_numbers.md  (the numbers quoted in captions)

The manuscript is kept in a separate folder; copy results/figures/*.pdf into
its figures/ directory after regenerating.

Conventions: primary threshold (prominence 0.02), full definition (+shape),
main stratum, group tier, powered rules only (at least 10 positives) unless a
figure says otherwise. Blue is Chemotion, orange is NIST throughout.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PROCESSED = ROOT / "data" / "processed"
FIG = ROOT / "results" / "figures"

CHEM = "#2a78d6"   # Chemotion (ATR)
NIST = "#eb6834"   # NIST (transmission)
THIRD = "#1baf7a"
INK = "#0b0b0b"
INK2 = "#52514e"
GRID = "#e6e5e1"
FILL = "#f0efec"

PRIMARY_PROM = 0.02
FINGERPRINT_MAX = 1350.0
DIAGNOSTIC_MIN = 1500.0

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Helvetica", "Arial"],
    "font.size": 8,
    "axes.titlesize": 8.5,
    "axes.labelsize": 8,
    "xtick.labelsize": 7.5,
    "ytick.labelsize": 7.5,
    "legend.fontsize": 7.5,
    "axes.edgecolor": INK2,
    "axes.linewidth": 0.6,
    "xtick.color": INK2,
    "ytick.color": INK2,
    "axes.labelcolor": INK,
    "text.color": INK,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

NOTES: list[str] = []


def note(s: str) -> None:
    NOTES.append(s)
    print("  " + s)


def primary(m: pd.DataFrame, definition: str = "+shape") -> pd.DataFrame:
    return m[(m.prominence == PRIMARY_PROM) & (m.definition == definition)
             & (m.stratum == "main") & (m.tier == "group")].copy()


def save(fig: plt.Figure, name: str) -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(FIG / f"{name}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"[figures] wrote {name}.pdf/.png")


LABELS = {
    "SMITH-BR4-CH3-ASYM": "methyl, asym. C-H", "SMITH-BR4-CH3-SYM": "methyl, sym. C-H",
    "SMITH-BR4-CH2-ASYM": "methylene, asym. C-H", "SMITH-BR4-CH2-SYM": "methylene, sym. C-H",
    "SMITH-BR4-CH3-UMBRELLA": "methyl umbrella", "SMITH-BR4-CH2-ROCK": "methylene rock",
    "SMITH-BR4-BZ-MONO-OOP": "mono benzene, wag", "SMITH-BR4-BZ-MONO-690": "mono benzene, 690",
    "SMITH-BR4-BZ-MONO-BOTH": "mono benzene, wag + 690", "SMITH-BR4-BZ-ORTHO-OOP": "ortho benzene, wag",
    "SMITH-BR4-BZ-META-OOP": "meta benzene, wag", "SMITH-BR4-BZ-META-690": "meta benzene, 690",
    "SMITH-BR4-BZ-META-BOTH": "meta benzene, wag + 690", "SMITH-BR4-BZ-PARA-OOP": "para benzene, wag",
    "SMITH-BR5-ROH-OH-STR": "alcohol O-H", "SMITH-BR5-ROH-OH-WAG": "alcohol O-H wag",
    "SMITH-BR5-ROH-PRIM-CO": "primary alcohol C-O", "SMITH-BR5-ROH-SEC-CO": "secondary alcohol C-O",
    "SMITH-BR5-ROH-TERT-CO": "tertiary alcohol C-O", "SMITH-BR5-PHENOL-CO": "phenol C-O",
    "SMITH-BR5-ETHER-SAT-CO": "sat. ether C-O", "SMITH-BR5-ETHER-MIX-CO-AR": "aryl alkyl ether, aryl C-O",
    "SMITH-BR5-ETHER-MIX-CO-SAT": "aryl alkyl ether, alkyl C-O", "SMITH-BR5-ETHER-ARYL-CO": "diaryl ether C-O",
    "SMITH-BR6-KET-SAT-CO": "sat. ketone C=O", "SMITH-BR6-KET-AR-CO": "arom. ketone C=O",
    "SMITH-BR6-KET-SAT-CCC": "sat. ketone C-C-C", "SMITH-BR6-KET-AR-CCC": "arom. ketone C-C-C",
    "SMITH-BR6-ACID-SAT-CO": "sat. acid C=O", "SMITH-BR6-ACID-AR-CO": "arom. acid C=O",
    "SMITH-BR6-ACID-CO": "acid C-O", "SMITH-BR6-ACID-OH-STR": "acid O-H",
    "SMITH-BR6-ACID-OH-IPB": "acid O-H in-plane", "SMITH-BR6-ACID-OH-OOP": "acid O-H wag",
    "SMITH-BR7-EST-SAT-CO": "sat. ester C=O", "SMITH-BR7-EST-SAT-CCO": "sat. ester C-C-O",
    "SMITH-BR7-EST-SAT-OCC": "sat. ester O-C-C", "SMITH-BR7-EST-AR-CO": "arom. ester C=O",
    "SMITH-BR7-EST-AR-CCO": "arom. ester C-C-O", "SMITH-BR7-EST-AR-OCC": "arom. ester O-C-C",
    "SMITH-BR7-CARB-SAT-CO": "sat. carbonate C=O", "SMITH-BR7-CARB-SAT-OCO": "sat. carbonate O-C-O",
    "SMITH-BR7-CARB-MIX-CO": "mixed carbonate C=O", "SMITH-BR7-CARB-MIX-OCO": "mixed carbonate O-C-O",
    "SMITH-BR7-CARB-AR-CO": "arom. carbonate C=O", "SMITH-BR7-CARB-AR-OCO": "arom. carbonate O-C-O",
    "SMITH-BR7-CARB-OCC": "carbonate O-C-C",
    "SMITH-BR8-AMD1-NH-STR": "primary amide N-H", "SMITH-BR8-AMD-CO": "amide C=O",
    "SMITH-BR8-AMD1-SCIS": "primary amide NH2 scissors", "SMITH-BR8-AMD1-CN": "primary amide C-N",
    "SMITH-BR8-AMD1-WAG": "primary amide N-H wag", "SMITH-BR8-AMD2-NH-STR": "secondary amide N-H",
    "SMITH-BR8-AMD2-NH-IPB": "secondary amide N-H bend", "SMITH-BR8-AMD2-CN": "secondary amide C-N",
    "SMITH-BR8-AMD2-WAG": "secondary amide N-H wag",
    "SMITH-BR8-AMN1-SAT-ASYM": "primary alkyl amine, NH2 asym.", "SMITH-BR8-AMN1-AR-ASYM": "primary aryl amine, NH2 asym.",
    "SMITH-BR8-AMN1-SAT-SYM": "primary alkyl amine, NH2 sym.", "SMITH-BR8-AMN1-AR-SYM": "primary aryl amine, NH2 sym.",
    "SMITH-BR8-AMN1-SCIS": "primary amine NH2 scissors", "SMITH-BR8-AMN1-SAT-CN": "primary alkyl amine C-N",
    "SMITH-BR8-AMN1-AR-CN": "primary aryl amine C-N", "SMITH-BR8-AMN1-WAG": "primary amine N-H wag",
    "SMITH-BR8-AMN2-SAT-NH": "secondary alkyl amine N-H", "SMITH-BR8-AMN2-AR-NH": "secondary aryl amine N-H",
    "SMITH-BR8-AMN2-SAT-CNC": "secondary alkyl amine C-N-C", "SMITH-BR8-AMN2-AR-CNC": "secondary aryl amine C-N-C",
    "SMITH-BR8-AMN2-WAG": "secondary amine N-H wag",
    "SMITH-ALD17-SAT-CO": "sat. aldehyde C=O", "SMITH-ALD17-AR-CO": "arom. aldehyde C=O",
    "SMITH-ALD17-CH-STR": "aldehyde C-H", "SMITH-ALD17-CH-BEND": "aldehyde C-H bend",
    "SMITH-ALK16-VINYL-CC": "vinyl C=C", "SMITH-ALK16-VINYL-WAG1": "vinyl C-H wag (990)",
    "SMITH-ALK16-VINYL-WAG2": "vinyl C-H wag (910)", "SMITH-ALK16-TRISUB-CC": "trisubst. alkene C=C",
    "SMITH-ALK16-TRISUB-WAG": "trisubst. alkene C-H wag",
    "SMITH-ALY17-TERM-CH": "terminal alkyne C-H", "SMITH-ALY17-TERM-CC": "terminal alkyne C\u2261C",
    "SMITH-ALY17-INT-CC": "internal alkyne C\u2261C", "SMITH-ALY17-TERM-CH-BEND": "terminal alkyne C-H bend",
    "SMITH-NIT19-SAT-CN": "sat. nitrile C\u2261N", "SMITH-NIT19-AR-CN": "arom. nitrile C\u2261N",
    "SMITH-NO2-20-ASYM": "nitro asym.", "SMITH-NO2-20-SYM": "nitro sym.", "SMITH-NO2-20-SCIS": "nitro scissors",
}


def short_label(rule_id: str) -> str:
    """Readable rule name for direct labels; falls back to the identifier."""
    if rule_id in LABELS:
        return LABELS[rule_id]
    s = rule_id.replace("SMITH-", "")
    return s.lower().replace("-", " ")


# ----------------------------------------------------------------------------
# Figure 1: LR+ against band position, both datasets
# ----------------------------------------------------------------------------
def fig1(chem: pd.DataFrame, nist: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, 1, figsize=(6.5, 5.2), sharex=True)
    for ax, (name, m, col) in zip(axes, [("Chemotion (ATR)", chem, CHEM), ("NIST WebBook (transmission)", nist, NIST)]):
        p = m[~m.underpowered].copy()
        p["centre"] = (p.wn_min + p.wn_max) / 2
        ax.axvspan(400, FINGERPRINT_MAX, color=FILL, lw=0, zorder=0)
        ax.axhline(1, color=INK2, lw=0.6, ls=(0, (3, 2)), zorder=1)
        ax.axhline(5, color=INK2, lw=0.4, ls=(0, (1, 2)), zorder=1)
        # bootstrap interval as a thin whisker
        lo = p.LR_pos_boot_lo.fillna(p.LR_pos_lo)
        hi = p.LR_pos_boot_hi.fillna(p.LR_pos_hi)
        ax.vlines(p.centre, lo, hi, color=col, lw=0.6, alpha=0.5, zorder=2)
        ax.scatter(p.centre, p.LR_pos, s=16, color=col, edgecolor="white", lw=0.5, zorder=3)
        ax.set_yscale("log")
        ax.set_ylim(0.3, 400)
        ax.set_yticks([0.5, 1, 2, 5, 10, 50, 100])
        ax.set_yticklabels(["0.5", "1", "2", "5", "10", "50", "100"])
        ax.grid(axis="y", color=GRID, lw=0.5)
        ax.set_ylabel("LR+ (log scale)")
        fp = p[p.wn_max <= FINGERPRINT_MAX].LR_pos.median()
        hi_med = p[p.wn_min >= DIAGNOSTIC_MIN].LR_pos.median()
        ax.set_title(f"{name}, {len(p)} powered rules", loc="left")
        ax.text(875, 0.36, f"fingerprint (window at or below {int(FINGERPRINT_MAX)} cm$^{{-1}}$)\nmedian LR+ {fp:.2f}",
                fontsize=7, color=INK2, ha="center", va="bottom")
        ax.text(2750, 0.36, f"at or above {int(DIAGNOSTIC_MIN)} cm$^{{-1}}$: median LR+ {hi_med:.2f}",
                fontsize=7, color=INK2, ha="center", va="bottom")
        ax.text(3980, 1.08, "LR+ = 1 (no information)", fontsize=6.5, color=INK2, ha="left", va="bottom")
        ax.text(3980, 5.3, "LR+ = 5", fontsize=6.5, color=INK2, ha="left", va="bottom")
        # direct labels for the strongest rules
        top = p.sort_values("LR_pos", ascending=False).head(3)
        for k, (_, r) in enumerate(top.iterrows()):
            ax.annotate(short_label(r.rule_id), (r.centre, min(r.LR_pos, 250)), xytext=(5, -2 if k else 2),
                        textcoords="offset points", fontsize=6.5, color=INK2, va="center")
        note(f"Fig1 {name}: n_powered={len(p)}, fingerprint median LR+={fp:.2f} "
             f"(n={int((p.wn_max <= FINGERPRINT_MAX).sum())}), >=1500 median LR+={hi_med:.2f} "
             f"(n={int((p.wn_min >= DIAGNOSTIC_MIN).sum())})")
    axes[1].set_xlabel("Centre of the published window (cm$^{-1}$)")
    axes[1].set_xlim(4000, 550)
    fig.align_ylabels(axes)
    fig.tight_layout(h_pad=1.0)
    save(fig, "fig1_lr_by_region")


# ----------------------------------------------------------------------------
# Figure 2: position only against the full rule definition
# ----------------------------------------------------------------------------
def fig2(mchem: pd.DataFrame, mnist: pd.DataFrame) -> None:
    rows = []
    for name, m in [("Chemotion", mchem), ("NIST", mnist)]:
        full = primary(m, "+shape").set_index("rule_id")
        pos = primary(m, "position").set_index("rule_id")
        common = full.index.intersection(pos.index)
        for rid in common:
            f, q = full.loc[rid], pos.loc[rid]
            if f.underpowered:
                continue
            if f.rule_intensity == "any" and f.rule_shape == "any":
                continue
            rows.append(dict(dataset=name, rule_id=rid, group=f.truth_group,
                             lr_pos=q.LR_pos, lr_full=f.LR_pos,
                             sens_pos=q.sensitivity, sens_full=f.sensitivity,
                             spec_pos=q.specificity, spec_full=f.specificity,
                             clause=f"{f.rule_intensity}" + ("" if f.rule_shape == "any" else f", {f.rule_shape}")))
    d = pd.DataFrame(rows)
    d.to_csv(PROCESSED / "fig2_position_vs_full.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(7.2, 6.2), sharey=False)
    for ax, (name, col) in zip(axes, [("Chemotion", CHEM), ("NIST", NIST)]):
        s = d[d.dataset == name].sort_values("lr_pos").reset_index(drop=True)
        y = np.arange(len(s))
        ax.axvline(1, color=INK2, lw=0.6, ls=(0, (3, 2)), zorder=1)
        ax.hlines(y, s.lr_pos, s.lr_full, color=col, lw=1.2, alpha=0.6, zorder=2)
        ax.scatter(s.lr_pos, y, s=18, facecolor="white", edgecolor=col, lw=1.0, zorder=3, label="position only")
        ax.scatter(s.lr_full, y, s=18, color=col, edgecolor="white", lw=0.5, zorder=4, label="with intensity clause")
        ax.set_yticks(y)
        ax.set_yticklabels([f"{short_label(r)}  ({c})" for r, c in zip(s.rule_id, s.clause)], fontsize=6.5)
        ax.set_xscale("log")
        ax.set_xlim(0.3, 500)
        ax.set_xticks([1, 10, 100])
        ax.set_xticklabels(["1", "10", "100"])
        ax.set_xticks([0.5, 2, 5, 20, 50, 200], minor=True)
        ax.set_xticklabels([], minor=True)
        ax.grid(axis="x", which="major", color=GRID, lw=0.5)
        ax.set_xlabel("LR+ (log scale)")
        ax.set_title(f"{name}: {len(s)} rules with an intensity clause", loc="left", fontsize=8)
        ax.tick_params(axis="y", length=0)
        ax.set_ylim(-0.7, len(s) - 0.3)
        from matplotlib.transforms import blended_transform_factory
        tr = blended_transform_factory(ax.transAxes, ax.transData)
        ax.set_title(f"{name}: {len(s)} rules with an intensity clause", loc="left", fontsize=8, pad=16)
        ax.text(1.02, len(s) - 0.3, "sensitivity\nposition \u2192 full", fontsize=6, color=INK2, va="bottom", ha="left",
                transform=tr)
        for yy, (_, r) in zip(y, s.iterrows()):
            ax.text(1.02, yy, f"{r.sens_pos:.2f} \u2192 {r.sens_full:.2f}", fontsize=6, color=INK2,
                    va="center", transform=tr)
        gain = (s.lr_full > s.lr_pos * 1.2).sum()
        loss_sens = (s.sens_full < s.sens_pos * 0.5).sum()
        note(f"Fig2 {name}: {len(s)} clause rules; LR+ up by >20% in {gain}; sensitivity halved or worse in {loss_sens}; "
             f"median sens position {s.sens_pos.median():.2f} full {s.sens_full.median():.2f}")
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 0.0))
    fig.tight_layout(w_pad=7, rect=(0, 0.04, 0.97, 1))
    save(fig, "fig2_position_vs_full")


# ----------------------------------------------------------------------------
# Figure 3: the nitrile band
# ----------------------------------------------------------------------------
def nitrile_bands(suf: str) -> pd.DataFrame:
    inv = pd.read_csv(PROCESSED / f"inventory{suf}.csv", low_memory=False).set_index("file_id")
    meta = pd.read_csv(PROCESSED / f"spectra_meta{suf}.csv")
    if suf == "":
        meta = meta[meta.split == "confirm"]
    main = meta[(meta.is_multifragment == False) & (meta.has_unusual_elements == False)].file_id  # noqa: E712
    bands = pd.read_csv(PROCESSED / f"bands{suf}.csv")
    bands = bands[bands.file_id.isin(main) & (bands.prominence_rel >= PRIMARY_PROM)]
    nit = inv.loc[inv.index.isin(main)]
    nit = nit[nit.fg_nitrile_saturated.astype(bool) | nit.fg_nitrile_aromatic.astype(bool)]
    rows = []
    for fid, r in nit.iterrows():
        b = bands[(bands.file_id == fid) & (bands.position_cm >= 2190) & (bands.position_cm <= 2280)]
        kind = "aromatic" if r.fg_nitrile_aromatic else "saturated"
        if len(b) == 0:
            rows.append(dict(file_id=fid, kind=kind, detected=False, height=0.0, position=np.nan, fwhm=np.nan))
        else:
            top = b.sort_values("height_rel", ascending=False).iloc[0]
            rows.append(dict(file_id=fid, kind=kind, detected=True, height=top.height_rel,
                             position=top.position_cm, fwhm=top.fwhm_cm))
    return pd.DataFrame(rows)


def fig3() -> None:
    dc = nitrile_bands("")
    dn = nitrile_bands("_nist")
    dc["dataset"], dn["dataset"] = "Chemotion", "NIST"
    d = pd.concat([dc, dn], ignore_index=True)
    d.to_csv(PROCESSED / "fig3_nitrile_bands.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(6.5, 2.9))
    # (a) height of the nitrile band relative to the strongest band, as a survival curve
    ax = axes[0]
    xs = np.linspace(0, 1, 201)
    for name, col in [("Chemotion", CHEM), ("NIST", NIST)]:
        s = d[(d.dataset == name)]
        frac = [(s.height >= x).mean() for x in xs]
        ax.plot(xs, frac, color=col, lw=1.6, label=f"{name} (n = {len(s)})")
    ax.axvline(0.6, color=INK2, lw=0.6, ls=(0, (3, 2)))
    ax.axvline(0.2, color=INK2, lw=0.6, ls=(0, (1, 2)))
    ax.text(0.61, 0.62, "\"strong\"\n(\u2265 0.6)", fontsize=6.5, color=INK2, va="top")
    ax.text(0.21, 0.62, "\"medium\"\n(\u2265 0.2)", fontsize=6.5, color=INK2, va="top")
    ax.set_xlabel("Relative height h of the C\u2261N band")
    ax.set_ylabel("Fraction of nitriles with a band of height \u2265 h")
    ax.set_ylim(0, 1.02)
    ax.set_xlim(0, 1)
    ax.set_title("(a) Intensity", loc="left")
    ax.legend(frameon=False, loc="upper right")
    ax.grid(axis="y", color=GRID, lw=0.5)
    # (b) apex position, by class, against the two published windows
    ax = axes[1]
    ax.axvspan(2220, 2240, color=FILL, lw=0)
    ax.axvspan(2240, 2260, color="#e0dfda", lw=0)
    ax.text(2230, 3.85, "aromatic 2220–2240", ha="center", va="top", fontsize=6.5, color=INK2)
    ax.text(2250, 3.45, "saturated 2240–2260", ha="center", va="top", fontsize=6.5, color=INK2)
    rng = np.random.default_rng(1)
    levels = [("Chemotion", "aromatic", CHEM, 2.6), ("Chemotion", "saturated", CHEM, 2.0),
              ("NIST", "aromatic", NIST, 1.2), ("NIST", "saturated", NIST, 0.6)]
    labels = []
    for name, kind, col, yy in levels:
        s = d[(d.dataset == name) & (d.kind == kind) & d.detected]
        jit = rng.uniform(-0.18, 0.18, len(s))
        ax.scatter(s.position, yy + jit, s=9, color=col, alpha=0.55, edgecolor="none")
        labels.append((yy, f"{name} {kind} (n = {len(s)})"))
        lo, hi = (2220, 2240) if kind == "aromatic" else (2240, 2260)
        inside = ((s.position >= lo) & (s.position <= hi)).mean() if len(s) else float("nan")
        note(f"Fig3 {name} {kind}: n_detected={len(s)}, inside own window {inside:.2f}, "
             f"apex median {s.position.median():.0f}, IQR {s.position.quantile(.25):.0f}-{s.position.quantile(.75):.0f}")
    ax.set_yticks([lv[0] for lv in labels])
    ax.set_yticklabels([lv[1] for lv in labels], fontsize=6.5)
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(2300, 2170)
    ax.set_ylim(0.1, 3.9)
    ax.set_xlabel("Apex of the C≡N band (cm$^{-1}$)")
    ax.set_title("(b) Position", loc="left")
    for name in ("Chemotion", "NIST"):
        s = d[d.dataset == name]
        det = s.detected.mean()
        strong = (s.height >= 0.6).mean()
        med = s[s.detected].height.median()
        note(f"Fig3 {name}: nitriles={len(s)}, detected at prominence>=0.02: {det:.2f}, "
             f"height median {med:.2f} (IQR {s[s.detected].height.quantile(.25):.2f}-{s[s.detected].height.quantile(.75):.2f}), "
             f"'strong' (>=0.6) share {strong:.2f}")
    fig.tight_layout(w_pad=2)
    save(fig, "fig3_nitrile")


# ----------------------------------------------------------------------------
# Figure 4: benzene substitution patterns
# ----------------------------------------------------------------------------
BENZENE = [
    ("SMITH-BR4-BZ-MONO-OOP", "mono: wag 710–770"),
    ("SMITH-BR4-BZ-MONO-690", "mono: ring bend 680–700"),
    ("SMITH-BR4-BZ-MONO-BOTH", "mono: wag and ring bend"),
    ("SMITH-BR4-BZ-ORTHO-OOP", "ortho: wag 735–770, no 690"),
    ("SMITH-BR4-BZ-META-OOP", "meta: wag 750–810"),
    ("SMITH-BR4-BZ-META-690", "meta: ring bend 680–700"),
    ("SMITH-BR4-BZ-META-BOTH", "meta: wag and ring bend"),
    ("SMITH-BR4-BZ-PARA-OOP", "para: wag 790–860, no 690"),
]


def fig4(chem: pd.DataFrame, nist: pd.DataFrame) -> None:
    c = chem.set_index("rule_id")
    n = nist.set_index("rule_id")
    ids = [r for r, _ in BENZENE if r in c.index]
    fig, axes = plt.subplots(1, 2, figsize=(6.5, 2.9), sharey=True)
    y = np.arange(len(ids))[::-1]
    for ax, (name, m, col, metric) in zip(axes, [("LR+ (rule in)", None, None, "LR_pos"), ("LR− (rule out)", None, None, "LR_neg")]):
        ax.axvline(1, color=INK2, lw=0.6, ls=(0, (3, 2)), zorder=1)
        for src, mm, cc, off in [("Chemotion", c, CHEM, 0.16), ("NIST", n, NIST, -0.16)]:
            v = mm.loc[ids, metric]
            lo = mm.loc[ids, f"{metric}_boot_lo"].fillna(mm.loc[ids, f"{metric}_lo"]) if f"{metric}_boot_lo" in mm else mm.loc[ids, f"{metric}_lo"]
            hi = mm.loc[ids, f"{metric}_boot_hi"].fillna(mm.loc[ids, f"{metric}_hi"]) if f"{metric}_boot_hi" in mm else mm.loc[ids, f"{metric}_hi"]
            ax.hlines(y + off, lo, hi, color=cc, lw=0.8, alpha=0.6, zorder=2)
            ax.scatter(v, y + off, s=18, color=cc, edgecolor="white", lw=0.5, zorder=3, label=src)
        ax.set_xscale("log")
        ax.set_xlabel(name)
        ax.grid(axis="x", color=GRID, lw=0.5)
        if metric == "LR_pos":
            ax.set_xlim(0.3, 20)
            ax.set_xticks([0.5, 1, 2, 5, 10])
            ax.set_xticklabels(["0.5", "1", "2", "5", "10"])
        else:
            ax.set_xlim(0.05, 3)
            ax.set_xticks([0.1, 0.2, 0.5, 1, 2])
            ax.set_xticklabels(["0.1", "0.2", "0.5", "1", "2"])
    axes[0].set_yticks(y)
    axes[0].set_yticklabels([lab for r, lab in BENZENE if r in c.index], fontsize=7)
    axes[0].tick_params(axis="y", length=0)
    axes[0].legend(frameon=False, loc="upper right", handletextpad=0.2)
    for rid in ids:
        note(f"Fig4 {rid}: Chemotion LR+ {c.loc[rid, 'LR_pos']:.2f} (n+ {c.loc[rid, 'n_pos']}) LR- {c.loc[rid, 'LR_neg']:.2f}; "
             f"NIST LR+ {n.loc[rid, 'LR_pos']:.2f} (n+ {n.loc[rid, 'n_pos']}) LR- {n.loc[rid, 'LR_neg']:.2f}")
    fig.tight_layout(w_pad=1.5)
    save(fig, "fig4_benzene")


# ----------------------------------------------------------------------------
# Figure 5: Chemotion against NIST
# ----------------------------------------------------------------------------
def fig5(comp: pd.DataFrame) -> None:
    d = comp[(comp.tier == "group") & (~comp.chem_underpowered) & (~comp.nist_underpowered)].copy()
    from scipy.stats import spearmanr
    rho = spearmanr(d.chem_LR_pos, d.nist_LR_pos).statistic
    ratio = d.nist_LR_pos / d.chem_LR_pos
    within2 = ((ratio >= 0.5) & (ratio <= 2)).mean()
    note(f"Fig5: {len(d)} rules powered in both; Spearman rho {rho:.2f}; within factor 2: {within2:.2f} ({int(((ratio >= 0.5) & (ratio <= 2)).sum())})")

    fig, ax = plt.subplots(figsize=(4.4, 4.4))
    lim = (0.4, 300)
    xx = np.array(lim)
    ax.fill_between(xx, xx / 2, xx * 2, color=FILL, lw=0, zorder=0)
    ax.plot(xx, xx, color=INK2, lw=0.6, ls=(0, (3, 2)), zorder=1)
    ax.axhline(1, color=GRID, lw=0.6, zorder=1)
    ax.axvline(1, color=GRID, lw=0.6, zorder=1)
    fp = d.wn_max <= FINGERPRINT_MAX
    ax.scatter(d.chem_LR_pos[fp], d.nist_LR_pos[fp], s=18, facecolor="white", edgecolor=THIRD, lw=1.0, zorder=3,
               label=f"fingerprint window (n = {int(fp.sum())})")
    ax.scatter(d.chem_LR_pos[~fp], d.nist_LR_pos[~fp], s=18, color=THIRD, edgecolor="white", lw=0.5, zorder=3,
               label=f"window above 1350 cm$^{{-1}}$ (n = {int((~fp).sum())})")
    out = d[(ratio < 0.5) | (ratio > 2)]
    offsets = {"secondary alkyl amine N-H": (4, 22, "left"), "sat. acid C=O": (6, 58, "left"),
               "terminal alkyne C\u2261C": (8, 2, "left"),
               "arom. aldehyde C=O": (52, -34, "left"), "primary aryl amine, NH2 asym.": (6, 9, "left"),
               "primary alkyl amine, NH2 asym.": (6, -9, "left"), "ortho benzene, wag": (40, -40, "left")}
    for _, r in out.iterrows():
        lab = short_label(r.rule_id)
        dx, dy, ha = offsets.get(lab, (5, 3, "left"))
        arrow = dict(arrowstyle="-", color=INK2, lw=0.5, shrinkA=0, shrinkB=2) if abs(dx) + abs(dy) > 16 else None
        ax.annotate(lab, (r.chem_LR_pos, r.nist_LR_pos), xytext=(dx, dy), ha=ha, va="center",
                    textcoords="offset points", fontsize=6, color=INK2, arrowprops=arrow)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(lim); ax.set_ylim(lim)
    ticks = [0.5, 1, 2, 5, 10, 50, 100]
    ax.set_xticks(ticks); ax.set_xticklabels([str(t) for t in ticks])
    ax.set_yticks(ticks); ax.set_yticklabels([str(t) for t in ticks])
    ax.set_xlabel("LR+ in Chemotion (ATR)")
    ax.set_ylabel("LR+ in NIST WebBook (transmission)")
    ax.text(0.45, 200, f"{len(d)} rules powered in both sets\nSpearman ρ = {rho:.2f}\n{within2 * 100:.0f}% agree within a factor of 2 (shaded)",
            fontsize=7, color=INK, va="top")
    ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.0, 0.84))
    ax.set_aspect("equal")
    fig.tight_layout()
    save(fig, "fig5_replication")


# ----------------------------------------------------------------------------
# Numbers quoted in the text that belong to no figure
# ----------------------------------------------------------------------------
def crowding_numbers() -> None:
    """Bands per spectrum in the fingerprint and share of 50 cm-1 windows occupied."""
    for suf, name in (("", "Chemotion"), ("_nist", "NIST")):
        meta = pd.read_csv(PROCESSED / f"spectra_meta{suf}.csv")
        if suf == "":
            meta = meta[meta.split == "confirm"]
        main = set(meta[(meta.is_multifragment == False) & (meta.has_unusual_elements == False)].file_id)  # noqa: E712
        b = pd.read_csv(PROCESSED / f"bands{suf}.csv")
        b = b[b.file_id.isin(main) & (b.prominence_rel >= PRIMARY_PROM)]
        fp = b[(b.position_cm >= 700) & (b.position_cm <= FINGERPRINT_MAX)]
        per = fp.groupby("file_id").size().reindex(list(main), fill_value=0)
        hi = b[b.position_cm >= DIAGNOSTIC_MIN].groupby("file_id").size().reindex(list(main), fill_value=0)
        edges = np.arange(700, FINGERPRINT_MAX + 1, 50)
        occ = np.zeros(len(main))
        for k, (_, g) in enumerate(fp.groupby("file_id")):
            h, _ = np.histogram(g.position_cm, bins=edges)
            occ[k] = (h > 0).mean()
        note(f"Crowding {name}: bands 700-{int(FINGERPRINT_MAX)} per spectrum median {per.median():.0f} "
             f"(IQR {per.quantile(.25):.0f}-{per.quantile(.75):.0f}); bands >= {int(DIAGNOSTIC_MIN)} median {hi.median():.0f}; "
             f"share of 50 cm-1 windows occupied, median {np.median(occ):.2f}")


def benzene_690_shares() -> None:
    """Share of compounds with a detected band at 680-700 cm-1, by substitution pattern."""
    for suf, name in (("", "Chemotion"), ("_nist", "NIST")):
        meta = pd.read_csv(PROCESSED / f"spectra_meta{suf}.csv")
        if suf == "":
            meta = meta[meta.split == "confirm"]
        main = meta[(meta.is_multifragment == False) & (meta.has_unusual_elements == False)].file_id  # noqa: E712
        inv = pd.read_csv(PROCESSED / f"inventory{suf}.csv", low_memory=False).set_index("file_id")
        inv = inv[inv.index.isin(main)]
        b = pd.read_csv(PROCESSED / f"bands{suf}.csv")
        has = set(b[b.file_id.isin(main) & (b.prominence_rel >= PRIMARY_PROM)
                    & (b.position_cm >= 680) & (b.position_cm <= 700)].file_id)
        parts = [f"aromatic share {inv.fg_aromatics.astype(bool).mean():.2f}"]
        for g in ("fg_aromatic_mono", "fg_aromatic_ortho", "fg_aromatic_para"):
            pos = inv[inv[g].astype(bool)].index.isin(has).mean()
            neg = inv[~inv[g].astype(bool)].index.isin(has).mean()
            parts.append(f"{g[12:]}: with 690 band {pos:.2f} vs others {neg:.2f}")
        note(f"Benzene {name}: " + "; ".join(parts))


def main() -> int:
    mchem = pd.read_csv(PROCESSED / "rule_metrics_confirm.csv")
    mnist = pd.read_csv(PROCESSED / "rule_metrics_nist_confirm.csv")
    comp = pd.read_csv(PROCESSED / "rule_metrics_comparison.csv")
    chem, nist = primary(mchem), primary(mnist)
    print("[figures] figure 1"); fig1(chem, nist)
    print("[figures] figure 2"); fig2(mchem, mnist)
    print("[figures] figure 3"); fig3()
    print("[figures] figure 4"); fig4(chem, nist)
    print("[figures] figure 5"); fig5(comp)
    print("[figures] crowding"); crowding_numbers()
    print("[figures] benzene 690"); benzene_690_shares()
    (FIG / "figure_numbers.md").write_text("# Numbers behind the figures\n\n" + "\n".join(f"- {s}" for s in NOTES) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
