import re, diagrams as dg, charts as ch
from svg import fig
FIGS={}; n=[0]
def F(key, svg, cap):
    n[0]+=1; FIGS[key]=fig(svg,cap,n[0])
def strip(f): return f.split('<div class="cap">')[0].replace('<div class="fig">','')

events=[("2021",[("Record profit $48bn; reserve releases","firm"),("Chase UK launches (Sep); Nutmeg, 55ip, OpenInvest, Campbell Global bought","deal"),("AWM: four ingredients; record $389bn flows","awm")]),
        ("2022",[("$15bn investment plan; Investor Day defends 'good expenses'","firm"),("Rates surge; Dimon's 'hurricane'; reserves rebuilt","macro"),("AWM passes 3,000 PB advisors; active ETFs #2; Global Shares bought","awm")]),
        ("2023",[("SVB and First Republic fail; JPM buys FRC (1 May)","deal"),("Record $162bn revenue; 400 AI use cases; Basel fight","firm"),("AWM: $490bn flows; $1bn/day into PB; 'four $100m clients a day'","awm")]),
        ("2024",[("CB merged into CIB (Jan); record profit; LLM Suite to 200k staff","firm"),("Excess capital $54bn; no buybacks 'at these prices'; 1,300 more Chase advisors","firm"),("AWM: ROE 34% vs peers 12-28%; #1 active ETF flows; six new offices","awm")]),
        ("2025",[("$1.5tn Security & Resiliency plan (Oct); Apple Card; 270 Park opens; JPMD token","deal"),("8th record year; ROTCE 20%; RTO five days; Piepszak COO","firm"),("AWM: $553bn flows; 4,101 advisors; ROE 40%; Frame global PB CEO","awm")]),
        ("2026",[("Basel rescinded (Mar); Chase Germany (May); co-presidents named (Jun)","firm"),("AI cuts 30-40% in 'discrete areas'; Q2 ROTCE 23% ex-items","firm"),("AWM: client assets $7.7tn; Europe named biggest PB share opportunity","awm")])]
F("timeline", ch.timeline(events), "Six years in one line. Gold boxes are AWM and Private Bank events; navy are firm-level; blue are deals and investments; grey are macro or regulatory.")
F("flywheel", strip(dg.flywheel()), "Mary Erdoes' four 'ingredients for growth' from the 2021 letter, drawn as the loop they form. Each feeds the next; the Advisor sits in ingredients 2 and 3 and is measured on ingredient 4.")
wealth_rows=[("Chase retail","everyday banking","CCB","Branches and app; mass market; scale economics"),
 ("Chase Private Client","$150,000+ (US)","CCB","Branch banker plus a J.P. Morgan advisor"),
 ("J.P. Morgan Private Client","$750,000+ (US, launched 2024)","CCB","First Republic-style dedicated banker and concierge service"),
 ("J.P. Morgan Wealth Management","broad; ~6,000 advisors","CCB","Advisors in branches, self-directed investing, Wealth Plan"),
 ("J.P. Morgan Private Bank","~$10m+ (US); ~£10m+ UK (indicative)","AWM","Team-based, global, lending and trust; ~4,100 advisors"),
 ("23 Wall","800+ families, avg net worth ~$5bn","AWM","Institutional-style coverage of the largest families")]
F("wealth_continuum", strip(dg.wealth_continuum(wealth_rows)), "The wealth continuum across CCB and AWM. Thresholds are indicative and vary by market.")
F("awm_hierarchy", ch.awm_hierarchy(), "AWM and Global Private Bank leadership as of September 2026, from the firm's leadership pages, press releases and Investor Day materials. The London team leads are those listed on the firm's London office page.")
F("jcurve", ch.jcurve(), "The advisor J-curve as Erdoes describes it. A new advisor costs money for two to three years, then compounds. The firm says AI-assisted training has made the curve steeper and shorter.")
F("emea", ch.emea_map_list(), "J.P. Morgan Private Bank's EMEA footprint from the firm's locations pages, 2026.")

css=open("style.css").read()
parts=[open(f).read() for f in ["g2_part_1.html","g2_part_2.html","g2_part_3.html","g2_part_5.html","g2_part_6.html","g2_part_7.html","g2_sources.html"]]
body=re.sub(r"\{\{FIG:(\w+)\}\}",lambda m: FIGS[m.group(1)],"\n".join(parts))
cover='''<div class="cover">
<div class="band"><div class="kicker">Application research guide 2 of 2</div>
<h1>Strategy from the Filings, 2021 to 2026</h1>
<div class="sub">What JPMorgan Chase's Form 10-Ks, shareholder letters and Investor Days say about where the firm is going, and a drill-down into Asset &amp; Wealth Management, the Global Private Bank and its International, EMEA and UK business. Written for a candidate for the 2027 Global Private Bank Advisor Summer Internship, London.</div></div>
<div class="meta"><p><strong>Prepared:</strong> 8 September 2026. Latest filing used: Form 10-K for fiscal 2025 (February 2026), the 2025 shareholder letters (April 2026), the February 2026 Company Update and second-quarter 2026 results (July 2026). The firm held no Investor Day in 2026; the next is expected in the first quarter of 2027.</p>
<p><strong>Companion:</strong> Guide 1 explains the role, the firm's structure, competitors, deals and the Private Bank's work from zero knowledge.</p>
<p><strong>How to read:</strong> The executive read and Section 4 give the conclusions. Sections 2 and 3 are the evidence. Section 5 is the AWM material the job posting pointed you to, extended from 2021 to 2025. Section 6 is London. Section 7 turns it into your own words.</p></div></div>
<h2>Contents</h2>
<div class="toc"><ol start="0">
<li>Executive read</li>
<li>How to read a 10-K</li>
<li>Year by year, 2021 to 2026</li>
<li>The ten through-lines, with quotes</li>
<li>Where the firm says it is going</li>
<li>Drill-down: AWM through Mary Erdoes' letters<ul><li>Four ingredients · Letter by letter · Keyword tracker · Targets · Business model · Continuum and hierarchy · Advisor economics · AI</li></ul></li>
<li>Drill-down: International Private Bank, EMEA and the UK</li>
<li>What it means for the Advisor role</li>
</ol><p><strong>Sources</strong></p></div>'''
html=f"<!doctype html><html><head><meta charset='utf-8'><title>Guide 2: Strategy from the Filings 2021 to 2026</title><style>{css}</style></head><body>{cover}{body}</body></html>"
open("guide2.html","w").write(html); print("built",len(html))
