"""Fetch market data from the Nasdaq public API (api.nasdaq.com): daily prices, short interest,
earnings surprises, analyst forecasts. Saved raw to data/market/. As-of date = run date."""
import json, os, time, urllib.request, datetime
UA = "equity-research-script/1.0"
B = os.path.join(os.path.dirname(__file__), "..", "data", "market"); os.makedirs(B, exist_ok=True)
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    return urllib.request.urlopen(req, timeout=60).read()
today = datetime.date.today().isoformat()
tick = {"CROX": "stocks", "DECK": "stocks", "BIRK": "stocks", "ONON": "stocks", "SPY": "etf", "XRT": "etf"}
for t, ac in tick.items():
    u = f"https://api.nasdaq.com/api/quote/{t}/historical?assetclass={ac}&fromdate=2016-11-01&todate={today}&limit=9999"
    open(os.path.join(B, f"px_{t}.json"), "wb").write(get(u)); time.sleep(0.5)
    u = f"https://api.nasdaq.com/api/quote/{t}/info?assetclass={ac}"
    open(os.path.join(B, f"info_{t}.json"), "wb").write(get(u)); time.sleep(0.5)
for t in ["CROX", "DECK", "BIRK", "ONON"]:
    for name, u in {
        "short": f"https://api.nasdaq.com/api/quote/{t}/short-interest?assetClass=stocks",
        "surprise": f"https://api.nasdaq.com/api/company/{t}/earnings-surprise",
        "epsfc": f"https://api.nasdaq.com/api/analyst/{t}/earnings-forecast",
        "ratings": f"https://api.nasdaq.com/api/analyst/{t}/ratings",
        "target": f"https://api.nasdaq.com/api/analyst/{t}/targetprice",
        "summary": f"https://api.nasdaq.com/api/quote/{t}/summary?assetclass=stocks",
        "inst": f"https://api.nasdaq.com/api/company/{t}/institutional-holdings?limit=25&type=TOTAL&sortColumn=marketValue&sortOrder=DESC",
        "insider": f"https://api.nasdaq.com/api/company/{t}/insider-trades?limit=100&type=ALL&sortColumn=lastDate&sortOrder=DESC",
        "peg": f"https://api.nasdaq.com/api/analyst/{t}/peg-ratio",
    }.items():
        try:
            open(os.path.join(B, f"{name}_{t}.json"), "wb").write(get(u))
        except Exception as e:
            print("FAIL", t, name, e)
        time.sleep(0.5)
json.dump({"fetched": today, "source": "api.nasdaq.com"}, open(os.path.join(B, "_asof.json"), "w"))
print("ok", today)
