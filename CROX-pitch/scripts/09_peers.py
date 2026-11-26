"""Peer comparison table: CROX vs DECK, BIRK, ONON.
Source: stockanalysis.com statistics/financials pages (data/sa/, fetched date in data/sa/_asof.json), Nasdaq API prices/consensus.
All peer multiples use ONE vendor's methodology so they are comparable; CROX is cross-checked against my own filing-based numbers.
Output: data/derived/peers.csv"""
import os, glob, json, pandas as pd, numpy as np
B = os.path.join(os.path.dirname(__file__), "..", "data"); D = os.path.join(B, "derived")
def stats(t):
    d = {}
    for f in sorted(glob.glob(os.path.join(B, "sa", f"{t}_stats_*.csv"))):
        for _, r in pd.read_csv(f).iterrows(): d[str(r.iloc[0])] = r.iloc[1]
    return d
def num(x):
    if x is None or (isinstance(x, float) and np.isnan(x)): return np.nan
    s = str(x).replace("$", "").replace(",", "").replace("%", "").strip()
    m = 1
    if s.endswith("B"): m, s = 1e3, s[:-1]
    elif s.endswith("M"): m, s = 1, s[:-1]
    try: return float(s) * m
    except ValueError: return np.nan
rows = {}
for t in ["crox", "deck", "birk", "onon"]:
    s = stats(t)
    isa = pd.read_csv(os.path.join(B, "sa", f"{t}_is_a_0.csv"))
    ttm_growth = num(isa.iloc[2, 1])
    fc = pd.read_csv(os.path.join(B, "sa", f"{t}_forecast_3.csv"))
    est_cols = [c for c in fc.columns if c.endswith("E")]
    fwd_growth = num(fc.loc[fc.iloc[:, 0] == "Revenue Growth", est_cols[0]].iloc[0])
    r = {"price_usd": json.load(open(os.path.join(B, "market", f"info_{t.upper()}.json")))["data"]["primaryData"]["lastSalePrice"].replace("$", ""),
         "mkt_cap_usd_m": num(s["Market Cap"]), "ev_usd_m": num(s["Enterprise Value"]), "rev_ttm_usd_m": num(s["Revenue"]),
         "ps_ttm": num(s["PS Ratio"]), "ps_fwd": num(s["Forward PS"]), "p_fcf": num(s["P/FCF Ratio"]), "ev_ebitda": num(s["EV / EBITDA"]),
         "ev_sales": num(s["EV / Sales"]), "pe_ttm": num(s["PE Ratio"]), "pe_fwd": num(s["Forward PE"]),
         "gross_margin_pct": num(s["Gross Margin"]), "op_margin_pct": num(s["Operating Margin"]), "fcf_margin_pct": num(s["FCF Margin"]),
         "rev_growth_ttm_pct": ttm_growth, "rev_growth_next_fy_cons_pct": fwd_growth, "rev_growth_3y_cons_pct": num(s["Revenue Growth Forecast (3Y)"]),
         "eps_growth_3y_cons_pct": num(s["EPS Growth Forecast (3Y)"]),
         "net_debt_usd_m": -num(s["Net Cash"]), "ebitda_usd_m": num(s["EBITDA"]), "roic_pct": num(s["Return on Invested Capital (ROIC)"]),
         "buyback_yield_pct": num(s["Buyback Yield"]), "beta_5y": num(s["Beta (5Y)"]), "short_pct_float": num(s["Short % of Float"]), "chg_52w_pct": num(s["52-Week Price Change"])}
    r["net_debt_to_ebitda"] = r["net_debt_usd_m"] / r["ebitda_usd_m"]
    r["value_growth_score_ttm"] = r["ps_ttm"] / r["rev_growth_ttm_pct"] if r["rev_growth_ttm_pct"] > 0 else np.nan
    r["value_growth_score_fwd"] = r["ps_ttm"] / r["rev_growth_next_fy_cons_pct"] if r["rev_growth_next_fy_cons_pct"] > 0 else np.nan
    r["pe_fwd_to_eps_growth"] = r["pe_fwd"] / r["eps_growth_3y_cons_pct"]
    rows[t.upper()] = r
P = pd.DataFrame(rows)
P.to_csv(os.path.join(D, "peers.csv"))
pd.set_option("display.width", 200)
print(P.round(2).to_string())
