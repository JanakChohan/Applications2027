"""Helpers for assembling the Investec pack HTML."""
import re, html as _h

FIGS = []  # (num, title)

def esc(s): return _h.escape(s, quote=False)

def md(s):
    """Light inline markup: [C]/[R]/[I] confidence tags, [Sxx] source markers, **bold**."""
    s = re.sub(r'\[C\]', '<span class="c cC">Confirmed</span>', s)
    s = re.sub(r'\[R\]', '<span class="c cR">Reported</span>', s)
    s = re.sub(r'\[I\]', '<span class="c cI">Inferred</span>', s)
    s = re.sub(r'\[(S\d+(?:[,;–-]\s*S?\d+)*)\]', r'<span class="s">[\1]</span>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    return s

def P(*paras): return ''.join(f'<p>{md(p)}</p>' for p in paras)
def UL(*items): return '<ul>' + ''.join(f'<li>{md(i)}</li>' for i in items) + '</ul>'
def OL(*items): return '<ol>' + ''.join(f'<li>{md(i)}</li>' for i in items) + '</ol>'

LABELS = {'term':'Key term','say':'Say this in the interview','dont':"Don't say this",
          'op':'Your opinion goes here','unc':'Source uncertain','note':'Note'}
def box(kind, body, label=None):
    return f'<div class="box {kind}"><span class="lab">{label or LABELS[kind]}</span>{md(body)}</div>'
def term(word, defn): return box('term', f'<b>{word}</b>: {defn}')

def table(head, rows, cls=''):
    h = ''.join(f'<th>{md(c)}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{md(str(c))}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'

def fig(title, svg, source, full=False):
    n = len(FIGS) + 1; FIGS.append((n, title))
    cls = 'fig fullpage' if full else 'fig'
    return (f'<div class="{cls}" id="fig{n}"><div class="ft"><span>Figure {n}</span>{esc(title)}</div>'
            f'{svg}<div class="fs">{md(source)}</div></div>')

def part(pid, num, title, blurb):
    return (f'<section class="part"><div class="band" id="{pid}"><div class="num">{num}</div>'
            f'<h1>{esc(title)}</h1><p>{md(blurb)}</p></div>')
END = '</section>'

def h2(hid, text): return f'<h2 id="{hid}">{esc(text)}</h2>'
def h3(text): return f'<h3>{md(text)}</h3>'

def card(level, title, setup, trap, say, why, twist):
    tag = {'easy':'Easy','med':'Medium','hard':'Hard'}[level]
    return (f'<div class="card {level}"><span class="tag">{tag}</span><h4>{md(title)}</h4><dl>'
            f'<dt>Setup</dt><dd>{md(setup)}</dd><dt>Trap</dt><dd>{md(trap)}</dd>'
            f'<dt>Say</dt><dd>{md(say)}</dd><dt>Why it works</dt><dd>{md(why)}</dd>'
            f'<dt>Twist</dt><dd>{md(twist)}</dd></dl></div>')

def qa(q, tests, structure, weave, trap):
    return (f'<div class="qa"><div class="q">{md(q)}</div><div class="m"><b>Tests:</b> {md(tests)} '
            f'<b>Structure:</b> {md(structure)} <b>Weave in:</b> {md(weave)} <b>Trap:</b> {md(trap)}</div></div>')

# ---------- SVG primitives ----------
NAVY='#0b1f3a'; NAVY2='#16325c'; ACC='#d98e2b'; SIG='#7b3fa8'; GRN='#2e7d4f'; RED='#b23a3a'; TEAL='#1f7a8c'
MUT='#5b6b82'; LINE='#d6dde8'; SOFT='#f3f6fa'; ACCS='#fbf1e2'; TEALS='#e5f3f6'; GRNS='#e7f4ec'; REDS='#fbeaea'; SIGS='#f3eaf9'

def svg(w, h, body):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica,Arial,sans-serif">'
            '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{MUT}"/></marker>'
            '<marker id="arA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{ACC}"/></marker></defs>{body}</svg>')

def wrap(text, width_chars):
    words = text.split(); lines=[]; cur=''
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) <= width_chars: cur = (cur+' '+w).strip()
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def text(x, y, s, size=11, fill=NAVY, anchor='start', weight='normal', width=None, lh=None, italic=False):
    lines = wrap(s, width) if width else [s]
    lh = lh or size*1.22
    st = ' font-style="italic"' if italic else ''
    out = f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{st}>'
    for i, l in enumerate(lines):
        out += f'<tspan x="{x}" dy="{0 if i==0 else lh}">{esc(l)}</tspan>'
    return out + '</text>'

def rect(x, y, w, h, fill=SOFT, stroke=LINE, rx=6, sw=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def node(x, y, w, h, title, sub=None, fill=SOFT, stroke=NAVY2, tc=NAVY, size=11, subsize=9, subw=None):
    """Box with centred title and optional wrapped subtitle."""
    out = rect(x, y, w, h, fill, stroke)
    cx = x + w/2
    if sub:
        tl = wrap(title, int(w/(size*0.56)))
        sl = wrap(sub, subw or int(w/(subsize*0.52)))
        total = len(tl)*size*1.2 + len(sl)*subsize*1.25 + 3
        y0 = y + h/2 - total/2 + size*0.9
        for i,l in enumerate(tl): out += text(cx, y0+i*size*1.2, l, size, tc, 'middle', 'bold')
        y1 = y0 + len(tl)*size*1.2 + 2
        for i,l in enumerate(sl): out += text(cx, y1+i*subsize*1.25, l, subsize, MUT, 'middle')
    else:
        tl = wrap(title, int(w/(size*0.56)))
        y0 = y + h/2 - (len(tl)-1)*size*0.6 + size*0.35
        for i,l in enumerate(tl): out += text(cx, y0+i*size*1.2, l, size, tc, 'middle', 'bold')
    return out

def arrow(x1, y1, x2, y2, color=MUT, sw=1.6, dash=False, accent=False):
    d = ' stroke-dasharray="5,4"' if dash else ''
    m = 'arA' if accent else 'ar'
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ACC if accent else color}" stroke-width="{sw}"{d} marker-end="url(#{m})"/>'

def path(d, color=MUT, sw=1.6, dash=False, accent=False, fill='none'):
    ds = ' stroke-dasharray="5,4"' if dash else ''
    m = 'arA' if accent else 'ar'
    return f'<path d="{d}" fill="{fill}" stroke="{ACC if accent else color}" stroke-width="{sw}"{ds} marker-end="url(#{m})"/>'

def hbar(items, w=700, label_w=200, bar_h=20, gap=8, color=NAVY2, unit='', maxv=None, valfmt='{:,.0f}', title_note=None, colors=None):
    """Horizontal bar chart. items = [(label, value, note)]"""
    maxv = maxv or max(v for _, v, *_ in items)
    h = len(items)*(bar_h+gap) + 10
    body = ''
    for i, it in enumerate(items):
        lab, v = it[0], it[1]; note = it[2] if len(it) > 2 else ''
        y = 5 + i*(bar_h+gap)
        bw = (w - label_w - 120) * v / maxv
        c = colors[i] if colors else color
        body += text(label_w-8, y+bar_h*0.7, lab, 10, NAVY, 'end')
        body += f'<rect x="{label_w}" y="{y}" width="{bw:.1f}" height="{bar_h}" fill="{c}" rx="2"/>'
        body += text(label_w+bw+6, y+bar_h*0.7, valfmt.format(v)+unit+(' '+note if note else ''), 9.5, MUT)
    return svg(w, h, body)
