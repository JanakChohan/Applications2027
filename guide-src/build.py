#!/usr/bin/env python3
import markdown, glob, os, sys
from weasyprint import HTML

base = os.path.dirname(os.path.abspath(__file__))
secdir = os.path.join(base, 'sections')
files = sorted(glob.glob(os.path.join(secdir, '*.md')))
if not files:
    print("no section files found"); sys.exit(1)
print("Assembling %d section files:" % len(files))
for f in files: print("  -", os.path.basename(f))

parts = []
for f in files:
    parts.append(open(f, encoding='utf-8').read().rstrip() + "\n")
md_text = "\n\n".join(parts)

md = markdown.Markdown(extensions=[
    'tables', 'attr_list', 'fenced_code', 'sane_lists', 'md_in_html'
])
body = md.convert(md_text)

css = open(os.path.join(base, 'style.css'), encoding='utf-8').read()
html = ("<!doctype html><html><head><meta charset='utf-8'>"
        "<style>%s</style></head><body>%s</body></html>" % (css, body))
open(os.path.join(base, 'guide.html'), 'w', encoding='utf-8').write(html)

out = os.path.join(base, 'guide.pdf')
HTML(string=html, base_url=base).write_pdf(out)
sz = os.path.getsize(out) / 1024.0
print("Wrote %s (%.0f KB)" % (out, sz))
