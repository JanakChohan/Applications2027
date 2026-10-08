import re, glob, os, html
HERE=os.path.dirname(os.path.abspath(__file__))
def load():
    rows={}
    for f in sorted(glob.glob(os.path.join(HERE,"..","research","*.md"))):
        for line in open(f,encoding="utf-8"):
            line=line.strip().strip("`")
            m=re.match(r"^\[(S\d+[a-z]?)\]\s*\|(.*)$",line)
            if not m: continue
            sid=m.group(1); parts=[p.strip() for p in m.group(2).split("|")]
            if sid in rows: continue
            rows[sid]=parts
    return rows
def key(s): 
    m=re.match(r"S(\d+)([a-z]?)",s); return (int(m.group(1)),m.group(2))
def table_html():
    rows=load(); out=['<table class="src-table" style="table-layout:fixed"><colgroup><col style="width:5%"><col style="width:11%"><col style="width:22%"><col style="width:8%"><col style="width:32%"><col style="width:8%"><col style="width:14%"></colgroup><thead><tr><th>ID</th><th>Outlet</th><th>Title</th><th>Published</th><th>URL</th><th>Status</th><th>Confidence note</th></tr></thead><tbody>']
    for sid in sorted(rows,key=key):
        p=rows[sid]+[""]*8
        outlet,title,pub,url=p[0],p[1],p[2],p[3]
        status=p[5] if len(p)>5 else ""
        note=p[6] if len(p)>6 else ""
        out.append(f'<tr id="src_{sid}"><td><b>{sid}</b></td><td>{html.escape(outlet)}</td><td>{html.escape(title)}</td><td>{html.escape(pub)}</td><td style="word-break:break-all">{html.escape(url)}</td><td>{html.escape(status)}</td><td>{html.escape(note)}</td></tr>')
    out.append("</tbody></table>")
    return "\n".join(out), len(rows)
def cited(text):
    ids=set()
    for m in re.finditer(r"\[(S\d+[a-z]?)\]",text): ids.add(m.group(1))
    for m in re.finditer(r"\[(S\d+)\]-\[(S\d+)\]",text): pass
    return ids
