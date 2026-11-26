"""Fetch peer fundamentals / ratios / consensus tables from stockanalysis.com (HTML tables) into data/sa/ as CSV.
Used for peer comparison and consensus revenue. As-of date = run date."""
import os, time, urllib.request, io, datetime, json
import pandas as pd
UA = "equity-research-script/1.0"
B = os.path.join(os.path.dirname(__file__), "..", "data", "sa"); os.makedirs(B, exist_ok=True)
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60).read().decode("utf8", "ignore")
pages = {"is_a": "financials/", "is_q": "financials/?p=quarterly", "bs_a": "financials/balance-sheet/", "bs_q": "financials/balance-sheet/?p=quarterly",
         "cf_a": "financials/cash-flow-statement/", "cf_q": "financials/cash-flow-statement/?p=quarterly",
         "ratios_a": "financials/ratios/", "ratios_q": "financials/ratios/?p=quarterly", "stats": "statistics/", "forecast": "forecast/"}
for t in ["crox", "deck", "birk", "onon"]:
    for k, p in pages.items():
        raw = os.path.join(B, f"{t}_{k}.html")
        if not os.path.exists(raw):
            try:
                open(raw, "w").write(get(f"https://stockanalysis.com/stocks/{t}/{p}")); time.sleep(1.0)
            except Exception as e:
                print("FAIL", t, k, e); continue
        try:
            tabs = pd.read_html(io.StringIO(open(raw).read()))
            for i, df in enumerate(tabs):
                df.to_csv(os.path.join(B, f"{t}_{k}_{i}.csv"), index=False)
        except Exception as e:
            print("no tables", t, k, e)
json.dump({"fetched": datetime.date.today().isoformat(), "source": "stockanalysis.com"}, open(os.path.join(B, "_asof.json"), "w"))
print("ok")
