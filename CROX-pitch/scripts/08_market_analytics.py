"""Market analytics: P/E history (CROX, DECK), earnings-day reactions, beta, drawdowns, sell-off capture.
Inputs: data/market/px_*.json (Nasdaq API, unadjusted closes; CROX pays no dividend), data/derived/quarterly_release_raw.csv,
        data/sec_companyfacts_DECK.json, data/market/epsfc_*.json (consensus EPS, Nasdaq/Zacks).
Outputs: data/derived/prices.csv, pe_history.csv, earnings_reactions.csv, risk_stats.json"""
import json, os, numpy as np, pandas as pd
B = os.path.join(os.path.dirname(__file__), "..", "data"); D = os.path.join(B, "derived")
def px(t):
    rows = json.load(open(os.path.join(B, "market", f"px_{t}.json")))["data"]["tradesTable"]["rows"]
    s = pd.Series({pd.Timestamp(r["date"]): float(r["close"].replace("$", "").replace(",", "")) for r in rows}).sort_index()
    return s
P = pd.DataFrame({t: px(t) for t in ["CROX", "DECK", "BIRK", "ONON", "SPY", "XRT"]})
P.to_csv(os.path.join(D, "prices.csv"))
asof = P.index[-1]
# ---------- CROX EPS timeline ----------
Q = pd.read_csv(os.path.join(D, "quarterly_release_raw.csv"))
import re
def rel_date(fn): return pd.Timestamp(re.match(r"(\d{4}-\d\d-\d\d)", fn).group(1))
Q["report_date"] = Q.file.map(rel_date)
Q = Q.sort_values("report_date").reset_index(drop=True)
Q["ttm_adj_eps"] = Q.adj_eps.rolling(4).sum()
cons = json.load(open(os.path.join(B, "market", "epsfc_CROX.json")))["data"]["quarterlyForecast"]["rows"]
fut = [c["consensusEPSForecast"] for c in cons][:4]          # Dec-26, Mar-27, Jun-27, Sep-27 consensus
eps_seq = list(Q.adj_eps) + fut
Q["ntm_eps_hindsight"] = [sum(eps_seq[i + 1:i + 5]) for i in range(len(Q))]
pe = pd.DataFrame(index=P.index)
pe["CROX_px"] = P.CROX
pe["CROX_ttm_eps"] = Q.set_index("report_date").ttm_adj_eps.reindex(P.index, method="ffill")
pe["CROX_ntm_eps"] = Q.set_index("report_date").ntm_eps_hindsight.reindex(P.index, method="ffill")
pe["CROX_pe_ttm"] = pe.CROX_px / pe.CROX_ttm_eps
pe["CROX_pe_ntm"] = pe.CROX_px / pe.CROX_ntm_eps
# ---------- DECK EPS from XBRL (split-adjusted: 6-for-1 in Sep 2024) ----------
cf = json.load(open(os.path.join(B, "sec_companyfacts_DECK.json")))["facts"]["us-gaap"]
def facts(tag):
    u = list(cf[tag]["units"].keys())[0]; rows = []
    for x in cf[tag]["units"][u]:
        if "start" not in x: continue
        rows.append((pd.Timestamp(x["start"]), pd.Timestamp(x["end"]), x["val"], x["filed"]))
    df = pd.DataFrame(rows, columns=["start", "end", "val", "filed"]).sort_values("filed").drop_duplicates(["start", "end"], keep="last")
    df["days"] = (df.end - df.start).dt.days
    return df
ni = facts("NetIncomeLoss"); sh = facts("WeightedAverageNumberOfDilutedSharesOutstanding")
def quarterly(df, flow=True):
    q = df[(df.days > 80) & (df.days < 100)].set_index("end").val.to_dict()
    fy = df[(df.days > 350) & (df.days < 380)]
    for _, r in fy.iterrows():
        if r.end in q: continue
        prev = [e for e in q if r.start < e < r.end]
        if len(prev) == 3: q[r.end] = (r.val - sum(q[e] for e in prev)) if flow else r.val
    return pd.Series(q).sort_index()
niq = quarterly(ni); shq = quarterly(sh, flow=False)
shq = shq.where(shq > 100e6, shq * 6)                  # put pre-split share counts on post-split basis
deck = pd.DataFrame({"ni": niq, "sh": shq}).dropna(); deck["eps"] = deck.ni / deck.sh
deck = deck[deck.index >= "2019-01-01"]
deck["avail"] = deck.index + pd.Timedelta(days=30)      # approx. report lag (DECK reports ~3-7 weeks after quarter end)
dcons = json.load(open(os.path.join(B, "market", "epsfc_DECK.json")))["data"]["quarterlyForecast"]["rows"]
dfut = [c["consensusEPSForecast"] for c in dcons][:4]
dseq = list(deck.eps) + dfut
deck["ttm"] = deck.eps.rolling(4).sum(); deck["ntm"] = [sum(dseq[i + 1:i + 5]) for i in range(len(deck))]
pe["DECK_px"] = P.DECK
pe["DECK_pe_ttm"] = P.DECK / deck.set_index("avail").ttm.reindex(P.index, method="ffill")
pe["DECK_pe_ntm"] = P.DECK / deck.set_index("avail").ntm.reindex(P.index, method="ffill")
pe["CROX_vs_DECK_ntm_prem_pct"] = (pe.CROX_pe_ntm / pe.DECK_pe_ntm - 1) * 100
pe = pe[pe.index >= "2021-05-01"]
pe.to_csv(os.path.join(D, "pe_history.csv"))
deck.to_csv(os.path.join(D, "deck_quarterly_eps.csv"))
# ---------- earnings reactions (last 8 reports; releases are pre-market so reaction = close/prev close) ----------
R = []
sur = {pd.Timestamp(r["dateReported"]): r for r in json.load(open(os.path.join(B, "market", "surprise_CROX.json")))["data"]["earningsSurpriseTable"]["rows"]}
for _, r in Q.tail(8).iterrows():
    d = r.report_date; i = P.index.get_loc(d)
    mv = P.CROX.iloc[i] / P.CROX.iloc[i - 1] - 1; spy = P.SPY.iloc[i] / P.SPY.iloc[i - 1] - 1
    mv5 = P.CROX.iloc[min(i + 5, len(P) - 1)] / P.CROX.iloc[i - 1] - 1
    s = sur.get(d, {})
    R.append({"report_date": d.date(), "quarter": r.period, "rev_yoy_pct": (r.revenue / r.revenue_py - 1) * 100, "adj_eps": r.adj_eps,
              "consensus_eps": s.get("consensusForecast"), "eps_surprise_pct": s.get("percentageSurprise"),
              "px_prev_close": P.CROX.iloc[i - 1], "px_close": P.CROX.iloc[i], "day_move_pct": mv * 100, "spy_move_pct": spy * 100, "move_5d_pct": mv5 * 100})
R = pd.DataFrame(R); R.to_csv(os.path.join(D, "earnings_reactions.csv"), index=False)
# ---------- beta, vol, drawdowns ----------
def beta(a, b, freq, start):
    x = P[[a, b]].loc[start:].resample(freq).last().pct_change().dropna()
    c = np.cov(x[a], x[b]); return c[0, 1] / c[1, 1]
st = {"asof": str(asof.date()), "price": float(P.CROX.iloc[-1])}
st["beta_weekly_5y"] = beta("CROX", "SPY", "W-FRI", asof - pd.DateOffset(years=5))
st["beta_weekly_2y"] = beta("CROX", "SPY", "W-FRI", asof - pd.DateOffset(years=2))
st["beta_monthly_5y"] = beta("CROX", "SPY", "ME", asof - pd.DateOffset(years=5))
dr = P.CROX.loc[asof - pd.DateOffset(years=1):].pct_change().dropna(); st["vol_1y_annualised_pct"] = float(dr.std() * np.sqrt(252) * 100)
dsp = P.SPY.loc[asof - pd.DateOffset(years=1):].pct_change().dropna(); st["spy_vol_1y_annualised_pct"] = float(dsp.std() * np.sqrt(252) * 100)
def maxdd(s):
    roll = s.cummax(); dd = s / roll - 1; t = dd.idxmin(); p = s.loc[:t].idxmax(); return float(dd.min() * 100), str(p.date()), str(t.date())
for w in (5, 10):
    st[f"crox_max_drawdown_{w}y"] = maxdd(P.CROX.loc[asof - pd.DateOffset(years=w):])
# S&P sell-off episodes: peak-to-trough SPY declines >= 10% (closing basis) in the last 10 years
spy = P.SPY; eps = []; peak = spy.iloc[0]; peak_d = spy.index[0]; trough = peak; trough_d = peak_d; in_dd = False
for d, v in spy.items():
    if v >= peak:
        if in_dd and (trough / peak - 1) <= -0.10: eps.append((peak_d, trough_d))
        peak, peak_d, trough, trough_d, in_dd = v, d, v, d, False
    elif v < trough: trough, trough_d, in_dd = v, d, True
if in_dd and (trough / peak - 1) <= -0.10: eps.append((peak_d, trough_d))
E_ = []
for a, b in eps:
    E_.append({"spy_peak": str(a.date()), "spy_trough": str(b.date()), "spy_pct": float((spy[b] / spy[a] - 1) * 100), "crox_pct": float((P.CROX[b] / P.CROX[a] - 1) * 100),
               "deck_pct": float((P.DECK[b] / P.DECK[a] - 1) * 100), "xrt_pct": float((P.XRT[b] / P.XRT[a] - 1) * 100)})
st["sp500_selloffs"] = E_
st["downside_capture_avg"] = float(np.mean([e["crox_pct"] / e["spy_pct"] for e in E_]))
# CROX own >=30% drawdown episodes in the last 6 years
c = P.CROX.loc["2020-11-01":]; eps2 = []; peak = c.iloc[0]; peak_d = c.index[0]; trough = peak; trough_d = peak_d
for d, v in c.items():
    if v >= peak:
        if trough / peak - 1 <= -0.30: eps2.append({"peak": str(peak_d.date()), "peak_px": float(peak), "trough": str(trough_d.date()), "trough_px": float(trough), "pct": float((trough / peak - 1) * 100)})
        peak, peak_d, trough, trough_d = v, d, v, d
    elif v < trough: trough, trough_d = v, d
if trough / peak - 1 <= -0.30: eps2.append({"peak": str(peak_d.date()), "peak_px": float(peak), "trough": str(trough_d.date()), "trough_px": float(trough), "pct": float((trough / peak - 1) * 100)})
st["crox_drawdowns_30pct"] = eps2
for k, days in (("1m", 21), ("3m", 63), ("6m", 126), ("1y", 252), ("3y", 756), ("5y", 1260)):
    st[f"crox_ret_{k}_pct"] = float((P.CROX.iloc[-1] / P.CROX.iloc[-1 - days] - 1) * 100); st[f"spy_ret_{k}_pct"] = float((P.SPY.iloc[-1] / P.SPY.iloc[-1 - days] - 1) * 100)
last = pe.dropna(subset=["CROX_pe_ntm"]).iloc[-1]
st["crox_pe_ntm_now"] = float(last.CROX_pe_ntm); st["crox_pe_ttm_now"] = float(last.CROX_pe_ttm); st["deck_pe_ntm_now"] = float(last.DECK_pe_ntm); st["deck_pe_ttm_now"] = float(last.DECK_pe_ttm)
for col in ("CROX_pe_ntm", "CROX_pe_ttm", "DECK_pe_ntm", "DECK_pe_ttm", "CROX_vs_DECK_ntm_prem_pct"):
    s = pe[col].dropna(); st[col + "_5y_stats"] = {"mean": float(s.mean()), "median": float(s.median()), "min": float(s.min()), "max": float(s.max()), "p25": float(s.quantile(.25)), "p75": float(s.quantile(.75)), "pctile_now": float((s < s.iloc[-1]).mean() * 100), "start": str(s.index[0].date())}
json.dump(st, open(os.path.join(D, "risk_stats.json"), "w"), indent=1)
print(json.dumps(st, indent=1)); print(R.round(2).to_string())
print(deck.tail(8).round(3))
