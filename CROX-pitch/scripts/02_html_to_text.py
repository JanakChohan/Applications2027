"""Convert downloaded SEC HTML filings to plain text (data/sec_txt/) for reading and parsing."""
import os, glob, re
from bs4 import BeautifulSoup
B = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(os.path.join(B, "sec_txt"), exist_ok=True)
for f in sorted(glob.glob(os.path.join(B, "sec", "*.htm"))):
    out = os.path.join(B, "sec_txt", os.path.basename(f)[:-4] + ".txt")
    if os.path.exists(out): continue
    soup = BeautifulSoup(open(f, "rb").read(), "lxml")
    for t in soup(["script", "style", "ix:header"]): t.decompose()
    for tr in soup.find_all("tr"):
        cells = [re.sub(r"\s+", " ", c.get_text(" ", strip=True)) for c in tr.find_all(["td", "th"])]
        cells = [c for c in cells if c not in ("", "$", ")", "%")]
        tr.replace_with(soup.new_string("\n" + " | ".join(cells) + "\n"))
    txt = soup.get_text("\n")
    txt = re.sub(r"[ \t\xa0]+", " ", txt); txt = re.sub(r"\n\s*\n+", "\n", txt)
    open(out, "w").write(txt)
print("done")
