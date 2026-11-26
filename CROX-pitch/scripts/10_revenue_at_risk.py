"""PROPRIETARY ANALYSIS - 'How much of Crocs is a fad?'  Revenue-at-risk scoring and stress test.
Sourced inputs : TTM revenue by brand/region/channel (press releases), FY2025 Crocs Brand product mix 74/13/8 (Q4-25 call),
                 China ~8% of sales (Q4-25 call), distribution cost in COGS $488.4M (10-K FY25), TTM adjusted P&L (press releases),
                 consensus FY27 EPS (Yahoo $16.01; Nasdaq/Zacks $15.85), fad precedents (Crocs 2007-09: 10-K FY2009; HEYDUDE 2023-25: 10-Ks).
My assumptions : the 1-5 scores, the score->haircut map, product mix applied uniformly across regions, China mix applied to Crocs Brand,
                 fixed/variable cost split, markdown pressure, tax 18% (company non-GAAP guidance), no buybacks in the stress.
Outputs: data/derived/revenue_at_risk.json / .csv  (the same logic is replicated with live formulas in model.xlsx 'RevAtRisk')."""
import json, os, numpy as np, pandas as pd
B = os.path.join(os.path.dirname(__file__), "..", "data"); D = os.path.join(B, "derived")
Q = pd.read_csv(os.path.join(D, "quarterly.csv"), index_col=0); T = Q.tail(4)
ttm = {k: float(T[k].sum()) for k in ["revenue", "crocs_rev", "hd_rev", "crocs_na_whsl", "crocs_na_dtc", "crocs_intl_whsl", "crocs_intl_dtc", "hd_whsl", "hd_dtc",
                                        "adj_gross_profit", "adj_sga", "adj_op_income", "da_q", "interest_expense", "adj_eps", "adj_net_income"]}
MIX = {"clog": 0.74, "sandal": 0.13, "jibbitz_other": 0.13}          # FY2025, Crocs Brand (Jibbitz 8% + other 5% residual)
CHINA_SHARE = 0.08                                                    # of Crocs Brand sales (ambiguity flagged in sources.md)
na = ttm["crocs_na_whsl"] + ttm["crocs_na_dtc"]; intl = ttm["crocs_intl_whsl"] + ttm["crocs_intl_dtc"]
china = CHINA_SHARE * ttm["crocs_rev"]; intl_x = intl - china
lines = [  # name, revenue, score, revenue basis
    ("Crocs NA - clogs, wholesale", ttm["crocs_na_whsl"] * MIX["clog"], 5, "reported x mix (est.)"),
    ("Crocs NA - clogs, DTC", ttm["crocs_na_dtc"] * MIX["clog"], 4, "reported x mix (est.)"),
    ("Crocs NA - sandals", na * MIX["sandal"], 2, "reported x mix (est.)"),
    ("Crocs NA - Jibbitz & other", na * MIX["jibbitz_other"], 5, "reported x mix (est.)"),
    ("Crocs Intl - China", china, 4, "8% of Crocs Brand (mgmt)"),
    ("Crocs Intl ex-China - clogs", intl_x * MIX["clog"], 3, "reported x mix (est.)"),
    ("Crocs Intl ex-China - sandals, Jibbitz, other", intl_x * (1 - MIX["clog"]), 2, "reported x mix (est.)"),
    ("HEYDUDE - wholesale", ttm["hd_whsl"], 4, "reported"),
    ("HEYDUDE - DTC", ttm["hd_dtc"], 3, "reported"),
]
HAIRCUT = {1: 0.00, 2: 0.05, 3: 0.12, 4: 0.20, 5: 0.30}               # 2-year cumulative revenue decline if the fad unwinds (my assumption)
A = dict(dist_cost=488.4, dist_fixed_share=0.50, sga_fixed_share=0.65, markdown_gm_hit=0.015, tax=0.18, shares=46.2 + 0.5,
         net_interest=75.0, trough_pe=7.0, price=159.93, cons_eps_fy27_yahoo=16.01, cons_eps_fy27_nasdaq=15.85)
def stress(scores, a=A, haircut=HAIRCUT):
    rev0 = ttm["revenue"]; cogs0 = rev0 - ttm["adj_gross_profit"]; sga0 = ttm["adj_sga"]
    at_risk = sum(r * haircut[s] for (_, r, _, _), s in zip(lines, scores))
    rev1 = rev0 - at_risk
    var_cogs = (cogs0 - a["dist_cost"] * a["dist_fixed_share"]) / rev0
    cogs1 = a["dist_cost"] * a["dist_fixed_share"] + var_cogs * rev1 + a["markdown_gm_hit"] * rev1
    sga1 = sga0 * a["sga_fixed_share"] + sga0 * (1 - a["sga_fixed_share"]) / rev0 * rev1
    ebit0 = rev0 - cogs0 - sga0; ebit1 = rev1 - cogs1 - sga1
    eps0 = (ebit0 - a["net_interest"]) * (1 - a["tax"]) / a["shares"]; eps1 = (ebit1 - a["net_interest"]) * (1 - a["tax"]) / a["shares"]
    return dict(rev0=rev0, at_risk=at_risk, at_risk_pct=at_risk / rev0 * 100, rev1=rev1, ebit0=ebit0, ebit1=ebit1, ebitda0=ebit0 + ttm["da_q"], ebitda1=ebit1 + ttm["da_q"],
                ebit_margin1=ebit1 / rev1 * 100, eps0=eps0, eps1=eps1, eps_chg_pct=(eps1 / eps0 - 1) * 100, decremental_margin=(ebit0 - ebit1) / at_risk * 100)
base_scores = [l[2] for l in lines]
central = stress(base_scores)
tab = pd.DataFrame([{"line": n, "ttm_revenue_usd_m": r, "pct_of_group": r / ttm["revenue"] * 100, "score": s, "haircut_pct": HAIRCUT[s] * 100,
                     "revenue_at_risk_usd_m": r * HAIRCUT[s], "basis": b} for n, r, s, b in lines])
tab.to_csv(os.path.join(D, "revenue_at_risk.csv"), index=False)
# --- sensitivity on the subjective scores ---
sens = {"all scores -1": stress([max(1, s - 1) for s in base_scores]), "central": central, "all scores +1": stress([min(5, s + 1) for s in base_scores])}
rng = np.random.default_rng(42); mc = []
for _ in range(20000):
    sc = [int(min(5, max(1, s + rng.choice([-1, 0, 1], p=[0.25, 0.5, 0.25])))) for s in base_scores]
    r = stress(sc); mc.append((r["at_risk_pct"], r["eps1"]))
mc = np.array(mc)
cost_sens = {f"SG&A fixed {int(f*100)}%": stress(base_scores, {**A, "sga_fixed_share": f})["eps1"] for f in (0.5, 0.65, 0.8)}
linear = stress(base_scores, haircut={1: 0, 2: 0.075, 3: 0.15, 4: 0.225, 5: 0.30})
out = {"ttm": ttm, "assumptions": A, "haircut_map": HAIRCUT, "mix": MIX, "china_share": CHINA_SHARE, "central": central,
       "score_sensitivity": {k: {"at_risk_pct": v["at_risk_pct"], "eps1": v["eps1"], "ebitda1": v["ebitda1"]} for k, v in sens.items()},
       "monte_carlo": {"n": len(mc), "at_risk_pct_p5_p50_p95": [float(np.percentile(mc[:, 0], p)) for p in (5, 50, 95)], "eps_p5_p50_p95": [float(np.percentile(mc[:, 1], p)) for p in (5, 50, 95)]},
       "cost_structure_sensitivity_eps": cost_sens, "linear_haircut_map": {"at_risk_pct": linear["at_risk_pct"], "eps1": linear["eps1"]},
       "stressed_value_at_trough_pe": central["eps1"] * A["trough_pe"],
       "precedents": {"crocs_2007_2009_rev_pct": (645.767 / 847.350 - 1) * 100, "crocs_2008_gm_pct": 233.966 / 721.589 * 100, "crocs_2007_gm_pct": 497.649 / 847.350 * 100,
                      "heydude_2023_2025_rev_pct": (714.84 / 949.393 - 1) * 100, "heydude_whsl_2023_2025_pct": (336.325 / 566.937 - 1) * 100, "crocs_na_2024_2025_pct": (1709.635 / 1833.422 - 1) * 100,
                      "crocs_2014_2017_rev_pct": (1023.513 / 1198.223 - 1) * 100}}
json.dump(out, open(os.path.join(D, "revenue_at_risk.json"), "w"), indent=1)
np.save(os.path.join(D, "revenue_at_risk_mc.npy"), mc)
pd.set_option("display.width", 200); print(tab.round(1).to_string()); print(json.dumps({k: out[k] for k in ("central", "score_sensitivity", "monte_carlo", "cost_structure_sensitivity_eps", "linear_haircut_map", "stressed_value_at_trough_pe", "precedents")}, indent=1))
