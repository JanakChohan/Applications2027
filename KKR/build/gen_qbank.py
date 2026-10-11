#!/usr/bin/env python3
"""Build output/Question_Bank.md from the interview parts (SVGs and figures stripped)."""
import re, subprocess, pathlib
from bs4 import BeautifulSoup
ROOT = pathlib.Path(__file__).resolve().parent
def md(path, keep_ids):
    soup = BeautifulSoup(path.read_text(), "html.parser")
    for f in soup.find_all(["figure", "svg", "style"]): f.decompose()
    for d in soup.select("div.part-band"): d.decompose()
    # keep only h2 sections whose id matches keep_ids prefixes or all if None
    html = str(soup)
    out = subprocess.run(["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"], input=html, capture_output=True, text=True).stdout
    out = re.sub(r"<[^>]+>", "", out)          # leftover div tags
    out = re.sub(r"\n{3,}", "\n\n", out).replace("\\[", "[").replace("\\]", "]")
    return out.strip()
parts = [("KCS edition (from the KCS Deep Dive, Part 9)", ROOT / "parts_kcs/09_interview.html"),
         ("Whole-programme edition (from the Complete Pack, Part 9)", ROOT / "parts_main/09_interview.html")]
doc = ["# KKR London 2027 Summer Internship: Question Bank", "",
       "Prepared 12 October 2026. Scaffolds, not scripts: each question shows what it really tests, a structure, the facts to weave in and the trap. Source markers like [S71] resolve to the source table in either PDF. Confidence tags: Confirmed, Reported, Inferred.", ""]
for title, p in parts:
    doc += ["", "---", "", f"# {title}", "", md(p, None)]
(ROOT.parent / "output/Question_Bank.md").write_text("\n".join(doc) + "\n")
print("ok")
