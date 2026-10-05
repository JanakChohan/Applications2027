# Build Part 15 (source table) from the [Sxx] rows in research/WS*.md
import re, glob, html, os
rows = {}
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), '../research/WS*.md'))):
    ws = os.path.basename(f)[:-3]
    for line in open(f):
        m = re.match(r'^\|?\s*\[S(\d+)\]\s*\|(.*)$', line.strip())
        if not m: continue
        cells = [c.strip() for c in m.group(2).strip().strip('|').split('|')]
        n = int(m.group(1))
        if n in rows: continue
        rows[n] = (ws, cells)
def e(s): return html.escape(s)
out = ['<section class="part" id="p15" data-toc="Part 15: Source table">',
 '<div class="band"><div class="num">Part 15</div><h1>Every source, in one table</h1><p class="lede">Each [Sxx] marker in the pack resolves here. All accessed 5 October 2026. Status shows whether the page was read in full (FETCHED), seen only as a search snippet (SNIPPET), or paywalled and not read.</p></div>',
 f'<h2 id="p15-table">Source table ({len(rows)} sources)</h2>',
 '<table class="src tight"><thead><tr><th>ID</th><th>Outlet</th><th>Title</th><th>Published</th><th>URL</th><th>Status</th><th>Confidence note</th></tr></thead><tbody>']
byurl={}
for n in sorted(rows):
    u=(rows[n][1]+['']*4)[3].strip().rstrip('/')
    if u.startswith('http'): byurl.setdefault(u,[]).append(n)
for n in sorted(rows):
    ws, c = rows[n]
    c = c + [''] * (7 - len(c))
    outlet, title, pub, url = c[0], c[1], c[2], c[3]
    rest = c[4:]
    status = next((x for x in rest if re.search(r'FETCHED|SNIPPET|PAYWALL', x)), '')
    note = ' | '.join(x for x in rest if x != status and not x.startswith('Accessed'))
    same=[m for m in byurl.get(url.strip().rstrip('/'),[]) if m!=n]
    if same: note = f"Same document as {', '.join('S'+str(m) for m in same)}. " + note
    out.append(f'<tr><td><b>S{n}</b></td><td>{e(outlet)}</td><td>{e(title)}</td><td>{e(pub)}</td><td>{e(url)}</td><td>{e(status)}</td><td>{e(note)}</td></tr>')
out.append('</tbody></table></section>')
open(os.path.join(os.path.dirname(__file__), 'parts/15_sources.html'), 'w').write('\n'.join(out))
print(len(rows), 'sources')
