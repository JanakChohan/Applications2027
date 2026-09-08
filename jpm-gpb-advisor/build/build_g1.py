import re, diagrams as dg, charts as ch
from svg import fig

FIGS={}
n=[0]
def F(key, svg, cap):
    n[0]+=1; FIGS[key]=fig(svg,cap,n[0])

wealth_rows=[("Chase retail","everyday banking","CCB","Branches and app; mass market; scale economics"),
 ("Chase Private Client","$150,000+ (US)","CCB","Branch banker plus a J.P. Morgan advisor"),
 ("J.P. Morgan Private Client","$750,000+ (US, launched 2024)","CCB","First Republic-style dedicated banker and concierge service in dedicated offices"),
 ("J.P. Morgan Wealth Management","broad; ~6,000 advisors","CCB","Financial advisors in branches, self-directed investing, Wealth Plan tool"),
 ("J.P. Morgan Private Bank","~$10m+ (US); ~£10m+ UK (indicative)","AWM","Team-based, global, lending and trust, bespoke; ~4,100 advisors"),
 ("23 Wall","800+ families, avg net worth ~$5bn","AWM","Institutional-style coverage of the largest families and family offices")]

# order of figure numbering follows appearance
F("team_model", dg.team_model().split('<div class="cap">')[0].replace('<div class="fig">',''), "The integrated team around one client. The Advisor is the single point of accountability; the specialists are shared across a team's clients. The client experiences one relationship, not five product salespeople.")
F("client_journey", dg.client_journey().split('<div class="cap">')[0].replace('<div class="fig">',''), "The client journey from prospect to multi-generational relationship. Steps 1 to 3 are 'sales'; steps 4 to 7 are 'relationship management'. At J.P. Morgan the same Advisor owns both, which is the point of the role.")
F("internal_workflow", dg.internal_workflow().split('<div class="cap">')[0].replace('<div class="fig">',''), "How the Advisor works with the firm. The Advisor rarely does the technical work; the job is to know the client well enough to bring the right specialist at the right time, and to own the answer that goes back.")
F("firm_org", dg.firm_org().split('<div class="cap">')[0].replace('<div class="fig">',''), "JPMorgan Chase's four lines of business as reported since the 2024 reorganisation. The Global Private Bank sits inside AWM. Chase's own wealth offering for less wealthy clients sits inside CCB, not AWM.")
F("segment_split", ch.bars("FY2025 revenue and net income by segment ($bn, managed basis)",["Consumer & Community Banking","Commercial & Investment Bank","Asset & Wealth Management","Corporate"],[("Revenue",[76.0,78.5,24.1,7.0]),("Net income",[18.2,27.8,6.5,4.5])],fmt=lambda v:f"{v:.0f}",note="Source: FY2025 Form 10-K"), "The CIB is now the largest revenue and profit engine. AWM is small by revenue but earns the firm's highest return on equity (40%).")
F("firm_trend", ch.bars("JPMorgan Chase managed revenue and net income, 2021 to 2025 ($bn)",["2021","2022","2023","2024","2025"],[("Revenue",[125.3,132.3,162.4,180.6,185.6]),("Net income",[48.3,37.7,49.6,58.5,57.0])],fmt=lambda v:f"{v:.0f}",note="2023 includes First Republic from May; 2024 includes a $7.9bn Visa gain"), "Five years of growth. Revenue rose by almost half between 2021 and 2025, driven first by higher interest rates and then by markets and investment banking. Net income dipped in 2022 as loan-loss reserves were rebuilt.")
F("one_firm", ch.one_firm(), "The referral engine around the Global Private Bank. Every arrow runs both ways: the Private Bank also sends its clients' companies to the investment and commercial banks. No internal transfer pricing is applied to these referrals.")
F("wealth_continuum", dg.wealth_continuum(wealth_rows).split('<div class="cap">')[0].replace('<div class="fig">',''), "The wealth ladder inside JPMorgan Chase. As a client's assets grow they move from a branch-based, scaled model in CCB to the bespoke, team-based Private Bank in AWM. Thresholds are indicative and vary by market.")
F("firm_leadership", ch.firm_leadership(), "Senior leadership as of September 2026, after the June 2026 co-president appointments.")
F("rotce_compare", ch.hbars("Return on tangible common equity, FY2025 (%)",["Morgan Stanley","JPMorgan Chase","HSBC (ex-notables)","Goldman Sachs (approx.)","Wells Fargo (approx.)","Bank of America","UBS (underlying)","Barclays","Citigroup"],[21.6,20.0,17.2,15.5,15.0,14.2,13.7,11.3,7.7],unit="%",fmt=lambda v:f"{v:.1f}",highlight="JPMorgan Chase",note="Company reports; GS and Wells approximate"), "Only Morgan Stanley, a wealth-heavy firm with far less balance sheet, earns a higher return than JPMorgan. Among universal banks JPMorgan is alone at 20%.")
F("wealth_peers", ch.hbars("Client assets or invested assets, FY2025 ($tn)",["BlackRock (AUM)","Morgan Stanley Wealth","J.P. Morgan AWM","Bank of America GWIM","UBS Global Wealth","Goldman Sachs AWM","HSBC wealth balances","Citi Wealth balances"],[14.0,9.3,7.1,4.8,4.8,3.6,2.1,1.1],unit="tn",fmt=lambda v:f"${v:.1f}",highlight="J.P. Morgan AWM",note="Different definitions; directional only"), "Scale in wealth and asset management. Morgan Stanley's number is client assets across all its wealth channels; J.P. Morgan's AWM figure excludes Chase Wealth Management's $1.3tn, which sits in CCB.")
F("awm_trend", ch.bars("Asset & Wealth Management: revenue ($bn), client assets ($tn) and Private Bank advisors (thousands), 2021 to 2025",["2021","2022","2023","2024","2025"],[("Revenue $bn",[17.0,17.7,19.8,21.6,24.1]),("Client assets $tn",[4.3,4.0,5.0,5.9,7.1]),("PB advisors (000s)",[2.7,3.1,3.5,3.8,4.1])],fmt=lambda v:f"{v:g}",ymax=28,note="Sources: 10-Ks; Erdoes letters; advisors 2021-23 derived",colors=("#2a78d6","#eb6834","#1baf7a")), "Three measures of AWM's growth on one scale for compactness (units differ per series; read each series against its own label). Revenue up 42%, client assets up 65%, advisors up roughly 50% in five years.")
F("pb_revenue", dg.pb_revenue().split('<div class="cap">')[0].replace('<div class="fig">',''), "The four revenue legs of a private bank relationship. A client with only an investment account is easy to lose; a client with investments, cash, lending and a trust is deeply embedded. This is what 'share of wallet' means in practice.")
F("emea", ch.emea_map_list(), "J.P. Morgan Private Bank's EMEA footprint (offices listed on the firm's EMEA locations pages, 2026).")

css=open("style.css").read()
parts=[open(f).read() for f in ["g1_part_a.html","g1_part_a2.html","g1_part_b.html","g1_part_c.html","g1_part_d.html","g1_part_e.html","g1_part_f.html","g1_glossary.html","g1_sources.html"]]
body="\n".join(parts)
def rep(m):
    return FIGS[m.group(1)]
body=re.sub(r"\{\{FIG:(\w+)\}\}",rep,body)

cover=f'''<div class="cover">
<div class="band"><div class="kicker">Application research guide 1 of 2</div>
<h1>The Advisor, the Private Bank, and JPMorgan Chase</h1>
<div class="sub">A zero-knowledge, in-depth briefing for the 2027 Global Private Bank Advisor Summer Internship, London. What the role is, how the client and internal work flows, what the firm is and why it is built the way it is, how it compares with its rivals, and what its values mean once the marketing is stripped away.</div></div>
<div class="meta"><p><strong>Prepared:</strong> 8 September 2026, for the application closing 1 November 2026 (rolling).</p>
<p><strong>Companion:</strong> Guide 2 covers the firm's strategy from the 2021 to 2025 Form 10-Ks and shareholder letters, and drills into Asset &amp; Wealth Management and the International Private Bank.</p>
<p><strong>How to read:</strong> Sections 1 and 2 first (the role). Then 6 (the division). Then 3 to 5 (the firm and its rivals). Section 7 last. Anything marked "assumption" or "unverified" should be checked with a recruiter or alumnus before you repeat it.</p>
<p><strong>Sources:</strong> JPMorgan Chase Form 10-K filings (FY2021 to FY2025), shareholder letters, Investor Day transcripts (2022 to 2025), the February 2026 Company Update, quarterly earnings through Q2 2026, J.P. Morgan Private Bank websites, and the press. Full list in Appendix B. Figures are as reported by the firm unless stated; peer figures come from their own reports.</p></div></div>
<h2>Contents</h2>
<div class="toc"><ol>
<li>The role, explained from zero</li>
<li>How the work flows: client, Advisor, and the firm behind them<ul><li>The team around one client · The client journey · Working with internal teams · The nine weeks · A week for an Advisor</li></ul></li>
<li>What JPMorgan Chase is<ul><li>History · The four lines of business · Why sectors sit where they do · The "one firm" engine · The wealth ladder · Leadership · Culture stripped down</li></ul></li>
<li>Competitor analysis by division</li>
<li>Acquisitions, investments and what the firm has not done</li>
<li>The Global Private Bank in depth<ul><li>Numbers · Clients · What we help with and why they come · Sales to relationship · Values stripped down · The London market · The house view</li></ul></li>
<li>Turning it into your own reasons</li>
</ol>
<p><strong>Appendix A</strong> Glossary<br><strong>Appendix B</strong> Sources</p></div>'''

html=f"<!doctype html><html><head><meta charset='utf-8'><title>Guide 1: The Advisor, the Private Bank and JPMorgan Chase</title><style>{css}</style></head><body>{cover}{body}</body></html>"
open("guide1.html","w").write(html)
print("built", len(html))
