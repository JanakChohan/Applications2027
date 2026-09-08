"""Tiny SVG helper for consistent flow diagrams."""
import html, textwrap

NAVY="#0b2545"; NAVY2="#13315c"; GOLD="#b08d57"; GOLD2="#e9dcc3"; GREY="#5b6573"; LINE="#9aa5b5"; BG="#f4f6f9"; GREEN="#2e7d5b"; RED="#a63d40"; BLUE="#2f6fb2"; LBLUE="#dbe7f5"; WHITE="#fff"

class D:
    def __init__(self, w, h, font="Liberation Sans, Arial, sans-serif"):
        self.w=w; self.h=h; self.font=font; self.parts=[]
        self.parts.append(f'<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L8,3 z" fill="{GREY}"/></marker>'
                          f'<marker id="arrn" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L8,3 z" fill="{NAVY}"/></marker>'
                          f'<marker id="arrg" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L8,3 z" fill="{GOLD}"/></marker></defs>')
    def text(self, x, y, s, size=11, fill="#1c2330", anchor="middle", weight="normal", italic=False, maxw=None, lh=1.25):
        lines=[s] if maxw is None else self._wrap(s, size, maxw)
        out=[]
        for i,l in enumerate(lines):
            dy = i*size*lh
            it = ' font-style="italic"' if italic else ''
            out.append(f'<text x="{x}" y="{y+dy}" font-family="{self.font}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{it}>{html.escape(l)}</text>')
        self.parts.append("".join(out)); return len(lines)
    def _wrap(self, s, size, maxw, bold=False):
        k = 0.62 if bold else 0.54
        if s.isupper(): k += 0.06
        cpl=max(6,int(maxw/(size*k)))
        out=[]
        for para in s.split("\n"):
            out+=textwrap.wrap(para, cpl) or [""]
        return out
    def box(self, x, y, w, h, title, body=None, fill=NAVY, stroke=None, tfill=WHITE, bfill=WHITE, tsize=11.5, bsize=9, r=6, dash=False, tweight="bold"):
        st = f' stroke="{stroke}" stroke-width="1.4"' if stroke else ''
        if dash: st += ' stroke-dasharray="5,4"'
        if fill in (WHITE, BG, LBLUE) and bfill == WHITE: bfill = GREY
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{st}/>')
        tl = self._wrap(title, tsize, w-14, bold=(tweight=="bold"))
        bl = self._wrap(body, bsize, w-14) if body else []
        total = len(tl)*tsize*1.2 + (len(bl)*bsize*1.25 + 4 if bl else 0)
        y0 = y + h/2 - total/2 + tsize*0.9
        self.text(x+w/2, y0, "\n".join(tl), size=tsize, fill=tfill, weight=tweight, maxw=w-14, lh=1.2)
        if bl:
            self.text(x+w/2, y0 + len(tl)*tsize*1.2 + 4, "\n".join(bl), size=bsize, fill=bfill, maxw=w-14)
    def arrow(self, x1,y1,x2,y2, color=GREY, width=1.6, label=None, lsize=8.5, dash=False, marker="arr", curve=None, loff=(0,-5)):
        st = f' stroke-dasharray="4,3"' if dash else ''
        if curve:
            cx,cy=curve
            self.parts.append(f'<path d="M{x1},{y1} Q{cx},{cy} {x2},{y2}" fill="none" stroke="{color}" stroke-width="{width}" marker-end="url(#{marker})"{st}/>')
            mx,my=(x1+2*cx+x2)/4,(y1+2*cy+y2)/4
        else:
            self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" marker-end="url(#{marker})"{st}/>')
            mx,my=(x1+x2)/2,(y1+y2)/2
        if label:
            self.text(mx+loff[0], my+loff[1], label, size=lsize, fill=GREY, italic=True)
    def line(self, x1,y1,x2,y2,color=LINE,width=1.2,dash=False):
        st = f' stroke-dasharray="4,3"' if dash else ''
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{st}/>')
    def poly(self, pts, color=GREY, width=1.6, marker="arr", dash=False):
        st = f' stroke-dasharray="4,3"' if dash else ''
        d="M"+" L".join(f"{x},{y}" for x,y in pts)
        self.parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" marker-end="url(#{marker})"{st}/>')
    def region(self, x,y,w,h,label,fill=BG,stroke=LINE,lsize=9.5,lfill=GREY, dash=True):
        st=f' stroke-dasharray="6,4"' if dash else ''
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.2"{st}/>')
        self.text(x+10, y+lsize+6, label, size=lsize, fill=lfill, anchor="start", weight="bold")
    def circle(self, cx,cy,r,fill=GOLD,stroke=None):
        st=f' stroke="{stroke}" stroke-width="1.5"' if stroke else ''
        self.parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}/>')
    def svg(self):
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}">'+"".join(self.parts)+'</svg>'

def fig(svg, cap, n=None):
    lab = f"<b>Figure {n}.</b> " if n else ""
    return f'<div class="fig">{svg}<div class="cap">{lab}{cap}</div></div>'
