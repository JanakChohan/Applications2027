import re, glob, os, html, sys
B=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(B,'..','research')
css=open(os.path.join(B,'style.css')).read()
body='\n'.join(open(p).read() for p in sorted(glob.glob(os.path.join(B,'parts','*.html'))))
used=sorted({int(n) for n in re.findall(r'S(\d+)', ' '.join(re.findall(r'\[S[\dS,\s\-]+\]', body)))})
rows={}
for f in sorted(glob.glob(os.path.join(R,'WS*.md'))):
    for line in open(f):
        m=re.match(r'^\s*\[S(\d+)\]\s*\|(.*)$', line.strip())
        if m and int(m.group(1)) not in rows: rows[int(m.group(1))]=[c.strip() for c in m.group(2).split('|')]
def c(r,i): return html.escape(r[i]) if len(r)>i else ''
missing=[n for n in used if n not in rows]
if missing: print('MISSING SOURCES', missing)
trs=''.join(f'<tr><td><b>S{n}</b></td><td>{c(rows[n],0)}</td><td>{c(rows[n],1)}</td><td>{c(rows[n],2)}</td><td style="word-break:break-all">{c(rows[n],3)}</td><td>{c(rows[n],5)}</td></tr>' for n in used if n in rows)
body=body.replace('<!--SOURCETABLE-->','<table class="src"><thead><tr><th>ID</th><th>Outlet</th><th>Title</th><th>Date</th><th>URL (accessed Oct 2026)</th><th>Status</th></tr></thead><tbody>'+trs+'</tbody></table>')
def tagify(t):
    t=re.sub(r'\[(S\d+(?:[,\s\-]+S\d+)*)\]', lambda m:'<span class="s">['+m.group(1)+']</span>', t)
    return t.replace('[Confirmed]','<span class="c">Confirmed</span>').replace('[Reported]','<span class="r">Reported</span>').replace('[Inferred]','<span class="i">Inferred</span>')
body=''.join(x if x.startswith('<svg') else tagify(x) for x in re.split(r'(<svg.*?</svg>)', body, flags=re.S))
body=re.sub(r'<(div|h2)([^>]*?)data-toc="([A-Za-z0-9_]+)"[^>]*>', lambda m:m.group(0)+f'<span class="mk">QQ{m.group(3)}QQ</span>', body)
toc=re.findall(r'data-toc="([A-Za-z0-9_]+)"[^>]*data-title="([^"]+)"(?:[^>]*data-lvl="(\d)")?', body)
body=body.replace('<!--TOC-->','\n'.join(f'<div class="row{" sub" if l=="2" else ""}"><span class="t">{t}</span><span class="dots"></span><span class="tocpg" data-for="{i}">000</span></div>' for i,t,l in toc))
open(os.path.join(B,'psg.html'),'w').write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Inside Hayfin PSG</title><style>{css}</style></head><body>{body}</body></html>')
print('sources used',len(used),'toc',len(toc))
