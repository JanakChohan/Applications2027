"""Build crocs-risk-catalyst-guide-easy-read.pdf: a dyslexia-friendly, diagram-led study guide to the pitch,
focused on risks, mitigants and catalysts. One idea per page; terminology is introduced level by level.
Design follows British Dyslexia Association style advice: sans-serif face (Lexend, SIL OFL), 12.5pt+, generous letter,
word and line spacing, left-aligned short lines, cream background, bold (never italics/underline/all-caps) for emphasis.
Numbers come from data/derived/facts.json (same source as the deck and memo)."""
import json, os, math, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); D = os.path.join(ROOT, "data", "derived")
F = json.load(open(os.path.join(D, "facts.json"))); RR = json.load(open(os.path.join(D, "rar_rows.json"))); ST = json.load(open(os.path.join(D, "study_stats.json")))
V = F["valuation"]; K = F["key"]; R = F["rar"]; B = F["scen"]["Base"]; SN = F["sens"]; Q = F["quarters"]; INS = F["insider"]; fy = lambda y: F[f"fy{y}"]
price = F["price"]; bear, base, bull, wtd = V["pt"]; rb, rba, rbu, rw = [v * 100 for v in V["ret"]]; e27 = V["eps27"][1]; exbb = e27 + SN["No buybacks at all in FY27 (cash retained)"][0]
tar = abs(SN["+1 pt US tariff rate on imports"][0]); impl = K["Market-implied probability of the bear case (base:bull 2:1)"] * 100
RED, TEAL, BLUE, VIO, ORG, NAVY, INK, MUTE, GREY, CREAM = "#c5362f", "#0e9f8e", "#2a78d6", "#7c5cd6", "#c46a00", "#1F3864", "#22262b", "#565b61", "#b9bdc2", "#FBF6E9"
CSS = """
@font-face { font-family: 'Lexend'; font-weight: 400; src: url('assets/fonts/lexend-latin-400-normal.woff2') format('woff2'); }
@font-face { font-family: 'Lexend'; font-weight: 600; src: url('assets/fonts/lexend-latin-600-normal.woff2') format('woff2'); }
@font-face { font-family: 'Lexend'; font-weight: 700; src: url('assets/fonts/lexend-latin-700-normal.woff2') format('woff2'); }
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #FBF6E9; }
body { font-family: 'Lexend', 'Verdana', 'DejaVu Sans', Arial, sans-serif; font-size: 13.5pt; line-height: 1.6; letter-spacing: 0.012em; word-spacing: 0.09em; color: #22262b; text-align: left; }
.pg { width: 210mm; height: 297mm; padding: 15mm 17mm 14mm; position: relative; overflow: hidden; break-after: page; background: #FBF6E9; }
.foot { position: absolute; left: 17mm; right: 17mm; bottom: 7mm; font-size: 8.5pt; color: #565b61; display: flex; justify-content: space-between; }
.lvl { display: inline-block; font-size: 10.5pt; font-weight: 600; padding: 2pt 9pt; border-radius: 10pt; color: #fff; margin-bottom: 6pt; }
h1 { font-size: 23pt; line-height: 1.25; margin: 0 0 8pt; color: #1F3864; font-weight: 700; max-width: 165mm; }
h2 { font-size: 15pt; line-height: 1.3; margin: 12pt 0 4pt; color: #1F3864; font-weight: 700; }
p { margin: 0 0 7pt; max-width: 150mm; }
ul { margin: 0 0 6pt; padding-left: 16pt; max-width: 152mm; } li { margin-bottom: 4pt; }
b, strong { font-weight: 700; }
.bl { background: #1F3864; color: #fff; border-radius: 7pt; padding: 9pt 13pt; margin: 9pt 0 10pt; font-weight: 600; font-size: 13.5pt; }
.bl span { display: block; font-size: 10pt; font-weight: 600; opacity: 0.85; margin-bottom: 1pt; }
.card { border-radius: 7pt; padding: 8pt 11pt 5pt; margin: 7pt 0; border-left: 5pt solid; }
.card .t { display: block; font-size: 10.5pt; font-weight: 700; margin-bottom: 2pt; }
.card p { margin-bottom: 4pt; max-width: none; } .card ul { max-width: none; margin-bottom: 2pt; }
.risk { background: #fbe7e4; border-color: #c5362f; } .risk .t { color: #9f271f; }
.mit { background: #e0f3ef; border-color: #0e9f8e; } .mit .t { color: #0a6b60; }
.cat { background: #e3edfa; border-color: #2a78d6; } .cat .t { color: #1b56a0; }
.term { background: #ece6fa; border-color: #7c5cd6; } .term .t { color: #5a3eb5; }
.say { background: #fcecd2; border-color: #c46a00; } .say .t { color: #8a4a00; } .say p { margin-bottom: 6pt; }
.note { background: #f1ecdd; border-color: #8b9096; } .note .t { color: #4a4f55; }
.word { font-size: 16pt; font-weight: 700; color: #1F3864; display: block; margin-bottom: 1pt; }
.kv { display: grid; grid-template-columns: 24mm 1fr; gap: 1pt 6pt; margin-top: 3pt; font-size: 12.5pt; } .kv div:nth-child(odd) { font-weight: 700; color: #5a3eb5; }
.badge { display: inline-block; font-size: 9.6pt; font-weight: 700; padding: 0 6pt; border-radius: 4pt; vertical-align: 1pt; white-space: nowrap; }
.fact { border: 1.4pt solid #22262b; color: #22262b; } .assume { border: 1.4pt dashed #8a4a00; color: #8a4a00; }
.cols2 { display: grid; grid-template-columns: 1fr 1fr; gap: 9pt; } .cols3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8pt; }
.flow { display: flex; align-items: stretch; gap: 0; margin: 8pt 0; } .flow .box { flex: 1; background: #fff; border: 1.4pt solid #b9bdc2; border-radius: 7pt; padding: 7pt 8pt; text-align: left; font-size: 12.5pt; line-height: 1.45; }
.flow .box b.big { display: block; font-size: 17pt; color: #1F3864; line-height: 1.2; } .flow .arr { flex: 0 0 9mm; display: flex; align-items: center; justify-content: center; font-size: 17pt; color: #1F3864; font-weight: 700; }
.tile { background: #fff; border: 1.4pt solid #b9bdc2; border-radius: 7pt; padding: 7pt 9pt; } .tile .n { font-size: 19pt; font-weight: 700; color: #1F3864; line-height: 1.2; display: block; } .tile .l { font-size: 11.6pt; line-height: 1.4; display: block; }
.hb { display: grid; grid-template-columns: 58mm 1fr; gap: 5pt 7pt; align-items: center; margin: 6pt 0; font-size: 12.5pt; } .hb .bar { height: 15pt; border-radius: 3pt; display: inline-block; vertical-align: middle; } .hb .v { font-weight: 700; margin-left: 6pt; }
.steps { list-style: none; padding: 0; margin: 6pt 0; counter-reset: s; max-width: none; } .steps li { counter-increment: s; position: relative; padding: 2pt 0 2pt 30pt; margin-bottom: 5pt; }
.steps li::before { content: counter(s); position: absolute; left: 0; top: 1pt; width: 21pt; height: 21pt; border-radius: 50%; background: #1F3864; color: #fff; font-weight: 700; font-size: 11pt; text-align: center; line-height: 21pt; }
table { border-collapse: collapse; width: 100%; font-size: 12.5pt; margin: 6pt 0; } th { text-align: left; background: #1F3864; color: #fff; padding: 5pt 8pt; font-weight: 600; } td { padding: 6pt 8pt; border-bottom: 1pt solid #d9d3c0; vertical-align: top; }
svg text { font-family: 'Lexend', 'DejaVu Sans', sans-serif; letter-spacing: 0.01em; }
.center { text-align: center; } .big { font-size: 30pt; font-weight: 700; color: #1F3864; line-height: 1.15; }
.script p { font-size: 13.5pt; margin-bottom: 7pt; max-width: none; }
.q { font-weight: 700; color: #1F3864; margin: 0 0 2pt; } .a { margin: 0 0 4pt; }
.small { font-size: 11pt; color: #565b61; }
"""
LV = {0: ("Start here", NAVY), 1: ("Level 1 · The business", TEAL), 2: ("Level 2 · Money words", VIO), 3: ("Level 3 · Why we say buy", BLUE), 4: ("Level 4 · Risks and mitigants", RED), 5: ("Level 5 · Catalysts", BLUE), 6: ("Level 6 · Say it out loud", ORG)}
PAGES = []
def page(level, title, body):
    n = len(PAGES) + 1; name, col = LV[level]
    PAGES.append(f'<section class="pg"><span class="lvl" style="background:{col}">{name}</span><h1>{title}</h1>{body}<div class="foot"><span>Crocs (CROX): risks, mitigants and catalysts · easy-read guide · data as of 25 Nov 2026</span><span>{n}</span></div></section>')
def bl(text): return f'<div class="bl"><span>Bottom line</span>{text}</div>'
def card(kind, tag, body): return f'<div class="card {kind}"><span class="t">{tag}</span>{body}</div>'
def term(word, plain, crocs, use, careful=None, extra=""):
    kv = f'<div>Means</div><div>{plain}</div><div>Crocs</div><div>{crocs}</div><div>Use it</div><div>"{use}"</div>' + (f'<div>Careful</div><div>{careful}</div>' if careful else "")
    return f'<div class="card term"><span class="t">New word</span><span class="word">{word}</span>{extra}<div class="kv">{kv}</div></div>'
FACT = '<span class="badge fact">Fact</span>'; ASSUME = '<span class="badge assume">Our assumption</span>'
def svg(w, h, body, width="100%"): return f'<svg viewBox="0 0 {w} {h}" width="{width}" role="img" style="display:block;margin:6pt auto">{body}</svg>'
def tx(x, y, s, size=15, weight=400, fill=INK, anchor="start"): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'
def pie_path(cx, cy, r, a0, a1):
    x0, y0 = cx + r * math.sin(a0), cy - r * math.cos(a0); x1, y1 = cx + r * math.sin(a1), cy - r * math.cos(a1); large = 1 if (a1 - a0) > math.pi else 0
    return f"M{cx},{cy} L{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f} Z"
def pizza(cx, cy, r, n):
    out = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f6dfa8" stroke="{INK}" stroke-width="2"/>' + f'<path d="{pie_path(cx, cy, r, 0, 2*math.pi/n)}" fill="{BLUE}" stroke="{INK}" stroke-width="2"/>'
    for i in range(n):
        a = 2 * math.pi * i / n; out += f'<line x1="{cx}" y1="{cy}" x2="{cx + r*math.sin(a):.1f}" y2="{cy - r*math.cos(a):.1f}" stroke="{INK}" stroke-width="2"/>'
    return out
def pie(cx, cy, r, pct, col):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{GREY}" stroke-width="2"/><path d="{pie_path(cx, cy, r, 0, 2*math.pi*pct/100)}" fill="{col}"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="2"/>'
def hbars(rows, maxv, col, fmt="${:,.0f}m", lab_w="58mm"):
    out = f'<div class="hb" style="grid-template-columns:{lab_w} 1fr">'
    for lab, v in rows: out += f'<div>{lab}</div><div><span class="bar" style="width:{max(2, v/maxv*68):.1f}%;background:{col}"></span><span class="v">{fmt.format(v)}</span></div>'
    return out + "</div>"
def flow(boxes, seps=None):
    out = '<div class="flow">'
    for i, b in enumerate(boxes):
        if i: out += f'<div class="arr">{(seps[i-1] if seps else "&#8594;")}</div>'
        out += f'<div class="box">{b}</div>'
    return out + "</div>"
def tile(n, l): return f'<div class="tile"><span class="n">{n}</span><span class="l">{l}</span></div>'

# =============================================== COVER ===============================================
stairs = "".join(f'<rect x="{20+i*105}" y="{250-i*38}" width="105" height="{40+i*38}" rx="5" fill="{c}" opacity="0.9"/>' + tx(72 + i*105, 240 - i*38, str(i + 1), 22, 700, INK, "middle") + tx(72 + i*105, 276 - 0, t1, 11.5, 700, "#fff", "middle") + tx(72 + i*105, 291, t2, 11.5, 700, "#fff", "middle")
                 for i, (c, t1, t2) in enumerate([(TEAL, "The", "business"), (VIO, "Money", "words"), (BLUE, "Why we", "say buy"), (RED, "Risks and", "mitigants"), (BLUE, "Catalysts", ""), (ORG, "Say it", "out loud")]))
PAGES.append(f'''<section class="pg"><div style="margin-top:38mm"><span class="lvl" style="background:{NAVY}">Easy-read study guide</span>
<div class="big" style="font-size:38pt;margin-top:6pt">Crocs (CROX)</div><div class="big" style="font-size:24pt;margin-top:4pt">Risks, mitigants and catalysts</div>
<p style="font-size:14pt;margin-top:12pt;max-width:140mm">One idea per page. Picture first, words second. Start simple, then build up the proper terms.</p>
{svg(660, 310, stairs)}
<p class="small" style="max-width:150mm;margin-top:6pt">Six levels. Each one builds on the last. Numbers are as of 25 November 2026, when the share price was ${price:.2f}.</p></div>
<div class="foot"><span>Crocs (CROX): risks, mitigants and catalysts · easy-read guide · data as of 25 Nov 2026</span><span>1</span></div></section>''')
# =============================================== START HERE ===============================================
page(0, "How this guide works", f'''
<ul><li><b>One idea per page.</b> Look at the picture first.</li><li><b>Short sentences.</b> Key words are in bold.</li><li><b>New words</b> come one at a time, with how to use them.</li><li><b>Say each page out loud</b> before you move on.</li></ul>
<h2>The colour code</h2>
<div class="cols2">{card("risk", "Risk", "<p>Something that could go wrong.</p>")}{card("mit", "Mitigant", "<p>Something that makes a risk smaller.</p>")}{card("cat", "Catalyst", "<p>An event that could move the share price.</p>")}{card("term", "New word", "<p>A term to learn and use.</p>")}</div>
{card("say", "Say it", "<p>Words you can use out loud. Change them to sound like you.</p>")}
<h2>Fact or assumption?</h2>
<p>Every number has one of two labels.</p>
<p>{FACT} &nbsp;It comes from Crocs' own reports or market data.</p>
<p>{ASSUME} &nbsp;It is our judgement. Say <b>"we assume"</b> or <b>"we estimate"</b>.</p>
{bl("Knowing which numbers are assumptions is what makes you sound credible.")}''')
page(0, "The bottom line", f'''
<div class="center" style="margin:4pt 0 0"><div class="big">We say: buy Crocs.</div></div>
{svg(660, 150, f'<rect x="40" y="35" width="230" height="90" rx="10" fill="#fff" stroke="{GREY}" stroke-width="2"/>' + tx(155, 68, "Share price today", 15, 400, INK, "middle") + tx(155, 106, f"${price:.0f}", 34, 700, NAVY, "middle")
   + f'<path d="M290 80 H360" stroke="{NAVY}" stroke-width="5"/><path d="M360 66 L386 80 L360 94 Z" fill="{NAVY}"/>' + f'<rect x="400" y="35" width="230" height="90" rx="10" fill="{NAVY}"/>' + tx(515, 68, "What we think it is worth", 15, 400, "#fff", "middle") + tx(515, 106, f"${base:,.0f}", 34, 700, "#fff", "middle")
   + tx(335, 58, f"{rba:+.0f}%", 17, 700, NAVY, "middle"))}
<p class="center" style="max-width:none">by December 2027 &nbsp;{ASSUME}</p>
<h2>Three sentences</h2>
<ul><li><b>Why buy?</b> Crocs makes a lot of spare cash. It uses the cash to shrink its number of shares.</li><li><b>Why is it cheap?</b> People fear the clog is a <b>fad</b> that is ending.</li><li><b>Your job:</b> explain the fear, what softens it, and when we find out.</li></ul>
{bl("The stock is cheap because of one fear. Your section is about that fear.")}''')
page(0, "Your section on one page", f'''
<p>Your part has three pieces. They answer three questions.</p>
<div class="cols3" style="margin-top:8pt">
{card("risk", "1. Risks", "<p><b>What could go wrong?</b></p><ul><li>The clog is a fad</li><li>Profit quality is weak</li><li>Bosses are selling shares</li></ul>")}
{card("mit", "2. Mitigants", "<p><b>What softens it?</b></p><ul><li>Over half of sales are now outside North America</li><li>The cash is real</li><li>We have sell rules</li></ul>")}
{card("cat", "3. Catalysts", "<p><b>When do we find out?</b></p><ul><li>About 11 Feb 2027: first forecast for 2027</li><li>Late Oct 2027: clean North America number</li></ul>")}</div>
{svg(660, 70, f'<path d="M110 35 H550" stroke="{NAVY}" stroke-width="4"/><path d="M550 22 L576 35 L550 48 Z" fill="{NAVY}"/>' + tx(110, 20, "the argument", 14, 600, INK, "start") + tx(330, 20, "why we are not too worried", 14, 600, INK, "middle") + tx(560, 20, "the test dates", 14, 600, INK, "end"))}
{bl("Risks say what the argument is. Mitigants say why we can live with it. Catalysts say when it gets settled.")}''')
# =============================================== LEVEL 1 ===============================================
ttm_na, ttm_in, ttm_hd = F["ttm_na"], F["ttm_intl"], F["ttm_hd"]; tot = ttm_na + ttm_in + ttm_hd; w1, w2, w3 = [v / tot * 600 for v in (ttm_na, ttm_in, ttm_hd)]
blocks = (f'<rect x="30" y="50" width="{w1-6:.0f}" height="110" rx="8" fill="{BLUE}"/>' + f'<rect x="{30+w1:.0f}" y="50" width="{w2-6:.0f}" height="110" rx="8" fill="{TEAL}"/>' + f'<rect x="{30+w1+w2:.0f}" y="50" width="{w3-6:.0f}" height="110" rx="8" fill="{ORG}"/>'
          + tx(30 + w1/2, 92, "Crocs brand", 14, 600, "#fff", "middle") + tx(30 + w1/2, 112, "North America", 14, 600, "#fff", "middle") + tx(30 + w1/2, 142, f"${ttm_na/1000:.1f}bn", 20, 700, "#fff", "middle")
          + tx(30 + w1 + w2/2, 92, "Crocs brand", 14, 600, "#fff", "middle") + tx(30 + w1 + w2/2, 112, "International", 14, 600, "#fff", "middle") + tx(30 + w1 + w2/2, 142, f"${ttm_in/1000:.1f}bn", 20, 700, "#fff", "middle")
          + tx(30 + w1 + w2 + w3/2, 102, "HEYDUDE", 13, 600, "#fff", "middle") + tx(30 + w1 + w2 + w3/2, 138, f"${ttm_hd/1000:.1f}bn", 18, 700, "#fff", "middle")
          + tx(30 + w1/2, 190, "Shrinking: -2%", 15, 700, INK, "middle") + tx(30 + w1 + w2/2, 190, "Growing: +12%", 15, 700, INK, "middle") + tx(30 + w1 + w2 + w3/2, 190, "Small: +6%", 15, 700, INK, "middle")
          + tx(30, 30, "Sales in the last 12 months (growth is the latest quarter)", 13.5, 400, MUTE))
page(1, "What Crocs sells", f'''
<p>Crocs makes the foam clog with holes in it. It also owns a second brand, <b>HEYDUDE</b>.</p>
{svg(660, 205, blocks)}
<ul><li>About <b>129 million pairs</b> of Crocs a year. {FACT}</li><li><b>Clogs are 74%</b> of the Crocs brand. {FACT}</li><li>Crocs does <b>not</b> own factories. Other companies make the shoes, mostly in Vietnam and China.</li><li>Half is sold in its own stores and websites. Half is sold to other shops.</li></ul>
{bl("Two engines. North America is slowing. International is growing. Remember these three blocks.")}''')
page(1, "Where the money goes on one $25 pair", f'''
<p>A pair of Crocs sells for about <b>$25</b> on average. Here is roughly where that goes.</p>
{svg(660, 170, f'<rect x="30" y="40" width="252" height="80" rx="8" fill="{GREY}"/><rect x="286" y="40" width="216" height="80" rx="8" fill="#8b9096"/><rect x="506" y="40" width="124" height="80" rx="8" fill="{TEAL}"/>'
   + tx(156, 75, "Make and ship it", 14, 600, INK, "middle") + tx(156, 102, "$10.50", 20, 700, INK, "middle") + tx(394, 75, "Run the business", 14, 600, "#fff", "middle") + tx(394, 102, "$9.00", 20, 700, "#fff", "middle") + tx(568, 75, "Profit", 14, 600, "#fff", "middle") + tx(568, 102, "$5.50", 20, 700, "#fff", "middle")
   + tx(30, 150, "Run the business = shops, staff, adverts, head office", 13.5, 400, MUTE))}
<p class="small">Rounded from 2025: 58% is left after making the shoe, and 22% after all running costs. {FACT}</p>
{bl("Crocs keeps about 22 cents of profit from every $1 of sales.")}
{card("note", "Why this matters for you", "<p>Some of those costs do <b>not</b> shrink when sales fall. That is the key to the risk section. You will see it again in Level 4.</p>")}''')
# =============================================== LEVEL 2 ===============================================
page(2, "Revenue and operating profit", f'''
<p>Start with the two most basic words.</p>
{term("Revenue", "Money coming in from selling shoes. Also called <b>sales</b>.", f"${fy(2025)['revenue']/1000:.2f}bn in 2025 {FACT}", "Revenue was roughly flat in 2025.", "Revenue is <b>not</b> profit.")}
{term("Operating profit", "What is left after <b>all</b> the running costs. Also called <b>EBIT</b>.", f"About ${fy(2025)['adj_op_income']:,.0f}m in 2025 {FACT}", "Operating profit is lower than it was in 2023.", "This is the profit of the <b>whole business</b>, before interest and tax.")}
{svg(660, 120, f'<rect x="30" y="30" width="600" height="46" rx="6" fill="{GREY}"/><rect x="496" y="30" width="134" height="46" rx="6" fill="{TEAL}"/>' + tx(263, 60, "Costs", 16, 600, INK, "middle") + tx(563, 60, "Profit", 16, 600, "#fff", "middle")
   + f'<path d="M30 92 H630" stroke="{INK}" stroke-width="2"/><path d="M30 86 V98 M630 86 V98" stroke="{INK}" stroke-width="2"/>' + tx(330, 114, "Revenue = the whole bar", 14.5, 600, INK, "middle"))}
{bl("Revenue is the whole bar. Operating profit is the green end of it.")}''')
page(2, "Margin and basis points", f'''
{term("Margin", "Profit as a share of revenue. It is a <b>percentage</b>.", f"Operating margin: 28% in 2023, 22% in 2025 {FACT}", "Operating margin fell from 28% to 22%.", "A margin is a %, never dollars.")}
{svg(660, 130, "".join(f'<rect x="{x}" y="34" width="250" height="40" rx="6" fill="{GREY}"/><rect x="{x}" y="34" width="{w}" height="40" rx="6" fill="{TEAL}"/>' + tx(x, 24, lab, 14.5, 600) + tx(x + w + 8, 61, pc, 16, 700) for x, w, lab, pc in [(40, 69, "2023: of every $1 of sales", "28c profit"), (360, 56, "2025: of every $1 of sales", "22c profit")])
   + tx(40, 108, "Gross margin = after making the shoe only (58%).", 13.5, 400, MUTE) + tx(40, 126, "Operating margin = after all running costs (22%).", 13.5, 400, MUTE))}
{term("Basis point (bps)", "One hundredth of 1%. So <b>100 basis points = 1 percentage point</b>.", "Margin rose 150 basis points last quarter (1.5 points)", "Margin was up 150 basis points on last year.", "For margin changes say <b>points</b> or <b>basis points</b>, not &quot;percent&quot;.")}
{bl("Margin tells you how much of each dollar is kept. Basis points measure small changes in it.")}''')
page(2, "Shares and EPS", f'''
{term("Share", "One small piece of ownership of the company.", f"About 46 million shares exist {FACT}", "The share count is falling.", None)}
{term("EPS (earnings per share)", "Profit <b>divided by</b> the number of shares.", f"${fy(2025)['adj_eps']:.2f} in 2025. About $14.55 expected for 2026 {FACT}", "EPS should grow about 16% this year.", "EPS can rise even when profit does not, if the share count falls.")}
{svg(660, 130, f'<rect x="40" y="30" width="170" height="64" rx="8" fill="{TEAL}"/>' + tx(125, 58, "Profit after tax", 14, 600, "#fff", "middle") + tx(125, 82, "about $708m", 16, 700, "#fff", "middle") + tx(240, 72, "÷", 30, 700, NAVY, "middle")
   + f'<rect x="270" y="30" width="170" height="64" rx="8" fill="{VIO}"/>' + tx(355, 58, "Shares (year average)", 13, 600, "#fff", "middle") + tx(355, 82, "about 48.7m", 16, 700, "#fff", "middle") + tx(470, 72, "=", 30, 700, NAVY, "middle")
   + f'<rect x="500" y="30" width="130" height="64" rx="8" fill="{NAVY}"/>' + tx(565, 58, "EPS", 14, 600, "#fff", "middle") + tx(565, 82, "about $14.54", 16, 700, "#fff", "middle") + tx(40, 120, "2026, our estimate, in line with Crocs' own forecast", 13, 400, MUTE))}
{bl("EPS is the number the stock market watches most. Two things move it: profit and share count.")}''')
page(2, "The P/E multiple", f'''
{term("P/E multiple", "Share price <b>divided by</b> EPS. How many years of profit you pay for one share.", f"${price:.0f} ÷ $16 = about <b>10 times</b> {FACT}", "Crocs trades on 10 times earnings.", "Low P/E means cheap. But cheap can also mean risky.")}
{svg(660, 150, f'<rect x="210" y="26" width="{10*20}" height="36" rx="6" fill="{BLUE}"/><rect x="210" y="82" width="{18.3*20:.0f}" height="36" rx="6" fill="{GREY}"/>' + tx(200, 50, "Crocs", 15, 600, INK, "end") + tx(200, 106, "Average big US company", 15, 600, INK, "end")
   + tx(210 + 200 + 8, 51, "10 times", 16, 700) + tx(210 + 366 + 8, 107, "18 times", 16, 700) + tx(210, 142, "P/E on next year's expected profit", 13, 400, MUTE))}
<h2>Two more words that go with it</h2>
<ul><li><b>Re-rating:</b> the P/E goes <b>up</b>. Investors pay more for the same profit.</li><li><b>De-rating:</b> the P/E goes <b>down</b>.</li></ul>
<p>Crocs was on about <b>6 times</b> in March 2026. It is on 10 times now. That was a re-rating.</p>
{bl("A share price is just EPS times the P/E. If either one falls, the price falls.")}''')
# =============================================== LEVEL 3 ===============================================
page(3, "Free cash flow and buybacks", f'''
{term("Free cash flow (FCF)", "Cash left over after running the business and investing in it.", f"${F['ttm_fcf']:,.0f}m in the last 12 months {FACT}", "Crocs has a free cash flow yield of about 10%.", "<b>FCF yield</b> = free cash flow ÷ the value of all the shares.")}
{term("Buyback", "The company buys its own shares and cancels them.", f"About 10% of its shares a year {FACT}", "Buybacks are shrinking the share count by about 10% a year.", None)}
{svg(660, 215, pizza(170, 105, 80, 10) + pizza(490, 105, 80, 9) + f'<path d="M285 105 H360" stroke="{NAVY}" stroke-width="5"/><path d="M360 92 L384 105 L360 118 Z" fill="{NAVY}"/>' + tx(330, 86, "buy back", 14, 600, INK, "middle") + tx(330, 138, "1 slice", 14, 600, INK, "middle")
   + tx(170, 208, "10 slices. Yours = 10%", 15, 700, INK, "middle") + tx(490, 208, "9 slices. Yours = 11%", 15, 700, INK, "middle"))}
{bl("The pizza is the same size. There are fewer slices. So each slice is bigger.")}''')
page(3, "The engine: slow sales, fast EPS", f'''
<p>This is the whole reason for the buy call. {ASSUME}</p>
{flow([f'<b class="big">+4%</b>Sales grow slowly each year', f'<b class="big">+5%</b>Profit grows a little faster', f'<b class="big">-8%</b>Shares fall each year from buybacks', f'<b class="big">+15%</b>EPS grows fast'])}
<p>Small growth in profit, spread over fewer shares, becomes big growth in <b>EPS</b>.</p>
<h2>But the stock is cheap</h2>
{flow(['<b class="big">10x</b>Crocs P/E', '<b class="big">18x</b>Average company P/E', '<b class="big">Why?</b>Investors fear the clog is a <b>fad</b>'])}
{bl("Good engine, low price. The gap is one fear. Level 4 is about that fear, and it is your section.")}''')
steps = [("12 Feb", 13.12), ("30 Apr", 13.48), ("30 Jul", 13.85), ("29 Oct", 14.55)]
gsvg = "".join(f'<rect x="{60+i*150}" y="{150-(v-12.5)*52:.0f}" width="110" height="{(v-12.5)*52:.0f}" rx="5" fill="{BLUE}"/>' + tx(115 + i*150, 150 - (v-12.5)*52 - 8, f"${v:.2f}", 16, 700, INK, "middle") + tx(115 + i*150, 172, d, 14, 600, INK, "middle") for i, (d, v) in enumerate(steps)) + f'<path d="M40 150 H640" stroke="{INK}" stroke-width="1.5"/>' + tx(40, 20, "Crocs' own forecast for 2026 EPS (middle of the range), by date given", 13.5, 400, MUTE)
page(3, "Guidance, consensus, beat and raise", f'''
<div class="cols2">{term("Guidance", "The company's <b>own</b> forecast.", "2026 EPS of $14.45 to $14.65 " + FACT, "Crocs raised guidance three times this year.")}{term("Consensus", "The <b>average</b> forecast of the professional analysts.", "2027 EPS of $16.01 " + FACT, "We are above consensus for 2027.")}</div>
<ul><li><b>Beat:</b> the result is <b>better</b> than expected.</li><li><b>Miss:</b> the result is <b>worse</b> than expected.</li><li><b>Raise:</b> the company lifts its guidance.</li></ul>
{svg(660, 185, gsvg)}
{bl("Crocs has done &quot;beat and raise&quot; all year. The share price doubled.")}''')
# =============================================== LEVEL 4 ===============================================
page(4, "What a risk section has to do", f'''
<p>A weak risk section is a long list. A strong one answers <b>five questions</b>.</p>
<ol class="steps"><li><b>What is the risk?</b> Say it simply.</li><li><b>How bad could it be?</b> Put a number on it.</li><li><b>How likely is it?</b> Give a view.</li><li><b>What softens it?</b> These are the mitigants.</li><li><b>What would make us sell?</b> These are the kill rules.</li></ol>
<h2>Four words to use</h2>
<div class="cols2">{card("term", "New word", '<span class="word">Risk</span><p>Something that could make our call wrong.</p>')}{card("term", "New word", '<span class="word">Downside</span><p>How much we could lose if it goes wrong.</p>')}
{card("term", "New word", '<span class="word">Mitigant</span><p>Something that makes a risk <b>smaller</b> or <b>less likely</b>. It does not remove it.</p>')}{card("term", "New word", '<span class="word">Kill criteria</span><p>Rules set in advance for when we would sell. Also called kill rules.</p>')}</div>
{bl("Name it, size it, give the odds, show what softens it, say when you would walk away.")}''')
dots = [(1, "The clog is a fad", 395, 70, RED), (2, "Weak profit quality", 330, 150, RED), (3, "Bosses selling shares", 300, 215, RED), (4, "Stock market falls", 250, 130, GREY), (5, "Tariffs go up", 215, 240, GREY), (6, "HEYDUDE slips again", 150, 225, GREY)]
msvg = (f'<rect x="80" y="30" width="400" height="260" fill="#fff" stroke="{GREY}" stroke-width="1.5"/><rect x="280" y="30" width="200" height="130" fill="#fbe7e4"/><path d="M280 30 V290 M80 160 H480" stroke="{GREY}" stroke-width="1.5" stroke-dasharray="5 5"/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="17" fill="{c}" stroke="#fff" stroke-width="2"/>' + tx(x, y + 6, str(n), 17, 700, "#fff" if c == RED else INK, "middle") for n, _, x, y, c in dots)
        + tx(280, 318, "How likely?", 17, 700, INK, "middle") + tx(85, 318, "less", 15, 400, MUTE) + tx(475, 318, "more", 15, 400, MUTE, "end") + f'<text x="58" y="160" font-size="17" font-weight="700" fill="{INK}" text-anchor="middle" transform="rotate(-90 58 160)">How bad?</text>'
        + tx(385, 52, "Focus here", 15.5, 700, "#9f271f", "middle"))
mleg = "".join(f'<div style="display:flex;gap:7pt;align-items:center;margin-bottom:7pt"><span style="flex:0 0 20pt;width:20pt;height:20pt;border-radius:50%;background:{c};color:{"#fff" if c == RED else INK};font-weight:700;font-size:11.5pt;text-align:center;line-height:20pt">{n}</span><span style="font-weight:{700 if c == RED else 400}">{lab}</span></div>' for n, lab, _, _, c in dots)
page(4, "The risk map", f'''
<p>Not all risks are equal. Rank them by <b>how bad</b> and <b>how likely</b>. {ASSUME}</p>
<div style="display:grid;grid-template-columns:62% 1fr;gap:6pt;align-items:center">{svg(500, 330, msvg)}<div>{mleg}</div></div>
<ul><li><b>Red dots</b> are your three main risks. Present these.</li><li><b>Grey dots</b> are smaller. Know them in case you are asked.</li></ul>
{bl("Spend most of your time on risk 1. It is the reason the stock is cheap.")}''')
page(4, "Risk 1: the clog is a fad", f'''
<p>A <b>fad</b> is a product that is hot, then suddenly not. If clogs cool off, Crocs has little else: clogs are 74% of the brand.</p>
<div class="cols2">
{card("risk", "The worry (what a bear says)", f"<ul><li>North America sales fell <b>7%</b> in 2025 and are still down <b>2%</b></li><li>US teens ranked Crocs <b>6th</b> in 2023 and <b>10th</b> in 2026</li><li>Copies are <b>legal</b>. Crocs lost in court in January 2026</li><li>It happened before: sales fell <b>24%</b> in 2007 to 2009</li></ul>")}
{card("mit", "The other side (what a bull says)", f"<ul><li>Crocs <b>chose</b> to cut discounts in May 2025</li><li>Its own stores and sites in North America still grew about <b>2%</b></li><li>International grew <b>12%</b> and is over <b>half</b> the brand</li><li>Pairs sold still rose <b>1.5%</b> in 2025</li></ul>")}</div>
<p class="small">All eight points are facts from Crocs' reports, a court ruling and a published teen survey. {FACT}</p>
<div class="cols2">{card("term", "New word", '<span class="word">Bear</span><p>Someone who thinks the shares will fall.</p>')}{card("term", "New word", '<span class="word">Bull</span><p>Someone who thinks the shares will rise.</p>')}</div>
{bl("Both sides are using real data. The debate is about which half of the business matters more.")}''')
qs = list(Q.keys())[-4:]; na = [Q[q]["crocs_na_yoy_pct"] for q in qs]; it = [Q[q]["crocs_intl_yoy_pct"] for q in qs]; qlab = ["Oct-Dec 2025", "Jan-Mar 2026", "Apr-Jun 2026", "Jul-Sep 2026"]; y0 = 150; sc = 7.2
gb = f'<path d="M50 {y0} H640" stroke="{INK}" stroke-width="2"/>' + tx(44, y0 + 5, "0%", 13, 400, MUTE, "end")
for i in range(4):
    x = 80 + i * 145
    for j, (v, c) in enumerate(((na[i], BLUE), (it[i], TEAL))):
        h = abs(v) * sc; yy = y0 - h if v >= 0 else y0; gb += f'<rect x="{x + j*54}" y="{yy:.0f}" width="48" height="{max(h, 2):.0f}" rx="4" fill="{c}"/>' + tx(x + j*54 + 24, (yy - 7) if v >= 0 else (yy + h + 18), f"{v:+.0f}%", 15, 700, INK, "middle")
    gb += tx(x + 51, 236, qlab[i], 13, 600, INK, "middle")
gb += f'<rect x="60" y="6" width="18" height="18" rx="3" fill="{BLUE}"/>' + tx(84, 21, "North America", 14.5, 600) + f'<rect x="230" y="6" width="18" height="18" rx="3" fill="{TEAL}"/>' + tx(254, 21, "International", 14.5, 600)
page(4, "Risk 1 in one picture", f'''
<p>Crocs brand sales growth compared with the same three months a year earlier. {FACT}</p>
{svg(660, 245, gb)}
<ul><li><b>Blue (North America):</b> at or below zero.</li><li><b>Green (International):</b> always above zero.</li></ul>
{card("say", "Say it", "<p>&quot;North America is still shrinking, down 2% last quarter. But international is growing 12% and is now more than half of the Crocs brand.&quot;</p>")}
{bl("The bear points at the blue bars. The bull points at the green bars.")}''')
waffle = "".join(f'<rect x="{20 + (i % 10) * 25}" y="{10 + (i // 10) * 25}" width="21" height="21" rx="3" fill="{RED if i < 16 else GREY}"/>' for i in range(100)) + tx(290, 60, "16 of every 100", 20, 700, NAVY) + tx(290, 88, "dollars of sales", 20, 700, NAVY) + tx(290, 122, f"= ${R['at_risk']:,.0f} million", 17, 600) + tx(290, 148, "would be lost if the fad ends", 15, 400) + tx(290, 190, "This is called", 14, 400, MUTE) + tx(290, 212, "revenue at risk", 17, 700, "#5a3eb5")
page(4, "Putting a number on the fad risk", f'''
<p>&quot;It might be a fad&quot; is an opinion. We turned it into a number in four steps.</p>
<ol class="steps"><li><b>Split</b> Crocs' sales into nine parts. {FACT}</li><li><b>Score</b> each part from 1 (safe) to 5 (very exposed). {ASSUME}</li><li><b>Convert</b> each score to a sales fall. Score 5 means a 30% fall. {ASSUME}</li><li><b>Add it up.</b></li></ol>
{svg(660, 265, waffle)}
<p class="small">Why 30% for the top score? It is close to what really happened: Crocs fell 24% in 2007 to 2009, and HEYDUDE fell 25% in 2023 to 2025. {FACT}</p>
{bl(f"About 16% of sales is at risk. That is ${R['at_risk']:,.0f} million.")}''')
g = {r["line"]: r for r in RR}; grp = [("North America clogs", g["Crocs NA - clogs, wholesale"]["revenue_at_risk_usd_m"] + g["Crocs NA - clogs, DTC"]["revenue_at_risk_usd_m"]), ("International clogs (not China)", g["Crocs Intl ex-China - clogs"]["revenue_at_risk_usd_m"]),
     ("HEYDUDE", g["HEYDUDE - wholesale"]["revenue_at_risk_usd_m"] + g["HEYDUDE - DTC"]["revenue_at_risk_usd_m"]), ("North America charms", g["Crocs NA - Jibbitz & other"]["revenue_at_risk_usd_m"]), ("China", g["Crocs Intl - China"]["revenue_at_risk_usd_m"]),
     ("Sandals and other", g["Crocs NA - sandals"]["revenue_at_risk_usd_m"] + g["Crocs Intl ex-China - sandals, Jibbitz, other"]["revenue_at_risk_usd_m"])]
r0 = g["Crocs NA - clogs, wholesale"]
page(4, "Where the risk sits", f'''
<p>Sales at risk, by part of the business. {ASSUME}</p>
{hbars(grp, max(v for _, v in grp), RED, lab_w="66mm")}
<p>Almost half of it is <b>North America clogs</b>.</p>
{card("note", "Worked example", f"<p>North America clogs sold to other shops bring in <b>${r0['ttm_revenue_usd_m']:,.0f}m</b> a year.</p><p>We scored it <b>5</b>. That means a <b>30%</b> fall.</p><p>30% of ${r0['ttm_revenue_usd_m']:,.0f}m = <b>${r0['revenue_at_risk_usd_m']:,.0f}m</b> at risk.</p>")}
{card("say", "If someone says &quot;you made the scores up&quot;", f"<p>&quot;The scores are our judgement, so we tested them. Move every score one notch and the answer is between {R['minus1_pct']*100:.0f}% and {R['plus1_pct']*100:.0f}% of sales. The conclusion does not change.&quot;</p>")}
{bl("The risk is concentrated. It is mostly one product in one region.")}''')
def stack(x, parts, scale, label, total):
    y = 290; out = ""
    for h, c, t1, tc in parts:
        hh = h * scale; y -= hh; out += f'<rect x="{x}" y="{y:.0f}" width="190" height="{hh - 3:.0f}" rx="5" fill="{c}"/>' + (tx(x + 95, y + hh/2 + 4, t1, 15, 700, tc, "middle") if t1 else "")
    return out + tx(x + 95, y - 10, total, 16, 700, INK, "middle") + tx(x + 95, 314, label, 15.5, 600, INK, "middle")
cof = stack(60, [(400, GREY, "Beans, milk, cups $400", INK), (400, "#8b9096", "Rent and wages $400", "#fff"), (200, TEAL, "Profit $200", "#fff")], 0.25, "A normal day", "Sales $1,000") + stack(300, [(320, GREY, "Beans, milk, cups $320", INK), (400, "#8b9096", "Rent and wages $400", "#fff"), (80, TEAL, "", "#fff")], 0.25, "A slow day", "Sales $800") \
      + tx(502, 104, "Profit $80", 15.5, 700, INK) + tx(502, 170, "Sales down 20%", 16.5, 700, "#9f271f") + tx(502, 200, "Profit down 60%", 16.5, 700, "#9f271f")
page(4, "Why profit falls faster than sales", f'''
<p>Think of a coffee shop.</p>
{svg(660, 322, cof)}
<p>The rent and wages <b>did not shrink</b>. So profit took most of the hit.</p>
<div class="cols2">{card("term", "New word", '<span class="word">Fixed costs</span><p>Costs that stay the same when sales fall. Rent, salaries, IT.</p>')}{card("term", "New word", '<span class="word">Operating leverage</span><p>When profit moves <b>more</b> than sales, because of fixed costs.</p>')}</div>
{bl("Fixed costs make a small fall in sales into a big fall in profit.")}''')
def shr(y, lab, a, b, fa, fb, pct, mx):
    return (tx(30, y + 16, lab, 15, 700) + f'<rect x="190" y="{y}" width="{a/mx*300:.0f}" height="22" rx="4" fill="{GREY}"/>' + tx(190 + a/mx*300 + 8, y + 17, fa, 14.5, 600) + f'<rect x="190" y="{y+28}" width="{b/mx*300:.0f}" height="22" rx="4" fill="{RED}"/>' + tx(190 + b/mx*300 + 8, y + 45, fb, 14.5, 700)
            + tx(630, y + 32, pct, 19, 700, "#9f271f", "end"))
st = (tx(190, 16, "Grey = today.  Red = if the fad ends.", 13.5, 400, MUTE) + shr(30, "Sales", ST["rev0"], ST["rev1"], f"${ST['rev0']/1000:.1f}bn", f"${ST['rev1']/1000:.1f}bn", f"-{R['at_risk_pct']*100:.0f}%", ST["rev0"])
      + shr(100, "Operating profit", ST["ebit0"], ST["ebit1"], f"${ST['ebit0']:,.0f}m", f"${ST['ebit1']:,.0f}m", f"{(ST['ebit1']/ST['ebit0']-1)*100:.0f}%", ST["ebit0"]) + shr(170, "EPS", R["eps0"], R["eps1"], f"${R['eps0']:.2f}", f"${R['eps1']:.2f}", f"{(R['eps1']/R['eps0']-1)*100:.0f}%", R["eps0"]))
page(4, "The stress test for Crocs", f'''
{card("term", "New word", '<span class="word">Stress test</span><p>Asking &quot;what if the bad thing happens?&quot; and running the numbers.</p>')}
{svg(660, 235, st)}
<p>We assume about <b>${ST['fixed']/1000:.1f} billion</b> of Crocs' costs are fixed. {ASSUME}</p>
<h2>What would a share be worth then?</h2>
{flow([f'<b class="big">${R["eps1"]:.2f}</b>EPS in the stress test', '<b class="big">7</b>P/E in bad times', f'<b class="big">about ${R["val"]:.0f}</b>a share'], seps=["×", "="])}
<p class="small">Why 7 times? In past bad periods Crocs traded at about 7 times profit. {ASSUME}</p>
{bl(f"If the fad fully ends, EPS roughly halves and a share could be worth about ${R['val']:.0f}. That is the worst case.")}''')
sc3 = ""
for i, (lab, v, pr, c, ch) in enumerate([("Bull case", bull, "25% chance", TEAL, rbu), ("Base case", base, "50% chance", BLUE, rba), ("Bear case", bear, "25% chance", RED, rb)]):
    y = 26 + i * 58; sc3 += tx(118, y + 26, lab, 15, 700, INK, "end") + f'<rect x="130" y="{y}" width="{v*1.45:.0f}" height="40" rx="5" fill="{c}"/>' + tx(140, y + 26, pr, 13.5, 600, "#fff") + tx(130 + v*1.45 + 8, y + 26, f"${v:,.0f} ({ch:+.0f}%)", 16, 700)
sc3 += f'<path d="M{130+price*1.45:.0f} 12 V200" stroke="{INK}" stroke-width="2" stroke-dasharray="6 5"/>' + tx(130 + price*1.45, 218, f"Today ${price:.0f}", 14, 700, INK, "middle")
page(4, "How likely? Three scenarios", f'''
{card("term", "New words", '<span class="word">Bear case, base case, bull case</span><p>Three versions of the future: <b>bad</b>, <b>expected</b>, <b>good</b>. Each gets a share price and a chance.</p>')}
{svg(660, 226, sc3)}
<p>Share price in December 2027. {ASSUME}</p>
<h2>The weighted average</h2>
{flow([f'<b class="big">25%</b>of ${bear:,.0f}', f'<b class="big">50%</b>of ${base:,.0f}', f'<b class="big">25%</b>of ${bull:,.0f}', f'<b class="big">${wtd:,.0f}</b>in total'], seps=["+", "+", "="])}
{card("term", "New word", f'<span class="word">Probability-weighted value</span><p>Each price times its chance, added up. Also called <b>expected value</b>. Ours is ${wtd:,.0f}, which is {rw:+.0f}%.</p>')}
{bl(f"Bear ${bear:,.0f}. Base ${base:,.0f}. Bull ${bull:,.0f}. Weighted average ${wtd:,.0f}.")}''')
page(4, "Being honest about the bet", f'''
<h2 style="margin-top:0">1. The loss is bigger than the gain</h2>
{svg(660, 112, tx(160, 34, "Base case gain", 15, 600, INK, "end") + f'<rect x="170" y="14" width="{rba*5:.0f}" height="30" rx="5" fill="{BLUE}"/>' + tx(170 + rba*5 + 8, 35, f"{rba:+.0f}%", 17, 700) + tx(160, 84, "Bear case loss", 15, 600, INK, "end") + f'<rect x="170" y="64" width="{abs(rb)*5:.0f}" height="30" rx="5" fill="{RED}"/>' + tx(170 + abs(rb)*5 + 8, 85, f"{rb:+.0f}%", 17, 700))}
<p>So this is <b>not</b> &quot;small downside, big upside&quot;. The bet works only because the bear case is <b>less likely</b>.</p>
<h2>2. What is the market assuming?</h2>
{svg(660, 150, pie(170, 70, 55, 25, RED) + pie(470, 70, 55, impl, RED) + tx(170, 145, "We think: 25% chance", 15.5, 700, INK, "middle") + tx(470, 145, f"Share price implies: about {impl:.0f}%", 15.5, 700, INK, "middle") + tx(320, 75, "vs", 18, 700, NAVY, "middle"))}
<p>Chance of the bear case. {ASSUME}</p>
{card("term", "New word", '<span class="word">Priced in</span><p>Already reflected in the share price. A lot of fear is priced in to Crocs.</p>')}
{card("say", "Say it", f"<p>&quot;The market is pricing in about a {impl:.0f}% chance that the clog trend unwinds. We think it is closer to one in four. That gap is our edge, and it is a modest one.&quot;</p>")}''')
page(4, "Risk 2: weak profit quality", f'''
<p>EPS is going <b>up</b>. But the profit of the whole business has gone <b>down</b>.</p>
{svg(660, 150, "".join(f'<rect x="{40+i*210}" y="20" width="180" height="100" rx="9" fill="{c}"/>' + tx(130 + i*210, 52, a, 14.5, 600, "#fff", "middle") + tx(130 + i*210, 92, b_, 30, 700, "#fff", "middle")
   for i, (a, b_, c) in enumerate([("Operating profit", f"{(B['ebit']['FY2026E']/fy(2023)['adj_op_income']-1)*100:.0f}%", RED), ("Number of shares", f"{(B['sh_avg']['FY2026E']/fy(2023)['sh_diluted']-1)*100:.0f}%", VIO), ("EPS", f"{(B['eps']['FY2026E']/fy(2023)['adj_eps']-1)*100:+.0f}%", TEAL)])) + tx(40, 142, "Change from 2023 to 2026 (2026 is expected)", 13.5, 400, MUTE))}
<p>The pizza got a bit smaller. But so many slices were removed that each slice still grew.</p>
<div class="cols2">{card("term", "New word", '<span class="word">Earnings quality</span><p>Is profit growth coming from a healthier business, or from something else?</p>')}{card("term", "New word", '<span class="word">Adjusted</span><p>Profit with one-off items left out. The official version is called <b>reported</b> or <b>GAAP</b>.</p>')}</div>
{card("mit", "Mitigant", f"<p>The cash is real. Free cash flow was <b>${F['ttm_fcf']:,.0f}m</b>, more than adjusted profit. And margin rose <b>150 basis points</b> last quarter. {FACT}</p>")}
{bl("EPS growth since 2023 is all buybacks. That is fine only if the business stops shrinking.")}''')
page(4, "Risk 3: bosses selling, bosses changing", f'''
<p>Shares sold and bought by Crocs' own directors and managers, last 12 months. {FACT}</p>
{hbars([("Sold", INS["sales_12m_usd"]/1e6), ("of which the CEO", INS["ceo_sales_usd"]/1e6), ("Bought", INS["buys_12m_usd"]/1e6)], INS["sales_12m_usd"]/1e6, RED, fmt="${:,.1f}m", lab_w="48mm")}
<div class="cols3">{card("term", "New word", '<span class="word">Insider</span><p>A director or top manager of the company.</p>')}{card("term", "New word", '<span class="word">Form 4</span><p>The public form insiders file when they trade.</p>')}{card("term", "New word", '<span class="word">10b5-1 plan</span><p>A selling schedule fixed in advance. Less worrying.</p>')}</div>
{card("risk", "Careful with your wording", "<p>Say: <b>&quot;The forms do not show a pre-arranged plan.&quot;</b></p><p>Do not say: &quot;There was no plan.&quot; One could exist without being marked.</p>")}
<ul><li><b>Three finance chiefs</b> in 16 months. {FACT}</li><li>HEYDUDE is on its <b>fourth boss</b> in four years. {FACT}</li></ul>
{card("mit", "Mitigant", f"<p>The CEO still owns about <b>${INS['ceo_shares_after']*price/1e6:.0f}m</b> of shares. He sold about 13% after the price doubled. {FACT}</p>")}''')
def mini(t, a, b_): return f'<div class="tile"><span class="l"><b>{t}</b></span><span class="l">{a}</span><span class="l" style="color:#565b61">{b_}</span></div>'
page(4, "The smaller risks", f'''
<p>You do not need to present these. Be ready if someone asks.</p>
<div class="cols2" style="gap:8pt">
{mini("Tariffs", "A tax on imported shoes. Now 10% to 12.5%.", f"Each extra point costs about {tar*100:.0f} cents of EPS. Small.")}
{mini("Factories", "45% of Crocs are made in Vietnam. Two makers produce 73%.", "A problem there would hurt supply.")}
{mini("HEYDUDE", "The second brand could shrink again.", "It is only 17% of sales now.")}
{mini("Stock market fall", "Crocs shares swing more than the market.", "2022: Crocs -42%, market -25%.")}
{mini("Price already up", "The shares doubled in a year.", "A short-term dip is more likely.")}
{mini("One big customer?", "Checked. No customer is even 10% of sales.", "Not a risk. Say you checked.")}</div>
<p class="small" style="margin-top:6pt">All of these are facts from Crocs' reports and market data, except the tariff cost per point, which is our estimate.</p>
{bl("Six smaller risks. None of them decides the investment. Risk 1 does.")}''')
def pair(r_, m_): return f'<div class="flow" style="margin:5pt 0"><div class="box" style="background:#fbe7e4;border-color:{RED};flex:0 0 36%"><b>{r_}</b></div><div class="arr">&#8594;</div><div class="box" style="background:#e0f3ef;border-color:{TEAL}">{m_}</div></div>'
page(4, "The mitigants", f'''
<p>For each risk, name what softens it. <b>Risk on the left, mitigant on the right.</b> {FACT}</p>
{pair("The clog is a fad", f"International is <b>{F['intl_share_ttm']:.0f}%</b> of the brand and growing <b>12%</b>. Sandals are growing too.")}
{pair("Weak profit quality", f"Cash is real: <b>${F['ttm_fcf']:,.0f}m</b> of free cash flow. Margin turned up last quarter.")}
{pair("Bosses selling shares", f"The CEO still holds about <b>${INS['ceo_shares_after']*price/1e6:.0f}m</b>. Bonuses depend on margin and cash flow.")}
{pair("Governance and supply chain", "MSCI gives Crocs an <b>AA</b> rating for ESG, the second-highest grade.")}
{pair("Tariffs", "Already cut from about 19% to 10 to 12.5%. Factories are spread over five countries.")}
{pair("Debt", f"Low: about <b>{F['nd_ebitda']:.1f} times</b> a year's profit. Nothing is due in the next 12 months.")}
{card("say", "Say it", "<p>&quot;The main mitigant to the fad risk is that more than half the brand's sales are now outside North America, and that half is growing at 12%.&quot;</p>")}
{bl("A mitigant does not remove a risk. It makes it smaller. Always pair them up.")}''')
def rule(t, m): return f'<div class="flow" style="margin:5pt 0"><div class="box" style="flex:0 0 58%"><b>If</b> {t}</div><div class="arr">&#8594;</div><div class="box" style="background:#fbe7e4;border-color:{RED}"><b>{m}</b></div></div>'
page(4, "Our kill criteria", f'''
<p>Rules we set <b>now</b>, while calm, for when we would sell. {ASSUME}</p>
{rule("North America direct sales are negative two quarters in a row", "Sell. The fad risk is real.")}
{rule("International growth is below 5% two quarters in a row", "Sell. The offset has stopped.")}
{rule("Crocs guides 2027 operating margin below 21.5%", "Sell. Profit is still slipping.")}
{rule("Crocs makes a big acquisition, over $500m", "Sell. The cash is not going to buybacks.")}
{rule("The CEO sells another 10% of his shares", "Cut the position.")}
{card("say", "Say it", "<p>&quot;We have written down what would prove us wrong. If North America direct sales turn negative for two quarters, we sell.&quot;</p>")}
{bl("Kill criteria turn &quot;we think it is fine&quot; into &quot;here is exactly what would change our mind&quot;.")}''')
# =============================================== LEVEL 5 ===============================================
page(5, "What a catalyst is", f'''
{card("term", "New word", '<span class="word">Catalyst</span><p>A specific upcoming <b>event</b> that could change what investors think the company is worth.</p>')}
{flow(['<b class="big">Event</b>What happens', '<b class="big">Date</b>When it happens', '<b class="big">Reason</b>Why the price would move'])}
<p>A good catalyst has all three.</p>
<h2>Why you need them</h2>
<p>A cheap stock can stay cheap for years. &quot;It is undervalued&quot; is not enough. You need a reason why other investors will change their mind, and when.</p>
<div class="cols2">{card("cat", "Hard catalyst", "<p>Has a <b>date</b>. Example: results in February.</p>")}{card("cat", "Soft catalyst", "<p>No fixed date. Example: a court ruling.</p>")}</div>
{bl("Catalysts are the test dates for your risks. Each one brings new evidence.")}''')
er = F["earn"]; eb = f'<path d="M40 110 H640" stroke="{INK}" stroke-width="2"/>'
for i, e in enumerate(er):
    v = e["day_move_pct"]; h = abs(v) * 2.6; x = 55 + i * 74; yy = 110 - h if v > 0 else 110
    eb += f'<rect x="{x}" y="{yy:.0f}" width="52" height="{h:.0f}" rx="4" fill="{TEAL if v > 0 else RED}"/>' + tx(x + 26, (yy - 7) if v > 0 else (yy + h + 18), f"{v:+.0f}%", 15, 700, INK, "middle")
eb += tx(40, 222, "Share price move on each of the last eight results days. Oldest on the left.", 13.5, 400, MUTE)
page(5, "Shares move on surprises", f'''
<p>A share price already includes what investors <b>expect</b>. It moves when the news is <b>different</b> from that.</p>
{flow(['<b class="big">Good news</b>but less good than expected', '<b class="big">Price falls</b>because investors hoped for more'])}
{svg(660, 230, eb)}
<ul><li>Crocs <b>beat</b> profit forecasts on all eight days. {FACT}</li><li>The shares still <b>fell on three</b> of them. {FACT}</li><li>The average move on a results day is <b>{F['earn_avg_abs_move']:.0f}%</b>, up or down. {FACT}</li></ul>
{bl("What the company says about the future matters more than the quarter just finished.")}''')
bw = lambda v: (v - 14) * 150
page(5, "A quirk: forecasts leave out buybacks", f'''
<p>When Crocs gives <b>guidance</b> for EPS, it assumes it will buy back <b>no</b> shares. Then it buys back hundreds of millions. Most analysts copy this.</p>
<p>So forecasts are built low. This is why ours is higher.</p>
{svg(660, 200, tx(30, 20, "EPS expected for 2027", 13.5, 400, MUTE) + "".join(tx(250, 58 + i*56, lab, 14.5, 600, INK, "end") + f'<rect x="262" y="{36+i*56}" width="{bw(v):.0f}" height="34" rx="5" fill="{c}"/>' + tx(262 + bw(v) + 8, 59 + i*56, f"${v:.2f}", 17, 700)
   for i, (lab, v, c) in enumerate([("Analysts (consensus)", 16.01, GREY), ("Ours, with no 2027 buybacks", exbb, "#7fb0ea"), ("Ours, with buybacks", e27, BLUE)])))}
<p>Top bar: {FACT} &nbsp; Bottom two bars: {ASSUME}</p>
{card("say", "Say it", f"<p>&quot;Guidance and consensus leave out buybacks. That is why we are about {V['vs_cons'][1]*100:.0f}% above consensus for 2027.&quot;</p>")}
{bl("Every buyback is a small positive surprise that is not in anyone's forecast.")}''')
def tl():
    x = lambda m: 58 + m * 41.5; o = f'<path d="M40 140 H640" stroke="{INK}" stroke-width="3"/>' + f'<rect x="{x(0)}" y="147" width="{x(8.2)-x(0):.0f}" height="26" rx="5" fill="#fcecd2" stroke="{ORG}" stroke-width="1.5"/>' + tx(x(4.1), 165, "The fog: North America looks worse than it is", 13, 600, "#8a4a00", "middle")
    for m, l1, l2, key, up in [(0.15, "1 Dec 2026", "Investor event", False, True), (2.5, "About 11 Feb", "2027 forecast", True, True), (5.1, "Late Apr", "Results", False, True), (8.1, "Late Jul", "Results", False, True), (11.0, "Late Oct", "The fog lifts", True, True), (13.2, "Dec 2027", "Our target", False, True)]:
        c = BLUE if key else "#8b9096"; hgt = 88 if key else 46
        o += f'<path d="M{x(m):.0f} 140 V{140-hgt}" stroke="{c}" stroke-width="{3 if key else 2}"/><circle cx="{x(m):.0f}" cy="140" r="{10 if key else 7}" fill="{c}" stroke="#fff" stroke-width="2"/>' + tx(x(m), 140 - hgt - 26, l1, 15 if key else 13.5, 700, INK, "middle") + tx(x(m), 140 - hgt - 8, l2, 15 if key else 13.5, 700 if key else 400, INK, "middle")
    o += f'<path d="M{x(0)} 205 H{x(13.1)}" stroke="{TEAL}" stroke-width="9" stroke-linecap="round" opacity="0.6"/>' + tx(x(6.5), 232, "All year: buybacks of about $600m. Any time: the tariff court case.", 13.5, 600, "#0a6b60", "middle")
    return o
page(5, "The calendar", f'''
<p>The next 13 months. The two <b>blue</b> dates matter most.</p>
{svg(660, 245, tl())}
<h2>Also on the list</h2>
<ul><li><b>1 December 2026.</b> Crocs speaks at an investor event. First hint on Christmas trading.</li><li><b>All year.</b> Buybacks. $1.7bn is approved, about {1700/F['mcap']*100:.0f}% of the company. {FACT}</li><li><b>Any time.</b> A court case could remove the tariffs, or they could rise.</li><li><b>About October 2027.</b> The teen survey. Crocs is 10th.</li></ul>
<p class="small">Results dates are estimates until Crocs confirms them. Say &quot;around&quot;.</p>
{bl("Two dates decide it: about 11 February and late October 2027.")}''')
def outcome(good, bad): return f'<div class="cols2">{card("mit", "Good outcome", good)}{card("risk", "Bad outcome", bad)}</div>'
page(5, "Key date 1: about 11 February 2027", f'''
{card("cat", "What happens", "<p>Crocs reports October to December results. It also gives its <b>first guidance for 2027</b>.</p>")}
<h2>The numbers to know</h2>
<div class="cols3">{tile("$3.40", "Consensus EPS for the quarter " + FACT)}{tile("$16.01", "Consensus EPS for 2027 " + FACT)}{tile(f"${exbb:.2f}", "Our 2027 EPS with no buybacks " + ASSUME)}</div>
<h2>What we want to see</h2>
{outcome("<p>2027 EPS guidance of <b>$16 or more</b>.</p><p>Margin guidance of <b>22.5% or more</b>.</p>", "<p>2027 EPS guidance below about <b>$15.50</b>.</p><p>Margin guidance below <b>21.5%</b>. That is a kill rule.</p>")}
<p>We put the chance of a good outcome at about <b>60%</b>. {ASSUME}</p>
{bl("This date tests two risks at once: did Christmas hold up, and is profit still slipping?")}''')
lem = (tx(165, 22, "Before", 16, 700, INK, "middle") + tx(495, 22, "After", 16, 700, INK, "middle") + f'<rect x="30" y="36" width="270" height="150" rx="9" fill="#fff" stroke="{GREY}" stroke-width="1.5"/><rect x="360" y="36" width="270" height="150" rx="9" fill="#fff" stroke="{GREY}" stroke-width="1.5"/>'
       + tx(165, 66, "You sell 10 cups", 15, 600, INK, "middle") + tx(165, 88, "at your own stall for $2", 15, 600, INK, "middle") + tx(165, 128, "Own-stall sales: $20", 16, 700, "#0a6b60", "middle") + tx(165, 152, "Sales to shops: $0", 15, 400, INK, "middle")
       + tx(495, 66, "A shop sells the 10 cups.", 15, 600, INK, "middle") + tx(495, 88, "You sell them to it for $1", 15, 600, INK, "middle") + tx(495, 128, "Own-stall sales: $0", 16, 700, "#9f271f", "middle") + tx(495, 152, "Sales to shops: $10", 15, 400, INK, "middle")
       + f'<path d="M308 110 H340" stroke="{NAVY}" stroke-width="4"/><path d="M340 100 L356 110 L340 120 Z" fill="{NAVY}"/>' + tx(330, 212, "Same 10 cups. Nothing got worse. The sales moved to a different column.", 14, 600, INK, "middle"))
page(5, "The fog, explained", f'''
<p>For a year, one number looks worse than it really is. Here is why, using a lemonade stall.</p>
{svg(660, 222, lem)}
<h2>What happened at Crocs</h2>
<ul><li>In summer 2026, one big online marketplace changed how it buys from Crocs.</li><li>Those sales moved from <b>direct</b> to <b>wholesale</b>, at a lower price.</li><li>So North America <b>direct</b> sales look <b>7 to 8 points worse</b> than they are, each quarter. {FACT}</li><li>This lasts until a full year has passed: <b>late October 2027</b>.</li></ul>
<div class="cols2">{card("term", "New word", '<span class="word">Direct (DTC)</span><p>Sold in Crocs&#39; own stores and websites.</p>')}{card("term", "New word", '<span class="word">Wholesale</span><p>Sold to other shops, who sell it on.</p>')}</div>
{bl("Until October 2027, nobody outside Crocs can see the true North America trend.")}''')
page(5, "Key date 2: late October 2027", f'''
{card("cat", "What happens", "<p>Crocs reports July to September 2027 results. The fog drops out. We get the <b>first clean look</b> at North America.</p>")}
{svg(660, 120, f'<rect x="40" y="20" width="250" height="70" rx="9" fill="#fcecd2" stroke="{ORG}" stroke-width="1.5"/>' + tx(165, 50, "Now to mid-2027", 15, 700, INK, "middle") + tx(165, 74, "Number is distorted", 14.5, 400, INK, "middle") + f'<path d="M300 55 H350" stroke="{NAVY}" stroke-width="4"/><path d="M350 44 L370 55 L350 66 Z" fill="{NAVY}"/>'
   + f'<rect x="380" y="20" width="250" height="70" rx="9" fill="#e3edfa" stroke="{BLUE}" stroke-width="1.5"/>' + tx(505, 50, "Late October 2027", 15, 700, INK, "middle") + tx(505, 74, "Number is clean", 14.5, 400, INK, "middle"))}
<h2>What we want to see</h2>
{outcome("<p>North America direct sales are <b>growing</b>.</p><p>The fad fear fades.</p>", "<p>They are <b>shrinking</b>, with no excuse left.</p><p>Two quarters of that is a kill rule.</p>")}
<p>We put the chance of a good outcome at about <b>55%</b>. {ASSUME}</p>
{bl("This is the date that settles the fad debate. It is the most important catalyst for risk 1.")}''')
def link(r_, d_, g_, b_): return f"<tr><td><b>{r_}</b></td><td>{d_}</td><td>{g_}</td><td>{b_}</td></tr>"
page(5, "Every risk has a test date", f'''
<p>This table joins your two halves together. Learn it.</p>
<table><thead><tr><th style="width:24%">Risk</th><th style="width:24%">When we learn more</th><th style="width:26%">Good sign</th><th style="width:26%">Bad sign</th></tr></thead><tbody>
{link("The clog is a fad", "Feb 2027, then the clean read in Oct 2027", "North America direct sales growing", "Negative two quarters running")}
{link("International slows", "Every quarter", "Growth of 7% or more", "Below 5% two quarters running")}
{link("Weak profit quality", "Feb 2027 guidance", "Margin 22.5% or more", "Margin below 21.5%")}
{link("Bosses selling", "Any new Form 4", "Selling stops", "CEO sells 10% more")}
{link("Tariffs", "When the court rules", "Removed", "Raised")}</tbody></table>
<p>The <b>bad signs</b> are our kill criteria. {ASSUME}</p>
{card("say", "Say it", "<p>&quot;Each risk has a date when it gets tested. The fad risk gets its first test in February and its real test in October 2027.&quot;</p>")}
{bl("Risks and catalysts are one piece of thinking. The catalyst is when the risk gets answered.")}''')
# =============================================== LEVEL 6 ===============================================
up = [("sales", "revenue"), ("profit per share", "EPS"), ("how many times profit you pay", "the P/E multiple"), ("spare cash", "free cash flow"), ("the company's own forecast", "guidance"), ("the analysts' average", "consensus"), ("how much we could lose", "the downside"),
      ("what softens the risk", "the mitigant"), ("costs that do not shrink", "fixed costs"), ("our sell rules", "kill criteria"), ("an event that moves the price", "a catalyst"), ("already in the price", "priced in")]
page(6, "Upgrade your words", f'''
<p>You now know the plain version. Here is the term to use in the room.</p>
<table><thead><tr><th style="width:50%">Plain version</th><th>Say this instead</th></tr></thead><tbody>{"".join(f"<tr><td>{a}</td><td><b>{b_}</b></td></tr>" for a, b_ in up)}</tbody></table>
{card("note", "Tip", "<p>Use the term, then explain it once in plain words. For example: &quot;the <b>mitigant</b>, the thing that softens this risk, is international growth.&quot;</p>")}''')
page(6, "Your risk script (about 75 seconds)", f'''
<div class="card say script"><span class="t">Say it. One line at a time.</span>
<p>&quot;Crocs is cheap because of one <b>risk</b>: that the clog is a fad.&quot;</p>
<p>&quot;There is real evidence. North America <b>revenue</b> fell 7% last year and is still down 2%.&quot;</p>
<p>&quot;So we measured it. About <b>16% of revenue</b> is at risk.&quot;</p>
<p>&quot;Crocs has high <b>fixed costs</b>. So a 16% fall in revenue would roughly <b>halve EPS</b>, from about ${R['eps0']:.0f} to about ${R['eps1']:.0f}.&quot;</p>
<p>&quot;In that <b>stress test</b>, a share is worth about ${R['val']:.0f}.&quot;</p>
<p>&quot;We do not think that is likely. Our <b>bear case</b> is ${bear:,.0f}, and we give it a one-in-four chance. The market is <b>pricing in</b> about {impl:.0f}%.&quot;</p>
<p>&quot;The main <b>mitigant</b> is international. It is over half the brand and growing 12%.&quot;</p>
<p>&quot;Two other risks: EPS growth is all buybacks, and the CEO has sold ${INS['ceo_sales_usd']/1e6:.0f} million of shares.&quot;</p>
<p>&quot;Our <b>kill criteria</b>: we sell if North America direct sales are negative for two quarters, or international growth drops below 5%.&quot;</p></div>
<p class="small">The bold words are the terms from this guide. Practise until you can say it without reading.</p>''')
page(6, "Your catalyst script (about 60 seconds)", f'''
<div class="card say script"><span class="t">Say it. One line at a time.</span>
<p>&quot;A cheap stock needs a reason to stop being cheap. So here are our <b>catalysts</b>.&quot;</p>
<p>&quot;First: around the 11th of February. Crocs gives its first <b>guidance</b> for 2027.&quot;</p>
<p>&quot;<b>Consensus</b> is 16 dollars of EPS. Guidance leaves out buybacks. Even so, we get about {exbb:.1f} dollars.&quot;</p>
<p>&quot;So we see a 60% chance that guidance is at or above consensus.&quot;</p>
<p>&quot;Second: late October 2027. An accounting change is hiding the real North America trend. In October it drops out.&quot;</p>
<p>&quot;That is the number that settles the fad debate.&quot;</p>
<p>&quot;In between, Crocs can buy back 1.7 billion dollars of shares. That is {1700/F['mcap']*100:.0f}% of the company, and it is not in consensus.&quot;</p>
<p>&quot;One warning. The shares move about {F['earn_avg_abs_move']:.0f}% on a results day. So we would start with half a position.&quot;</p></div>
{card("say", "The 20-second version of your whole section", f"<p>&quot;The main risk is that the clog is a fad. We sized it: 16% of revenue, which would halve EPS. We think that is a one-in-four outcome. The mitigant is international growth. And we find out on two dates: February, and October 2027.&quot;</p>")}''')
qa = [("What is the biggest risk?", "That the clog is a fad and it is ending in North America. Our stress test says EPS could halve."), ("How did you get 16%? Is it made up?", f"The revenue figures are facts. The scores are our judgement. We tested them: one notch either way gives {R['minus1_pct']*100:.0f}% to {R['plus1_pct']*100:.0f}%."),
      ("Why would profit fall more than revenue?", f"Fixed costs. About ${ST['fixed']/1000:.1f} billion of Crocs' costs do not shrink when sales fall."), ("How likely is the bad case?", f"We say one in four. The share price implies about {impl:.0f}%."),
      ("What would make you sell?", "North America direct sales negative for two quarters. Or international growth below 5%. Or a margin guide below 21.5%."), ("The CEO is selling. Why buy?", f"It is a fair concern. He sold ${INS['ceo_sales_usd']/1e6:.0f} million and the forms show no pre-arranged plan. He still owns about ${INS['ceo_shares_after']*price/1e6:.0f} million."),
      ("What is the next catalyst?", "Around 11 February: first 2027 guidance. We want EPS guidance of 16 dollars or more."), ("What if results are good but the shares fall?", "It has happened three times in eight. That is why we start with half a position."),
      ("Are tariffs a big risk?", f"No. Each point costs about {tar*100:.0f} cents of EPS. Tariffs were cut this year."), ("The shares doubled. Is it priced in?", "A lot is. What is not priced in is the buybacks. They are missing from consensus.")]
def qcards(items): return "".join(f'<div class="card note" style="padding:6pt 10pt 3pt;margin:5pt 0"><p class="q">{q}</p><p class="a">{a}</p></div>' for q, a in items)
page(6, "Ten questions you might get (1 to 5)", f'''<p>Cover the answer. Say it out loud. Then check.</p>{qcards(qa[:5])}''')
page(6, "Ten questions you might get (6 to 10)", f'''{qcards(qa[5:])}{card("say", "If you do not know", "<p>&quot;I do not have that number. I can tell you how it would change our view.&quot; Then link it to a kill rule.</p>")}''')
nums = [(f"${price:.0f}", "Share price today " + FACT), (f"${base:,.0f}", f"Base case, Dec 2027 ({rba:+.0f}%) " + ASSUME), (f"${bear:,.0f}", f"Bear case ({rb:+.0f}%), 25% chance " + ASSUME), (f"about ${R['val']:.0f}", "Worst case, full fad unwind " + ASSUME),
        ("16%", f"Revenue at risk (${R['at_risk']:,.0f}m) " + ASSUME), (f"${R['eps0']:.0f} to ${R['eps1']:.0f}", "EPS in the stress test: halved " + ASSUME), (f"25% vs {impl:.0f}%", "Our bear chance vs what is priced in " + ASSUME), ("-2% and +12%", "North America and International, latest quarter " + FACT),
        (f"${INS['ceo_sales_usd']/1e6:.0f}m", "Shares sold by the CEO since June " + FACT), ("11 Feb, late Oct", "The two key catalyst dates in 2027"), (f"{F['earn_avg_abs_move']:.0f}%", "Average move on a results day " + FACT), ("AA", "MSCI ESG rating. A governance mitigant " + FACT)]
page(6, "Twelve numbers to know by heart", f'''<div class="cols3" style="gap:8pt;margin-top:4pt">{"".join(tile(n, l) for n, l in nums)}</div>
{card("risk", "Do not mix these two up", f"<p><b>${bear:,.0f}</b> is the <b>bear case</b>. <b>${R['val']:.0f}</b> is the <b>worst case</b>.</p><p>Asked for your downside? Say ${bear:,.0f}. Asked for the worst case? Say about ${R['val']:.0f}.</p>")}''')
page(6, "Our assumptions, all in one place", f'''
<p>These are judgements, not facts. If you use one, say <b>&quot;we assume&quot;</b>.</p>
<table><thead><tr><th style="width:36%">Assumption</th><th>What we assumed</th></tr></thead><tbody>
<tr><td><b>The chances</b></td><td>Bear 25%, base 50%, bull 25%</td></tr>
<tr><td><b>The share prices</b></td><td>${bear:,.0f}, ${base:,.0f}, ${bull:,.0f}. That is a P/E of 7, 10.5 and 13 on 2028 EPS</td></tr>
<tr><td><b>The risk scores</b></td><td>1 to 5 for nine parts of the business. Score 5 = a 30% fall in sales</td></tr>
<tr><td><b>Fixed costs</b></td><td>About ${ST['fixed']/1000:.1f} billion does not shrink when sales fall</td></tr>
<tr><td><b>Growth</b></td><td>Sales grow about 4% a year. Operating margin stays near 23%</td></tr>
<tr><td><b>Buybacks</b></td><td>Continue at about $600 million a year</td></tr>
<tr><td><b>Odds on catalysts</b></td><td>60% for February, 55% for October</td></tr></tbody></table>
{card("say", "If someone challenges an assumption", "<p>&quot;That is our assumption. We tested it, and here is how much the answer moves.&quot;</p>")}
{card("note", "Check the date", "<p>Everything here is as of <b>25 November 2026</b>. Crocs speaks on 1 December and reports around 11 February. If you present after either, check what changed.</p>")}''')
page(6, "Six slips to avoid", f'''
<ol class="steps">
<li><b>Do not say the risk is small.</b> Say the loss in the bear case ({rb:+.0f}%) is bigger than the gain in the base case ({rba:+.0f}%), and the bet works on the odds.</li>
<li><b>Do not say North America is growing.</b> Reported sales are down 2%. Only direct sales, adjusted for the fog, are up.</li>
<li><b>Do not say the CEO sold &quot;without a plan&quot;.</b> Say the forms do not show one.</li>
<li><b>Do not call HEYDUDE a success.</b> It grew for one quarter, against a very weak year before.</li>
<li><b>Do not promise dates.</b> Say &quot;around 11 February&quot;.</li>
<li><b>Do not present an assumption as a fact.</b> Say &quot;we estimate&quot;.</li></ol>
<h2>Where to find more</h2>
<ul><li><b>deep-dive.md</b>: the full research.</li><li><b>model.xlsx</b>: the numbers behind every estimate.</li><li><b>sources.md</b>: every source, with links.</li></ul>
{bl("You are ready when you can explain page 3 and the two scripts without looking.")}''')
doc = f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>Crocs (CROX): risks, mitigants and catalysts - easy-read study guide</title><style>{CSS}</style></head><body>{''.join(PAGES)}</body></html>"
hp = os.path.join(ROOT, "easy-read.html"); open(hp, "w").write(doc)
js = """
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.argv[2], { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
  const over = await p.evaluate(() => [...document.querySelectorAll('.pg')].map((s, i) => { const f = s.querySelector('.foot'); let bottom = 0; for (const c of s.children) { if (c !== f) bottom = Math.max(bottom, c.getBoundingClientRect().bottom); } return [i + 1, Math.round(bottom - f.getBoundingClientRect().top)]; }).filter(x => x[1] > -4));
  console.log('fonts:', await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').length), 'pages overflowing (page, px past footer):', JSON.stringify(over));
  await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, margin: { top: '0', bottom: '0', left: '0', right: '0' } });
  await b.close();
})();
"""
jp = os.path.join(ROOT, "scripts", "_print_easy.js"); open(jp, "w").write(js)
out = os.path.join(ROOT, "crocs-risk-catalyst-guide-easy-read.pdf")
print(subprocess.run(["node", jp, hp, out], check=True, capture_output=True, text=True).stdout.strip()); os.remove(hp)
from pypdf import PdfReader
import re
words = len(re.sub(r"<[^>]+>", " ", "".join(PAGES)).split())
print("saved", out, "pages:", len(PdfReader(out).pages), "sections:", len(PAGES), "words:", words)
