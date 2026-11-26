"""Build study-guide-risk-and-catalysts.pdf: a beginner's explainer of the CROX pitch, focused on risk and catalysts.
HTML is generated from data/derived/facts.json and printed to PDF with headless Chromium (Playwright)."""
import json, os, subprocess, html
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); D = os.path.join(ROOT, "data", "derived")
F = json.load(open(os.path.join(D, "facts.json"))); RR = json.load(open(os.path.join(D, "rar_rows.json"))); ST = json.load(open(os.path.join(D, "study_stats.json")))
V = F["valuation"]; K = F["key"]; R = F["rar"]; B = F["scen"]["Base"]; SN = F["sens"]; Q = F["quarters"]; INS = F["insider"]
price = F["price"]; bear, base, bull, wtd = V["pt"]; rb, rba, rbu, rw = [v * 100 for v in V["ret"]]; e27 = V["eps27"][1]; exbb = e27 + SN["No buybacks at all in FY27 (cash retained)"][0]
tar = abs(SN["+1 pt US tariff rate on imports"][0]); fy = lambda y: F[f"fy{y}"]
CSS = """
@page { size: A4; margin: 17mm 16mm 18mm 16mm; }
* { box-sizing: border-box; }
html { font-family: 'Inter', 'Liberation Sans', Arial, sans-serif; font-size: 10.2pt; line-height: 1.5; color: #1f2328; }
body { margin: 0; }
h1 { font-size: 21pt; color: #1F3864; margin: 0 0 4pt; line-height: 1.2; letter-spacing: -0.2pt; }
h2 { font-size: 14pt; color: #1F3864; margin: 20pt 0 6pt; line-height: 1.25; break-after: avoid; }
h3 { font-size: 11.2pt; color: #1f2328; margin: 13pt 0 4pt; break-after: avoid; }
p { margin: 0 0 7pt; }
ul, ol { margin: 0 0 8pt; padding-left: 16pt; } li { margin-bottom: 3pt; }
.part { break-before: page; border-bottom: 2.5pt solid #2a78d6; padding-bottom: 6pt; margin-bottom: 10pt; }
.part .kicker { font-size: 9pt; font-weight: 700; color: #2a78d6; text-transform: uppercase; letter-spacing: 1pt; }
.lede { font-size: 11pt; color: #3c4043; margin-bottom: 10pt; }
.box { border-radius: 5pt; padding: 8pt 11pt 4pt; margin: 8pt 0 10pt; break-inside: avoid; }
.box .tag { font-size: 8pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8pt; margin-bottom: 3pt; display: block; }
.plain { background: #eef3fa; border-left: 3.5pt solid #2a78d6; } .plain .tag { color: #1c5aa6; }
.say { background: #fff8e6; border-left: 3.5pt solid #d97706; } .say .tag { color: #9a5200; } .say p { font-size: 10.4pt; }
.warn { background: #fdeeee; border-left: 3.5pt solid #c5362f; } .warn .tag { color: #a12a24; }
.key { background: #e8f6f3; border-left: 3.5pt solid #0e9f8e; } .key .tag { color: #0a6e63; }
table { width: 100%; border-collapse: collapse; margin: 6pt 0 11pt; font-size: 9.2pt; }
thead { display: table-header-group; } tr { break-inside: avoid; } table.keep { break-inside: avoid; }
h2.np { break-before: page; margin-top: 0; }
th { background: #1F3864; color: #fff; text-align: left; padding: 4.5pt 6pt; font-weight: 600; vertical-align: bottom; }
td { padding: 4.5pt 6pt; border-bottom: 0.6pt solid #dfe3e8; vertical-align: top; }
tr:nth-child(even) td { background: #f7f9fc; }
td.n, th.n { text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums; }
td b { color: #1F3864; }
figure { margin: 8pt 0 10pt; break-inside: avoid; text-align: center; } figure img { max-width: 100%; }
.cover { height: 250mm; display: flex; flex-direction: column; justify-content: center; }
.cover .eyebrow { font-size: 10pt; font-weight: 700; color: #2a78d6; text-transform: uppercase; letter-spacing: 1.5pt; margin-bottom: 10pt; }
.cover h1 { font-size: 34pt; letter-spacing: -0.6pt; margin-bottom: 10pt; }
.cover .sub { font-size: 14pt; color: #3c4043; margin-bottom: 26pt; max-width: 150mm; }
.cover .meta { font-size: 9.5pt; color: #5f6368; border-top: 0.8pt solid #c7c9cc; padding-top: 9pt; max-width: 150mm; }
.toc { margin-top: 22pt; font-size: 10.5pt; } .toc div { display: flex; gap: 10pt; padding: 3.5pt 0; border-bottom: 0.5pt dotted #c7c9cc; max-width: 150mm; } .toc b { color: #1F3864; min-width: 52pt; }
.card { border: 0.8pt solid #cfd6e0; border-radius: 6pt; padding: 8pt 11pt 3pt; margin: 8pt 0; break-inside: avoid; }
.card.keycard { border: 1.4pt solid #2a78d6; }
.card h3 { margin-top: 0; color: #1F3864; } .card .when { font-size: 8.5pt; font-weight: 700; color: #2a78d6; text-transform: uppercase; letter-spacing: 0.7pt; }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 0 14pt; }
.chip { display: inline-block; background: #1F3864; color: #fff; border-radius: 10pt; padding: 0 6pt; font-size: 8.5pt; font-weight: 600; }
.small { font-size: 8.6pt; color: #5f6368; }
.qa h3 { color: #1F3864; margin-bottom: 2pt; } .qa p { margin-bottom: 9pt; }
.steps { counter-reset: s; list-style: none; padding-left: 0; } .steps li { counter-increment: s; position: relative; padding-left: 24pt; margin-bottom: 6pt; }
.steps li::before { content: counter(s); position: absolute; left: 0; top: 0.5pt; width: 16pt; height: 16pt; border-radius: 50%; background: #2a78d6; color: #fff; font-size: 8.5pt; font-weight: 700; text-align: center; line-height: 16pt; }
"""
def box(kind, tag, body): return f'<div class="box {kind}"><span class="tag">{tag}</span>{body}</div>'
def fig(name, w="100%"): return f'<figure><img src="charts/{name}" style="width:{w}"></figure>'
def table(head, rows, num_cols=(), widths=None, keep=True):
    h = "".join(f'<th class="{"n" if i in num_cols else ""}">{c}</th>' for i, c in enumerate(head))
    b = "".join("<tr>" + "".join(f'<td class="{"n" if i in num_cols else ""}">{c}</td>' for i, c in enumerate(r)) + "</tr>" for r in rows)
    cg = ("<colgroup>" + "".join(f'<col style="width:{w}%">' for w in widths) + "</colgroup>") if widths else ""
    return f'<table class="{"keep" if keep else ""}">{cg}<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'
P = []; add = P.append
# ================================= COVER =================================
add(f"""<div class="cover"><div class="eyebrow">Stock pitch study guide</div><h1>Crocs (CROX):<br>the risks and the catalysts</h1>
<div class="sub">Everything you need to understand, explained from zero, so you can stand up and talk about it without notes.</div>
<div class="meta">All numbers are as of the market close on 25 November 2026 (share price ${price:.2f}). Company figures come from Crocs' own filings. Price targets, probabilities and risk scores are estimates from the pitch model and are labelled as such.</div>
<div class="toc"><div><b>Start here</b><span>How to use this guide</span></div><div><b>Part 1</b><span>The background: what Crocs is and why the pitch says buy</span></div><div><b>Part 2</b><span>Risk: what could go wrong, how bad, how likely, and what we would do</span></div>
<div><b>Part 3</b><span>Catalysts: the dates that could move the stock, and what we need to see</span></div><div><b>Part 4</b><span>Speaking: scripts, likely questions, numbers to memorise, mistakes to avoid</span></div></div></div>""")
# ================================= START HERE =================================
add(f"""<div class="part"><div class="kicker">Start here</div><h1>How to use this guide</h1></div>
<p class="lede">Your part of the pitch is risk and catalysts. That is the part where the audience decides whether the team has really thought about the stock, so it is worth knowing properly.</p>
<p>By the end you should be able to answer four questions out loud, in plain words:</p>
<ol><li><b>What could go wrong with Crocs?</b> (the risks)</li><li><b>How bad could it get, in numbers?</b> (the stress test)</li><li><b>What upcoming dates could move the share price?</b> (the catalysts)</li><li><b>What would make us change our mind?</b> (the kill criteria)</li></ol>
<h3>How the guide is laid out</h3>
<p>Read Part 1 first even though it is not your section. You cannot explain the risks to a business you cannot describe. Parts 2 and 3 are your material. Part 4 turns it into things you can say.</p>
<p>You will see four kinds of box:</p>
{box("plain", "In plain English", "<p>A jargon-free version of the idea you just read.</p>")}
{box("say", "Say it like this", "<p>Wording you could use out loud. Change it until it sounds like you.</p>")}
{box("key", "Number to remember", "<p>A figure worth having in your head.</p>")}
{box("warn", "Watch out", "<p>A place where people commonly get caught out in questions.</p>")}
<h3>Two things to know before you start</h3>
<p><b>Facts and estimates are different, and you should say which is which.</b> Sales, profits, share counts and insider trades come from Crocs' official filings: those are facts. The price targets, the probabilities and the 1-to-5 risk scores are estimates from the model built for this pitch. They are reasoned, but they are opinions. When you present one, say "our estimate". If your group thinks a score or a probability should be different, change it. The method is what you are being assessed on, not the exact number.</p>
<p><b>Use this to understand, then write your own version.</b> The scripts show the logic and the order. Your own words will be more convincing than memorised ones, and they are what you will fall back on when someone asks a question.</p>""")
# ================================= PART 1 =================================
add(f"""<div class="part"><div class="kicker">Part 1</div><h1>The background: what Crocs is and why the pitch says buy</h1></div>
<h2>1.1 What the company does</h2>
<p>Crocs makes the foam clog with holes in it. The shoe is moulded in one piece, which makes it cheap to produce. Crocs does not own factories: other companies make the shoes, mostly in Vietnam and China. Crocs designs them, markets them and sells them.</p>
<ul><li><b>Size.</b> About ${fy(2025)['revenue']/1000:.1f} billion of sales in 2025, from roughly 129 million pairs of Crocs at an average price of about $25 a pair.</li>
<li><b>Two brands.</b> The <b>Crocs brand</b> is 82% of sales and almost all of the profit. <b>HEYDUDE</b>, a slip-on loafer brand bought in 2022 for $2.5 billion, is the other 18%.</li>
<li><b>Two regions.</b> For the Crocs brand, about half of sales are in North America and half in the rest of the world ("international"). International has grown from 33% of the brand in 2021 to {F['intl_share_ttm']:.0f}% now.</li>
<li><b>Two ways of selling.</b> About half through its own stores and websites, and half to other retailers.</li></ul>
{fig("01_revenue_mix.png", "86%")}
{box("plain", "In plain English", "<p>Look at the chart. The blue block (North America) has stopped growing. The green block (international) keeps getting bigger. The orange block (HEYDUDE) got smaller. Keep that picture in mind: nearly every risk and catalyst in your section is about one of those three blocks.</p>")}
<h2>1.2 Why the pitch says "buy"</h2>
<p>The argument has three steps.</p>
<ol class="steps"><li><b>Crocs produces a lot of spare cash.</b> After paying all its bills it had ${F['ttm_fcf']:,.0f} million left over in the last twelve months. This is called free cash flow.</li>
<li><b>It uses that cash to buy back its own shares.</b> It has been removing about 10% of its shares every year. Fewer shares means each remaining share owns a bigger slice of the company.</li>
<li><b>So profit per share grows fast even though sales grow slowly.</b> The pitch expects sales to grow about 4% a year but profit per share to grow about 15% a year.</li></ol>
{box("plain", "In plain English: buybacks", "<p>Imagine a pizza cut into ten slices and you own one. If the pizzeria buys back and throws away one slice, there are nine left. Your one slice is now one-ninth of the pizza instead of one-tenth. The pizza did not get bigger, but your share of it did. Crocs does this with its own shares every year.</p>")}
<p>Yet the stock is cheap. Investors pay about 10 times one year of Crocs' profit for a share. The average large US company costs about 18 times. The pitch's base case is that the shares are worth about <b>${base:,.0f}</b> by December 2027, against <b>${price:.0f}</b> today.</p>
<h2>1.3 So why is it cheap? That is your section</h2>
<p>The stock is cheap because investors are afraid of something specific: that the clog is a fashion fad, and that the fad is ending. Crocs has been through this once already. Between 2007 and 2009 its sales fell by about a quarter.</p>
{box("key", "The bridge into your section", f"<p>The rest of the team explains why Crocs is worth more than ${price:.0f}. Your job is to explain <b>why the market disagrees</b> (the risks), <b>how wrong we could be</b> (the downside), and <b>when we will find out who is right</b> (the catalysts).</p>")}
<h2>1.4 The words you need</h2>
{table(["Term", "What it means", "Crocs example"], [
 ["Revenue (sales)", "Money coming in from customers.", f"${fy(2025)['revenue']/1000:.2f}bn in 2025"],
 ["Margin", "The share of each dollar of sales kept as profit. <i>Gross</i> margin is after the cost of the product. <i>Operating</i> margin is after all running costs.", "Gross about 58%, operating about 22%"],
 ["Basis point (bps)", "One hundredth of a percent. 100 bps = 1 percentage point.", "\"Margin fell 340 bps\" means it fell 3.4 points"],
 ["EPS", "Earnings per share: total profit divided by the number of shares. The number the stock market watches most.", "About $14.55 expected for 2026"],
 ["P/E multiple", "Share price divided by EPS. How many years of profit you pay for one share. Lower means cheaper.", f"${price:.0f} / $16 = about 10 times"],
 ["Free cash flow", "Cash left after running the business and investing in it.", f"${F['ttm_fcf']:,.0f}m in the last 12 months"],
 ["Buyback", "The company buying its own shares and cancelling them.", "About 10% of shares a year"],
 ["Guidance", "The company's own forecast, given with each set of results.", "2026 EPS of $14.45 to $14.65"],
 ["Consensus", "The average forecast of the professional analysts who follow the stock.", "2027 EPS of $16.01"],
 ["DTC and wholesale", "DTC (direct to consumer) is Crocs' own stores and websites. Wholesale is selling to other retailers.", "52% DTC, 48% wholesale"],
 ["Tariff", "A tax on imported goods. Crocs pays it on shoes brought into the US.", "Currently 10% to 12.5%"],
 ["Bear, base, bull case", "Three versions of the future: bad, expected, good. Each gets a share price and a probability.", f"${bear:,.0f} / ${base:,.0f} / ${bull:,.0f}"],
 ["Catalyst", "A specific upcoming event that could make the share price move.", "Results in February 2027"]], widths=[19, 52, 29], keep=False)}""")
# ================================= PART 2 RISK =================================
rows_scores = {"Crocs NA - clogs, wholesale": ("North America clogs sold to retailers", "Already falling. Retailers decide what goes on the shelf and cut quickly."),
    "Crocs NA - clogs, DTC": ("North America clogs sold in Crocs' own stores and sites", "The same product, but Crocs controls the shelf, so it falls more slowly."),
    "Crocs NA - sandals": ("North America sandals", "A different product, still growing at double-digit rates."),
    "Crocs NA - Jibbitz & other": ("North America charms and other", "Charms only sell if clogs sell."),
    "Crocs Intl - China": ("China", "The fastest-growing market (+30% in 2025), which usually means the most fashion-driven."),
    "Crocs Intl ex-China - clogs": ("International clogs outside China", "Still new in many countries, so less worn out."),
    "Crocs Intl ex-China - sandals, Jibbitz, other": ("International sandals, charms, other", "New products in new markets."),
    "HEYDUDE - wholesale": ("HEYDUDE sold to retailers", "Already fell 41% in two years and is fragile."),
    "HEYDUDE - DTC": ("HEYDUDE sold direct", "More stable than wholesale.")}
score_rows = [[rows_scores[r["line"]][0], f"${r['ttm_revenue_usd_m']:,.0f}m", str(r["score"]), f"{r['haircut_pct']:.0f}%", f"${r['revenue_at_risk_usd_m']:,.0f}m", rows_scores[r["line"]][1]] for r in RR]
score_rows.append(["<b>Whole company</b>", f"<b>${R['at_risk']/R['at_risk_pct']:,.0f}m</b>", "", "", f"<b>${R['at_risk']:,.0f}m</b>", f"<b>= {R['at_risk_pct']*100:.1f}% of all sales</b>"])
add(f"""<div class="part"><div class="kicker">Part 2</div><h1>Risk: what could go wrong, how bad, how likely, and what we would do</h1></div>
<h2>2.1 What a good risk section does</h2>
<p>A weak risk section is a list of ten things that could go wrong. A strong one picks the few that matter and answers five questions about each.</p>
{table(["Question", "What the audience is really asking"], [["1. What is the risk?", "Can you explain it simply?"], ["2. How bad could it be?", "Have you put a number on it?"], ["3. How likely is it?", "Do you have a view, and is it honest?"], ["4. What does the other side say?", "Have you listened to people who disagree?"], ["5. How would you know, and what would you do?", "Do you have a plan, or just hope?"]])}
<p>The pitch has <b>three main risks</b>, ranked by how much damage they could do. Learn them in this order.</p>
{table(["Rank", "Risk", "One-line version"], [["1", "<b>The fad risk</b>", "People stop wanting clogs, starting in North America."], ["2", "<b>Earnings quality</b>", "Profit per share is rising, but the underlying business is earning less than it did in 2023."], ["3", "<b>Insiders and management</b>", "The CEO has been selling shares, and senior managers keep changing."]])}

<h2>2.2 Risk 1: the fad risk</h2>
<p>This is the big one. It is the reason the stock is cheap.</p>
<h3>What the worry is</h3>
<p>Fashion moves in cycles. A product gets hot, everyone buys it, then it cools. If Crocs clogs are cooling, sales fall, and because clogs are 74% of the Crocs brand, there is not much else to fall back on.</p>
<h3>Why people believe it (the bear's evidence)</h3>
<ul><li><b>North America is shrinking.</b> Crocs brand sales there fell 6.8% in 2025. In 2026 they went -6.1%, +0.4%, -2.1% over the first three quarters.</li>
<li><b>Teenagers are losing interest.</b> In a well-known survey of US teens (Piper Sandler), Crocs was the 6th favourite shoe brand in 2023. In autumn 2026 it was 10th, with a 1% share. Birkenstock was 4th.</li>
<li><b>Copies are legal.</b> Crocs tried to stop lookalike clogs using trademark law and lost on appeal in January 2026. Anyone can sell a similar shoe.</li>
<li><b>It has happened before.</b> Crocs' sales fell 24% between 2007 and 2009. HEYDUDE's sales fell 25% between 2023 and 2025.</li></ul>
<h3>Why it might be wrong (the bull's evidence)</h3>
<ul><li><b>Part of the fall was Crocs' own choice.</b> From May 2025 it cut back on discounts to protect its prices. Fewer sales at full price can still mean more profit.</li>
<li><b>Crocs' own stores and websites in North America are still growing</b>: about +5% in the first half of 2026 and about +2% in the third quarter, once you adjust for an accounting change (explained in Part 3).</li>
<li><b>The rest of the world is growing fast.</b> International sales rose 11.8% in the latest quarter and are now more than half of the brand.</li>
<li><b>People are still buying more pairs.</b> Crocs sold 1.5% more pairs in 2025 than in 2024.</li></ul>
{fig("04_crocs_brand.png", "96%")}
{box("plain", "In plain English", "<p>Left chart: blue bars are North America, mostly below zero. Green bars are international, always above zero. Right chart: international's share of the brand keeps rising. The bear looks at the blue bars. The bull looks at the green ones. Both are looking at real data.</p>")}

<h2>2.3 Putting a number on it: \"revenue at risk\"</h2>
<p>Saying \"it might be a fad\" is not analysis. The pitch turns the worry into a number in four steps. This is the original piece of work in the pitch, so it is worth being able to explain.</p>
<ol class="steps"><li><b>Split the company's sales into nine buckets</b> by brand, region, product and how it is sold. The sales figures come from Crocs' reports.</li>
<li><b>Score each bucket from 1 to 5</b> for how exposed it is to clogs going out of fashion. 1 means safe, 5 means very exposed. These scores are judgement calls.</li>
<li><b>Turn each score into a sales fall over two years</b> if the fad ends: a score of 1 means 0%, 2 means 5%, 3 means 12%, 4 means 20%, 5 means 30%. The 30% is set close to what actually happened to Crocs in 2007-09 (-24%) and HEYDUDE in 2023-25 (-25%).</li>
<li><b>Multiply and add up.</b></li></ol>
{table(["Bucket", "Sales, last 12 months", "Score", "Fall if the fad ends", "Sales at risk", "Why that score"], score_rows, num_cols=(1, 2, 3, 4), widths=[24, 13, 7, 11, 11, 34])}
{box("plain", "Worked example", f"<p>Take the first row. North America clogs sold to retailers bring in ${RR[0]['ttm_revenue_usd_m']:,.0f} million a year. We scored it 5, which means a 30% fall. 30% of ${RR[0]['ttm_revenue_usd_m']:,.0f} million is ${RR[0]['revenue_at_risk_usd_m']:,.0f} million. Do that for all nine rows and add them up: ${R['at_risk']:,.0f} million, which is {R['at_risk_pct']*100:.1f}% of the company's sales.</p>")}
{box("key", "Number to remember", f"<p><b>About 16% of sales (${R['at_risk']:,.0f} million) is exposed if the clog trend reverses.</b> Most of it sits in North America clogs.</p>")}

<h2 class="np">2.4 The stress test: why a 16% fall in sales means a much bigger fall in profit</h2>
<p>This is the step people find surprising, and you will probably be asked about it.</p>
<p>Some costs shrink when you sell fewer shoes: you make fewer shoes and ship fewer boxes. Other costs do not shrink: store rents, head-office salaries, computer systems. Those are called <b>fixed costs</b>. When sales fall, the fixed costs stay, so the profit takes most of the hit.</p>
{box("plain", "In plain English: a coffee shop", "<p>A coffee shop sells $1,000 of coffee a day. Beans, milk and cups cost $400. Rent and wages cost $400. Profit is $200. Now sales fall 20% to $800. Beans, milk and cups fall to $320. Rent and wages are still $400. Profit is now $80. Sales fell 20% but profit fell 60%.</p>")}
{fig("18_operating_leverage.png", "94%")}
<p>For Crocs, the pitch assumes about ${ST['fixed']:,.0f} million of costs are fixed. Running the 16% sales fall through:</p>
{table(["", "Today", "If the fad ends", "Change"], [["Sales", f"${ST['rev0']:,.0f}m", f"${ST['rev1']:,.0f}m", f"-{R['at_risk_pct']*100:.0f}%"], ["Operating profit", f"${ST['ebit0']:,.0f}m", f"${ST['ebit1']:,.0f}m", f"{(ST['ebit1']/ST['ebit0']-1)*100:.0f}%"],
   ["Profit per share (EPS)", f"${R['eps0']:.2f}", f"${R['eps1']:.2f}", f"{(R['eps1']/R['eps0']-1)*100:.0f}%"], ["What the share might be worth", f"${price:.0f} (today's price)", f"about ${R['val']:.0f}", f"{R['val_vs_px']*100:.0f}%"]], num_cols=(1, 2, 3))}
<p>The last line needs one more idea. When a company is in trouble, investors also pay a lower multiple of its profit. In past bad periods Crocs traded at about 7 times profit. ${R['eps1']:.2f} of profit per share times 7 is about <b>${R['val']:.0f}</b>.</p>
<h3>\"But you made the scores up\"</h3>
<p>Someone will say this. The answer is that we tested it. If every score is moved down a notch, profit per share falls to ${R['minus1_eps']:.2f} instead of ${R['eps1']:.2f}. If every score is moved up a notch, it falls to ${R['plus1_eps']:.2f}. We also ran 20,000 random versions where each score could be wrong by one notch in either direction: nine times out of ten the answer landed between ${F['rar_mc']['eps_p5_p50_p95'][0]:.2f} and ${F['rar_mc']['eps_p5_p50_p95'][2]:.2f}.</p>
{box("say", "Say it like this", f"<p>\"The scores are our judgement, so we tested how much they matter. Even if every one of them is off by a notch, the conclusion is the same: a real fad unwind roughly halves profit per share. What matters is whether it happens, not how we scored it.\"</p>")}

<h2>2.5 How likely is it? Three scenarios</h2>
<p>The stress test is the worst case. A pitch also needs a view on how likely the bad outcome is. The model uses three scenarios.</p>
{fig("19_scenarios_simple.png", "84%")}
{table(["Scenario", "The story", "Chance (our estimate)", "Share price, Dec 2027", "vs today"], [
 ["Bear", "The fad partly unwinds. North America falls 8% a year for two years, international stops growing, HEYDUDE falls again.", "25%", f"${bear:,.0f}", f"{rb:+.0f}%"],
 ["Base", "Roughly what management has described: Crocs brand grows about 4%, HEYDUDE a little, margins flat.", "50%", f"${base:,.0f}", f"{rba:+.0f}%"],
 ["Bull", "North America grows again, international grows at low-teens rates, margins recover.", "25%", f"${bull:,.0f}", f"{rbu:+.0f}%"]], num_cols=(2, 3, 4))}
<h3>The weighted average</h3>
<p>Multiply each price by its chance and add up: (25% x ${bear:,.0f}) + (50% x ${base:,.0f}) + (25% x ${bull:,.0f}) = <b>${wtd:,.0f}</b>. That is {rw:+.0f}% above today's price. This is called the probability-weighted value, or expected value.</p>
{box("warn", "Watch out: two different \"bad\" numbers", f"<p><b>${bear:,.0f}</b> is the <b>bear case</b>: a partial unwind, given a 25% chance. <b>${R['val']:.0f}</b> is the <b>full stress test</b>: the complete fad unwind, the worst end of the bear case. Do not mix them up. If asked \"what is your downside?\", say ${bear:,.0f}. If asked \"what is the worst case?\", say about ${R['val']:.0f}.</p>")}
<h3>Being honest about the shape of the bet</h3>
<p>In the base case we make {rba:.0f}%. In the bear case we lose {abs(rb):.0f}%. The loss is bigger than the gain. So this is not a \"small downside, big upside\" stock. The bet works only because we think the bear case is the less likely outcome. The expected return falls to zero if the bear case has a {K['Break-even bear probability (EV = 0, base:bull kept 2:1)']*100:.0f}% chance instead of 25%.</p>
<h3>What is the market assuming?</h3>
<p>You can run the sum backwards. If our three prices are right, what chance of the bear case would make ${price:.0f} a fair price today? The answer is about <b>{K['Market-implied probability of the bear case (base:bull 2:1)']*100:.0f}%</b>. So the market is behaving as if the bad outcome is roughly a {K['Market-implied probability of the bear case (base:bull 2:1)']*100:.0f}% chance. We think it is 25%. That gap is why we think the fear is overdone, but only moderately. Eight months ago, when the shares were at $76, the gap was far larger.</p>
{box("say", "Say it like this", f"<p>\"The market is pricing in about a 40% chance that the clog trend unwinds. We think it is closer to one in four. That difference is our edge, and we want to be upfront that it is a modest edge, not a huge one.\"</p>")}""")
add(f"""<h2>2.6 Risk 2: earnings quality</h2>
<p>\"Earnings quality\" means: is the profit growth coming from a healthier business, or from something else?</p>
<h3>The issue</h3>
<p>Profit per share is going up. But the profit of the whole business has gone down.</p>
{table(["", "2023", "2026 (expected)", "Change"], [["Operating profit of the whole business", f"${fy(2023)['adj_op_income']:,.0f}m", f"${B['ebit']['FY2026E']:,.0f}m", f"{(B['ebit']['FY2026E']/fy(2023)['adj_op_income']-1)*100:.0f}%"],
   ["Number of shares", f"{fy(2023)['sh_diluted']:.1f}m", f"{B['sh_avg']['FY2026E']:.1f}m", f"{(B['sh_avg']['FY2026E']/fy(2023)['sh_diluted']-1)*100:.0f}%"], ["Profit per share (EPS)", f"${fy(2023)['adj_eps']:.2f}", f"${B['eps']['FY2026E']:.2f}", f"{(B['eps']['FY2026E']/fy(2023)['adj_eps']-1)*100:+.0f}%"]], num_cols=(1, 2, 3))}
{box("plain", "In plain English", "<p>Back to the pizza. The pizza has got a bit smaller since 2023. But so many slices have been removed that each remaining slice is bigger. That is fine as long as the pizza stops shrinking. If it keeps shrinking, removing slices cannot save you forever.</p>")}
<h3>Three more things under this heading</h3>
<ul><li><b>Margins were falling.</b> Operating margin was lower than a year earlier in three of the last four quarters ({F['opm_yoy_bps']['2025Q4']:+.0f}, {F['opm_yoy_bps']['2026Q1']:+.0f}, {F['opm_yoy_bps']['2026Q2']:+.0f} basis points), then higher in the latest one ({F['opm_yoy_bps']['2026Q3']:+.0f}).</li>
<li><b>\"Adjusted\" profit.</b> Crocs reports two versions of profit: the official accounting one, and an \"adjusted\" one that leaves out items it considers one-off. One adjustment is a lower tax rate (18% instead of 23%), which adds about ${F['ip_tax_eps_fy26e']:.2f} to profit per share, roughly 6%. That adjustment repeats every year.</li>
<li><b>Some of the recent improvement was help from outside.</b> Lower US tariffs lifted the latest quarter. The next quarter's growth is flattered because the same quarter last year was unusually weak.</li></ul>
<h3>The other side</h3>
<p>The cash is real. Crocs' free cash flow (${F['ttm_fcf']:,.0f} million) is higher than its adjusted profit, which you would not see if the profit were an accounting illusion. And Crocs left a one-off $64 million tariff refund <i>out</i> of its adjusted profit, which is the conservative choice.</p>
<p><b>What would settle it:</b> operating profit in dollars growing again in 2027, not just profit per share.</p>
{box("say", "Say it like this", f"<p>\"Profit per share is up about 20% since 2023, but the operating profit of the business is down about 14%. The whole difference is buybacks. We are comfortable with that because the buybacks are paid for with real cash, not debt. But it means we need the underlying profit to stop falling, and that is one of the things we are watching in February.\"</p>")}

<h2>2.7 Risk 3: insiders selling and managers changing</h2>
<h3>The insider selling</h3>
<p>\"Insiders\" are the company's directors and top managers. When they buy or sell the company's shares they must report it publicly within two working days on a form called a <b>Form 4</b>. Investors watch these because insiders know the business best.</p>
<ul><li>Over the last twelve months insiders <b>sold ${INS['sales_12m_usd']/1e6:.1f} million</b> of shares and <b>bought ${INS['buys_12m_usd']/1e6:.1f} million</b>.</li>
<li>The chief executive, Andrew Rees, sold {INS['ceo_sales_sh']:,.0f} shares for <b>${INS['ceo_sales_usd']/1e6:.1f} million</b> between June and November 2026.</li>
<li>Insiders sold ${INS['post_q3_sales_usd']/1e6:.1f} million in the week after the strong results in late October.</li></ul>
<p>There is a detail that matters here. Executives can set up a pre-arranged selling schedule months in advance, called a <b>10b5-1 plan</b>. Sales under a plan are less worrying because the timing was fixed before they knew the latest news. The Form 4 has a box to tick if the sale was under a plan. On all {INS['n_sales']} of these sales the box was not ticked.</p>
{box("warn", "Watch out", "<p>Say \"the forms do not show a pre-arranged plan\". Do not say \"there was no plan\". A plan could exist and simply not have been marked. That difference matters if someone in the audience knows the rules.</p>")}
<p><b>The other side:</b> the CEO still owns about {INS['ceo_shares_after']:,} shares, worth roughly ${INS['ceo_shares_after']*price/1e6:.0f} million. He sold around 13% of his holding after the share price doubled. Three directors bought shares when the price was between $75 and $112.</p>
<h3>The management changes</h3>
<ul><li>Three finance chiefs (CFOs) in 16 months. One resigned with immediate effect three weeks after a profit warning in August 2025.</li>
<li>HEYDUDE is on its fourth boss in four years.</li>
<li>Shareholders are suing over HEYDUDE. They claim Crocs pushed too much stock onto retailers in 2022-24 to make sales look better. The case has not been decided.</li></ul>
<p><b>What would settle it:</b> whether the CEO keeps selling above $150, and what the court decides.</p>

<h2>2.8 The other risks, quickly</h2>
<p>You do not need to present all of these. You do need to be able to answer if asked.</p>
{table(["Risk", "What it is, simply", "How big"], [
 ["Tariffs", "Taxes on shoes imported into the US. They were about 18-20% in 2025, were struck down by the Supreme Court in February 2026, and were replaced with 10-12.5%.", f"Each 1 point costs about $4m a year, about ${tar:.2f} of profit per share. Small, and it can go either way."],
 ["Factory concentration", "45% of Crocs are made in Vietnam, and two manufacturers make 73% of them.", "A problem at one supplier or in one country would hurt supply."],
 ["HEYDUDE relapses", "The second brand starts shrinking again.", "It is 17% of sales and already written down, so smaller than it was."],
 ["A stock market fall", "Crocs shares swing more than the market. In 2022 they fell 42% while the market fell 25%.", "In a 20% market fall, plan for Crocs to be down 25-30%."],
 ["The price has already risen", "The stock has doubled in a year and rose 34% in the last month. It is at the average analyst target.", "Raises the chance of a short-term dip. This is why the pitch says start with half a position."],
 ["Currency", "44% of sales are outside the US, so a stronger dollar reduces them when converted.", "About 0.7% of profit per share for each 1% move. Small."],
 ["Interest rates", "Just under half of Crocs' $1.3bn of debt has a floating rate.", "About 0.6% of profit per share for each 1 point. Small."],
 ["Debt", "Borrowings are about 1.2 times one year of profit before interest, tax and depreciation.", "Low. Nothing has to be repaid in the next 12 months."],
 ["One big customer", "Checked: no single customer is even 10% of sales.", "Not a risk. Worth saying, because it shows you checked."]], widths=[17, 45, 38], keep=False)}

<h2>2.9 What we would do about it: kill criteria</h2>
<p>A <b>kill criterion</b> is a rule you set in advance for when you would sell. The point is to decide while you are calm, so you do not talk yourself into holding a losing position later.</p>
{table(["If this happens...", "...it tells us", "Action"], [
 ["North America sales in Crocs' own stores and sites (adjusted for the accounting change) are negative two quarters in a row", "The fall was not just Crocs' own choice. The fad risk is real.", "Sell"],
 ["International growth drops below 5% for two quarters in a row", "The thing that was offsetting North America has stopped working.", "Sell"],
 ["Management guides 2027 operating margin below 21.5%", "The business is still getting less profitable.", "Sell"],
 ["Crocs makes another big acquisition (over $500m) or debt rises above 1.5 times profit", "The cash is no longer going to buybacks.", "Sell"],
 ["The CEO sells another 10% of his shares, or the CFO leaves", "Insiders are less confident than we are.", "Cut the position"]])}
{box("key", "Why this matters in a pitch", "<p>Kill criteria turn \"we think the risk is manageable\" into \"here is exactly what would prove us wrong\". Audiences trust the second version much more.</p>")}

<h2>2.10 Your risk section in about 90 seconds</h2>
{box("say", "Say it like this", f"<p>\"The reason Crocs is cheap is one fear: that the clog is a fad and the fad is ending. There is real evidence for that. North America sales fell about 7% last year and are still down 2%. In surveys, teenagers have moved Crocs from their 6th favourite shoe brand to their 10th. And it has happened before: between 2007 and 2009 Crocs lost a quarter of its sales.</p><p>So we measured it. We split the company's sales into nine parts and scored each for how exposed it is. About 16% of sales, roughly ${R['at_risk']:,.0f} million dollars, is at risk. Because a lot of Crocs' costs are fixed, losing 16% of sales would cut profit per share roughly in half, from about ${R['eps0']:.0f} dollars to about ${R['eps1']:.0f}. In that world the shares could be worth around ${R['val']:.0f} dollars.</p><p>We do not think that is the likely outcome. International sales are now more than half the brand and growing 12%. Our bear case, which we give a one-in-four chance, is ${bear:,.0f} dollars. The market is pricing closer to a 40% chance.</p><p>Two other things we are watching: profit per share is rising mainly because of buybacks while underlying profit is below 2023, and the CEO has sold {INS['ceo_sales_usd']/1e6:.0f} million dollars of shares since June. And we have set rules for when we would sell: if North America direct sales turn negative for two quarters, or international growth drops below 5%.\"</p>")}""")
# ================================= PART 3 CATALYSTS =================================
er = F["earn"]
add(f"""<div class="part"><div class="kicker">Part 3</div><h1>Catalysts: the dates that could move the stock, and what we need to see</h1></div>
<h2>3.1 What a catalyst is and why it matters</h2>
<p>A catalyst is a specific upcoming event that could change what investors think the company is worth. Company results, a court ruling, a new forecast from management: all catalysts.</p>
<p>They matter because of a simple problem: a cheap stock can stay cheap for years. \"It is undervalued\" is not enough. You also need a reason why other investors will come round to your view, and roughly when. Catalysts are that reason.</p>
{box("plain", "In plain English", "<p>The risk section says \"here is what we are arguing about\". The catalyst section says \"here are the dates on which new evidence arrives\". A good catalyst list is really a list of test dates for the risks.</p>")}

<h2>3.2 The most important idea: shares move on surprises, not on good or bad</h2>
<p>A share price already includes what investors expect. So the price moves when results are <b>different from what was expected</b>, not simply when they are good.</p>
<p>Crocs proves it. In the last eight sets of results, Crocs beat profit forecasts every single time. The shares still fell on three of those eight days.</p>
{fig("11_earnings_reactions.png", "80%")}
{table(["Results date", "What happened", "Share price that day"], [
 ["7 Aug 2025", "Profit beat forecasts, but Crocs wrote off $737m on HEYDUDE and warned next quarter's sales would fall 9-11%", "-29.2%"],
 ["30 Jul 2026", "Profit beat forecasts and the full-year forecast was raised, but the forecast for the next quarter was below what analysts hoped", "-7.4%"],
 ["29 Oct 2026", "Profit beat forecasts, full-year forecast raised a third time, HEYDUDE grew for the first time in three years", "+25.5%"]])}
<p>Two lessons. First, <b>what management says about the future matters more than the quarter just finished</b>. Second, Crocs shares move a lot on results days: the average move over the last eight is {F['earn_avg_abs_move']:.0f}%, up or down.</p>
{box("key", "Number to remember", f"<p><b>Average move on results day: {F['earn_avg_abs_move']:.0f}%.</b> Four of the last eight moved the stock by 19% or more.</p>")}

<h2>3.3 One quirk you must understand: Crocs' forecasts leave out buybacks</h2>
<p>When Crocs gives its profit-per-share forecast, it assumes it will buy back <b>no</b> shares in the period ahead. It then buys back hundreds of millions of dollars' worth. So its forecasts are built to be beaten, and most analysts copy the same assumption.</p>
<p>This is why the pitch's 2027 forecast is higher than everyone else's.</p>
{table(["2027 profit per share", "Number", "What it assumes"], [["Analysts' average (consensus)", "$16.01", "Few or no buybacks"], ["Our model, without any 2027 buybacks", f"${exbb:.2f}", "Shares already bought back in 2026, nothing more"], ["Our model, base case", f"${e27:.2f}", f"About ${B['bb']['FY2027E']:,.0f}m of buybacks in 2027"]], num_cols=(1,))}
<p>You can see the pattern in 2026. Crocs raised its full-year forecast after every quarter:</p>
{table(["Forecast given on", "12 Feb", "30 Apr", "30 Jul", "29 Oct"], [["2026 profit per share", "$12.88 to $13.35", "$13.20 to $13.75", "$13.70 to $14.00", "$14.45 to $14.65"], ["2026 sales growth", "-1% to slightly up", "-1% to +1%", "+1% to +2%", "about +3%"]])}

<h2>3.4 The calendar</h2>
{fig("17_catalyst_timeline.png", "100%")}
<p>There are two dates that matter most, shown in blue. Learn those two properly and know the rest in outline.</p>
<div class="card keycard"><div class="when">Around 11 February 2027 &nbsp;|&nbsp; the big one</div><h3>Results for the last quarter of 2026, and the first forecast for 2027</h3>
<p><b>What happens.</b> Crocs reports its October-December results and, for the first time, tells investors what it expects for 2027. The date is an estimate until Crocs confirms it.</p>
<p><b>Why it matters.</b> It tests two things at once: whether the recent improvement held over the Christmas season, and whether management's 2027 forecast is above what analysts already expect.</p>
<p><b>The numbers.</b> For the quarter, Crocs has said sales will grow 7-9% and profit per share will be $3.25 to $3.45. Analysts expect $3.40. For 2027, analysts expect $16.01.</p>
<div class="grid2"><div><p><b>Good outcome:</b> quarterly profit per share above about $3.60, and a 2027 forecast with a midpoint of $16 or more.</p></div><div><p><b>Bad outcome:</b> a 2027 forecast below about $15.50, or a profit-margin forecast below 21.5%. The second is one of our sell rules.</p></div></div>
<p><b>Our estimate of the odds:</b> about 60% that the 2027 forecast is at or above $16.</p></div>
<div class="card keycard"><div class="when">Late October 2027 &nbsp;|&nbsp; the fog lifts</div><h3>Results for the third quarter of 2027</h3>
<p><b>First, the \"fog\".</b> In the third quarter of 2026 one large online marketplace changed how it buys from Crocs. Before, Crocs counted those sales as its own direct sales, at the full shop price. Now Crocs sells the shoes to that partner at a lower wholesale price. The same number of shoes are sold. But on paper, North America direct sales look 7 to 8 percentage points worse than they really are, every quarter, until a full year has passed.</p>
<p><b>Why it matters.</b> North America is the heart of the fad debate, and for a year nobody outside the company can see the true trend. In late October 2027 the distortion drops out and we get the first clean number.</p>
<div class="grid2"><div><p><b>Good outcome:</b> North America direct sales are growing.</p></div><div><p><b>Bad outcome:</b> they are shrinking, with no accounting excuse left.</p></div></div>
<p><b>Our estimate of the odds:</b> about 55% that the number is positive.</p></div>
{box("plain", "In plain English: the fog", "<p>Imagine you sell lemonade at $2 a cup from your own stall. Then a shop offers to sell it for you, and you sell cups to the shop for $1 each. You sell the same number of cups, but your \"own stall\" sales drop to zero and your takings look lower. Nothing got worse. The sales just moved to a different column, at a lower price. That is what happened to part of Crocs' North America direct sales.</p>")}
<h3>The rest of the calendar</h3>
{table(["When", "Event", "Why it matters", "Numbers", "Our odds"], [
 ["1 Dec 2026", "Crocs speaks at an investor conference", "First hint about Black Friday and Christmas trading", "The quarter's forecast is sales +7-9%", "50% it moves the stock"],
 ["Late Apr and late Jul 2027", "Results for the first and second quarters", "The \"fog\" is at its thickest. North America will look bad on paper.", "Direct sales may show about -5% even if the true figure is +2%", "40% that investors look past it"],
 ["All year", "Share buybacks", "Not in Crocs' forecasts or analysts' numbers, so every purchase is a small positive surprise", f"$1.7bn approved, equal to {1700/F['mcap']*100:.0f}% of the company's value; about ${B['bb']['FY2027E']:,.0f}m expected in 2027", "85% they exceed $500m"],
 ["Any time", "Court case on US tariffs", "The current 10-12.5% tariffs are being challenged. Could be removed, or raised.", f"Each point is about ${tar:.2f} of profit per share. Full removal is worth about +$0.84", "20% removed, 20% raised"],
 ["Any time", "Ruling in the shareholder lawsuit", "Removes a worry, or keeps it alive", "No estimate of damages available", "50% dismissed"],
 ["About Oct 2027", "The teen survey", "Crocs is 10th. Dropping out of the top ten would feed the fad story.", "The stock fell 3% on a weak survey in 2024", "40% it drops out"],
 ["By Nov 2027", "Renewing the bank borrowing facility", "Routine, but must be done", "$1.0bn facility, $113m in use", "90% no problem"]], widths=[13, 19, 27, 25, 16], keep=True)}
{box("warn", "Watch out: things that are NOT catalysts", "<p>If asked: Crocs is too small to join the S&P 500 index, so that is not coming. No investor day has been announced. And Crocs used to give an early trading update each January but has not done so for the last two years, so do not promise one.</p>")}

<h2 class="np">3.5 How the catalysts connect to the risks</h2>
<p>This table is the most useful thing in your section, because it shows the two halves are one piece of thinking.</p>
{table(["The risk", "When we learn more", "Good sign", "Bad sign (our sell rule)"], [
 ["The fad risk in North America", "A first read in February 2027. The clean read in late October 2027.", "Direct sales growing once adjusted", "Negative two quarters in a row"],
 ["International slows down", "Every quarter", "Growth of 7% or more", "Below 5% two quarters in a row"],
 ["Profitability keeps slipping", "February 2027 forecast", "Operating margin forecast of 22.5% or more", "Forecast below 21.5%"],
 ["Earnings quality", "February 2027 and through the year", "Operating profit in dollars growing", "Profit per share up only because of buybacks, again"],
 ["Insiders selling", "Any time a Form 4 is filed", "Selling stops, or a plan is disclosed", "CEO sells another 10%"],
 ["Tariffs", "Whenever the court rules", "Tariffs removed", "Tariffs raised"],
 ["HEYDUDE", "Every quarter", "Sales flat or up", "Down more than 5%"]])}

<h2>3.6 Your catalyst section in about 75 seconds</h2>
{box("say", "Say it like this", f"<p>\"A cheap stock needs a reason to stop being cheap, so here is when we find out if we are right.</p><p>The first date is around the 11th of February, when Crocs reports its Christmas quarter and gives its first forecast for 2027. Analysts expect 16 dollars of profit per share for 2027. Crocs' forecasts leave out share buybacks, and even on that basis we get about {exbb:.1f} dollars, so we think there is a 60% chance the forecast comes in at or above what the market expects.</p><p>The second date is late October 2027. For the next year, an accounting change makes North America sales look 7 to 8 points worse than they really are. In October that drops out and we get the first clean look at whether the clog business in America is growing or shrinking. That is the number that settles the fad debate.</p><p>In between, there is a steady tailwind: Crocs has approval to buy back 1.7 billion dollars of shares, about {1700/F['mcap']*100:.0f}% of the company, and none of that is in anyone's forecasts.</p><p>One warning. Crocs shares move about {F['earn_avg_abs_move']:.0f}% on a typical results day, and they have fallen even on good results when the outlook disappointed. So we would start with half a position and add if the shares dip.\"</p>")}""")
# ================================= PART 4 SPEAKING =================================
qa = [("What is the single biggest risk?", f"That the clog is a fashion fad and it is ending in North America, which is still Crocs' biggest single market. Sales there fell about 7% last year. If it gets worse, our stress test says profit per share could halve."),
      ("How did you get to 16% of sales at risk? Is that not just made up?", f"The sales figures are from Crocs' reports. The 1-to-5 scores are our judgement, and we say so. We set the top score to match what really happened to Crocs in 2007-09 and to HEYDUDE in 2023-25, when sales fell about a quarter. Then we tested it: moving every score a notch either way gives 9% to 24%, and the conclusion does not change."),
      ("Why would profit fall so much more than sales?", "Because a lot of the costs are fixed. Store rents, salaries and systems do not shrink when you sell fewer shoes. So when sales fall, the profit absorbs most of the drop. We estimate about 1.2 billion dollars of Crocs' costs behave that way."),
      ("How likely is the bad outcome?", f"We give the bear case a one-in-four chance. The share price today implies the market thinks it is closer to 40%. We would be honest that our edge is that gap, and that if the true chance were above about 50% this would not be a good investment."),
      ("What would make you sell?", "Three main things. North America direct sales negative for two quarters once adjusted for the accounting change. International growth below 5% for two quarters. Or a 2027 margin forecast below 21.5%. We would also cut if the CEO sold another 10% of his shares."),
      ("The CEO is selling. Why should we buy?", f"It is a fair concern and we flag it. He sold about {INS['ceo_sales_usd']/1e6:.0f} million dollars of shares since June, and the filings do not show a pre-arranged plan. Against that, he still owns over 100 million dollars' worth, and he sold about 13% after the price doubled. If he keeps selling, that is one of our sell rules."),
      ("What is the next catalyst, and what do you need to see?", f"Results around the 11th of February with the first 2027 forecast. We want a profit-per-share forecast of 16 dollars or more, and a margin forecast of at least 22.5%. Below 15.50, or a margin below 21.5%, and we would reconsider."),
      ("What if results are good but the stock falls anyway?", "It has happened twice in the last eight quarters, both times because the outlook for the next quarter was soft. That is why we would start with half a position. If the fall is about short-term outlook and none of our sell rules is triggered, we would buy more."),
      ("Are tariffs not a huge risk?", f"Less than you would think. Each point of tariff costs Crocs about 4 million dollars a year, around {tar*100:.0f} cents of profit per share. Tariffs were cut from about 19% to 10-12.5% this year. It could go either way from here, but it is not what decides whether this investment works."),
      ("The stock has doubled. Is the good news not already in the price?", f"A lot of it is, and we say so. The shares are at the average analyst target and are no longer cheap compared with similar companies. What is not in the price is the buybacks: they are missing from the company's forecasts and from most analysts' numbers. That is where our extra profit per share comes from."),
      ("Crocs crashed in 2008. Why is this time different?", f"Three differences. Then, Crocs was losing money; now it generates over 700 million dollars of spare cash a year. Then, it was mostly a US business; now more than half the brand's sales are abroad. And then its profit on each shoe collapsed, with gross margin falling from 59% to 32%; now it is deliberately holding back supply and discounts to protect that margin. It could still happen, which is why it is our main risk."),
      ("What if the whole stock market falls?", "Crocs usually falls more than the market. In 2022 it fell 42% when the market fell 25%. For a 20% market fall we would plan on Crocs being down 25 to 30%. That is a reason for a medium-sized position, not a reason to avoid it.")]
add(f"""<div class="part"><div class="kicker">Part 4</div><h1>Speaking: scripts, questions, numbers and mistakes to avoid</h1></div>
<h2>4.1 Your whole section in 30 seconds</h2>
<p>If you are short of time, or someone asks you to sum up, this is the core.</p>
{box("say", "Say it like this", f"<p>\"The main risk is that the clog is a fad. We measured it: about 16% of sales is exposed, and a full unwind would halve profit per share. We think that is a one-in-four outcome and the market is pricing closer to 40%. We find out who is right on two dates: the 2027 forecast in February, and October 2027, when we get the first clean look at North America. And we have written down in advance what would make us sell.\"</p>")}
<h2>4.2 Twelve questions you might get</h2>
<p>Answers are short on purpose. Each has one number in it. Practise saying them aloud rather than reading them.</p>
<div class="qa">""" + "".join(f"<h3>{i}. {html.escape(q)}</h3><p>{a}</p>" for i, (q, a) in enumerate(qa, 1)) + f"""</div>
<h2>4.3 Twelve numbers to know by heart</h2>
{table(["#", "Number", "What it is"], [
 ["1", f"<b>${price:.0f}</b>", "Share price today (25 November 2026)"], ["2", f"<b>${base:,.0f}</b>", f"Base-case target for December 2027 ({rba:+.0f}%). Our estimate."],
 ["3", f"<b>${bear:,.0f}</b>", f"Bear case ({rb:+.0f}%), 25% chance. Our estimate."], ["4", f"<b>about ${R['val']:.0f}</b>", "Worst case if the fad fully unwinds. Our estimate."],
 ["5", f"<b>16%</b>", f"Share of sales at risk (${R['at_risk']:,.0f} million). Our estimate."], ["6", f"<b>${R['eps0']:.0f} to ${R['eps1']:.0f}</b>", "Profit per share before and after the stress test: roughly halved."],
 ["7", "<b>25% vs 40%</b>", "Our chance of the bear case vs what the share price implies."], ["8", "<b>-7% and -2%</b>", "North America Crocs sales: 2025, and the latest quarter. Reported."],
 ["9", "<b>+12% and over half</b>", "International growth in the latest quarter, and its share of the brand. Reported."], ["10", f"<b>${INS['ceo_sales_usd']/1e6:.0f} million</b>", "Shares sold by the CEO, June to November 2026. Reported."],
 ["11", "<b>11 Feb and late Oct 2027</b>", "The two key dates: the 2027 forecast, and the first clean North America number."], ["12", f"<b>{F['earn_avg_abs_move']:.0f}%</b>", "Average share-price move on a results day."]])}
<h2>4.4 Mistakes to avoid</h2>
<ul><li><b>Do not say there is little risk.</b> The honest position is stronger: the downside in the bear case ({rb:+.0f}%) is bigger than the upside in the base case ({rba:+.0f}%), and the bet works because of the odds.</li>
<li><b>Do not mix up ${bear:,.0f} and ${R['val']:.0f}.</b> Bear case versus worst case.</li>
<li><b>Do not present estimates as facts.</b> Say \"we estimate\" for scores, probabilities and price targets.</li>
<li><b>Do not say the CEO sold \"without a plan\".</b> Say the filings do not show one.</li>
<li><b>Do not say North America is growing.</b> Reported sales are down 2%. Only direct sales, adjusted for the accounting change, are up.</li>
<li><b>Do not call HEYDUDE a success.</b> It grew one quarter against a very weak comparison. Management itself said so.</li>
<li><b>Do not promise dates.</b> The February results date is an estimate. Say \"around\".</li>
<li><b>Do not forget the date of your data.</b> Everything here is as of 25 November 2026. If you present after 1 December or after the February results, check what has changed.</li></ul>
<h2>4.5 What is fact and what is our estimate</h2>
{table(["Reported facts (from Crocs' filings and market data)", "Our estimates (from the pitch model)"], [
 ["Sales, profit, margins, share counts for past periods", "Price targets: $92, $207, $289"], ["North America and international growth rates", "Probabilities: 25%, 50%, 25%"], ["Product mix: clogs 74%, sandals 13%, charms 8% (2025)", "The nine risk scores and the score-to-fall table"],
 ["Insider trades and amounts", "The split between fixed and variable costs"], ["Crocs' own forecasts for 2026", "All 2027 and 2028 forecasts, including $17.27"], ["Analysts' average forecast of $16.01 for 2027", "The odds on each catalyst"],
 ["Tariff rates and the $64m refund", "The \"40% implied by the market\" calculation"], ["Debt amounts and repayment dates", "The split of each region's sales by product"]])}
<p class="small">Things that could not be found and that you should not guess at if asked: how much a rise in oil prices would cost Crocs; how much the shareholder lawsuit could cost; sales figures for individual countries; a confirmed date for the February results. The full source list, with links, is in <b>sources.md</b>, and the detailed workings are in <b>deep-dive.md</b> and <b>model.xlsx</b> in the same folder.</p>""")
doc = f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>Crocs (CROX): the risks and the catalysts - study guide</title><style>{CSS}</style></head><body>{''.join(P)}</body></html>"
hp = os.path.join(ROOT, "study-guide.html"); open(hp, "w").write(doc)
js = """
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.argv[2], { waitUntil: 'networkidle' });
  await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-family:Inter,Arial,sans-serif;font-size:7.5pt;color:#5f6368;width:100%;padding:0 16mm;display:flex;justify-content:space-between;"><span>Crocs (CROX): risks and catalysts. Study guide. Data as of 25 Nov 2026. Not investment advice.</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
    margin: { top: '17mm', bottom: '18mm', left: '16mm', right: '16mm' } });
  await b.close();
})();
"""
jp = os.path.join(ROOT, "scripts", "_print_pdf.js"); open(jp, "w").write(js)
out = os.path.join(ROOT, "study-guide-risk-and-catalysts.pdf")
subprocess.run(["node", jp, hp, out], check=True); os.remove(hp)
from pypdf import PdfReader
print("saved", out, "pages:", len(PdfReader(out).pages), "words:", len(" ".join(P).split()))
