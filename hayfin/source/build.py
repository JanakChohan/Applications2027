import re, glob, os, html, sys
B = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(B, '..', 'research')
css = open(os.path.join(B, 'style.css')).read()
parts = sorted(glob.glob(os.path.join(B, 'parts', '*.html')))
body = '\n'.join(open(p).read() for p in parts)

# sources table
rows = {}
for f in sorted(glob.glob(os.path.join(R, 'WS*.md'))):
    for line in open(f):
        m = re.match(r'^\s*\[S(\d+)\]\s*\|(.*)$', line.strip())
        if not m: continue
        n = int(m.group(1)); cells = [c.strip() for c in m.group(2).split('|')]
        if n in rows: continue
        rows[n] = cells
def cell(c, i): return html.escape(c[i]) if len(c) > i else ''
trs = []
for n in sorted(rows):
    c = rows[n]
    if not c or 'reserved' in c[0].lower(): continue
    url = cell(c, 3)
    trs.append(f'<tr><td><b>S{n}</b></td><td>{cell(c,0)}</td><td>{cell(c,1)}</td><td>{cell(c,2)}</td><td style="word-break:break-all">{url}</td><td>{cell(c,5)}</td><td>{cell(c,6)}</td></tr>')
srctable = ('<table class="src"><thead><tr><th style="width:5%">ID</th><th style="width:13%">Outlet</th><th style="width:22%">Title</th><th style="width:9%">Pub. date</th><th style="width:27%">URL (all accessed 2026-10-08)</th><th style="width:8%">Status</th><th>Note</th></tr></thead><tbody>'
            + '\n'.join(trs) + '</tbody></table>')
body = body.replace('<!--SOURCETABLE-->', srctable).replace('<!--SOURCECOUNT-->', str(len(trs)))

# inline tags (outside svg only)
def tagify(t):
    t = re.sub(r'\[(S\d+(?:[,\s\-]+S\d+)*)\]', lambda m: '<span class="s">['+m.group(1)+']</span>', t)
    return t.replace('[Confirmed]','<span class="c">Confirmed</span>').replace('[Reported]','<span class="r">Reported</span>').replace('[Inferred]','<span class="i">Inferred</span>')
chunks = re.split(r'(<svg.*?</svg>)', body, flags=re.S)
body = ''.join(c if c.startswith('<svg') else tagify(c) for c in chunks)
# TOC markers
toc = []
def mark(m):
    tag, attrs, tid, inner_start = m.group(1), m.group(2), m.group(3), m.group(0)
    return m.group(0) + f'<span class="mk">QQ{tid}QQ</span>'
body = re.sub(r'<(div|h2|section)([^>]*?)data-toc="([A-Za-z0-9_]+)"[^>]*>', mark, body)
for m in re.finditer(r'data-toc="([A-Za-z0-9_]+)"[^>]*data-title="([^"]+)"(?:[^>]*data-lvl="(\d)")?', body):
    toc.append((m.group(1), m.group(2), m.group(3) or '1'))
tochtml = '\n'.join(
    f'<div class="row{" sub" if l=="2" else ""}"><span class="t">{t}</span><span class="dots"></span><span class="tocpg" data-for="{i}">000</span></div>'
    for i, t, l in toc)
body = body.replace('<!--TOC-->', tochtml)
out = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Hayfin PSG Interview Pack</title><style>{css}</style></head><body>{body}</body></html>'''
dest = sys.argv[1] if len(sys.argv) > 1 else os.path.join(B, 'pack.html')
open(dest, 'w').write(out)
print('sources', len(trs), 'toc', len(toc), 'bytes', len(out))
