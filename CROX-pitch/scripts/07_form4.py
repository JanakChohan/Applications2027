"""Download and parse Form 4 insider filings for CROX (issuer CIK 1334036) since 2024-07-01.
Output: data/derived/form4_transactions.csv. Flags Rule 10b5-1 via the <aff10b5One> checkbox and footnote text.
Source: SEC EDGAR."""
import json, os, re, time, urllib.request
import xml.etree.ElementTree as ET
import pandas as pd
UA = "equity-research-script/1.0 (contact: research@example.com)"
B = os.path.join(os.path.dirname(__file__), "..", "data"); O = os.path.join(B, "sec", "form4"); os.makedirs(O, exist_ok=True)
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=60).read()
s = json.load(open(os.path.join(B, "sec_submissions_CROX.json"))); r = s["filings"]["recent"]
rows = []
for i in range(len(r["form"])):
    if r["form"][i] not in ("4", "4/A") or r["filingDate"][i] < "2024-07-01": continue
    acc = r["accessionNumber"][i]; accn = acc.replace("-", ""); doc = r["primaryDocument"][i].split("/")[-1]
    path = os.path.join(O, f"{r['filingDate'][i]}_{accn}.xml")
    url = f"https://www.sec.gov/Archives/edgar/data/1334036/{accn}/{doc}"
    if not os.path.exists(path):
        open(path, "wb").write(get(url)); time.sleep(0.2)
    try: root = ET.parse(path).getroot()
    except ET.ParseError: continue
    def t(node, p):
        x = node.find(p); return x.text.strip() if x is not None and x.text else ""
    owner = t(root, ".//reportingOwner/reportingOwnerId/rptOwnerName")
    title = t(root, ".//reportingOwner/reportingOwnerRelationship/officerTitle")
    isdir = t(root, ".//reportingOwner/reportingOwnerRelationship/isDirector")
    aff = t(root, "aff10b5One")
    foot = " ".join((f.text or "") for f in root.findall(".//footnotes/footnote"))
    for tr in root.findall(".//nonDerivativeTable/nonDerivativeTransaction"):
        code = t(tr, "transactionCoding/transactionCode"); sh = float(t(tr, "transactionAmounts/transactionShares/value") or 0)
        px = t(tr, "transactionAmounts/transactionPricePerShare/value"); px = float(px) if px else 0.0
        ad = t(tr, "transactionAmounts/transactionAcquiredDisposedCode/value")
        post = t(tr, "postTransactionAmounts/sharesOwnedFollowingTransaction/value")
        rows.append({"filed": r["filingDate"][i], "trade_date": t(tr, "transactionDate/value"), "owner": owner, "title": title or ("Director" if isdir in ("1", "true") else ""),
                     "code": code, "acq_disp": ad, "shares": sh, "price": px, "value_usd": sh * px, "shares_after": float(post) if post else None,
                     "aff10b5One": aff, "footnote_mentions_10b5_1": bool(re.search(r"10b5-1", foot)), "url": url})
df = pd.DataFrame(rows).sort_values("trade_date")
df.to_csv(os.path.join(B, "derived", "form4_transactions.csv"), index=False)
pd.set_option("display.width", 250); pd.set_option("display.max_rows", 200)
op = df[df.code.isin(["S", "P"])]
print(op[["trade_date", "owner", "title", "code", "shares", "price", "value_usd", "shares_after", "aff10b5One", "footnote_mentions_10b5_1"]].to_string())
print(df.groupby("code").agg(n=("shares", "size"), shares=("shares", "sum"), value=("value_usd", "sum")))
