import json,subprocess,time
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
BASE="https://pimco.wd1.myworkdayjobs.com/wday/cxs/pimco/pimco-careers/jobs"
def q(text="",offset=0,limit=20,facets=None):
    body=json.dumps({"appliedFacets":facets or {},"limit":limit,"offset":offset,"searchText":text})
    r=subprocess.run(["curl","-sS","--max-time","45","-X","POST",BASE,"-H","Content-Type: application/json","-H","Accept: application/json","-A",UA,"-d",body],capture_output=True)
    try: return json.loads(r.stdout)
    except Exception as e: return {"err":str(e),"raw":r.stdout[:400].decode('utf8','ignore')}
allj={}
for term in ["","Summer Intern","Intern","Analyst","Summer"]:
    off=0
    while True:
        d=q(term,off,20)
        if "jobPostings" not in d: print("ERR",term,d); break
        for p in d["jobPostings"]:
            allj[p["externalPath"]]=p
        tot=d.get("total",0); off+=20
        if off>=tot or off>400: break
    print(f"term={term!r} total={tot} cum_unique={len(allj)}")
json.dump(list(allj.values()),open("all_jobs.json","w"),indent=1)
print("=== TOTAL UNIQUE:",len(allj),"===")
print("\n=== LONDON / UK / EMEA POSTINGS ===")
for p in sorted(allj.values(),key=lambda x:x["title"]):
    loc=p["locationsText"]
    if any(k in loc for k in ["London","GBR","Locations"]) or "EMEA" in p["title"] or "UK" in p["title"]:
        print(f'{p["bulletFields"]} | {p["title"]} | {loc} | {p["postedOn"]}')
        print(f'   https://pimco.wd1.myworkdayjobs.com/en-US/pimco-careers{p["externalPath"]}')
