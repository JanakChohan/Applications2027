"""Build deck.pptx: 15 main slides + appendix, takeaway titles, source lines and speaker notes. Numbers from facts.json."""
import json, os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); F = json.load(open(os.path.join(ROOT, "data", "derived", "facts.json"))); MO = json.load(open(os.path.join(ROOT, "data", "derived", "model_outputs.json")))
V = F["valuation"]; K = F["key"]; RAR = F["rar"]; S = F["scen"]; B = S["Base"]; RK = F["risk"]; PEER = F["peers"]; SN = F["sens"]; Q = F["quarters"]
price = F["price"]; pt_bear, pt_base, pt_bull, pt_w = V["pt"]; r_bear, r_base, r_bull, r_w = [v * 100 for v in V["ret"]]; e27 = V["eps27"]; e28 = V["eps28"]; dcf = V["dcf"]
m = lambda x, d=0: f"${x:,.{d}f}m"; pk = lambda t, k: PEER[t][k]; fy = lambda y: F[f"fy{y}"]
NAVY = RGBColor(0x1F, 0x38, 0x64); INK = RGBColor(0x1F, 0x23, 0x28); GREY = RGBColor(0x5F, 0x63, 0x68); BLUE = RGBColor(0x2A, 0x78, 0xD6); LIGHT = RGBColor(0xEE, 0xF3, 0xFA); WHITE = RGBColor(255, 255, 255); RED = RGBColor(0xC5, 0x36, 0x2F)
prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5); BLANK = prs.slide_layouts[6]; count = {"n": 0}
def tb(slide, x, y, w, h, text="", size=12, bold=False, color=INK, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = box.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05); tf.margin_top = tf.margin_bottom = Inches(0.03)
    p = tf.paragraphs[0]; r = p.add_run(); r.text = text; r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color; r.font.name = "Calibri"; p.alignment = align
    return box
def bullets(slide, x, y, w, h, items, size=13, gap=5):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = box.text_frame; tf.word_wrap = True; tf.margin_left = Inches(0.05)
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); p.space_after = Pt(gap)
        lead, text = it if isinstance(it, tuple) else (None, it)
        r0 = p.add_run(); r0.text = "•  "; r0.font.size = Pt(size); r0.font.color.rgb = BLUE; r0.font.name = "Calibri"
        if lead: r = p.add_run(); r.text = lead + " "; r.font.bold = True; r.font.size = Pt(size); r.font.color.rgb = INK; r.font.name = "Calibri"
        r = p.add_run(); r.text = text; r.font.size = Pt(size); r.font.color.rgb = INK; r.font.name = "Calibri"
    return box
def table(slide, rows, x, y, w, col_w=None, size=10.5, row_h=0.3, header=True, first_bold=True):
    t = slide.shapes.add_table(len(rows), len(rows[0]), Inches(x), Inches(y), Inches(w), Inches(row_h * len(rows))).table
    tot = sum(col_w) if col_w else None
    for j in range(len(rows[0])):
        t.columns[j].width = Inches(w * col_w[j] / tot) if col_w else Inches(w / len(rows[0]))
    for i, row in enumerate(rows):
        t.rows[i].height = Inches(min(row_h, 0.4) if (header and i == 0) else row_h)
        for j, val in enumerate(row):
            c = t.cell(i, j); c.text = ""; tf = c.text_frame; tf.word_wrap = True; c.margin_left = c.margin_right = Inches(0.05); c.margin_top = c.margin_bottom = Inches(0.02); c.vertical_anchor = MSO_ANCHOR.MIDDLE
            r = tf.paragraphs[0].add_run(); r.text = str(val); r.font.size = Pt(size); r.font.name = "Calibri"; r.font.color.rgb = INK
            c.fill.solid()
            if header and i == 0: c.fill.fore_color.rgb = NAVY; r.font.color.rgb = WHITE; r.font.bold = True
            else:
                c.fill.fore_color.rgb = LIGHT if i % 2 == 0 else WHITE
                if j == 0 and first_bold: r.font.bold = True
    return t
def pic(slide, name, x, y, w=None, h=None, max_h=None):
    path = os.path.join(ROOT, "charts", name); iw, ih = Image.open(path).size
    if w and max_h and w * ih / iw > max_h: w = max_h * iw / ih
    if w: return slide.shapes.add_picture(path, Inches(x), Inches(y), width=Inches(w))
    return slide.shapes.add_picture(path, Inches(x), Inches(y), height=Inches(h))
def new(title, source, notes, section=None):
    s = prs.slides.add_slide(BLANK); count["n"] += 1
    tb(s, 0.45, 0.28, 12.4, 1.0, title, size=23, bold=True, color=NAVY, anchor=MSO_ANCHOR.MIDDLE)
    ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(1.3), Inches(12.33), Emu(22000)); ln.fill.solid(); ln.fill.fore_color.rgb = BLUE; ln.line.fill.background()
    tb(s, 0.45, 7.02, 11.6, 0.4, "Source: " + source, size=8.5, color=GREY)
    tb(s, 12.2, 7.02, 0.7, 0.4, (section + " " if section else "") + str(count["n"]), size=9, color=GREY, align=PP_ALIGN.RIGHT)
    s.notes_slide.notes_text_frame.text = notes; return s

# ------------------------------------------------ 1 SUMMARY ------------------------------------------------
s = new(f"LONG Crocs: a 10% free-cash-flow yield retiring a tenth of the shares each year, still priced for a clog bust",
        "Company filings; Nasdaq and Yahoo Finance consensus as of 2026-11-26; model.xlsx (my estimates). Price = Nasdaq close 2026-11-25.",
        f"Opening. I am recommending a long in Crocs with a base-case target of {pt_base:.0f} dollars for December 2027, about {r_base:.0f} percent upside, and a probability-weighted value of {pt_w:.0f}. The one-line thesis: Crocs generates about 750 million dollars of free cash flow, a 10 percent yield, and is using it to retire eight to ten percent of its shares a year. That turns 4 percent revenue growth into mid-teens EPS growth. The stock is on 10 times earnings because the market still fears the clog is a fad. I will be direct about the caveats: the stock has doubled, it is not cheap against Deckers, and the CEO has been selling. The key risk is that the fad unwinds in North America; my stress test puts that at about 52 dollars. So this is a mid-sized position, not a top-five one.")
box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.5), Inches(6.1), Inches(1.55)); box.fill.solid(); box.fill.fore_color.rgb = NAVY; box.line.fill.background()
tb(s, 0.65, 1.55, 5.8, 0.5, f"LONG   |   Target ${pt_base:,.0f} (Dec-2027)   |   {r_base:+.0f}%", size=20, bold=True, color=WHITE)
tb(s, 0.65, 2.1, 5.8, 0.9, f"Probability-weighted ${pt_w:,.0f} ({r_w:+.0f}%)   |   Bear ${pt_bear:,.0f} ({r_bear:+.0f}%)   |   Bull ${pt_bull:,.0f} ({r_bull:+.0f}%)\nHolding period 12-18 months   |   Half size now, add below $140", size=12.5, color=WHITE)
bullets(s, 0.5, 3.2, 6.1, 3.7, [("Thesis.", f"Free cash flow of {m(F['ttm_fcf'])} funds buybacks of about 10% of the shares a year. Revenue +4% becomes EPS +15%. The market pays {F['pe_fy27_cons']:.1f}x FY27 earnings."),
    ("Variant view.", f"FY27E EPS ${e27[1]:.2f} vs consensus $16.01: guidance and the Street exclude buybacks. North America is distorted, not collapsing. International is {F['intl_share_ttm']:.0f}% of the brand."),
    ("Key risk.", f"The clog cycle reverses: {RAR['at_risk_pct']*100:.0f}% of revenue at risk, EPS to ${RAR['eps1']:.2f}, value about ${RAR['val']:.0f}."),
    ("Caveats.", f"Stock +99% in a year; at the mean sell-side target; CEO sold ${F['insider']['ceo_sales_usd']/1e6:.1f}m since June.")], size=12.5)
table(s, [["Market data", ""], ["Share price (25-Nov-2026)", f"${price:.2f}"], ["Market cap / EV", f"${F['mcap']/1000:.1f}bn / ${F['ev']/1000:.1f}bn"], ["P/E FY26 guide / FY27 consensus", f"{F['pe_fy26_guide']:.1f}x / {F['pe_fy27_cons']:.1f}x"], ["P/E on my FY27E EPS", f"{F['pe_fy27_mine']:.1f}x"],
          ["EV / TTM adj. EBITDA", f"{F['ev_ebitda']:.1f}x"], ["FCF yield / buyback yield (TTM)", f"{F['fcf_yield']:.1f}% / {F['buyback_yield']:.1f}%"], ["Net debt / EBITDA", f"{F['nd_ebitda']:.1f}x"], ["52-week range", "$75.13 - $164.24"],
          ["Short interest", f"{F['short']['pct_shares']:.1f}% of shares"], ["Sell-side", "5 Buy / 5 Hold / 1 Sell; mean PT $160.75"]], 6.9, 1.5, 5.95, col_w=[3.2, 2.75], size=11, row_h=0.31)
table(s, [["Key holders (latest filing)", "Shares", "%"], ["BlackRock (13F Sep-26)", "4.52m", "9.9%"], ["FMR (13G Jun-26)", "3.51m", "7.1%"], ["WIT Partners: HEYDUDE founder (13G)", "2.85m", "5.3%"], ["Vanguard Capital Mgmt (13G Mar-26)", "2.57m", "5.1%"], ["Directors and officers (proxy)", "1.59m", "3.1%"]],
      6.9, 5.05, 5.95, col_w=[3.9, 1.0, 1.05], size=10.5, row_h=0.3)

# ------------------------------------------------ 2 WHAT THE COMPANY DOES ------------------------------------------------
s = new("Crocs sells 129m pairs of moulded clogs a year at a 61% gross margin; the Crocs Brand is 82% of revenue and nearly all of the profit",
        "Crocs 10-K FY2025; Q4-2025 earnings call (product mix); Q3-2026 release. FY26E-27E: guidance and my base case.",
        "What the company does, in plain English. Crocs designs a one-piece foam clog, has contract factories in Vietnam and China make it for a few dollars, and sells it for about 50 dollars at retail. Because the shoe is moulded in one piece, gross margin is 61 percent, which is unusual at that price point. Clogs are 74 percent of the Crocs Brand, sandals 13 and the Jibbitz charms 8. The second brand, HEYDUDE, is a US slip-on loafer bought in 2022 for 2.5 billion dollars; it is 18 percent of revenue. Revenue is entirely one-off product sales, split about half direct-to-consumer and half wholesale. No customer is 10 percent of revenue. The chart shows the mix shift that matters: the teal international block keeps growing while North America in blue has been flat to down.")
bullets(s, 0.5, 1.55, 5.5, 5.3, [("Product.", "Moulded foam clogs (74% of Crocs Brand), sandals (13%), Jibbitz charms (8%). HEYDUDE slip-on loafers since 2022."),
    ("How it is paid.", "Per pair. 52% direct-to-consumer (514 stores, 23 websites, marketplaces), 48% wholesale. No subscription or licence revenue; nothing contractual."),
    ("Customers.", "Mass market, $50-60 price points. No customer is 10% of revenue."),
    ("Geography.", f"United States 56% of group revenue. Crocs Brand international is {F['intl_share_ttm']:.0f}% of the brand on a trailing basis."),
    ("Economics.", f"Outsourced manufacturing (45% Vietnam). Gross margin 58%, adj. operating margin 22%, capex under 2% of revenue, free cash flow {F['ttm_fcf']/F['ttm_rev']*100:.0f}% of revenue."),
    ("Scale.", f"FY25 revenue {m(fy(2025)['revenue'])}; 8,010 employees; marketing {m(fy(2025)['marketing'])} ({fy(2025)['marketing_pct_rev']:.1f}% of revenue).")], size=12.5)
pic(s, "01_revenue_mix.png", 6.2, 1.55, w=6.7, max_h=5.3)

# ------------------------------------------------ 3 WHAT DRIVES THE STOCK ------------------------------------------------
s = new("The stock trades on the North America trend and on guidance; EPS itself is most sensitive to margin and to buybacks",
        "model.xlsx sheet Sens (my estimates; assumptions stated in the model); 10-K FY2025 Item 7A; Q4-2025 call (tariff cost); Nasdaq prices.",
        f"What drives the share price. On the company side the market watches Crocs North America, because it is the read on whether the brand is a fad, then international growth, margin and HEYDUDE. On the macro side it is the US lower-income consumer, tariffs, the dollar, oil and rates. The table quantifies each on my FY27 EPS of {e27[1]:.2f} dollars. One percent of revenue is worth about 2.4 percent of EPS because incremental margins are roughly 50 percent. A hundred basis points of margin is worth almost 5 percent. Tariffs, currency and rates are each under 1 percent per unit move. The point of the slide is that the fundamental sensitivities are modest. What makes the stock volatile is the multiple, which has ranged from 4 to 17 times in five years and moves with guidance: the average earnings-day move is 15 percent.")
table(s, [["Driver", "Type", "Change", "FY27E EPS impact", "Basis"],
          ["Group revenue", "Company", "+1%", f"{SN['+1% group revenue'][0]:+.2f} ({SN['+1% group revenue'][1]*100:+.1f}%)", "50% incremental margin (E)"],
          ["Crocs North America revenue", "Company / US consumer", "+1%", f"{SN['+1% Crocs North America revenue'][0]:+.2f} ({SN['+1% Crocs North America revenue'][1]*100:+.1f}%)", "same"],
          ["Crocs International revenue", "Company", "+1%", f"{SN['+1% Crocs International revenue'][0]:+.2f} ({SN['+1% Crocs International revenue'][1]*100:+.1f}%)", "same"],
          ["Adjusted operating margin", "Company", "+100 bps", f"{SN['+100 bps adjusted EBIT margin'][0]:+.2f} ({SN['+100 bps adjusted EBIT margin'][1]*100:+.1f}%)", "mechanical"],
          ["Share repurchases", "Company", "+$100m", f"{SN['+$100m share repurchases (full-year effect)'][0]:+.2f} ({SN['+$100m share repurchases (full-year effect)'][1]*100:+.1f}%)", "at $175 a share"],
          ["US tariff rate on imports", "Macro", "+1 point", f"{SN['+1 pt US tariff rate on imports'][0]:+.2f} ({SN['+1 pt US tariff rate on imports'][1]*100:+.1f}%)", "$80m for the 2025 layer (R)"],
          ["US dollar", "Macro", "+1%", f"{SN['+1% USD vs all currencies'][0]:+.2f} ({SN['+1% USD vs all currencies'][1]*100:+.1f}%)", "35% flow-through (E)"],
          ["Interest rates", "Macro", "+100 bps", f"{SN['+100 bps interest rates'][0]:+.2f} ({SN['+100 bps interest rates'][1]*100:+.1f}%)", "$5.6m per 1% (R)"],
          ["Oil / resin cost", "Macro", "", "not found", "no company disclosure"]], 0.5, 1.55, 7.9, col_w=[2.3, 1.7, 0.9, 1.6, 2.0], size=10.5, row_h=0.42)
bullets(s, 8.7, 1.55, 4.2, 5.3, [("What the market watches.", "1) Crocs North America, 2) international growth, 3) operating margin, 4) HEYDUDE direction, 5) buyback pace."),
    ("Guidance is the trigger.", f"Four of the last eight earnings days moved the stock 19% or more. Average absolute move {F['earn_avg_abs_move']:.0f}%."),
    ("The multiple is the swing factor.", f"Forward P/E has ranged from {RK['CROX_pe_ntm_5y_stats']['min']:.0f}x to {RK['CROX_pe_ntm_5y_stats']['max']:.0f}x in five years; today {RK['crox_pe_ntm_now']:.1f}x."),
    ("Macro.", "Lower-income US consumer, tariffs on Vietnam and China, the dollar (44% of revenue abroad), oil, rates (47% of debt floating).")], size=12)

# ------------------------------------------------ 4 TRACK RECORD ------------------------------------------------
s = new("Revenue stalled and margin fell five points after 2023, yet EPS and cash kept rising because the share count fell by a quarter",
        "Crocs 10-K and Q4 earnings releases FY2021-FY2025 (reported); FY26E from guidance; ratios my calculation.",
        f"Track record. There are two halves. Up to 2021 this was a turnaround: revenue doubled and margin reached 30 percent. Since the HEYDUDE deal in 2022 the operating story has been weaker. Revenue has been about 4 billion for three years. Adjusted operating margin fell from 27.7 percent in 2023 to 22.3 percent in 2025. Gross margin held; the loss is SG&A, which went from 29 to 36 percent of revenue as the mix shifted to direct-to-consumer and the company added people and marketing. Despite that, EPS rose from 12 dollars to about 14.5 this year, and free cash flow has been 650 to 920 million a year, because the diluted share count went from 64 million to under 49 million. The compounding algorithm, growth plus margin plus buybacks, only works when margin stops falling. It stopped falling this year.")
pic(s, "03_eps_fcf_shares.png", 0.5, 1.5, w=7.4, max_h=2.75)
pic(s, "02_margins.png", 0.5, 4.2, w=6.2, max_h=2.75)
table(s, [["", "FY21", "FY23", "FY25", "FY26E"], ["Revenue, $m", f"{fy(2021)['revenue']:,.0f}", f"{fy(2023)['revenue']:,.0f}", f"{fy(2025)['revenue']:,.0f}", f"{B['rev']['FY2026E']:,.0f}"],
          ["Adj. operating margin", f"{fy(2021)['adj_op_margin_pct']:.1f}%", f"{fy(2023)['adj_op_margin_pct']:.1f}%", f"{fy(2025)['adj_op_margin_pct']:.1f}%", f"{B['margin']['FY2026E']*100:.1f}%"],
          ["Adjusted EPS", f"${fy(2021)['adj_eps']:.2f}", f"${fy(2023)['adj_eps']:.2f}", f"${fy(2025)['adj_eps']:.2f}", f"${B['eps']['FY2026E']:.2f}"],
          ["Free cash flow, $m", f"{fy(2021)['fcf']:,.0f}", f"{fy(2023)['fcf']:,.0f}", f"{fy(2025)['fcf']:,.0f}", f"{F['ttm_fcf']:,.0f} (TTM)"],
          ["Net debt / EBITDA", f"{fy(2021)['net_debt_to_adj_ebitda']:.1f}x", f"{fy(2023)['net_debt_to_adj_ebitda']:.1f}x", f"{fy(2025)['net_debt_to_adj_ebitda']:.1f}x", f"{F['nd_ebitda']:.1f}x (Sep)"],
          ["ROIC", f"{fy(2021)['roic_pct']:.0f}%", f"{fy(2023)['roic_pct']:.0f}%", f"{fy(2025)['roic_pct']:.0f}%", ""],
          ["Diluted shares, m", f"{fy(2021)['sh_diluted']:.1f}", f"{fy(2023)['sh_diluted']:.1f}", f"{fy(2025)['sh_diluted']:.1f}", f"{B['sh_avg']['FY2026E']:.1f}"]], 8.1, 1.6, 4.75, col_w=[2.0, 0.9, 0.9, 0.9, 1.15], size=10, row_h=0.33)
bullets(s, 7.0, 4.5, 5.85, 2.4, [("Test of the algorithm.", "FY23-25: revenue +2%, margin -540 bps, shares -13%: EPS +4% in total. It failed while margin fell."),
    ("FY26.", f"Revenue about +3%, margin about +30 bps, shares about -10%: EPS about +16%. Operating income grows only about 5%.")], size=11.5)

# ------------------------------------------------ 5 MOAT ------------------------------------------------
s = new("The moat is cost structure and brand, not patents: copies are legal, so the edge lasts only while the brand stays relevant",
        "Crocs 10-K FY2025 and FY2009; Federal Circuit No. 24-1300 (2026-01-08) and No. 22-2160; Q4-2025 and Q3-2026 earnings calls; Piper Sandler survey via SGB Media.",
        "Moat. I want to be precise here because this is where bulls overstate the case. Crocs does not have a patent moat. The clog patents have expired, and in January 2026 the Federal Circuit left standing a finding that Hobby Lobby and other importers did not infringe the shape trademark. There are no switching costs on a 50 dollar shoe. What Crocs does have is a cost structure rivals cannot match at the price, 61 percent gross margin on a 25 dollar average selling price, and a brand with the scale to spend almost 400 million dollars a year on marketing. Pricing power is real abroad and limited in the US: when discounts were cut in 2025, North America fell 7 percent. The runway is international, where share in the big growth markets is a third of mature levels. I give no weight to management's TAM figure, which went from 160 to 280 billion while revenue was flat.")
table(s, [["Source of edge", "Verdict", "Evidence"],
          ["Patent / legal protection", "No", "Clog patents expired. ITC and Federal Circuit (Jan-2026): active importers do not infringe the 3D clog marks. 'Patented Croslite' claim conceded false."],
          ["Switching cost", "No", "A $50 purchase."], ["Network effect", "Weak", "Jibbitz charms and collaborations create collecting behaviour: 8% of brand revenue."],
          ["Cost structure", "Yes", "One-piece moulded shoe: 61% gross margin at a $25 average selling price. 129m pairs a year."],
          ["Brand", "Yes, cyclical", f"Funds {m(fy(2025)['marketing'])} of marketing. But 2007-09 revenue fell 24% and gross margin fell from 59% to 32%."]], 0.5, 1.55, 7.6, col_w=[1.9, 1.0, 4.7], size=10.5, row_h=0.62)
bullets(s, 8.4, 1.55, 4.5, 5.3, [("Competitors.", "Deckers (UGG clogs, HOKA slides), Birkenstock (Boston clog), Skechers Foamies; unbranded copies online."),
    ("Structure.", "Casual footwear is fragmented. The moulded-clog niche is one brand plus copies. No audited share data found."),
    ("Pricing power.", "ASP $22.27 (FY21) to $25.52 (FY24) with units up. In FY25 ASP -0.5% on discounting; cutting promotions cost 7% of North America revenue."),
    ("Runway.", "US saturated. Share in China, India, Japan, Germany and France is about one-third of established markets (CEO, Feb-2026). China is 8% of sales, +30% in 2025."),
    ("TAM claims.", "Management: $160bn (2023), '$280bn+' (2026). I give these no weight.")], size=11.5)

# ------------------------------------------------ 6 CROCS BRAND ------------------------------------------------
s = new(f"Crocs Brand: international is now over half of sales and growing 12%, while North America is still shrinking 2%",
        "Crocs earnings releases and 10-Ks (reported); Q3-2026 call for underlying DTC and the marketplace shift. FY27E is my base case; segment consensus not found.",
        "The Crocs Brand, 82 percent of revenue. The left chart is the story. International, in teal, has grown between 6 and 18 percent in every one of the last eight quarters. North America, in blue, has been negative in six of the last seven. International crossed 50 percent of the brand this year, from 33 percent in 2021. Management's explanation for North America is that it cut promotions from May 2025 and reduced what it ships to wholesale, to protect the price of the Classic Clog. There is some support for that: North America direct-to-consumer grew 5 percent in the first half. But from Q3 a marketplace partner moved from direct to wholesale accounting, which takes 7 to 8 points off reported DTC growth each quarter until Q3 2027. So the clean number is hidden for a year. Segment margin is 33 percent, down from 37, entirely because of SG&A. My base case has North America flat and international growing 9 percent in 2027.")
pic(s, "04_crocs_brand.png", 0.5, 1.5, w=7.6, max_h=3.0)
table(s, [["Crocs Brand", "FY21", "FY23", "FY25", "FY26 (G)", "FY27 (E)"], ["Revenue, $m", f"{fy(2021)['crocs_rev']:,.0f}", f"{fy(2023)['crocs_rev']:,.0f}", f"{fy(2025)['crocs_rev']:,.0f}", f"~{B['crocs']['FY2026E']:,.0f}", f"{B['crocs']['FY2027E']:,.0f}"],
          ["Growth", "+67%", "+13%", "+1.5%", "~+4%", f"{(B['crocs']['FY2027E']/B['crocs']['FY2026E']-1)*100:+.1f}%"],
          ["Segment margin", f"{fy(2021)['crocs_op_margin_pct']:.1f}%", f"{fy(2023)['crocs_op_margin_pct']:.1f}%", f"{fy(2025)['crocs_op_margin_pct']:.1f}%", "33.8% (9M)", ""],
          ["Pairs, m / ASP", "103 / $22.27", "120 / $24.92", "129 / $25.40", "", ""]], 0.5, 4.65, 7.6, col_w=[1.7, 1.1, 1.1, 1.1, 1.3, 1.3], size=10.5, row_h=0.36)
bullets(s, 8.4, 1.55, 4.5, 5.3, [("What it sells.", "Clogs 74%, sandals 13% (about $450m, double-digit growth), Jibbitz 8%. DTC 52% of the brand."),
    ("Growth drivers.", "International +11% in 2025 on +19%; China +30% on +64%; international DTC +24% in Q3-26."),
    ("Margins.", "Gross margin 61%. Segment SG&A +27% in two years on revenue +10%: DTC mix, talent, marketing. Q3-26: lower duties +130 bps, product mix -130 bps."),
    ("North America.", "FY25 -6.8%; Q3-26 -2.1% (wholesale -4.9%). DTC ex accounting shift about +2%."),
    ("Risks.", "Teen rank No. 6 (2023) to No. 10 (2026). Two factories make 73% of volume. Newer products carry lower margins.")], size=11.5)

# ------------------------------------------------ 7 HEYDUDE ------------------------------------------------
s = new("HEYDUDE: a $2.5bn acquisition that lost a quarter of its revenue; it has stopped shrinking and only needs to stay flat",
        "Crocs 10-Ks, 10-Qs and earnings releases (reported); acquisition press releases 2021-12-23 and 2022-02-17; 10-Q Q2-2025 (impairment); Q3-2026 call.",
        "HEYDUDE, 18 percent of revenue. This is the capital allocation mistake. Crocs paid 2.5 billion dollars in February 2022, 2.05 billion in cash funded by a term loan and 450 million in stock. Revenue peaked at 949 million in 2023 after wholesale customers were loaded with inventory, then fell 25 percent in two years. Wholesale fell 41 percent. Segment margin went from 24 percent to under 10. Crocs wrote off 737 million in mid-2025. Five of the six big falls in the share price since 2021 were HEYDUDE guide-downs. What has changed: wholesale grew 14 percent in Q3, the first growth in three years, and gross margin recovered 350 basis points. The CEO was candid that this is against a weak comparison and that the sustainable rate is low to mid single digits. I do not need HEYDUDE to recover. At 17 percent of revenue and already written down, I need it to stop producing negative surprises. My base case is plus 4 percent in 2027.")
pic(s, "06_heydude.png", 0.5, 1.5, w=7.7, max_h=3.1)
table(s, [["HEYDUDE", "FY22*", "FY23", "FY24", "FY25", "FY26 (G)", "FY27 (E)"], ["Revenue, $m", "896", "949", "824", "715", "~715", f"{B['hd']['FY2027E']:,.0f}"], ["Growth", "n/a", "+6.0%", "-13.2%", "-13.3%", "~flat", "+4%"],
          ["Gross margin", "40.8%", "44.0%", "47.7%", "44.8%", "44.6% (9M adj.)", ""], ["Segment margin ex-impairment", f"{fy(2022)['hd_op_margin_ex_impair_pct']:.1f}%", f"{fy(2023)['hd_op_margin_ex_impair_pct']:.1f}%", f"{fy(2024)['hd_op_margin_ex_impair_pct']:.1f}%", f"{fy(2025)['hd_op_margin_ex_impair_pct']:.1f}%", "12.3% (9M)", ""]],
      0.5, 4.75, 7.7, col_w=[2.3, 0.8, 0.8, 0.8, 0.8, 1.3, 0.9], size=10.5, row_h=0.36)
bullets(s, 8.5, 1.55, 4.4, 5.3, [("What it sells.", "Wally and Wendy slip-on loafers, about $32 a pair, almost all in the US. 55% DTC (75 outlets, Amazon), 45% wholesale."),
    ("The deal.", "$2.5bn: $2.05bn cash + $450m stock (2.85m shares, still held by the founder). $737m written off in Q2-25."),
    ("Now.", "Q3-26 revenue +6.1%, wholesale +14.0%, adj. gross margin 45.8% (+350 bps). Q4 guide +10-12%."),
    ("Management view.", "'We are up against a weak compare' (CEO, Oct-2026). Sustainable growth low- to mid-single digits."),
    ("Risks.", "Fourth leader in four years. Off the teen top-ten list. Class action over 2022-24 wholesale inventory.")], size=11.5)
tb(s, 0.5, 6.62, 7.7, 0.3, "*FY22 from acquisition close on 17-Feb-2022.", size=9, color=GREY)

# ------------------------------------------------ 8 KEY RISK + PROPRIETARY ------------------------------------------------
s = new(f"Key risk: {RAR['at_risk_pct']*100:.0f}% of revenue is exposed to a clog-cycle reversal, concentrated in North America clogs, Jibbitz and China",
        "TTM revenue from Crocs releases (reported); FY2025 product mix from Q4-2025 call; 10-K FY2009 for the precedent. Scores and haircuts are my assumptions (model.xlsx RevAtRisk).",
        f"The key risk and my own analysis of it. The debate is whether the clog is a fad. Rather than argue it qualitatively, I split the last twelve months of revenue into nine lines and scored each from 1 to 5 for exposure to a reversal in clog demand. North America wholesale clogs and Jibbitz get a 5: they are already declining, retailers control the shelf, and charms are a pure derivative of clog heat. North America direct clogs, China and HEYDUDE wholesale get a 4. International clogs get a 3 because penetration is low. Sandals get a 2. Each score maps to a two-year revenue decline; a 5 is 30 percent, calibrated to Crocs' own 2007 to 2009 bust, minus 24 percent, and to HEYDUDE, minus 25 percent. The answer is {RAR['at_risk_pct']*100:.1f} percent of group revenue, about {RAR['at_risk']:.0f} million dollars. The revenue figures are reported; the product split within each region and all the scores are my judgement, and I test them on the next slide.")
pic(s, "12_revenue_at_risk.png", 0.5, 1.5, w=7.9, max_h=5.4)
bullets(s, 8.6, 1.55, 4.3, 5.3, [("The debate.", "Fad unwinding in its home market, or durable franchise in a deliberate reset?"),
    ("Method.", "Nine revenue lines, scored 1-5 for exposure to falling clog demand. Score maps to a 2-year decline: 0 / 5 / 12 / 20 / 30%."),
    ("Calibration.", "Crocs 2007-09: revenue -24%. HEYDUDE 2023-25: -25% (wholesale -41%). Crocs North America FY25: -7%."),
    ("Sourced.", "Revenue by brand, region, channel; FY25 product mix 74/13/8; China about 8% of sales."),
    ("My assumptions.", "The scores; the haircut map; the same product mix in every region."),
    ("Result.", f"{m(RAR['at_risk'])} of {m(RAR['at_risk']/RAR['at_risk_pct'])} at risk = {RAR['at_risk_pct']*100:.1f}%.")], size=11.5)

# ------------------------------------------------ 9 STRESS TEST ------------------------------------------------
s = new(f"A full fad unwind would halve EPS to about ${RAR['eps1']:.0f}; the price implies roughly a 40% chance of my milder bear case, and I put it at 25%",
        "model.xlsx sheets RevAtRisk and Valuation; scripts/10_revenue_at_risk.py (Monte Carlo). Consensus FY27E EPS $16.01: Yahoo Finance, 2026-11-26.",
        f"Stress test. I run the lost revenue through the cost structure. I assume half of distribution cost and 65 percent of SG&A are fixed and add 150 basis points of markdown pressure. EBITDA falls from {RAR['ebitda0']:.0f} to {RAR['ebitda1']:.0f} million. At an 18 percent tax rate and today's share count, EPS goes from {RAR['eps0']:.2f} to {RAR['eps1']:.2f}, which is {abs(RAR['vs_cons'])*100:.0f} percent below consensus for 2027. Consensus has none of this in it. On the right is the sensitivity to my own scoring: if every score is independently wrong by one notch, stressed EPS still lands between about 6 and 9 dollars. So the answer does not depend on my scores; it depends on whether the unwind happens. At 7 times, the stressed value is about {RAR['val']:.0f} dollars. In March the stock traded at 76, pricing nearly all of this. Today, reconciling my three scenario targets with the price implies about a 40 percent chance of my bear case. I think 25 percent is right. So the fear is still over-priced, but the gap is modest.")
pic(s, "13_stress_eps.png", 0.5, 1.5, w=7.9, max_h=3.3)
table(s, [["", "TTM base", "Stressed", "Change"], ["Revenue, $m", f"{RAR['at_risk']/RAR['at_risk_pct']:,.0f}", f"{RAR['rev1']:,.0f}", f"-{RAR['at_risk_pct']*100:.1f}%"], ["Adj. EBITDA, $m", f"{RAR['ebitda0']:,.0f}", f"{RAR['ebitda1']:,.0f}", f"{(RAR['ebitda1']/RAR['ebitda0']-1)*100:.0f}%"],
          ["EPS at today's shares (18% tax)", f"${RAR['eps0']:.2f}", f"${RAR['eps1']:.2f}", f"{(RAR['eps1']/RAR['eps0']-1)*100:.0f}%"], ["vs consensus FY27E $16.01", "", f"{RAR['vs_cons']*100:.0f}%", ""], ["Value at 7x trough P/E", "", f"${RAR['val']:.0f}", f"{RAR['val_vs_px']*100:.0f}% vs price"]],
      0.5, 4.95, 7.9, col_w=[3.2, 1.5, 1.5, 1.7], size=10.5, row_h=0.32)
bullets(s, 8.6, 1.55, 4.3, 5.3, [("Cost assumptions (mine).", f"50% of distribution cost fixed; 65% of SG&A fixed; +150 bps markdowns. Decremental margin {RAR['decr']*100:.0f}%."),
    ("Score sensitivity.", f"All scores -1 / +1: revenue at risk {RAR['minus1_pct']*100:.0f}% / {RAR['plus1_pct']*100:.0f}%, EPS ${RAR['minus1_eps']:.2f} / ${RAR['plus1_eps']:.2f}."),
    ("Monte Carlo.", f"5th-95th percentile EPS ${F['rar_mc']['eps_p5_p50_p95'][0]:.2f} - ${F['rar_mc']['eps_p5_p50_p95'][2]:.2f}."),
    ("Then.", f"March 2026 low of $75.78 was 6.1x trailing EPS, {(75.78/RAR['val']-1)*100:.0f}% above the full-unwind value: fear over-priced."),
    ("Now.", f"Price implies about {K['Market-implied probability of the bear case (base:bull 2:1)']*100:.0f}% probability of my bear case (${pt_bear:.0f}). My estimate: 25%. Still over-priced, modestly.")], size=11.5)

# ------------------------------------------------ 10 HOW THE COMPANY IS ADAPTING ------------------------------------------------
s = new("Management's response shows up in hard revenue abroad and in the share count; in North America it is still mostly activity metrics",
        "Crocs earnings releases and 10-Q Q3-2026 (hard figures); earnings call transcripts Q3-2025 to Q3-2026 (management statements); Piper Sandler via TIKR (TikTok share).",
        "How the company is adapting. I separate what shows up in reported revenue from what is only an activity metric. Left column is hard evidence. Sandals are about 450 million dollars and growing double digits. International is up 8.8 percent in nine months and international direct-to-consumer is up 25 percent. Adjusted gross margin rose 180 basis points in Q3 after the promotion pull-back. HEYDUDE wholesale grew 14 percent. Adjusted SG&A grew 3 percent, with 150 million of cost savings. And the company has retired 10.9 million shares since January 2025. Right column is what management talks about that I cannot verify in the numbers: TikTok Shop rankings, collaborations selling out, campaign impressions, and the claim that it is outselling its inventory in the wholesale channel. The evidence is strong abroad and in capital return, moderate for HEYDUDE, which has one good quarter against an easy comparison, and weakest for North America.")
table(s, [["Response", "Hard revenue or financial evidence (reported)", "Activity metrics only (management statements)"],
          ["Diversify beyond the Classic Clog", "Sandals 13% of the brand, about $450m in FY25, growing double digits; aim about $0.5bn in 2026", "New franchises (Echo, Crafted, recovery clog, ballet flats). 2026 mix not disclosed"],
          ["Grow outside North America", "International +8.8% in 9M-26 ($1,398m vs $1,284m); international DTC +25%", "63 store openings in 2025; China campaign '40 billion impressions'"],
          ["Protect price", "Adjusted gross margin +180 bps y/y in Q3-26", "'Many more days that were non-promotional'"],
          ["Social commerce", "TikTok Shop about 3% of Crocs Brand revenue in 2026 (Piper Sandler estimate)", "No. 1 footwear brand on TikTok Shop in the US, UK, Japan, Malaysia"],
          ["Fix HEYDUDE", "Q3-26 revenue +6.1%; wholesale +14.0%; adj. gross margin +350 bps", "Eight collaborations in Q3, 'each one selling out'; 'we are outselling our inventory in the channel'"],
          ["Cut cost", "$150m of savings in 2025-26; adjusted SG&A +3.1% in 9M-26", ""],
          ["Shrink the equity", "10.9m shares retired since Jan-2025 for $1.08bn; diluted shares 54.0m to 48.0m in a year", ""]], 0.5, 1.55, 12.35, col_w=[2.5, 5.2, 4.65], size=11, row_h=0.6)
tb(s, 0.5, 6.45, 12.3, 0.5, "Read: evidence is strongest for international and capital return, moderate for HEYDUDE (one quarter, easy comparison), weakest for North America.", size=12.5, bold=True, color=NAVY)

# ------------------------------------------------ 11 SHARE PRICE HISTORY ------------------------------------------------
s = new("Every large move in five years was an earnings or guidance event, and five of the six big falls were about HEYDUDE",
        "Nasdaq daily closes; Crocs press releases on the dates shown (8-K exhibits). Moves are close-to-close.",
        "Share price history. The stock is roughly where it was five years ago, having fallen 74 percent and tripled in between. Every numbered move is an earnings or guidance event. Read the red ones: December 2021, the HEYDUDE deal is announced, minus 12 percent. July 2023, HEYDUDE growth guide cut. October 2024, HEYDUDE guide cut again, minus 19. August 2025, the HEYDUDE impairment and a guide-down, minus 29. Five of the six big falls trace to HEYDUDE. The green ones are beats and guidance raises on the core brand. Two implications. First, this is a guidance stock; you have to have a view on the next guide, which is why the February 2027 print matters. Second, the source of most past negative surprises, HEYDUDE, is now 17 percent of revenue, written down, and growing against easy comparisons. That does not remove the risk, but it changes where the next surprise is likely to come from: North America clogs.")
pic(s, "07_price_5y.png", 0.5, 1.5, w=7.7, max_h=5.4)
table(s, [["#", "Date", "Move", "Cause"], ["1", "23-Dec-21", "-11.6%", "$2.5bn HEYDUDE deal announced"], ["2", "17-Jun-22", "low $47", "Bear market; leverage 2.1x; -74% from peak"], ["3", "3-Nov-22", "+14.2%", "Q3-22 beat; HEYDUDE guided above $1bn"],
          ["4", "27-Apr-23", "-15.9%", "Soft Q2 EPS guide despite full-year raise"], ["5", "27-Jul-23", "-14.6%", "HEYDUDE growth guide cut to 14-18%"], ["6", "8-Jan-24", "+20.3%", "Pre-announced record 2023"],
          ["7", "29-Oct-24", "-19.2%", "HEYDUDE 2024 guide cut to -14.5%"], ["8", "13-Feb-25", "+23.9%", "Q4-24 beat; 2025 guide above consensus"], ["9", "7-Aug-25", "-29.2%", "$737m impairment; Q3 guided -9% to -11%"],
          ["10", "12-Feb-26", "+19.0%", "Q4-25 beat; 2026 EPS guide well above consensus"], ["11", "29-Oct-26", "+25.5%", "Q3-26 beat; third raise; HEYDUDE grows"]], 8.4, 1.5, 4.5, col_w=[0.35, 0.95, 0.8, 2.4], size=9.5, row_h=0.43)

# ------------------------------------------------ 12 VALUATION VS PEERS & HISTORY ------------------------------------------------
s = new("Valuation: no longer cheap against Deckers or its own history, but still 45% below the market with a 10% free-cash-flow yield",
        "StockAnalysis.com at 2026-11-25 (peer multiples); my P/E series from Nasdaq prices and reported EPS (Macrotrends not accessible); FactSet Earnings Insight 13-Nov-2026 (S&P 500 18.3x).",
        f"Valuation against peers and history. I picked Deckers, Birkenstock and On: brand-led footwear companies with icon franchises and 57 to 67 percent gross margins. Skechers went private. Three honest observations. One, against Deckers, the closest peer, Crocs is no longer cheap: forward P/E {pk('CROX','pe_fwd'):.1f} against {pk('DECK','pe_fwd'):.1f}, and a premium on EV to EBITDA. For five years Crocs traded at about half of Deckers' multiple. That gap closed from both ends: Deckers de-rated from 32 times to 11 and Crocs re-rated from 6 to 10. Two, on a value to growth score, price to sales over revenue growth, Crocs is the worst of the four, because it barely grows. This is cash at a discount, not growth at a discount. Three, against its own history Crocs is at the 76th percentile. So I am not arguing for multiple expansion, and I would not run this as a pair against Deckers. The case is absolute: a 10 percent free cash flow yield at a 45 percent discount to the market multiple.")
pic(s, "08_pe_history.png", 0.5, 1.5, w=7.2, max_h=2.75)
pic(s, "10_peers.png", 0.5, 4.3, w=7.2, max_h=2.6)
table(s, [["", "CROX", "DECK", "BIRK", "ONON"], ["P/S TTM / forward", f"{pk('CROX','ps_ttm'):.2f} / {pk('CROX','ps_fwd'):.2f}", f"{pk('DECK','ps_ttm'):.2f} / {pk('DECK','ps_fwd'):.2f}", f"{pk('BIRK','ps_ttm'):.2f} / {pk('BIRK','ps_fwd'):.2f}", f"{pk('ONON','ps_ttm'):.2f} / {pk('ONON','ps_fwd'):.2f}"],
          ["P/FCF", f"{pk('CROX','p_fcf'):.1f}", f"{pk('DECK','p_fcf'):.1f}", f"{pk('BIRK','p_fcf'):.1f}", f"{pk('ONON','p_fcf'):.1f}"], ["EV/EBITDA", f"{pk('CROX','ev_ebitda'):.1f}", f"{pk('DECK','ev_ebitda'):.1f}", f"{pk('BIRK','ev_ebitda'):.1f}", f"{pk('ONON','ev_ebitda'):.1f}"],
          ["Forward P/E", f"{pk('CROX','pe_fwd'):.1f}", f"{pk('DECK','pe_fwd'):.1f}", f"{pk('BIRK','pe_fwd'):.1f}", f"{pk('ONON','pe_fwd'):.1f}"], ["Gross / operating margin", f"{pk('CROX','gross_margin_pct'):.0f}% / {pk('CROX','op_margin_pct'):.0f}%", f"{pk('DECK','gross_margin_pct'):.0f}% / {pk('DECK','op_margin_pct'):.0f}%", f"{pk('BIRK','gross_margin_pct'):.0f}% / {pk('BIRK','op_margin_pct'):.0f}%", f"{pk('ONON','gross_margin_pct'):.0f}% / {pk('ONON','op_margin_pct'):.0f}%"],
          ["Revenue growth TTM", f"{pk('CROX','rev_growth_ttm_pct'):.1f}%", f"{pk('DECK','rev_growth_ttm_pct'):.1f}%", f"{pk('BIRK','rev_growth_ttm_pct'):.1f}%", f"{pk('ONON','rev_growth_ttm_pct'):.1f}%"],
          ["Value/Growth score", f"{pk('CROX','value_growth_score_ttm'):.2f}", f"{pk('DECK','value_growth_score_ttm'):.2f}", f"{pk('BIRK','value_growth_score_ttm'):.2f}", f"{pk('ONON','value_growth_score_ttm'):.2f}"],
          ["Net debt / EBITDA", f"{pk('CROX','net_debt_to_ebitda'):.1f}x", "net cash", f"{pk('BIRK','net_debt_to_ebitda'):.1f}x", "net cash"], ["ROIC", f"{pk('CROX','roic_pct'):.0f}%", f"{pk('DECK','roic_pct'):.0f}%", f"{pk('BIRK','roic_pct'):.0f}%", f"{pk('ONON','roic_pct'):.0f}%"],
          ["FCF margin", f"{pk('CROX','fcf_margin_pct'):.0f}%", f"{pk('DECK','fcf_margin_pct'):.0f}%", f"{pk('BIRK','fcf_margin_pct'):.0f}%", f"{pk('ONON','fcf_margin_pct'):.0f}%"]], 7.95, 1.5, 4.95, col_w=[1.75, 0.8, 0.8, 0.8, 0.8], size=9.5, row_h=0.3)
bullets(s, 7.95, 4.95, 4.95, 2.0, [("Gap to Deckers.", f"5-year median discount {abs(RK['CROX_vs_DECK_ntm_prem_pct_5y_stats']['median']):.0f}%; now {abs((RK['crox_pe_ntm_now']/RK['deck_pe_ntm_now']-1)*100):.0f}%. Closed from both ends. If it reopens, more likely by Crocs falling."),
    ("Own history.", f"{RK['crox_pe_ntm_now']:.1f}x vs 5-year median {RK['CROX_pe_ntm_5y_stats']['median']:.1f}x: {RK['CROX_pe_ntm_5y_stats']['pctile_now']:.0f}th percentile."), ("Index.", "S&P 500 18.3x forward (10-year average 19.1x).")], size=10.5, gap=3)

# ------------------------------------------------ 13 CATALYSTS ------------------------------------------------
s = new("Catalysts: the FY2027 guide in February and the Q3 2027 lapping of the accounting shift are the two events that settle the debate",
        "Company guidance 2026-10-29; Yahoo consensus 2026-11-26; 10-Q Q3-2026 (debt, refunds, authorisation); USTR; model.xlsx. Probabilities are my estimates. Q4 date is Yahoo's estimate, not confirmed.",
        f"Catalysts, all inside a 12 to 18 month holding period. The first that matters is the Q4 report, expected around the 11th of February, with the first 2027 guide. Consensus is {16.01} dollars. Crocs guides excluding buybacks; on my numbers that is still about {e27[1] + SN['No buybacks at all in FY27 (cash retained)'][0]:.2f}, so I see a 60 percent chance the midpoint is at or above 16. Then two awkward quarters, Q1 and Q2 2027, where reported North America direct-to-consumer will look like minus 5 even if the underlying is plus 2, because of the marketplace accounting change. The second key event is Q3 2027 in late October, when that is lapped and we get a clean number. Running underneath all of it are the buybacks: 1.7 billion dollars authorised, 23 percent of the market cap, and not in guidance or consensus. Tariff litigation is a two-way option worth about 8 cents of EPS per point. The revolver needs refinancing by November 2027; with 113 million drawn that is routine.")
table(s, [["Window", "Catalyst", "Mechanism", "Size in numbers", "Probability (E)", "In period?"],
          ["1-Dec-2026", "Morgan Stanley conference", "First holiday read vs Q4 guide of +7-9%", "Q4 revenue guide about $1,034m", "50% it moves the stock", "Yes"],
          ["~11-Feb-2027", "Q4-26 results; first FY27 guide", "EPS guide vs consensus; guide excludes buybacks", f"Consensus $16.01; mine ${e27[1]:.2f}; ex-buyback ${e27[1] + SN['No buybacks at all in FY27 (cash retained)'][0]:.2f}", "60% midpoint at or above $16.0", "Yes"],
          ["Apr / Jul 2027", "Q1-27, Q2-27 results", "Worst North America optics: 700-800 bps accounting drag", "Reported NA DTC about -5% if underlying +2%", "40% market looks through", "Yes"],
          ["Late Oct-2027", "Q3-27 results", "Accounting shift lapped: clean North America number", "GAAP also laps $64m of refunds", "55% NA DTC positive", "Yes"],
          ["Continuous", "Buybacks", "Not in guidance or consensus", f"$1.7bn authorised = {1700/F['mcap']*100:.0f}% of market cap; base {m(B['bb']['FY2027E'])} in FY27", "85% above $500m", "Yes"],
          ["Open-ended", "Section 301 tariffs (10-12.5%)", "Court challenge; rate changes", f"About $4m and ${abs(SN['+1 pt US tariff rate on imports'][0]):.2f} EPS per point", "20% removed; 20% raised", "Possibly"],
          ["By Nov-2027", "Revolver refinancing", "$1.0bn facility matures", "$113m drawn", "90% routine", "Yes"],
          ["Open-ended", "Class action: motion to dismiss", "Removes or extends an overhang", "Damages not quantified; $0.6m accrued", "50% dismissed", "Possibly"],
          ["~Oct-2027", "Piper Sandler teen survey", "Crocs is No. 10; could drop out", "Stock fell 3% on the Spring 2024 survey", "40% drops out", "Yes"]], 0.5, 1.55, 12.35, col_w=[1.2, 2.1, 2.9, 3.2, 1.9, 0.9], size=10, row_h=0.52)

# ------------------------------------------------ 14 FINANCIALS ------------------------------------------------
s = new(f"Financials: 4% revenue growth and flat margins compound EPS at about 15% a year because buybacks retire 7-8% of the shares annually",
        "FY23-FY25 reported (10-K, earnings releases); FY26E on company guidance; FY27E-28E my base case (model.xlsx sheet Base). Consensus: Yahoo / Nasdaq, 2026-11-26.",
        f"Financials and forecast. Base case. Revenue grows about 4 percent a year: North America flat, international 8 to 9 percent, HEYDUDE 3 to 4. I hold margin at about 23 percent; lower tariffs and the cost programme offset the lower-margin product mix and oil. Free cash flow is about 700 million dollars after treating stock compensation as a cash cost, and 85 percent of it goes to buybacks, which keeps leverage falling below one times. The share count falls from 48.7 million to 41 million by 2028. EPS goes from 14.54 to {e27[1]:.2f} to {e28[1]:.2f}. The bridge on the right shows where the growth comes from between 2026 and 2028: about 1.5 dollars from revenue, 60 cents from margin and interest, and more than 3 dollars from buybacks. I am 8 percent above consensus for 2027, and almost all of that gap is share count. Even with zero buybacks in 2027 my number would be 16.6 against 16.0.")
rows = [["$m", "FY23", "FY24", "FY25", "FY26E", "FY27E", "FY28E"],
        ["Revenue", f"{fy(2023)['revenue']:,.0f}", f"{fy(2024)['revenue']:,.0f}", f"{fy(2025)['revenue']:,.0f}", f"{B['rev']['FY2026E']:,.0f}", f"{B['rev']['FY2027E']:,.0f}", f"{B['rev']['FY2028E']:,.0f}"],
        ["Growth", f"{fy(2023)['rev_growth_pct']:+.1f}%", f"{fy(2024)['rev_growth_pct']:+.1f}%", f"{fy(2025)['rev_growth_pct']:+.1f}%", f"{B['g']['FY2026E']*100:+.1f}%", f"{B['g']['FY2027E']*100:+.1f}%", f"{B['g']['FY2028E']*100:+.1f}%"],
        ["Adj. gross margin", f"{fy(2023)['adj_gm_pct']:.1f}%", f"{fy(2024)['adj_gm_pct']:.1f}%", f"{fy(2025)['adj_gm_pct']:.1f}%", "up slightly (G)", "", ""],
        ["Adj. EBIT", f"{fy(2023)['adj_op_income']:,.0f}", f"{fy(2024)['adj_op_income']:,.0f}", f"{fy(2025)['adj_op_income']:,.0f}", f"{B['ebit']['FY2026E']:,.0f}", f"{B['ebit']['FY2027E']:,.0f}", f"{B['ebit']['FY2028E']:,.0f}"],
        ["Adj. EBIT margin", f"{fy(2023)['adj_op_margin_pct']:.1f}%", f"{fy(2024)['adj_op_margin_pct']:.1f}%", f"{fy(2025)['adj_op_margin_pct']:.1f}%", f"{B['margin']['FY2026E']*100:.1f}%", f"{B['margin']['FY2027E']*100:.1f}%", f"{B['margin']['FY2028E']*100:.1f}%"],
        ["Free cash flow", f"{fy(2023)['fcf']:,.0f}", f"{fy(2024)['fcf']:,.0f}", f"{fy(2025)['fcf']:,.0f}", f"{F['ttm_fcf']:,.0f} (TTM)", f"{B['fcf']['FY2027E']:,.0f}", f"{B['fcf']['FY2028E']:,.0f}"],
        ["Buybacks", f"{fy(2023)['buybacks']:,.0f}", f"{fy(2024)['buybacks']:,.0f}", f"{fy(2025)['buybacks']:,.0f}", f"{F['ttm_buyback']:,.0f} (TTM)", f"{B['bb']['FY2027E']:,.0f}", f"{B['bb']['FY2028E']:,.0f}"],
        ["Diluted shares, m", f"{fy(2023)['sh_diluted']:.1f}", f"{fy(2024)['sh_diluted']:.1f}", f"{fy(2025)['sh_diluted']:.1f}", f"{B['sh_avg']['FY2026E']:.1f}", f"{B['sh_avg']['FY2027E']:.1f}", f"{B['sh_avg']['FY2028E']:.1f}"],
        ["Adjusted EPS", f"${fy(2023)['adj_eps']:.2f}", f"${fy(2024)['adj_eps']:.2f}", f"${fy(2025)['adj_eps']:.2f}", f"${B['eps']['FY2026E']:.2f}", f"${B['eps']['FY2027E']:.2f}", f"${B['eps']['FY2028E']:.2f}"],
        ["Consensus EPS", "", "", "", "$14.63", "$16.01 / $15.85", "$16.69 (1 est.)"],
        ["Net debt / EBITDA", f"{fy(2023)['net_debt_to_adj_ebitda']:.1f}x", f"{fy(2024)['net_debt_to_adj_ebitda']:.1f}x", f"{fy(2025)['net_debt_to_adj_ebitda']:.1f}x", f"{B['lev']['FY2026E']:.1f}x", f"{B['lev']['FY2027E']:.1f}x", f"{B['lev']['FY2028E']:.1f}x"],
        ["Stock comp % revenue", f"{fy(2023)['sbc_pct_rev']:.1f}%", f"{fy(2024)['sbc_pct_rev']:.1f}%", f"{fy(2025)['sbc_pct_rev']:.1f}%", "1.1% (TTM)", "", ""]]
table(s, rows, 0.5, 1.55, 7.5, col_w=[1.9, 0.9, 0.9, 0.9, 1.15, 1.15, 1.05], size=10, row_h=0.36)
pic(s, "16_eps_bridge.png", 8.2, 1.5, w=4.75, max_h=2.9)
bullets(s, 8.2, 4.45, 4.7, 2.5, [("Assumptions (base).", "North America 0% then +1%; international +9% fading to +5%; HEYDUDE +4% to +2%; margin 22.8-23.0%; buybacks 85% of FCF at $175 then $190."),
    ("vs consensus.", f"FY27E EPS {V['vs_cons'][1]*100:+.0f}%. With zero FY27 buybacks: ${e27[1] + SN['No buybacks at all in FY27 (cash retained)'][0]:.2f}."),
    ("Quality.", f"FCF {F['ttm_fcf_conv']:.0f}% of adjusted net income (TTM). Non-GAAP tax 18% vs 23% GAAP.")], size=10.5, gap=3)

# ------------------------------------------------ 15 CONCLUSION ------------------------------------------------
s = new(f"Conclusion: long at half size now, add below $140. Target ${pt_base:,.0f}, expected return {r_w:+.0f}%, with explicit kill criteria",
        "model.xlsx sheets Valuation, Bear, Base, Bull (my estimates); sell-side targets from Nasdaq 2026-11-26.",
        f"Conclusion. Base case {pt_base:.0f} dollars, {r_base:.0f} percent upside by December 2027, at ten and a half times 2028 earnings, which is roughly today's multiple on consensus. Bull {pt_bull:.0f}. Bear {pt_bear:.0f}, down {abs(r_bear):.0f} percent. Weighted 25, 50, 25, the expected value is {pt_w:.0f}, a {r_w:.0f} percent expected return. I want to be straight about the shape: base upside against bear downside is only 0.7 to 1. The trade works because I think the bear is a one in four outcome, not because the downside is small. The expected return only goes to zero if the bear probability is above 50 percent. So: a mid-sized long, half now because the stock is up 34 percent in a month, the rest below 140. I exit if North America direct-to-consumer excluding the accounting shift is negative for two quarters, if international growth drops below 5 percent for two quarters, if the 2027 margin guide is below 21.5 percent, or on a large acquisition. Three things I would ask you to check yourself are on the right.")
pic(s, "14_valuation_range.png", 0.5, 1.5, w=6.6, max_h=3.1)
table(s, [["", "Bear", "Base", "Bull", "Weighted"], ["Probability", "25%", "50%", "25%", ""], ["FY28E EPS", f"${e28[0]:.2f}", f"${e28[1]:.2f}", f"${e28[2]:.2f}", f"${e28[3]:.2f}"], ["Exit P/E", "7.0x", "10.5x", "13.0x", ""],
          ["Price target Dec-2027", f"${pt_bear:,.0f}", f"${pt_base:,.0f}", f"${pt_bull:,.0f}", f"${pt_w:,.0f}"], ["Return", f"{r_bear:+.0f}%", f"{r_base:+.0f}%", f"{r_bull:+.0f}%", f"{r_w:+.0f}%"], ["DCF per share", f"${dcf[0]:,.0f}", f"${dcf[1]:,.0f}", f"${dcf[2]:,.0f}", f"${dcf[3]:,.0f}"]],
      0.5, 4.7, 6.6, col_w=[2.2, 1.1, 1.1, 1.1, 1.1], size=10.5, row_h=0.31)
bullets(s, 7.4, 1.55, 5.5, 2.5, [("Three pillars.", "1) Capital return does the work. 2) International offsets North America. 3) The earnings base has stopped shrinking."),
    ("Skew.", f"Base vs bear {K['Upside/downside ratio, base vs bear (x)']:.2f}x; probability-weighted {K['Upside/downside ratio, probability-weighted (x)']:.1f}x. Break-even bear probability {K['Break-even bear probability (EV = 0, base:bull kept 2:1)']*100:.0f}%."),
    ("Sizing.", f"Mid-sized. Half now; add below $140 (expected return about {(pt_w/140-1)*100:.0f}%). Plan for -25-30% in a 20% market fall.")], size=11.5, gap=4)
tb(s, 7.4, 3.75, 5.5, 0.3, "Kill criteria", size=12.5, bold=True, color=RED)
bullets(s, 7.4, 4.05, 5.5, 1.5, ["North America DTC ex-shift negative for two quarters", "International growth below 5% for two quarters", "FY27 margin guide below 21.5%; or acquisition above $500m; or leverage above 1.5x", "CEO sells a further 10% of his stake, or the CFO leaves"], size=11, gap=2)
tb(s, 7.4, 5.55, 5.5, 0.3, "Three things to check yourself", size=12.5, bold=True, color=NAVY)
bullets(s, 7.4, 5.85, 5.5, 1.1, ["The CEO's Form 4s: no 10b5-1 plan is marked on them", "North America DTC ex-shift when Q4 is reported", "My buyback assumption (model.xlsx, Assump): it drives the gap to consensus"], size=11, gap=2)

# ================================================ APPENDIX ================================================
div = prs.slides.add_slide(BLANK); count["n"] += 1; tb(div, 0.5, 3.0, 12.3, 1.0, "Appendix", size=36, bold=True, color=NAVY); tb(div, 0.5, 3.9, 12.3, 0.6, "Bear case detail, valuation detail, expectations, management and holders, corporate actions, quality of earnings, downside, peers, sources", size=14, color=GREY)
div.notes_slide.notes_text_frame.text = "Appendix slides for Q&A. Not presented in the 15 minutes."
# A1 bear case
s = new("A1. Bear case: three red flags ranked by severity, each with the bull's rebuttal and the data that would settle it",
        "Crocs filings (10-K FY2025, 10-Q Q3-2026, earnings releases); SEC Form 4s; Piper Sandler via SGB Media; Federal Circuit; D. Del. docket.", "Bear case detail for Q&A. The ranking reflects impact on value: the fad risk drives the multiple and the earnings base; earnings quality drives how much of EPS is durable; insider selling and churn are a governance and signalling issue.", "A")
table(s, [["#", "Red flag", "Evidence", "Bull's rebuttal", "Data that would settle it"],
          ["1", "The core franchise is still shrinking in its largest market", "Crocs North America -6.8% FY25, -6.1% Q1-26, +0.4% Q2, -2.1% Q3; wholesale -4.9% in Q3. Teen rank No. 6 (2023) to No. 10, 1% share, off the girls' top ten (Piper Sandler). Clogs 74% of brand. 3D trademark lost at ITC and on appeal (Jan-2026). Clean trend hidden until Q3-27 by an accounting shift.",
           "Decline was chosen: promotions cut from May-2025, sell-in reduced; gross profit dollars rose. DTC ex-shift +2% (Q3), +5% (Q1, Q2). North America under half of the brand. Units +1.5% in FY25. Circana: clogs grew in H1-26.", "North America DTC ex-shift for Q4-26 and Q1-27. Fall 2027 teen survey. Retailer sell-through."],
          ["2", "Earnings quality: EPS growth is share count and adjustments", f"Adj. operating income FY26E {m(B['ebit']['FY2026E'])} vs {m(fy(2023)['adj_op_income'])} in FY23. Margin down y/y in 3 of the last 4 quarters. Q3 helped by lower duties (+130 bps); Q4 laps a cut quarter. Non-GAAP tax 18% vs 23% GAAP = about ${F['ip_tax_eps_fy26e']:.2f} EPS. Unrecognised tax benefits $637m.",
           f"$64m tariff refund excluded from adjusted EPS. FCF {m(F['ttm_fcf'])} exceeds adjusted net income. Margin turned in Q3-26. Buying back 10% a year at 7-10x earnings creates value.", "Operating income in dollars growing in FY27. Gross margin once duty comparisons normalise. Cash tax rate."],
          ["3", "Insiders selling into the rally; management turnover", f"12-month open-market sales ${F['insider']['sales_12m_usd']/1e6:.1f}m vs purchases ${F['insider']['buys_12m_usd']/1e6:.1f}m; none marked 10b5-1. CEO: {F['insider']['ceo_sales_sh']:,.0f} shares, ${F['insider']['ceo_sales_usd']/1e6:.1f}m, at $117-154. Three CFOs in 16 months. Four HEYDUDE leaders. Class action on HEYDUDE inventory; $0.6m accrued.",
           f"CEO retains about {F['insider']['ceo_shares_after']:,} shares (about ${F['insider']['ceo_shares_after']*price/1e6:.0f}m). Directors bought at $75-112. New CFO ex-SharkNinja and Nike.", "Further CEO sales above $150. A disclosed 10b5-1 plan. Ruling on the motion to dismiss."]], 0.5, 1.55, 12.35, col_w=[0.3, 1.9, 4.4, 3.6, 2.15], size=10.5, row_h=1.5)
# A2 checklist
s = new("A2. Bear-case checklist: no customer concentration and no guidance cuts, but margin compression and unscheduled insider selling are real",
        "10-K FY2025; 10-Q Q3-2026; earnings releases; Form 4 XML; Nasdaq short interest 2026-11-13; web research (data/research/news_bear_notes.md).", "Checklist the brief asked for, with findings. Two of the five standard flags are present: margin compression in three of the last four quarters, and insider selling not under a 10b5-1 plan.", "A")
table(s, [["Check", "Finding", "Detail"], ["Customer over 25% of revenue", "No", "No customer is 10% or more (10-K FY2025)"],
          ["Margin compression, last 4 quarters", "Yes, 3 of 4", f"Adj. gross margin {F['gm_yoy_bps']['2025Q4']:+.0f} / {F['gm_yoy_bps']['2026Q1']:+.0f} / {F['gm_yoy_bps']['2026Q2']:+.0f} / {F['gm_yoy_bps']['2026Q3']:+.0f} bps y/y; adj. operating margin {F['opm_yoy_bps']['2025Q4']:+.0f} / {F['opm_yoy_bps']['2026Q1']:+.0f} / {F['opm_yoy_bps']['2026Q2']:+.0f} / {F['opm_yoy_bps']['2026Q3']:+.0f} bps"],
          ["Unscheduled insider selling", "Yes", f"${F['insider']['sales_12m_usd']/1e6:.1f}m in 12 months across {F['insider']['n_sales']} transactions; 10b5-1 box unchecked on all"],
          ["Widening GAAP vs non-GAAP gap", "No (one-offs)", "Q2-25 $737m impairment; Q3-26 GAAP above adjusted ($64m refunds); recurring ~6% tax adjustment"],
          ["Guidance cuts, last 12 months", "None", "Three raises. Last cut 7-Aug-2025; FY25 guidance withdrawn 8-May-2025"],
          ["Accounting quality", "Watch", "IP transfers: $905m deferred tax assets, $637m unrecognised tax benefits; $404m goodwill and $1.3bn intangibles depend on HEYDUDE"],
          ["Debt maturities", "Fine", "Revolver Nov-2027 ($113m drawn of $1.0bn); $500m TLB Feb-2029; $350m notes Mar-2029; $350m notes Aug-2031"],
          ["Dilution", "Negative", "Shares -11% y/y; stock comp 1.1% of revenue"], ["Litigation", "Open", "Securities class action (D. Del.) plus 4 derivative suits; Dawgs false-advertising; Joybees. Damages not found"],
          ["Regulation / geopolitics / FX", "Moderate", "Tariffs 10-12.5%; 45% of production in Vietnam, 2 factories 73%; Middle East hit distributors; 44% of revenue abroad, $223m hedged"],
          ["Short interest; short reports", "Low; none", f"{F['short']['pct_shares']:.1f}% of shares, {F['short']['dtc']:.1f} days; down from {F['short']['peak_12m']/1e6:.1f}m shares. No published short report found; Goldman Sachs Sell, PT $128"]], 0.5, 1.5, 12.35, col_w=[2.6, 1.4, 8.35], size=10, row_h=0.44)
# A3 scenarios & DCF
s = new(f"A3. Scenario assumptions and DCF: base-case DCF of ${dcf[1]:,.0f} cross-checks the ${pt_base:,.0f} target; terminal value is {S['Base']['dcf']['tvpct']*100:.0f}% of enterprise value",
        "model.xlsx sheets Assump, Bear, Base, Bull, Sens (all my estimates). WACC 10.0%: risk-free 5.0%, beta 1.2, ERP 5.0%, pre-tax debt 6.5%, cash tax 22%.", "Scenario drivers and the DCF sensitivity grid. Every 50 basis points on WACC is worth about 14 dollars a share in the base case.", "A")
table(s, [["Driver (FY27E / FY28E)", "Bear", "Base", "Bull"], ["Crocs North America growth", "-8% / -8%", "0% / +1%", "+3% / +3%"], ["Crocs International growth", "+2% / 0%", "+9% / +8%", "+13% / +11%"], ["HEYDUDE growth", "-10% / -8%", "+4% / +3%", "+8% / +6%"],
          ["Adjusted EBIT margin", "20.5% / 18.5%", "22.8% / 23.0%", "23.5% / 24.3%"], ["Buybacks % of FCF; price", "70%; $120 / $90", "85%; $175 / $190", "90%; $190 / $230"], ["FY27E / FY28E EPS", f"${e27[0]:.2f} / ${e28[0]:.2f}", f"${e27[1]:.2f} / ${e28[1]:.2f}", f"${e27[2]:.2f} / ${e28[2]:.2f}"],
          ["Exit P/E; price target", f"7.0x; ${pt_bear:,.0f}", f"10.5x; ${pt_base:,.0f}", f"13.0x; ${pt_bull:,.0f}"], ["DCF: EV / equity, $m", f"{S['Bear']['dcf']['ev']:,.0f} / {S['Bear']['dcf']['eq']:,.0f}", f"{S['Base']['dcf']['ev']:,.0f} / {S['Base']['dcf']['eq']:,.0f}", f"{S['Bull']['dcf']['ev']:,.0f} / {S['Bull']['dcf']['eq']:,.0f}"],
          ["DCF per share", f"${dcf[0]:,.0f}", f"${dcf[1]:,.0f}", f"${dcf[2]:,.0f}"], ["Probability", "25%", "50%", "25%"]], 0.5, 1.55, 7.0, col_w=[2.6, 1.45, 1.45, 1.5], size=10.5, row_h=0.4)
g = MO["sens_dcf_grid"]; table(s, [["WACC \\ g"] + [f"{v*100:.0f}%" for v in g[0][1:]]] + [[f"{r[0]*100:.1f}%"] + [f"${v:,.0f}" for v in r[1:]] for r in g[1:]], 7.9, 1.95, 5.0, size=10.5, row_h=0.36)
tb(s, 7.9, 1.55, 5.0, 0.35, "Base-case DCF value per share: WACC x terminal growth", size=12, bold=True, color=NAVY)
bullets(s, 7.9, 5.0, 5.0, 1.9, [f"Even at a 12% WACC and 2% growth the base-case DCF is ${g[7][3]:,.0f}, above the ${price:.2f} price.", "Stock comp is not added back; cash tax 22% rather than the 18% non-GAAP rate.", f"Multiple check: 5-year mean P/E {RK['CROX_pe_ntm_5y_stats']['mean']:.1f}x on FY28E EPS = ${RK['CROX_pe_ntm_5y_stats']['mean']*e28[1]:,.0f}. Mean reversion is a headwind."], size=10.5, gap=3)
# A4 reverse DCF
s = new(f"A4. Reverse DCF: ${price:.0f} implies about {F['reverse']['implied_cagr']*100:.0f}% revenue growth for ten years at today's margin; the market pays for a business standing still",
        "model.xlsx sheet ReverseDCF (my calculation): 10-year explicit period, 2% terminal growth, 10% WACC, 22% cash tax, 3% reinvestment.", "Reverse DCF grid. Find today's price in the table. At a 22.6 percent margin the price sits between the zero and two percent growth rows.", "A")
gr = MO["reverse"]["grid"]; table(s, [["10y revenue CAGR \\ EBIT margin"] + [f"{v*100:.1f}%" for v in gr[0][1:]]] + [[f"{r[0]*100:+.0f}%"] + [f"${v:,.0f}" for v in r[1:]] for r in gr[1:]], 0.5, 1.6, 8.2, col_w=[2.4] + [0.83] * 7, size=11, row_h=0.42)
bullets(s, 9.0, 1.6, 3.9, 5.2, [("Single-stage.", f"EV {m(F['ev'])}; trailing unlevered FCF {m(F['reverse']['fcf'])}. Implied perpetual growth {F['reverse']['implied_g']*100:.1f}%."), ("Two-stage.", f"At a 22.6% margin the price implies about {F['reverse']['implied_cagr']*100:.0f}% a year for ten years. Base case {V['rcagr'][1]*100:.1f}%."),
    ("Zero growth.", f"Needs a {F['reverse']['implied_margin']*100:.0f}% margin forever, above anything since FY23."), ("Bear check.", "A 4% annual decline at an 18% margin is worth about $76: the March 2026 low."), ("Read.", "Not priced for decline, not priced for growth.")], size=11.5)
# A5 expectations bar
s = new("A5. Expectations bar: eight straight beats, three straight raises, yet the stock fell on two of them when the next-quarter guide was soft",
        "Nasdaq closes; Crocs press releases (EPS, guidance); Nasdaq/Zacks and news reports for consensus at the time.", "Expectations. The bar for February is a Q4 EPS above about 3.60 and a 2027 guide at or above 16 dollars.", "A")
pic(s, "11_earnings_reactions.png", 0.5, 1.5, w=6.6, max_h=3.4)
table(s, [["FY2026 guidance", "12-Feb", "30-Apr", "30-Jul", "29-Oct"], ["Revenue", "-1% to slightly up", "-1% to +1%", "+1% to +2%", "about +3%"], ["Crocs Brand", "flat to +2%", "flat to +2%", "+2% to +3%", "about +4%"], ["HEYDUDE", "-9% to -7%", "-7% to -5%", "-4% to -2%", "about flat"],
          ["Adj. operating margin", ">22.3%", ">22.3%", ">22.3%", ">22.5%"], ["Adjusted EPS", "$12.88-13.35", "$13.20-13.75", "$13.70-14.00", "$14.45-14.65"]], 0.5, 5.0, 6.6, col_w=[1.7, 1.3, 1.2, 1.2, 1.2], size=9.5, row_h=0.31)
table(s, [["Quarter", "EPS guide", "Actual", "vs top of guide", "Stock"], ["Q4-25", "$1.82-1.92", "$2.29", "+19%", "+19.0%"], ["Q1-26", "$2.67-2.77", "$2.99", "+8%", "+1.8%"], ["Q2-26", "$4.15-4.35", "$4.55", "+5%", "-7.4%"], ["Q3-26", "$3.20-3.30", "$3.69", "+12%", "+25.5%"], ["Q4-26", "$3.25-3.45", "cons. $3.40", "", ""]],
      7.4, 1.55, 5.5, col_w=[0.9, 1.3, 1.2, 1.2, 0.9], size=10.5, row_h=0.36)
bullets(s, 7.4, 3.9, 5.5, 3.0, [("To beat in February.", "Q4 EPS above about $3.61 (the smallest recent beat applied to $3.45) and revenue at or above +9%."), ("FY27 guide.", f"Consensus $16.01. Ex-buyback I get ${e27[1] + SN['No buybacks at all in FY27 (cash retained)'][0]:.2f}. Below $15.5 would break the margin leg."),
    ("Pattern.", f"Average absolute move {F['earn_avg_abs_move']:.0f}%. Falls came on soft next-quarter guides (Oct-25, Jul-26), not on the quarter."), ("Revisions.", "FY27 consensus EPS $14.95 to $16.01 in 30 days (Yahoo).")], size=11)
# A6 management/holders/insiders
s = new("A6. Management, incentives and shareholders: pay is tied to margin and cash; the CEO has sold 13% of his shares since June",
        "DEF 14A 2026; SEC Form 4s (parsed in data/derived/form4_transactions.csv); Schedule 13G filings; Nasdaq 13F data at 2026-09-30.", "Management and ownership. Incentive design is sensible. The record on buybacks is good and on M&A is poor. The insider selling is the item to probe.", "A")
bullets(s, 0.5, 1.55, 6.0, 5.3, [("CEO Andrew Rees (59).", "President 2014, CEO since 2017. Led the 2017-21 turnaround and the HEYDUDE deal. Owns 2.0% beneficially."),
    ("CFO Patraic Reagan.", "Since Sep-2025 (ex-SharkNinja CFO, 14 years at Nike). Third CFO in 16 months; predecessor resigned with immediate effect on 28-Aug-2025."),
    ("Brand heads.", "Anne Mehlman (Crocs, ex-CFO); Rupert Campbell (HEYDUDE, ex-adidas North America, from Nov-2025); Terence Reilly (Chief Brand Officer)."),
    ("Incentives.", "LTIP 67% PSUs: adjusted EBIT margin, and revenue with a relative-TSR modifier. Bonus 40% on adjusted free cash flow. 2023-25 revenue PSU paid zero. 22% voted against the 2026 equity plan."),
    ("Capital allocation.", "Buybacks: 6.5m shares at $88.68 (2025), about 4.4m at about $115 (9M-26). M&A: one deal, $2.5bn, 30% written off."),
    ("Activists.", "None; no 13D. Himalaya Capital reportedly a new holder in Q4-25 (not verified on EDGAR).")], size=11)
table(s, [["Open-market insider trades, last 12 months", "Shares", "Value", "Price"], ["A. Rees, CEO: sales Jun, Aug, Nov-26", f"{F['insider']['ceo_sales_sh']:,.0f}", f"${F['insider']['ceo_sales_usd']/1e6:.1f}m", "$117-154"], ["D. Treff, director: sales Nov-26", "25,516", "$4.0m", "$151-159"], ["R. Frasch, director: sale Oct-26", "15,000", "$2.3m", "$153.51"],
          ["A. Mehlman, brand president: sale Feb-26", "12,145", "$1.2m", "$100.06"], ["T. Smach, chair: sales Feb-26", "9,963", "$1.0m", "$98-100"], ["R. Campbell, HEYDUDE: sale Oct-26", "2,645", "$0.4m", "$150.87"],
          ["Total sales (none marked 10b5-1)", "", f"${F['insider']['sales_12m_usd']/1e6:.1f}m", ""], ["Purchases: Smach, Kaplan (Sep-26)", "5,565", f"${F['insider']['buys_12m_usd']/1e6:.1f}m", "$109-112"]], 6.8, 1.55, 6.1, col_w=[3.3, 0.9, 0.9, 1.0], size=10, row_h=0.34)
table(s, [["Holder", "Shares", "%", "Source"], ["BlackRock", "4.52m", "9.9%", "13F Sep-26"], ["FMR", "3.51m", "7.1%", "13G Jun-26"], ["WIT Partners (HEYDUDE founder)", "2.85m", "5.3%", "13G May-26"], ["Vanguard Capital Management", "2.57m", "5.1%", "13G Mar-26"],
          ["American Century", "2.07m", "4.5%", "13F Sep-26 (+41% q/q)"], ["LSV Asset Management", "1.83m", "4.0%", "13F Sep-26"]], 6.8, 4.75, 6.1, col_w=[2.9, 0.9, 0.7, 1.6], size=10, row_h=0.31)
# A7 corporate actions and debt
s = new("A7. Corporate actions: no deals in three years, $1.1bn of buybacks since January 2025, and the 2022 HEYDUDE deal still defines the rating",
        "Crocs press releases 2021-12-23 and 2022-02-17; 10-K FY2022 Note 3; 10-Q Q2-2025 (impairment); 10-Q Q3-2026 Note 7 (borrowings).", "Corporate actions and the debt stack. There have been no acquisitions or disposals in the last three years. HEYDUDE is shown for context because it explains the mix, the margin and the multiple.", "A")
table(s, [["Date", "Action", "Value", "Rationale", "Effect on mix, margin, rating"],
          ["Dec-2021 / Feb-2022", "Acquisition of HEYDUDE", "$2.5bn headline: $2.05bn cash + $450m stock (2,852,280 shares); about $2.3bn recorded at close; $2.0bn Term Loan B", "Second casual brand", "Mix: 25% of revenue at peak, 17% now. Margin: HEYDUDE 9.5% vs Crocs 33.4% (FY25). Leverage 0.8x to 2.1x, now 1.2x. Forward P/E about 15x before the deal, about 8x for three years after."],
          ["Q2-2025", "HEYDUDE impairment", "$737m: $430m trademark, $307m goodwill", "Slower recovery; tariffs", "GAAP loss in FY25; non-cash. About 30% of the purchase price."],
          ["2025", "Share repurchases", "$577m; 6.5m shares at $88.68", "Return of free cash flow", "Share count -10%"], ["9M-2026", "Share repurchases", "$501m; about 4.4m shares", "Same", "Diluted shares 48.0m in Q3-26 vs 54.0m"],
          ["Feb-2025; Jul-2026", "Authorisation increases", "+$1.0bn; raised to about $2.0bn", "", f"$1.7bn remaining = {1700/F['mcap']*100:.0f}% of market cap"]], 0.5, 1.5, 12.35, col_w=[1.4, 1.9, 3.3, 1.6, 4.15], size=9.5, row_h=0.42)
tb(s, 0.5, 4.75, 12.3, 0.35, "November 2023 to November 2026: no acquisitions, disposals or spin-offs (only a $4.4m takeback of the Malaysian distributor).", size=11.5, bold=True, color=NAVY)
table(s, [["Debt at 30-Sep-2026", "Amount", "Rate", "Maturity"], ["Revolving facility ($1.0bn)", "$113m", "floating", "Nov-2027"], ["Term Loan B", "$500m", "SOFR + 2.25%", "Feb-2029"], ["Senior notes", "$350m", "4.250%", "Mar-2029"], ["Senior notes", "$350m", "4.125%", "Aug-2031"], ["Total / net of $163m cash", "$1,313m / $1,150m", "", f"{F['nd_ebitda']:.1f}x EBITDA"]],
      0.5, 5.2, 7.0, col_w=[2.6, 1.7, 1.4, 1.3], size=9.5, row_h=0.27)
# A8 quality
s = new("A8. Quality of earnings: margins compressed in three of the last four quarters; the GAAP gap is one-offs plus a recurring tax adjustment",
        "Crocs earnings releases (non-GAAP reconciliations), 10-K FY2025 tax note. Units and ASP from 10-Ks.", "Quality of earnings and the unit economics of the Crocs Brand.", "A")
pic(s, "15_margins_gaap_gap.png", 0.5, 1.5, w=7.3, max_h=2.75)
pic(s, "05_crocs_units_asp.png", 0.5, 4.25, w=7.3, max_h=2.7)
bullets(s, 8.1, 1.55, 4.8, 5.3, [("Cash conversion.", f"FCF {m(F['ttm_fcf'])} TTM = {F['ttm_fcf_conv']:.0f}% of adjusted net income. Above 100% in three of four years."), ("Tax.", f"Non-GAAP rate 18% vs GAAP 23%: excludes amortisation of IP-transfer tax assets, about ${F['ip_tax_eps_fy26e']:.2f} of FY26 EPS. Cash taxes paid $185m in 2025. Unrecognised tax benefits $637m (from $219m at start of 2023)."),
    ("One-offs.", "Q2-25: $737m impairment. Q4-24: tax benefit from an IP transfer. Q3-26: $64m tariff refunds, excluded from adjusted EPS."), ("Stock comp.", f"{m(F['ttm_sbc'])} TTM, 1.1% of revenue; share count -11% y/y."),
    ("ROIC.", "46% (FY22) to 27% (FY25) as HEYDUDE capital earns little."), ("Units.", "Crocs Brand pairs +1.5% in FY25 with ASP -0.5%: volume is not collapsing.")], size=11)
# A9 downside
s = new("A9. Downside in a market sell-off: plan for -25-30% in a 20% market fall; the stock fell 74% peak-to-trough in 2021-22",
        "Nasdaq daily closes for CROX, DECK, SPY, XRT (my calculation, scripts/08); Yahoo Finance beta; FactSet for S&P 500 P/E.", "Downside and beta. The October to November 2026 episode is flattering because it contained the Q3 print; do not read it as defensiveness.", "A")
so = RK["sp500_selloffs"]; table(s, [["S&P 500 drawdown (peak to trough)", "S&P 500", "CROX", "DECK", "Retail ETF (XRT)"]] + [[f"{e['spy_peak']} to {e['spy_trough']}", f"{e['spy_pct']:.0f}%", f"{e['crox_pct']:+.0f}%", f"{e['deck_pct']:+.0f}%", f"{e['xrt_pct']:+.0f}%"] for e in so], 0.5, 1.55, 7.2, col_w=[3.0, 1.0, 1.0, 1.0, 1.2], size=10.5, row_h=0.38)
pic(s, "09_pe_vs_history_index.png", 0.5, 4.35, w=6.2, max_h=2.6)
bullets(s, 8.0, 1.55, 4.9, 5.3, [("Beta.", f"{RK['beta_weekly_5y']:.2f} (5y weekly, mine); 1.50 (Yahoo, 5y monthly); {RK['beta_weekly_2y']:.2f} (2y weekly)."), ("Volatility.", f"{RK['vol_1y_annualised_pct']:.0f}% annualised over one year vs {RK['spy_vol_1y_annualised_pct']:.0f}% for the S&P 500."),
    ("Worst drawdown.", "-74%: $180.57 (12-Nov-2021) to $47.21 (17-Jun-2022)."), ("Planning number.", "20% market fall, no company news: -25-30%, about $112-120."), ("Floor.", f"25th-percentile P/E of {RK['CROX_pe_ntm_5y_stats']['p25']:.1f}x on consensus FY27 EPS is about ${RK['CROX_pe_ntm_5y_stats']['p25']*16.01:,.0f}."),
    ("Support.", f"Buybacks of about {m(B['bb']['FY2027E'])} a year are 8% of the market cap; more shares are retired at lower prices.")], size=11.5)
# A10 sources / caveats
s = new("A10. Sources, method and what is uncertain or stale",
        "Full list with URLs and as-of dates: sources.md. Scripts: scripts/01-18. Raw data: data/.", "Caveats. The main ones: Yahoo's price API and Macrotrends refused automated access, so prices come from Nasdaq and historical P/E is my own calculation; segment consensus was not found; the product split by region is my estimate.", "A")
bullets(s, 0.5, 1.55, 6.1, 5.3, [("Primary sources.", "10-K FY2021-25 and FY2009; 10-Qs to Q3-2026; 26 earnings releases; 2026 proxy; Form 4 XML; 13Gs; six earnings-call transcripts (five company-hosted)."),
    ("Market data.", "Nasdaq API (prices, short interest, Zacks consensus, 13F); Yahoo Finance pages (consensus, beta); StockAnalysis (peer multiples); FactSet (index P/E)."),
    ("Not accessible.", "Macrotrends (403) and the Yahoo price API (429). Substitutes used and labelled; no access controls were bypassed."),
    ("Labels.", "Every number is reported, guidance, consensus, named broker, or my estimate. All quotes are verbatim from transcripts."),
    ("Model.", "model.xlsx: 1,046 live formulas, no errors after recalculation; scenario sheets share one formula structure.")], size=11.5)
bullets(s, 6.9, 1.55, 6.0, 5.3, [("Sources disagree.", "FY27 EPS consensus $16.01 (Yahoo) vs $15.85 (Nasdaq). Beta 1.50 vs 1.21 vs 0.67. 10-year yield 4.84-5.13% (5.0% used). Net debt $1.15bn (mine) vs $1.50bn incl. leases (vendor)."),
    ("My estimates.", "Product mix by region; China share applied to the brand; all nine risk scores; fixed/variable split; scenario drivers; probabilities."),
    ("Not found.", "Segment consensus; short reports; class-action ruling; sell-through data; oil sensitivity; long-term targets; confirmed Q4 date."),
    ("Stale or approximate.", "BlackRock/Vanguard proxy figures date from 2023 13Gs (13F used instead). DECK Sep-26 EPS $2.31 (XBRL) vs $2.03 (Zacks). S&P 500 P/E from a search summary of the FactSet report."),
    ("Not verified.", "Himalaya Capital holding; Citi and Williams Trading ratings; Hedgeye short thesis (paywalled).")], size=11.5)
out = os.path.join(ROOT, "deck.pptx"); prs.save(out); print("saved", out, "slides:", len(prs.slides))
