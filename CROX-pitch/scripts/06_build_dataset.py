"""Build the annual and quarterly fundamental datasets used everywhere else.
Inputs : data/sec_companyfacts_CROX.json (XBRL, reported), data/derived/release_rows_*.json (press releases, reported),
         data/sec_txt/*10-Q*.txt (segment note), data/manual/segment_annual.csv (hand-keyed from 10-Ks, sources in file)
Outputs: data/derived/annual.csv, data/derived/quarterly.csv
All $ in millions unless noted. Derived metrics (FCF, ROIC, net debt...) are 'my calculation' on reported inputs."""
import json, os, re, glob
import pandas as pd, numpy as np
B = os.path.join(os.path.dirname(__file__), "..", "data"); D = os.path.join(B, "derived")
cf = json.load(open(os.path.join(B, "sec_companyfacts_CROX.json")))["facts"]["us-gaap"]
def annual(tag):
    u = list(cf[tag]["units"].keys())[0]; d = {}
    for x in cf[tag]["units"][u]:
        if x.get("form") != "10-K": continue
        if "start" in x:
            if x["end"][5:] == "12-31" and x["start"][5:] == "01-01" and x["start"][:4] == x["end"][:4]: d[int(x["end"][:4])] = x["val"]
        elif x["end"][5:] == "12-31": d[int(x["end"][:4])] = x["val"]
    return d
tags = {"revenue": "RevenueFromContractWithCustomerExcludingAssessedTax", "gross_profit": "GrossProfit", "sga": "SellingGeneralAndAdministrativeExpense",
        "op_income": "OperatingIncomeLoss", "net_income": "NetIncomeLoss", "cfo": "NetCashProvidedByUsedInOperatingActivities",
        "capex": "PaymentsToAcquirePropertyPlantAndEquipment", "sbc": "ShareBasedCompensation", "buybacks": "PaymentsForRepurchaseOfCommonStock",
        "da": "DepreciationDepletionAndAmortization", "sh_diluted": "WeightedAverageNumberOfDilutedSharesOutstanding", "eps_gaap": "EarningsPerShareDiluted",
        "lt_debt": "LongTermDebtNoncurrent", "cash": "CashAndCashEquivalentsAtCarryingValue", "inventory": "InventoryNet", "marketing": "MarketingAndAdvertisingExpense",
        "tax": "IncomeTaxExpenseBenefit", "equity": "StockholdersEquity", "assets": "Assets", "op_lease_liab": "OperatingLeaseLiability",
        "interest_paid": "InterestPaidNet", "receivables": "AccountsReceivableNetCurrent", "goodwill": "Goodwill", "intangibles": "IntangibleAssetsNetExcludingGoodwill"}
A = pd.DataFrame({k: annual(v) for k, v in tags.items()}).sort_index()
A = A.loc[2019:2025]
money = [c for c in A.columns if c not in ("eps_gaap",)]
A[money] = A[money] / 1e6
# adjusted (non-GAAP) annual figures from Q4 press releases: columns [Q4, Q4 PY, FY, FY PY]
adj = {}
for y in (2022, 2023, 2024, 2025):
    r = json.load(open(os.path.join(D, f"release_rows_{y}Q4.json")))
    def g(k, i):
        return r[k][i] if k in r and len(r[k]) > i else np.nan
    for yy, i in ((y, 2), (y - 1, 3)):
        adj.setdefault(yy, {})
        adj[yy].update({"adj_op_income": g("//Non-GAAP income from operations", i) / 1e3, "adj_op_margin_pct": g("//Non-GAAP operating margin", i),
                        "adj_gm_pct": g("//Non-GAAP gross margin", i), "adj_eps": g("/Non-GAAP net income per common share/Diluted", i),
                        "adj_net_income": g("//Non-GAAP net income", i) / 1e3})
A = A.join(pd.DataFrame(adj).T)
seg = pd.read_csv(os.path.join(B, "manual", "segment_annual.csv")).set_index("year")
for c in seg.columns:
    if c == "source": continue
    A[c] = seg[c] / (1e3 if c not in ("crocs_asp", "hd_asp", "crocs_gm_pct", "hd_gm_pct", "crocs_units_k", "hd_units_k") else 1)
# derived
A["rev_growth_pct"] = A.revenue.pct_change() * 100
A["gm_pct"] = A.gross_profit / A.revenue * 100
A["op_margin_pct"] = A.op_income / A.revenue * 100
A["fcf"] = A.cfo - A.capex
A["fcf_margin_pct"] = A.fcf / A.revenue * 100
A["fcf_conv_adj_ni_pct"] = A.fcf / A.adj_net_income * 100
A["net_debt"] = A.lt_debt - A.cash                       # borrowings (carrying) less cash; excludes operating leases
A["adj_ebitda"] = A.adj_op_income + A.da                 # my definition: non-GAAP EBIT + D&A (company does not publish EBITDA)
A["net_debt_to_adj_ebitda"] = A.net_debt / A.adj_ebitda
A["sbc_pct_rev"] = A.sbc / A.revenue * 100
A["sh_change_pct"] = A.sh_diluted.pct_change() * 100
A["marketing_pct_rev"] = A.marketing / A.revenue * 100
# ROIC = NOPAT / avg invested capital; NOPAT = adj EBIT x (1-18% non-GAAP tax rate, my assumption in line with company guidance);
# invested capital = equity + borrowings - cash (book, incl. HEYDUDE goodwill & intangibles)
A["invested_capital"] = A.equity + A.lt_debt - A.cash
A["roic_pct"] = A.adj_op_income * (1 - 0.18) / A.invested_capital.rolling(2).mean() * 100
A["crocs_op_margin_pct"] = A.crocs_op_inc / A.crocs_rev * 100
A["hd_op_inc_ex_impair"] = A.hd_op_inc; A.loc[2025, "hd_op_inc_ex_impair"] = A.loc[2025, "hd_op_inc"] + 737.0; A.loc[2024, "hd_op_inc_ex_impair"] = A.loc[2024, "hd_op_inc"] + 5.441
A["hd_op_margin_ex_impair_pct"] = A.hd_op_inc_ex_impair / A.hd_rev * 100
A.round(3).to_csv(os.path.join(D, "annual.csv"))

# ---------------- quarterly ----------------
Q = pd.read_csv(os.path.join(D, "quarterly_release_raw.csv"))
Q = Q[Q.year >= 2023].copy().set_index("period")
# YTD cash-flow items from releases -> quarterly
def ytd(key):
    out = {}
    for p in Q.index:
        r = json.load(open(os.path.join(D, f"release_rows_{p}.json")))
        # the cash flow statement is the first table in each release that contains these row labels (YTD column first)
        kk = [k for k in r if k.endswith("/" + key) and ("operating activities" in k or "investing activities" in k or "financing activities" in k or "operating assets" in k)]
        out[p] = (r[kk[0]][0] if kk else np.nan)
    return pd.Series(out)
def ytd_any(keys):
    s = ytd(keys[0])
    for k in keys[1:]: s = s.fillna(ytd(k))
    return s
for name, key in {"cfo_ytd": "Cash provided by operating activities", "capex_ytd": "Purchases of property, equipment, and software",
                  "sbc_ytd": "Share-based compensation", "buyback_ytd": "Repurchases of common stock, including excise tax", "da_ytd": "Depreciation and amortization"}.items():
    Q[name] = ytd(key)
Q["cfo_ytd"] = ytd_any(["Cash provided by operating activities", "Cash used in operating activities", "Cash provided by (used in) operating activities", "Cash (used in) provided by operating activities"])
Q["buyback_ytd"] = Q["buyback_ytd"].fillna(ytd("Repurchases of common stock"))
for c in ("cfo", "capex", "sbc", "buyback", "da"):
    y = Q[c + "_ytd"]; q = y.copy()
    for p in Q.index:
        yr, qq = int(p[:4]), int(p[-1])
        if qq > 1 and f"{yr}Q{qq-1}" in Q.index: q[p] = y[p] - y[f"{yr}Q{qq-1}"]
        elif qq > 1: q[p] = np.nan
    Q[c + "_q"] = q
Q["capex_q"] = Q["capex_q"].abs(); Q["buyback_q"] = Q["buyback_q"].abs()
Q["fcf_calc"] = Q.cfo_q - Q.capex_q
# segment note from 10-Qs / 10-K: income from operations and cost of sales by brand
segq = {}
def segparse(path):
    rows = {}; section = ""
    for ln in open(path).read().split("\n"):
        ln = ln.strip()
        if "|" not in ln:
            if ln.endswith(":") and len(ln) < 60: section = ln[:-1]
            continue
        parts = [p.strip() for p in ln.split("|")]
        vals = []
        for p in parts[1:]:
            s = p.replace(",", "").replace("$", "").replace(" ", "")
            neg = s.startswith("("); s = s.strip("()")
            try: vals.append(-float(s) if neg else float(s))
            except ValueError: pass
        lab = re.sub(r"\s*\(\d\)\s*$", "", parts[0])
        if vals: rows.setdefault(f"{section}/{lab}", vals)
    return rows
for f in sorted(glob.glob(os.path.join(B, "sec_txt", "*10-Q*.txt"))):
    m = re.search(r"crox-(\d{4})(\d\d)\d\d", f); y, mo = int(m.group(1)), int(m.group(2)); q = mo // 3
    r = segparse(f)
    for brand, tag in (("Crocs Brand", "crocs"), ("HEYDUDE Brand", "hd")):
        for lab, nm in (("Cost of sales", "cogs"), ("Selling, general and administrative expenses", "sga"), ("Income from operations", "opinc"), ("Income (loss) from operations", "opinc"), ("Revenues", "rev")):
            k = f"{brand}/{lab}"
            if k in r:
                segq.setdefault(f"{y}Q{q}", {})[f"{tag}_{nm}_seg"] = r[k][0] / 1e3
                segq.setdefault(f"{y-1}Q{q}", {}).setdefault(f"{tag}_{nm}_seg", r[k][1] / 1e3)
for f in sorted(glob.glob(os.path.join(B, "sec_txt", "*10-Q*.txt"))):
    m = re.search(r"crox-(\d{4})(\d\d)\d\d", f); y, mo = int(m.group(1)), int(m.group(2)); q = mo // 3
    for ln in open(f).read().split("\n"):
        mm = re.match(r"^(Crocs Brand|HEYDUDE Brand) income(?: \(loss\))? from operations \|(.*)", ln.strip())
        if not mm: continue
        tag = "crocs" if mm.group(1).startswith("Crocs") else "hd"
        v = []
        for x in mm.group(2).split("|")[:2]:
            x = x.strip().replace(",", ""); neg = x.startswith("("); v.append((-1 if neg else 1) * float(x.strip("()")) / 1e3)
        segq.setdefault(f"{y}Q{q}", {})[f"{tag}_opinc_seg"] = v[0]
        segq.setdefault(f"{y-1}Q{q}", {})[f"{tag}_opinc_seg"] = v[1]
S = pd.DataFrame(segq).T
Q = Q.join(S)
# Q4 = FY - 9M using annual segment table
for y in (2024, 2025):
    p = f"{y}Q4"
    if p not in Q.index: continue
    nine = Q.loc[[f"{y}Q1", f"{y}Q2", f"{y}Q3"]]
    Q.loc[p, "crocs_opinc_seg"] = A.loc[y, "crocs_op_inc"] - nine.crocs_opinc_seg.sum()
    Q.loc[p, "hd_opinc_seg"] = A.loc[y, "hd_op_inc"] - nine.hd_opinc_seg.sum()
    if nine.crocs_cogs_seg.notna().all():
        fy_c = A.loc[y, "crocs_rev"] * (1 - A.loc[y, "crocs_gm_pct"] / 100); fy_h = A.loc[y, "hd_rev"] * (1 - A.loc[y, "hd_gm_pct"] / 100)
        Q.loc[p, "crocs_cogs_seg"] = fy_c - nine.crocs_cogs_seg.sum(); Q.loc[p, "hd_cogs_seg"] = fy_h - nine.hd_cogs_seg.sum()
money = ["revenue", "revenue_py", "cogs", "gross_profit", "sga", "op_income", "interest_expense", "pretax", "tax", "net_income", "adj_gross_profit", "adj_sga", "adj_op_income",
         "adj_net_income", "crocs_rev", "hd_rev", "crocs_na", "crocs_intl", "crocs_na_whsl", "crocs_na_dtc", "crocs_intl_whsl", "crocs_intl_dtc", "crocs_whsl", "crocs_dtc", "hd_whsl", "hd_dtc",
         "cash", "inventories", "lt_borrowings", "fcf_q", "cfo_q", "capex_q", "sbc_q", "buyback_q", "da_q", "fcf_calc", "cfo_ytd", "capex_ytd"]
Q[money] = Q[money] / 1e3
Q["sh_diluted_m"] = Q.sh_diluted_gaap / 1e3
Q["gm_pct"] = Q.gross_profit / Q.revenue * 100
Q["op_margin_pct"] = Q.op_income / Q.revenue * 100
Q["crocs_gm_seg_pct"] = (1 - Q.crocs_cogs_seg / Q.crocs_rev) * 100
Q["hd_gm_seg_pct"] = (1 - Q.hd_cogs_seg / Q.hd_rev) * 100
Q["crocs_opm_seg_pct"] = Q.crocs_opinc_seg / Q.crocs_rev * 100
Q["hd_opinc_ex_impair"] = Q.hd_opinc_seg; Q.loc["2025Q2", "hd_opinc_ex_impair"] = Q.loc["2025Q2", "hd_opinc_seg"] + 737.0
Q["hd_opm_ex_impair_pct"] = Q.hd_opinc_ex_impair / Q.hd_rev * 100
Q["crocs_gm_use_pct"] = Q.crocs_adj_gm_pct.fillna(Q.crocs_gm_seg_pct)   # non-GAAP where published, else segment GAAP (identical when no adjustments)
Q["hd_gm_use_pct"] = Q.hd_adj_gm_pct.fillna(Q.hd_gm_seg_pct)
Q["net_debt"] = Q.lt_borrowings - Q.cash
for c in ("revenue", "crocs_rev", "hd_rev", "crocs_na", "crocs_intl", "crocs_dtc", "crocs_whsl", "hd_whsl", "hd_dtc", "adj_eps", "adj_op_income", "inventories"):
    Q[c + "_yoy_pct"] = Q[c].pct_change(4) * 100
Q["ttm_adj_ebitda"] = (Q.adj_op_income + Q.da_q).rolling(4).sum()
Q["ttm_fcf"] = Q.fcf_calc.rolling(4).sum()
Q["ttm_adj_eps"] = Q.adj_eps.rolling(4).sum()
Q["ttm_revenue"] = Q.revenue.rolling(4).sum()
Q["net_debt_to_ttm_ebitda"] = Q.net_debt / Q.ttm_adj_ebitda
Q["gaap_minus_adj_op_income"] = Q.op_income - Q.adj_op_income
Q.round(3).to_csv(os.path.join(D, "quarterly.csv"))
pd.set_option("display.width", 320); pd.set_option("display.max_columns", 80)
print(A[["revenue","rev_growth_pct","gm_pct","op_margin_pct","adj_op_margin_pct","adj_eps","eps_gaap","cfo","capex","fcf","fcf_margin_pct","fcf_conv_adj_ni_pct","net_debt","adj_ebitda","net_debt_to_adj_ebitda","sbc","sbc_pct_rev","sh_diluted","buybacks","roic_pct","marketing_pct_rev"]].round(1).to_string())
print(A[["crocs_rev","hd_rev","crocs_op_margin_pct","hd_op_margin_ex_impair_pct","crocs_na","crocs_intl","crocs_units_k","crocs_asp","hd_units_k","hd_asp"]].round(1).to_string())
print(Q[["revenue","revenue_yoy_pct","adj_gm_pct","adj_op_margin_pct","op_margin_pct","adj_eps","adj_eps_yoy_pct","cfo_q","capex_q","fcf_calc","fcf_q","buyback_q","sbc_q","net_debt","net_debt_to_ttm_ebitda","sh_diluted_m","ttm_fcf","ttm_adj_eps"]].round(1).to_string())
print(Q[["crocs_rev_yoy_pct","hd_rev_yoy_pct","crocs_na_yoy_pct","crocs_intl_yoy_pct","crocs_dtc_yoy_pct","crocs_whsl_yoy_pct","hd_whsl_yoy_pct","hd_dtc_yoy_pct","crocs_gm_seg_pct","hd_gm_seg_pct","crocs_opm_seg_pct","hd_opm_ex_impair_pct","inventories","inventories_yoy_pct"]].round(1).to_string())
