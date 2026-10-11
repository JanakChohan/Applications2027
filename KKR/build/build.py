#!/usr/bin/env python3
"""Assemble parts into one HTML, two-pass render to PDF with real TOC page numbers.

Usage: python3 build.py main|kcs|cheat [--png]
"""
import re, sys, subprocess, html, pathlib, json
from pypdf import PdfWriter, PdfReader

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT.parent / "output"
CSS = (ROOT / "style.css").read_text()

REPORTS = {
    "main": dict(parts="parts_main", cover="cover_main.html",
                 stem="KKR_London_Summer_Internship_2027_Complete_Interview_Pack",
                 header="KKR London Summer Internship 2027 · Complete Interview Pack"),
    "kcs": dict(parts="parts_kcs", cover="cover_kcs.html",
                stem="KKR_Client_Solutions_KCS_Deep_Dive",
                header="KKR Global Client Solutions (KCS) · Role Deep Dive"),
    "learn": dict(parts="parts_learn", cover="cover_learn.html",
                  stem="KKR_KCS_What_You_Will_Learn_Technical_Guide",
                  header="KKR KCS · What you will learn: the technical guide"),
    "cheat": dict(parts="parts_cheat", cover=None,
                  stem="Cheat_Sheet", header="KKR KCS · Cheat Sheet"),
}

CONF = {"Confirmed": "c", "Reported": "r", "Inferred": "i"}


def decorate(body: str):
    # leave SVG blocks untouched (spans are invalid inside SVG)
    parts = re.split(r"(<svg.*?</svg>)", body, flags=re.S)
    out = []
    for i, seg in enumerate(parts):
        out.append(seg if i % 2 else _decorate_text(seg))
    body = "".join(out)
    n = [0]
    def fig(m):
        n[0] += 1
        return f'<span class="fig-num">Figure {n[0]}.</span>'
    body = re.sub(r'<span class="fig-num"></span>', fig, body)
    return body, n[0]


def _decorate_text(body: str) -> str:
    # [S12] or [S12, S40] or [S12-S14] -> styled source marker (skip inside src-table first cells handled by class)
    body = re.sub(r"\[(S\d+(?:\s*[,–-]\s*S?\d+)*)\]", r'<span class="src">[\1]</span>', body)
    body = re.sub(r"\[(Confirmed|Reported|Inferred)\]",
                  lambda m: f'<span class="conf {CONF[m.group(1)]}">{m.group(1).upper()}</span>', body)
    return body


def build_toc(body: str):
    entries = []
    def part_marker(m):
        pid = m.group(1)
        entries.append(("part", pid, None))
        return m.group(0)
    # collect parts and h2s in order
    items = []
    for m in re.finditer(r'<section class="part[^"]*" id="([^"]+)"[^>]*>|<h2 id="([^"]+)"[^>]*>(.*?)</h2>', body, re.S):
        if m.group(1):
            pid = m.group(1)
            seg = body[m.end(): m.end() + 1500]
            num = re.search(r'<div class="num">(.*?)</div>', seg, re.S)
            h1 = re.search(r"<h1>(.*?)</h1>", seg, re.S)
            items.append(("part", pid, (num.group(1) if num else "") + " · " + re.sub("<.*?>", "", h1.group(1) if h1 else pid)))
        else:
            items.append(("sub", m.group(2), re.sub("<.*?>", "", m.group(3))))
    # insert markers
    def add_marker_part(m):
        return m.group(0) + f'<span class="marker">@@{m.group(1)}@@</span>'
    body = re.sub(r'<section class="part[^"]*" id="([^"]+)"[^>]*>', add_marker_part, body)
    body = re.sub(r'(<h2 id="([^"]+)"[^>]*>)(.*?)(</h2>)',
                  lambda m: m.group(1) + m.group(3) + f'<span class="marker">@@{m.group(2)}@@</span>' + m.group(4), body, flags=re.S)
    return body, items


def toc_html(items, pages, with_subs=True):
    rows = []
    for kind, pid, title in items:
        if kind == "sub" and not with_subs:
            continue
        p = pages.get(pid, "00")
        cls = "sub" if kind == "sub" else ""
        rows.append(f'<li class="{cls}"><span class="t"><a href="#{pid}">{title}</a></span><span class="p">{p}</span></li>')
    return '<section class="toc"><h1>Contents</h1><ol>' + "\n".join(rows) + "</ol></section>"


def page_map(pdf_path):
    pages = {}
    import pypdfium2 as pdfium
    pdf = pdfium.PdfDocument(str(pdf_path))
    for i in range(len(pdf)):
        txt = pdf[i].get_textpage().get_text_range() or ""
        txt = re.sub(r"\s", "", txt)
        for m in re.finditer(r"@@([A-Za-z0-9_\-]+)@@", txt):
            pages.setdefault(m.group(1), i + 1)
    return pages


def render(html_path, pdf_path, header, mode=""):
    subprocess.run(["node", str(ROOT / "render.mjs"), str(html_path), str(pdf_path), header, mode], check=True)


def main():
    key = sys.argv[1]
    cfg = REPORTS[key]
    parts_dir = ROOT / cfg["parts"]
    global OUT
    files = sorted(parts_dir.glob("*.html"))
    if "--only" in sys.argv:
        pref = sys.argv[sys.argv.index("--only") + 1].split(",")
        files = [f for f in files if any(f.name.startswith(x) for x in pref)]
        OUT = OUT / ("_preview_" + key + "_" + "_".join(pref))
        OUT.mkdir(parents=True, exist_ok=True)
    def inc(m):
        return (ROOT / m.group(1)).read_text()
    body = "\n".join(re.sub(r'<!--#include "([^"]+)"-->', inc, f.read_text()) for f in files)
    body, nfig = decorate(body)
    body, items = build_toc(body)
    with_toc = key != "cheat"
    head = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{cfg["header"]}</title><style>{CSS}</style></head><body>'
    tmp = OUT / f"_{key}_pass1.html"
    final_html = OUT / f'{cfg["stem"]}.html'
    body_pdf = OUT / f"_{key}_body.pdf"
    pages = {}
    for p in range(2):
        doc = head + (toc_html(items, pages) if with_toc else "") + body + "</body></html>"
        tmp.write_text(doc)
        render(tmp, body_pdf, cfg["header"])
        pages = page_map(body_pdf)
    missing = [pid for _, pid, _ in items if pid not in pages]
    if missing:
        print("WARNING markers not found:", missing)
    # final html (standalone, includes cover)
    cover_html = ""
    if cfg["cover"]:
        cover_src = (ROOT / cfg["cover"]).read_text()
        cover_doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{cover_src}</body></html>'
        cpath = OUT / f"_{key}_cover.html"
        cpath.write_text(cover_doc)
        cover_pdf = OUT / f"_{key}_cover.pdf"
        render(cpath, cover_pdf, "", "cover")
        cover_html = cover_src
        w = PdfWriter()
        for f in (cover_pdf, body_pdf):
            for pg in PdfReader(str(f)).pages:
                w.add_page(pg)
        w.write(str(OUT / f'{cfg["stem"]}.pdf'))
    else:
        (OUT / f'{cfg["stem"]}.pdf').write_bytes(body_pdf.read_bytes())
    final_html.write_text(head + cover_html + (toc_html(items, pages) if with_toc else "") + body + "</body></html>")
    n = len(PdfReader(str(OUT / f'{cfg["stem"]}.pdf')).pages)
    print(f"{cfg['stem']}.pdf: {n} pages, {nfig} figures, {len(items)} toc entries")
    if "--png" in sys.argv:
        import pypdfium2 as pdfium
        pngdir = OUT / f"_png_{key}"
        pngdir.mkdir(exist_ok=True)
        for f in pngdir.glob("*.png"):
            f.unlink()
        pdf = pdfium.PdfDocument(str(OUT / f'{cfg["stem"]}.pdf'))
        for i in range(len(pdf)):
            pdf[i].render(scale=1.1).to_pil().save(pngdir / f"p{i+1:03d}.png")
        print("pngs in", pngdir)


if __name__ == "__main__":
    main()
