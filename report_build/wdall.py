import json,subprocess,re,html,sys
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def detail(path):
    url="https://pimco.wd1.myworkdayjobs.com/wday/cxs/pimco/pimco-careers"+path
    r=subprocess.run(["curl","-sS","--max-time","45","-H","Accept: application/json","-A",UA,url],capture_output=True)
    try: return json.loads(r.stdout)
    except: return {}
def clean(h):
    s=re.sub(r'(?i)<li>','\n - ',h or '')
    s=re.sub(r'(?i)</(p|div|li|ul|h[1-6])>','\n',s); s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'<[^>]+>','',s); s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s); return re.sub(r'\n\s*\n+','\n',s).strip()
jobs=json.load(open("all_jobs.json"))
interns=[p for p in jobs if re.search(r'(?i)\b(intern|internship)\b',p["title"])]
print(f"### {len(interns)} intern postings total\n")
out=open("intern_jobs_full.txt","w")
summary=[]
for p in sorted(interns,key=lambda x:x["title"]):
    d=detail(p["externalPath"]); ji=d.get("jobPostingInfo",{})
    locs=ji.get("location","")
    add=ji.get("additionalLocations") or []
    alll=locs+ ((" + "+"; ".join(add)) if add else "")
    rid=p["bulletFields"][0] if p["bulletFields"] else "?"
    summary.append((rid,ji.get("title",p["title"]),alll,ji.get("startDate")))
    out.write("="*100+f"\nREQ {rid} | {ji.get('title')}\nLOCATIONS: {alll}\nPOSTED: {ji.get('startDate')}\nAPPLY: {ji.get('externalUrl')}\n"+"-"*60+"\n"+clean(ji.get("jobDescription"))+"\n")
out.close()
print(f"{'REQ':<10}{'LOCATIONS':<62}{'POSTED':<12} TITLE")
for rid,t,l,sd in summary:
    mark="**LONDON**" if "London" in l else ""
    print(f"{rid:<10}{l[:60]:<62}{str(sd):<12} {t} {mark}")
