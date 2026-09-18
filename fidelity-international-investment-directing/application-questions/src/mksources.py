#!/usr/bin/env python3
"""Build the source table for the questions pack from the T-range research files,
filtered to markers actually cited in the built HTML."""
import re, glob, html as H, pathlib
HERE = pathlib.Path(__file__).parent
Q    = HERE.parent / 'q'

EDITOR = {
 'T260': ('Fidelity International','Investment Directing Summer Internship 2027, London. Full job posting, supplied verbatim by the candidate.','2026 cycle','careers.fidelityinternational.com','VERBATIM','Authoritative. Stored at research/JD_VERBATIM.md in this repository.'),
 'T261': ('Fidelity International','Careers site: hiring process, FAQs and early careers pages','accessed 2026','careers.fidelityinternational.com','FETCHED','Primary. Source of the strengths-based description.'),
 'T262': ('This repository','Fidelity International interview pack, Parts 2 to 4 and its source table','2026-09-16','fidelity-international-investment-directing/','DERIVED','Facts carried over from the first pack, each individually sourced there.'),
}

def collect():
    cited=set()
    for f in sorted(glob.glob(str(HERE/'*.html'))):
        for m in re.findall(r'\[(T\d+)\]', open(f,encoding='utf-8').read()): cited.add(m)
    rows=dict(EDITOR)
    for f in sorted(glob.glob(str(Q/'T*.md'))):
        for line in open(f,encoding='utf-8'):
            line=line.strip()
            m=re.match(r'^\[(T\d+)\]\s*\|(.*)$', line)
            if not m: continue
            sid=m.group(1)
            if sid in rows: continue
            p=[x.strip() for x in m.group(2).split('|')]
            g=lambda i:(p[i] if len(p)>i else '')
            url=g(3)
            if not url.startswith('http'):
                url=next((x for x in p if x.startswith('http')),'')
            rows[sid]=(g(0),g(1),g(2),url,g(5),' | '.join(p[6:]) if len(p)>6 else '')
    return cited, rows

def chip(s):
    s=(s or '').upper()
    if 'PAYWALL'  in s: return '<span class="cf cf-r">PAYWALLED</span>'
    if 'VERBATIM' in s: return '<span class="cf cf-c">VERBATIM</span>'
    if 'FETCH'    in s: return '<span class="cf cf-c">FETCHED</span>'
    if 'SNIPPET'  in s: return '<span class="cf cf-r">SNIPPET</span>'
    if 'DERIVED'  in s: return '<span class="cf cf-i">DERIVED</span>'
    if 'INFER'    in s: return '<span class="cf cf-i">INFERRED</span>'
    return '<span class="cf cf-r">%s</span>' % (H.escape(s[:12]) or '&mdash;')

if __name__ == '__main__':
    cited, rows = collect()
    ids = sorted(cited, key=lambda s:int(s[1:]))
    missing = [i for i in ids if i not in rows]
    out=['<section class="part">\n<span class="marker">@@ANCHOR:q4@@</span>\n',
     '<div class="part-band"><p class="kicker">Part 4</p><h2 class="part-title">Source table</h2>',
     '<p class="standfirst">Every marker used in this pack. %d sources. FETCHED means the page was read in full. '
     'SNIPPET means only a search summary was seen. PAYWALLED means the content was not read and was not guessed at. '
     'Check the status of any source before you rely on its claim in a written answer.</p></div>\n' % len(ids),
     '<table class="long srctable"><thead><tr><th style="width:5%">ID</th><th style="width:15%">Outlet</th>'
     '<th style="width:30%">Title</th><th style="width:10%">Published</th><th style="width:24%">URL</th>'
     '<th style="width:8%">Status</th><th style="width:8%">Accessed</th></tr></thead><tbody>\n']
    for sid in ids:
        if sid in rows:
            o,t,pub,url,st,note = rows[sid]
            out.append('<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td><td class="u">%s</td><td>%s</td><td>2026-09-18</td></tr>\n'
                       % (sid,H.escape(o)[:60],H.escape(t)[:150],H.escape(pub)[:28],H.escape(url)[:140],chip(st)))
        else:
            out.append('<tr><td><strong>%s</strong></td><td colspan="6"><em>No row recorded by the workstream that used this marker. Treat any claim citing it as unverified.</em></td></tr>\n' % sid)
    out.append('</tbody><caption>All URLs accessed 18 September 2026.</caption></table>\n</section>\n')
    (HERE/'80_part04.html').write_text(''.join(out), encoding='utf-8')
    print("sources:", len(ids), "| unmatched:", missing or "none")
