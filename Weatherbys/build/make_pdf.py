"""Two-pass render: find section markers in pass 1, write real page numbers into the contents, re-render."""
import re, subprocess, pathlib
B = pathlib.Path(__file__).parent
OUT = B.parent
H = OUT / "Weatherbys_Private_Banking_Internship_Complete_Pack.html"
P = OUT / "Weatherbys_Private_Banking_Internship_Complete_Pack.pdf"

def render(src, dst, title=None):
    args = ["node", str(B / "render.js"), str(src), str(dst)] + ([title] if title else [])
    subprocess.run(args, check=True)

def page_map(pdf):
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, check=True).stdout
    found = {}
    for i, pg in enumerate(txt.split("\f"), 1):
        for m in re.findall(r"@@(P\w+?)@@", re.sub(r"\s+", "", pg)):
            found.setdefault(m, i)
    return found

doc = H.read_text()
render(H, P)
pm = page_map(P)
print("pass 1 markers:", pm)
for k, v in pm.items():
    doc = re.sub(rf'(<td class="pg" data-for="{k}">)[^<]*(</td>)', rf"\g<1>{v}\g<2>", doc)
H.write_text(doc)
render(H, P)
pm2 = page_map(P)
print("pass 2 markers:", pm2, "stable:", pm == pm2)
render(B / "cheat_standalone.html", OUT / "Cheat_Sheet.pdf", "Weatherbys Internship 2027: Cheat Sheet")
