"""Tiny helpers for hand-built inline SVG diagrams (print, A4 column = 680 units)."""
import html

NAVY = "#0B1F3A"; NAVY2 = "#16335C"; ACC = "#C8813A"; ACC_L = "#FBF1E6"; OPI = "#7A3E9D"
INK = "#1B1B1F"; INK2 = "#4A4F5A"; MUTED = "#7A808C"; LINE = "#C9CED6"; WASH = "#F4F6F9"
S = ["#2A62B0", "#D9822B", "#1B9E8A", "#8E4FB8", "#C94A4A", "#6B7A8F"]
EASY = "#2E7D5B"; MED = "#B7860B"; HARD = "#B23A3A"
CONF = "#2E7D5B"; REP = "#B7860B"; INF = "#7A3E9D"
FONT = "'Source Sans 3',Arial,sans-serif"


def e(s):
    return html.escape(str(s), quote=True)


def wrap(text, width_chars):
    words = str(text).split()
    lines, cur = [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width_chars:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines or [""]


def text(x, y, s, size=11, fill=INK, anchor="start", weight=400, width=None, lh=1.25, italic=False, cls=""):
    """Multi-line text. width = max chars per line. y is the first baseline."""
    lines = wrap(s, width) if width else [str(s)]
    st = ' font-style="italic"' if italic else ""
    out = [f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" font-family="{FONT}"{st}>']
    for i, ln in enumerate(lines):
        dy = 0 if i == 0 else size * lh
        out.append(f'<tspan x="{x}" dy="{dy:.1f}">{e(ln)}</tspan>')
    out.append("</text>")
    return "".join(out), len(lines)


def box(x, y, w, h, label="", fill=WASH, stroke=LINE, tcol=INK, size=11, weight=400, rx=4, sub=None,
        subsize=9, subcol=None, dash=None, sw=1.2, align="middle", chars=None):
    """Rectangle with centred wrapped label (and optional smaller sub line)."""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>']
    chars = chars or max(6, int(w / (size * 0.52)))
    lines = wrap(label, chars) if label else []
    slines = wrap(sub, max(6, int(w / (subsize * 0.5)))) if sub else []
    total = len(lines) * size * 1.2 + (len(slines) * subsize * 1.2 + (3 if slines else 0))
    ty = y + (h - total) / 2 + size * 0.95
    tx = x + w / 2 if align == "middle" else x + 7
    anchor = "middle" if align == "middle" else "start"
    for i, ln in enumerate(lines):
        out.append(f'<text x="{tx}" y="{ty + i*size*1.2:.1f}" font-size="{size}" fill="{tcol}" text-anchor="{anchor}" font-weight="{weight}" font-family="{FONT}">{e(ln)}</text>')
    sy = ty + len(lines) * size * 1.2 + 3 - size * 0.95 + subsize * 0.95
    for i, ln in enumerate(slines):
        out.append(f'<text x="{tx}" y="{sy + i*subsize*1.2:.1f}" font-size="{subsize}" fill="{subcol or tcol}" text-anchor="{anchor}" font-family="{FONT}">{e(ln)}</text>')
    return "".join(out)


def arrow_defs(uid="a"):
    return (f'<defs><marker id="ar{uid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{INK2}"/></marker>'
            f'<marker id="aa{uid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{ACC}"/></marker></defs>')


def line(x1, y1, x2, y2, uid="a", col=INK2, sw=1.4, arrow=True, dash=None, accent=False):
    m = f' marker-end="url(#{"aa" if accent else "ar"}{uid})"' if arrow else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{sw}"{m}{d}/>'


def path(dstr, uid="a", col=INK2, sw=1.4, arrow=True, dash=None, accent=False):
    m = f' marker-end="url(#{"aa" if accent else "ar"}{uid})"' if arrow else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{dstr}" fill="none" stroke="{col}" stroke-width="{sw}"{m}{d}/>'


def svg(w, h, body, title=""):
    t = f"<title>{e(title)}</title>" if title else ""
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img">{t}{body}</svg>'


def figure(svg_str, caption, fid="", cls=""):
    i = f' id="{fid}"' if fid else ""
    c = f' class="{cls}"' if cls else ""
    return f'<figure{i}{c}>{svg_str}<figcaption><b>Figure #.</b> {caption}</figcaption></figure>'


def hbar(rows, w=680, bar_h=18, gap=8, label_w=170, val_fmt="{:,.0f}", unit="", maxv=None, colors=None,
         note=None, est=None):
    """Horizontal bar chart. rows = [(label, value, sublabel_or_None)]. est = set of labels to mark estimate."""
    est = est or set()
    maxv = maxv or max(r[1] for r in rows) * 1.12
    plot_w = w - label_w - 70
    h = len(rows) * (bar_h + gap) + 10
    out = []
    for i, r in enumerate(rows):
        lab, v = r[0], r[1]
        y = 5 + i * (bar_h + gap)
        col = (colors[i] if colors else S[0])
        bw = max(2, plot_w * v / maxv)
        out.append(text(label_w - 8, y + bar_h * 0.72, lab, 10.5, INK, "end")[0])
        dash = ' stroke="#fff" stroke-dasharray="3 2" stroke-width="1"' if lab in est else ""
        op = ' fill-opacity="0.55"' if lab in est else ""
        out.append(f'<rect x="{label_w}" y="{y}" width="{bw:.1f}" height="{bar_h}" rx="3" fill="{col}"{op}{dash}/>')
        vs = (unit if unit in ("£", "$", "€") else "") + val_fmt.format(v) + ("" if unit in ("£", "$", "€") else unit)
        if lab in est:
            vs += " (est.)"
        out.append(text(label_w + bw + 5, y + bar_h * 0.72, vs, 10, INK2)[0])
    return svg(w, h, "".join(out)), h


def tree(root, w=680, level_h=78, node_w=None, uid="t", size=10):
    """Top-down decision tree. node = dict(t=text, kind='q'|'a'|'stop', edge=label, kids=[...])."""
    # compute leaf counts
    def leaves(n):
        k = n.get("kids", [])
        return 1 if not k else sum(leaves(c) for c in k)
    total = leaves(root)
    col_w = w / total
    nw = node_w or min(170, col_w - 10)
    out = [arrow_defs(uid)]
    depth = [0]

    def place(n, x0, d):
        depth[0] = max(depth[0], d)
        k = n.get("kids", [])
        span = leaves(n) * col_w
        cx = x0 + span / 2
        y = 6 + d * level_h
        kind = n.get("kind", "q")
        fill, stroke, tc = {"q": (NAVY, NAVY, "#fff"), "a": (ACC_L, ACC, INK), "stop": ("#F9E7E7", HARD, INK),
                            "go": ("#E8F4EE", EASY, INK)}[kind]
        bh = n.get("h", max(40, len(wrap(n["t"], max(6, int(nw / (size * 0.52))))) * size * 1.2 + 14))
        out.append(box(cx - nw / 2, y, nw, bh, n["t"], fill, stroke, tc, size, 600 if kind == "q" else 400))
        xx = x0
        for c in k:
            cspan = leaves(c) * col_w
            ccx = xx + cspan / 2
            cy = 6 + (d + 1) * level_h
            out.append(line(cx, y + bh, ccx, cy - 2, uid))
            if c.get("edge"):
                mx, my = (cx + ccx) / 2, (y + bh + cy) / 2
                out.append(f'<rect x="{mx-24}" y="{my-8}" width="48" height="14" rx="7" fill="#fff" stroke="{LINE}"/>')
                out.append(text(mx, my + 3, c["edge"], 8.5, INK2, "middle", 700)[0])
            place(c, xx, d + 1)
            xx += cspan
    place(root, 0, 0)
    h = 6 + depth[0] * level_h + 64
    return svg(w, h, "".join(out))
