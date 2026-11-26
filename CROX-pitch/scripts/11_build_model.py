"""Build model.xlsx with LIVE formulas: inputs, history, 3 scenario forecasts, DCF, reverse DCF, sensitivities,
revenue-at-risk stress test, peers, quarterly data, checks.  Colour code: blue = hard-coded input, black = formula.
Run scripts/12_recalc_model.py afterwards (LibreOffice headless) to compute values and export data/derived/model_outputs.json."""
import os, json, pandas as pd, numpy as np
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
ROOT = os.path.join(os.path.dirname(__file__), ".."); D = os.path.join(ROOT, "data", "derived")
A = pd.read_csv(os.path.join(D, "annual.csv"), index_col=0); Q = pd.read_csv(os.path.join(D, "quarterly.csv"), index_col=0)
RAR = json.load(open(os.path.join(D, "revenue_at_risk.json"))); RT = pd.read_csv(os.path.join(D, "revenue_at_risk.csv"))
PEERS = pd.read_csv(os.path.join(D, "peers.csv"), index_col=0); RISK = json.load(open(os.path.join(D, "risk_stats.json")))
BLUE = Font(color="0000FF"); BOLD = Font(bold=True); HDR = PatternFill("solid", fgColor="1F3864"); HF = Font(bold=True, color="FFFFFF")
SUB = PatternFill("solid", fgColor="D9E1F2"); KEY = PatternFill("solid", fgColor="FFF2CC"); thin = Side(style="thin", color="999999")
wb = Workbook()
def sheet(name, widths=None):
    ws = wb.create_sheet(name); ws.sheet_view.showGridLines = False
    for i, w in enumerate(widths or [], 1): ws.column_dimensions[L(i)].width = w
    return ws
def put(ws, ref, v, fmt=None, inp=False, bold=False, fill=None):
    c = ws[ref]; c.value = v
    if fmt: c.number_format = fmt
    if inp: c.font = BLUE
    if bold: c.font = Font(bold=True, color=("0000FF" if inp else "000000"))
    if fill: c.fill = fill
    return c
def header(ws, row, labels, col0=1):
    for i, t in enumerate(labels):
        c = ws.cell(row=row, column=col0 + i, value=t); c.fill = HDR; c.font = HF; c.alignment = Alignment(horizontal="center", wrap_text=True)
def title(ws, text, sub=None):
    ws["A1"] = text; ws["A1"].font = Font(bold=True, size=14)
    if sub: ws["A2"] = sub; ws["A2"].font = Font(italic=True, color="666666")
PCT = "0.0%"; USD = '#,##0.0;(#,##0.0)'; USD0 = '#,##0;(#,##0)'; PS = '$#,##0.00'; X = '0.0"x"'

# ============================ README ============================
ws = wb.active; ws.title = "README"; ws.sheet_view.showGridLines = False; ws.column_dimensions["A"].width = 120
for i, t in enumerate([
    "Crocs, Inc. (NASDAQ: CROX) - pitch model", f"Price and market data as of {RISK['asof']} close. Fundamentals through Q3 2026 (10-Q filed 2026-10-29).",
    "", "COLOUR CODE: blue font = hard-coded input (reported, consensus or my assumption - labelled in column 'Basis'); black = live formula.",
    "SHEETS: Inputs | Hist | Assump (scenario drivers) | Bear / Base / Bull (forecast + DCF, identical formula structure) | Valuation (price targets, weights, expected return)",
    "        ReverseDCF | Sens (sensitivity tables) | RevAtRisk (proprietary fad stress test) | Peers | Quarterly | Checks",
    "UNITS: US$ millions except per-share data. Fiscal year = calendar year.",
    "LABELS: 'reported' = SEC filings; 'guidance' = company outlook 2026-10-29; 'consensus' = Yahoo Finance / Nasdaq (Zacks) as of 2026-11-26; 'my estimate' = analyst assumption.",
    "EPS is the company's non-GAAP ('adjusted') definition: 18% tax rate, excludes IEEPA tariff refunds, impairments and cost-programme charges.",
    "DCF uses a 22% cash tax rate (not the 18% non-GAAP rate) and does NOT add back stock comp - both deliberately conservative.",
    "Sources and as-of dates for every input: see sources.md in the pitch folder. Scripts that generate this file: scripts/11_build_model.py."], 1):
    ws.cell(row=i, column=1, value=t)
ws["A1"].font = Font(bold=True, size=14)

# ============================ Inputs ============================
ws = sheet("Inputs", [46, 16, 60]); title(ws, "Inputs - market data, capital structure, discount rate"); header(ws, 3, ["Item", "Value", "Basis / source"])
last = Q.iloc[-1]
inp = [("Share price (US$)", RISK["price"], PS, "Nasdaq close 2026-11-25", "price"),
       ("Shares outstanding (m)", 45.73, "0.00", "Market cap $7,313m / price (Nasdaq, StockAnalysis); 46.2m at 30-Sep-26 per 10-Q", "shares"),
       ("Dilutive securities (m)", 0.5, "0.00", "Q3-26 diluted less basic shares (press release): 0.54m", "dil"),
       ("Borrowings, face value 30-Sep-26", 1313.0, USD, "reported, 10-Q Q3-26 Note 7", "debt"),
       ("Cash and equivalents 30-Sep-26", 163.457, USD, "reported, 10-Q Q3-26", "cash"),
       ("Operating lease liabilities (memo, not in net debt)", 374.074, USD, "reported, 10-Q Q3-26 (90.8 + 283.3)", "leases"),
       ("Risk-free rate (10y UST)", 0.050, PCT, "approx. Nov-2026; sources disagree 4.84%-5.13% (see sources.md)", "rf"),
       ("Equity risk premium", 0.050, PCT, "my assumption", "erp"),
       ("Equity beta", 1.20, "0.00", "my calc: 5y weekly vs SPY = 1.21 (Yahoo 5y monthly 1.50; 2y weekly 0.67)", "beta"),
       ("Pre-tax cost of debt", 0.065, PCT, "my estimate: TLB at SOFR+2.25%, notes 4.125-4.25% trade at a discount", "kd"),
       ("Cash tax rate (DCF)", 0.22, PCT, "my assumption: GAAP ETR guidance ~23%; cash taxes paid 2025 $185m", "ctax"),
       ("Non-GAAP tax rate (EPS)", 0.18, PCT, "company guidance FY26", "ntax"),
       ("Terminal growth", 0.02, PCT, "my assumption", "g"),
       ("Net share dilution from stock comp (m per year)", 0.45, "0.00", "my estimate: issued shares rose 0.5m in 9M-26", "sbcdil")]
N = {}
for i, (lab, v, fmt, basis, key) in enumerate(inp, 4):
    ws[f"A{i}"] = lab; put(ws, f"B{i}", v, fmt, inp=True); ws[f"C{i}"] = basis; N[key] = f"Inputs!$B${i}"
r = 4 + len(inp) + 1
calc = [("Market capitalisation", f"={N['price']}*{N['shares']}", USD, "mcap"), ("Net debt (borrowings less cash)", f"={N['debt']}-{N['cash']}", USD, "nd"),
        ("Enterprise value", f"=B{r}+B{r+1}", USD, "ev"), ("Cost of equity (CAPM)", f"={N['rf']}+{N['beta']}*{N['erp']}", PCT, "ke"),
        ("Equity weight", f"=B{r}/(B{r}+{N['debt']})", PCT, "we"), ("WACC", f"=B{r+4}*B{r+3}+(1-B{r+4})*{N['kd']}*(1-{N['ctax']})", PCT, "wacc_calc"),
        ("WACC used (rounded, input)", 0.10, PCT, "wacc")]
for j, (lab, f, fmt, key) in enumerate(calc):
    ws[f"A{r+j}"] = lab; put(ws, f"B{r+j}", f, fmt, inp=(key == "wacc"), bold=(key in ("ev", "wacc")), fill=(KEY if key == "wacc" else None)); N[key] = f"Inputs!$B${r+j}"
ws[f"C{r+6}"] = "my assumption: computed WACC rounded; sensitivity in 'Sens'"

# ============================ Hist ============================
ws = sheet("Hist", [44] + [12] * 6 + [50]); title(ws, "Historical financials FY2021-FY2025 (reported) and derived ratios", "US$ m. Source: 10-K filings (XBRL), Q4 earnings releases for non-GAAP. Derived rows are formulas.")
yrs = [2021, 2022, 2023, 2024, 2025]; header(ws, 4, ["US$ m"] + [f"FY{y}" for y in yrs] + ["", "Basis"])
hrows = [("Crocs Brand - North America", "crocs_na"), ("Crocs Brand - International", "crocs_intl"), ("HEYDUDE Brand", "hd_rev"), ("Revenue", "revenue"), ("Gross profit (GAAP)", "gross_profit"),
         ("SG&A incl. impairments excluded (GAAP SG&A)", "sga"), ("Operating income (GAAP)", "op_income"), ("Adjusted operating income (non-GAAP)", "adj_op_income"),
         ("Adjusted diluted EPS (non-GAAP, $)", "adj_eps"), ("GAAP diluted EPS ($)", "eps_gaap"), ("D&A", "da"), ("Stock-based compensation", "sbc"),
         ("Cash from operations", "cfo"), ("Capex", "capex"), ("Share repurchases", "buybacks"), ("Borrowings (carrying value)", "lt_debt"), ("Cash", "cash"),
         ("Diluted shares (weighted avg, m)", "sh_diluted"), ("Crocs Brand segment operating income", "crocs_op_inc"), ("HEYDUDE segment operating income ex-impairment", "hd_op_inc_ex_impair"),
         ("Marketing expense", "marketing"), ("Crocs Brand pairs sold (m)", "crocs_units_k"), ("HEYDUDE pairs sold (m)", "hd_units_k")]
H = {}
for i, (lab, key) in enumerate(hrows, 5):
    ws[f"A{i}"] = lab; H[key] = i
    for j, y in enumerate(yrs):
        v = A.loc[y, key] if key in A.columns else None
        if key in ("crocs_units_k", "hd_units_k") and pd.notna(v): v = v / 1000.0
        if v is not None and pd.notna(v): put(ws, f"{L(2+j)}{i}", round(float(v), 3), ("0.00" if "eps" in key else USD), inp=True)
    ws[f"H{i}"] = "reported"
r0 = 5 + len(hrows) + 1; ws[f"A{r0-1}"] = "Derived (formulas)"; ws[f"A{r0-1}"].font = BOLD
der = [("Revenue growth", lambda c, p: f"={c}{H['revenue']}/{p}{H['revenue']}-1" if p else None, PCT),
       ("Gross margin", lambda c, p: f"={c}{H['gross_profit']}/{c}{H['revenue']}", PCT),
       ("Adjusted operating margin", lambda c, p: f"={c}{H['adj_op_income']}/{c}{H['revenue']}", PCT),
       ("GAAP operating margin", lambda c, p: f"={c}{H['op_income']}/{c}{H['revenue']}", PCT),
       ("Free cash flow (CFO - capex)", lambda c, p: f"={c}{H['cfo']}-{c}{H['capex']}", USD),
       ("FCF margin", lambda c, p: f"=({c}{H['cfo']}-{c}{H['capex']})/{c}{H['revenue']}", PCT),
       ("Adjusted EBITDA (adj. EBIT + D&A)", lambda c, p: f"={c}{H['adj_op_income']}+{c}{H['da']}", USD),
       ("Net debt", lambda c, p: f"={c}{H['lt_debt']}-{c}{H['cash']}", USD),
       ("Net debt / adjusted EBITDA", lambda c, p: f"=({c}{H['lt_debt']}-{c}{H['cash']})/({c}{H['adj_op_income']}+{c}{H['da']})", X),
       ("Stock comp % revenue", lambda c, p: f"={c}{H['sbc']}/{c}{H['revenue']}", PCT),
       ("Change in diluted shares", lambda c, p: f"={c}{H['sh_diluted']}/{p}{H['sh_diluted']}-1" if p else None, PCT),
       ("Adjusted EPS growth", lambda c, p: f"={c}{H['adj_eps']}/{p}{H['adj_eps']}-1" if p else None, PCT),
       ("International share of Crocs Brand", lambda c, p: f"={c}{H['crocs_intl']}/({c}{H['crocs_intl']}+{c}{H['crocs_na']})", PCT),
       ("Crocs Brand segment margin", lambda c, p: f"={c}{H['crocs_op_inc']}/({c}{H['crocs_na']}+{c}{H['crocs_intl']})", PCT),
       ("HEYDUDE segment margin ex-impairment", lambda c, p: f"=IF({c}{H['hd_rev']}=0,\"n/a\",{c}{H['hd_op_inc_ex_impair']}/{c}{H['hd_rev']})", PCT),
       ("Marketing % revenue", lambda c, p: f"={c}{H['marketing']}/{c}{H['revenue']}", PCT)]
for i, (lab, fn, fmt) in enumerate(der, r0):
    ws[f"A{i}"] = lab
    for j in range(5):
        f = fn(L(2 + j), L(1 + j) if j > 0 else None)
        if f: put(ws, f"{L(2+j)}{i}", f, fmt)

# ============================ Assump ============================
ws = sheet("Assump", [46] + [11] * 6 + [58]); title(ws, "Scenario assumptions (all blue cells are my estimates unless stated)", "FY2026E is common to all scenarios and anchored on company guidance of 2026-10-29.")
FY = [2026, 2027, 2028, 2029, 2030, 2031]
base26 = {"na": 1679.0, "intl": 1780.0, "hd": 715.0, "margin": 0.226, "int": 77.0, "other": -3.0, "shares_avg": 48.70, "shares_end": 45.00, "nd_end": 1050.0}
header(ws, 4, ["FY2026E (common)", "Value", "", "", "", "", "", "Basis"])
c26 = [("Crocs NA revenue", base26["na"], USD, "9M-26 reported 1,243.0 + Q4E ~436 (flat y/y, my est.); FY -1.8%"),
       ("Crocs International revenue", base26["intl"], USD, "Guidance: Crocs Brand ~+4% => ~3,459; international = remainder (+10.1%)"),
       ("HEYDUDE revenue", base26["hd"], USD, "Guidance: ~flat vs FY25 $714.8m"),
       ("Adjusted EBIT margin", base26["margin"], PCT, "Guidance: 'expand modestly from 22.5%'; 9M 23.3%, Q4 guide ~20.5%"),
       ("Net interest expense", base26["int"], USD, "9M-26 ex refund interest ~58 + Q4E ~19"),
       ("Other / FX", base26["other"], USD, "9M-26 FX and other -3.1"),
       ("Average diluted shares (m)", base26["shares_avg"], "0.00", "Q1 50.7 / Q2 49.6 / Q3 48.0 / Q4E ~46.6 (my est.)"),
       ("Year-end shares outstanding (m)", base26["shares_end"], "0.00", "45.73m latest less ~0.7m Q4 buyback (my est.)"),
       ("Year-end net debt", base26["nd_end"], USD, "Net debt 1,150 at Q3 less Q4 FCF ~250 plus Q4 buybacks ~150 (my est.)")]
C26 = {}
for i, (lab, v, fmt, basis) in enumerate(c26, 5):
    ws[f"A{i}"] = lab; put(ws, f"B{i}", v, fmt, inp=True); ws[f"H{i}"] = basis; C26[lab] = f"Assump!$B${i}"
drivers = [("Crocs NA revenue growth", PCT), ("Crocs International revenue growth", PCT), ("HEYDUDE revenue growth", PCT), ("Adjusted EBIT margin", PCT),
           ("D&A % revenue", PCT), ("Capex % revenue", PCT), ("NWC investment % of revenue change", PCT), ("Interest rate on average net debt", PCT),
           ("Buybacks as % of free cash flow", PCT), ("Average buyback price ($)", PS), ("Exit P/E (NTM) at Dec-2027", X), ("Probability", PCT)]
SC = {"Bear": {"Crocs NA revenue growth": [-0.08, -0.08, -0.03, 0.0, 0.0], "Crocs International revenue growth": [0.02, 0.0, 0.02, 0.02, 0.02], "HEYDUDE revenue growth": [-0.10, -0.08, -0.03, 0.0, 0.0],
               "Adjusted EBIT margin": [0.205, 0.185, 0.185, 0.19, 0.19], "Buybacks as % of free cash flow": [0.70] * 5, "Average buyback price ($)": [120, 90, 95, 100, 105], "Exit": 7.0, "P": 0.25,
               "note": "Fad partially unwinds: NA clog demand falls again, international stalls, HEYDUDE relapses; ~60% decremental margin. Multiple = 25th percentile of 5y range."},
      "Base": {"Crocs NA revenue growth": [0.0, 0.01, 0.01, 0.01, 0.01], "Crocs International revenue growth": [0.09, 0.08, 0.07, 0.06, 0.05], "HEYDUDE revenue growth": [0.04, 0.03, 0.03, 0.02, 0.02],
               "Adjusted EBIT margin": [0.228, 0.230, 0.230, 0.230, 0.230], "Buybacks as % of free cash flow": [0.85] * 5, "Average buyback price ($)": [175, 190, 205, 220, 235], "Exit": 10.5, "P": 0.50,
               "note": "Management 2027 colour (Crocs ~+4%, HEYDUDE LSD-MSD); NA flat incl. marketplace shift; margins flat (tariff relief offsets DTC mix/oil). Multiple ~ today's."},
      "Bull": {"Crocs NA revenue growth": [0.03, 0.03, 0.02, 0.02, 0.02], "Crocs International revenue growth": [0.13, 0.11, 0.09, 0.08, 0.06], "HEYDUDE revenue growth": [0.08, 0.06, 0.05, 0.04, 0.03],
               "Adjusted EBIT margin": [0.235, 0.243, 0.245, 0.245, 0.245], "Buybacks as % of free cash flow": [0.90] * 5, "Average buyback price ($)": [190, 230, 260, 285, 310], "Exit": 13.0, "P": 0.25,
               "note": "NA returns to growth, international compounds at low-teens, HEYDUDE recovers; margin recaptures ~1/3 of the 2023-25 loss. Multiple still a ~30% discount to S&P 500 (18.3x)."}}
COMMON = {"D&A % revenue": [0.020] * 5, "Capex % revenue": [0.019] * 5, "NWC investment % of revenue change": [0.08] * 5, "Interest rate on average net debt": [0.065] * 5}
AS = {}; r = 16
for sc in ("Bear", "Base", "Bull"):
    ws[f"A{r}"] = f"{sc} case"; ws[f"A{r}"].font = Font(bold=True, size=12); ws[f"H{r}"] = SC[sc]["note"]
    header(ws, r + 1, ["Driver", "FY2027E", "FY2028E", "FY2029E", "FY2030E", "FY2031E"])
    for k, (dname, fmt) in enumerate(drivers):
        rr = r + 2 + k; ws[f"A{rr}"] = dname; AS[(sc, dname)] = rr
        if dname == "Exit P/E (NTM) at Dec-2027": put(ws, f"B{rr}", SC[sc]["Exit"], fmt, inp=True)
        elif dname == "Probability": put(ws, f"B{rr}", SC[sc]["P"], fmt, inp=True)
        else:
            vals = SC[sc].get(dname) or COMMON[dname]
            for j, v in enumerate(vals): put(ws, f"{L(2+j)}{rr}", v, fmt, inp=True)
    r += len(drivers) + 4

# ============================ Scenario sheets ============================
SR = {}
def scen_sheet(sc):
    ws = sheet(sc, [44] + [13] * 7 + [44]); title(ws, f"{sc} case - forecast, EPS bridge and DCF", "US$ m. FY2025A reported; FY2026E common base; FY2027E-31E from 'Assump'. All cells are formulas.")
    header(ws, 4, ["US$ m", "FY2025A", "FY2026E", "FY2027E", "FY2028E", "FY2029E", "FY2030E", "FY2031E", "Notes"])
    R = {}; names = ["na", "intl", "crocs", "hd", "rev", "g", "margin", "ebit", "da", "ebitda", "int", "other", "pbt", "tax", "ni", "sh_avg", "eps", "epsg", "_b1",
                     "capex", "nwc", "ctax", "fcf", "bb", "bbpx", "sh_rep", "sh_end", "nd", "lev", "_b2", "fcff", "t", "df", "pv", "_b3"]
    labels = {"na": "Crocs Brand - North America", "intl": "Crocs Brand - International", "crocs": "Crocs Brand revenue", "hd": "HEYDUDE revenue", "rev": "Total revenue", "g": "  growth",
              "margin": "Adjusted EBIT margin", "ebit": "Adjusted EBIT", "da": "D&A", "ebitda": "Adjusted EBITDA", "int": "Net interest expense", "other": "Other / FX", "pbt": "Adjusted pre-tax income",
              "tax": "Tax at non-GAAP rate", "ni": "Adjusted net income", "sh_avg": "Average diluted shares (m)", "eps": "Adjusted diluted EPS ($)", "epsg": "  growth",
              "capex": "Capex", "nwc": "Working-capital investment", "ctax": "Cash taxes (cash tax rate on pre-tax)", "fcf": "Free cash flow to equity (no SBC add-back)", "bb": "Share repurchases",
              "bbpx": "Average repurchase price ($)", "sh_rep": "Shares repurchased (m)", "sh_end": "Year-end shares outstanding (m)", "nd": "Year-end net debt", "lev": "Net debt / adj. EBITDA",
              "fcff": "Unlevered FCF (EBIT x (1-cash tax) + D&A - capex - NWC)", "t": "Discount period (mid-year, from 31-Dec-26)", "df": "Discount factor", "pv": "PV of unlevered FCF"}
    for i, n in enumerate(names, 5):
        R[n] = i
        if not n.startswith("_"): ws[f"A{i}"] = labels[n]
    for n in ("rev", "ebit", "ni", "eps", "fcf"): ws[f"A{R[n]}"].font = BOLD
    a = lambda d, col: f"Assump!{col}${AS[(sc, d)]}"
    # FY2025A (col B)
    put(ws, f"B{R['na']}", f"=Hist!F{H['crocs_na']}", USD); put(ws, f"B{R['intl']}", f"=Hist!F{H['crocs_intl']}", USD); put(ws, f"B{R['hd']}", f"=Hist!F{H['hd_rev']}", USD)
    put(ws, f"B{R['crocs']}", f"=B{R['na']}+B{R['intl']}", USD); put(ws, f"B{R['rev']}", f"=B{R['crocs']}+B{R['hd']}", USD)
    put(ws, f"B{R['ebit']}", f"=Hist!F{H['adj_op_income']}", USD); put(ws, f"B{R['margin']}", f"=B{R['ebit']}/B{R['rev']}", PCT); put(ws, f"B{R['da']}", f"=Hist!F{H['da']}", USD)
    put(ws, f"B{R['ebitda']}", f"=B{R['ebit']}+B{R['da']}", USD); put(ws, f"B{R['eps']}", f"=Hist!F{H['adj_eps']}", "0.00"); put(ws, f"B{R['sh_avg']}", f"=Hist!F{H['sh_diluted']}", "0.00")
    put(ws, f"B{R['nd']}", f"=Hist!F{H['lt_debt']}-Hist!F{H['cash']}", USD)
    # FY2026E (col C)
    put(ws, f"C{R['na']}", f"={C26['Crocs NA revenue']}", USD); put(ws, f"C{R['intl']}", f"={C26['Crocs International revenue']}", USD); put(ws, f"C{R['hd']}", f"={C26['HEYDUDE revenue']}", USD)
    put(ws, f"C{R['margin']}", f"={C26['Adjusted EBIT margin']}", PCT); put(ws, f"C{R['int']}", f"={C26['Net interest expense']}", USD); put(ws, f"C{R['other']}", f"={C26['Other / FX']}", USD)
    put(ws, f"C{R['sh_avg']}", f"={C26['Average diluted shares (m)']}", "0.00"); put(ws, f"C{R['sh_end']}", f"={C26['Year-end shares outstanding (m)']}", "0.00"); put(ws, f"C{R['nd']}", f"={C26['Year-end net debt']}", USD)
    put(ws, f"C{R['da']}", f"=C{R['rev']}*Assump!B{AS[(sc,'D&A % revenue')]}", USD)
    for j, col in enumerate("DEFGH"):
        p = L(2 + j + 1); ac = L(2 + j)   # prev column in this sheet; assumption column in Assump (B..F)
        put(ws, f"{col}{R['na']}", f"={p}{R['na']}*(1+{a('Crocs NA revenue growth', ac)})", USD)
        put(ws, f"{col}{R['intl']}", f"={p}{R['intl']}*(1+{a('Crocs International revenue growth', ac)})", USD)
        put(ws, f"{col}{R['hd']}", f"={p}{R['hd']}*(1+{a('HEYDUDE revenue growth', ac)})", USD)
        put(ws, f"{col}{R['margin']}", f"={a('Adjusted EBIT margin', ac)}", PCT)
        put(ws, f"{col}{R['da']}", f"={col}{R['rev']}*{a('D&A % revenue', ac)}", USD)
        put(ws, f"{col}{R['int']}", f"={p}{R['nd']}*{a('Interest rate on average net debt', ac)}", USD)
        put(ws, f"{col}{R['other']}", 0, USD)
        put(ws, f"{col}{R['capex']}", f"={col}{R['rev']}*{a('Capex % revenue', ac)}", USD)
        put(ws, f"{col}{R['nwc']}", f"=({col}{R['rev']}-{p}{R['rev']})*{a('NWC investment % of revenue change', ac)}", USD)
        put(ws, f"{col}{R['ctax']}", f"={col}{R['pbt']}*{N['ctax']}", USD)
        put(ws, f"{col}{R['fcf']}", f"={col}{R['ebitda']}-{col}{R['int']}+{col}{R['other']}-{col}{R['ctax']}-{col}{R['capex']}-{col}{R['nwc']}", USD)
        put(ws, f"{col}{R['bb']}", f"=MAX(0,{col}{R['fcf']})*{a('Buybacks as % of free cash flow', ac)}", USD)
        put(ws, f"{col}{R['bbpx']}", f"={a('Average buyback price ($)', ac)}", PS)
        put(ws, f"{col}{R['sh_rep']}", f"={col}{R['bb']}/{col}{R['bbpx']}", "0.00")
        put(ws, f"{col}{R['sh_end']}", f"={p}{R['sh_end']}-{col}{R['sh_rep']}+{N['sbcdil']}", "0.00")
        put(ws, f"{col}{R['sh_avg']}", f"=AVERAGE({p}{R['sh_end']},{col}{R['sh_end']})+{N['dil']}", "0.00")
        put(ws, f"{col}{R['nd']}", f"={p}{R['nd']}-{col}{R['fcf']}+{col}{R['bb']}", USD)
        put(ws, f"{col}{R['fcff']}", f"={col}{R['ebit']}*(1-{N['ctax']})+{col}{R['da']}-{col}{R['capex']}-{col}{R['nwc']}", USD)
        put(ws, f"{col}{R['t']}", j + 0.5, "0.0"); put(ws, f"{col}{R['df']}", f"=1/(1+{N['wacc']})^{col}{R['t']}", "0.000"); put(ws, f"{col}{R['pv']}", f"={col}{R['fcff']}*{col}{R['df']}", USD)
    for col in "CDEFGH":
        p = L("ABCDEFGH".index(col))
        put(ws, f"{col}{R['crocs']}", f"={col}{R['na']}+{col}{R['intl']}", USD); put(ws, f"{col}{R['rev']}", f"={col}{R['crocs']}+{col}{R['hd']}", USD)
        put(ws, f"{col}{R['g']}", f"={col}{R['rev']}/{p}{R['rev']}-1", PCT); put(ws, f"{col}{R['ebit']}", f"={col}{R['rev']}*{col}{R['margin']}", USD)
        put(ws, f"{col}{R['ebitda']}", f"={col}{R['ebit']}+{col}{R['da']}", USD); put(ws, f"{col}{R['pbt']}", f"={col}{R['ebit']}-{col}{R['int']}+{col}{R['other']}", USD)
        put(ws, f"{col}{R['tax']}", f"={col}{R['pbt']}*{N['ntax']}", USD); put(ws, f"{col}{R['ni']}", f"={col}{R['pbt']}-{col}{R['tax']}", USD)
        put(ws, f"{col}{R['eps']}", f"={col}{R['ni']}/{col}{R['sh_avg']}", "0.00"); put(ws, f"{col}{R['epsg']}", f"={col}{R['eps']}/{p}{R['eps']}-1", PCT)
        put(ws, f"{col}{R['lev']}", f"={col}{R['nd']}/{col}{R['ebitda']}", X)
    put(ws, f"B{R['lev']}", f"=B{R['nd']}/B{R['ebitda']}", X)
    ws[f"I{R['eps']}"] = "FY26 guidance $14.45-14.65; consensus FY26 $14.63, FY27 $16.01 (Yahoo)"; ws[f"I{R['fcf']}"] = "after interest and cash tax; SBC treated as a cash cost"
    ws[f"I{R['int']}"] = "prior year-end net debt x rate (avoids circularity)"; ws[f"I{R['sh_avg']}"] = "avg of opening/closing shares + dilutive securities"
    # DCF block
    d0 = R["_b3"] + 1; ws[f"A{d0}"] = "DCF (valuation date 31-Dec-2026)"; ws[f"A{d0}"].font = Font(bold=True, size=12)
    dcf = [("Sum of PV of FCF FY27-31", f"=SUM(D{R['pv']}:H{R['pv']})", USD, "sumpv"), ("Terminal value (Gordon growth on FY31 FCF)", f"=H{R['fcff']}*(1+{N['g']})/({N['wacc']}-{N['g']})", USD, "tv"),
           ("PV of terminal value", f"=B{d0+2}*H{R['df']}", USD, "pvtv"), ("Enterprise value", f"=B{d0+1}+B{d0+3}", USD, "ev"), ("Less net debt (31-Dec-26E)", f"=C{R['nd']}", USD, "nd"),
           ("Equity value", f"=B{d0+4}-B{d0+5}", USD, "eq"), ("Diluted shares (31-Dec-26E, m)", f"=C{R['sh_end']}+{N['dil']}", "0.00", "sh"),
           ("DCF value per share ($)", f"=B{d0+6}/B{d0+7}", PS, "dcf"), ("  vs current price", f"=B{d0+8}/{N['price']}-1", PCT, "dcf_up"),
           ("Terminal value % of EV", f"=B{d0+3}/B{d0+4}", PCT, "tvpct"), ("Implied EV / FY27E EBITDA", f"=B{d0+4}/D{R['ebitda']}", X, "evx"),
           ("Price target Dec-2027 = exit P/E x FY2028E EPS ($)", f"=Assump!B{AS[(sc,'Exit P/E (NTM) at Dec-2027')]}*E{R['eps']}", PS, "pt"),
           ("  vs current price", f"=B{d0+12}/{N['price']}-1", PCT, "pt_up"), ("Exit P/E applied", f"=Assump!B{AS[(sc,'Exit P/E (NTM) at Dec-2027')]}", X, "exit"),
           ("FY27E EPS vs consensus $16.01 (Yahoo)", f"=D{R['eps']}/Peers!$B$22-1", PCT, "vs_cons"), ("EPS CAGR FY26E-FY29E", f"=(F{R['eps']}/C{R['eps']})^(1/3)-1", PCT, "cagr"),
           ("Revenue CAGR FY26E-FY31E", f"=(H{R['rev']}/C{R['rev']})^(1/5)-1", PCT, "rcagr"), ("Cumulative buybacks FY27-29E", f"=SUM(D{R['bb']}:F{R['bb']})", USD, "cumbb")]
    S = {}
    for k, (lab, f, fmt, key) in enumerate(dcf, d0 + 1):
        ws[f"A{k}"] = lab; put(ws, f"B{k}", f, fmt, bold=(key in ("dcf", "pt")), fill=(KEY if key in ("dcf", "pt") else None)); S[key] = f"{sc}!$B${k}"
    SR[sc] = (R, S)
for sc in ("Bear", "Base", "Bull"): scen_sheet(sc)

# ============================ Valuation ============================
ws = sheet("Valuation", [46, 14, 14, 14, 16, 50]); title(ws, "Valuation summary - price targets, probability weights, expected return", "Price target horizon: December 2027 (about 13 months). PT = exit P/E x FY2028E EPS; DCF is the cross-check.")
header(ws, 4, ["", "Bear", "Base", "Bull", "Prob-weighted", "Comment"])
vr = [("Probability", lambda sc: f"=Assump!B{AS[(sc,'Probability')]}", PCT, "=SUM(B5:D5)"), ("FY2027E adj. EPS ($)", lambda sc: f"={sc}!D{SR[sc][0]['eps']}", "0.00", "=SUMPRODUCT($B$5:$D$5,B6:D6)"),
      ("FY2028E adj. EPS ($)", lambda sc: f"={sc}!E{SR[sc][0]['eps']}", "0.00", "=SUMPRODUCT($B$5:$D$5,B7:D7)"), ("Exit P/E (NTM)", lambda sc: f"={SR[sc][1]['exit']}", X, None),
      ("Price target Dec-2027 ($)", lambda sc: f"={SR[sc][1]['pt']}", PS, "=SUMPRODUCT($B$5:$D$5,B9:D9)"), ("Return vs current price", lambda sc: f"=B9/{N['price']}-1".replace("B9", "{c}9"), PCT, f"=E9/{N['price']}-1"),
      ("DCF value per share today ($)", lambda sc: f"={SR[sc][1]['dcf']}", PS, "=SUMPRODUCT($B$5:$D$5,B11:D11)"), ("DCF vs current price", lambda sc: "={c}11/" + N['price'] + "-1", PCT, f"=E11/{N['price']}-1"),
      ("Revenue CAGR FY26E-31E", lambda sc: f"={SR[sc][1]['rcagr']}", PCT, None), ("FY2028E adj. EBIT margin", lambda sc: f"={sc}!E{SR[sc][0]['margin']}", PCT, None),
      ("FY2027E EPS vs consensus $16.01", lambda sc: f"={SR[sc][1]['vs_cons']}", PCT, None), ("FY2028E net debt / EBITDA", lambda sc: f"={sc}!E{SR[sc][0]['lev']}", X, None)]
for i, (lab, fn, fmt, tot) in enumerate(vr, 5):
    ws[f"A{i}"] = lab
    for j, sc in enumerate(("Bear", "Base", "Bull")):
        c = L(2 + j); put(ws, f"{c}{i}", fn(sc).replace("{c}", c), fmt)
    if tot: put(ws, f"E{i}", tot, fmt, bold=True)
for rr in (9, 10): 
    for c in "ABCDE": ws[f"{c}{rr}"].fill = KEY
ws["A19"] = "Key outputs"; ws["A19"].font = Font(bold=True, size=12)
ko = [("Current price ($)", f"={N['price']}", PS), ("Base-case price target ($)", "=C9", PS), ("Base-case upside", "=C10", PCT), ("Probability-weighted value ($)", "=E9", PS),
      ("Expected return (probability-weighted)", "=E10", PCT), ("Bear-case downside", "=B10", PCT), ("Bull-case upside", "=D10", PCT),
      ("Upside/downside ratio, base vs bear (x)", "=C10/-B10", '0.00"x"'), ("Upside/downside ratio, probability-weighted (x)", "=(C5*C10+D5*D10)/(-B5*B10)", '0.00"x"'),
      ("Break-even bear probability (EV = 0, base:bull kept 2:1)", "=(2/3*C10+1/3*D10)/((2/3*C10+1/3*D10)-B10)", PCT),
      ("P/E on FY27E consensus EPS (Yahoo $16.01)", f"={N['price']}/Peers!$B$22", X), ("P/E on my FY27E base EPS", f"={N['price']}/C6", X),
      ("FCF yield, TTM ($754m / market cap)", f"=Quarterly!$B$3/{N['mcap']}", PCT), ("EV / TTM adjusted EBITDA", f"={N['ev']}/Quarterly!$B$4", X),
      ("Market-implied probability of the bear case (base:bull 2:1)", f"=((2/3*C9+1/3*D9)-{N['price']}*1.11)/((2/3*C9+1/3*D9)-B9)", PCT)]
VK = {}
for i, (lab, f, fmt) in enumerate(ko, 20):
    ws[f"A{i}"] = lab; put(ws, f"B{i}", f, fmt, bold=True); VK[lab] = f"Valuation!$B${i}"
ws["F34"] = "Price x (1 + 11% cost of equity for 13 months ~ 1.11) = PT the market needs; solves p_bear given my three PTs."
ws["F29"] = "Bear probability at which the expected return is zero."

# ============================ ReverseDCF ============================
ws = sheet("ReverseDCF", [48, 14] + [12] * 7); title(ws, "Reverse DCF - what does $159.93 imply?", "10-year explicit period then terminal growth. Closed-form geometric sums, so every cell is live.")
rd = [("Enterprise value today", f"={N['ev']}", USD), ("TTM revenue (to Sep-26)", "=Quarterly!$B$2", USD), ("TTM adjusted EBIT margin", "=Quarterly!$B$5/Quarterly!$B$2", PCT),
      ("Cash tax rate", f"={N['ctax']}", PCT), ("Reinvestment (capex + NWC - D&A) % of NOPAT", 0.03, PCT), ("WACC", f"={N['wacc']}", PCT), ("Terminal growth after year 10", f"={N['g']}", PCT),
      ("TTM unlevered FCF = revenue x margin x (1-tax) x (1-reinvestment)", "=B5*B6*(1-B7)*(1-B8)", USD),
      ("(1) Implied perpetual FCF growth, single-stage: g = (EV x WACC - FCF) / (EV + FCF)", "=(B4*B9-B11)/(B4+B11)", "0.0%"),
      ("(2) Implied flat EBIT margin forever at 0% growth: margin = EV x WACC / (rev x (1-t) x (1-reinv))", "=B4*B9/(B5*(1-B7)*(1-B8))", PCT)]
for i, (lab, f, fmt) in enumerate(rd, 4):
    ws[f"A{i}"] = lab; put(ws, f"B{i}", f, fmt, inp=(i == 8), bold=(i >= 12))
ws["C8"] = "my assumption (FY27E base: capex 1.9% + NWC 0.3% - D&A 2.0% of revenue, vs NOPAT ~18% of revenue)"
ws["A16"] = "(3) Implied share price for 10-year revenue CAGR (rows) x steady-state adjusted EBIT margin (columns)"; ws["A16"].font = BOLD
margins = [0.16, 0.18, 0.20, 0.22, 0.226, 0.24, 0.26]; growths = [-0.04, -0.02, 0.0, 0.02, 0.04, 0.06, 0.08]
ws["A17"] = "10y revenue CAGR \\ EBIT margin"
for j, m in enumerate(margins): put(ws, f"{L(2+j)}17", m, PCT, inp=True, bold=True)
for i, g in enumerate(growths):
    rr = 18 + i; put(ws, f"A{rr}", g, PCT, inp=True, bold=True)
    for j in range(len(margins)):
        c = L(2 + j); q = f"((1+$A{rr})/(1+$B$9))"
        f0 = f"($B$5*{c}$17*(1-$B$7)*(1-$B$8))"
        pv = f"IF(ABS({q}-1)<0.000001,{f0}*10,{f0}*{q}*(1-{q}^10)/(1-{q}))"
        tv = f"{f0}*(1+$A{rr})^10*(1+$B$10)/(($B$9-$B$10)*(1+$B$9)^10)"
        put(ws, f"{c}{rr}", f"=(({pv})+({tv})-{N['nd']})/({N['shares']}+{N['dil']})", '$#,##0')
ws["A26"] = "Read-across: find today's price in the grid. At the current 22-23% margin the market is paying for roughly 0% revenue growth for a decade."
ws["A28"] = "(4) Implied 10-year revenue CAGR at the TTM margin (interpolated from the grid row values at the TTM-margin column)"; ws["A28"].font = BOLD
# linear interpolation between the bracketing growth rows in the 22.6% column (F)
ws["A29"] = "Implied 10y revenue CAGR at 22.6% margin"
put(ws, "B29", f"=FORECAST({N['price']},A18:A24,F18:F24)", "0.0%", bold=True); ws["C29"] = "linear fit across the grid column (approximation)"

# ============================ RevAtRisk ============================
ws = sheet("RevAtRisk", [46, 14, 12, 9, 11, 14, 30]); title(ws, "Proprietary analysis - how much of Crocs is a fad? Revenue-at-risk score and stress test",
      "Risk scored = brand-heat reversal (demand falls as the fashion cycle turns). Score 1-5 per line is MY subjective input (blue). Revenue is TTM to Sep-2026.")
header(ws, 4, ["Revenue line", "TTM revenue", "% of group", "Score 1-5", "Haircut", "Revenue at risk", "Revenue basis"])
n = len(RT)
for i, row in RT.iterrows():
    rr = 5 + i; ws[f"A{rr}"] = row["line"]; put(ws, f"B{rr}", round(row.ttm_revenue_usd_m, 1), USD, inp=True); put(ws, f"C{rr}", f"=B{rr}/$B${5+n}", PCT)
    put(ws, f"D{rr}", int(row.score), "0", inp=True, fill=KEY); put(ws, f"E{rr}", f"=INDEX($B${9+n}:$F${9+n},D{rr})", PCT); put(ws, f"F{rr}", f"=B{rr}*E{rr}", USD); ws[f"G{rr}"] = row.basis
t = 5 + n; ws[f"A{t}"] = "Group"; ws[f"A{t}"].font = BOLD; put(ws, f"B{t}", f"=SUM(B5:B{t-1})", USD, bold=True); put(ws, f"F{t}", f"=SUM(F5:F{t-1})", USD, bold=True); put(ws, f"E{t}", f"=F{t}/B{t}", PCT, bold=True, fill=KEY)
ws[f"G{t}"] = "<- % of group revenue at risk"
ws[f"A{t+2}"] = "Score -> 2-year cumulative revenue decline if the fad unwinds (my assumption; score 5 calibrated to Crocs 2007-09 -24% and HEYDUDE 2023-25 -25%)"; ws[f"A{t+2}"].font = BOLD
for j in range(5): put(ws, f"{L(2+j)}{t+3}", j + 1, "0", bold=True); put(ws, f"{L(2+j)}{t+4}", [0.0, 0.05, 0.12, 0.20, 0.30][j], PCT, inp=True)
ws[f"A{t+3}"] = "Score"; ws[f"A{t+4}"] = "Haircut"
s = t + 7; ws[f"A{s-1}"] = "Stress test through the P&L"; ws[f"A{s-1}"].font = Font(bold=True, size=12); header(ws, s, ["", "TTM base", "Stressed", "Change", "", "", "Assumption (blue = mine unless stated)"])
T = RAR["ttm"]; Aa = RAR["assumptions"]
ins = [("Distribution costs inside cost of sales (FY25)", Aa["dist_cost"], USD, "reported, 10-K FY2025"), ("  of which fixed", Aa["dist_fixed_share"], PCT, "my assumption"),
       ("SG&A fixed share", Aa["sga_fixed_share"], PCT, "my assumption (stores, people, IT fixed; DTC fulfilment, marketing variable)"),
       ("Extra markdown pressure on gross margin", Aa["markdown_gm_hit"], PCT, "my assumption (2008: gross margin fell 26 pts)"), ("Net interest expense", Aa["net_interest"], USD, "my estimate, TTM ~77"),
       ("Tax rate", Aa["tax"], PCT, "company non-GAAP guidance"), ("Diluted shares, no further buybacks (m)", Aa["shares"], "0.0", "46.2m at Sep-26 + 0.5m dilution"),
       ("Trough P/E", Aa["trough_pe"], X, "my assumption: ~25th percentile of 5y NTM range (6.8x)")]
I = {}
for k, (lab, v, fmt, basis) in enumerate(ins):
    rr = s + 12 + k; ws[f"A{rr}"] = lab; put(ws, f"B{rr}", v, fmt, inp=True); ws[f"G{rr}"] = basis; I[k] = f"$B${rr}"
pl = [("Revenue", round(T["revenue"], 1), f"=B{s+1}-F{t}"), ("Cost of sales (adjusted)", round(T["revenue"] - T["adj_gross_profit"], 1), f"={I[0]}*{I[1]}+(B{s+2}-{I[0]}*{I[1]})/B{s+1}*C{s+1}+{I[3]}*C{s+1}"),
      ("SG&A (adjusted)", round(T["adj_sga"], 1), f"=B{s+3}*{I[2]}+B{s+3}*(1-{I[2]})/B{s+1}*C{s+1}"), ("Adjusted EBIT", f"=B{s+1}-B{s+2}-B{s+3}", f"=C{s+1}-C{s+2}-C{s+3}"),
      ("D&A", round(T["da_q"], 1), f"=B{s+5}"), ("Adjusted EBITDA", f"=B{s+4}+B{s+5}", f"=C{s+4}+C{s+5}"), ("EBIT margin", f"=B{s+4}/B{s+1}", f"=C{s+4}/C{s+1}"),
      ("Adjusted EPS, run-rate ($)", f"=(B{s+4}-{I[4]})*(1-{I[5]})/{I[6]}", f"=(C{s+4}-{I[4]})*(1-{I[5]})/{I[6]}"),
      ("Stressed EPS x trough P/E = fad-unwind value ($)", None, f"=C{s+8}*{I[7]}"), ("Decremental EBIT margin on lost revenue", None, f"=(B{s+4}-C{s+4})/(B{s+1}-C{s+1})")]
for k, (lab, b, c) in enumerate(pl, s + 1):
    ws[f"A{k}"] = lab; fmt = PCT if "margin" in lab.lower() else ("0.00" if "EPS" in lab else USD)
    if b is not None: put(ws, f"B{k}", b, fmt, inp=not str(b).startswith("="))
    put(ws, f"C{k}", c, fmt, bold=("EPS" in lab))
    if b is not None: put(ws, f"D{k}", f"=C{k}/B{k}-1", PCT)
ws[f"G{s+1}"] = "TTM reported (press releases)"; ws[f"G{s+8}"] = "run-rate at today's share count; TTM reported adj. EPS was $13.52 on a higher average share count"
cx = s + 22; ws[f"A{cx-1}"] = "Comparison with consensus and price"; ws[f"A{cx-1}"].font = Font(bold=True, size=12)
cmp_ = [("Consensus FY2027E EPS (Yahoo, 15 analysts)", "=Peers!$B$22", "0.00"), ("Stressed EPS vs consensus FY27E", f"=C{s+8}/B{cx}-1", PCT), ("Current price / stressed EPS (x)", f"={N['price']}/C{s+8}", X),
        ("Fad-unwind value vs current price", f"=C{s+9}/{N['price']}-1", PCT), ("Price at the Mar-2026 closing low ($75.78) / TTM adj. EPS then ($12.51)", "=75.78/12.51", X),
        ("Price at the Mar-2026 low vs fad-unwind value", f"=75.78/C{s+9}-1", PCT)]
for k, (lab, f, fmt) in enumerate(cmp_, cx):
    ws[f"A{k}"] = lab; put(ws, f"B{k}", f, fmt, bold=True)
sx = cx + 8; ws[f"A{sx-1}"] = "Sensitivity of the subjective scores (all nine scores shifted together; Monte Carlo of independent +/-1 moves is in scripts/10)"; ws[f"A{sx-1}"].font = BOLD
header(ws, sx, ["Shift applied to every score", "Rev. at risk %", "Stressed EPS", "", "", "", "Note"])
for k, sh in enumerate((-1, 0, 1)):
    rr = sx + 1 + k; ws[f"A{rr}"] = f"{sh:+d} notch" if sh else "Central (as scored)"
    terms = "+".join(f"B{5+i}*INDEX($B${9+n}:$F${9+n},MIN(5,MAX(1,D{5+i}+({sh}))))" for i in range(n))
    put(ws, f"B{rr}", f"=({terms})/B{t}", PCT)
    rev1 = f"(B{s+1}*(1-B{rr}))"
    ebit1 = f"({rev1}-({I[0]}*{I[1]}+(B{s+2}-{I[0]}*{I[1]})/B{s+1}*{rev1}+{I[3]}*{rev1})-(B{s+3}*{I[2]}+B{s+3}*(1-{I[2]})/B{s+1}*{rev1}))"
    put(ws, f"C{rr}", f"=({ebit1}-{I[4]})*(1-{I[5]})/{I[6]}", "0.00")
mc = RAR["monte_carlo"]; ws[f"A{sx+5}"] = f"Monte Carlo (20,000 draws, each score -1/0/+1 with 25/50/25%): revenue at risk p5/p50/p95 = {mc['at_risk_pct_p5_p50_p95'][0]:.1f}% / {mc['at_risk_pct_p5_p50_p95'][1]:.1f}% / {mc['at_risk_pct_p5_p50_p95'][2]:.1f}%; stressed EPS p5/p50/p95 = ${mc['eps_p5_p50_p95'][0]:.2f} / ${mc['eps_p5_p50_p95'][1]:.2f} / ${mc['eps_p5_p50_p95'][2]:.2f} (static values from scripts/10_revenue_at_risk.py)"
RA = {"at_risk_pct": f"RevAtRisk!$E${t}", "at_risk": f"RevAtRisk!$F${t}", "eps1": f"RevAtRisk!$C${s+8}", "eps0": f"RevAtRisk!$B${s+8}", "ebitda1": f"RevAtRisk!$C${s+6}", "ebitda0": f"RevAtRisk!$B${s+6}", "val": f"RevAtRisk!$C${s+9}",
      "rev1": f"RevAtRisk!$C${s+1}", "ebit1": f"RevAtRisk!$C${s+4}", "decr": f"RevAtRisk!$C${s+10}", "vs_cons": f"RevAtRisk!$B${cx+1}", "px_over_stress": f"RevAtRisk!$B${cx+2}", "val_vs_px": f"RevAtRisk!$B${cx+3}",
      "minus1_pct": f"RevAtRisk!$B${sx+1}", "minus1_eps": f"RevAtRisk!$C${sx+1}", "plus1_pct": f"RevAtRisk!$B${sx+3}", "plus1_eps": f"RevAtRisk!$C${sx+3}"}

# ============================ Sens ============================
ws = sheet("Sens", [44] + [12] * 8); title(ws, "Sensitivity tables (live formulas on the Base case)")
R, S = SR["Base"]
ws["A4"] = "(A) Base-case DCF value per share: WACC (rows) x terminal growth (columns)"; ws["A4"].font = BOLD
waccs = [0.085, 0.09, 0.095, 0.10, 0.105, 0.11, 0.12]; gs = [0.0, 0.01, 0.02, 0.03]
ws["A5"] = "WACC \\ g"
for j, g in enumerate(gs): put(ws, f"{L(2+j)}5", g, PCT, inp=True, bold=True)
for i, w in enumerate(waccs):
    rr = 6 + i; put(ws, f"A{rr}", w, PCT, inp=True, bold=True)
    for j in range(len(gs)):
        c = L(2 + j)
        pv = f"SUMPRODUCT(Base!$D${R['fcff']}:$H${R['fcff']},1/(1+$A{rr})^Base!$D${R['t']}:$H${R['t']})"
        tv = f"Base!$H${R['fcff']}*(1+{c}$5)/($A{rr}-{c}$5)/(1+$A{rr})^Base!$H${R['t']}"
        put(ws, f"{c}{rr}", f"=({pv}+{tv}-Base!$C${R['nd']})/(Base!$C${R['sh_end']}+{N['dil']})", '$#,##0')
ws["A15"] = "(B) Price target Dec-2027: exit P/E (rows) x FY2028E EPS scenario (columns)"; ws["A15"].font = BOLD
ws["A16"] = "Exit P/E \\ FY28E EPS"
for j, sc in enumerate(("Bear", "Base", "Bull")): put(ws, f"{L(2+j)}16", f"={sc}!E{SR[sc][0]['eps']}", "0.00", bold=True); ws[f"{L(2+j)}17"] = sc
for i, m in enumerate([6, 7, 8, 9, 10, 10.5, 11, 12, 13, 14]):
    rr = 18 + i; put(ws, f"A{rr}", m, X, inp=True, bold=True)
    for j in range(3): put(ws, f"{L(2+j)}{rr}", f"=$A{rr}*{L(2+j)}$16", '$#,##0')
ws["A30"] = "(C) What moves FY2027E EPS (Base case run-rate; stated assumption in column D)"; ws["A30"].font = BOLD
header(ws, 31, ["Driver (change)", "EPS impact $", "EPS impact %", "Assumption"])
e27 = f"Base!$D${R['eps']}"; ni27 = f"Base!$D${R['ni']}"; sh27 = f"Base!$D${R['sh_avg']}"; rev27 = f"Base!$D${R['rev']}"
sens = [("+1% group revenue", f"={rev27}*0.01*0.50*(1-{N['ntax']})/{sh27}", "50% incremental EBIT margin (variable COGS + 35% variable SG&A), my assumption"),
        ("+1% Crocs North America revenue", f"=Base!$D${R['na']}*0.01*0.50*(1-{N['ntax']})/{sh27}", "same 50% incremental margin"),
        ("+1% Crocs International revenue", f"=Base!$D${R['intl']}*0.01*0.50*(1-{N['ntax']})/{sh27}", "same 50% incremental margin"),
        ("+100 bps adjusted EBIT margin", f"={rev27}*0.01*(1-{N['ntax']})/{sh27}", "mechanical"),
        ("+100 bps adjusted gross margin", f"={rev27}*0.01*(1-{N['ntax']})/{sh27}", "mechanical; Q3-26: lower duties +130 bps, product mix -130 bps"),
        ("+1 pt US tariff rate on imports", f"=-80/19.5*(1-{N['ntax']})/{sh27}", "$80m annualised unmitigated cost (mgmt, Feb-26) for ~19-20 pt IEEPA layer => ~$4m per point"),
        ("+1% USD vs all currencies", f"=-(Base!$D${R['intl']})*0.01*0.35*(1-{N['ntax']})/{sh27}", "international revenue translated; 35% flow-through after local costs and hedges, my assumption"),
        ("+100 bps interest rates", f"=-5.6*(1-{N['ntax']})/{sh27}", "$5.6m per 1% on variable-rate debt (10-K FY25 Item 7A)"),
        ("+$100m share repurchases (full-year effect)", f"={e27}*((100/Assump!$B${AS[('Base','Average buyback price ($)')]})/{sh27})", "at the Base-case FY27 repurchase price"),
        ("+10% average repurchase price", f"=-{e27}*(Base!$D${R['sh_rep']}*(1-1/1.1)/2/{sh27})", "fewer shares retired; half-year average effect"),
        ("No buybacks at all in FY27 (cash retained)", f"={ni27}/(Base!$C${R['sh_end']}+{N['sbcdil']}/2+{N['dil']})-{e27}", "shows how much of FY27 EPS growth is financial engineering")]
for k, (lab, f, basis) in enumerate(sens, 32):
    ws[f"A{k}"] = lab; put(ws, f"B{k}", f, '0.00;(0.00)'); put(ws, f"C{k}", f"=B{k}/{e27}", '0.0%;(0.0%)'); ws[f"D{k}"] = basis
SN = {lab: (f"Sens!$B${k}", f"Sens!$C${k}") for k, (lab, f, basis) in enumerate(sens, 32)}

# ============================ Peers ============================
ws = sheet("Peers", [44, 13, 13, 13, 13, 46]); title(ws, "Relative valuation - CROX vs DECK, BIRK, ONON", "Vendor multiples: StockAnalysis.com as of 2026-11-25 close (one methodology for all four). BIRK/ONON converted to USD by vendor.")
header(ws, 4, ["Metric", "CROX", "DECK", "BIRK", "ONON", "Note"])
prow = [("Share price (US$)", "price_usd", PS), ("Market cap (US$ m)", "mkt_cap_usd_m", USD0), ("Enterprise value (US$ m)", "ev_usd_m", USD0), ("P/S (TTM)", "ps_ttm", "0.00"), ("P/S (forward)", "ps_fwd", "0.00"),
        ("P/FCF (TTM)", "p_fcf", "0.0"), ("EV/EBITDA (TTM)", "ev_ebitda", "0.0"), ("EV/Sales (TTM)", "ev_sales", "0.00"), ("P/E (TTM)", "pe_ttm", "0.0"), ("P/E (forward)", "pe_fwd", "0.0"),
        ("Gross margin %", "gross_margin_pct", "0.0"), ("Operating margin %", "op_margin_pct", "0.0"), ("FCF margin %", "fcf_margin_pct", "0.0"), ("Revenue growth, TTM y/y %", "rev_growth_ttm_pct", "0.0"),
        ("Revenue growth, next FY consensus %", "rev_growth_next_fy_cons_pct", "0.0"), ("ROIC %", "roic_pct", "0.0"), ("Net debt (US$ m; negative = net cash, incl. leases)", "net_debt_usd_m", USD0), ("EBITDA TTM (US$ m)", "ebitda_usd_m", USD0)]
PR = {}
for i, (lab, key, fmt) in enumerate(prow, 5):
    ws[f"A{i}"] = lab; PR[key] = i
    for j, tkr in enumerate(("CROX", "DECK", "BIRK", "ONON")): put(ws, f"{L(2+j)}{i}", float(PEERS.loc[key, tkr]), fmt, inp=True)
ws["A22"] = "CROX consensus FY2027E EPS (Yahoo, 15 analysts)"; put(ws, "B22", 16.01, "0.00", inp=True); ws["F22"] = "Nasdaq/Zacks shows $15.85 (5 analysts) - sources disagree"
ws["A23"] = "CROX consensus FY2026E EPS (Yahoo)"; put(ws, "B23", 14.63, "0.00", inp=True); ws["A24"] = "CROX consensus FY2027E revenue (Yahoo, US$ m)"; put(ws, "B24", 4340.0, USD0, inp=True)
ws["A26"] = "Derived (formulas)"; ws["A26"].font = BOLD
pd_ = [("Value/Growth score = P/S TTM / TTM revenue growth % (lowest = best)", lambda c: f"={c}{PR['ps_ttm']}/{c}{PR['rev_growth_ttm_pct']}", "0.00"),
       ("Value/Growth score on next-FY consensus growth", lambda c: f"={c}{PR['ps_ttm']}/{c}{PR['rev_growth_next_fy_cons_pct']}", "0.00"),
       ("Net debt / EBITDA", lambda c: f"={c}{PR['net_debt_usd_m']}/{c}{PR['ebitda_usd_m']}", X), ("FCF yield % (1 / P/FCF)", lambda c: f"=1/{c}{PR['p_fcf']}", PCT),
       ("Forward P/E premium (discount) to DECK", lambda c: f"={c}{PR['pe_fwd']}/$C${PR['pe_fwd']}-1", PCT), ("EV/EBITDA premium (discount) to DECK", lambda c: f"={c}{PR['ev_ebitda']}/$C${PR['ev_ebitda']}-1", PCT)]
for i, (lab, fn, fmt) in enumerate(pd_, 27):
    ws[f"A{i}"] = lab
    for j in range(4): put(ws, f"{L(2+j)}{i}", fn(L(2 + j)), fmt)
ws["F27"] = "CROX screens WORST on growth per dollar of sales multiple"; ws["F31"] = "5-year median discount to DECK on NTM P/E was ~52% (scripts/08)"

# ============================ Quarterly ============================
ws = sheet("Quarterly", [40] + [11] * 12); ws["A1"] = "Quarterly data - last 12 quarters (reported, press releases)"; ws["A1"].font = Font(bold=True, size=14)
ws["A2"] = "TTM revenue (to Sep-26)"; ws["A3"] = "TTM free cash flow"; ws["A4"] = "TTM adjusted EBITDA"; ws["A5"] = "TTM adjusted EBIT"; ws["A6"] = "TTM adjusted EPS ($)"
q12 = Q.tail(12); header(ws, 8, ["US$ m"] + list(q12.index))
qrows = [("Revenue", "revenue", USD), ("Crocs Brand revenue", "crocs_rev", USD), ("  North America", "crocs_na", USD), ("  International", "crocs_intl", USD), ("HEYDUDE revenue", "hd_rev", USD),
         ("Adjusted gross margin %", "adj_gm_pct", "0.0"), ("Adjusted operating income", "adj_op_income", USD), ("Adjusted operating margin %", "adj_op_margin_pct", "0.0"), ("GAAP operating income", "op_income", USD),
         ("Adjusted diluted EPS ($)", "adj_eps", "0.00"), ("GAAP diluted EPS ($)", "eps_diluted", "0.00"), ("Cash from operations", "cfo_q", USD), ("Capex", "capex_q", USD), ("D&A", "da_q", USD),
         ("Stock-based compensation", "sbc_q", USD), ("Borrowings (carrying)", "lt_borrowings", USD), ("Cash", "cash", USD), ("Inventories", "inventories", USD), ("Diluted shares (m)", "sh_diluted_m", "0.0")]
QR = {}
for i, (lab, key, fmt) in enumerate(qrows, 9):
    ws[f"A{i}"] = lab; QR[key] = i
    for j, p in enumerate(q12.index):
        v = q12.loc[p, key]
        if pd.notna(v): put(ws, f"{L(2+j)}{i}", round(float(v), 3), fmt, inp=True)
e = 9 + len(qrows); ws[f"A{e}"] = "Free cash flow (formula)"; ws[f"A{e+1}"] = "Revenue growth y/y (formula)"; ws[f"A{e+2}"] = "Net debt (formula)"; ws[f"A{e+3}"] = "GAAP less adjusted operating income (formula)"
for j in range(12):
    c = L(2 + j); put(ws, f"{c}{e}", f"={c}{QR['cfo_q']}-{c}{QR['capex_q']}", USD); put(ws, f"{c}{e+2}", f"={c}{QR['lt_borrowings']}-{c}{QR['cash']}", USD); put(ws, f"{c}{e+3}", f"={c}{QR['op_income']}-{c}{QR['adj_op_income']}", USD)
    if j >= 4: put(ws, f"{c}{e+1}", f"={c}{QR['revenue']}/{L(2+j-4)}{QR['revenue']}-1", PCT)
put(ws, "B2", f"=SUM(J{QR['revenue']}:M{QR['revenue']})", USD, bold=True); put(ws, "B3", f"=SUM(J{e}:M{e})", USD, bold=True)
put(ws, "B4", f"=SUM(J{QR['adj_op_income']}:M{QR['adj_op_income']})+SUM(J{QR['da_q']}:M{QR['da_q']})", USD, bold=True)
put(ws, "B5", f"=SUM(J{QR['adj_op_income']}:M{QR['adj_op_income']})", USD, bold=True); put(ws, "B6", f"=SUM(J{QR['adj_eps']}:M{QR['adj_eps']})", "0.00", bold=True)

# ============================ Checks ============================
ws = sheet("Checks", [70, 16, 12]); title(ws, "Model integrity checks (all should read OK)"); header(ws, 3, ["Check", "Value", "Status"])
Rb, Sb = SR["Base"]
chk = [("Scenario probabilities sum to 100%", "=Valuation!E5", "=IF(ABS(B4-1)<0.0001,\"OK\",\"ERROR\")"),
       ("FY2025A revenue ties to Hist (Base sheet)", f"=Base!B{Rb['rev']}-Hist!F{H['revenue']}", "=IF(ABS(B5)<0.5,\"OK\",\"ERROR\")"),
       ("FY2026E EPS inside guidance $14.45-14.65", f"=Base!C{Rb['eps']}", "=IF(AND(B6>=14.45,B6<=14.65),\"OK\",\"CHECK\")"),
       ("FY2026E revenue growth ~3% (guidance)", f"=Base!C{Rb['g']}", "=IF(AND(B7>0.025,B7<0.04),\"OK\",\"CHECK\")"),
       ("Bear PT < Base PT < Bull PT", "=Valuation!C9", "=IF(AND(Valuation!B9<Valuation!C9,Valuation!C9<Valuation!D9),\"OK\",\"ERROR\")"),
       ("RevAtRisk line revenues sum to TTM revenue", f"=RevAtRisk!B{5+n}-Quarterly!B2", "=IF(ABS(B9)<1,\"OK\",\"ERROR\")"),
       ("TTM adjusted EPS = 13.52 (cross-check with scripts)", "=Quarterly!B6", "=IF(ABS(B10-13.52)<0.01,\"OK\",\"ERROR\")"),
       ("WACC used within 100 bps of computed WACC", f"={N['wacc']}-{N['wacc_calc']}", "=IF(ABS(B11)<0.01,\"OK\",\"CHECK\")"),
       ("Base net debt/EBITDA stays <= 1.5x (company target 1-1.5x)", f"=MAX(Base!D{Rb['lev']}:H{Rb['lev']})", "=IF(B12<=1.5,\"OK\",\"CHECK\")"),
       ("Count of formula errors in key outputs", f"=SUMPRODUCT(--ISERROR(Valuation!B5:E16))+SUMPRODUCT(--ISERROR(Sens!B6:E12))+SUMPRODUCT(--ISERROR(ReverseDCF!B18:H24))", "=IF(B13=0,\"OK\",\"ERROR\")")]
for i, (lab, f, st) in enumerate(chk, 4):
    ws[f"A{i}"] = lab; put(ws, f"B{i}", f, "0.000"); put(ws, f"C{i}", st.replace("B4", f"B{i}") if i == 4 else st, bold=True)
wb.move_sheet("Valuation", offset=-(len(wb.sheetnames) - 2))
out = os.path.join(ROOT, "model.xlsx"); wb.save(out)
# cell map for the extraction step
cellmap = {"inputs": N, "valuation": {"prob": ["Valuation!B5", "Valuation!C5", "Valuation!D5"], "eps27": ["Valuation!B6", "Valuation!C6", "Valuation!D6", "Valuation!E6"], "eps28": ["Valuation!B7", "Valuation!C7", "Valuation!D7", "Valuation!E7"],
           "exit": ["Valuation!B8", "Valuation!C8", "Valuation!D8"], "pt": ["Valuation!B9", "Valuation!C9", "Valuation!D9", "Valuation!E9"], "ret": ["Valuation!B10", "Valuation!C10", "Valuation!D10", "Valuation!E10"],
           "dcf": ["Valuation!B11", "Valuation!C11", "Valuation!D11", "Valuation!E11"], "dcf_ret": ["Valuation!B12", "Valuation!C12", "Valuation!D12", "Valuation!E12"], "rcagr": ["Valuation!B13", "Valuation!C13", "Valuation!D13"],
           "margin28": ["Valuation!B14", "Valuation!C14", "Valuation!D14"], "vs_cons": ["Valuation!B15", "Valuation!C15", "Valuation!D15"], "lev28": ["Valuation!B16", "Valuation!C16", "Valuation!D16"]},
           "key": VK, "rar": RA, "sens": SN, "scen_rows": {sc: SR[sc][0] for sc in SR}, "scen_dcf": {sc: SR[sc][1] for sc in SR},
           "reverse": {"implied_g": "ReverseDCF!B12", "implied_margin": "ReverseDCF!B13", "implied_cagr": "ReverseDCF!B29", "fcf": "ReverseDCF!B11", "grid": "ReverseDCF!A17:H24"},
           "sens_dcf_grid": "Sens!A5:E12", "sens_pt_grid": "Sens!A16:D27", "checks": "Checks!A4:C13", "peers_derived": "Peers!A27:E32"}
json.dump(cellmap, open(os.path.join(D, "model_cellmap.json"), "w"), indent=1)
print("saved", out)
