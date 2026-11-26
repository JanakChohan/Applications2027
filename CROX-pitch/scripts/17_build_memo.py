"""Build pitch-memo.docx (5-8 pages) from data/derived/facts.json and the chart pack."""
import json, os
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); F = json.load(open(os.path.join(ROOT, "data", "derived", "facts.json")))
V = F["valuation"]; K = F["key"]; RAR = F["rar"]; B = F["scen"]["Base"]; RK = F["risk"]; PEER = F["peers"]; SN = F["sens"]
price = F["price"]; pt_bear, pt_base, pt_bull, pt_w = V["pt"]; r_bear, r_base, r_bull, r_w = [v * 100 for v in V["ret"]]; e27 = V["eps27"]; e28 = V["eps28"]; dcf = V["dcf"]
NAVY = RGBColor(0x1F, 0x38, 0x64); GREY = RGBColor(0x5F, 0x63, 0x68)
doc = Document()
for s in doc.sections: s.left_margin = s.right_margin = Cm(2.0); s.top_margin = Cm(1.8); s.bottom_margin = Cm(1.8)
st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10.5); st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri"); st.paragraph_format.space_after = Pt(5); st.paragraph_format.line_spacing = 1.08
for lvl, sz in ((1, 14), (2, 11.5)):
    h = doc.styles[f"Heading {lvl}"]; h.font.name = "Calibri"; h.font.size = Pt(sz); h.font.bold = True; h.font.color.rgb = NAVY; h.paragraph_format.space_before = Pt(10 if lvl == 1 else 6); h.paragraph_format.space_after = Pt(4)
    h.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
def para(text, bold_lead=None, size=None, italic=False, color=None, align=None, after=None):
    p = doc.add_paragraph()
    if bold_lead: r = p.add_run(bold_lead); r.bold = True
    r = p.add_run(text); r.italic = italic
    if size:
        for rr in p.runs: rr.font.size = Pt(size)
    if color:
        for rr in p.runs: rr.font.color.rgb = color
    if align: p.alignment = align
    if after is not None: p.paragraph_format.space_after = Pt(after)
    return p
def bullet(text, lead=None):
    p = doc.add_paragraph(style="List Bullet"); p.paragraph_format.space_after = Pt(2)
    if lead: p.add_run(lead).bold = True
    p.add_run(text); return p
def shade(cell, hexcol):
    tcPr = cell._tc.get_or_add_tcPr(); shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hexcol); tcPr.append(shd)
def table(rows, widths=None, header=True, size=9):
    t = doc.add_table(rows=len(rows), cols=len(rows[0])); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            c = t.cell(i, j); c.text = ""; p = c.paragraphs[0]; r = p.add_run(str(val)); r.font.size = Pt(size); p.paragraph_format.space_after = Pt(0)
            if header and i == 0: r.bold = True; r.font.color.rgb = RGBColor(255, 255, 255); shade(c, "1F3864")
            elif j == 0: r.bold = True
            if widths: c.width = Inches(widths[j])
    if widths:
        t.autofit = False
        tblPr = t._tbl.tblPr; lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
        for j, wd in enumerate(widths):
            t.columns[j].width = Inches(wd)
            for cell in t.columns[j].cells: cell.width = Inches(wd)
    doc.add_paragraph().paragraph_format.space_after = Pt(2); return t
def fig(name, width=6.3, caption=None):
    doc.add_picture(os.path.join(ROOT, "charts", name), width=Inches(width)); doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    if caption: para(caption, size=8, italic=True, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER, after=6)
m = lambda x, d=0: f"${x:,.{d}f}m"; pk = lambda t, k: PEER[t][k]

# ---------------- header ----------------
p = doc.add_paragraph(); r = p.add_run("Crocs, Inc. (NASDAQ: CROX)"); r.bold = True; r.font.size = Pt(20); r.font.color.rgb = NAVY; p.paragraph_format.space_after = Pt(0)
p = doc.add_paragraph(); r = p.add_run("LONG: a cash-return compounder still priced for a clog bust"); r.bold = True; r.font.size = Pt(13); p.paragraph_format.space_after = Pt(2)
para(f"Pitch memo for the portfolio manager | 26 November 2026 | Price ${price:.2f} (close {F['asof']}) | Labels: (R) reported, (G) guidance, (C) consensus, (B) broker, (E) my estimate | Sources: sources.md", size=8.5, color=GREY, after=6)
table([["Recommendation", "Base target (Dec-2027)", "Prob-weighted value", "Bear / Bull", "Holding period", "Position"],
       ["LONG", f"${pt_base:,.0f} ({r_base:+.0f}%)", f"${pt_w:,.0f} ({r_w:+.0f}%)", f"${pt_bear:,.0f} ({r_bear:+.0f}%) / ${pt_bull:,.0f} ({r_bull:+.0f}%)", "12-18 months", "Mid-sized; half now, add below $140"]], size=9.5)
table([["Market cap", "EV", "P/E FY27 (C)", "EV/EBITDA TTM", "FCF yield", "Net debt/EBITDA", "FY27E EPS mine vs (C)", "Short interest"],
       [f"${F['mcap']/1000:.1f}bn", f"${F['ev']/1000:.1f}bn", f"{F['pe_fy27_cons']:.1f}x", f"{F['ev_ebitda']:.1f}x", f"{F['fcf_yield']:.1f}%", f"{F['nd_ebitda']:.1f}x", f"${e27[1]:.2f} vs $16.01", f"{F['short']['pct_shares']:.1f}%"]], size=9)

doc.add_heading("1. The call in five sentences", 1)
para(f"Crocs turns about 18% of revenue into free cash flow ({m(F['ttm_fcf'])} in the last twelve months, a {F['fcf_yield']:.1f}% yield) and spends nearly all of it on buybacks, retiring about 10% of its shares in each of the last two years. "
     f"Revenue growth of 4% therefore becomes mid-teens EPS growth: I forecast ${e27[1]:.2f} for FY2027 against consensus of $16.01, because guidance and most Street models exclude repurchases. "
     f"The stock trades on {F['pe_fy27_cons']:.1f}x that consensus number because investors still fear the clog is a fad that is unwinding in North America. "
     f"My stress test says a full unwind would cut EPS to about ${RAR['eps1']:.2f}, but the evidence (international now {F['intl_share_ttm']:.0f}% of the brand and growing 12%, margins turning, HEYDUDE no longer shrinking) points to a much lower probability than the roughly 40% the price implies. "
     f"The base case is worth ${pt_base:,.0f} by December 2027 with no help from the multiple beyond what the stock already trades on.")
para("Three honest caveats up front. ", bold_lead=None)
bullet(f"The stock has doubled in a year and rose 34% in the last month. It sits at the sell-side mean target of $160.75 (C) and in the top quartile of its own five-year P/E range. The re-rating has happened.", "Entry. ")
bullet(f"Base-case upside of {r_base:+.0f}% against bear-case downside of {r_bear:+.0f}% is a ratio of {K['Upside/downside ratio, base vs bear (x)']:.2f}x. The trade works on probabilities ({K['Upside/downside ratio, probability-weighted (x)']:.1f}x weighted), not on magnitudes.", "Skew. ")
bullet(f"The CEO sold ${F['insider']['ceo_sales_usd']/1e6:.1f}m of stock between June and November 2026 with no 10b5-1 plan marked on the Form 4s.", "Insiders. ")

doc.add_heading("2. The business in brief", 1)
para(f"Crocs designs and markets moulded foam clogs (74% of the Crocs Brand), sandals (13%) and clip-on charms (8%), and since 2022 owns HEYDUDE, a US slip-on loafer brand. Manufacturing is outsourced, mostly to Vietnam. FY2025 revenue was {m(F['fy2025']['revenue'])} (R): Crocs Brand 82%, HEYDUDE 18%; direct-to-consumer 52%, wholesale 48%; United States 56%. "
     f"All revenue is one-off product sales; nothing is contractual. No customer is 10% of revenue (R). The economics come from the product: a one-piece moulded shoe earns a 61% gross margin at a $25 average selling price, and capex is under 2% of revenue.")
fig("01_revenue_mix.png", 5.6)
para(f"The track record has two halves. From 2017 to 2021 revenue more than doubled and operating margin went from 2% to 30%. From 2022 the $2.5bn HEYDUDE acquisition, then tariffs and DTC investment, took adjusted operating margin from 27.7% (FY23) to 22.3% (FY25). Adjusted operating income in FY26E ({m(B['ebit']['FY2026E'])}) is {(1-B['ebit']['FY2026E']/F['fy2023']['adj_op_income'])*100:.0f}% below FY23, yet adjusted EPS is {(B['eps']['FY2026E']/F['fy2023']['adj_eps']-1)*100:.0f}% higher because the share count fell from 62m to under 49m.")

doc.add_heading("3. The debate, and where I differ from consensus", 1)
para("The single question driving the stock is whether the clog is a fad now unwinding in its home market, or a durable franchise going through a deliberate reset while it grows abroad.")
table([["", "Consensus believes", "I believe", "Why the market is wrong"],
       ["Earnings", "FY27 EPS $16.01, +9% (C)", f"${e27[1]:.2f}, +{B['epsg']['FY2027E']*100:.0f}% (E)", "Guidance excludes buybacks and the Street follows. Two-thirds of the FY27 share-count benefit is already banked from 2026 repurchases."],
       ["North America", "Structural decline", "Mostly self-inflicted, and distorted until Q3 2027", "Promotions were cut on purpose in May 2025. A marketplace moving to wholesale accounting hides 700-800 bps of DTC growth a quarter. Underlying DTC grew 2-5% each quarter of 2026. Lowest-confidence leg."],
       ["The company", "A one-product US fad", "A majority-international brand", f"International is {F['intl_share_ttm']:.0f}% of the brand, up from 33% in FY21, growing 9-12%; share in China, India, Japan, Germany and France is one-third of mature levels (management)."],
       ["HEYDUDE", "A liability", "Small and stable", "17% of revenue, already written down by $737m; revenue +6% in Q3-26 and guided +10-12% in Q4."]], widths=[0.9, 1.4, 1.5, 2.9], size=8.5)
fig("04_crocs_brand.png", 6.2)

doc.add_heading("4. Proprietary analysis: how much of Crocs is a fad?", 1)
para(f"I split trailing revenue into nine lines by brand, region, channel and product, scored each from 1 to 5 for exposure to a reversal in clog demand, and mapped each score to a two-year revenue decline (5 = 30%, calibrated to Crocs' own 2007-09 bust of -24% and HEYDUDE's -25% in 2023-25). The scores are my judgement; the revenue figures are reported, with the product split estimated from the FY2025 mix.")
fig("12_revenue_at_risk.png", 6.0)
para(f"Result: {RAR['at_risk_pct']*100:.1f}% of group revenue ({m(RAR['at_risk'])}) is at risk. Assuming half of distribution cost and 65% of SG&A are fixed, plus 150 bps of markdown pressure, adjusted EBITDA falls from {m(RAR['ebitda0'])} to {m(RAR['ebitda1'])} and run-rate EPS from ${RAR['eps0']:.2f} to ${RAR['eps1']:.2f} at an 18% tax rate, {abs(RAR['vs_cons'])*100:.0f}% below consensus FY27. At a 7x trough multiple that is ${RAR['val']:,.0f} a share. "
     f"Shifting every score by one notch moves stressed EPS to ${RAR['minus1_eps']:.2f} or ${RAR['plus1_eps']:.2f}; a 20,000-draw simulation of independent one-notch errors gives a 5th-95th percentile range of ${F['rar_mc']['eps_p5_p50_p95'][0]:.2f} to ${F['rar_mc']['eps_p5_p50_p95'][2]:.2f}. The finding that a full unwind roughly halves EPS does not depend on my scoring.")
para(f"What is priced in. At the March 2026 low of $75.78 the stock traded within {(75.78/RAR['val']-1)*100:.0f}% of that full-unwind value: the fear was heavily over-priced. At ${price:.2f}, solving for the probability that reconciles my three scenario targets with today's price gives about {K['Market-implied probability of the bear case (base:bull 2:1)']*100:.0f}% on my (milder) bear case. I estimate 25%. The fear is still over-priced, but the margin is now modest.", bold_lead="")
para("How management is responding. Hard revenue evidence: sandals about $450m and growing double digits; international +8.8% in the first nine months of 2026 with DTC +25%; HEYDUDE wholesale +14% in Q3 (against an easy comparison, as the CEO conceded: \"we are up against a weak compare\"); 10.9m shares retired since January 2025. Activity metrics only: TikTok Shop rankings, collaborations \"selling out\", campaign impressions. The evidence is strongest abroad and weakest in North America.")

doc.add_heading("5. Valuation", 1)
table([["", "Bear", "Base", "Bull"], ["Probability (E)", "25%", "50%", "25%"],
       ["Revenue CAGR FY26E-31E", f"{V['rcagr'][0]*100:+.1f}%", f"{V['rcagr'][1]*100:+.1f}%", f"{V['rcagr'][2]*100:+.1f}%"], ["FY28E adj. EBIT margin", f"{V['margin28'][0]*100:.1f}%", f"{V['margin28'][1]*100:.1f}%", f"{V['margin28'][2]*100:.1f}%"],
       ["FY27E / FY28E EPS", f"${e27[0]:.2f} / ${e28[0]:.2f}", f"${e27[1]:.2f} / ${e28[1]:.2f}", f"${e27[2]:.2f} / ${e28[2]:.2f}"], ["Exit P/E on FY28E (Dec-2027)", "7.0x", "10.5x", "13.0x"],
       ["Price target", f"${pt_bear:,.0f} ({r_bear:+.0f}%)", f"${pt_base:,.0f} ({r_base:+.0f}%)", f"${pt_bull:,.0f} ({r_bull:+.0f}%)"], ["DCF per share (10% WACC, 2% g)", f"${dcf[0]:,.0f}", f"${dcf[1]:,.0f}", f"${dcf[2]:,.0f}"]], widths=[2.3, 1.4, 1.4, 1.4])
bullet(f"Probability-weighted value ${pt_w:,.0f}; expected return {r_w:+.0f}% over about 13 months. The expected return is zero only if the bear probability is {K['Break-even bear probability (EV = 0, base:bull kept 2:1)']*100:.0f}%.", "Expected value. ")
bullet(f"Today's multiple on my FY27E EPS is {F['pe_fy27_mine']:.1f}x. Held constant, the December 2027 value is ${F['pe_fy27_mine']*e28[1]:,.0f} ({(F['pe_fy27_mine']*e28[1]/price-1)*100:+.0f}%). The rest of the base target assumes consensus rises to my numbers and the stock keeps its current {F['pe_fy27_cons']:.1f}x consensus multiple.", "How much is multiple? ")
bullet(f"The price implies about {F['reverse']['implied_cagr']*100:.0f}% revenue growth a year for ten years at today's margin, then 2% ({F['reverse']['implied_g']*100:.1f}% perpetual free-cash-flow growth). My base case is {V['rcagr'][1]*100:.1f}%. The market pays for a business standing still.", "Reverse DCF. ")
bullet(f"Forward P/E of {RK['crox_pe_ntm_now']:.1f}x is the {RK['CROX_pe_ntm_5y_stats']['pctile_now']:.0f}th percentile of five years (median {RK['CROX_pe_ntm_5y_stats']['median']:.1f}x). Mean reversion is a headwind. Against the S&P 500 at 18.3x it is a 45% discount.", "Own history. ")
bullet(f"Crocs is not cheap against Deckers: {pk('CROX','pe_fwd'):.1f}x vs {pk('DECK','pe_fwd'):.1f}x forward P/E and {pk('CROX','ev_ebitda'):.1f}x vs {pk('DECK','ev_ebitda'):.1f}x EV/EBITDA, with Deckers growing faster and holding net cash. The five-year median discount of {abs(RK['CROX_vs_DECK_ntm_prem_pct_5y_stats']['median']):.0f}% has closed from both ends. On a Value/Growth score (P/S over growth) Crocs is the worst of the four peers at {pk('CROX','value_growth_score_ttm'):.2f} vs {pk('ONON','value_growth_score_ttm'):.2f} for On. This is cash at a discount, not growth at a discount.", "Peers. ")
fig("14_valuation_range.png", 5.6)
fig("08_pe_history.png", 6.2)

doc.add_heading("6. The bear case, ranked", 1)
table([["#", "Red flag", "Evidence", "Bull's rebuttal", "Data that settles it"],
       ["1", "Core franchise still shrinking in its largest market", "Crocs North America -6.8% in FY25 and -2.1% in Q3-26; wholesale -4.9%. Piper Sandler teen rank No. 6 (2023) to No. 10, 1% share (B). 3D clog trademark lost at the ITC and on appeal (Jan-2026).", "Decline was chosen (promotion cuts, tighter sell-in); DTC ex-shift +2% to +5%; region is under half the brand; units still growing.", "North America DTC ex-shift in Q4-26 and Q1-27; Fall 2027 teen survey."],
       ["2", "Earnings quality", f"Operating income {(1-B['ebit']['FY2026E']/F['fy2023']['adj_op_income'])*100:.0f}% below FY23 while EPS is up; margins down y/y in 3 of the last 4 quarters; non-GAAP tax 18% vs 23% GAAP adds about ${F['ip_tax_eps_fy26e']:.2f} of EPS; $637m unrecognised tax benefits.", f"Tariff refund excluded from adjusted EPS; FCF ({m(F['ttm_fcf'])}) exceeds adjusted net income; margin turned up in Q3-26.", "Operating income dollars growing in FY27; cash tax rate."],
       ["3", "Insider selling and management churn", f"${F['insider']['sales_12m_usd']/1e6:.1f}m sold vs ${F['insider']['buys_12m_usd']/1e6:.1f}m bought in 12 months, none marked 10b5-1; CEO ${F['insider']['ceo_sales_usd']/1e6:.1f}m. Three CFOs in 16 months. Securities class action over HEYDUDE inventory.", f"CEO keeps about ${F['insider']['ceo_shares_after']*price/1e6:.0f}m of stock; directors bought at $75-112.", "Further CEO sales; a 10b5-1 plan; ruling on the motion to dismiss."]], widths=[0.25, 1.2, 2.3, 1.7, 1.25], size=8)
para(f"Other checks. No customer above 10% of revenue. No guidance cut in the last twelve months (three raises; last cut August 2025). Debt: revolver November 2027 ($113m drawn), $500m term loan and $350m notes in 2029, $350m notes in 2031; leverage {F['nd_ebitda']:.1f}x. Dilution is negative. Short interest {F['short']['pct_shares']:.1f}% of shares, halved in a year. No published short report found; Goldman Sachs rates the stock Sell with a $128 target (B).", size=9.5)

doc.add_heading("7. Catalysts and expectations", 1)
table([["When", "Catalyst", "Numbers", "Probability (E)"],
       ["About 11-Feb-2027", "Q4-26 results and first FY27 guide", f"Q4 guide: revenue +7-9%, EPS $3.25-3.45 (consensus $3.40). FY27 consensus $16.01; my ex-buyback EPS ${e27[1] + SN['No buybacks at all in FY27 (cash retained)'][0]:.2f}", "60% guide midpoint at or above $16.0"],
       ["Apr-Jul 2027", "Q1 and Q2 results", "North America DTC reported about -5% even if underlying +2%", "40% the market looks through it"],
       ["Late Oct-2027", "Q3-27: accounting shift lapped", "First clean North America number in a year", "55% positive DTC"],
       ["Continuous", "Buybacks", f"$1.7bn authorised = {1700/F['mcap']*100:.0f}% of market cap; base {m(B['bb']['FY2027E'])} in FY27", "85% above $500m"],
       ["Open", "Tariff litigation (Section 301)", f"Each point about $4m, ${abs(SN['+1 pt US tariff rate on imports'][0]):.2f} EPS", "20% removed, 20% raised"],
       ["By Nov-2027", "Revolver refinancing", "$1.0bn facility, $113m drawn", "90%"]], widths=[1.1, 1.8, 2.6, 1.3], size=8.5)
para(f"Expectations bar. Crocs has beaten the top of its EPS guide by 5-19% in each of the last four quarters, and the stock still fell on two of the last eight reports when the next-quarter guide was soft. Average absolute move on results: {F['earn_avg_abs_move']:.0f}%. In a 20% market sell-off I would plan for the stock down 25-30% (beta 1.2-1.5; -42% in 2022 against -25% for the index).")

doc.add_heading("8. Risks, mitigants and kill criteria", 1)
table([["Risk", "Mitigant", "Kill criterion"],
       ["Fad unwinds in North America", "International majority; price protected", "North America DTC ex-shift negative two quarters running"],
       ["International slows", "Share one-third of mature levels; China only 8% of sales", "International growth below 5% two quarters running"],
       ["Margin slips again", "$150m cost programme; duties 10-12.5% vs 18-20%", "FY27 adj. margin guided below 21.5%"],
       ["Another large acquisition", "Leverage target 1-1.5x", "Deal above $500m, or leverage above 1.5x, or buybacks below $300m a year"],
       ["HEYDUDE relapses", "Channel inventory clean", "Revenue down more than 5% y/y after Q1-27"],
       ["Insider selling continues", "CEO retains a large stake", "CEO sells a further 10% of his holding, or the CFO leaves"]], widths=[1.9, 2.4, 2.5], size=8.5)

doc.add_heading("9. Conclusion", 1)
para(f"The evidence supports a long, with moderate conviction. It does not support a short: estimates are rising, cash generation is real and the company is retiring a tenth of itself each year. It also does not support a table-pounding buy: the stock is at consensus targets after a 99% run, peers are just as cheap, and the left tail is {r_bear:+.0f}% or worse. I recommend starting at half size at ${price:.0f}, adding below $140 where the expected return rises to about {(pt_w/140-1)*100:.0f}%, and holding to the December 2027 target of ${pt_base:,.0f} unless a kill criterion triggers.")
para("Three things the PM should check independently: (1) the Form 4s for the CEO's sales and whether a 10b5-1 plan exists (the forms do not mark one); (2) Crocs North America DTC growth excluding the marketplace shift when Q4 is reported; (3) my buyback assumption, which drives most of the gap to consensus EPS (model.xlsx, sheet Assump).", italic=True, size=9.5)
out = os.path.join(ROOT, "pitch-memo.docx"); doc.save(out); print("saved", out)
