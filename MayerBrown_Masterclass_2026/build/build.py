"""Assemble parts -> HTML, two-pass render -> PDF with real TOC page numbers."""
import re, json, os, subprocess, sys, glob, html
from pypdf import PdfReader, PdfWriter
import figures, qbank, sources

HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.dirname(HERE)
NAME="Mayer_Brown_SEO_Masterclass_2026_Complete_Interview_Pack"
TITLE="Mayer Brown × SEO London Masterclass 2026 · Complete Pack"

def load_parts():
    files=sorted(glob.glob(os.path.join(HERE,"parts","*.html")))
    return [(os.path.basename(f),open(f,encoding="utf-8").read()) for f in files]

def sub_figs(body, counter):
    def rep(m):
        key=m.group(1)
        svg,cap,full=figures.get(key)
        counter[0]+=1
        n=counter[0]
        cls=' class="fig-full"' if full else ''
        return f'<figure id="fig-{key}"{cls}>{svg}<figcaption><span class="fignum">Figure {n}.</span> {cap}</figcaption></figure>'
    return re.sub(r"\{\{FIG:([a-z0-9_]+)\}\}",rep,body)

def collect_toc(body):
    entries=[]
    for m in re.finditer(r'<section class="part[^"]*" id="([^"]+)" data-title="([^"]+)"',body):
        entries.append((m.start(),"part",m.group(1),m.group(2)))
    for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>',body,re.S):
        entries.append((m.start(),"sub",m.group(1),re.sub("<[^>]+>","",m.group(2))))
    entries.sort()
    return [(k,i,t) for _,k,i,t in entries]

def add_markers(body):
    body=re.sub(r'(<section class="part[^"]*" id="([^"]+)"[^>]*>)',lambda m:m.group(1)+f'<span class="pm">QZQ{m.group(2)}QZQ</span>',body)
    body=re.sub(r'<h2 id="([^"]+)">',lambda m:f'<h2 id="{m.group(1)}"><span class="pm">QZQ{m.group(1)}QZQ</span>',body)
    return body

def toc_html(entries,pages):
    rows=[]
    for k,i,t in entries:
        p=pages.get(i,"--")
        cls="row" if k=="part" else "row sub"
        tt=f"<b>{t}</b>" if k=="part" else t
        rows.append(f'<div class="{cls}"><span class="t"><a href="#{i}">{tt}</a></span><span class="p">{p}</span></div>')
    return '<div class="toc">'+"".join(rows)+'</div>'

def assemble(pages,markers):
    parts=load_parts()
    css=open(os.path.join(HERE,"style.css")).read()
    css+='\n.pm{position:absolute;font-size:3px;color:#fefefe;line-height:1;white-space:nowrap;}\n'
    cover=""; body=""
    for fn,txt in parts:
        if fn.startswith("00_"): cover=txt
        else: body+=txt+"\n"
    counter=[0]
    body=sub_figs(body,counter)
    body=body.replace("{{QBANK}}",qbank_html()).replace("{{ASK}}",ask_html())
    st,n=sources.table_html(); body=body.replace("{{SOURCES}}",st).replace("{{NSRC}}",str(n)).replace("{{NFIG}}",str(counter[0]))
    entries=collect_toc(body)
    body=body.replace("{{TOC}}",toc_html(entries,pages))
    if markers: body=add_markers(body)
    head=f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>Mayer Brown Masterclass Pack</title><style>{css}</style></head><body>'
    return head+body+"</body></html>", head+cover+"</body></html>", counter[0], entries

def qbank_html():
    out=[]; grp=None; i=0
    for g,q,t,st,f,tr in qbank.Q:
        i+=1
        if g!=grp: out.append(f"<h3>{g}</h3>"); grp=g
        out.append(f'<div class="qa"><div class="q">{i}. {q}</div><div><span class="k">Really testing</span> {t}</div><div><span class="k">Structure</span> {st}</div>'+(f'<div><span class="k">Facts to weave in</span> {f}</div>' if f else '')+f'<div><span class="k">Trap</span> {tr}</div></div>')
    return "".join(out)
def ask_html():
    out=['<table class="small"><thead><tr><th style="width:4%">#</th><th style="width:16%">To</th><th>Question</th><th style="width:14%">Built on</th></tr></thead><tbody>']
    for i,(w,q,src) in enumerate(qbank.ASK,1):
        out.append(f"<tr><td>{i}</td><td>{w}</td><td>{q}</td><td><span class='src'>{src}</span></td></tr>")
    return "".join(out)+"</tbody></table>"

def render(html_path,pdf_path,hf=True):
    subprocess.run(["node",os.path.join(HERE,"render.js"),html_path,pdf_path,"1" if hf else "0",TITLE],check=True)

def page_map(pdf):
    r=PdfReader(pdf); m={}
    for i,p in enumerate(r.pages):
        t=p.extract_text() or ""
        for k in re.findall(r"QZQ([A-Za-z0-9_\-]+?)QZQ",t):
            m.setdefault(k,i+1)
    return m,len(r.pages)

def main():
    tmp=os.path.join(HERE,"tmp"); os.makedirs(tmp,exist_ok=True)
    b1,cov,nf,entries=assemble({},True)
    open(f"{tmp}/pass1.html","w").write(b1)
    render(f"{tmp}/pass1.html",f"{tmp}/pass1.pdf")
    pages,np_=page_map(f"{tmp}/pass1.pdf")
    missing=[i for k,i,t in entries if i not in pages]
    print("figures:",nf,"pages:",np_,"missing markers:",missing[:10])
    b2,cov,nf,entries=assemble(pages,False)
    body_html=os.path.join(OUT,NAME+".html")
    # standalone HTML keeps cover at top
    full=b2.replace("<body>","<body>"+cov.split("<body>",1)[1].replace("</body></html>",""),1)
    open(body_html,"w").write(full)
    open(f"{tmp}/body.html","w").write(b2); open(f"{tmp}/cover.html","w").write(cov)
    render(f"{tmp}/body.html",f"{tmp}/body.pdf")
    render(f"{tmp}/cover.html",f"{tmp}/cover.pdf",hf=False)
    p2,np2=page_map(f"{tmp}/pass1.pdf")
    w=PdfWriter()
    for f in (f"{tmp}/cover.pdf",f"{tmp}/body.pdf"):
        for pg in PdfReader(f).pages: w.add_page(pg)
    w.add_metadata({"/Title":TITLE,"/Author":"Prep pack built from public sources"})
    with open(os.path.join(OUT,NAME+".pdf"),"wb") as fh: w.write(fh)
    json.dump(pages,open(f"{tmp}/pages.json","w"),indent=1)
    print("done",np2+1,"pages incl cover")

if __name__=="__main__" and len(sys.argv)==1: main()

def companions():
    import html as H
    # Cheat sheet PDF (one page)
    css=open(os.path.join(HERE,"style.css")).read()
    cheat=open(os.path.join(HERE,"parts","13_cheat.html")).read()
    cheat=cheat.replace('class="part"','class=""')
    doc=f'<!doctype html><html><head><meta charset="utf-8"><style>{css} @page{{size:A4;margin:10mm 11mm}}</style></head><body>{cheat}</body></html>'
    tmp=os.path.join(HERE,"tmp"); open(f"{tmp}/cheat.html","w").write(doc)
    render(f"{tmp}/cheat.html",os.path.join(OUT,"Cheat_Sheet.pdf"),hf=False)
    n=len(PdfReader(os.path.join(OUT,"Cheat_Sheet.pdf")).pages); print("cheat pages",n)
    # Question bank md
    def md(t): return re.sub("<[^>]+>","",t).replace("&amp;","&")
    L=["# Mayer Brown Masterclass 2026: question bank","","Scaffolds, not scripts. Built 8 October 2026 from public sources; [Sxx] markers resolve to Part 15 of the main pack.",""]
    grp=None
    for i,(g,q,t,st,f,tr) in enumerate(qbank.Q,1):
        if g!=grp: L+=[f"## {g}",""]; grp=g
        L+=[f"### {i}. {md(q)}",f"- **Really testing:** {md(t)}",f"- **Structure:** {md(st)}"]+([f"- **Facts to weave in:** {md(f)}"] if f else [])+[f"- **Trap:** {md(tr)}",""]
    L+=["## Ten questions to ask",""]
    for i,(w,q,src) in enumerate(qbank.ASK,1): L.append(f"{i}. **{w}:** {md(q)} {src}")
    open(os.path.join(OUT,"Question_Bank.md"),"w").write("\n".join(L)+"\n")

if __name__=="__main__" and len(sys.argv)>1 and sys.argv[1]=="companions": companions()
