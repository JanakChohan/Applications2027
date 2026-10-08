"""Two-pass render: HTML -> PDF with real TOC page numbers.
Each section heading carries id="sec-x"; TOC entries have <span class="pg" data-for="sec-x"></span>.
Pass 1 renders with a marker text in each heading; we find which page each marker lands on."""
import sys, re
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
src, out = sys.argv[1], sys.argv[2]
html = open(src, encoding='utf-8').read()
HEADER = '<div style="font-size:7.5px;width:100%;padding:0 14mm;color:#7a8499;font-family:Helvetica;display:flex;justify-content:space-between"><span>Real Estate Investor Relations, explained</span><span>Harrison Street ISG, London</span></div>'
FOOTER = '<div style="font-size:7.5px;width:100%;padding:0 14mm;color:#7a8499;font-family:Helvetica;display:flex;justify-content:space-between"><span>Built from public sources. See source table.</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
def render(h, path):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(); pg.set_content(h, wait_until='load')
        pg.pdf(path=path, format='A4', print_background=True, display_header_footer=True,
               header_template=HEADER, footer_template=FOOTER,
               margin={'top':'16mm','bottom':'16mm','left':'14mm','right':'14mm'})
        b.close()
ids = re.findall(r'data-for="([^"]+)"', html)
h1 = html
for i in ids:
    h1 = h1.replace(f'id="{i}">', f'id="{i}"><span style="font-size:4px;opacity:0.01">QQ{i}QQ</span>', 1)
pages = {}
for it in range(4):
    h2 = h1
    for i in ids:
        h2 = h2.replace(f'data-for="{i}"></span>', f'data-for="{i}">{pages.get(i,"")}</span>')
    render(h2, out)
    r = PdfReader(out); new = {}
    for n, page in enumerate(r.pages, 1):
        t = (page.extract_text() or '').replace('\n','').replace(' ','')
        for m in re.findall(r'QQ(.+?)QQ', t):
            new.setdefault(m, n)
    if new == pages: break
    pages = new
print('iterations', it+1, 'pages', len(PdfReader(out).pages), pages)
