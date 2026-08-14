#!/usr/bin/env python3
"""Convert a markdown file to a nicely styled PDF via chromium headless."""
import sys, subprocess, pathlib, markdown

CSS = """
@page { size: A4; margin: 20mm 18mm; }
* { box-sizing: border-box; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.6pt;
       line-height: 1.5; color: #1a1a1a; max-width: 100%; }
h1 { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 21pt;
     color: #0b1f3a; margin: 0 0 2pt; line-height: 1.15; }
h1 + h3 { font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 500;
     color: #6b7280; font-size: 11pt; margin: 0 0 6pt; }
h2 { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 14pt;
     color: #0b1f3a; margin: 20pt 0 6pt; padding-bottom: 3pt;
     border-bottom: 1.5px solid #b9932f; }
h3 { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 11.5pt;
     color: #14284a; margin: 13pt 0 4pt; }
p { margin: 0 0 7pt; }
ul, ol { margin: 0 0 8pt; padding-left: 20px; }
li { margin: 0 0 3pt; }
strong { color: #0b1f3a; }
hr { border: none; border-top: 1px solid #d8d8d8; margin: 14pt 0; }
blockquote { margin: 8pt 0; padding: 6pt 12pt; background: #f6f7f9;
     border-left: 3px solid #b9932f; color: #33383f; }
blockquote p { margin: 0 0 4pt; }
code { background: #eef0f3; padding: 1px 4px; border-radius: 3px;
     font-family: 'SFMono-Regular', Consolas, monospace; font-size: 9pt; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 9.6pt; }
th, td { border: 1px solid #cfd4da; padding: 5px 8px; text-align: left;
     vertical-align: top; }
th { background: #0b1f3a; color: #fff; font-family: Arial, sans-serif; }
tr:nth-child(even) td { background: #f6f7f9; }
h2, h3 { page-break-after: avoid; }
blockquote, table, li { page-break-inside: avoid; }
"""

def convert(md_path):
    md_path = pathlib.Path(md_path).resolve()
    text = md_path.read_text()
    html_body = markdown.markdown(text, extensions=["extra", "sane_lists", "tables"])
    html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{html_body}</body></html>"
    html_path = md_path.with_suffix(".html")
    html_path.write_text(html)
    pdf_path = md_path.with_suffix(".pdf")
    subprocess.run([
        "/opt/pw-browsers/chromium",
        "--headless", "--no-sandbox", "--disable-gpu",
        f"--print-to-pdf={pdf_path}", "--no-pdf-header-footer",
        html_path.as_uri(),
    ], check=True, capture_output=True)
    print(f"wrote {pdf_path}")

if __name__ == "__main__":
    for a in sys.argv[1:]:
        convert(a)
