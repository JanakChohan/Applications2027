import diagrams as dg, diagrams2 as d2, charts as ch, figs_def2 as f2
from svg import fig
def strip(f): return f.split('<div class="cap">')[0].replace('<div class="fig">','')
n=[0]
def F(svg,cap):
    n[0]+=1; return f'<div class="fig">{svg}<div class="cap"><b>Figure {n[0]}.</b> {cap}</div></div>'
css=open("pack_style.css").read()+"""
body{font-size:10.6pt} h2{margin-top:16pt} .big{font-size:12.5pt;line-height:1.5;color:#0b2545}
.mech{border:1px solid #d6dbe3;border-left:5px solid #b08d57;border-radius:4pt;padding:8pt 11pt;margin:8pt 0;break-inside:avoid}
.mech .h{font-weight:700;color:#0b2545;font-size:11.5pt;margin-bottom:3pt}
.mech .num{display:inline-block;background:#0b2545;color:#e9dcc3;font-weight:700;padding:1pt 6pt;border-radius:3pt;margin-right:5pt}
.say{background:#eaf5ef;border-left:4px solid #2e7d5b;padding:5pt 9pt;margin-top:5pt;font-size:9.8pt}
.say b{color:#2e7d5b;font-size:8.4pt;letter-spacing:.6px;text-transform:uppercase}
"""
figs={
 "money": F(d2.money_flow(),"Where the money comes from and where it goes, 2025. Three businesses, two kinds of revenue, one balance sheet."),
 "layers": F(d2.operating_layers(),"The firm as layers: customers and capital, the front line, the centre."),
 "legs": F(strip(dg.pb_revenue()),"The four legs of a private-bank relationship. Fees on investments, spread on deposits and loans, planning and trust fees."),
 "works": F(f2.why_works(),"The arithmetic behind 'be the primary bank': each added leg raises assets, revenue and retention, in the firm's own disclosed numbers."),
 "one": F(ch.one_firm(),"The network around the Private Bank. Every arrow runs both ways and nobody counts the referral credit."),
 "team": F(strip(dg.team_model()),"One client, five seats, one owner. The Advisor is the single point of accountability."),
 "teamvs": F(d2.team_vs_alternative(),"The firm owns the client (J.P. Morgan) against the adviser owns the client (the grid model at many rivals)."),
 "fly": F(strip(dg.flywheel()),"Mary Erdoes' four ingredients drawn as the loop they are. The Advisor sits in 2 and 3 and is measured on 4."),
 "why": F(d2.why_firm_one_page(),"Six mechanisms, each with a number. None can be said of a rival in the same words."),
}
body=f"""
<div class="cover" style="height:250mm">
<div class="band"><div class="kicker">The short version</div>
<h1>How J.P. Morgan's Private Bank Works, and Why It Stands Out</h1>
<div class="sub">The business model, the mechanisms that make it different, and the values stripped to what they mean in practice. Ten pages, no weeds. Built for one purpose: so you can say, in your own words and with a number, what this firm does better than everyone else, and what it does not.</div></div>
<div class="meta"><p><strong>Prepared:</strong> 15 September 2026, for the 2027 Global Private Bank Advisor Summer Internship, London (closes 1 November 2026).</p>
<p><strong>Where the numbers come from:</strong> JPMorgan Chase's 2025 Form 10-K, Mary Erdoes' 2021 to 2025 shareholder letters, the 2022 to 2025 Investor Days, and the Euromoney 2026 interviews. The full source table is Part 15 of the complete pack.</p>
<p><strong>How to read:</strong> Sections 1 and 2 explain the machine. Section 3 is what to say. Section 4 is what the values mean once the marketing is removed. Section 5 is the honest edge, including where the firm does not lead.</p></div></div>

<h2>1. The business model in one page</h2>
<p class="big">JPMorgan Chase is three businesses sharing one balance sheet and one client base. Chase banks 94 million American consumers and small businesses. The Commercial &amp; Investment Bank advises, lends to, trades for and moves money for 80,000 companies and institutions. Asset &amp; Wealth Management manages money and advises the wealthy. In 2025 that produced $185.6bn of revenue and $57.0bn of profit, about half from interest spread and half from fees and trading.</p>
<p>The Private Bank is the wealth half of Asset &amp; Wealth Management: $12.4bn of revenue in 2025 at a 37% pretax margin, about 4,100 advisors, roughly $3tn of client assets. It is small inside the firm (7% of revenue) and unusually profitable (AWM earns a 40% return on equity, the highest in the firm) because it earns fees rather than putting large amounts of capital at risk.</p>
{figs["money"]}
<p>What the diagram tells you: the firm is a machine for turning customer relationships into two kinds of revenue, and the profit goes three ways. About $46bn went back to shareholders in 2025. A large sum was retained as capital, which is what "fortress balance sheet" means. And the rest was reinvested in people and technology: 500 more branches planned, advisors up from 2,500 to 4,101 in five years, about $20bn a year on technology. The Private Bank sits on the reinvestment side of that line.</p>
{figs["layers"]}

<h2>2. How the Private Bank makes money, and what it is really selling</h2>
<p class="big">A private bank client pays in four ways: a percentage fee on invested assets, the spread the bank earns on their cash and loans, commissions and placement fees on alternatives, and fees for trusts and planning. The whole model is built around one idea: a family that uses all four is worth far more and is far harder to lose than a family that uses one.</p>
{figs["legs"]}
<p>The firm discloses the arithmetic. When a US Private Bank client also actively banks with the firm, assets and revenue are on average 65% higher. Only 2% of clients are credit-only. More than 95% of clients stay each year. Loans of $266bn produce charge-offs of one to four basis points a year because "we want two ways out", meaning every loan can be repaid from the collateral and from the client's cash flow. That is why the balance sheet is part of the product and not a side business.</p>
{figs["works"]}
<p>What the client is buying is not a portfolio. Portfolios are available everywhere. They are buying <strong>one accountable relationship that can do everything</strong>: invest £50m, lend £20m against it without selling, hold cash in five currencies, set up the trust that passes it on, and bring the investment bank to the table when their company is sold. The Advisor is that relationship. Everything else in the firm exists to make that person more capable.</p>
{figs["team"]}

<h2>3. What makes it different: six mechanisms, each with a number</h2>
<p class="big">Every private bank says "trusted relationships" and "long-term partnership". Those words are true here, but they are not what makes the firm different, because they are not what makes any firm different. What makes J.P. Morgan different is six pieces of machinery that most rivals do not have, and each one can be stated with a number.</p>

<div class="mech"><div class="h"><span class="num">1</span>The referral network, and the rule that makes it work</div>
<p>Founders whose companies the investment bank sells become Private Bank clients. Owners of the 60,000 companies the commercial bank lends to become clients. "There are 2,000 private banking clients that walk into those Chase branches every day." A workplace equity platform with 1.8 million employee shareholders is tomorrow's pipeline. Over 95% of AWM's top 50 clients use other parts of the firm. The rule that makes the network work, in Erdoes' words: "We do not have side accounting groups that think about where those revenues get counted for. We are trying to win for the client." Most banks have referral programmes that fail because divisions fight over credit. Dimon's own phrase for the whole firm is "its own strong neural network, powerful and healthy connections between our people".</p>
<div class="say"><b>Say this</b> "The investment bank that sells the founder's company is the bank that meets the founder first, and nobody counts who booked the revenue. That is why clients arrive here that other private banks have to cold-call."</div></div>

<div class="mech"><div class="h"><span class="num">2</span>The balance sheet</div>
<p>$266bn of Private Bank loans, described by the firm as "the largest lending business in the private banking space"; the number one lender on $3m+ mortgages in the US; financier of 10 of the last 15 major sports-team transactions; losses of one to four basis points a year. A Swiss partnership or an independent adviser cannot lend £20m against private company shares in three currencies. This is what turns a client with one leg into a client with four.</p>
<div class="say"><b>Say this</b> "Wealthy people borrow rather than sell. The firm can lend at a scale and in a range of currencies that boutiques cannot, and it does it with losses of a few basis points, which is why lending is how a client becomes primary."</div></div>

<div class="mech"><div class="h"><span class="num">3</span>The apprenticeship: seeded books, not bought ones</div>
<p>"This isn't the brokerage business model... We don't buy books of business. We seed books of business." Half of new advisors are grown internally; productivity doubles after a year; break-even by year three; home-grown 25-year-olds are now "just as productive as our 30- to 35-year-old mid-career hires". Advisors went from 2,500 in 2020 to 4,101 in 2025, an 11% a year build, which the firm says will "normalize later this decade". The internship is the top of that funnel.</p>
<div class="say"><b>Say this</b> "The firm has told shareholders that growing its own advisors is cheaper and more loyal than poaching them, and that the hiring surge peaks now. I am applying to be grown."</div></div>

<div class="mech"><div class="h"><span class="num">4</span>The uniform global model, run for the international bank from London</div>
<p>"We operate the only private bank in the industry with a uniform business model globally." The same five-seat team, the same platform and the same credit process in London, Dubai, Geneva and New York, which matters when a family lives in three of them. The international business is run from 60 Victoria Embankment; its CEO told Euromoney in 2026 that "the biggest opportunity to grow market share is very much within the European franchise"; the UK head has a reported mandate to double the business in five years.</p>
<div class="say"><b>Say this</b> "London is not a satellite. It runs the international bank, and Europe is the named share opportunity, which is why the 2027 class is being hired."</div></div>

<div class="mech"><div class="h"><span class="num">5</span>The fiduciary stance with an open shelf</div>
<p>"Our North Star has never changed: to be the best in the industry for our clients, not the biggest." "We do not believe that any fiduciary manager should dictate choice." The Private Bank runs 850+ external alternatives managers next to its own funds, places about $2bn a month into alternatives, and 83% of its ten-year active fund assets beat the peer median. Twenty-two consecutive years of positive client flows, $553bn in 2025 alone, are the market's verdict.</p>
<div class="say"><b>Say this</b> "Clients vote with their feet. $553bn of net new money in one year is the number I trust more than any award."</div></div>

<div class="mech"><div class="h"><span class="num">6</span>The economics that fund all of the above</div>
<p>AWM set four targets in 2020 (5% revenue growth, 25% margin, 25% return on equity, 4% flows) and has beaten all of them every year; in 2025 it delivered 12%, 36% and 40%. It refuses to raise them: "I don't want them to be constrained by raising higher targets." Investment spend in AWM reached a record $2.7bn in 2025. Barclays' private bank profit fell that year and Julius Baer's fell 25%. A 36% margin is what pays for hiring through a rate shock and a banking crisis.</p>
<div class="say"><b>Say this</b> "A business that beats its own targets every year and refuses to raise them is a business that spends on growth rather than on hitting a number. That is the culture I want to learn in."</div></div>
{figs["one"]}
{figs["why"]}

<h2>4. The values, stripped to what they mean in practice</h2>
<p class="big">The firm's published values (Heart, Courage, Curiosity, Excellence, Service) barely appear in what its leaders say. What they say, repeatedly, reduces to six operating ideas. Each has a plain meaning and a place where you can see it.</p>
<table>
<tr><th style="width:20%">The phrase</th><th style="width:40%">What it means, stripped down</th><th>Where you can see it</th></tr>
<tr><td><strong>"First-class business in a first-class way"</strong> (J.P. Morgan Jr., 1933)</td><td>Only take clients and business you would be happy to explain in public. Do it properly, not quickly.</td><td>Source-of-wealth checks that take weeks and are never skipped; the firm's public reckoning with the Epstein relationship it should have exited.</td></tr>
<tr><td><strong>Fortress balance sheet</strong> (Business Principle 5)</td><td>Hold more capital than required so you are the safe place in a crisis and can act when others cannot. "A bank can't be a fair weather friend."</td><td>Bear Stearns 2008, Washington Mutual 2008, First Republic 2023; 40,000 Private Bank accounts opened in the ten weeks after Silicon Valley Bank failed.</td></tr>
<tr><td><strong>Fiduciary "north star"</strong> (Erdoes)</td><td>The advice must be right for the client even when it earns the bank less, and the house is allowed to say no. "If a client says 'I don't like fixed income', that's not the right answer."</td><td>External managers on the shelf; suitability records for every recommendation; the Consumer Duty in the UK.</td></tr>
<tr><td><strong>"Banking is not a commodity"</strong> (the first lesson in advisor training)</td><td>A client pays for judgment, access and an accountable person, not for a product they could buy cheaper elsewhere.</td><td>The five-seat team; salary-plus-bonus pay rather than a commission grid.</td></tr>
<tr><td><strong>"Our client", not "my client"</strong></td><td>The firm owns the relationship; the banker is its steward; specialists share it without fighting over credit.</td><td>Retention above 95% when bankers leave; the no-side-accounting rule on referrals.</td></tr>
<tr><td><strong>Face facts; kill bureaucracy</strong> (Dimon)</td><td>Look at the numbers coldly, admit mistakes, decide in the room. "Bureaucracy, complacency, and arrogance will take down a company."</td><td>Fifty-page shareholder letters that list what could go wrong; a private bank expected to get a founder a term sheet in days.</td></tr>
</table>
<p><strong>So what does "long-term trust" mean here?</strong> Not a feeling. It means the bank will lend to you in 2009, keep your deposits safe in 2023, tell you no when you ask for 100% in one stock, and still be there when your children inherit. Trust is the accumulated record of the machine in Section 3 working in bad years. That is the sentence to use instead of "trusted relationships".</p>
{figs["teamvs"]}
{figs["fly"]}

<h2>5. The honest edge: better than everyone else at what, and not at what</h2>
<table>
<tr><th style="width:34%">J.P. Morgan is better than any rival at</th><th>Because</th></tr>
<tr><td>Turning corporate relationships into private clients</td><td>The number one investment bank by fees for 15+ years sits next to the number one private bank (Global Finance, seven years running), with no internal pricing between them. UBS has the private bank but a smaller investment bank; Goldman and Morgan Stanley have the investment bank but smaller private banks abroad.</td></tr>
<tr><td>Lending to wealthy families at scale</td><td>$266bn of loans, "the largest lending business in private banking", losses of one to four basis points. Boutiques and Swiss partnerships cannot match it.</td></tr>
<tr><td>Growing its own advisors</td><td>Disclosed economics no rival publishes: seeded books, break-even in year three, half of advisors home-grown, +64% advisors in five years while revenue per banker rose 15%.</td></tr>
<tr><td>Alternatives for private clients</td><td>Euromoney's world's best for alternatives in 2025 and 2026; over $200bn; $2bn a month; 850+ external managers.</td></tr>
<tr><td>Consistency</td><td>22 consecutive years of positive flows; targets beaten every year since 2020; a 36% margin while UK and Swiss rivals' profits fell.</td></tr>
</table>
<table>
<tr><th style="width:34%">J.P. Morgan is not the leader at</th><th>The fact</th></tr>
<tr><td>Size in wealth management</td><td>Morgan Stanley has $10tn of client assets and UBS $4.8tn in wealth alone; AWM has $7.1tn across asset and wealth management.</td></tr>
<tr><td>Scale in Europe</td><td>About $750bn of international client assets against UBS's $4.8tn; share "below 1%" in several markets. A runway, not a lead.</td></tr>
<tr><td>UK domestic banking</td><td>Coutts (now with Evelyn, £127bn), Barclays and HSBC own sterling current accounts and the "family bank" role.</td></tr>
<tr><td>Awards in every year</td><td>Goldman won Euromoney's global title in 2025 and DBS in 2026.</td></tr>
<tr><td>A clean conduct record</td><td>London Whale, FX, spoofing, recordkeeping, trade surveillance, Epstein. The firm discloses all of it, which is itself the point to make.</td></tr>
</table>
<div class="box say"><div class="t">The thirty-second version</div>"Two things about this bank I cannot get elsewhere. First, how clients arrive: the investment bank sells a founder's company, the founder becomes a Private Bank client, and nobody counts the credit, which is why 95% of its top clients use other parts of the firm. Second, how bankers are made: it seeds books rather than buying them, half its advisors are home-grown, and it has gone from 2,500 to 4,100 advisors in five years while naming Europe as where it wants share. I want to be trained in that model, in London, on the work with families rethinking where they live after the 2025 tax changes."</div>
<div class="box dont"><div class="t">Don't say</div>"Biggest and best", "global leader", "trusted relationships", "great culture". Every candidate will. Say the mechanism and the number instead, and say one thing the firm is not the best at. Erdoes' own line is "the best in the industry for our clients, not the biggest".</div>
<p class="small">All figures are as reported by JPMorgan Chase for fiscal 2025 unless stated; peer figures from their own 2025 results. Quotations: Erdoes' 2021 to 2025 letters and Investor Days 2022 to 2025; Dimon's 2025 letter and the April 2026 NBIM remarks; Adam Tejpaul, Euromoney, March 2026; J.P. Morgan Jr., 1933. Full sources: the complete pack, Part 15.</p>
"""
open("core_model.html","w").write(f"<!doctype html><html><head><meta charset='utf-8'><title>How the Private Bank Works and Why It Stands Out</title><style>{css}</style></head><body>{body}</body></html>")
print("ok")
