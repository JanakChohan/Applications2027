"""Collect every number quoted in the deliverables into data/derived/facts.json (single source for deck, memo, markdown).
Each entry: value + label (reported / consensus / broker / my estimate) + source key (see sources.md)."""
import json, os, pandas as pd, numpy as np
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); D = os.path.join(ROOT, "data", "derived")
A = pd.read_csv(os.path.join(D, "annual.csv"), index_col=0); Q = pd.read_csv(os.path.join(D, "quarterly.csv"), index_col=0); M = json.load(open(os.path.join(D, "model_outputs.json")))
R = json.load(open(os.path.join(D, "risk_stats.json"))); RAR = json.load(open(os.path.join(D, "revenue_at_risk.json"))); PE = pd.read_csv(os.path.join(D, "peers.csv"), index_col=0)
F4 = pd.read_csv(os.path.join(D, "form4_transactions.csv")); ER = pd.read_csv(os.path.join(D, "earnings_reactions.csv")); short = json.load(open(os.path.join(ROOT, "data", "market", "short_CROX.json")))["data"]["shortInterestTable"]["rows"]
t4 = Q.tail(4); p4 = Q.iloc[-8:-4]; I = M["inputs"]; V = M["valuation"]; f = {}
f["price"] = I["price"]; f["asof"] = R["asof"]; f["shares"] = I["shares"]; f["mcap"] = I["mcap"]; f["net_debt"] = I["nd"]; f["ev"] = I["ev"]; f["wacc"] = I["wacc"]; f["ke"] = I["ke"]
f["ttm_rev"] = t4.revenue.sum(); f["ttm_rev_g"] = (t4.revenue.sum() / p4.revenue.sum() - 1) * 100; f["ttm_adj_ebit"] = t4.adj_op_income.sum(); f["ttm_adj_ebit_m"] = f["ttm_adj_ebit"] / f["ttm_rev"] * 100
f["ttm_ebitda"] = f["ttm_adj_ebit"] + t4.da_q.sum(); f["ttm_fcf"] = t4.fcf_calc.sum(); f["ttm_eps"] = t4.adj_eps.sum(); f["ttm_sbc"] = t4.sbc_q.sum(); f["ttm_buyback"] = 180.0 + 506.194; f["ttm_gaap_ni"] = t4.net_income.sum()
f["fcf_yield"] = f["ttm_fcf"] / f["mcap"] * 100; f["ev_ebitda"] = f["ev"] / f["ttm_ebitda"]; f["nd_ebitda"] = f["net_debt"] / f["ttm_ebitda"]; f["pe_fy26_guide"] = f["price"] / 14.55; f["pe_fy27_cons"] = f["price"] / 16.01
f["pe_fy27_mine"] = f["price"] / V["eps27"][1]; f["ttm_fcf_conv"] = f["ttm_fcf"] / t4.adj_net_income.sum() * 100; f["buyback_yield"] = f["ttm_buyback"] / f["mcap"] * 100
f["ttm_crocs"] = t4.crocs_rev.sum(); f["ttm_hd"] = t4.hd_rev.sum(); f["ttm_na"] = t4.crocs_na.sum(); f["ttm_intl"] = t4.crocs_intl.sum(); f["intl_share_ttm"] = f["ttm_intl"] / f["ttm_crocs"] * 100
f["ttm_dtc_share"] = (t4.crocs_dtc.sum() + t4.hd_dtc.sum()) / f["ttm_rev"] * 100
for y in (2021, 2022, 2023, 2024, 2025):
    f[f"fy{y}"] = {k: (None if pd.isna(A.loc[y, k]) else float(A.loc[y, k])) for k in ["revenue", "rev_growth_pct", "gm_pct", "adj_gm_pct", "op_margin_pct", "adj_op_margin_pct", "adj_op_income", "adj_eps", "eps_gaap", "cfo", "capex", "fcf", "fcf_margin_pct",
            "fcf_conv_adj_ni_pct", "net_debt", "adj_ebitda", "net_debt_to_adj_ebitda", "sbc", "sbc_pct_rev", "sh_diluted", "sh_change_pct", "buybacks", "roic_pct", "marketing", "marketing_pct_rev", "crocs_rev", "hd_rev", "crocs_op_margin_pct",
            "hd_op_margin_ex_impair_pct", "crocs_na", "crocs_intl", "crocs_units_k", "crocs_asp", "hd_units_k", "hd_asp", "crocs_gm_pct", "hd_gm_pct", "da", "net_income"]}
f["quarters"] = {p: {k: (None if pd.isna(Q.loc[p, k]) else float(Q.loc[p, k])) for k in ["revenue", "revenue_yoy_pct", "adj_gm_pct", "adj_op_margin_pct", "op_margin_pct", "adj_eps", "eps_diluted", "adj_eps_yoy_pct", "cfo_q", "capex_q", "fcf_calc", "sbc_q",
            "net_debt", "net_debt_to_ttm_ebitda", "sh_diluted_m", "crocs_rev_yoy_pct", "hd_rev_yoy_pct", "crocs_na_yoy_pct", "crocs_intl_yoy_pct", "crocs_dtc_yoy_pct", "crocs_whsl_yoy_pct", "hd_whsl_yoy_pct", "hd_dtc_yoy_pct",
            "crocs_gm_use_pct", "hd_gm_use_pct", "inventories", "inventories_yoy_pct", "gaap_minus_adj_op_income", "crocs_rev", "hd_rev", "crocs_na", "crocs_intl"]} for p in Q.tail(8).index}
q = f["quarters"]; f["gm_yoy_bps"] = {p: (Q.loc[p, "adj_gm_pct"] - Q.loc[f"{int(p[:4])-1}{p[4:]}", "adj_gm_pct"]) * 100 for p in Q.tail(4).index}; f["opm_yoy_bps"] = {p: (Q.loc[p, "adj_op_margin_pct"] - Q.loc[f"{int(p[:4])-1}{p[4:]}", "adj_op_margin_pct"]) * 100 for p in Q.tail(4).index}
f["valuation"] = V; f["key"] = M["key"]; f["rar"] = M["rar"]; f["rar_mc"] = RAR["monte_carlo"]; f["rar_prec"] = RAR["precedents"]; f["rar_cost"] = RAR["cost_structure_sensitivity_eps"]; f["rar_linear"] = RAR["linear_haircut_map"]
f["sens"] = M["sens"]; f["reverse"] = {k: M["reverse"][k] for k in ("implied_g", "implied_margin", "implied_cagr", "fcf")}; f["scen"] = M["scen"]; f["risk"] = R; f["peers"] = PE.to_dict()
s12 = F4[(F4.code == "S") & (F4.trade_date >= "2025-11-26")]; b12 = F4[(F4.code == "P") & (F4.trade_date >= "2025-11-26")]
f["insider"] = {"sales_12m_usd": float(s12.value_usd.sum()), "buys_12m_usd": float(b12.value_usd.sum()), "ceo_sales_usd": float(s12[s12.owner.str.contains("Rees")].value_usd.sum()), "ceo_sales_sh": float(s12[s12.owner.str.contains("Rees")].shares.sum()),
                "n_10b5_flagged": int(((s12.aff10b5One.astype(str) == "1") | s12.footnote_mentions_10b5_1).sum()), "n_sales": int(len(s12)), "ceo_shares_after": 673293,
                "post_q3_sales_usd": float(s12[s12.trade_date >= "2026-10-29"].value_usd.sum())}
f["short"] = {"shares": float(short[0]["interest"].replace(",", "")), "date": short[0]["settlementDate"], "dtc": short[0]["daysToCover"], "pct_shares": float(short[0]["interest"].replace(",", "")) / (I["shares"] * 1e6) * 100,
              "peak_12m": max(float(r["interest"].replace(",", "")) for r in short), "peak_date": max(short, key=lambda r: float(r["interest"].replace(",", "")))["settlementDate"]}
f["earn"] = ER.to_dict(orient="records"); f["earn_avg_abs_move"] = float(ER.day_move_pct.abs().mean())
f["ip_tax_adj_9m26"] = 33.706; f["ip_tax_eps_fy26e"] = 45.0 / 48.7
f["cons"] = {"fy26_eps": 14.63, "fy27_eps_yahoo": 16.01, "fy27_eps_nasdaq": 15.85, "fy28_eps_nasdaq": 16.69, "fy26_rev": 4180, "fy27_rev": 4340, "q4_eps": 3.40, "pt_mean_nasdaq": 160.75, "pt_low": 128, "pt_high": 184, "pt_yahoo": 164.67, "buy": 5, "hold": 5, "sell": 1}
json.dump(f, open(os.path.join(D, "facts.json"), "w"), indent=1, default=float)
for k in ("mcap", "net_debt", "ev", "ttm_rev", "ttm_rev_g", "ttm_adj_ebit", "ttm_adj_ebit_m", "ttm_ebitda", "ttm_fcf", "ttm_eps", "fcf_yield", "ev_ebitda", "nd_ebitda", "pe_fy26_guide", "pe_fy27_cons", "pe_fy27_mine", "ttm_fcf_conv", "buyback_yield", "ttm_buyback", "ttm_na", "ttm_intl", "intl_share_ttm", "ttm_dtc_share", "ttm_sbc", "ttm_gaap_ni"): print(k, round(f[k], 2))
print(f["insider"]); print(f["short"]); print(f["gm_yoy_bps"], f["opm_yoy_bps"]); print(f["earn_avg_abs_move"])
