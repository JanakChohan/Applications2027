"""Explainer charts for the beginner study guide (risk and catalysts). Same validated palette as scripts/13_charts.py."""
import os, json, datetime as dt, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt; import matplotlib.dates as mdates
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); D = os.path.join(ROOT, "data", "derived"); OUT = os.path.join(ROOT, "charts")
F = json.load(open(os.path.join(D, "facts.json"))); R = json.load(open(os.path.join(D, "revenue_at_risk.json")))
BLUE, ORANGE, TEAL, GREY, INK, MUTED, RED, NAVY = "#2a78d6", "#d97706", "#0e9f8e", "#9aa0a6", "#1f2328", "#5f6368", "#c5362f", "#1F3864"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": "#c7c9cc", "xtick.color": MUTED, "ytick.color": MUTED,
                     "figure.dpi": 200, "text.parse_math": False, "axes.titlesize": 11.5, "axes.titleweight": "bold", "axes.titlecolor": INK, "axes.titlelocation": "left", "legend.frameon": False})
# ---------- 17 catalyst timeline ----------
fig, ax = plt.subplots(figsize=(9.6, 4.3)); d = lambda s: dt.datetime.strptime(s, "%Y-%m-%d")
ax.axhline(0, color=INK, lw=1.4, zorder=1)
ax.axvspan(d("2026-11-26"), d("2027-08-05"), ymin=0.47, ymax=0.53, color=ORANGE, alpha=0.25, zorder=0)
ev = [("2026-12-01", "1 Dec\nInvestor conference\n(first holiday read)", 1.0, False), ("2027-02-11", "~11 Feb\nQ4 results +\nfirst 2027 guidance", 2.1, True), ("2027-04-29", "Late Apr\nQ1 results", 1.0, False),
      ("2027-07-29", "Late Jul\nQ2 results", 1.0, False), ("2027-10-14", "~Oct\nTeen survey", -1.25, False), ("2027-10-28", "Late Oct\nQ3 results:\nthe fog lifts", 2.1, True), ("2027-11-20", "Nov\nBank facility\ndue for renewal", -2.4, False), ("2027-12-31", "Dec 2027\nOur price-\ntarget date", 1.0, False)]
for date, label, h, key in ev:
    x = d(date); c = BLUE if key else GREY
    ax.plot([x, x], [0, h], color=c, lw=1.6 if key else 1.1, zorder=2); ax.scatter([x], [0], s=130 if key else 60, color=c, zorder=3, edgecolor="white", linewidth=1.5)
    ax.text(x, h + (0.12 if h > 0 else -0.12), label, ha="center", va="bottom" if h > 0 else "top", fontsize=8.6, color=INK, fontweight="bold" if key else None, linespacing=1.25)
ax.text(d("2027-03-30"), -0.38, "Until Q3 2027: North America sales look worse than they are (accounting change)", ha="center", va="top", fontsize=8.3, color="#8a4b00")
ax.annotate("", xy=(d("2027-12-28"), -3.95), xytext=(d("2026-11-28"), -3.95), arrowprops=dict(arrowstyle="-", color=TEAL, lw=5, alpha=0.55))
ax.text(d("2027-06-14"), -4.3, "All year: share buybacks (about $600m a year) and the tariff court case (could land any time)", ha="center", va="top", fontsize=8.6, color="#0a6e63")
ax.set_ylim(-5.0, 3.9); ax.set_xlim(d("2026-11-10"), d("2028-01-20")); ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2)); ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.set_yticks([]); ax.set_xticks([]); ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
ax.set_title("The next 13 months: when we find out who is right (blue = the two that matter most)")
fig.tight_layout(rect=[0, 0.03, 1, 1]); fig.text(0.01, 0.01, "Source: company guidance and filings; dates for results are estimates until Crocs confirms them. Probabilities and sizing are in the guide.", fontsize=6.8, color=MUTED)
fig.savefig(os.path.join(OUT, "17_catalyst_timeline.png"), bbox_inches="tight", facecolor="white"); plt.close(fig)
# ---------- 18 why profit falls faster than sales ----------
t = R["ttm"]; a = R["assumptions"]; rev0 = t["revenue"]; cogs0 = rev0 - t["adj_gross_profit"]; sga0 = t["adj_sga"]
fixed = a["dist_cost"] * a["dist_fixed_share"] + sga0 * a["sga_fixed_share"]; var0 = cogs0 + sga0 - fixed; ebit0 = rev0 - var0 - fixed
rev1 = F["rar"]["rev1"]; ebit1 = F["rar"]["ebit1"]; var1 = rev1 - fixed - ebit1
fig, ax = plt.subplots(figsize=(8.2, 4.4)); xs = [0, 1]; w = 0.82
for x, (v, f_, e, r) in zip(xs, [(var0, fixed, ebit0, rev0), (var1, fixed, ebit1, rev1)]):
    ax.bar(x, v, w, color="#d5d8dc", edgecolor="white", linewidth=2); ax.bar(x, f_, w, bottom=v, color="#8b9096", edgecolor="white", linewidth=2); ax.bar(x, e, w, bottom=v + f_, color=BLUE, edgecolor="white", linewidth=2)
    ax.text(x, v / 2, f"Costs that shrink with sales\n(making and shipping shoes)\n${v:,.0f}m", ha="center", va="center", fontsize=8.4, color=INK)
    ax.text(x, v + f_ / 2, f"Costs that do NOT shrink\n(stores, staff, IT)\n${f_:,.0f}m", ha="center", va="center", fontsize=8.4, color="white")
    ax.text(x, v + f_ + e / 2, f"Profit ${e:,.0f}m", ha="center", va="center", fontsize=9.2, color="white", fontweight="bold")
    ax.text(x, r + 70, f"Sales ${r:,.0f}m", ha="center", fontsize=9.5, fontweight="bold", color=INK)
ax.annotate("", xy=(0.62, rev1 + 330), xytext=(0.38, rev0 + 330), arrowprops=dict(arrowstyle="->", color=RED, lw=1.6))
ax.text(1.5, 3300, f"Sales down {abs(rev1/rev0-1)*100:.0f}%", fontsize=10, color=RED, fontweight="bold", va="center"); ax.text(1.5, 2750, f"Profit down {abs(ebit1/ebit0-1)*100:.0f}%", fontsize=10, color=RED, fontweight="bold", va="center")
ax.text(1.5, 2050, f"Profit per share\ndown {abs(F['rar']['eps1']/F['rar']['eps0']-1)*100:.0f}%", fontsize=10, color=RED, fontweight="bold", va="center")
ax.set_xticks(xs); ax.set_xticklabels(["Today\n(last 12 months)", "If the fad unwinds\n(our stress test)"], fontsize=9.5); ax.set_xlim(-0.5, 2.25); ax.set_ylim(0, 4900); ax.set_yticks([]); ax.spines["left"].set_visible(False)
ax.set_title("Why losing 16% of sales would cost almost half the profit")
fig.tight_layout(rect=[0, 0.05, 1, 1]); fig.text(0.01, 0.01, "Source: Crocs earnings releases (last 12 months to Sep-2026); cost split and stress are our estimates (model.xlsx, RevAtRisk).\nProfit = adjusted operating profit. The stressed case also includes $51m of extra discounting.", fontsize=6.8, color=MUTED)
fig.savefig(os.path.join(OUT, "18_operating_leverage.png"), bbox_inches="tight", facecolor="white"); plt.close(fig)
# ---------- 19 three scenarios ----------
V = F["valuation"]; price = F["price"]; fig, ax = plt.subplots(figsize=(8.2, 3.7))
rows = [("Bull case", V["pt"][2], "25% chance", TEAL), ("Base case", V["pt"][1], "50% chance", BLUE), ("Bear case", V["pt"][0], "25% chance", ORANGE), ("Worst case: full fad unwind\n(a tail inside the bear case)", F["rar"]["val"], "", RED)]
for i, (n, v, pr, c) in enumerate(rows):
    ax.barh(i, v, color=c, height=0.55, alpha=0.9 if i < 3 else 0.6); ax.text(v + 5, i, f"${v:,.0f}  ({(v/price-1)*100:+.0f}%)", va="center", fontsize=10, fontweight="bold", color=INK, bbox=dict(fc="white", ec="none", pad=1.5), zorder=5); ax.text(6, i, pr, va="center", fontsize=8.5, color="white")
ax.axvline(price, color=INK, lw=1.3, ls="--"); ax.text(price, -0.62, f"Today's price ${price:.0f}", ha="center", fontsize=9, fontweight="bold")
ax.axvline(V["pt"][3], color=NAVY, lw=1.3, ls=":"); ax.text(V["pt"][3] + 3, 3.55, f"Average of the three, weighted by chance: ${V['pt'][3]:.0f}", ha="left", fontsize=8.8, color=NAVY, fontweight="bold")
ax.set_yticks(range(4)); ax.set_yticklabels([r[0] for r in rows], fontsize=9.5); ax.invert_yaxis(); ax.set_xlim(0, 345); ax.set_ylim(3.85, -0.95); ax.set_xlabel("Share price in December 2027 (US$)", fontsize=9, color=MUTED); ax.xaxis.grid(True, color="#e8eaed"); ax.set_axisbelow(True)
ax.set_title("Three possible futures for the share price")
fig.tight_layout(rect=[0, 0.04, 1, 1]); fig.text(0.01, 0.01, "Source: our estimates (model.xlsx). Probabilities are judgement calls, not facts.", fontsize=6.8, color=MUTED)
fig.savefig(os.path.join(OUT, "19_scenarios_simple.png"), bbox_inches="tight", facecolor="white"); plt.close(fig)
json.dump({"fixed": fixed, "var0": var0, "var1": var1, "ebit0": ebit0, "ebit1": ebit1, "rev0": rev0, "rev1": rev1}, open(os.path.join(D, "study_stats.json"), "w"), indent=1)
print("ok", round(fixed), round(var0), round(var1), round(ebit0), round(ebit1))
