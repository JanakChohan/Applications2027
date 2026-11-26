"""Parse Crocs quarterly earnings press releases (8-K EX-99.1, text in data/sec_txt) into a tidy quarterly dataset.
Output: data/derived/quarterly_reported.csv  (all figures 'reported', $ thousands unless noted).
Source: SEC EDGAR 8-K exhibits listed in data/sec_filing_index.json."""
import os, re, glob, json
import pandas as pd
B = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(os.path.join(B, "derived"), exist_ok=True)
def num(s):
    s = s.strip().replace("$", "").replace(",", "").replace("%", "").replace("bp", "").strip()
    neg = s.startswith("(") or s.startswith("-")
    s = s.strip("()- ").strip()
    if s in ("—", "", "–"): return 0.0
    try: v = float(s)
    except ValueError: return None
    return -v if neg else v
def parse(path):
    rows = {}; table = ""; section = ""
    for ln in open(path).read().split("\n"):
        ln = ln.strip()
        if not ln: continue
        if "|" not in ln:
            if ln.isupper() and len(ln) > 8: table = ln; section = ""
            elif ln.endswith(":") and len(ln) < 90: section = ln[:-1]
            continue
        parts = [p.strip() for p in ln.split("|")]
        label = re.sub(r"\s*\(\d\)\s*$", "", parts[0]).strip()
        vals = [num(p) for p in parts[1:]]
        vals = [v for v in vals if v is not None]
        if vals:
            rows.setdefault(f"{table}/{section}/{label}", vals)
            rows.setdefault(f"//{label}", vals)   # first occurrence shortcut
            rows.setdefault(f"/{section}/{label}", vals)
    return rows
files = sorted(glob.glob(os.path.join(B, "sec_txt", "*8-K_EX_crox*release*.txt")))
out = []
qmap = {"q1": "Q1", "q2": "Q2", "q3": "Q3", "q4": "Q4"}
for f in files:
    base = os.path.basename(f)
    m = re.search(r"croxq(\d)(\d{4})", base)
    if m: q, y = int(m.group(1)), int(m.group(2))
    else:
        m = re.search(r"crox1231(\d\d)", base); q, y = 4, 2000 + int(m.group(1))
    r = parse(f)
    def g(key, i=0, default=None):
        for k in ([key] if isinstance(key, str) else key):
            if k in r and len(r[k]) > i: return r[k][i]
        return default
    d = {"period": f"{y}Q{q}", "year": y, "q": q, "file": base}
    d["revenue"] = g("//Revenues"); d["revenue_py"] = g("//Revenues", 1)
    d["cogs"] = g("//Cost of sales"); d["gross_profit"] = g("//Gross profit")
    d["sga"] = g("//Selling, general and administrative expenses")
    d["op_income"] = g(["//Income from operations", "//Income (loss) from operations"])
    d["interest_expense"] = g("//Interest expense"); d["pretax"] = g(["//Income before income taxes", "//Income (loss) before income taxes"])
    d["tax"] = g(["//Income tax expense", "//Income tax expense (benefit)", "//Income tax (benefit) expense"])
    d["net_income"] = g(["//Net income", "//Net income (loss)"])
    d["eps_diluted"] = g("//Diluted"); d["sh_basic"] = g("//Basic", 0)
    d["sh_diluted_gaap"] = g(["//GAAP weighted average common shares outstanding - diluted"])
    d["adj_gross_profit"] = g("//Non-GAAP gross profit"); d["adj_gm_pct"] = g("//Non-GAAP gross margin")
    d["adj_sga"] = g(["//Non-GAAP selling, general and administrative expenses"])
    d["adj_op_income"] = g("//Non-GAAP income from operations"); d["adj_op_margin_pct"] = g("//Non-GAAP operating margin")
    d["adj_net_income"] = g("//Non-GAAP net income")
    d["adj_tax_rate_pct"] = g("//Non-GAAP effective income tax rate")
    d["crocs_adj_gm_pct"] = g(["//Non-GAAP Crocs Brand gross margin"]); d["hd_adj_gm_pct"] = g(["//Non-GAAP HEYDUDE Brand gross margin"])
    d["crocs_gaap_gm_pct"] = g(["//GAAP Crocs Brand gross margin"]); d["hd_gaap_gm_pct"] = g(["//GAAP HEYDUDE Brand gross margin"])
    # adjusted diluted EPS: the 'Diluted' row under 'Non-GAAP net income per common share'
    d["adj_eps"] = g(["/Non-GAAP net income per common share/Diluted"])
    d["crocs_rev"] = g(["//Total Crocs Brand"]); d["hd_rev"] = g(["//Total HEYDUDE Brand"])
    d["crocs_na"] = g(["//Total North America", "//North America"]); d["crocs_intl"] = g(["//Total International", "//International"])
    d["crocs_na_whsl"] = g("/North America/Wholesale"); d["crocs_na_dtc"] = g("/North America/Direct-to-consumer")
    d["crocs_intl_whsl"] = g("/International/Wholesale"); d["crocs_intl_dtc"] = g("/International/Direct-to-consumer")
    d["crocs_whsl"] = g("/Crocs Brand/Wholesale"); d["crocs_dtc"] = g("/Crocs Brand/Direct-to-consumer")
    d["hd_whsl"] = g("/HEYDUDE Brand/Wholesale"); d["hd_dtc"] = g("/HEYDUDE Brand/Direct-to-consumer")
    d["cfo_q"] = g("//Cash provided by operating activities") ; d["fcf_q"] = g("//Free cash flow")
    d["cash"] = g("//Cash and cash equivalents"); d["inventories"] = g("//Inventories"); d["receivables"] = None
    d["lt_borrowings"] = g("//Long-term borrowings"); d["cur_borrowings"] = g("//Current portion of long-term borrowings", 0, 0.0)
    out.append(d); json.dump(r, open(os.path.join(B, "derived", f"release_rows_{y}Q{q}.json"), "w"))
df = pd.DataFrame(out).sort_values(["year", "q"]).reset_index(drop=True)
df.to_csv(os.path.join(B, "derived", "quarterly_release_raw.csv"), index=False)
pd.set_option("display.width", 300); pd.set_option("display.max_columns", 60)
print(df[["period","revenue","gross_profit","sga","op_income","net_income","eps_diluted","adj_gm_pct","adj_op_income","adj_op_margin_pct","adj_eps","crocs_rev","hd_rev"]].to_string())
print(df[["period","crocs_na","crocs_intl","crocs_whsl","crocs_dtc","hd_whsl","hd_dtc","cfo_q","fcf_q","cash","inventories","lt_borrowings","cur_borrowings","sh_diluted_gaap","crocs_adj_gm_pct","hd_adj_gm_pct"]].to_string())
