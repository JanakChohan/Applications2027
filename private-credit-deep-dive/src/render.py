#!/usr/bin/env python3
"""Assemble the pack HTML from chunks, render to PDF in two passes so the
contents page carries real page numbers, then audit figures for clipping."""
import re, sys, pathlib, json
from playwright.sync_api import sync_playwright
import pypdf, pypdfium2

BUILD = pathlib.Path(__file__).parent
OUT   = BUILD.parent / "out"
OUT.mkdir(exist_ok=True)
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
NAME   = "Private_Credit_Deep_Dive"

HDR = ("<div style=\"font-family:Liberation Sans,Arial,sans-serif;font-size:6.5pt;color:#8A93A0;"
       "width:100%;padding:0 14mm;display:flex;justify-content:space-between;\">"
       "<span>Private credit &nbsp;·&nbsp; a deep dive from zero</span>"
       "<span>Built from public sources</span></div>")
FTR = ("<div style=\"font-family:Liberation Sans,Arial,sans-serif;font-size:6.5pt;color:#8A93A0;"
       "width:100%;padding:0 14mm;display:flex;justify-content:space-between;\">"
       "<span>Compiled 19 September 2026</span>"
       "<span>Page <span class=\"pageNumber\"></span> of <span class=\"totalPages\"></span></span></div>")

def assemble():
    parts = sorted(p for p in BUILD.glob("*.html"))
    html = "".join(p.read_text(encoding="utf-8") for p in parts)
    return html

def pdf(html_path, pdf_path, header=True):
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=CHROME, args=["--no-sandbox","--font-render-hinting=none"])
        pg = b.new_page()
        pg.goto("file://" + str(html_path.resolve()), wait_until="networkidle")
        pg.emulate_media(media="print")
        pg.pdf(path=str(pdf_path), format="A4", print_background=True,
               margin={"top":"19mm","bottom":"17mm","left":"14mm","right":"14mm"},
               display_header_footer=header, header_template=HDR, footer_template=FTR,
               prefer_css_page_size=True)
        b.close()

def marker_pages(pdf_path):
    """Map @@ANCHOR:id@@ markers to the 1-based PDF page they land on."""
    r = pypdf.PdfReader(str(pdf_path))
    m = {}
    for i, page in enumerate(r.pages, start=1):
        try: txt = page.extract_text() or ""
        except Exception: txt = ""
        for a in re.findall(r"@@ANCHOR:([A-Za-z0-9_.\-]+)@@", txt.replace("\n","")):
            m.setdefault(a, i)
    return m, len(r.pages)

def inject(html, pages):
    def rep(mo):
        ref = mo.group(1)
        return '<span class="p">%s</span>' % pages.get(ref, "—")
    return re.sub(r'<span class="p" data-ref="([A-Za-z0-9_.\-]+)"></span>', rep, html)

def audit(html_path):
    """In-browser overflow audit: any element wider than its container, any svg
    text outside its viewBox, any table/figure exceeding the A4 content width."""
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        pg = b.new_page(viewport={"width":688,"height":1123})
        pg.goto("file://" + str(html_path.resolve()), wait_until="networkidle")
        pg.emulate_media(media="print")
        res = pg.evaluate("""() => {
          const CONTENT_W = document.documentElement.clientWidth;  // viewport = printed content width
          const bad = [];
          document.querySelectorAll('figure,table,.card,.box,svg,pre').forEach(el=>{
            const r = el.getBoundingClientRect();
            if (r.width > CONTENT_W + 1.5)
              bad.push({kind:'wide', tag:el.tagName, id:el.id||'', w:Math.round(r.width),
                        max:Math.round(CONTENT_W), near:(el.textContent||'').trim().slice(0,70)});
            if (el.scrollWidth > el.clientWidth + 2 && el.tagName!=='svg')
              bad.push({kind:'hscroll', tag:el.tagName, id:el.id||'',
                        sw:el.scrollWidth, cw:el.clientWidth, near:(el.textContent||'').trim().slice(0,70)});
          });
          // svg text escaping its own viewBox
          document.querySelectorAll('svg').forEach(svg=>{
            const vb = svg.viewBox && svg.viewBox.baseVal;
            if(!vb || !vb.width) return;
            svg.querySelectorAll('text,rect,line,path,circle').forEach(t=>{
              // getBBox() is pre-transform, so a rotated/translated element's box is not
              // comparable to the viewBox. Skip those and rely on the visual page check.
              if (t.hasAttribute('transform')) return;
              let bb; try{ bb = t.getBBox(); }catch(e){ return; }
              const pad = 0.6;
              if (bb.x < vb.x - pad || bb.y < vb.y - pad ||
                  bb.x + bb.width  > vb.x + vb.width  + pad ||
                  bb.y + bb.height > vb.y + vb.height + pad)
                bad.push({kind:'svg-overflow', id:svg.id||'(no id)', el:t.tagName,
                          txt:(t.textContent||'').trim().slice(0,45),
                          box:[Math.round(bb.x),Math.round(bb.y),Math.round(bb.width),Math.round(bb.height)],
                          vb:[vb.x,vb.y,vb.width,vb.height]});
            });
          });
          const figs = document.querySelectorAll('figure').length;
          const svgs = document.querySelectorAll('figure svg').length;
          return {bad, figs, svgs, words: document.body.innerText.split(/\\s+/).length};
        }""")
        b.close()
    return res

def raster(pdf_path, pages, outdir, scale=1.6):
    outdir.mkdir(exist_ok=True, parents=True)
    doc = pypdfium2.PdfDocument(str(pdf_path))
    written=[]
    for p in pages:
        if p < 1 or p > len(doc): continue
        img = doc[p-1].render(scale=scale).to_pil()
        f = outdir / ("page_%03d.png" % p)
        img.save(f); written.append(str(f))
    return written

if __name__ == "__main__":
    html = assemble()
    src = OUT / (NAME + ".html")
    # pass 1
    tmp = OUT / "_pass1.html"; tmp.write_text(html, encoding="utf-8")
    pdf(tmp, OUT / "_pass1.pdf")
    pages, n = marker_pages(OUT / "_pass1.pdf")
    print("pass1 pages:", n, "| anchors found:", len(pages))
    missing = re.findall(r'data-ref="([A-Za-z0-9_.\-]+)"', html)
    miss = [m for m in set(missing) if m not in pages]
    if miss: print("!! TOC refs with no anchor:", sorted(miss))
    # pass 2
    html2 = inject(html, pages)
    src.write_text(html2, encoding="utf-8")
    pdf(src, OUT / (NAME + ".pdf"))
    _, n2 = marker_pages(OUT / (NAME + ".pdf"))
    print("final pages:", n2)
    a = audit(src)
    print("figures:", a["figs"], "| svg figures:", a["svgs"], "| words:", a["words"])
    print("layout problems:", len(a["bad"]))
    for x in a["bad"][:40]: print("   ", json.dumps(x))
    json.dump({"pages":n2,"anchors":pages,"audit":a}, open(OUT/"_audit.json","w"), indent=1)
