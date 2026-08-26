# -*- coding: utf-8 -*-
"""Work Experience Guide - A5 stapled booklet. HTML -> (chromium) -> PDF."""
import os, html as _h

BASE = os.path.dirname(os.path.abspath(__file__))

S1, S2, S3, S4 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
S5, S6, S7, S8 = "#e87ba4", "#008300", "#4a3aa7", "#e34948"
B100, B200, B300, B450, B650 = "#cde2fb", "#9ec5f4", "#6da7ec", "#2a78d6", "#104281"
INK, INK2, INK3 = "#12110f", "#54524c", "#8a877e"
SURF, PANEL, RULE = "#ffffff", "#f7f6f2", "#e5e1d8"
NAVY = "#12324e"
GRID = "#e8e5dd"


def esc(t):
    return _h.escape(str(t))


def svg_open(w, h):
    return (f'<svg class="fig" viewBox="0 0 {w} {h}" width="100%" role="img" '
            f'xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">')


def txt(x, y, s, size=8, fill=INK2, weight=400, anchor="start", ls="0"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" text-anchor="{anchor}" '
            f'letter-spacing="{ls}">{esc(s)}</text>')


def rrect(x, y, w, h, fill, r=3, extra=""):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(w,0.1):.1f}" '
            f'height="{max(h,0.1):.1f}" rx="{r}" fill="{fill}" {extra}/>')


def wrap(s, n):
    words, lines, cur = s.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if len(t) <= n:
            cur = t
        else:
            lines.append(cur); cur = wd
    if cur:
        lines.append(cur)
    return lines


DEFS = f'''<defs>
<marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6"
 markerHeight="6" orient="auto-start-reverse">
 <path d="M0 0 L10 5 L0 10 z" fill="{INK3}"/></marker>
</defs>'''


def stackc(cx, y, lines, size=7.4, fill=INK2, lh=9, weight=400):
    return "".join(txt(cx, y + i * lh, ln, size, fill, weight, "middle")
                   for i, ln in enumerate(lines))


# ------------------------------------------------------------- diagrams ---
def diag_group():
    """Pictet Group -> the four business lines."""
    W, H = 480, 250
    o = [svg_open(W, H), DEFS]
    o.append(rrect(90, 4, 300, 44, NAVY, 6))
    o.append(txt(240, 22, "THE PICTET GROUP", 10, "#ffffff", 700, "middle", ".5"))
    o.append(txt(240, 37, "Founded 1805 in Geneva. Owned by 7 partners who work here.",
                 7, "#c3d5e5", 400, "middle"))
    o.append(f'<path d="M240 48 V62 M58 62 H422 M58 62 V74 M179 62 V74 '
             f'M301 62 V74 M422 62 V74" fill="none" stroke="{INK3}" '
             f'stroke-width="1"/>')
    lines = [("WEALTH\nMANAGEMENT", S1,
              ["Looks after rich", "families and their", "money"]),
             ("ASSET\nMANAGEMENT", S2,
              ["Runs funds for", "pension funds and", "big institutions"]),
             ("ALTERNATIVE\nADVISORS", S3,
              ["Invests in things", "not on the stock", "market"]),
             ("ASSET\nSERVICES", S4,
              ["Holds and admin-", "isters assets for", "other firms"])]
    cw = 112
    for i, (name, col, body) in enumerate(lines):
        x = i * (cw + 10)
        o.append(rrect(x, 74, cw, 92, "#ffffff", 6,
                       f'stroke="{RULE}" stroke-width="1"'))
        o.append(rrect(x, 74, cw, 4, col, 2))
        ty = 92
        for ln in name.split("\n"):
            o.append(txt(x + cw / 2, ty, ln, 7.6, INK, 700, "middle", ".2"))
            ty += 10
        o.append(stackc(x + cw / 2, ty + 8, body))
    o.append(rrect(0, 178, 480, 32, "#eef4fb", 5, f'stroke="{B200}"'))
    o.append(txt(240, 191, "You are almost certainly sitting in ONE of these four.",
                 8, INK, 700, "middle"))
    o.append(txt(240, 203, "Find out which one on day one - it is the single most "
                           "useful thing to know.", 7.4, INK2, 400, "middle"))
    o.append(txt(0, 228, "I am in:", 8, INK, 700))
    o.append(f'<line x1="42" y1="230" x2="300" y2="230" stroke="{INK3}" '
             f'stroke-width="0.8" stroke-dasharray="2 2"/>')
    o.append(txt(0, 244, "My team is called:", 8, INK, 700))
    o.append(f'<line x1="82" y1="246" x2="300" y2="246" stroke="{INK3}" '
             f'stroke-width="0.8" stroke-dasharray="2 2"/>')
    o.append("</svg>")
    return "".join(o)


def diag_shop():
    """Asset management explained as a shop."""
    W, H = 480, 200
    o = [svg_open(W, H)]
    cols = [("WHO WE SELL TO", S1, "the customers",
             ["Pension funds", "Insurance companies",
              "Sovereign wealth funds", "Wealthy families",
              "Other banks who sell", "our funds on"]),
            ("WHAT WE SELL", S2, "the product",
             ["Not a thing you can", "hold. We sell a",
              "DECISION: what to buy,", "what to sell, when.",
              "Wrapped in a fund or", "a mandate."]),
            ("HOW WE GET PAID", S3, "the till",
             ["A small % of the money", "we look after, every",
              "year.", "", "0.5% of GBP 1bn is", "GBP 5m a year."])]
    cw = 152
    for i, (name, col, sub, body) in enumerate(cols):
        x = i * (cw + 12)
        o.append(rrect(x, 4, cw, 136, "#ffffff", 6,
                       f'stroke="{RULE}" stroke-width="1"'))
        o.append(rrect(x, 4, cw, 4, col, 2))
        o.append(txt(x + cw / 2, 24, name, 8, INK, 700, "middle", ".3"))
        o.append(txt(x + cw / 2, 36, sub, 7.2, col, 600, "middle"))
        o.append(stackc(x + cw / 2, 58, body, 7.6, INK2, 11))
    o.append(rrect(0, 150, 480, 46, PANEL, 6, f'stroke="{RULE}"'))
    o.append(txt(240, 167, "THE WHOLE INDUSTRY IN ONE SENTENCE", 8, INK, 700,
                 "middle", ".3"))
    o.append(txt(240, 181, "We look after other people's money and get paid a "
                           "small slice of it each year.", 8.4, INK2, 400,
                 "middle"))
    o.append(txt(240, 192, "The money is never ours. The decisions are.", 7.6,
                 INK3, 400, "middle"))
    o.append("</svg>")
    return "".join(o)


def diag_client_flow():
    """How someone becomes a client - the commercial side of the business."""
    W, H = 480, 312
    o = [svg_open(W, H), DEFS]
    steps = [("1", "MARKETING", S1,
              "Gets our name in front of the right people. Campaigns, events, "
              "brochures, the website, thought-leadership articles."),
             ("2", "SALES", S2,
              "Actually goes and meets them. Pitches the funds, answers the "
              "hard questions, wins the mandate. Also called Distribution or "
              "Client Relationship."),
             ("3", "PRODUCT & RFP", S3,
              "Builds the pitch behind the pitch. Fills in the huge "
              "questionnaires clients send, and decides which funds we should "
              "even offer."),
             ("4", "ONBOARDING", S4,
              "The paperwork that turns a yes into an account. Legal "
              "agreements, compliance checks, opening the account."),
             ("5", "CLIENT SERVICE", S7,
              "Looks after them once they are in. Day-to-day questions, "
              "queries, problems. Often called the Global Client Group."),
             ("6", "REPORTING", S6,
              "Tells the client how their money did, every month and quarter. "
              "Where Performance and Client Reporting sit."),
             ("7", "THEY STAY (OR THEY GO)", S8,
              "Keeping a client is cheaper than winning one. This is why "
              "everyone in the chain above matters.")]
    y = 4
    for i, (n, name, col, body) in enumerate(steps):
        h = 40
        o.append(rrect(0, y, 480, h, "#ffffff", 5,
                       f'stroke="{RULE}" stroke-width="1"'))
        o.append(rrect(0, y, 4, h, col, 2))
        o.append(f'<circle cx="20" cy="{y+h/2}" r="8" fill="{col}"/>')
        o.append(txt(20, y + h / 2 + 3, n, 8, "#ffffff", 700, "middle"))
        o.append(txt(36, y + 15, name, 8, INK, 700, "start", ".25"))
        for j, ln in enumerate(wrap(body, 78)):
            o.append(txt(36, y + 26 + j * 9, ln, 7.2, INK2))
        if i < len(steps) - 1:
            o.append(f'<path d="M20 {y+h+1} v4" stroke="{INK3}" '
                     f'stroke-width="1.2" marker-end="url(#a)"/>')
        y += h + 4
    o.append("</svg>")
    return "".join(o)


def diag_trade_flow():
    """How an investment decision actually becomes a trade."""
    W, H = 480, 372
    o = [svg_open(W, H), DEFS]
    steps = [("RESEARCH & ANALYSTS", S1,
              "Study companies, countries and economies all day. Produce the "
              "view: is this a good thing to own?"),
             ("PORTFOLIO MANAGER (PM)", S2,
              "Makes the call. Decides what goes in the fund, how much of it, "
              "and when to sell. Carries the performance."),
             ("TRADER / DEALING DESK", S3,
              "Takes the PM's instruction and works out HOW to buy it without "
              "moving the price or paying over the odds."),
             ("EXECUTION", S4,
              "The order actually hits the market, usually through a broker "
              "or an electronic platform."),
             ("OPERATIONS / SETTLEMENT", S7,
              "Makes sure the money goes one way and the shares go the other, "
              "on the right day, to the right place."),
             ("TRADE SUPPORT", S5,
              "Fixes it when that breaks. Chases the mismatches, the failed "
              "settlements, the wrong prices."),
             ("REPORTING & CUSTODY", S6,
              "The asset is recorded, valued daily, and shows up in what the "
              "client sees.")]
    y = 4
    for i, (name, col, body) in enumerate(steps):
        h = 42
        o.append(rrect(0, y, 480, h, "#ffffff", 5,
                       f'stroke="{RULE}" stroke-width="1"'))
        o.append(rrect(0, y, 4, h, col, 2))
        o.append(txt(14, y + 14, name, 8, INK, 700, "start", ".25"))
        for j, ln in enumerate(wrap(body, 84)):
            o.append(txt(14, y + 25 + j * 9, ln, 7.2, INK2))
        if i < len(steps) - 1:
            o.append(f'<path d="M14 {y+h+1} v3" stroke="{INK3}" '
                     f'stroke-width="1.2" marker-end="url(#a)"/>')
        y += h + 3
    o.append(rrect(0, y + 4, 480, 44, "#eef4fb", 5, f'stroke="{B200}"'))
    o.append(txt(240, y + 20, "WATCHING OVER ALL OF IT, ALL THE TIME", 7.6, INK,
                 700, "middle", ".3"))
    o.append(txt(240, y + 33, "Risk  -  Compliance  -  Legal  -  Finance  -  "
                              "Technology  -  Investment Data", 8, INK2, 500,
                 "middle"))
    o.append(txt(240, y + 43, "No trade happens without them. They are not "
                              "'support' in the boring sense.", 6.8, INK3, 400,
                 "middle"))
    o.append("</svg>")
    return "".join(o)


# ----------------------------------------------------------- components ---
def page(inner, cls=""):
    return f'<section class="page {cls}">{inner}</section>'


def head(kicker, title, dek=""):
    d = f'<p class="dek">{dek}</p>' if dek else ""
    return (f'<div class="phead"><span class="kick">{esc(kicker)}</span>'
            f'<h1>{esc(title)}</h1>{d}</div>')


def fig(svg, cap=""):
    c = f'<p class="figcap">{cap}</p>' if cap else ""
    return f'<figure>{svg}{c}</figure>'


def box(kind, title, body="", items=None, ol=False):
    li = ""
    if items:
        tag = "ol" if ol else "ul"
        li = f"<{tag}>" + "".join(f"<li>{i}</li>" for i in items) + f"</{tag}>"
    b = f"<p>{body}</p>" if body else ""
    t = f"<h4>{esc(title)}</h4>" if title else ""
    return f'<div class="box {kind}">{t}{b}{li}</div>'


def qlist(title, colour, items):
    li = "".join(f"<li>{i}</li>" for i in items)
    return (f'<div class="qgroup" style="--c:{colour}">'
            f'<h5>{esc(title)}</h5><ul>{li}</ul></div>')


def teamtable(rows):
    tb = ""
    for name, what in rows:
        tb += (f'<tr><td class="tn">{esc(name)}</td>'
               f'<td class="tw">{esc(what)}</td><td class="tf"></td></tr>')
    return (f'<table class="teams"><thead><tr><th>Team</th>'
            f'<th>What they actually do</th><th>Floor</th></tr></thead>'
            f'<tbody>{tb}</tbody></table>')


CSS = f"""
@page {{ size: A5 portrait; margin: 11mm 11mm 10mm 11mm; }}
* {{ box-sizing: border-box; -webkit-print-color-adjust: exact;
     print-color-adjust: exact; }}
html {{ font-size: 9.2pt; }}
body {{ margin: 0; font-family: Inter, 'Liberation Sans', sans-serif;
        color: {INK2}; line-height: 1.5; background: {SURF}; }}
h1, h2, h3, h4, h5 {{ color: {INK}; line-height: 1.2; margin: 0; }}
p {{ margin: 0 0 0.6em; }}
strong {{ color: {INK}; font-weight: 600; }}
.page {{ break-after: page; }}
.page:last-child {{ break-after: auto; }}

/* ---------- page heads ---------- */
.phead {{ border-top: 3px solid {NAVY}; padding-top: 3mm; margin-bottom: 4mm; }}
.kick {{ display: block; font-size: 6.6pt; letter-spacing: .18em;
         font-weight: 700; text-transform: uppercase; color: {S2};
         margin-bottom: 1.6mm; }}
.phead h1 {{ font-family: 'Source Serif 4', Georgia, serif; font-size: 16pt;
             font-weight: 600; letter-spacing: -0.01em; color: {NAVY}; }}
.phead .dek {{ font-size: 8.4pt; color: {INK2}; margin: 2mm 0 0; }}
h2 {{ font-family: 'Source Serif 4', Georgia, serif; font-size: 11.5pt;
      font-weight: 600; margin: 4mm 0 1.8mm; }}
h3 {{ font-size: 7pt; font-weight: 700; text-transform: uppercase;
      letter-spacing: .14em; color: {S2}; margin: 3.5mm 0 1.5mm; }}

/* ---------- cover ---------- */
.cover {{ height: 189mm; display: flex; flex-direction: column;
          justify-content: space-between; }}
.logobox {{ border: 1.5px dashed {B200}; border-radius: 4px; height: 20mm;
            display: flex; align-items: center; justify-content: center;
            color: {B300}; font-size: 6.8pt; letter-spacing: .18em;
            font-weight: 700; text-transform: uppercase; }}
.cover h1 {{ font-family: 'Source Serif 4', Georgia, serif; font-size: 30pt;
             font-weight: 600; color: {NAVY}; letter-spacing: -0.02em;
             line-height: 1.05; margin: 0 0 3mm; }}
.cover .tag {{ font-family: 'Source Serif 4', Georgia, serif; font-size: 11.5pt;
               color: {INK2}; line-height: 1.35; }}
.bars {{ display: flex; gap: 2.5px; margin: 5mm 0; }}
.bars i {{ height: 7px; flex: 1; border-radius: 2px; }}
.fillin {{ border-top: 1px solid {RULE}; padding-top: 3.5mm; }}
.fillin .row {{ display: flex; align-items: baseline; gap: 3mm;
                margin-bottom: 3.2mm; }}
.fillin .row b {{ font-size: 7.4pt; color: {INK}; width: 26mm;
                  flex: 0 0 26mm; font-weight: 600; }}
.fillin .row span {{ flex: 1; border-bottom: 1px dotted {INK3}; height: 4mm; }}
.cover .foot {{ font-size: 7pt; color: {INK3}; }}

/* ---------- boxes ---------- */
.box {{ border: 1px solid {RULE}; border-left: 3px solid {S1};
        background: {PANEL}; border-radius: 4px; padding: 3mm 3.5mm;
        margin: 3mm 0; font-size: 8pt; break-inside: avoid; }}
.box h4 {{ font-size: 6.8pt; text-transform: uppercase; letter-spacing: .13em;
           font-weight: 700; margin-bottom: 1.5mm; color: {S1}; }}
.box p {{ margin-bottom: 1.5mm; }}
.box ul, .box ol {{ margin: 0; padding-left: 4mm; }}
.box li {{ margin-bottom: 1.2mm; }}
.box.warn {{ border-left-color: {S8}; background: #fdf2f2; }}
.box.warn h4 {{ color: #b32b2b; }}
.box.win {{ border-left-color: {S6}; background: #f1f8f1; }}
.box.win h4 {{ color: #086108; }}
.box.key {{ border-left-color: {S4}; background: #fdf7e8; }}
.box.key h4 {{ color: #8a5e00; }}
.box.dark {{ border: none; border-left: 3px solid {S2}; background: {NAVY};
             color: #d5e2ee; }}
.box.dark h4 {{ color: {S4}; }}
.box.dark strong {{ color: #ffffff; }}

/* ---------- figures ---------- */
figure {{ margin: 3mm 0; break-inside: avoid; }}
svg.fig {{ display: block; }}
.figcap {{ font-size: 6.8pt; color: {INK3}; margin: 1.5mm 0 0; }}

/* ---------- contents ---------- */
.toc {{ font-size: 8pt; }}
.toc .r {{ display: flex; gap: 3mm; padding: 1.6mm 0;
           border-bottom: 1px dotted {RULE}; }}
.toc .r em {{ font-style: normal; font-weight: 700; color: {S1}; width: 5mm;
              flex: 0 0 5mm; }}
.toc .r b {{ color: {INK}; font-weight: 600; }}
.toc .r span {{ color: {INK3}; }}

/* ---------- teams table ---------- */
table.teams {{ width: 100%; border-collapse: collapse; font-size: 7.2pt; }}
table.teams th {{ text-align: left; font-size: 6.2pt; text-transform: uppercase;
                  letter-spacing: .1em; color: {INK3}; font-weight: 700;
                  padding: 0 2mm 1.2mm 0; border-bottom: 1.2px solid {INK3}; }}
table.teams td {{ padding: 1.3mm 2mm 1.3mm 0; border-bottom: 1px solid {RULE};
                  vertical-align: top; line-height: 1.32; }}
td.tn {{ color: {INK}; font-weight: 600; width: 31%; }}
td.tw {{ width: 55%; }}
td.tf {{ width: 14%; border-bottom: 1px solid {RULE};
         background: repeating-linear-gradient(90deg, {GRID} 0 3px,
         transparent 3px 6px) bottom / 100% 1px no-repeat; }}
tr {{ break-inside: avoid; }}

/* ---------- question groups ---------- */
.qgroup {{ margin-bottom: 3mm; break-inside: avoid; }}
.qgroup h5 {{ font-size: 6.8pt; text-transform: uppercase; letter-spacing: .12em;
              font-weight: 700; color: var(--c); margin-bottom: 1.2mm;
              border-bottom: 1.5px solid var(--c); padding-bottom: 1mm; }}
.qgroup ul {{ margin: 0; padding-left: 3.6mm; font-size: 7.6pt; }}
.qgroup li {{ margin-bottom: 1.1mm; line-height: 1.38; }}

/* ---------- misc ---------- */
ul.plain, ol.plain {{ margin: 0 0 2.5mm; padding-left: 4mm; font-size: 8pt; }}
ul.plain li, ol.plain li {{ margin-bottom: 1.4mm; }}
.two {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; }}
.tick {{ list-style: none; padding-left: 0; font-size: 8pt; }}
.tick li {{ position: relative; padding-left: 6mm; margin-bottom: 2mm; }}
.tick li::before {{ content: ""; position: absolute; left: 0; top: 0.4mm;
                    width: 3.4mm; height: 3.4mm; border: 1.2px solid {INK3};
                    border-radius: 1px; }}
.notes {{ border: 1px solid {RULE}; border-radius: 4px; }}
.notes table {{ width: 100%; border-collapse: collapse; font-size: 7pt; }}
.notes th {{ background: {PANEL}; text-align: left; font-size: 6.2pt;
             text-transform: uppercase; letter-spacing: .1em; color: {INK3};
             font-weight: 700; padding: 1.6mm 2mm; border-bottom: 1px solid {RULE}; }}
.notes td {{ height: 8mm; border-bottom: 1px solid {GRID};
             border-right: 1px solid {GRID}; }}
.notes td:last-child {{ border-right: none; }}
.linkrow {{ font-size: 7.6pt; border-bottom: 1px dotted {RULE};
            padding: 1.8mm 0; display: flex; gap: 3mm; }}
.linkrow b {{ color: {INK}; font-weight: 600; width: 34mm; flex: 0 0 34mm; }}
.linkrow span {{ flex: 1; border-bottom: 1px dotted {INK3}; }}
.pagenum {{ position: fixed; bottom: 0; right: 0; font-size: 6.4pt;
            color: {INK3}; }}
"""


# ---------------------------------------------------------------- pages ---
def p_cover():
    bars = "".join(f'<i style="background:{c}"></i>'
                   for c in [S1, S2, S3, S4, S5, S7, S6, S8])
    return page(f'''
<div class="cover">
  <div>
    <div class="logobox">Logo goes here</div>
    <div style="height:16mm"></div>
    <h1>Work<br>Experience<br>Guide</h1>
    <p class="tag">Everything nobody sits you down and explains.<br>
    Twelve pages. Read it on the train.</p>
    <div class="bars">{bars}</div>
  </div>
  <div>
    <div class="fillin">
      <div class="row"><b>Name</b><span></span></div>
      <div class="row"><b>Dates here</b><span></span></div>
      <div class="row"><b>My host</b><span></span></div>
      <div class="row"><b>My desk / floor</b><span></span></div>
    </div>
    <p class="foot">Written by people who were sitting where you are, not
    that long ago.</p>
  </div>
</div>''', "cover")


def p_contents():
    rows = [("1", "What this is", "and the five rules that matter"),
            ("2", "Who we actually are", "the Group, and the four bits of it"),
            ("3", "What asset management is", "explained as a shop"),
            ("4", "How the business works", "how someone becomes a client"),
            ("5", "How an investment happens", "from an idea to a trade"),
            ("6", "Who does what", "every team, in one line each"),
            ("7", "Coffee chats", "what they are actually for"),
            ("8", "Questions to ask", "so you never sit there blank"),
            ("9", "Things we wish we'd known", "the honest list"),
            ("10", "Useful links", "and what to watch"),
            ("11", "Your notes", "who you met and what to do next")]
    body = "".join(f'<div class="r"><em>{n}</em><b>{t}</b>'
                   f'<span>&mdash; {d}</span></div>' for n, t, d in rows)
    return page(head("Start here", "What's in this guide",
                     "You are here for a few days or a few weeks. That is not "
                     "long. This exists so you do not spend the first three "
                     "of them working out what everyone does.") + f'''
<div class="toc">{body}</div>
{box("key", "The five rules", "", [
 "<strong>Bring a notebook.</strong> A real one. You will not remember six "
 "names by Thursday.",
 "<strong>Sleep.</strong> Genuinely. The days are long and you are on show.",
 "<strong>Say yes to every coffee.</strong> Especially the boring-sounding ones.",
 "<strong>Ask the obvious question.</strong> Nobody expects you to know "
 "anything - only to be curious.",
 "<strong>Write down names.</strong> Name, team, one thing they said. Page 11 "
 "is for exactly this."], ol=True)}
{box("", "What a good week looks like",
 "You leave knowing what the different jobs are and which of them sound like "
 "you. Everything else is a bonus - nobody understood it all in week one.")}
''')


def p_group():
    return page(head("Page 2", "Who we actually are",
                     "Most people spend their whole placement not quite sure "
                     "what the company is. Two minutes now saves you that.") +
                fig(diag_group()) + f'''
{box("", "The bit that confuses everyone",
 "<strong>Pictet Group</strong> is the whole company. Inside it are four "
 "separate businesses that do genuinely different jobs for different "
 "customers. When someone says 'we', ask which one they mean. It is not a "
 "silly question - people who have worked here for years get it wrong.")}
{box("win", "Worth knowing",
 "The firm is 220 years old and has no shareholders and no stock market "
 "listing. It is owned by seven partners who all work in the building. That "
 "is unusual in finance, and it is the reason people here talk about decades "
 "rather than quarters.")}
''')


def p_shop():
    return page(head("Page 3", "What asset management is",
                     "Forget the jargon. It is a shop.") +
                fig(diag_shop()) + f'''
{box("", "So what is a 'fund'?",
 "A big pot that lots of different customers put money into, run as one "
 "portfolio by one team. Easier and cheaper than running a separate pot for "
 "everyone. A <strong>mandate</strong> is the opposite - one giant customer, "
 "their own pot, their own rules.")}
{box("key", "The two words you will hear constantly",
 "", ["<strong>AUM</strong> - assets under management. How much money we look "
      "after. Everything in this building is ultimately about making that "
      "number go up and keeping it there.",
      "<strong>bps</strong> - said 'bips'. One bp is 0.01%. It is how fees "
      "get quoted, because the amounts of money involved are enormous."])}
''')


def p_client():
    return page(head("Page 4", "How the business works",
                     "How a stranger turns into a client, and who touches them "
                     "on the way. Almost every non-investment job in this "
                     "building sits somewhere on this chain.") +
                fig(diag_client_flow()) + f'''
{box("key", "Why this chain matters to you",
 "Most of the jobs in this building are on this page rather than the next "
 "one. If someone says they work in RFP, onboarding or client service, you "
 "now know exactly where they sit and who they hand work to.")}
''')


def p_trade():
    return page(head("Page 5", "How an investment actually happens",
                     "Someone has an idea. Days later it is a real holding in "
                     "a real portfolio. This is what happens in between.") +
                fig(diag_trade_flow()) + f'''
{box("", "The question this page is really asking",
 "Which of those boxes sounded interesting? Fast and loud (trading)? "
 "Judgement and research (PM, analyst)? Making complicated things run "
 "properly (operations, trade support)? People and persuasion (sales, client "
 "service)? There is no wrong answer, and knowing which one you lean towards "
 "is worth more than knowing all the jargon.")}
''')


FRONT = [("Portfolio Management", "Decide what the funds buy and sell. Carry "
          "the performance. Often just called 'the PMs'."),
         ("Research / Analysts", "Study companies, sectors and economies and "
          "feed the PMs a view."),
         ("Trading / Dealing", "Turn a PM's decision into a real trade at the "
          "best price they can get."),
         ("Sales / Distribution", "Go out and win the clients. Also called "
          "Client Relationship or Business Development."),
         ("Product / Product Specialists", "Know one strategy inside out and "
          "explain it to clients. Decide what we should launch."),
         ("RFP & Proposals", "Answer the enormous questionnaires clients send "
          "before they will give us money."),
         ("Marketing & Communications", "Campaigns, brand, events, the "
          "website, and getting our views published."),
         ("Client Service", "Look after clients day to day once they are in. "
          "Often the Global Client Group.")]

BACK = [("Operations", "Make sure trades settle - money one way, assets the "
         "other, on the right day."),
        ("Trade Support", "Fix it when that breaks. Chase failed settlements "
         "and mismatched instructions."),
        ("Performance & Reporting", "Work out exactly how each portfolio did "
         "and tell the client."),
        ("Investment Data", "Keep the underlying numbers clean. Everything "
         "above depends on this."),
        ("Risk", "Check portfolios are not taking risks they were not asked "
         "to take."),
        ("Compliance", "Make sure everything we do follows the rules of every "
         "country we do it in."),
        ("Legal", "Draft and review the contracts and agreements behind every "
         "client and every fund."),
        ("Finance", "The firm's own money. Budgets, costs, results."),
        ("Technology", "The systems, platforms and data everyone else uses "
         "all day."),
        ("HR / People", "Hiring, training, and the reason you are here."),
        ("Facilities & Front of House", "The building, the desks, the people "
         "who make it run.")]

BLANKS = [("", ""), ("", ""), ("", "")]


def p_teams_a():
    return page(head("Page 6", "Who does what",
                     "One line each. Nobody expects you to memorise this - use "
                     "it to work out who you want to go and talk to.") + f'''
<h3>The investment side</h3>
{teamtable(FRONT)}
{box("", "Fill in the floors yourself",
 "Teams move around, so the right-hand column is deliberately blank. Ask "
 "someone on your first day and pencil them in - it is a genuinely good "
 "excuse to start a conversation.")}
''')


def p_teams_b():
    return page(f'''
<h3>Everything around it</h3>
{teamtable(BACK + BLANKS)}
{box("key", "A word on job titles",
 "Analyst, Associate, Vice President, Director, Managing Director, Partner - "
 "roughly in that order. Do not be intimidated by a long one. Ask what "
 "someone does, not what they are called.")}
{box("key", "The thing people get wrong",
 "These are not the 'boring' teams. A trade that does not settle is a real "
 "problem for a real client, and the people who fix it are some of the "
 "busiest in the building. Plenty of people in the front office started "
 "somewhere on this page.")}
''')


def p_coffee():
    return page(head("Page 7", "Coffee chats",
                     "You will be booked into a lot of these. Most people turn "
                     "up with no idea what they are for, have a nice enough "
                     "chat, and get nothing out of it. Here is the actual "
                     "point.") + f'''
{box("dark", "The goal, which nobody tells you",
 "Every coffee chat is for <strong>one of two things</strong>. Decide which "
 "before you sit down.", [
 "<strong>Learn about their job.</strong> What do they actually do all day, "
 "and would you want to do it?",
 "<strong>Learn about the industry.</strong> How does this bit connect to "
 "everything else, and what is changing?"])}
<p style="font-size:8pt">It is <em>not</em> an interview and nobody is
scoring you. The only bad outcome is walking out knowing nothing new.</p>
<h3>How to run 15 minutes</h3>
{box("", "", "", [
 "<strong>0-2 min &middot; You.</strong> Two sentences: who you are and what "
 "you are trying to work out. Then stop talking.",
 "<strong>2-10 min &middot; Them.</strong> Get them describing their actual "
 "day. People enjoy that far more than strategy questions.",
 "<strong>10-13 min &middot; Your questions.</strong> Have four ready. You "
 "will use two.",
 "<strong>13-15 min &middot; Close.</strong> Thank them, and ask the one "
 "question on the next page that always works."])}
{box("win", "Before and after",
 "", ["<strong>Before:</strong> two minutes finding out what their team does "
      "puts you ahead of most people.",
      "<strong>After:</strong> three lines in your notebook while it is fresh, "
      "and a short thank-you the same day."])}
{box("warn", "Do not",
 "", ["Ask something the intranet would have answered in 90 seconds.",
      "Ask how much they earn. People do. Do not be one of them.",
      "Spend the whole time talking about yourself.",
      "Sit in silence because you did not prepare - that is what page 8 is for."])}
''')


def p_questions():
    return page(head("Page 8", "Questions to ask",
                     "Cut this page out if you want. Pick four before every "
                     "chat.") + f'''
{qlist("About their actual job", S1, [
 "What did you actually do yesterday?",
 "What is the part of the job people outside the firm would never guess?",
 "What is the hardest part - and what is the boring part?",
 "Who do you deal with most in a normal week?",
 "What does a good day look like versus a bad one?"])}
{qlist("About how they got here", S2, [
 "What did you study, and does it matter as much as people think?",
 "Was this the plan, or did you end up here?",
 "What would you tell yourself at my age?",
 "Did you move teams to get here? Is that normal?"])}
{qlist("About the industry", S3, [
 "What has changed most in the time you have been doing this?",
 "What is everyone in your team talking about at the moment?",
 "Which other team do you rely on most, and why?",
 "If I wanted to understand your world, what should I read or watch?"])}
{qlist("About the firm", S7, [
 "How is this place different from where you worked before?",
 "What surprised you when you joined?",
 "What does being partner-owned actually change day to day?"])}
{qlist("The three that always work", S6, [
 "What should I be asking that I have not?",
 "Is there anyone else you think I should talk to while I am here?",
 "What would make this week genuinely useful for me?"])}
{box("key", "If your mind goes blank",
 "Use this one: <strong>&ldquo;Talk me through what you did yesterday.&rdquo;</strong> "
 "It works on absolutely everyone, in every team, at every level, and it "
 "always leads somewhere.")}
''')


def p_wish():
    return page(head("Page 9", "Things we wish we'd known",
                     "The honest list.") + f'''
{box("", "", "", [
 "<strong>Nobody expects you to know anything.</strong> Genuinely. The people "
 "who look impressive are the ones asking questions, not the ones nodding "
 "along.",
 "<strong>Everyone is busy, and almost everyone will still make time.</strong> "
 "People like talking about their job. Ask.",
 "<strong>The 'boring' teams are often the most interesting.</strong> Some of "
 "the best conversations happen in operations and risk.",
 "<strong>You will not understand half of what you hear in week one.</strong> "
 "Write the words down and look them up later. That is the job.",
 "<strong>Say yes to lunch.</strong> More gets explained over lunch than in "
 "any meeting.",
 "<strong>Nobody will chase you.</strong> If you sit quietly at a desk for a "
 "week, that is what the week will be. Go and ask for things to do.",
 "<strong>Turn up early, not on time.</strong> Ten minutes is enough and it "
 "gets noticed.",
 "<strong>Names matter more than facts.</strong> Remembering someone's name "
 "on day four is worth more than knowing what a basis point is.",
 "<strong>You are allowed to say 'I don't know'.</strong> Followed by "
 "'&mdash; how does that work?'",
 "<strong>Keep in touch afterwards.</strong> A short message in six months "
 "beats an urgent one in two years."])}
{box("win", "The one that matters most",
 "The point of this is not to impress anyone. It is to find out whether you "
 "want to do this for a living, and if so, which bit. Spend the week "
 "answering that and it will have been a good week - even if the answer "
 "turns out to be no.")}
''')


def p_links():
    def lr(a):
        return f'<div class="linkrow"><b>{esc(a)}</b><span></span></div>'
    rows = "".join(lr(x) for x in [
        "People directory", "Intranet home", "Strategy / fund videos",
        "Our funds page", "Learning platform", "Who to email if stuck"])
    return page(head("Page 10", "Useful links",
                     "Half of this page is blank on purpose - your host will "
                     "fill in the internal ones on day one.") + f'''
<h3>Internal &mdash; ask your host</h3>
{rows}
<h3>Worth watching or reading</h3>
{box("", "", "Search these. Twenty minutes each and the rest of the week "
     "makes more sense.", [
 "&ldquo;What does an asset manager do&rdquo; &mdash; the basics, in plain "
 "English",
 "&ldquo;What is a fund / what is an ETF&rdquo; &mdash; what we actually sell",
 "&ldquo;What does a portfolio manager do all day&rdquo;",
 "&ldquo;Front office vs middle office vs back office&rdquo;",
 "&ldquo;Trade lifecycle explained&rdquo; &mdash; page 5 in more detail",
 "<strong>Investopedia</strong> &mdash; look up any word you did not know"])}
<h3>Videos we'd actually recommend</h3>
<div class="linkrow"><b>1.</b><span></span></div>
<div class="linkrow"><b>2.</b><span></span></div>
<div class="linkrow"><b>3.</b><span></span></div>
''')


def p_notes():
    rows = "".join('<tr><td></td><td></td><td></td><td></td></tr>'
                   for _ in range(9))
    return page(head("Page 11", "Your notes",
                     "Fill this in as you go, not on the last afternoon.") +
                f'''
<div class="notes"><table>
<thead><tr><th style="width:24%">Name</th><th style="width:22%">Team</th>
<th style="width:34%">What they do</th><th style="width:20%">Follow up?</th>
</tr></thead><tbody>{rows}</tbody></table></div>
<h3>Before you leave</h3>
<ul class="tick">
<li>Thanked everyone who gave you time</li>
<li>Connected with the people you actually clicked with</li>
<li>Written down the three jobs that interested you most</li>
<li>Asked your host what a good next step would look like</li>
<li>Given honest feedback on the week &mdash; it genuinely gets used</li>
</ul>
{box("dark", "Last thing",
 "You now know more about how this industry works than most people your age, "
 "and quite a few adults. Use it. Good luck.")}
''')


def main():
    fonts = open(os.path.join(BASE, "fonts_embedded.css")).read()
    body = "".join([p_cover(), p_contents(), p_group(), p_shop(), p_client(),
                    p_trade(), p_teams_a(), p_teams_b(), p_coffee(),
                    p_questions(), p_wish(), p_links(), p_notes()])
    doc = ("<!doctype html><html lang='en'><head><meta charset='utf-8'>"
           "<title>Work Experience Guide</title>"
           f"<style>{fonts}</style><style>{CSS}</style></head>"
           f"<body>{body}</body></html>")
    out = os.path.join(BASE, "work_experience_guide.html")
    open(out, "w").write(doc)
    print("wrote", out, len(doc))


if __name__ == "__main__":
    main()
