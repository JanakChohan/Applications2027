"""Tiny SVG helpers for the report diagrams."""
NAVY = '#14213d'; NAVY2 = '#24365f'; ACC = '#e09f3e'; ACCL = '#fbf1e1'; SIG = '#2a9d8f'; SIGL = '#e3f4f1'
RED = '#c0392b'; REDL = '#fbe9e7'; PALE = '#f4f6fa'; LINE = '#c5cbd8'; MUTE = '#5d6678'; INK = '#1d2433'; PURP = '#7a5ea8'; PURPL = '#f1edf8'

def svg(w, h, body):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="Helvetica, Arial, sans-serif">'
            '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{NAVY2}"/></marker>'
            '<marker id="arA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{ACC}"/></marker>'
            '<marker id="arS" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{SIG}"/></marker></defs>'
            f'{body}</svg>')

def text(x, y, s, size=11, color=INK, weight='normal', anchor='middle', italic=False):
    st = ' font-style="italic"' if italic else ''
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}"{st}>{s}</text>'

def box(x, y, w, h, lines, fill=PALE, stroke=NAVY2, color=INK, size=11, title=None, tcolor=None, rx=6, sw=1.2, dash=False):
    """lines: list of strings. If title given, first bold line in tcolor."""
    d = ' stroke-dasharray="5,3"' if dash else ''
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>']
    allines = ([(title, True)] if title else []) + [(l, False) for l in lines]
    lh = size * 1.3
    total = lh * len(allines)
    y0 = y + h / 2 - total / 2 + size * 0.95
    for i, (l, bold) in enumerate(allines):
        out.append(text(x + w / 2, y0 + i * lh, l, size=size + (0.5 if bold else 0),
                        color=(tcolor or color) if bold else color, weight='bold' if bold else 'normal'))
    return ''.join(out)

def arrow(x1, y1, x2, y2, color=NAVY2, label=None, lx=None, ly=None, size=9.5, marker='ar', sw=1.6, dash=False, lcolor=None, anchor='middle'):
    d = ' stroke-dasharray="5,3"' if dash else ''
    s = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" marker-end="url(#{marker})"{d}/>'
    if label:
        lx = (x1 + x2) / 2 if lx is None else lx
        ly = (y1 + y2) / 2 - 4 if ly is None else ly
        s += text(lx, ly, label, size=size, color=lcolor or color, anchor=anchor)
    return s

def path(d, color=NAVY2, sw=1.6, marker='ar', dash=False):
    ds = ' stroke-dasharray="5,3"' if dash else ''
    m = f' marker-end="url(#{marker})"' if marker else ''
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"{m}{ds}/>'

def circle(cx, cy, r, fill, stroke=None):
    st = f' stroke="{stroke}" stroke-width="1.2"' if stroke else ''
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}/>'

def fig(svgstr, caption, src):
    return f'<figure>{svgstr}<figcaption><b>{caption}</b> Source: {src}</figcaption></figure>'
