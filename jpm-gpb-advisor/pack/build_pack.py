"""Assemble the complete interview pack: parts/*.html with {{FIG:key}} and [Sxx] markers, two-pass render for TOC page numbers."""
import re, subprocess, sys, json, glob
import pymupdf
import diagrams as dg, charts as ch, diagrams2 as d2
from svg import fig
from sources_base import S
try:
    from sources_extra import S as S2; S.update(S2)
except ImportError: pass

FIGS={}; ORDER=[]
def strip(f): return f.split('<div class="cap">')[0].replace('<div class="fig">','')
def F(key, svg, cap, full=False):
    FIGS[key]=(svg,cap,full)

def build_figs():
    import figs_def, figs_def2; figs_def.define(F, dg, ch, d2, strip); figs_def2.define2(F, dg, ch, d2, strip)

def render_fig(key, n):
    svg,cap,full=FIGS[key]
    cls="fig full" if full else "fig"
    return f'<div class="{cls}" id="fig{n}">{svg}<div class="cap"><b>Figure {n}.</b> {cap}</div></div>'

def process(body):
    n=[0]
    def rep(m):
        n[0]+=1; ORDER.append(m.group(1)); return render_fig(m.group(1), n[0])
    body=re.sub(r"\{\{FIG:(\w+)\}\}", rep, body)
    # protect SVG blocks from marker rewriting
    svgs=[]
    def keep(m):
        svgs.append(m.group(0)); return f"@@SVG{len(svgs)-1}@@"
    body=re.sub(r"<svg.*?</svg>", keep, body, flags=re.S)
    # source markers
    def srep(m):
        ids=[int(x) for x in re.findall(r"\d+", m.group(0))]
        for i in ids:
            if i not in S: print("WARNING missing source", i, file=sys.stderr)
        return '<span class="s">'+"".join(f"[S{i}]" for i in ids)+'</span>'
    body=re.sub(r"(\[S\d+\])+", srep, body)
    body=body.replace("[Confirmed]",'<span class="conf c">CONFIRMED</span>').replace("[Reported]",'<span class="conf r">REPORTED</span>').replace("[Inferred]",'<span class="conf i">INFERRED</span>')
    body=re.sub(r"@@SVG(\d+)@@", lambda m: svgs[int(m.group(1))], body)
    return body, n[0]

def source_table():
    rows=[]
    for k in sorted(S):
        o,t,pd,u,acc,st,conf=S[k]
        rows.append(f"<tr><td>S{k}</td><td>{o}</td><td>{t}</td><td>{pd}</td><td><a href='{u}'>{u}</a></td><td>{acc}</td><td>{st}</td><td>{conf}</td></tr>")
    return '<table class="src"><tr><th>ID</th><th>Outlet</th><th>Title</th><th>Pub date</th><th>URL</th><th>Accessed</th><th>Status</th><th>Confidence</th></tr>'+"".join(rows)+'</table>'

def assemble(toc_pages=None):
    css=open("pack_style.css").read()
    parts=json.load(open("parts_order.json"))
    body=""
    heads=[]  # (level, id, title)
    for p in parts:
        html=open(p).read()
        body+="\n"+html
    body=body.replace("{{SOURCE_TABLE}}", source_table())
    body,nfig=process(body)
    # collect headings for TOC: h1 in partband (data-toc) and h2
    for m in re.finditer(r'<div class="partband" id="(\w+)">.*?<h1>(.*?)</h1>', body, re.S):
        heads.append((1,m.group(1),re.sub("<.*?>","",m.group(2))))
    for m in re.finditer(r'<h2 id="(\w+)">(.*?)</h2>', body):
        heads.append((2,m.group(1),re.sub("<.*?>","",m.group(2))))
    # order by position
    pos={}
    for lvl,i,t in heads:
        pos[i]=body.find(f'id="{i}"')
    heads.sort(key=lambda h: pos[h[1]])
    toc_rows=""
    for lvl,i,t in heads:
        pg = toc_pages.get(i,"") if toc_pages else ""
        toc_rows+=f'<tr class="l{lvl}"><td>{t}</td><td class="pg">{pg}</td></tr>'
    cover=open("cover.html").read().replace("{{TOC_ROWS}}",toc_rows).replace("{{NFIG}}",str(nfig))
    # anchors: add invisible marker text after each id so we can find pages
    for lvl,i,t in heads:
        body=body.replace(f'id="{i}"', f'id="{i}"',1)
    html=f"<!doctype html><html><head><meta charset='utf-8'><title>JPMorgan GPB Advisor Internship: Complete Interview Pack</title><style>{css}</style></head><body>{cover}{body}</body></html>"
    return html, heads

def find_pages(pdf, heads):
    doc=pymupdf.open(pdf); pages={}
    # search for marker text 'Ⓐid' inserted invisibly
    for lvl,i,t in heads:
        marker=f"⟦{i}⟧"
        for pno,page in enumerate(doc):
            if page.search_for(marker):
                pages[i]=pno+1; break
    return pages

if __name__=="__main__":
    build_figs()
    html,heads=assemble()
    # insert invisible markers
    for lvl,i,t in heads:
        html=html.replace(f'id="{i}"', f'id="{i}"><span class="anchor">⟦{i}⟧</span',1) if False else html
    # simpler: put marker spans right after opening tag by regex
    def addmark(m):
        return m.group(0)+f'<span class="anchor">⟦{m.group(1)}⟧</span>'
    html=re.sub(r'<(?:div class="partband"|h2) id="(\w+)">', addmark, html)
    open("pack_pass1.html","w").write(html)
    subprocess.run(["node","topdf_pack.js","pack_pass1.html","pack_pass1.pdf","Complete Interview Pack"],check=True)
    pages=find_pages("pack_pass1.pdf",heads)
    print("pages found:",len(pages),"of",len(heads), file=sys.stderr)
    html,heads=assemble(pages)
    html=re.sub(r'<(?:div class="partband"|h2) id="(\w+)">', addmark, html)
    out="JPMorgan_GPB_Advisor_Internship_Complete_Interview_Pack"
    open(out+".html","w").write(html)
    subprocess.run(["node","topdf_pack.js",out+".html",out+".pdf","Complete Interview Pack"],check=True)
    doc=pymupdf.open(out+".pdf"); print("PDF pages:",doc.page_count,"figures:",len(ORDER)//2)
