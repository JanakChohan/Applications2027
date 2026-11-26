"""Chart pack (PNG, 2x) for the deck and memo. Every chart carries its own source line.
Palette validated with the dataviz skill validator (light mode): blue/orange/teal/violet + neutral grey."""
import os, json, numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt; import matplotlib.dates as mdates
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); D = os.path.join(ROOT, "data", "derived"); OUT = os.path.join(ROOT, "charts")
BLUE, ORANGE, TEAL, VIOLET, GREY, INK, MUTED, RED = "#2a78d6", "#d97706", "#0e9f8e", "#7c5cd6", "#9aa0a6", "#1f2328", "#5f6368", "#c5362f"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": "#c7c9cc", "axes.labelcolor": MUTED,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.grid": True, "grid.color": "#e8eaed", "grid.linewidth": 0.8, "axes.axisbelow": True, "figure.dpi": 200,
                     "text.parse_math": False, "axes.titlesize": 11.5, "axes.titleweight": "bold", "axes.titlecolor": INK, "axes.titlelocation": "left", "legend.frameon": False})
A = pd.read_csv(os.path.join(D, "annual.csv"), index_col=0); Q = pd.read_csv(os.path.join(D, "quarterly.csv"), index_col=0)
P = pd.read_csv(os.path.join(D, "prices.csv"), index_col=0, parse_dates=True); PE = pd.read_csv(os.path.join(D, "pe_history.csv"), index_col=0, parse_dates=True)
M = json.load(open(os.path.join(D, "model_outputs.json"))); RISK = json.load(open(os.path.join(D, "risk_stats.json"))); RT = pd.read_csv(os.path.join(D, "revenue_at_risk.csv"))
RAR = json.load(open(os.path.join(D, "revenue_at_risk.json"))); PEERS = pd.read_csv(os.path.join(D, "peers.csv"), index_col=0); ER = pd.read_csv(os.path.join(D, "earnings_reactions.csv"))
def save(fig, name, s):
    nl = s.count("\n") + 1; h = fig.get_figheight()
    fig.tight_layout(rect=[0, (0.10 + 0.13 * nl) / h, 1, 1])
    fig.text(0.01, 0.012, s, fontsize=6.8, color=MUTED, ha="left", va="bottom")
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", facecolor="white"); plt.close(fig)
def lab(ax, bars, fmt="{:.0f}", dy=3, color=INK, size=8):
    for b in bars:
        h = b.get_height()
        if np.isfinite(h): ax.annotate(fmt.format(h + 0.0 if abs(h) >= 0.5 or "." in fmt.format(h).replace("-0", "") else 0.0), (b.get_x() + b.get_width() / 2, h), xytext=(0, dy if h >= 0 else -dy - 8), textcoords="offset points", ha="center", fontsize=size, color=color)
S = M["scen"]["Base"]
# 1 revenue by brand ----------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.2, 3.6)); yrs = [2021, 2022, 2023, 2024, 2025]; x = list(range(len(yrs) + 2)); lbl = [f"FY{y%100}" for y in yrs] + ["FY26E", "FY27E"]
na = list(A.loc[yrs, "crocs_na"]) + [S["na"]["FY2026E"], S["na"]["FY2027E"]]; it = list(A.loc[yrs, "crocs_intl"]) + [S["intl"]["FY2026E"], S["intl"]["FY2027E"]]; hd = list(A.loc[yrs, "hd_rev"]) + [S["hd"]["FY2026E"], S["hd"]["FY2027E"]]
b1 = ax.bar(x, na, 0.62, color=BLUE, label="Crocs Brand - North America", edgecolor="white", linewidth=1.5); b2 = ax.bar(x, it, 0.62, bottom=na, color=TEAL, label="Crocs Brand - International", edgecolor="white", linewidth=1.5)
b3 = ax.bar(x, hd, 0.62, bottom=np.add(na, it), color=ORANGE, label="HEYDUDE", edgecolor="white", linewidth=1.5)
for i in x: ax.text(i, na[i] + it[i] + hd[i] + 60, f"{(na[i]+it[i]+hd[i])/1000:.2f}", ha="center", fontsize=8.5, color=INK, fontweight="bold")
for i in (5, 6):
    for b in (b1[i], b2[i], b3[i]): b.set_alpha(0.55)
ax.set_xticks(x); ax.set_xticklabels(lbl); ax.set_ylabel("US$ m"); ax.set_ylim(0, 5200); ax.legend(loc="upper left", fontsize=8, ncol=3); ax.set_title("Revenue by brand and region (US$ bn on top)")
save(fig, "01_revenue_mix.png", "Source: Crocs 10-K FY2021-FY2025 (reported); FY26E = company guidance split by my estimate; FY27E = my base case. As of 2026-11-26.")
# 2 margins -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.2, 3.4)); xs = lbl[:6]; gm = list(A.loc[yrs, "adj_gm_pct"]) + [np.nan]; om = list(A.loc[yrs, "adj_op_margin_pct"]) + [S["margin"]["FY2026E"] * 100]; sg = [g - o for g, o in zip(list(A.loc[yrs, "adj_gm_pct"]), list(A.loc[yrs, "adj_op_margin_pct"]))] + [np.nan]
ax.plot(xs, gm, color=BLUE, lw=2, marker="o", ms=5, label="Adjusted gross margin"); ax.plot(xs, om, color=ORANGE, lw=2, marker="o", ms=5, label="Adjusted operating margin"); ax.plot(xs, sg, color=GREY, lw=2, marker="o", ms=5, label="Adjusted SG&A % revenue (gross less operating)")
for xx, v in zip(xs, gm):
    if np.isfinite(v): ax.annotate(f"{v:.1f}", (xx, v), xytext=(0, 6), textcoords="offset points", ha="center", fontsize=8)
for xx, v in zip(xs, om): ax.annotate(f"{v:.1f}", (xx, v), xytext=(0, -13), textcoords="offset points", ha="center", fontsize=8)
for xx, v in zip(xs, sg):
    if np.isfinite(v): ax.annotate(f"{v:.1f}", (xx, v), xytext=(0, 6), textcoords="offset points", ha="center", fontsize=8)
ax.set_ylim(5, 70); ax.set_ylabel("% of revenue"); ax.legend(fontsize=8, loc="lower left", ncol=3); ax.set_title("Margins: gross margin held, SG&A deleverage took 5 points off operating margin")
save(fig, "02_margins.png", "Source: Crocs Q4 earnings releases (non-GAAP reconciliations), FY2021-FY2025 reported; FY26E operating margin = guidance ('expand modestly from 22.5%').")
# 3 EPS / FCF / shares small multiples ------------------------------------------------------
fig, axs = plt.subplots(1, 3, figsize=(9.6, 3.1)); xs = [f"FY{y%100}" for y in yrs] + ["FY26E"]
v = list(A.loc[yrs, "adj_eps"]) + [S["eps"]["FY2026E"]]; b = axs[0].bar(xs, v, color=BLUE, width=0.6); b[-1].set_alpha(0.55); lab(axs[0], b, "{:.2f}"); axs[0].set_title("Adjusted diluted EPS ($)")
v = list(A.loc[yrs, "fcf"]) + [Q.fcf_calc.tail(4).sum()]; b = axs[1].bar([f"FY{y%100}" for y in yrs] + ["TTM"], v, color=TEAL, width=0.6); lab(axs[1], b); axs[1].set_title("Free cash flow (US$ m)")
v = list(A.loc[yrs, "sh_diluted"]) + [S["sh_avg"]["FY2026E"]]; b = axs[2].bar(xs, v, color=VIOLET, width=0.6); b[-1].set_alpha(0.55); lab(axs[2], b, "{:.1f}"); axs[2].set_title("Average diluted shares (m)")
for a in axs: a.tick_params(axis="x", labelsize=8)
save(fig, "03_eps_fcf_shares.png", "Source: Crocs 10-K / earnings releases (reported). FY26E EPS and shares = my estimate inside company guidance ($14.45-14.65). FCF = CFO less capex; TTM to Sep-2026.")
# 4 Crocs brand NA vs Intl quarterly growth -------------------------------------------------
q8 = Q.tail(8); fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.3), gridspec_kw={"width_ratios": [1.25, 1]}); xi = np.arange(8); w = 0.38
b1 = axs[0].bar(xi - w / 2, q8.crocs_na_yoy_pct, w, color=BLUE, label="North America"); b2 = axs[0].bar(xi + w / 2, q8.crocs_intl_yoy_pct, w, color=TEAL, label="International")
lab(axs[0], b1, "{:.0f}", size=7.5); lab(axs[0], b2, "{:.0f}", size=7.5); axs[0].axhline(0, color=INK, lw=0.8); axs[0].set_xticks(xi); axs[0].set_xticklabels([p[2:4] + p[4:] for p in q8.index], fontsize=8)
axs[0].set_ylabel("y/y %"); axs[0].legend(fontsize=8, loc="upper left"); axs[0].set_title("Crocs Brand revenue growth by region"); axs[0].set_ylim(-14, 24)
sh = A.loc[yrs, "crocs_intl"] / A.loc[yrs, "crocs_rev"] * 100; t4 = Q.tail(4); sh_ttm = t4.crocs_intl.sum() / t4.crocs_rev.sum() * 100
b = axs[1].bar([f"FY{y%100}" for y in yrs] + ["TTM"], list(sh) + [sh_ttm], color=TEAL, width=0.6); lab(axs[1], b, "{:.0f}%"); axs[1].set_ylim(0, 65); axs[1].set_title("International share of Crocs Brand revenue")
save(fig, "04_crocs_brand.png", "Source: Crocs earnings releases and 10-Ks (reported). Q3-26 North America includes a ~2.7-pt DTC headwind from a marketplace moving to wholesale accounting. TTM to Sep-2026.")
# 5 Crocs brand segment margin + units/ASP -------------------------------------------------
fig, axs = plt.subplots(1, 3, figsize=(9.6, 3.0)); xs = [f"FY{y%100}" for y in yrs]
fig.suptitle("Crocs Brand: volume still growing, price flat, margin down 3 points since FY21", x=0.01, ha="left", fontsize=11.5, fontweight="bold", color=INK)
b = axs[0].bar(xs, A.loc[yrs, "crocs_op_margin_pct"], color=BLUE, width=0.6); lab(axs[0], b, "{:.1f}"); axs[0].set_title("Segment margin (%)"); axs[0].set_ylim(0, 45)
b = axs[1].bar(xs, A.loc[yrs, "crocs_units_k"] / 1000, color=BLUE, width=0.6); lab(axs[1], b, "{:.0f}"); axs[1].set_title("Pairs sold (m)"); axs[1].set_ylim(0, 150)
b = axs[2].bar(xs, A.loc[yrs, "crocs_asp"], color=BLUE, width=0.6); lab(axs[2], b, "{:.2f}"); axs[2].set_title("Average selling price ($)"); axs[2].set_ylim(0, 30)
save(fig, "05_crocs_units_asp.png", "Source: Crocs 10-K FY2022-FY2025 (reported). Segment margin is before unallocated enterprise corporate costs (~7% of revenue).")
# 6 HEYDUDE ------------------------------------------------------------------------------
fig, axs = plt.subplots(1, 3, figsize=(9.6, 3.1), gridspec_kw={"width_ratios": [1, 1.25, 1]}); y4 = [2022, 2023, 2024, 2025]; xs = ["FY22*", "FY23", "FY24", "FY25", "TTM"]
fig.suptitle("HEYDUDE: revenue down 27% from peak, wholesale now growing against easy comparisons", x=0.01, ha="left", fontsize=11.5, fontweight="bold", color=INK)
wv = list(A.loc[y4, "hd_whsl"]) + [t4.hd_whsl.sum()]; dv = list(A.loc[y4, "hd_dtc"]) + [t4.hd_dtc.sum()]
axs[0].bar(xs, wv, 0.6, color=ORANGE, label="Wholesale", edgecolor="white", linewidth=1.5); axs[0].bar(xs, dv, 0.6, bottom=wv, color="#f2b45c", label="DTC", edgecolor="white", linewidth=1.5)
for i in range(5): axs[0].text(i, wv[i] + dv[i] + 15, f"{wv[i]+dv[i]:.0f}", ha="center", fontsize=8, color=INK)
axs[0].legend(fontsize=7.5, loc="upper right", ncol=2); axs[0].set_title("Revenue (US$ m)"); axs[0].set_ylim(0, 1250); axs[0].tick_params(axis="x", labelsize=8)
b1 = axs[1].bar(xi - w / 2, q8.hd_whsl_yoy_pct, w, color=ORANGE, label="Wholesale"); b2 = axs[1].bar(xi + w / 2, q8.hd_dtc_yoy_pct, w, color="#f2b45c", label="DTC"); lab(axs[1], b1, "{:.0f}", size=7); lab(axs[1], b2, "{:.0f}", size=7)
axs[1].axhline(0, color=INK, lw=0.8); axs[1].set_xticks(xi); axs[1].set_xticklabels([p[2:4] + p[4:] for p in q8.index], fontsize=7.5); axs[1].set_ylim(-50, 25); axs[1].set_title("Growth by channel (y/y %)"); axs[1].legend(fontsize=7.5, loc="lower right")
b = axs[2].bar(["FY22*", "FY23", "FY24", "FY25"], A.loc[y4, "hd_op_margin_ex_impair_pct"], color=ORANGE, width=0.6); lab(axs[2], b, "{:.1f}"); axs[2].set_title("Segment margin ex-impairment (%)"); axs[2].set_ylim(0, 30)
save(fig, "06_heydude.png", "Source: Crocs 10-Ks, 10-Qs and earnings releases (reported). *FY22 from acquisition close on 17-Feb-2022. FY25 margin excludes the $737m impairment. TTM to Sep-2026.")
# 7 5-year price, annotated -------------------------------------------------------------
c = P.CROX.loc["2021-11-24":]; fig, ax = plt.subplots(figsize=(9.8, 4.4)); ax.plot(c.index, c.values, color=BLUE, lw=1.6)
ev = [("2021-12-23", "1", -11.6), ("2022-06-17", "2", None), ("2022-11-03", "3", 14.2), ("2023-04-27", "4", -15.9), ("2023-07-27", "5", -14.6), ("2024-01-08", "6", 20.3), ("2024-10-29", "7", -19.2),
      ("2025-02-13", "8", 23.9), ("2025-08-07", "9", -29.2), ("2026-02-12", "10", 19.0), ("2026-10-29", "11", 25.5)]
for d, n, mv in ev:
    d = pd.Timestamp(d); y = c.loc[d]; up = (mv is None) or mv > 0
    ax.annotate(n, (d, y), xytext=(0, 16 if up else -20), textcoords="offset points", ha="center", fontsize=8, fontweight="bold", color="white",
                bbox=dict(boxstyle="circle,pad=0.25", fc=(TEAL if up else RED), ec="white", lw=1), arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
ax.annotate(f"${c.iloc[-1]:.2f}", (c.index[-1], c.iloc[-1]), xytext=(6, 0), textcoords="offset points", fontsize=9, fontweight="bold", color=INK, va="center")
ax.set_ylabel("Share price (US$)"); ax.xaxis.set_major_locator(mdates.YearLocator()); ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y")); ax.set_xlim(c.index[0], c.index[-1] + pd.Timedelta(days=75)); ax.set_ylim(30, 190)
ax.set_title("CROX share price, five years to 25-Nov-2026: every big move was an earnings or guidance event")
save(fig, "07_price_5y.png", "Source: Nasdaq daily closes (CROX pays no dividend). Numbered events are listed on the slide; moves are close-to-close.")
# 8 P/E history -----------------------------------------------------------------------
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.5), gridspec_kw={"width_ratios": [1.3, 1]}); s = PE.CROX_pe_ntm.dropna(); d = PE.DECK_pe_ntm.dropna()
axs[0].plot(s.index, s.values, color=BLUE, lw=1.6, label="CROX"); axs[0].plot(d.index, d.values, color=ORANGE, lw=1.6, label="DECK")
axs[0].axhline(s.mean(), color=BLUE, lw=0.9, ls="--"); axs[0].text(s.index[0], s.mean() + 0.6, f"CROX 5y mean {s.mean():.1f}x", fontsize=7.5, color=MUTED)
axs[0].annotate(f"{s.iloc[-1]:.1f}x", (s.index[-1], s.iloc[-1]), xytext=(5, -9), textcoords="offset points", fontsize=8.5, fontweight="bold"); axs[0].annotate(f"{d.iloc[-1]:.1f}x", (d.index[-1], d.iloc[-1]), xytext=(5, 5), textcoords="offset points", fontsize=8.5, fontweight="bold")
axs[0].set_xlim(s.index[0], s.index[-1] + pd.Timedelta(days=110)); axs[0].legend(fontsize=8, loc="upper right"); axs[0].set_title("Forward P/E (next-four-quarter EPS)"); axs[0].xaxis.set_major_locator(mdates.YearLocator()); axs[0].xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
pr = PE.CROX_vs_DECK_ntm_prem_pct.dropna(); axs[1].fill_between(pr.index, pr.values, 0, color=BLUE, alpha=0.18); axs[1].plot(pr.index, pr.values, color=BLUE, lw=1.4)
axs[1].axhline(pr.median(), color=MUTED, lw=0.9, ls="--"); axs[1].text(pr.index[0], pr.median() - 7, f"median {pr.median():.0f}%", fontsize=7.5, color=MUTED)
axs[1].annotate(f"{pr.iloc[-1]:.0f}%", (pr.index[-1], pr.iloc[-1]), xytext=(4, 0), textcoords="offset points", fontsize=8.5, fontweight="bold", va="center"); axs[1].set_xlim(pr.index[0], pr.index[-1] + pd.Timedelta(days=150))
axs[1].set_title("CROX P/E premium (discount) to DECK, %"); axs[1].xaxis.set_major_locator(mdates.YearLocator()); axs[1].xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
save(fig, "08_pe_history.png", "Source: my calculation. Price (Nasdaq) / next-four-quarter EPS: actual reported EPS for past quarters (hindsight proxy for consensus), Nasdaq/Zacks consensus for future quarters.\nCROX adjusted EPS (press releases); DECK GAAP EPS (XBRL, split-adjusted). Broker forward-P/E history (Macrotrends) was not accessible.")
# 9 own history + vs index ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.2, 3.3)); names = ["CROX today", "CROX 5y median", "CROX 5y 25th-75th pct", "DECK today", "S&P 500 today", "S&P 500 10y avg"]
st = RISK["CROX_pe_ntm_5y_stats"]; vals = [RISK["crox_pe_ntm_now"], st["median"], None, RISK["deck_pe_ntm_now"], 18.3, 19.1]; cols = [BLUE, BLUE, BLUE, ORANGE, GREY, GREY]
for i, (n, v, cc) in enumerate(zip(names, vals, cols)):
    if v is None: ax.barh(i, st["p75"] - st["p25"], left=st["p25"], color=BLUE, alpha=0.35, height=0.55); ax.text(st["p75"] + 0.3, i, f"{st['p25']:.1f}x - {st['p75']:.1f}x", va="center", fontsize=8.5)
    else: ax.barh(i, v, color=cc, alpha=(1 if i in (0, 3, 4) else 0.55), height=0.55); ax.text(v + 0.3, i, f"{v:.1f}x", va="center", fontsize=8.5, fontweight="bold" if i == 0 else None)
ax.set_yticks(range(len(names))); ax.set_yticklabels(names); ax.invert_yaxis(); ax.set_xlim(0, 23); ax.grid(axis="y", visible=False); ax.set_title("Forward P/E: top quartile of its own range, still ~45% below the index")
save(fig, "09_pe_vs_history_index.png", "Source: CROX/DECK my calculation (see chart 8), May-2021 to Nov-2026; S&P 500 forward 12m P/E 18.3x and 10y average 19.1x from FactSet Earnings Insight, 13-Nov-2026.")
# 10 peers ---------------------------------------------------------------------------------
fig, axs = plt.subplots(1, 4, figsize=(9.8, 2.9)); tk = ["CROX", "DECK", "BIRK", "ONON"]; pc = [BLUE, ORANGE, TEAL, VIOLET]
for a, (key, ttl, fmt) in zip(axs, [("pe_fwd", "Forward P/E (x)", "{:.1f}"), ("ev_ebitda", "EV/EBITDA TTM (x)", "{:.1f}"), ("rev_growth_ttm_pct", "Revenue growth TTM (%)", "{:.1f}"), ("value_growth_score_ttm", "Value/Growth score\n(P/S / growth; low = good)", "{:.2f}")]):
    b = a.bar(tk, [PEERS.loc[key, t] for t in tk], color=pc, width=0.62); lab(a, b, fmt); a.set_title(ttl, fontsize=9.5); a.tick_params(axis="x", labelsize=8)
    a.set_ylim(0, max(PEERS.loc[key, t] for t in tk) * 1.22)
save(fig, "10_peers.png", "Source: StockAnalysis.com statistics pages as of 2026-11-25 close (one vendor methodology for all four); Value/Growth score = P/S TTM / TTM revenue growth %, my calculation.")
# 11 earnings reactions ---------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.6, 3.7)); xs = [f"{q[2:4]}{q[4:]}\n{d[5:]}" for q, d in zip(ER.quarter, ER.report_date.astype(str))]
b = ax.bar(xs, ER.day_move_pct, color=[TEAL if v > 0 else RED for v in ER.day_move_pct], width=0.62); lab(ax, b, "{:+.1f}%", size=8.5); ax.axhline(0, color=INK, lw=0.8); ax.set_ylim(-44, 34)
for i, r in ER.iterrows(): ax.text(i, -42, f"EPS ${r.adj_eps:.2f}", ha="center", fontsize=7.5, color=MUTED)
ax.set_ylabel("Share price move on the day, %"); ax.set_title("Reaction to the last eight earnings reports (quarter / report date)"); ax.tick_params(axis="x", labelsize=8)
save(fig, "11_earnings_reactions.png", "Source: Nasdaq closes (close-to-close on report day; results are released pre-market); adjusted EPS from Crocs press releases. Every one of the eight beat the EPS guidance or consensus.")
# 12 revenue at risk ------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.8, 4.3)); r = RT.iloc[::-1].reset_index(drop=True); seq = {1: "#cfe0f7", 2: "#a9c8f0", 3: "#6fa3e3", 4: "#2a78d6", 5: "#14457f"}
ax.barh(r.line, r.ttm_revenue_usd_m, color=[seq[s] for s in r.score], height=0.66, edgecolor="white")
ax.barh(r.line, r.revenue_at_risk_usd_m, color=RED, height=0.22, label="Revenue at risk (2-year, if the fad unwinds)")
for i, row in r.iterrows(): ax.text(row.ttm_revenue_usd_m + 15, i, f"${row.ttm_revenue_usd_m:,.0f}m | score {row.score} | at risk ${row.revenue_at_risk_usd_m:,.0f}m", va="center", fontsize=8)
ax.set_xlim(0, 1850); ax.set_xlabel("TTM revenue, US$ m (bar shade = risk score 1-5, darker = more exposed)", fontsize=8.5); ax.grid(axis="y", visible=False); ax.legend(fontsize=8, loc="center right")
ax.set_title(f"Revenue at risk: {M['rar']['at_risk_pct']*100:.1f}% of group revenue (${M['rar']['at_risk']:,.0f}m) is exposed to a clog-cycle reversal")
save(fig, "12_revenue_at_risk.png", "Source: TTM revenue to Sep-2026 from Crocs releases (reported by brand/region/channel); product split uses FY2025 mix 74/13/8% (Q4-25 call) applied uniformly - my assumption.\nScores and haircuts (1=0%, 2=5%, 3=12%, 4=20%, 5=30%) are my subjective inputs; see model.xlsx 'RevAtRisk'.")
# 13 stress EPS ---------------------------------------------------------------------------
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.8), gridspec_kw={"width_ratios": [1.35, 1]}); rar = M["rar"]
names = ["TTM adj. EPS\n(reported)", "Run-rate EPS\ntoday's shares", "Consensus\nFY27E", "My base\nFY27E", "Bear case\nFY27E", "Full fad\nunwind"]; vals = [13.52, rar["eps0"], 16.01, M["valuation"]["eps27"][1], M["valuation"]["eps27"][0], rar["eps1"]]
b = axs[0].bar(names, vals, color=[GREY, GREY, GREY, BLUE, ORANGE, RED], width=0.62); lab(axs[0], b, "${:.2f}"); axs[0].tick_params(axis="x", labelsize=7); axs[0].set_ylim(0, 21); axs[0].set_title("EPS: consensus vs my cases vs the stress test")
mc = np.load(os.path.join(D, "revenue_at_risk_mc.npy")); axs[1].hist(mc[:, 1], bins=30, color=RED, alpha=0.75, edgecolor="white"); p = RAR["monte_carlo"]["eps_p5_p50_p95"]
for v, t in zip(p, ("p5", "median", "p95")): axs[1].axvline(v, color=INK, lw=0.9, ls="--"); axs[1].text(v, axs[1].get_ylim()[1] * 0.93, f"{t}\n${v:.2f}", fontsize=7.5, ha="center", bbox=dict(fc="white", ec="none", pad=1))
axs[1].set_xlabel("Stressed EPS ($)"); axs[1].set_yticks([]); axs[1].grid(False); axs[1].set_title("Sensitivity to my scores (20,000 draws, each score +/-1)")
save(fig, "13_stress_eps.png", "Source: my calculation (scripts/10_revenue_at_risk.py; model.xlsx 'RevAtRisk'). Stress assumes 50% of distribution cost and 65% of SG&A fixed, 150 bps markdown pressure, 18% tax, no buybacks.\nConsensus FY27E EPS $16.01 = Yahoo Finance, 15 analysts, 2026-11-26 (Nasdaq/Zacks: $15.85).")
# 14 scenario football field --------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.4, 3.9)); V = M["valuation"]; price = M["inputs"]["price"]
rows = [("Full fad unwind (stress EPS x 7x)", rar["val"], rar["val"], RED), ("Bear: PT / DCF", V["pt"][0], V["dcf"][0], ORANGE), ("Base: PT / DCF", V["pt"][1], V["dcf"][1], BLUE), ("Bull: PT / DCF", V["dcf"][2], V["pt"][2], TEAL),
        ("Sell-side targets (low / mean / high)", 128, 184, GREY), ("52-week range", 75.13, 164.24, GREY)]
for i, (n, lo, hi, cc) in enumerate(rows):
    a, bb = min(lo, hi), max(lo, hi)
    if abs(bb - a) < 1: ax.plot([a], [i], marker="D", color=cc, ms=8)
    else: ax.barh(i, bb - a, left=a, color=cc, height=0.5, alpha=0.85)
    ax.text(bb + 4, i, (f"${a:,.0f}" if abs(bb - a) < 1 else f"${a:,.0f} - ${bb:,.0f}"), va="center", fontsize=8.5)
ax.plot([160.75], [4], marker="|", color=INK, ms=14, mew=2); ax.axvline(price, color=INK, lw=1.2, ls="--"); ax.text(price, -0.75, f"Price ${price:.2f}", ha="center", fontsize=8.5, fontweight="bold")
ax.axvline(V["pt"][3], color=BLUE, lw=1.2, ls=":"); ax.text(V["pt"][3], 5.72, f"Prob-weighted ${V['pt'][3]:.0f}", ha="center", fontsize=8.5, color=BLUE, fontweight="bold")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows]); ax.invert_yaxis(); ax.set_xlim(30, 340); ax.set_ylim(6.1, -1.1); ax.grid(axis="y", visible=False); ax.set_xlabel("US$ per share")
ax.set_title("Valuation range: price targets (Dec-2027) and DCF by scenario")
save(fig, "14_valuation_range.png", "Source: model.xlsx (my estimates): PT = exit P/E (7.0x / 10.5x / 13.0x) x FY2028E EPS; DCF at 10% WACC, 2% terminal growth. Sell-side targets: Nasdaq, 2026-11-26. Price: Nasdaq close 2026-11-25.")
# 15 GAAP vs non-GAAP & margin trend last 8 quarters ---------------------------------------
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.2)); xl = [p[2:4] + p[4:] for p in q8.index]
axs[0].plot(xl, q8.adj_gm_pct, color=BLUE, lw=2, marker="o", ms=4, label="Adj. gross margin"); axs[0].plot(xl, q8.adj_op_margin_pct, color=ORANGE, lw=2, marker="o", ms=4, label="Adj. operating margin")
for xx, v in zip(xl, q8.adj_gm_pct): axs[0].annotate(f"{v:.1f}", (xx, v), xytext=(0, 5), textcoords="offset points", ha="center", fontsize=7.5)
for xx, v in zip(xl, q8.adj_op_margin_pct): axs[0].annotate(f"{v:.1f}", (xx, v), xytext=(0, 5), textcoords="offset points", ha="center", fontsize=7.5)
axs[0].set_ylim(10, 70); axs[0].legend(fontsize=8, loc="center right"); axs[0].set_title("Quarterly margins (%)"); axs[0].tick_params(axis="x", labelsize=8)
gap = q8.eps_diluted - q8.adj_eps; b = axs[1].bar(xl, gap, color=[TEAL if v > 0 else RED for v in gap], width=0.6); lab(axs[1], b, "{:+.2f}", size=7.5); axs[1].axhline(0, color=INK, lw=0.8)
axs[1].set_title("GAAP EPS less adjusted EPS ($ per share)"); axs[1].tick_params(axis="x", labelsize=8); axs[1].set_ylim(-16, 6)
save(fig, "15_margins_gaap_gap.png", "Source: Crocs earnings releases (reported). Q2-25 GAAP includes the $737m HEYDUDE impairment; Q4-24 a $269m tax benefit from an IP transfer; Q3-26 $64m of IEEPA tariff refunds.")
# 16 EPS bridge FY26E -> FY28E -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.6, 3.3)); e26, e28 = S["eps"]["FY2026E"], S["eps"]["FY2028E"]; ni26, ni28 = S["ni"]["FY2026E"], S["ni"]["FY2028E"]; sh26, sh28 = S["sh_avg"]["FY2026E"], S["sh_avg"]["FY2028E"]
rev_eff = (S["rev"]["FY2028E"] - S["rev"]["FY2026E"]) * S["margin"]["FY2026E"] * 0.82 / sh26; mar_eff = S["rev"]["FY2028E"] * (S["margin"]["FY2028E"] - S["margin"]["FY2026E"]) * 0.82 / sh26
int_eff = (S["int"]["FY2026E"] - S["int"]["FY2028E"] - 3) * 0.82 / sh26; ni_eps = ni28 / sh26; bb_eff = e28 - ni_eps; oth = ni_eps - e26 - rev_eff - mar_eff - int_eff
steps = [("FY26E EPS", e26), ("Revenue\ngrowth", rev_eff), ("Margin", mar_eff), ("Lower\ninterest", int_eff + oth), ("Buybacks", bb_eff), ("FY28E EPS", e28)]; cum = 0
for i, (n, v) in enumerate(steps):
    if i in (0, len(steps) - 1): ax.bar(i, v, color=BLUE, width=0.6); ax.text(i, v + 0.3, f"${v:.2f}", ha="center", fontsize=9, fontweight="bold"); cum = v
    else: ax.bar(i, v, bottom=cum, color=TEAL, width=0.6); ax.text(i, cum + v + 0.3, f"+${v:.2f}", ha="center", fontsize=9); cum += v
ax.set_xticks(range(len(steps))); ax.set_xticklabels([s[0] for s in steps], fontsize=8.5); ax.set_ylim(0, 23); fig.set_figheight(3.7); ax.set_title("The compounding algorithm: base-case EPS bridge, FY2026E to FY2028E")
save(fig, "16_eps_bridge.png", "Source: model.xlsx Base case (my estimates). Buybacks at 85% of free cash flow, at $175 (FY27) and $190 (FY28) per share. Tax 18% (non-GAAP).")
json.dump({"eps_bridge": {"rev": rev_eff, "margin": mar_eff, "interest_other": int_eff + oth, "buybacks": bb_eff, "e26": e26, "e28": e28}}, open(os.path.join(D, "chart_stats.json"), "w"), indent=1)
print("charts:", sorted(os.listdir(OUT)))
