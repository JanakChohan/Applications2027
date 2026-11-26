"""Download CROX primary filings from SEC EDGAR into data/sec/. Source: sec.gov (EDGAR)."""
import json, os, time, urllib.request, re
UA = "equity-research-script/1.0 (contact: research@example.com)"
BASE = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(os.path.join(BASE, "sec"), exist_ok=True)
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for i in range(4):
        try:
            return urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:
            time.sleep(2 * (i + 1)); err = e
    raise err
s = json.load(open(os.path.join(BASE, "sec_submissions_CROX.json")))
r = s["filings"]["recent"]
want = []
for i in range(len(r["form"])):
    f, d = r["form"][i], r["filingDate"][i]
    if (f in ("10-K",) and d >= "2021-01-01") or (f == "10-Q" and d >= "2024-01-01") or (f == "DEF 14A" and d >= "2026-01-01") or (f == "8-K" and d >= "2023-01-01"):
        want.append((d, f, r["accessionNumber"][i], r["primaryDocument"][i]))
log = []
for d, f, acc, doc in want:
    accn = acc.replace("-", "")
    folder = f"https://www.sec.gov/Archives/edgar/data/1334036/{accn}/"
    out = os.path.join(BASE, "sec", f"{d}_{f.replace(' ','')}_{doc}")
    if not os.path.exists(out):
        open(out, "wb").write(get(folder + doc)); time.sleep(0.25)
    log.append({"date": d, "form": f, "url": folder + doc, "file": os.path.basename(out)})
    if f == "8-K":
        # fetch exhibits (press release EX-99.1) via index.json
        idx = json.loads(get(folder + "index.json")); time.sleep(0.2)
        for it in idx["directory"]["item"]:
            n = it["name"]
            if re.search(r"(ex|exhibit).*99|991|99-1", n, re.I) and n.endswith(".htm"):
                o2 = os.path.join(BASE, "sec", f"{d}_8-K_EX_{n}")
                if not os.path.exists(o2):
                    open(o2, "wb").write(get(folder + n)); time.sleep(0.25)
                log.append({"date": d, "form": "8-K EX-99", "url": folder + n, "file": os.path.basename(o2)})
json.dump(log, open(os.path.join(BASE, "sec_filing_index.json"), "w"), indent=1)
print(len(log), "files")
