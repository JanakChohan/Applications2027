import sys, subprocess, re, html, os
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
def get(url, out=None):
    r=subprocess.run(["curl","-sSL","--max-time","60","-A",UA,"-H","Accept-Language: en-GB,en;q=0.9",url],capture_output=True)
    d=r.stdout
    if out:
        open(out,'wb').write(d)
    return d
def totext(b):
    try: s=b.decode('utf-8','ignore')
    except: s=str(b)
    s=re.sub(r'(?is)<script.*?</script>',' ',s)
    s=re.sub(r'(?is)<style.*?</style>',' ',s)
    s=re.sub(r'(?is)<noscript.*?</noscript>',' ',s)
    s=re.sub(r'(?s)<!--.*?-->',' ',s)
    s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'(?i)</(p|div|tr|li|h[1-6]|section)>','\n',s)
    s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s.strip()
if __name__=="__main__":
    url=sys.argv[1]
    raw=get(url)
    t=totext(raw)
    if len(sys.argv)>2 and sys.argv[2]=='--raw':
        print(raw.decode('utf-8','ignore')[:200000])
    else:
        print(t[:200000])
