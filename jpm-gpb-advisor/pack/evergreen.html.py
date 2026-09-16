import re, diagrams3 as d3, charts as ch
n=[0]
def F(svg,cap):
    n[0]+=1; return f'<div class="fig">{svg}<div class="cap"><b>Figure {n[0]}.</b> {cap}</div></div>'
css=open("pack_style.css").read()+"""
body{font-size:10.4pt} h2{margin-top:16pt} .big{font-size:12pt;line-height:1.5;color:#0b2545}
.tl td:first-child{white-space:nowrap;font-weight:700;color:#0b2545;width:15%}
.script{border:1px solid #d6dbe3;border-radius:4pt;padding:9pt 12pt;margin:8pt 0;background:#fff}
.script .seg{display:flex;gap:10pt;margin-bottom:7pt;break-inside:avoid}
.script .tm{flex:0 0 58pt;font-size:8pt;color:#8a6414;font-weight:700;text-transform:uppercase;letter-spacing:.5px;padding-top:2pt}
.script .tx{flex:1;font-size:10.2pt;line-height:1.5}
.script .tx b{color:#0b2545}
.notes{font-family:monospace;font-size:9pt;background:#f4f6f9;padding:6pt 10pt;border-radius:4pt;white-space:pre-line;break-inside:avoid}
table.src td:first-child{white-space:nowrap} table.src td{overflow-wrap:anywhere;word-break:normal} table.src{font-size:7pt} .s{margin-left:1pt}
"""
# ---------- sources actually cited ----------
S={
"S500":("Blue Owl (ocic.com)","Blue Owl Credit Income Corp. fund page: repurchase terms, fees, portfolio","2026","https://ocic.com/","READ","High"),
"S501":("Blackstone (bcred.com)","BCRED offering terms (2% early repurchase deduction)","undated","https://www.bcred.com/offering-terms/","Snippet only","Med"),
"S502":("NBER, Fang, Goldstein and Zeng","The Fragility of Semi-Liquid Private Credit Funds (w35385)","2026","https://www.nber.org/papers/w35385","Abstract only","Med"),
"S503":("Morningstar","Semiliquid fund market nears $600bn as private credit loses steam","2026-06-16","https://newsroom.morningstar.com/news/news-details/2026/Morningstar-Report-Finds-Semiliquid-Fund-Market-Nears-600-Billion-as-Private-Credit-Loses-Steam/default.aspx","READ","High"),
"S504":("Preqin","Evergreen funds set off at record-breaking pace in 2026","2026-02-27","https://www.preqin.com/news/evergreen-funds-set-off-at-record-breaking-pace-in-2026","READ","High"),
"S506":("Alternative Credit Investor","LTAFs gain ground as retail access to private markets widens","2026-04-07","https://alternativecreditinvestor.com/2026/04/07/ltafs-gain-ground-as-retail-access-to-private-markets-widens/","READ","High"),
"S507":("IMF","Global Financial Stability Report press briefing, Spring Meetings 2026","2026-04-14","https://www.imf.org/en/news/articles/2026/04/15/tr-04142026-press-briefing-transcript-global-financial-stability-report-spring-meetings-2026","Snippet only","Med"),
"S508":("Financial Stability Board","FSB warns on private credit vulnerabilities","2026-05-06","https://www.fsb.org/2026/05/fsb-warns-on-private-credit-vulnerabilities/","READ","High"),
"S509":("WealthManagement.com","iCapital data shows private investors shying away from private credit","2026-06-04","https://www.wealthmanagement.com/alternative-investments/icapital-data-shows-private-investors-shying-away-from-private-credit","READ","High"),
"S510":("InvestmentNews","Blackstone REIT hits key milestone, lifts redemption limit","2024-03-01","https://www.investmentnews.com/alternatives/blackstone-reit-hits-key-milestone-lifts-redemption-limit/250253","READ","High"),
"S511":("AltsWire","Starwood REIT suspends most redemptions, cuts distribution","2026-04-29","https://altswire.com/starwood-reit-suspends-most-redemptions-cuts-distribution/","READ","High"),
"S513":("Fortune","Jamie Dimon: 'When you see one cockroach, there are probably more'","2025-10-15","https://fortune.com/2025/10/15/jamie-dimon-issues-private-credit-warning-when-you-see-one-cockroach-there-are-probably-more","READ","High"),
"S514":("InvestmentNews","Blue Owl faces investor suit over BDC redemptions, liquidity, merger","2025-12-10","https://www.investmentnews.com/ria-news/blue-owl-faces-investor-suit-over-bdc-redemptions-liquidity-merger/263501","READ","High"),
"S515":("BIS Quarterly Review","Private credit's software lending meets AI disruption","2026-03-16","https://www.bis.org/publ/qtrpdf/r_qt2603v.htm","READ","High"),
"S516":("AltsWire","Blue Owl sells $1.4bn in loans, halts OBDC II redemptions, shifts to capital returns","2026-02-19","https://altswire.com/blue-owl-sells-1-4b-in-loans-halts-obdc-ii-redemptions-and-shifts-to-capital-returns/","READ","High"),
"S518":("AltsWire","Blackstone's BCRED meets record 7.9% redemption requests","2026-03-03","https://altswire.com/blackstones-bcred-meets-record-7-9-redemption-requests/","READ","High"),
"S519":("Fortune","The $265 billion private credit meltdown","2026-03-14","https://fortune.com/2026/03/14/private-credit-meltdown-how-wall-streets-blackstone-kkr-apollo-ares-blue-owl-investment-craze-panic/","READ","High"),
"S520":("Bloomberg via WealthManagement.com","Private credit funds trap $5 billion as investors rush for exit","2026-03-26","https://www.wealthmanagement.com/alternative-investments/private-credit-funds-trap-5-billion-as-investors-rush-for-exit","READ","High"),
"S521":("Semafor","Blue Owl credit funds face heavy redemption requests as private credit jitters persist","2026-04-02","https://www.semafor.com/article/04/02/2026/blue-owl-credit-funds-face-heavy-redemption-requests-as-private-credit-jitters-persist","READ","High"),
"S522":("CNBC","Blue Owl caps private credit funds redemptions at 5% after steep request levels","2026-04-02","https://www.cnbc.com/2026/04/02/blue-owl-private-credit-funds-redemptions-requests.html","Snippet only","Med"),
"S523":("Financial Times (via @FT on X)","Blue Owl struck by $5.4bn of redemption requests","c. 2026-04-02","https://x.com/FT/status/2039683943423713376","PAYWALLED-NOT-READ","Med"),
"S524":("Private Equity Wire, citing FT","Private credit fund redemption requests topped $20bn in Q1","2026-04-09","https://www.privateequitywire.co.uk/private-credit-fund-redemption-requests-topped-20bn-in-q1/","READ","High"),
"S525":("Financial Times (via Seeking Alpha)","Private credit funds face massive redemption wave as wealthy investors head for exits","c. 2026-04-09","https://seekingalpha.com/news/4564712-private-credit-funds-face-massive-redemption-wave-as-wealthy-investors-head-for-exits---ft","PAYWALLED-NOT-READ","Med"),
"S527":("CNBC","'You're an idiot': Marc Rowan on lenders that cannot meet 5% redemptions","2026-04-16","https://www.cnbc.com/2026/04/16/apollo-global-marc-rowan-private-credit-funds-redemptions.html","Snippet only","Med"),
"S528":("Partners Group","Partners Group expects solid net AuM growth for 2026 despite recent uncertainty around evergreen redemptions","2026-06-04","https://www.partnersgroup.com/en/news-and-views/press-releases/corporate-news/detail?news_id=60379ff3-2bcb-4c37-a781-6c1ab170b16b","READ","High"),
"S529":("Bloomberg Law","Blue Owl fund hit by redemptions sells $500 million bonds","2026-06-08","https://news.bloomberglaw.com/banking-law/blue-owl-fund-hit-by-redemptions-set-to-sell-500-million-bond","READ","High"),
"S530":("AltsWire","Apollo Debt Solutions BDC caps Q2 redemptions at 5% as requests hit 16.8%","2026-06","https://altswire.com/apollo-debt-solutions-bdc-caps-q2-redemptions-at-5-as-withdrawal-requests-hit-16-8/","Snippet only","Med"),
"S532":("Alternative Credit Investor","Goldman BDC bucks wider redemption trend","2026-07-01","https://alternativecreditinvestor.com/2026/07/01/goldman-bdc-bucks-wider-redemption-trend/","READ","High"),
"S533":("Semafor","Blue Owl hit by billions in redemptions, again","2026-07-02","https://www.semafor.com/article/07/02/2026/blue-owl-hit-by-billions-in-redemptions-again","READ","High"),
"S534":("AltsWire","Blue Owl BDCs hit by $4.7bn in redemption requests as demand eases","2026-07-05","https://altswire.com/blue-owl-bdcs-draw-4-7b-in-combined-redemption-requests-as-demand-eases/","READ","High"),
"S535":("Financial Times (via @FT on X)","Big investors commit billions to private credit despite turmoil","2026-07-06","https://x.com/FT/status/2073982807827718637","PAYWALLED-NOT-READ","Med"),
"S536":("AltsWire","BCRED caps Q3 repurchases at 5% as requests hit $4.3bn, about 10% of shares","2026-09-03","https://altswire.com/bcred-caps-q3-repurchases-at-5-as-requests-hit-4-3b-about-10-of-shares/","READ","High"),
"S538":("Bank of England","Financial Stability Report, July 2026","2026-07-07","https://www.bankofengland.co.uk/financial-stability-report/2026/july-2026","READ","High"),
"S539":("European Central Bank","Stress in global private credit markets and its implications for euro area financial stability","2026-05","https://www.ecb.europa.eu/press/financial-stability-publications/fsr/special/html/ecb.fsrart202605_04~3f2135af91.en.html","READ","High"),
"S540":("Partners Group","H1 2026 results and rotations to the Executive Team (Cagnati and Jenkner co-CEOs)","2026-09-01","https://www.partnersgroup.com/en/news-and-views/press-releases/corporate-news/detail?news_id=92e4c08c-6c4e-48d8-88df-ee5389b89641","READ","High"),
"S541":("Reuters via Yahoo Finance","Partners Group replaces CEO as it works through evergreen fund redemptions","2026-09-01","https://finance.yahoo.com/markets/stocks/articles/partners-group-replaces-ceo-works-125844835.html","READ","High"),
"S543":("Bloomberg via swissinfo.ch","Partners Group management reshuffle leaves investors unimpressed","2026-09-01","https://www.swissinfo.ch/eng/partners-group-management-reshuffle-leaves-investors-unimpressed/91986026","READ","High"),
"S546":("Bloomberg via swissinfo.ch","Partners Group likely to cap flagship US evergreen fund","2026-06-04","https://www.swissinfo.ch/eng/partners-group-likely-to-cap-flagship-us-evergreen-fund/91525795","READ","High"),
"S548":("SEC EDGAR","Partners Group Private Equity Fund, LLC: offer to repurchase ~5% of net assets","2026-04-28","https://www.sec.gov/Archives/edgar/data/1447247/000139834426007393/fp0098689-1_ex9912b.htm","READ","High"),
"S549":("Reuters via AOL","Partners Group expects evergreen fund withdrawals to continue after June turmoil","2026-07-16","https://www.aol.com/articles/partners-group-readout-private-equity-101107000.html","READ","Med"),
"S550":("Reuters via Global Banking & Finance","Partners Group may trim evergreen fund size amid withdrawal caps","2026-06-25","https://www.globalbankingandfinance.com/partners-group-considers-slightly-smaller-evergreen-funds/","READ","Med"),
"S554":("Reuters via U.S. News","Blue Owl's Lipschultz dismisses concerns over AI disrupting software businesses","2026-02-05","https://money.usnews.com/investing/news/articles/2026-02-05/blue-owl-beats-profit-estimates-aum-crosses-300-billion-milestone","Snippet only","Med"),
"S556":("Yahoo Finance","Blue Owl sinks 68.2% from peak as redemptions surge in private credit","2026-04-02","https://finance.yahoo.com/markets/stocks/articles/blue-owl-sinks-68-2-165700127.html","READ","Med"),
"S557":("Blue Owl Capital","Q1 2026 earnings call transcript","2026-04-30","https://s202.q4cdn.com/477831904/files/doc_financials/2026/q1/Blue-Owl_1Q26_Full-Transcript_20260430.pdf","READ","High"),
"S560":("SEC EDGAR, Blue Owl Credit Income Corp 8-K","OCIC Q2 2026 shareholder update and tender results","2026-07-02","https://www.sec.gov/Archives/edgar/data/0001812554/000119312526293509/d16628dex991.htm","READ","High"),
"S563":("Investing.com","Blue Owl Capital Q2 2026 earnings call transcript","2026-07-30","https://www.investing.com/news/transcripts/earnings-call-transcript-blue-owl-capital-tops-revenue-estimates-in-q2-2026-93CH-4825378","READ","Med"),
"S564":("Equibles","Blue Owl Capital Q2 2026 earnings call transcript (AUM, capital raised)","2026-07-30","https://equibles.com/stocks/owl/calls/2026-q2","READ","Med"),
"S565":("Blue Owl Capital","OCIC repurchase offers page (Q3 2026 tender open 1 to 30 September)","2026-09","https://www.blueowl.com/repurchase-offers-ocic","READ","High"),
"S569":("The Irish Times","Private credit losses will be larger than feared, JPMorgan Chase boss warns (2026 shareholder letter)","2026-04-07","https://www.irishtimes.com/business/financial-services/2026/04/07/private-credit-losses-will-be-larger-than-feared-jp-morgan-chase-boss-warns/","READ","High"),
"S570":("PYMNTS","Dimon: private credit 'large but contained' (Q1 2026 call)","2026-04-14","https://www.pymnts.com/earnings/2026/jpmorgan-ceo-dimon-says-private-credit-wont-break-the-system-yet","READ","Med"),
"S572":("JPMorgan Chase","J.P. Morgan increases direct lending commitment to $50 billion","2025-02-24","https://www.jpmorgan.com/about-us/corporate-news/2025/jpmorgan-increases-direct-lending-commitment-to-50-billion","READ","High"),
"S574":("Euromoney","The world's best for alternative investments 2026: JPMorgan Private Bank","2026-03-20","https://www.euromoney.com/article/4g5m6u1urreockw0c0s4o4c44/private-banking/the-worlds-best-for-alternative-investments-2026-jpmorgan-private-bank/","READ","High"),
"S575":("JPMorgan Chase","2025 Investor Day, Asset & Wealth Management transcript (Erdoes on evergreens)","2025-05-19","https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/events/2025/jpmc-2025-investor-day/awm.pdf","READ","High"),
"S576":("J.P. Morgan Private Bank","Private credit under the microscope: separating headlines from fundamentals","2026-03-12","https://privatebank.jpmorgan.com/nam/en/insights/markets-and-investing/private-credit-under-the-microscope-separating-headlines-from-fundamentals","READ","High"),
"S577":("J.P. Morgan Private Bank","Private credit still earns its place in portfolios, with the right approach","2026-04-16","https://privatebank.jpmorgan.com/eur/en/insights/markets-and-investing/ideas-and-insights/private-credit-still-earns-its-place-in-portfolios-with-the-right-approach","READ","High"),
"S578":("J.P. Morgan, Michael Cembalest","The Deep End: 2025 Alternative Investments Review","2025-12-02","https://privatebank.jpmorgan.com/nam/en/insights/latest-and-featured/eotm/the-deep-end","READ","High"),
"S579":("Boursorama (JPMAM release)","J.P. Morgan AM launches JPMorgan Private Markets Fund and JPMorgan Credit Markets Fund for EMEA wealth clients","2026-09-15","https://www.boursorama.com/bourse/actualites/j-p-morgan-am-elargit-son-offre-dans-le-private-equity-et-la-dette-privee-2a57b6affd00b260acaf20debad334a1","READ","Med"),
"S580":("Private Equity Wire","SEC approves Blackstone's evergreen multi-asset credit fund (BMACX)","2025-03-11","https://www.privateequitywire.co.uk/sec-approves-blackstones-evergreen-multi-asset-credit-fund/","READ","High"),
"S582":("Investing.com","Blackstone Q2 2026 earnings call transcript","2026-07-23","https://www.investing.com/news/transcripts/earnings-call-transcript-blackstone-tops-q2-2026-estimates-on-fees-aum-growth-93CH-4809469","READ","High"),
"S584":("SEC EDGAR, BCRED","BCRED Q3 2026 tender offer shareholder letter","2026-09-03","https://www.sec.gov/Archives/edgar/data/0001803498/000121390026096935/ea0244647-03_ex99a1vii.htm","READ","High"),
"S585":("SEC EDGAR, BCRED","BCRED Q2 2026 tender offer shareholder letter","2026-06-04","https://www.sec.gov/Archives/edgar/data/1803498/000121390026065024/ea0292864-01_ex99a1vii.htm","READ","High"),
"S587":("BNN Bloomberg","Blackstone private credit fund caps withdrawals as redemption requests jump","2026-06-04","https://www.bnnbloomberg.ca/investing/2026/06/04/blackstone-private-credit-fund-caps-withdrawals-as-redemption-requests-surge/","READ","High"),
"S589":("AltsWire","Ares Strategic Income Fund caps Q2 tender at 5% as demand reaches 14.4%","2026-06-25","https://altswire.com/ares-strategic-income-fund-caps-q2-tender-at-5-as-redemption-demand-reaches-14-4/","READ","High"),
"S590":("Vanguard","Wellington, Vanguard and Blackstone launch two investment solutions (WVB funds)","2026-07-22","https://corporate.vanguard.com/content/corporatesite/us/en/corp/who-we-are/pressroom/press-release-wellington-vanguard-and-blackstone-launch-two-investment-solutions-simplifying-access-to-public-and-private-markets-072226.html","READ","High"),
"S593":("HedgeCo","Blackstone debuts hedge fund for 'mini-millionaires' (BXHF)","2026-04-01","https://hedgeco.net/news/04/2026/blackstone-debuts-hedge-fund-for-mini-millionaires.html","READ","Med"),
"S597":("Private Equity Wire","Blackstone and KKR evergreen funds for wealth investors attract institutional backers","2026-08-26","https://www.privateequitywire.co.uk/blackstone-and-kkr-evergreen-funds-for-wealth-investors-attract-institutional-backers/","READ","High"),
"S599":("Alt Goes Mainstream","Alts & Wealth weekly roundup, 28 Aug 2026 (FT headlines)","2026-08-28","https://altgoesmainstream.substack.com/p/agm-alts-and-wealth-weekly-news-roundup-1c8","READ","Med"),
"S601":("AltsWire","Private wealth push propels Blackstone to record 2025 performance","2026-01-29","https://altswire.com/private-wealth-push-propels-blackstone-to-record-2025-performance/","READ","High"),
"S604":("WealthManagement.com","Evergreen funds reach $607bn despite redemptions (Morningstar/PitchBook)","2026 Q2","https://www.wealthmanagement.com/alternative-investments/evergreen-funds-grow-to-607b-despite-redemptions","READ","Med"),
"S608":("Money Marketing","LTAFs gain ISA access as retail push gathers pace","2026-04-07","https://www.moneymarketing.co.uk/news/ltafs-gain-isa-access-as-retail-push-gathers-pace/","READ","High"),
"S612":("Reuters via Investing.com","BlackRock (HPS) private credit fund redemption requests fall in third quarter","2026-09-11","https://www.investing.com/news/stock-market-news/blackrock-private-credit-fund-redemptions-fall-in-third-quarter-4897830","READ","High"),
"S613":("J.P. Morgan Private Bank","The new frontier: 3 themes driving alternatives in 2026","2026-01-15","https://privatebank.jpmorgan.com/nam/en/insights/markets-and-investing/ideas-and-insights/the-new-frontier-3-themes-driving-alternatives-in-2026","READ","High"),
"S614":("iCapital","BDC redemptions: looking beyond the gates","2026-03-03","https://icapital.com/insights/investment-market-strategy/bdc-redemptions-looking-beyond-the-gates/","READ","High"),
"S616":("Alt Goes Mainstream","Alts & Wealth weekly roundup, 4 Sept 2026 (FT and Bloomberg headlines)","2026-09-04","https://altgoesmainstream.substack.com/p/agm-alts-and-wealth-weekly-news-roundup-46e","READ","Med"),
"S620":("Financial Times (via @FT on X)","Blue Owl permanently halts redemptions at fund aimed at retail investors","2026-02-18","https://x.com/FT/status/2024300963289297115","PAYWALLED-NOT-READ","Med"),
}
figs={
 "structures": F(d3.structures(),"The old model and the new one. A drawdown fund locks money for ten years. An evergreen fund takes money every month and offers to buy back at most about 5% of its shares each quarter [S500][S502]."),
 "chain": F(d3.chain(),"The four links between a private company's loan and a private-bank client's statement. J.P. Morgan's Private Bank is link 3, the gatekeeper, and also links 1 and 2 through its own lending and fund arms [S572][S574][S579]."),
 "gate": F(d3.gate(),"What a binding cap does. In Q1 2026 Blue Owl's flagship fund had requests for 21.9% of shares and paid 5%, so each investor got about 23 cents on the dollar and had to ask again [S521][S560]."),
 "mismatch": F(d3.mismatch(),"The mismatch in one picture. Illiquid assets on the left, quarterly promises on the right, and the 5% cap as the only thing holding them together [S502][S538]."),
 "cash": F(d3.sources_of_cash(),"How a manager finds the cash. Blue Owl used steps 2 to 5 in 2026: subscriptions, repayments, a $500m bond and a $1.4bn loan sale. OBDC II went to step 6 [S516][S529][S560]."),
 "requests": F(d3.requests_chart([('Blue Owl OTIC (software loans)',38.1,5),('Blue Owl OCIC (flagship)',18.8,5),('Apollo Debt Solutions',16.8,5),('Ares Strategic Income',14.4,5),('HPS Corporate Lending',13.3,5),('Blackstone BCRED',10,5),('Partners Group Global Value',9.8,5),('Oaktree BDC',4.5,None),('Goldman Sachs BDC',3.24,None)]),"Second-quarter 2026 redemption requests as a share of each fund, against the 5% cap. Seven of the nine largest wealth funds paid only the cap. Requests are quarterly; the cap is quarterly [S530][S532][S534][S536][S589][S612][S528]."),
 "blueowl": F(ch.bars("Blue Owl's two wealth funds: requested against paid, % of shares, by quarter",["OCIC Q1 26","OCIC Q2 26","OTIC Q4 25","OTIC Q1 26","OTIC Q2 26"],[("Requested",[21.9,18.8,15.4,40.7,38.1]),("Paid (cap)",[5,5,5,5,5])],unit="%",h=280,note="OTIC Q4 2025 figure reported by CNBC; fully paid that quarter is not confirmed"),"The Blue Owl numbers. Requests fell slightly from Q1 to Q2, which management called proof the worst had passed. The share of each request actually paid was 23% then 27% at OCIC and 12% then 13% at OTIC [S522][S534][S560]."),
}
def box(kind,title,body): return f'<div class="box {kind}"><div class="t">{title}</div>{body}</div>'
body=f"""
<div class="cover" style="height:250mm">
<div class="band"><div class="kicker">Commercial awareness brief</div>
<h1>Evergreen Private Credit Funds and the 2026 Redemption Squeeze</h1>
<div class="sub">What these funds are, why investors cannot get their money out, what happened at Blue Owl, Partners Group and Blackstone, what regulators and J.P. Morgan say, and a two-minute HireVue answer that uses all of it. Zero knowledge assumed, nothing you do not need.</div></div>
<div class="meta"><p><strong>Prepared:</strong> 16 September 2026, for the 2027 Global Private Bank Advisor Summer Internship, London.</p>
<p><strong>Reading order:</strong> Section 1 is the story in one page. Sections 2 and 3 teach the product and the 5% rule. Sections 4 to 7 are the cases. Section 8 is J.P. Morgan's position. Section 9 is the answer, with timings and screen notes. Section 10 is the reading list, including the FT pieces.</p>
<p><strong>Honesty note:</strong> the FT's site is closed to the tools used here, so FT headlines are recorded from the FT's own social posts and secondary coverage and marked PAYWALLED-NOT-READ. Everything with a number carries a source marker [Sxxx] that resolves in Section 11. Blue Owl's third-quarter tender closes on 30 September, so its Q3 figures do not exist yet [S565].</p></div></div>

<h2>1. The story in one page</h2>
<p class="big">Over the last five years private credit managers built a new kind of fund for wealthy individuals: it never closes, takes money every month, and offers to hand back up to 5% of the fund each quarter. In 2026 far more than 5% asked at once. The managers paid the 5% and no more. Investors discovered that "semi-liquid" means liquid at the manager's pace, and the argument about whether that is a broken promise or the product working as designed is the story.</p>
<div class="kpi">
<div><div class="v">$607bn</div><div class="l">in semi-liquid evergreen funds at March 2026, across 567 funds, more than double 2022 [S604][S503]</div></div>
<div><div class="v">5%</div><div class="l">of shares a fund will buy back per quarter, at most, and only if its board chooses to [S500]</div></div>
<div><div class="v">$20.8bn</div><div class="l">of redemption requests in Q1 2026 across funds managing ~$300bn; just over half honoured (FT count) [S524]</div></div>
<div><div class="v">21.9% / 40.7%</div><div class="l">Q1 requests at Blue Owl's flagship and software funds. Both paid 5% [S522]</div></div>
</div>
<table>
<tr><th style="width:26%">What happened</th><th>The short version</th></tr>
<tr><td>The trigger</td><td>Two lender collapses in autumn 2025 (Tricolor, First Brands) and then an AI-driven sell-off in software companies, which are 19% of direct loans. Jamie Dimon's line, "when you see one cockroach, there are probably more", set the tone [S513][S515].</td></tr>
<tr><td>The run</td><td>Wealthy investors, mostly through private banks and advisers, asked for their money back at the same time. Q1 2026 requests topped $20bn. Blue Owl, Apollo, Ares, HPS, Morgan Stanley and later Blackstone and Partners Group all paid only the 5% cap [S520][S524][S528][S587].</td></tr>
<tr><td>The damage</td><td>Listed alternative managers lost about $265bn of market value from September 2025 to March 2026; Blue Owl fell two-thirds from its peak. Partners Group's shares fell about a third in 2026 and it replaced its CEO on 1 September [S519][S556][S541].</td></tr>
<tr><td>The defence</td><td>The loans are mostly fine. Blue Owl's flagship has 0.2% of loans not paying. The cap exists to stop a rush for the exit forcing fire sales that would hurt whoever stays. Jon Gray: "a feature, not a bug". Marc Rowan: a first-lien manager that cannot meet 5% a quarter is "an idiot" [S560][S519][S527].</td></tr>
<tr><td>Where it is now</td><td>Requests eased in Q2 and Q3 at most funds but stayed above the cap at Blue Owl, Blackstone, Apollo and Ares. Institutions are buying what individuals sell. Blackstone, Vanguard and J.P. Morgan launched new evergreens anyway, the latest on 15 September [S612][S535][S590][S579].</td></tr>
</table>

<h2>2. What an evergreen fund is, from zero</h2>
<p><strong>Private credit</strong> is lending to companies by funds rather than banks. The borrower is usually a mid-sized company owned by a private equity firm; the loan is "senior secured" (first in line, backed by the company's assets), floating rate, and lasts five to seven years. There is no public market for these loans, so they cannot be sold in an afternoon [S500][S515].</p>
<p><strong>The old wrapper</strong> was a closed-end fund: an insurer or pension fund commits money for about ten years, the manager draws it down as loans are made, and the money comes back only as the loans repay. Nobody can redeem. <strong>The new wrapper</strong>, the evergreen or semi-liquid fund, has no end date, prices itself once a month at net asset value (NAV, the manager's estimate of what the loans are worth), accepts new money every month, and offers a quarterly exit window capped at about 5% of the fund [S500][S502]. In the United States the usual legal form is a non-traded business development company (BDC) such as Blue Owl's OCIC or Blackstone's BCRED; in Europe it is an ELTIF or a Luxembourg fund; in the UK, a Long-Term Asset Fund (LTAF), which became ISA-eligible in April 2026 [S506][S608].</p>
{figs["structures"]}
<p><strong>Why the wrapper was invented.</strong> Institutions were already full of private credit. The next $80tn or so sits with wealthy individuals, who will not lock money for ten years or take capital calls, but will buy a fund that pays 9 to 11% income monthly and lets them sell "when they need to". Managers earn a management fee of about 1.25% plus 12.5% of income, on a base that grows every month and never has to be re-raised; Morningstar puts the all-in cost near 3% [S500][S503]. Preqin counted a record 123 evergreen launches in 2025 and 30 in the first two months of 2026 [S504].</p>
{figs["chain"]}
<dl class="glossary">
<dt>NAV</dt><dd>Net asset value: the manager's monthly estimate of the portfolio's worth per share. Private loans have no market price, so NAV is a judgment with a third-party check.</dd>
<dt>Tender / repurchase offer</dt><dd>The quarterly window in which the fund offers to buy back shares. Not an obligation for most structures.</dd>
<dt>Gate / cap</dt><dd>The limit on how much the fund will buy back, usually 5% of shares per quarter. "Gating" is the cap binding.</dd>
<dt>Pro rata</dt><dd>When requests exceed the cap, everyone gets the same fraction of what they asked for. The remainder is cancelled, not queued; you tender again next quarter.</dd>
<dt>Non-traded BDC</dt><dd>The US legal form of most wealth private credit funds. Registered with the SEC but not listed on an exchange.</dd>
<dt>Senior secured / first lien</dt><dd>The loan is first in line for repayment and backed by the company's assets. Losses are rare but recoveries take time.</dd>
<dt>Non-accrual</dt><dd>A loan that has stopped paying interest. OCIC's were 0.2% of the portfolio in June 2026 [S560].</dd>
<dt>Illiquidity premium</dt><dd>The extra return for accepting that you cannot sell. The manager's argument: if the fund had to sell to meet every request, that premium would vanish.</dd>
<dt>Early repurchase deduction</dt><dd>A charge, typically 2% of NAV, for selling within a year of buying [S501].</dd>
<dt>ELTIF / LTAF</dt><dd>The European and UK regulated wrappers for retail access to private assets. ELTIF assets reached €34bn at end-2025; 25 LTAFs hold £7.3bn [S506][S608].</dd>
</dl>

<h2>3. The 5% rule and why it matters</h2>
<p class="big">The whole story sits in one sentence from OCIC's own terms: the fund "intends to repurchase once per quarter no more than 5% of our outstanding shares" [S500]. Intends, not must. No more than 5%, not 5%. Everything in 2026 followed from investors reading that as a promise and managers reading it as a ceiling.</p>
{figs["gate"]}
<p>The reason the cap exists is the mismatch between what the fund owns and what it has offered. The NBER paper that economists now cite finds that cash buffers and loan repayments cannot fund repeated 5% quarterly outflows, that new money dries up exactly when redemptions rise, and that shortfalls are met by selling loans, borrowing and delaying payment, which shifts cost onto whoever stays and creates the incentive to be first out, the mechanics of a bank run [S502].</p>
{figs["mismatch"]}
{figs["cash"]}
<p><strong>The template everyone had already seen.</strong> Blackstone's property fund BREIT hit its cap in November 2022 and prorated for fifteen months, returning more than $15bn before lifting the cap in March 2024 once requests had fallen 82% from the peak. Starwood's rival property fund did worse: it cut the cap to a third of a percent a month in 2024, then in April 2026 suspended repurchases for most investors and cut its dividend [S510][S511]. Private credit managers told investors in 2025 that their loans were far more liquid than buildings. 2026 was the test.</p>

<h2>4. What happened, in order</h2>
<table class="tl">
<tr><th>Date</th><th>Event</th></tr>
<tr><td>Sep to Oct 2025</td><td>Tricolor (subprime car loans) and First Brands (car parts) collapse within weeks, the latter with hidden financing. JPMorgan takes about $170m of Tricolor losses. Dimon on the Q3 call: "When you see one cockroach, there are probably more" [S513].</td></tr>
<tr><td>5 to 19 Nov 2025</td><td>Blue Owl tries to fold its non-traded fund OBDC II into its listed fund. Because the listed fund trades below NAV, the FT reports a potential 20% haircut for OBDC II holders. The deal is scrapped in two weeks. A class action follows [S514].</td></tr>
<tr><td>Oct 2025 to Feb 2026</td><td>Software stocks fall about 30% on fears that AI will replace the products of the companies private credit lends to. Software loans had grown from about $8bn in 2015 to over $500bn, 19% of all direct loans [S515].</td></tr>
<tr><td>19 Feb 2026</td><td>Blue Owl sells $1.4bn of loans at 99.7 cents on the dollar to four pension and insurance buyers and permanently halts redemptions at OBDC II, replacing them with a return of about 30% of capital. FT headline: "Blue Owl permanently halts redemptions at fund aimed at retail investors" [S516][S620].</td></tr>
<tr><td>2 to 3 Mar 2026</td><td>Blackstone's BCRED receives a record 7.9% of requests, lifts its cap to 7% and, with employees, buys about $400m of shares to pay everyone in full. Its credit head Brad Marshall: investors "should never buy these products if they expect 100% liquidity" [S518].</td></tr>
<tr><td>23 to 26 Mar 2026</td><td>Apollo (11.2%) and Ares (11.6%) cap at 5%; Cliffwater and Morgan Stanley gate too. Bloomberg tallies $13bn of requests and $4.6bn "trapped" [S520].</td></tr>
<tr><td>2 Apr 2026</td><td>Blue Owl: OCIC requests 21.9%, OTIC 40.7%, both capped at 5%. Its shares close 68% below the January 2025 peak. FT: "Blue Owl struck by $5.4bn of redemption requests" [S522][S556][S523].</td></tr>
<tr><td>9 Apr 2026</td><td>FT count: $20.8bn of Q1 requests across funds managing about $300bn, just over half honoured. Headline: "Private credit funds face massive redemption wave as wealthy investors head for exits" [S524][S525].</td></tr>
<tr><td>16 Apr 2026</td><td>Marc Rowan (Apollo): "If you can't, as a first lien credit manager, meet 5% redemptions per quarter... you're an idiot" [S527].</td></tr>
<tr><td>3 to 4 Jun 2026</td><td>Partners Group gates its flagship Global Value fund (9.8% requests) and prepares to cap its $15.8bn US fund; shares fall 18% in a day. BCRED's Q2 requests hit about 10% and it pays 5% [S528][S546][S587].</td></tr>
<tr><td>8 Jun 2026</td><td>OCIC sells $500m of five-year bonds to repay debt, priced at 255 basis points over Treasuries [S529].</td></tr>
<tr><td>1 to 6 Jul 2026</td><td>Q2 tenders: Blue Owl 18.8% and 38.1%, Apollo 16.8%, Ares 14.4%, HPS 13.3%; Goldman's fund gets 3.2% and pays in full. FT: institutions committed at least $16bn to direct-lending funds in Q2 while wealth funds got over $22bn of requests [S534][S530][S589][S532][S535].</td></tr>
<tr><td>1 Sep 2026</td><td>Partners Group names Roberto Cagnati and Juri Jenkner co-CEOs from January 2027; David Layton becomes CIO. Performance fees down 39%, profit down 13%, shares down about 32% in the year. Reuters: "Partners Group replaces CEO as it works through evergreen fund redemptions" [S540][S541].</td></tr>
<tr><td>3 Sep 2026</td><td>BCRED's third straight quarter above the cap: $4.3bn, about 10%, paid at 5%. Jon Gray: "We went through this with BREIT... we're going to go through this with BCRED" [S536].</td></tr>
<tr><td>11 to 15 Sep 2026</td><td>HPS reports Q3 requests falling to 11.5% and says the backlog is clearing. J.P. Morgan Asset Management launches two new evergreens for European wealth clients. Blue Owl's Q3 tender is open until 30 September [S612][S579][S565].</td></tr>
</table>
{figs["requests"]}

<h2>5. Case one: Blue Owl</h2>
<p>Blue Owl is a New York manager with about $319bn under management, run by co-CEOs Doug Ostrover and Marc Lipschultz, and one of the biggest direct lenders to software companies. Its two wealth funds are OCIC, the diversified flagship of about $36bn of investments, and OTIC, a $5bn to $6bn fund of loans to technology companies [S564][S560][S522].</p>
{figs["blueowl"]}
<p><strong>Why Blue Owl was hit hardest.</strong> OTIC lends to software firms, the sector investors decided AI would hollow out. Lipschultz's answer in February: AI "can certainly hurt some of these software companies. But does it hurt so many of the right ones down to 30% of their value? It doesn't", and the loans are three years on average. By April the firm said it was "working down our exposure to software" [S554][S557].</p>
<p><strong>The three defences.</strong> First, the requests came from few people: "1% of investors representing the majority of tenders and approximately 90% of the investor base electing not to tender", a "headline-driven, not fundamental-driven redemption environment". Second, the advisers who sell the fund wanted the cap held: "they want the products to work as designed, 5% tenders per quarter, not more... so that shareholders benefit from the asset class, the illiquidity premium". Third, liquidity is ample: OCIC had $11.6bn of liquidity against a $958m tender, and repayments from borrowers covered gross redemptions three times over [S557][S560].</p>
<p><strong>What it cost.</strong> A $1.4bn loan sale, a $500m bond, a permanent halt at OBDC II, a class action, and a share price that fell 68% peak to trough. Q2 requests eased and the shares rose 10% on the day, which tells you what the market was watching [S516][S529][S514][S556][S533].</p>
{box("say","The line to use","&quot;Blue Owl paid exactly what its documents said it would, 5% a quarter, and its loans are performing. The problem was never the credit. It was that a product sold as semi-liquid turned out to be liquid at the manager's pace, and OTIC investors got 12 cents on the dollar of what they asked for, twice.&quot;")}

<h2>6. Case two: Partners Group</h2>
<p>Partners Group is a Swiss-listed manager with $186bn under management, based near Zug, and the pioneer of the evergreen model: its Global Value fund has run since 2007. Evergreens are about 30% of its assets, around $56bn, and unlike Blue Owl its evergreen problem is mainly private equity rather than credit [S540][S543].</p>
<table>
<tr><th style="width:22%">Date</th><th>What happened</th></tr>
<tr><td>4 Jun 2026</td><td>Q2 requests of 9.8% at Global Value trigger the 5% cap; the $15.8bn US fund sees about 6%. Layton: liquidity features "are designed to protect long-term investors". The firm says the trouble "started in private credit vehicles and has recently spilled over to private equity". Shares fall 18% in a day [S528][S546][S548].</td></tr>
<tr><td>25 Jun 2026</td><td>Chairman Steffen Meister: "We clearly don't see the need to change our strategy", but the firm "might keep them slightly smaller in size going forward". No plan to freeze any fund. Insiders buy over CHF 60m of shares [S550].</td></tr>
<tr><td>16 Jul 2026</td><td>H1 client withdrawals of $3.8bn, 79% from three mature evergreen strategies; redemptions expected "for several quarters" [S549].</td></tr>
<tr><td>1 Sep 2026</td><td>H1 results: performance fees down 39%, profit down 13% to CHF 502m, a miss. Cagnati (risk and portfolio solutions) and Jenkner (president, formerly head of private credit) become co-CEOs on 1 January 2027; Layton moves to CIO. The release calls it "rotations" for "this next cycle"; Reuters and the FT tie it to the redemptions and a share price down about a third [S540][S541][S543][S616].</td></tr>
</table>
{box("unc","Be careful with the CEO story","The company's own release gives no reason for the change and frames it as a rotation, with Layton staying as CIO. The link to evergreen redemptions is the press's reading (Reuters, Bloomberg, FT), supported by the timing, the guidance cut and the share price. Say &quot;replaced its CEO as it works through evergreen redemptions&quot;, which is Reuters' wording, not &quot;fired over the gates&quot;.")}

<h2>7. Case three: Blackstone, and what it is actually launching</h2>
<p class="big">Blackstone is the largest player in the wealth channel with $324bn from individuals, up 16% in a year through the worst redemption cycle since 2022, and it has kept launching. What you read in September was not a first move into evergreens; it was the next step in a strategy that began with BREIT in 2017 and BCRED in 2021 [S582].</p>
<table>
<tr><th style="width:24%">Blackstone product</th><th>What it is</th><th style="width:28%">Why it matters now</th></tr>
<tr><td>BCRED (2021)</td><td>The largest private credit evergreen, NAV about $43bn. Q1 2026: 7.9% requests met in full with Blackstone's own money. Q2 and Q3: about 10% each, paid at 5%; queued investors got about 75% of their money within 90 days [S518][S585][S584].</td><td>Shows even the biggest balance sheet chose to hold the cap after one quarter of paying in full.</td></tr>
<tr><td>BMACX (May 2025)</td><td>An interval fund mixing corporate, asset-based, real-estate and liquid credit; $2,500 minimum; 0.75% fee plus 12.5% of income; still a 5% quarterly repurchase [S580].</td><td>The "multi-asset credit" evergreen widely mis-dated to 2026.</td></tr>
<tr><td>BXHF (spring 2026)</td><td>Its first hedge fund for individuals with $5m or more [S593].</td><td>Evergreens now stretch beyond credit and property.</td></tr>
<tr><td>WVB funds (22 Jul 2026)</td><td>Two interval funds built with Wellington and Vanguard: one blends public stocks and bonds with Blackstone privates, one holds only privates. Sold first through Merrill and Bank of America Private Bank, quarterly tenders, "no guarantee of repurchase" [S590].</td><td>Vanguard, the index-fund purist, now sells private markets to its clients. That is the landscape shift.</td></tr>
<tr><td>Institutional money in wealth funds (Aug 2026)</td><td>The FT reported pensions and endowments buying into Blackstone's and KKR's evergreens built for individuals, because their old drawdown funds have "struggled to exit investments and distribute proceeds" [S597][S599].</td><td>The wrapper built for retail is becoming the wrapper for everyone.</td></tr>
</table>
<p><strong>How this changes the landscape.</strong> Three ways. First, the evergreen is now the default wrapper for wealth, and increasingly for institutions, so a private bank's alternatives shelf will be mostly evergreens within a few years; J.P. Morgan's already has about 20% of its alternatives assets in them, four times five years ago [S613]. Second, the stress split the market: Blackstone and Oaktree paid above the cap, Goldman never hit it, and Blue Owl, Apollo, Ares and HPS held it for two or three quarters, so "which manager" now matters more than "which asset class" [S524][S532]. Third, the distribution channel is consolidating around the biggest gatekeepers: Merrill for WVB, UBS and the private banks for the rest, and the regulators are opening more doors, with LTAFs in ISAs from April and a US proposal to widen retail access sent to the White House on 1 September [S590][S608][S616].</p>
{box("opinion","A view you can defend","The 2026 cycle was not a private credit crisis. Defaults stayed low and the loans paid. It was a product-design crisis: a quarterly exit window was sold as liquidity to buyers who had never seen it bind. The winners are the managers with the balance sheet and reputation to hold the line (Blackstone) or never hit it (Goldman), and the gatekeepers who sized the products correctly for their clients. That is a private bank story, which is why it belongs in this interview.")}

<h2>8. Regulators, and where J.P. Morgan stands</h2>
<p><strong>Regulators say the same thing in different accents.</strong> The Bank of England's July Financial Stability Report: "redemption requests have been elevated in several retail funds, with some limiting redemptions, underlining both liquidity mismatch and valuation concerns", though the effect on UK stability is judged limited [S538]. The IMF sized the redeemable part of direct lending at about $300bn of $2tn and called systemic risk "contained" [S507]. The Financial Stability Board warned that redemption options "may heighten the procyclicality of private credit" [S508]. The ECB noted US funds have faced "sizeable redemption requests" and mismatches "could grow" as retail vehicles expand [S539].</p>
<p><strong>Jamie Dimon</strong> has been the loudest bank voice: the "cockroach" line in October, then in his April 2026 shareholder letter that losses in a downturn "will be higher than expected", that "credit standards have been modestly weakening pretty much across the board", and that the industry has "not had a credit recession in a long time and it seems that some people assume it will never happen". On the same day's call: "I don't think it's systemic" [S513][S569][S570]. The firm competes in the same market: a $50bn balance-sheet commitment to direct lending, announced February 2025 [S572].</p>
<p><strong>The Private Bank's position</strong> is the one to know for this interview. Its strategists wrote in March that elevated requests "appear to be driven more by sentiment than by fundamentals", that "gates and redemption queues are prudent tools", and that private credit should be about 15% of a client's private-markets allocation, roughly 1.5% to 4.5% of a portfolio; in April, that "gates are simply a feature of the vehicles' structure" and "manager selection matters more as dispersion rises" [S576][S577]. The bank runs an evergreen shelf across private equity, credit and real assets, has an 18-person structuring team, uses a pacing tool to model each client's liquidity, and its alternatives head said no one "has anchored more solutions than us this year... in the rise of evergreens" [S574]. Mary Erdoes at the 2025 Investor Day: "with these evergreen strategies, you see the green in the evergreen. That's really the retail side that's going to grow" [S575]. And on 15 September 2026 its asset manager launched two more, a private equity fund and a private credit fund, for European wealth clients [S579]. Michael Cembalest's warning sits alongside: retail fundraising has gone from $25bn to an annualised $175bn and the fund documents' "firewalls" will be stressed "if a sharp recession and liquidity crunch coincide" [S578].</p>
{box("term","What this means for the Advisor seat","Three jobs. Sizing: a semi-liquid fund can never be a client's emergency reserve, because in a squeeze a full exit takes five quarters or more. Selection: the same wrapper behaved very differently across managers in 2026, so due diligence on the manager's liquidity sources matters more than the headline yield. Explaining: when a client asks why they received 27 cents on the dollar, the advisor is the person in the room. The bank's own guidance is to keep taking the risk, but to &quot;ensure risk taken is intentional&quot; [S576].")}

<h2>9. The HireVue answer</h2>
<p>Built for the confirmed AWM prompt, "Describe what factors have influenced financial markets in recent months and how they might affect our clients", and it works unchanged for "tell us about something in the world that interests you". Target 105 to 115 seconds at a natural pace. The content section lands the technical vocabulary and the numbers inside the first fifteen seconds, then three distinct parts: the product, the events, the client.</p>
<div class="script">
<div class="seg"><div class="tm">0:00 to 0:15<br>content section</div><div class="tx">Thank you for taking the time to watch this. The theme I have followed most closely this year is the liquidity squeeze in <b>evergreen private credit funds</b>. I will cover what these <b>semi-liquid vehicles</b> promise, why <b>Blue Owl, Blackstone and Partners Group</b> have all capped redemptions at <b>5% a quarter</b>, and what that means for a private bank client.</div></div>
<div class="seg"><div class="tm">0:15 to 0:35<br>the product</div><div class="tx">First, the product. A fund like Blue Owl's Credit Income Corp holds <b>five-to-seven-year senior secured loans</b> to private companies, strikes a <b>net asset value monthly</b>, takes new money monthly, and offers to buy back <b>at most 5% of its shares a quarter</b>. That 5% is a ceiling at the board's discretion. Investors read it as a promise.</div></div>
<div class="seg"><div class="tm">0:35 to 1:05<br>the events</div><div class="tx">Second, what happened. After the <b>First Brands and Tricolor</b> collapses last autumn, then the <b>AI sell-off in software</b>, a fifth of all direct loans, wealthy investors asked for their money back at once. Blue Owl's flagship had first-quarter requests for <b>22%</b> of its shares, its software fund <b>41%</b>. Both paid 5%, so investors got about a quarter of what they asked for, twice. <b>Blackstone's BCRED</b> has been over its cap three quarters running. <b>Partners Group</b> gated its flagship in June and replaced its chief executive this month.</div></div>
<div class="seg"><div class="tm">1:05 to 1:40<br>the client</div><div class="tx">Third, why it matters for your clients. The loans are performing; Blue Owl's <b>non-accruals are 0.2%</b>. The problem is trust: a product sold as semi-liquid turned out to be liquid at the manager's pace. J.P. Morgan's Private Bank has about <b>a fifth of its alternatives in evergreens</b>, four times five years ago. So the advisor's job becomes <b>sizing and liquidity budgeting</b>: emergency cash never sits behind a 5% gate, and the manager matters more than the yield, because the same wrapper behaved very differently at Goldman and Blue Owl.</div></div>
<div class="seg"><div class="tm">1:40 to 1:50<br>close</div><div class="tx">That is why the Advisor seat interests me: it is where product knowledge becomes the conversation the client needs.</div></div>
</div>
<p class="small">About 315 spoken words. At a rehearsed 160 words a minute that is 1:58; at a slower 150 it is 2:05, so time yourself and, if you run long, drop the Blackstone sentence first (saves 8 seconds). If you have ten seconds spare, add after the Partners Group line: "The FT counted over $20bn of requests in the first quarter, with only about half paid", or "with its shares down about a third" after "this month".</p>
<p><strong>Screen notes</strong> (two or three words a line, taped under the webcam):</p>
<div class="notes">thank you
evergreen / semi-liquid / 5% quarter
Blue Owl, Blackstone, Partners Group
--
5-7yr senior secured / NAV monthly
ceiling not promise
--
First Brands, Tricolor / AI software 1/5
22% and 41% / paid 5% / quarter back
BCRED 3 quarters / PG gate, CEO
--
non-accruals 0.2% / trust
JPM fifth in evergreens, 4x
sizing, liquidity budget / manager > yield
--
product knowledge to conversation</div>
<table>
<tr><th style="width:34%">If they could ask a follow-up</th><th>Your answer</th></tr>
<tr><td>Is this a crisis?</td><td>No. Defaults are low and the loans pay. It is a product-design problem: a quarterly window was sold as liquidity. The IMF and the Bank of England both say the systemic effect is limited [S507][S538].</td></tr>
<tr><td>So should clients avoid these funds?</td><td>No. The bank's own guidance is to keep private credit at around 15% of a private-markets allocation, senior and diversified, and to treat gates as a feature. The change is in sizing and manager choice, not in the asset class [S576][S577].</td></tr>
<tr><td>Why did Goldman not gate?</td><td>Requests were 3.2%, under the cap. Its fund is smaller and less exposed to software. The point is that the wrapper is the same and the outcome was not, so the manager is the decision [S532].</td></tr>
<tr><td>What does Dimon think?</td><td>"When you see one cockroach, there are probably more"; losses in a downturn will be higher than expected; but "I don't think it's systemic". And the firm is lending $50bn of its own into the same market [S513][S569][S570][S572].</td></tr>
</table>
{box("dont","Do not say","&quot;Investors aren't getting their money back.&quot; They are, at 5% a quarter, pro rata, and Blackstone paid in full in Q1. Say &quot;they got about a quarter of what they asked for&quot;. Do not say Blackstone &quot;launched its first evergreen funds&quot; in September; BREIT is from 2017 and BCRED from 2021, and the 2026 news is the Vanguard tie-up and institutions buying in. Do not say Partners Group &quot;fired&quot; Layton; he becomes CIO and the company calls it a rotation. Do not say &quot;investors can only redeem 5% of their money&quot;; the cap is 5% of the fund, shared pro rata, which is why individuals got 12 to 27 cents on the dollar.")}
{box("say","The thirty-second version, if the question is narrower","&quot;The factor I would flag is liquidity in private markets. Evergreen private credit funds offer to buy back 5% of shares a quarter; this year Blue Owl saw requests for 22% and 41% at its two wealth funds, Blackstone's BCRED has been over its cap three quarters running, and Partners Group replaced its CEO. For our clients the loans are mostly fine, the lesson is about sizing: nothing a client may need in the next two years belongs behind a quarterly gate, and the manager matters more than the yield.&quot;")}

<h2>10. Reading list, FT first</h2>
<p>The FT is closed to the tools used to build this brief, so these headlines are recorded from the FT's own posts and from secondary coverage and marked accordingly. Search each headline on ft.com with your university access; all are from the last twelve months.</p>
<table>
<tr><th style="width:15%">Date</th><th style="width:16%">Outlet</th><th>Headline</th><th style="width:16%">Status</th></tr>
<tr><td>16 Nov 2025</td><td>FT</td><td>Blue Owl's OBDC II merger implies a ~20% haircut for retail investors (reported via InvestmentNews)</td><td>PAYWALLED-NOT-READ [S514]</td></tr>
<tr><td>18 Feb 2026</td><td>FT</td><td>Blue Owl permanently halts redemptions at fund aimed at retail investors</td><td>PAYWALLED-NOT-READ [S620]</td></tr>
<tr><td>~2 Apr 2026</td><td>FT</td><td>Blue Owl struck by $5.4bn of redemption requests</td><td>PAYWALLED-NOT-READ [S523]</td></tr>
<tr><td>~9 Apr 2026</td><td>FT</td><td>Private credit funds face massive redemption wave as wealthy investors head for exits ($20.8bn in Q1)</td><td>PAYWALLED-NOT-READ [S525][S524]</td></tr>
<tr><td>Jun 2026</td><td>FT</td><td>Partners Group set to cap withdrawals at US private equity fund</td><td>PAYWALLED-NOT-READ [S546]</td></tr>
<tr><td>6 Jul 2026</td><td>FT</td><td>Big investors commit billions to private credit despite turmoil</td><td>PAYWALLED-NOT-READ [S535]</td></tr>
<tr><td>~26 Aug 2026</td><td>FT (Heal, Livsey)</td><td>Institutional investors back Blackstone and KKR funds for wealthy individuals</td><td>PAYWALLED-NOT-READ [S597][S599]</td></tr>
<tr><td>~2 Sep 2026</td><td>FT (Heal, Ruehl)</td><td>Partners Group replaces chief as fund redemptions weigh on shares</td><td>PAYWALLED-NOT-READ [S616]</td></tr>
<tr><td>14 Mar 2026</td><td>Fortune</td><td>The $265 billion private credit meltdown</td><td>READ [S519]</td></tr>
<tr><td>2 Apr and 2 Jul 2026</td><td>Semafor (Liz Hoffman)</td><td>Blue Owl credit funds face heavy redemption requests; Blue Owl hit by billions in redemptions, again</td><td>READ [S521][S533]</td></tr>
<tr><td>16 Mar 2026</td><td>BIS Quarterly Review</td><td>Private credit's software lending meets AI disruption (the best short explanation of the AI angle)</td><td>READ [S515]</td></tr>
<tr><td>12 Mar and 16 Apr 2026</td><td>J.P. Morgan Private Bank</td><td>Private credit under the microscope; Private credit still earns its place in portfolios</td><td>READ [S576][S577]</td></tr>
<tr><td>2 Jul and 3 Sep 2026</td><td>SEC filings</td><td>OCIC Q2 shareholder update; BCRED Q3 tender letter (primary sources for every number above)</td><td>READ [S560][S584]</td></tr>
</table>

<h2>11. Sources</h2>
<p class="small">Status: READ means the page was fetched and read in full; Snippet only means only the search excerpt was available; PAYWALLED-NOT-READ means the headline and date are recorded from a public mirror. Confidence reflects how directly the source supports the figures cited.</p>
{{SOURCE_TABLE}}
"""
# source table
used=sorted(set(re.findall(r"\[(S\d+)\]",body)),key=lambda s:int(s[1:]))
missing=[u for u in used if u not in S]
if missing: print("WARNING missing source",missing)
rows="".join(f"<tr><td>{k}</td><td>{S[k][0]}</td><td>{S[k][1]}</td><td>{S[k][2]}</td><td><a href='{S[k][4]}'>{S[k][3]}</a></td><td>{S[k][4]}</td><td>{S[k][5]}</td></tr>" for k in used)
table=f"<table class='src'><tr><th>ID</th><th>Outlet</th><th>Title</th><th>Date</th><th>URL</th><th>Status</th><th>Conf.</th></tr>{rows}</table>"
body=body.replace("{SOURCE_TABLE}",table)
svgs=[]
def keep(m): svgs.append(m.group(0)); return f"@@SVG{len(svgs)-1}@@"
body=re.sub(r"<svg.*?</svg>", keep, body, flags=re.S)
body=re.sub(r"\[(S\d+)\]", lambda m:f'<span class="s">[{m.group(1)}]</span>', body)
body=re.sub(r"@@SVG(\d+)@@", lambda m: svgs[int(m.group(1))], body)
open("evergreen.html","w").write(f"<!doctype html><html><head><meta charset='utf-8'><title>Evergreen Private Credit Funds and the 2026 Redemption Squeeze</title><style>{css}</style></head><body>{body}</body></html>")
print("ok", len(used), "sources")
