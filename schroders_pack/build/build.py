#!/usr/bin/env python3
"""Assemble the Schroders interview pack from HTML fragments and render PDFs.

Pipeline:
  1. Concatenate parts/*.html (sorted) into one document, add cover + TOC.
  2. Insert invisible anchor markers before every part opener and h2.
  3. Render once, find each marker's page with PyMuPDF, fill the TOC, re-render.
  4. Render the cover separately (no running header) and merge it in front.
  5. Render the spin-off PDFs (Question Bank, Reading List, Cheat Sheet).
  6. Rasterise figure pages to PNG for a clipping check.
"""
import glob, html, os, re, sys
import pymupdf as fitz
from pypdf import PdfReader, PdfWriter
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(ROOT)
CHROME = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome")[0]
NAME = "Schroders_Client_Group_Internship_2027_Complete_Interview_Pack"
CSS = open(os.path.join(ROOT, "style.css")).read()
HEADER_TXT = "Schroders &middot; Client Group Internship Programme 2027 &middot; Interview Research Pack"

HEADER = f"""<div style="width:100%;font-family:'Source Sans 3',Arial;font-size:7.5px;color:#7A808C;
padding:0 15mm;display:flex;justify-content:space-between;"><span>{HEADER_TXT}</span>
<span>Built 29 Sep 2026 from public sources</span></div>"""
FOOTER = """<div style="width:100%;font-family:'Source Sans 3',Arial;font-size:7.5px;color:#7A808C;
padding:0 15mm;display:flex;justify-content:space-between;"><span>[C] Confirmed &middot; [R] Reported &middot; [I] Inferred &middot; [Sxx] see Part 15</span>
<span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>"""


def doc(body, title):
    return f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<title>{title}</title><style>{CSS}</style></head><body>{body}</body></html>"""


import json
KEYMAP = json.load(open(os.path.join(ROOT, "keymap.json"))) if os.path.exists(os.path.join(ROOT, "keymap.json")) else {}


def expand(txt):
    txt = re.sub(r"<!--INCLUDE:([\w.\-]+)-->", lambda m: open(os.path.join(ROOT, "fragments", m.group(1))).read(), txt)
    def key(m):
        k = m.group(1)
        if k not in KEYMAP:
            print("MISSING KEY", k); return "[S?]"
        return KEYMAP[k]
    txt = re.sub(r"\{\{([A-Z_0-9]+)\}\}", key, txt)
    pieces = re.split(r"(<svg.*?</svg>)", txt, flags=re.S)
    for i in range(0, len(pieces), 2):  # only outside inline SVG
        t = re.sub(r"\[(S\d+(?:[,\u2013\- ]+S?\d+)*)\]", r'<span class="src">[\1]</span>', pieces[i])
        for w, c in (("Confirmed", "c"), ("Reported", "r"), ("Inferred", "i")):
            t = t.replace(f"[{w}]", f'<span class="tag {c}">{w}</span>')
        pieces[i] = t
    return "".join(pieces)


def load_parts():
    files = sorted(glob.glob(os.path.join(ROOT, "parts", "*.html")))
    return [(os.path.basename(f), expand(open(f).read())) for f in files]


def add_markers(body):
    """Give every part opener and h2 an id + marker, return body and toc entries."""
    toc = []
    n = [0]

    def part_sub(m):
        n[0] += 1
        aid = f"A{n[0]:03d}"
        title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        toc.append((1, aid, f"Part {len([t for t in toc if t[0] == 1])}: {title}"))
        return f'<span class="anchor-marker">@@{aid}@@</span>{m.group(1)}{m.group(2)}</h1>'

    def h2_sub(m):
        n[0] += 1
        aid = f"A{n[0]:03d}"
        title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if 'data-notoc' not in m.group(1):
            toc.append((2, aid, title))
        return f'<span class="anchor-marker">@@{aid}@@</span>{m.group(1)}{m.group(2)}</h2>'

    pattern = re.compile(r'(<h1 class="ph"[^>]*>|<h2[^>]*>)(.*?)</h(1|2)>', re.S)

    def dispatch(m):
        if m.group(1).startswith("<h1"):
            return part_sub(m)
        return h2_sub(m)

    body = pattern.sub(dispatch, body)
    return body, toc


def toc_html(toc, pages):
    rows = []
    for lvl, aid, title in toc:
        p = pages.get(aid, "")
        rows.append(f'<div class="row l{lvl}"><span class="t">{title}</span><span class="p">{p}</span></div>')
    return ('<section class="tocsec"><div class="part-band" style="--band:#C8813A"><div class="pn">Contents</div>'
            '<h1 style="color:#fff">What is in this pack</h1><p class="lede">Page numbers match the running footer. '
            'The cover is unnumbered.</p></div><div class="toc">' + "".join(rows) + "</div></section>")


def render(page, html_str, path, header=True):
    page.set_content(html_str, wait_until="networkidle")
    page.emulate_media(media="print")
    kw = dict(path=path, format="A4", print_background=True,
              margin=dict(top="18mm", bottom="18mm", left="15mm", right="15mm"))
    if header:
        kw.update(display_header_footer=True, header_template=HEADER, footer_template=FOOTER)
    else:
        kw.update(margin=dict(top="0", bottom="0", left="0", right="0"))
    page.pdf(**kw)


def find_pages(pdf_path):
    pages = {}
    d = fitz.open(pdf_path)
    for i, pg in enumerate(d):
        for m in re.finditer(r"@@(A\d{3})@@", pg.get_text()):
            pages.setdefault(m.group(1), i + 1)
    return pages, d.page_count


def main():
    parts = load_parts()
    cover = next(c for n, c in parts if "cover" in n)
    body_parts = [c for n, c in parts if "cover" not in n]
    joined = "\n".join(body_parts)
    cnt = [0]
    def fignum(m):
        cnt[0] += 1
        return f"<b>Figure {cnt[0]}.</b>"
    joined = re.sub(r"<b>Figure #\.</b>", fignum, joined)
    print("figures numbered:", cnt[0])
    body, toc = add_markers(joined)

    html_path = os.path.join(OUT, NAME + ".html")
    pdf_path = os.path.join(OUT, NAME + ".pdf")
    tmp = os.path.join(ROOT, "_tmp")
    os.makedirs(tmp, exist_ok=True)

    with sync_playwright() as p:
        br = p.chromium.launch(executable_path=CHROME)
        page = br.new_page()
        # pass 1
        first = doc(toc_html(toc, {a: "00" for _, a, _ in toc}) + body, "pass1")
        render(page, first, os.path.join(tmp, "pass1.pdf"))
        pages, _ = find_pages(os.path.join(tmp, "pass1.pdf"))
        # pass 2
        final_body = toc_html(toc, pages) + body
        render(page, doc(final_body, "Schroders Client Group Interview Pack"), os.path.join(tmp, "body.pdf"))
        pages2, total = find_pages(os.path.join(tmp, "body.pdf"))
        mism = [a for a in pages if pages[a] != pages2.get(a)]
        if mism:
            print("WARNING page shift after pass 2:", mism[:10])
        render(page, doc('<style>@page{size:A4;margin:0}.cover{height:297mm;width:210mm}</style>' + cover, "cover"), os.path.join(tmp, "cover.pdf"), header=False)

        w = PdfWriter()
        for f in ("cover.pdf", "body.pdf"):
            for pg in PdfReader(os.path.join(tmp, f)).pages:
                w.add_page(pg)
        w.add_metadata({"/Title": "Schroders Client Group Internship 2027: Complete Interview Pack"})
        with open(pdf_path, "wb") as fh:
            w.write(fh)
        with open(html_path, "w") as fh:
            fh.write(doc(cover + final_body, "Schroders Client Group Interview Pack"))
        print(f"Main pack: {total + 1} pages -> {pdf_path}")

        # Spin-offs: any element with data-spin="qb|rl|cs" is extracted.
        full = "\n".join(body_parts)
        for key, fname, title in (("qb", "Question_Bank", "Question Bank"),
                                  ("rl", "Reading_List", "Reading List"),
                                  ("cs", "Cheat_Sheet", "Cheat Sheet")):
            chunks = re.findall(r'<!--SPIN:%s-->(.*?)<!--/SPIN:%s-->' % (key, key), full, re.S)
            if not chunks:
                print("no spin content for", key)
                continue
            sb = "\n".join(chunks).replace('class="part"', 'class="part0"')
            if key != "cs":
                sb = (f'<div class="part-band" style="--band:#C8813A"><div class="pn">Schroders Client Group Internship 2027</div>'
                      f'<h1 style="color:#fff">{title}</h1><p class="lede">Extracted from the complete interview pack. Source markers resolve to Part 15 of the full pack.</p></div>') + sb
            spath = os.path.join(OUT, f"Schroders_Client_Group_2027_{fname}.pdf")
            render(page, doc(sb, title), spath)
            with open(spath.replace(".pdf", ".html"), "w") as fh:
                fh.write(doc(sb, title))
            print(f"{fname}: {fitz.open(spath).page_count} pages")
        br.close()

    # Rasterise every page that contains an svg-heavy figure for eyeballing.
    if "--png" in sys.argv:
        d = fitz.open(pdf_path)
        pngdir = os.path.join(tmp, "png")
        os.makedirs(pngdir, exist_ok=True)
        for f in glob.glob(os.path.join(pngdir, "*.png")):
            os.remove(f)
        for i, pg in enumerate(d):
            pg.get_pixmap(dpi=60).save(os.path.join(pngdir, f"p{i+1:03d}.png"))
        print("PNGs in", pngdir)


if __name__ == "__main__":
    main()
