import re, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Applications2027/48f0ca46-3145-5442-8b7b-eeed664bcf13/scratchpad')
from svg import fig
import diagrams as D
SP = '/tmp/claude-0/-home-user-Applications2027/48f0ca46-3145-5442-8b7b-eeed664bcf13/scratchpad/'
OUT = '/home/user/Applications2027/HarrisonStreet/'

def S(*ids):
    return '<span class="s">[' + ', '.join(ids) + ']</span>'
CF = '<span class="c cf">Confirmed</span>'; RP = '<span class="c rp">Reported</span>'; IN = '<span class="c inf">Inferred</span>'
def bx(kind, title, body):
    return f'<div class="box {kind}"><b class="t">{title}</b>{body}</div>'
KEY = lambda t, b: bx('key', 'KEY TERM: ' + t, b)
SAY = lambda b: bx('say', 'SAY THIS IN THE INTERVIEW', b)
DONT = lambda b: bx('dont', "DON'T SAY THIS", b)
OP = lambda b: bx('op', 'YOUR OPINION GOES HERE', b)
UNC = lambda b: bx('unc', 'SOURCE UNCERTAIN', b)

parts = []
toc = []
def part(id_, title, sub=''):
    toc.append((id_, title, True))
    return f'<h2 class="part" id="{id_}">{title}<small>{sub}</small></h2>'
def sec(id_, title):
    toc.append((id_, title, False))
    return f'<h3 id="{id_}">{title}</h3>'

# ---------------- PART 0
parts.append(part('p0', 'Part 0. The answer on one page', 'Read this if you only have ten minutes'))
parts.append('''
<p class="big">Real estate investor relations is the job of finding money for property funds and then looking after the people who gave it.</p>
<p>A real estate investment manager like Harrison Street does not mostly use its own money. It runs funds. Big savers, such as pension funds that pay teachers' and firefighters' pensions, put money into those funds. The manager's deal teams then buy, build and run buildings with it. The manager is paid fees for doing this, plus a share of profits if returns are good.</p>
<p>Investor relations, which Harrison Street calls the <b>Investor Solutions Group (ISG)</b>, sits between the investors and the funds. It does two things:</p>
<ol><li><b>Raise:</b> find investors who might want a fund, pitch it, answer their due diligence questions, and help get them to sign a commitment.</li>
<li><b>Retain:</b> report to existing investors every quarter, answer whatever they ask, and keep them happy enough to invest in the next fund.</li></ol>
''')
parts.append(fig(D.d_onepicture(), 'Figure 0.1. Who is the client?', 'author synthesis from the job description and [F6], [F8]. [Inferred]'))
parts.append('''
<table><tr><th style="width:28%">Question</th><th>Short answer</th></tr>
<tr><td>Who is the client?</td><td>The <b>investor</b> in the fund: pensions, sovereign wealth funds, insurers, endowments, and wealth advisers who invest for rich individuals. Plus the <b>investment consultants</b> who advise them. Not the tenant. Not a buyer of a building.</td></tr>
<tr><td>What is being sold?</td><td>A share of a fund: a long, illiquid commitment to a strategy and a team. Often the buildings have not been bought yet.</td></tr>
<tr><td>How is it different from estate agency?</td><td>An agent (CBRE, JLL, Colliers' brokers) earns a one-off fee per deal. A fund manager earns recurring fees on the money it manages. ISG raises money for funds, not for one building. ''' + S('I52') + '''</td></tr>
<tr><td>How is it different from company IR?</td><td>A listed company's IR talks to shareholders who can sell any day. Fund IR talks to a few hundred professional investors who are locked in for years and negotiate terms. ''' + S('I42', 'I50') + '''</td></tr>
<tr><td>What is Harrison Street?</td><td>A Chicago-founded (2005) manager of "alternative" real assets: student and senior housing, life science, storage, data centres, infrastructure and credit. About $110bn of assets, majority owned by Colliers. ''' + S('F2', 'F8', 'F3') + CF + '''</td></tr>
<tr><td>What would I do?</td><td>Build slides, draft answers to investor questions, keep Salesforce clean, research potential investors in Europe and the Middle East, track rivals' fundraising, and help run conferences.</td></tr></table>
''')
parts.append(SAY('"ISG is the firm\'s link to its capital. It raises money for the funds and then services the investors who gave it. At Harrison Street that means selling a demand-driven, alternatives-only story to pensions, sovereign funds and wealth advisers, and the best fundraising for the next fund is the reporting we do on this one."'))

# ---------------- PART 1
parts.append(part('p1', 'Part 1. Real estate investing from zero', 'The building, the fund, the manager, the investor'))
parts.append(sec('p1a', 'Four players'))
parts.append('''
<p>Every real estate fund has four players. Learn them and the rest of this pack falls into place.</p>
<table><tr><th style="width:20%">Player</th><th>What they are</th><th style="width:30%">At Harrison Street</th></tr>
<tr><td><b>Investor (LP)</b></td><td>The source of the money. "LP" means limited partner: a part-owner of the fund whose liability is limited to what it put in, and who has no say in day-to-day decisions.</td><td>Over 1,100 institutions and over 300 wealth advisers ''' + S('F8') + CF + '''</td></tr>
<tr><td><b>Manager (GP)</b></td><td>"GP" means general partner: the firm that runs the fund, picks the deals and is responsible for it. Also called the sponsor or investment manager.</td><td>Harrison Street Asset Management</td></tr>
<tr><td><b>Fund</b></td><td>The legal pot that holds the money and the buildings. Often a limited partnership, sometimes a Luxembourg vehicle in Europe.</td><td>e.g. Core Property Fund, Real Estate Partners IX, European Property Partners III ''' + S('F11', 'F6', 'F26') + '''</td></tr>
<tr><td><b>Occupier</b></td><td>The people who use the buildings and pay rent: students, older residents, labs, storage users, data centre tenants.</td><td>The end demand that the strategy is built around</td></tr></table>
''')
parts.append(KEY('AUM', 'Assets under management: the total value of money and assets a manager runs for clients. It includes borrowed money in some counts, so "fee-paying AUM" (the part that earns fees) is often much lower. Harrison Street: $108.2bn AUM but $54.2bn fee-paying at 31 Dec 2025 ' + S('F3') + '.'))
parts.append(sec('p1b', 'How the money flows'))
parts.append(fig(D.d_moneyflow(), 'Figure 1.1. Money through a real estate fund, step by step.', 'generic structure, author synthesis [Inferred]; fee and carry concepts per [I42], [I32].'))
parts.append('''
<ol><li><b>Commitment and capital calls.</b> An investor promises an amount, say $100m. The manager does not take it all at once. It "calls" capital when it has a deal. Money promised but not yet called is called <i>dry powder</i> or <i>unfunded commitment</i>.</li>
<li><b>Equity in, plus debt.</b> The fund adds bank loans to the investors' money. <i>LTV</i> (loan-to-value) is loan divided by property value. More debt means higher potential return and higher risk.</li>
<li><b>Income.</b> Occupiers pay rent. For senior housing or student housing, the building is also a business with staff and services.</li>
<li><b>Cash and value.</b> Income and any sale proceeds flow back to the fund.</li>
<li><b>Distributions.</b> The fund pays investors back. In a closed-end fund this comes mostly as buildings are sold.</li>
<li><b>Fees and carry.</b> The manager takes a management fee (a percentage of money committed or invested) and, if returns pass a minimum level called the <i>hurdle</i> or <i>preferred return</i>, a share of profits called <i>carried interest</i>. Older industry studies quote about 150 basis points (1.5%) on committed equity and 20% carry for opportunity funds, and about 70 basis points for core funds ''' + S('I32') + RP + '''. These are dated, general figures, not Harrison Street's terms.</li></ol>
''')
parts.append(UNC('Harrison Street\'s actual fees are private and set fund by fund in legal documents. No source in this pack shows them. Never quote a number for HS fees in the interview.'))
parts.append(sec('p1c', 'Why investors use a manager at all'))
parts.append('''
<p>A pension fund with £20bn could, in theory, buy student housing itself. Most do not, for four reasons. [Inferred]</p>
<ul><li><b>Access:</b> the manager finds and wins deals the pension never sees.</li>
<li><b>Operations:</b> running a senior housing community is closer to running a hotel and care business than owning an office. Specialists do it better.</li>
<li><b>Diversification:</b> one fund cheque buys exposure to 70 assets. Fund IX was about 70% allocated across 70 assets at final close ''' + S('F6') + CF + '''.</li>
<li><b>Staff:</b> a pension's real estate team may be three people. They outsource the work and keep the oversight.</li></ul>
<p>That last point is why IR exists. The pension's three people need answers, data and confidence. ISG provides them.</p>
''')

# ---------------- PART 2
parts.append(part('p2', 'Part 2. Who is the client?', 'The question you asked, answered in full'))
parts.append(sec('p2a', 'Two different customers, do not mix them up'))
parts.append('''
<p>A real estate firm has two kinds of customer, and people outside the industry often confuse them.</p>
<div class="two"><div class="card"><h4>The occupier</h4><p>Students, residents, patients, lab tenants. They pay rent. They are the customer of the <b>property and asset management</b> teams and the operators who run the buildings. ISG never sells to them.</p></div>
<div class="card" style="border-color:#e09f3e"><h4>The investor (your client)</h4><p>The institutions and advisers who put money into the funds. They pay fees. They are the customer of <b>ISG</b>. The JD's "current clients, consultants and prospective investors" all sit here.</p></div></div>
<p>The two are linked. Happy occupiers mean full buildings, steady income and good returns. Good returns are what ISG reports and sells. So ISG cares about occupancy figures, but it does not manage occupiers. [Inferred]</p>
''')
parts.append(sec('p2b', 'The investor types, one by one'))
parts.append(fig(D.d_clientmap(), 'Figure 2.1. The three groups ISG serves.', 'investor types from [F6], [F8], [F14]; gatekeeper role from [I24], [I22]. Grouping is the author\'s. [Inferred]'))
parts.append('''<table><tr><th style="width:19%">Investor type</th><th>What it is</th><th style="width:31%">What it wants from real estate</th></tr>
<tr><td>Public pension fund</td><td>Pays pensions for public workers. In the UK, the Local Government Pension Scheme (LGPS); in the US, plans like CalSTRS (California teachers).</td><td>Long, steady, inflation-linked income to match pensions paid out over decades. CalSTRS put €150m into HS European Property Partners III ''' + S('F27') + RP + '''</td></tr>
<tr><td>Corporate pension</td><td>A company's own staff pension.</td><td>Similar, often more cautious as schemes mature.</td></tr>
<tr><td>Taft-Hartley plan</td><td>A US union-run pension (named after a 1947 US law). Listed among Fund IX investors ''' + S('F6') + '''</td><td>Income and safety.</td></tr>
<tr><td>Sovereign wealth fund (SWF)</td><td>A state investment fund, e.g. ADIA (Abu Dhabi), QIA (Qatar), PIF (Saudi Arabia), KIA (Kuwait).</td><td>Big tickets, long horizons, often co-investment and separate accounts. Gulf SWFs invested a record $119bn in 2025 ''' + S('I39') + RP + '''</td></tr>
<tr><td>Insurer</td><td>Holds premiums for decades before paying claims.</td><td>Income to match long liabilities; credit is attractive too.</td></tr>
<tr><td>Endowment / foundation</td><td>University or charity money meant to last for ever.</td><td>Higher return, will accept illiquidity.</td></tr>
<tr><td>Wealth adviser (RIA)</td><td>US "registered investment adviser" managing rich individuals' money. Invests via easier products like interval funds.</td><td>Smaller cheques, some liquidity, simple reporting. HS serves 300+ RIAs ''' + S('F8') + '''</td></tr></table>
''')
parts.append(sec('p2c', 'The gatekeepers: consultants and pools'))
parts.append('''
<p><b>Investment consultants</b> such as Mercer advise pensions on which managers to hire. They research managers and give ratings. Mercer grades strategies A, B, C or R and says it has over 11,400 ratings and more than 250 due diligence staff ''' + S('I24') + CF + '''. If a consultant does not rate your fund, many pension clients will not even take the meeting. That is why the JD lists consultants separately and why HSAM's global co-head of ISG leads "consultant engagement" ''' + S('F19') + '''.</p>
<p><b>UK LGPS pools.</b> The UK government is forcing local council pension funds into fewer, bigger pools. Its 4 June 2025 response backed six pools, down from eight, with a pooling deadline of 31 March 2026, and the pools must be FCA-authorised ''' + S('I22') + CF + '''. The Pension Schemes Act 2026 received Royal Assent on 29 April 2026 ''' + S('I23') + RP + '''. For an IR team this means fewer, larger buyers with professional teams.</p>
<p><b>Dutch pensions</b> are moving about €1.8 to €1.9 trillion into a new system by January 2028 ''' + S('I40') + RP + ''', which shifts how they buy illiquid assets. APG is reported to be lifting private markets from about 26% to just over 30% ''' + S('I41') + RP + '''.</p>
''')
parts.append(KEY('Placement agent', 'A third-party firm a manager hires to help raise money, paid mainly a success fee. It works for the manager, not the investor ' + S('I53') + '. So it is a partner of ISG, not a client.'))
parts.append(sec('p2d', 'How much do investors want real estate right now?'))
parts.append('''
<p>The Hodes Weill and Cornell Baker 2025 survey found the average institutional target allocation to real estate fell to 10.7%, the first fall since the survey began in 2013. Investors sat 90 basis points below target, and expected a 10 basis point rise in 2026 led by Europe, Middle East and Africa ''' + S('I2', 'I3') + CF + '''. Douglas Weill called it "a tactical pause... rather than a strategic shift away from real estate" ''' + S('I3') + '''.</p>
<p>The INREV/ANREV/PREA 2026 intentions survey put the global allocation at 12.4% against a 12.5% target, with European investors about 20 basis points over a 13.9% target, and debt funds the most favoured vehicle ''' + S('I15') + CF + '''. The two surveys use different samples, so do not compare the numbers directly.</p>
''')
parts.append(OP('Under-allocated investors are a fundraising opportunity, but the competition for that money is not only other real estate funds. Infrastructure and private credit are taking share ' + S('I4', 'I63') + '. Harrison Street sells all three, which lets ISG keep a client even when the client\'s money moves between asset classes. Do you think that is a real advantage, or does it blur the firm\'s identity?'))

# ---------------- PART 3
parts.append(part('p3', 'Part 3. What investor relations actually does', 'Raise, then retain'))
parts.append(fig(D.d_twohalves(), 'Figure 3.1. The two halves of the job.', 'tasks from the JD and [I42], [I43]. Re-up link: Fund IX ~60% from existing investors [F6].'))
parts.append(sec('p3a', 'Raising a fund, stage by stage'))
parts.append(fig(D.d_fundraise(), 'Figure 3.2. One investor\'s path into one fund.', 'stages from [I42], [I14], [I24]; timing from [I1].'))
parts.append('''<table><tr><th style="width:17%">Stage</th><th>What happens</th><th style="width:30%">Documents and tools</th></tr>
<tr><td>Map</td><td>Build a target list: which investors have money, like this strategy and invest in this region. The JD asks you to "map and conduct research on potential investors in Europe and Middle East".</td><td>Salesforce, databases (PERE lists 15,000+ institutions ''' + S('I1') + '''), annual reports, pension board minutes</td></tr>
<tr><td>Pre-market</td><td>Test interest before a fund is formally offered. In the EU this is a defined, regulated activity since 2 August 2021 ''' + S('I14') + '''.</td><td>Draft terms, no subscription documents</td></tr>
<tr><td>Meet</td><td>Introductory meetings, then deeper sessions with the portfolio managers.</td><td>Pitch book, track record, market research</td></tr>
<tr><td>Diligence</td><td>The investor and its consultant check everything: team, track record, risk, operations, ESG.</td><td>DDQ (due diligence questionnaire), RFP responses, virtual data room. INREV publishes a standard DDQ ''' + S('I17') + '''</td></tr>
<tr><td>Approve</td><td>The investor's own investment committee votes.</td><td>Consultant recommendation paper</td></tr>
<tr><td>Legal</td><td>Negotiate the limited partnership agreement (LPA) and side letters with special terms ''' + S('I42') + '''.</td><td>LPA, subscription docs, side letters</td></tr>
<tr><td>Close</td><td>Money is legally committed. Funds hold a first close and later a final close.</td><td>Press release, e.g. Fund IX final close, 7 Oct 2024 ''' + S('F6') + '''</td></tr></table>
''')
parts.append(sec('p3b', 'Retaining investors: the quiet half'))
parts.append(fig(D.d_lifecycle(), 'Figure 3.3. What an investor experiences over a fund\'s life.', 'illustrative J-curve shape [Inferred]; re-up share [F6].'))
parts.append('''<p>Once an investor is in, ISG and its Investor Services colleagues owe them a steady stream of information. Industry standards set the shape:</p>
<ul><li><b>INREV Reporting Guidelines</b> (Europe): an annual report plus interim reports, covering governance, performance, the property portfolio, risk and ESG. The current version applies to reporting periods from 1 January 2024 ''' + S('I16') + CF + '''.</li>
<li><b>ILPA Reporting Template v2.0</b> (mainly private equity, US-led): released January 2025, applies to funds starting from 1 January 2026, and standardises how fees, expenses and carry are shown ''' + S('I20') + CF + '''.</li>
<li><b>Ad hoc requests:</b> "what is your exposure to UK student housing by city?", "send us your carbon data for our own report". The JD calls these "ad-hoc client requests for information and investment analysis".</li></ul>
''')
parts.append(fig(D.d_request(), 'Figure 3.4. The life of one investor request.', 'author synthesis from the JD and compliance rules in Part 7. [Inferred]'))
parts.append(sec('p3c', 'ISG as the hub of the firm'))
parts.append('<p>ISG does not own most of the information it sends out. It gathers it. That makes it one of the most connected teams in the building. A Chicago ISG posting said the role works "closely with the Investor Services and Marketing teams" ' + S('F20b') + CF + '.</p>')
parts.append(fig(D.d_isg_inside(), 'Figure 3.5. Who ISG pulls from to answer one investor.', 'functions inferred from postings [F20b], [F19] and standard practice. [Inferred]'))
parts.append(sec('p3d', 'The calendar: conferences'))
parts.append('''<p>The JD asks you to support "the team's attendance to conference, industry events and sponsorship applications". The European calendar a London ISG team would know, 2026 dates ''' + S('I55', 'I56', 'I57', 'I58', 'I59') + RP + ''':</p>
<table><tr><th>Event</th><th>Where</th><th>2026 dates</th><th>Why it matters</th></tr>
<tr><td>MIPIM</td><td>Cannes</td><td>9-13 March</td><td>The biggest European property fair</td></tr>
<tr><td>INREV Annual Conference</td><td>Barcelona</td><td>7-9 April (2027: 12-14 April)</td><td>Investors in non-listed European real estate</td></tr>
<tr><td>SuperReturn International</td><td>Berlin</td><td>8-12 June</td><td>Private markets broadly, many LPs</td></tr>
<tr><td>PERE Europe Forum</td><td>London</td><td>15-16 September</td><td>Private real estate fundraising</td></tr>
<tr><td>Expo Real</td><td>Munich</td><td>5-7 October</td><td>German-speaking market</td></tr></table>
''')

# ---------------- PART 4
parts.append(part('p4', 'Part 4. How real estate IR differs from everything near it', 'So you never confuse it in the interview'))
parts.append(fig(D.d_jobsgrid(), 'Figure 4.1. Real estate jobs on two axes: who you face, and at what level.', 'author synthesis; agency vs manager economics per [I52]; listed IR per [I50]. [Inferred]'))
parts.append(sec('p4a', 'Versus listed company investor relations'))
parts.append(fig(D.d_listed_vs_private(), 'Figure 4.2. Two jobs with the same name.', 'MAR Art. 17 and Reg FD [I50]; private fund features [I42], [I28].'))
parts.append('<p>A REIT (real estate investment trust, a company that owns property and trades on a stock exchange) has an investor relations team too, but the job is different. Its rules are about <b>disclosure</b>: under the Market Abuse Regulation, Article 17, inside information must go to everyone at once, not to favoured analysts ' + S('I50') + RP + '. Fund IR rules are about <b>marketing</b>: who you may approach, with what, and when (Part 7). Mergers &amp; Inquisitions notes a move from corporate IR into private fund IR is "uncommon" because the skills differ ' + S('I42') + '.</p>')
parts.append(sec('p4b', 'Versus the rest'))
parts.append('''<table><tr><th style="width:22%">Role</th><th>Main counterparty</th><th>How it earns</th><th style="width:30%">Key difference from ISG</th></tr>
<tr><td>Agency capital markets (CBRE, JLL, Colliers brokerage)</td><td>Building owners and buyers</td><td>One-off commission per deal ''' + S('I52') + '''</td><td>Raises money for <i>one deal</i>. ISG raises it for a <i>fund</i>, often before the deals exist.</td></tr>
<tr><td>Property management</td><td>Tenants, residents</td><td>Contract fee</td><td>Faces occupiers, not investors.</td></tr>
<tr><td>Asset / portfolio management</td><td>Buildings, operators</td><td>Part of the manager</td><td>Produces the results ISG reports. Your best internal source.</td></tr>
<tr><td>Acquisitions</td><td>Sellers, brokers</td><td>Part of the manager</td><td>Spends the money ISG raised.</td></tr>
<tr><td>Long-only asset manager sales</td><td>Wholesale and institutional buyers</td><td>Fees on daily-dealing funds</td><td>Liquid products, fast sales. ISG sells illiquid commitments over many months. [Inferred]</td></tr>
<tr><td>Private equity IR</td><td>LPs</td><td>Fees and carry</td><td>The closest cousin: same GP/LP model. Real estate adds property data (INREV, valuations, GRESB). ''' + S('I16', 'I20') + '''</td></tr>
<tr><td>Hedge fund IR</td><td>LPs</td><td>Fees and performance fee</td><td>Monthly NAVs, open subscriptions and redemptions. [Inferred]</td></tr></table>
''')
parts.append(DONT('"It\'s basically sales." Half of the job is service and reporting, and nothing goes out without compliance sign-off. Also avoid "it\'s like estate agency". Agents sell buildings; ISG sells a team\'s ability to buy and run buildings for a decade.'))
parts.append(SAY('"An agent raises money for a building. ISG raises money for a strategy and a team, often before the buildings exist, so what we really sell is trust and evidence: track record, process and transparent reporting."'))

# ---------------- PART 5
parts.append(part('p5', 'Part 5. The products ISG sells', 'Fund types, risk styles and channels'))
parts.append(sec('p5a', 'Open-end versus closed-end'))
parts.append(fig(D.d_open_closed(), 'Figure 5.1. The two basic fund shapes.', 'generic structures; HS examples from [F11], [F6]. ~10-year life [I43] Reported.'))
parts.append('<p>This matters for your daily work. An open-end fund needs steady selling and reporting all the time. A closed-end fund has a burst of fundraising every few years. Harrison Street runs both: its Core Property Fund had a gross asset value of $15.12bn at the March 2026 filing ' + S('F11') + CF + ', and its US opportunistic series reached its ninth fund in 2024 and launched a tenth in 2025, which took $1bn at first close against a $3bn hard cap ' + S('F6', 'F23') + RP + '. No final close for Fund X had been found as of 8 October 2026.</p>')
parts.append(sec('p5b', 'The risk ladder: core to opportunistic'))
parts.append(fig(D.d_spectrum(), 'Figure 5.2. Real estate risk styles, using the European industry body\'s definitions.', '[I51] (snippet of INREV 2012 classification, Reported); HS products [F11], [F6].'))
parts.append(sec('p5c', 'The Harrison Street shelf'))
parts.append('''<table><tr><th style="width:24%">Product family</th><th>What it is</th><th style="width:28%">Size / latest fact</th></tr>
<tr><td>Core Property Fund (US, open-end)</td><td>Launched 2011; alternative property only (student, senior, medical office, storage, and more) ''' + S('F34') + '''</td><td>$15.12bn GAV, Form ADV March 2026 ''' + S('F11') + CF + '''</td></tr>
<tr><td>Real Estate Partners series (US, closed-end opportunistic)</td><td>Ten funds since 2006</td><td>IX: ~$2.5bn incl. co-invest, Oct 2024 ''' + S('F6') + CF + '''; X: $1bn first close ''' + S('F23') + RP + '''</td></tr>
<tr><td>European Property Partners (Europe, closed-end)</td><td>Alternative real estate in UK and Europe</td><td>III: over €800m, Feb 2022 ''' + S('F26') + RP + '''; IV: €1.5bn target, 2023 ''' + S('F28') + '''</td></tr>
<tr><td>Canada Alternative Real Estate Fund</td><td>Open-end, Canada</td><td>$1.16bn GAV ''' + S('F11') + '''</td></tr>
<tr><td>Infrastructure</td><td>Core infrastructure fund (ex-Social Infrastructure Fund), Basalt mid-market funds, a digital fund</td><td>~$30bn platform ''' + S('F10') + '''; Infrastructure Fund $3.22bn GAV ''' + S('F11') + '''</td></tr>
<tr><td>Credit</td><td>RoundShield (European asset-backed credit), HSAM European Private Debt Fund (evergreen real estate lending)</td><td>RoundShield $5.4bn at purchase ''' + S('F16') + '''</td></tr>
<tr><td>Private wealth</td><td>Interval funds (Real Assets, Real Estate, Infrastructure Income) and an infrastructure ETF launched Feb 2026</td><td>Ex-Versus Capital, Denver ''' + S('F22', 'F37') + RP + '''</td></tr></table>
''')
parts.append(KEY('Interval fund / evergreen fund', 'A fund that stays open and lets investors in and out at set intervals, usually with limits. These are how private assets are sold to wealthier individuals. In Europe the equivalent is the ELTIF (applying in its new form from 10 January 2024) and in the UK the LTAF (rules in force 15 November 2021) ' + S('I65', 'I66') + '. Preqin counted a record 123 evergreen fund launches in 2025 ' + S('I36') + '.'))

# ---------------- PART 6
parts.append(part('p6', 'Part 6. The firm: Harrison Street Asset Management', 'What it is, where it came from, how it is built'))
parts.append(sec('p6a', 'The founding idea'))
parts.append('''<p>Christopher Merrill founded Harrison Street in Chicago in 2005 ''' + S('F2', 'F6') + CF + '''. He had spent his career at Heitman, a Chicago real estate manager, where he launched its first foreign fund and in 1997 "moved to London with the idea of building a business around Central European real estate" ''' + S('F5') + CF + '''. He started Harrison Street as a 50-50 partnership with Christopher Galvin, a former Motorola CEO, and his brother Michael ''' + S('F5') + '''.</p>
<p>His design idea, in his own words: <b>"Let's not necessarily be a macro-investor, but a demand investor."</b> He wanted to be "the first firm that was a pure-play investor around alternative real estate" ''' + S('F4', 'F5') + CF + '''. Instead of betting on offices and shops, which rise and fall with the economy, the firm backs buildings people need whatever the cycle: student beds, care for older people, medical space, storage, and later data centres and infrastructure. The firm's boilerplate calls them "demographic-driven, needs-based assets" ''' + S('F6') + '''.</p>
''')
parts.append(fig(D.d_sectors(), 'Figure 6.1. The demand-driven sectors Harrison Street invests in.', 'sector list [F6], [F29]; demand drivers are plain-English summaries [Inferred].'))
parts.append(sec('p6b', 'From boutique to $110bn'))
parts.append(fig(D.d_timeline(), 'Figure 6.2. Key dates.', '[F2], [F34], [F7], [F3], [F6], [F1], [F16], [F12], [F8].'))
parts.append('''<ul><li><b>2018: Colliers buys control.</b> Colliers International, the listed Canadian property services group, bought 75% for $450m plus a $100m earn-out paid in 2022. Harrison Street then managed about $14.6bn. Colliers' Jay Hennick called it "transformational and the most significant in our history" ''' + S('F2') + CF + '''. Some press says $550m, which includes the earn-out.</li>
<li><b>2022: Colliers buys more managers.</b> Basalt (infrastructure), Rockwood (US real estate) and Versus Capital (wealth products) ''' + S('F3') + CF + '''.</li>
<li><b>23 July 2025: the rebrand.</b> Colliers renamed its whole investment management division Harrison Street Asset Management, with Merrill as Global CEO and over $100bn of AUM ''' + S('F1') + CF + '''.</li>
<li><b>30 July 2025:</b> HSAM bought 60% of RoundShield, a European credit manager with $5.4bn ''' + S('F16') + CF + '''.</li>
<li><b>20 July 2026:</b> Harrison Street Europe was merged into RoundShield and rebranded <b>HSAM Europe</b>, with over $10bn and more than 90 people across seven offices ''' + S('F12') + CF + '''.</li></ul>
''')
parts.append(fig(D.d_aum(), 'Figure 6.3. AUM over time. The 2025 jump is a combination, not organic growth.', 'firm and Colliers figures as labelled; Merrill quote [F5].'))
parts.append('<p>Merrill on the jump: "It wasn\'t really a jump as much as it was a coming together" ' + S('F5') + CF + '. Know this. If you say "they doubled in a year", an interviewer will correct you.</p>')
parts.append(sec('p6c', 'How the group fits together'))
parts.append(fig(D.d_platform(), 'Figure 6.4. HSAM and its platforms.', 'ownership [F3]; platforms [F1], [F12], [F22]; ISG size [F8].'))
parts.append('<p>Colliers holds an 82% economic interest in HSAM; Merrill is the largest individual shareholder ' + S('F3', 'F1') + CF + '. In 2025 Colliers\' investment management segment earned $532m revenue and $215m adjusted EBITDA, a 40% margin ' + S('F3') + CF + '. Being inside a listed group means more public data than at most private managers: Colliers\' annual filings disclose segment results, AUM and fee-paying AUM.</p>')
parts.append(sec('p6d', 'The numbers, and why they disagree'))
parts.append('''<table><tr><th>Metric</th><th>Figure</th><th>As of</th><th>Source</th></tr>
<tr><td>AUM</td><td>$108.2bn ($54.2bn fee-paying; 86% in perpetual or long-dated vehicles)</td><td>31 Dec 2025</td><td>''' + S('F3') + CF + '''</td></tr>
<tr><td>AUM (latest)</td><td>$110bn</td><td>9 Sep 2026</td><td>''' + S('F8') + CF + '''</td></tr>
<tr><td>Staff</td><td>"more than 520" (JD) / "over 600" (2026 releases) / 620 (Colliers segment)</td><td>2025-26</td><td>''' + S('F21', 'F8', 'F3') + '''</td></tr>
<tr><td>Clients</td><td>over 1,100 institutions and over 300 RIAs</td><td>Sep 2026</td><td>''' + S('F8') + CF + '''</td></tr>
<tr><td>ISG headcount</td><td>50 worldwide</td><td>Sep 2026</td><td>''' + S('F8', 'F9') + CF + '''</td></tr>
<tr><td>Capital raised since 2006 (legacy HS)</td><td>$30bn equity; 1,657 assets</td><td>Oct 2024</td><td>''' + S('F6') + CF + '''</td></tr></table>
''')
parts.append(UNC('Staff and client counts differ between releases (520 vs 600+, 1,100 vs 1,200 institutions in May 2026 ' + S('F17') + '). The JD uses year-end-2025 boilerplate. In the interview say "around $110bn and about 600 people since the Colliers businesses came together", and you will be right either way.'))
parts.append(sec('p6e', 'Europe and the Middle East'))
parts.append('''<p>The European platform launched in 2015; the UK company, Harrison Street Real Estate Capital Ltd (Companies House 09665510), was incorporated on 1 July 2015 at 20 St James's Street ''' + S('F7', 'F41') + CF + '''. By 2023 Europe had nearly 50 people in four offices ''' + S('F7') + '''; HSAM Europe now has over 90 ''' + S('F12') + '''. Deals include UK life science (the BioCity purchase that created We Are Pioneer, about £120m, 2021) and a £150m UK self-storage joint venture in 2025 ''' + S('F42', 'F43') + RP + '''.</p>
<p>The Middle East matters directly to your JD ("potential investors in Europe and Middle East"). HSAM opened an office in Abu Dhabi Global Market on 10 June 2025 with a regulatory permission to deal with professional clients, and appointed Hadi Nasser as Head of Investor Relations, Middle East ''' + S('F14') + CF + '''. Merrill has described "substantial appetite among Gulf-based investors for exposure to long-duration, inflation-protected assets" ''' + S('F40') + RP + '''.</p>
''')
parts.append(sec('p6f', 'Anything awkward?'))
parts.append('<p>The SEC adviser database shows no disclosures (no regulatory actions) for the main US adviser or the wealth adviser ' + S('F11', 'F11b') + CF + '. Searches found no enforcement or lawsuits ' + S('F45') + '. That is absence of evidence, not proof. The real talking points are structural: open-end core funds across the industry had redemption queues in 2023-24 (no HS-specific data found), and the merger of several brands is still bedding in.</p>')

# ---------------- PART 7
parts.append(part('p7', 'Part 7. The ISG seat and your job description', 'Every line decoded'))
parts.append(sec('p7a', 'The team, reconstructed'))
parts.append('<p>The firm publishes no org chart. This one is built from firm press releases, public bios and job postings. Names and titles are public professional information only.</p>')
parts.append(fig(D.d_isg_org(), 'Figure 7.1. Investor Solutions Group, reconstructed. Colour shows how sure we are.', '[F8], [F10], [F14], [F18], [F19], [F20b]. Reporting lines below the heads are inferred.'))
parts.append('''<p>Key facts: ISG has 50 people across the US, Europe and Asia ''' + S('F9') + CF + '''. The global co-heads are Geoff Regnery (also Co-President) and Jenna Sheehan, whose bio covers "global investor relations, consultant engagement, and brand strategy" ''' + S('F8', 'F19') + '''. In London, Mina Kojuri is Head of ISG for Europe and sits on the European Executive Committee ''' + S('F18') + CF + '''. Jane Bowes joined in August 2026 as a Managing Director covering infrastructure capital formation ''' + S('F10') + '''. On 9 September 2026 the firm announced five senior ISG appointments ''' + S('F8') + '''. The team was called "Investor Relations" until about 2025 ''' + S('F33') + IN + '''.</p>''')
parts.append(OP('A firm that just merged six brands and then hires five senior IR people in one month is telling you its next priority is selling the combined shelf. Think about what that means for an intern: lots of new materials, new mapping, and a CRM that needs cleaning after a merger. [Inferred]'))
parts.append(sec('p7b', 'The JD, line by line'))
jd = [
 ('Support creating presentations for current clients, consultants and prospective investors.', 'Updating pitch books and client review decks: refreshing performance pages each quarter, building charts, checking every number against the source, matching brand format.', 'Three audiences, three decks. Consultants want process and risk; clients want their portfolio; prospects want the story.'),
 ('Help craft responses to ad-hoc client requests for information and investment analysis.', 'Drafting answers to emailed questions and DDQ sections, pulling data from finance and portfolio teams.', 'Every figure needs a source and compliance check. Speed matters but accuracy wins.'),
 ('Contribute to other marketing and communications related projects.', 'Press releases, website content, thought-leadership pieces, newsletters.', 'ISG and Marketing work closely ' + S('F20b') + '.'),
 ('Help maintain our CRM system Salesforce up to date.', 'Logging meetings, updating contacts and investor status, tagging which funds each investor saw.', 'After a six-brand merger, a clean CRM is a real asset. GDPR applies to personal data in it. [Inferred]'),
 ('Leveraging AI to monitor industry trends, competitor fundraising activity, and LP allocation patterns.', 'Using AI tools to summarise news, fund closes and pension board minutes into a regular digest.', 'Vendor surveys say nearly 80% of managers at least pilot AI ' + S('I45') + ' (directional). Check every AI output against the source.'),
 ('Support senior team members with ad hoc fundraising related tasks.', 'Meeting prep packs, investor briefing notes, follow-up tracking.', 'You are the person who makes seniors look prepared.'),
 ('Help map and conduct research on potential investors in Europe and Middle East.', 'Building target lists: who, how much in real estate, which strategies, who decides, consultant used.', 'Ties to the Abu Dhabi office ' + S('F14') + ' and LGPS / Dutch changes ' + S('I22', 'I40') + '.'),
 ('Support managing the team\'s attendance to conference, industry events and sponsorship applications.', 'Registration, meeting schedules, sponsorship forms, follow-up lists.', 'Events are where many first meetings happen.'),
 ('Ensure that all client needs are consistently met and strive to exceed client expectations.', 'Tracking every open request to closure on time.', 'The retain half of the job, in one line.')]
rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in jd)
parts.append('<table><tr><th style="width:30%">JD line</th><th>What it means day to day [Inferred]</th><th style="width:32%">Why it matters</th></tr>' + rows + '</table>')
parts.append(UNC('The JD asks for graduation "in Summer 2026 or recently graduated" for a Summer 2027 internship ' + S('F21') + '. This looks like an unedited line from last year\'s ad. If it affects you, ask the recruiter politely rather than assume.'))
parts.append(sec('p7c', 'A plausible day in the seat'))
parts.append(fig(D.d_day(), 'Figure 7.2. An illustrative day for a London ISG intern.', 'built from the JD; not a firm description. [Inferred]'))

# ---------------- PART 8
parts.append(part('p8', 'Part 8. The rules: why nothing goes out without sign-off', 'Marketing regulation an IR intern should know exists'))
parts.append('<p>Selling a private fund is regulated marketing. You will not need to be an expert, but knowing why compliance reviews every slide will impress any interviewer.</p>')
parts.append(fig(D.d_regs(), 'Figure 8.1. Regulation timeline for fund marketing in the UK and EU.', 'dates as cited on the figure.'))
parts.append('''<table><tr><th style="width:24%">Rule</th><th>What it does</th><th style="width:30%">What it means for ISG</th></tr>
<tr><td>AIFMD (EU) and AIFMD II, Directive (EU) 2024/927</td><td>The EU rulebook for alternative fund managers. AIFMD II was published 26 March 2024, in force 15 April 2024, and applied from 16 April 2026, with some reporting from 16 April 2027 ''' + S('I8', 'I10') + '''</td><td>Sets how funds can be marketed across EU countries.</td></tr>
<tr><td>EU pre-marketing rules (Directive (EU) 2019/1160)</td><td>From 2 August 2021, defines pre-marketing; any subscription within 18 months counts as marketing ''' + S('I14') + '''</td><td>Even early "testing the water" calls are logged.</td></tr>
<tr><td>UK National Private Placement Regime (NPPR)</td><td>How non-UK funds are marketed in the UK: notify the FCA, then market ''' + S('I28') + CF + '''</td><td>Which funds can be shown to which UK investors.</td></tr>
<tr><td>UK AIFM reform, FCA CP26/28</td><td>Published 14 July 2026; consultation closes 14 October 2026; new regime intended for 2028; NPPR kept with limited changes ''' + S('I6') + '''</td><td>A live topic: ask about it.</td></tr>
<tr><td>s21 and s238 FSMA 2000</td><td>Financial promotions must be made or approved by an authorised firm; promotion of unregulated funds is restricted to exempt audiences ''' + S('I48', 'I49') + '''</td><td>Decks go only to professional investors; wording is checked.</td></tr>
<tr><td>FCA anti-greenwashing rule (ESG 4.3.1R)</td><td>From 31 May 2024, sustainability claims must be fair, clear and not misleading ''' + S('I13') + '''</td><td>No loose "green" or "impact" claims in materials.</td></tr>
<tr><td>SFDR and SFDR 2.0 (EU)</td><td>Sustainability disclosure. The 20 Nov 2025 proposal would replace Article 8/9 labels with three categories; not yet law, about 2028 ''' + S('I11') + '''</td><td>Investors ask how a fund is classified.</td></tr></table>
''')
parts.append(DONT('"I\'d just send the deck to anyone interested." Or using AI to write numbers you cannot trace. Both break rules in this table.'))
parts.append(SAY('"Because these are private funds, every piece of material is regulated marketing. So I\'d expect anything I draft to go through compliance, and I\'d always keep the source of every number."'))

# ---------------- PART 9
parts.append(part('p9', 'Part 9. The market right now', 'What the people interviewing you are living through'))
parts.append(fig(D.d_fundraising_chart(), 'Figure 9.1. Real estate fundraising fell for three years, then rose in 2025.', '[I1], [I34].'))
parts.append('''<ul><li><b>Fundraising is slower.</b> Funds that closed in 2025 took 25 months on average, a record. Only 52% hit their target, though that was up from 40% in 2024 ''' + S('I1') + CF + '''.</li>
<li><b>Money concentrates in the biggest names.</b> Blackstone and Brookfield took 16% of 2025's total ''' + S('I1') + '''. Mid-sized specialists must differentiate.</li>
<li><b>Alternatives are winning share.</b> Data centres took 37% of sector-specific capital in 2025, up from 2% ''' + S('I1') + '''. That is Harrison Street's home turf: Merrill says the firm has $7-8bn in data centres ''' + S('F4') + RP + '''.</li>
<li><b>Europe has a backlog.</b> Europe-focused funds raised $40.6bn in 2025, with $90.4bn still in market at 1 January 2026 ''' + S('I1') + '''. A London ISG team competes for that capital.</li>
<li><b>2026 is mixed.</b> Colliers reported US real estate fundraising of $92.6bn in H1 2026, down 38% ''' + S('I60') + RP + '''.</li>
<li><b>Wealth is the new channel.</b> Blackstone raised $43bn from private wealth in 2025 ''' + S('I37') + RP + '''. HSAM's Versus purchase and its interval funds and ETF are its route in ''' + S('F22', 'F37') + '''.</li>
<li><b>The denominator effect</b> is fading. When public markets fell in 2022, private assets became too large a share of portfolios and investors paused new commitments ''' + S('I67') + '''.</li></ul>
''')
parts.append(OP('Is a one-stop shop (real estate, infrastructure, credit, wealth) the right answer to a slow, concentrated fundraising market, or will investors still prefer pure specialists? Harrison Street began as the specialist and is now becoming the platform. Pick a side and be ready to defend it.'))

# ---------------- PART 10
parts.append(part('p10', 'Part 10. Ten questions you can now answer', 'Scaffolds, not scripts'))
qs = [('What is real estate investor relations?', 'Raise + retain. Client = investor. Sell a fund, not a building. Good service drives re-ups (Fund IX ~60% from existing LPs ' + S('F6') + ').'),
 ('Who are Harrison Street\'s clients?', 'Pensions, Taft-Hartley, SWFs, insurers, endowments ' + S('F6') + '; 1,100+ institutions, 300+ RIAs ' + S('F8') + '; consultants as gatekeepers.'),
 ('Why Harrison Street?', 'Demand, not macro ' + S('F5') + '. 20-year alternatives specialist now with infra, credit and wealth under one brand ' + S('F1') + '. London ISG growing, Middle East office ' + S('F14') + '. Name a sector you care about.'),
 ('How is this different from working at an agency like CBRE?', 'Deal-level vs fund-level; one-off fees vs recurring fees ' + S('I52') + '. Agents sell buildings; ISG sells a team.'),
 ('What is the difference between open-end and closed-end?', 'Core Property Fund vs Real Estate Partners. Continuous vs episodic fundraising.'),
 ('What is happening in fundraising?', '$172bn in 2024, $222bn in 2025, 25 months on road ' + S('I1') + '. Alternatives and data centres up.'),
 ('A consultant asks for a number tomorrow and finance has not replied. What do you do?', 'Tell your senior early, chase with a clear deadline, never estimate a number, keep a record. Accuracy over speed.'),
 ('How would you use AI in this role?', 'Monitor news and fund closes, summarise pension minutes; verify every output; never put confidential client data into unapproved tools.'),
 ('What do you know about European investors?', 'LGPS pooling to six pools ' + S('I22') + '; Dutch Wtp transition ' + S('I40') + '; European allocations near target ' + S('I15') + '.'),
 ('What would you want to learn here?', 'How a consultant decides to rate a fund; how the combined shelf is sold to one client.')]
parts.append('<table><tr><th style="width:36%">Question</th><th>Points to hit</th></tr>' + ''.join(f'<tr><td><b>{q}</b></td><td>{a}</td></tr>' for q, a in qs) + '</table>')
parts.append('<h4>Three questions to ask them</h4><ol><li>"Since HSAM Europe was formed in July, how has the London ISG changed the way it presents the combined equity and credit offer to European investors?"</li><li>"With the Abu Dhabi office now open, how does the London team split coverage of Gulf investors with the Middle East team?"</li><li>"How are you using AI tools for LP mapping today, and what would a great intern project in that area look like?"</li></ol>')

# ---------------- GLOSSARY
parts.append(part('p11', 'Part 11. Glossary', 'Every term in plain English'))
gl = [('AGM', 'Annual general meeting: the yearly meeting a manager holds for its fund investors.'), ('AIF / AIFM', 'Alternative investment fund / its manager. Covers most private real estate funds in the EU and UK.'),
 ('AIFMD II', 'Directive (EU) 2024/927, the update to the EU fund manager rulebook; applied from 16 April 2026.'), ('Asset management', 'Running individual buildings to a business plan (leasing, capex, sales).'),
 ('AUM', 'Assets under management.'), ('Basis point (bp)', 'One hundredth of one percent. 90 bp = 0.9%.'), ('Build-to-rent (BTR)', 'Homes built to be rented, owned by one landlord.'),
 ('Capital call', 'A request to an investor to send part of its committed money.'), ('Capital account statement', 'A report showing an investor what it has paid in, received and still owns.'),
 ('Carried interest (carry)', 'The manager\'s share of profits above the hurdle, often around 20% (dated general figure).'), ('Closed-end fund', 'A fund with a fixed raise and a fixed life.'),
 ('Co-investment', 'An investor putting extra money directly into one deal alongside the fund.'), ('Commitment', 'The amount an investor promises to a fund.'),
 ('Consultant', 'A firm that advises pensions on which managers to hire (e.g. Mercer).'), ('Core / core-plus', 'Lowest-risk real estate: stable, income-producing, low debt.'),
 ('CRM', 'Customer relationship management system; at HS, Salesforce.'), ('Data room', 'A secure website holding fund documents for investors in diligence.'),
 ('DDQ', 'Due diligence questionnaire: a long standard question list investors send managers.'), ('Denominator effect', 'When falls in public markets make private holdings too big a share, so investors pause new commitments.'),
 ('Distribution', 'Cash a fund pays back to investors.'), ('Dry powder', 'Money committed but not yet invested.'), ('ELTIF', 'European long-term investment fund, a wrapper for selling private assets more widely.'),
 ('Endowment', 'A university or charity\'s permanent investment pot.'), ('ESG', 'Environmental, social and governance factors.'), ('Evergreen fund', 'A fund with no end date.'),
 ('Fee-paying AUM', 'The part of AUM that earns fees.'), ('Final close', 'The last date investors can join a closed-end fund.'), ('First close', 'The first legal commitment of investors to a fund.'),
 ('FCA', 'Financial Conduct Authority, the UK markets regulator.'), ('Financial promotion', 'Any invitation to invest. Regulated under s21 FSMA.'),
 ('GAV', 'Gross asset value: the total value of a fund\'s assets before debt.'), ('GP', 'General partner: the manager of the fund.'),
 ('GRESB', 'A global ESG benchmark for real estate funds.'), ('Hard cap', 'The maximum a fund will accept.'), ('Hurdle / preferred return', 'The minimum return investors get before the manager earns carry.'),
 ('ILPA', 'Institutional Limited Partners Association, which publishes reporting templates.'), ('INREV', 'European association for investors in non-listed real estate; sets reporting and DDQ standards.'),
 ('Interval fund', 'A US fund that lets investors redeem at set intervals; used for wealth clients.'), ('IRR', 'Internal rate of return: annualised return taking timing of cash flows into account.'),
 ('J-curve', 'The early dip in a closed-end fund\'s returns while money goes in and fees are paid before profits arrive.'), ('LGPS', 'Local Government Pension Scheme, the UK council workers\' pension.'),
 ('Life sciences real estate', 'Labs and science parks for research companies.'), ('LP', 'Limited partner: an investor in a fund.'), ('LPA', 'Limited partnership agreement: the fund\'s legal rulebook.'),
 ('LPAC', 'LP advisory committee: a small group of investors consulted on conflicts and valuations.'), ('LTAF', 'Long-term asset fund, the UK wrapper for private assets.'),
 ('LTV', 'Loan-to-value: debt divided by property value.'), ('Management fee', 'The annual fee a manager charges for running a fund.'), ('NAV', 'Net asset value: assets minus debts.'),
 ('NPPR', 'National Private Placement Regime: the UK route for marketing non-UK funds.'), ('Open-end fund', 'A fund investors can join and leave over time.'),
 ('Opportunistic', 'Highest-risk real estate: development, heavy debt, turnarounds.'), ('PBSA', 'Purpose-built student accommodation.'),
 ('Placement agent', 'A firm hired by a manager to help raise money.'), ('PPM', 'Private placement memorandum: the fund\'s offering document.'),
 ('Pre-marketing', 'Testing investor interest before a fund is formally offered; regulated in the EU since 2021.'), ('RFP', 'Request for proposal: a formal tender from an investor.'),
 ('RIA', 'Registered investment adviser (US): manages money for individuals.'), ('Re-up', 'An existing investor committing to the next fund in a series.'),
 ('REIT', 'Real estate investment trust: a listed property company.'), ('Senior housing', 'Homes and care for older people, from independent living to memory care.'),
 ('SFDR', 'EU Sustainable Finance Disclosure Regulation.'), ('Side letter', 'A private agreement giving one investor special terms.'), ('Sovereign wealth fund', 'A state-owned investment fund.'),
 ('Taft-Hartley plan', 'A US union-run pension plan.'), ('Value-add', 'Middle-risk real estate: buy, improve, re-let.')]
parts.append('<table><tr><th style="width:25%">Term</th><th>Meaning</th></tr>' + ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a, b in gl) + '</table>')

# ---------------- SOURCES
parts.append(part('p12', 'Part 12. Sources', 'F = firm research, I = industry research. All accessed 2026-10-08.'))
rows = []
for line in open(SP + 'ws_firm.md', encoding='utf-8'):
    if line.startswith('[F'):
        c = [x.strip() for x in line.split('|')]
        rows.append((c[0], c[1], c[2], c[3], c[4], c[6]))
for line in open(SP + 'ws_industry.md', encoding='utf-8'):
    if line.startswith('| [I'):
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        rows.append((c[0], c[1], c[2], c[3], c[4], c[6]))
esc = lambda s: s.replace('—', 'n/a').replace('&', '&amp;').replace('<', '&lt;')
parts.append('<table class="src"><tr><th>ID</th><th>Outlet</th><th>Title</th><th>Date</th><th>URL</th><th>Status</th></tr>' +
             ''.join(f'<tr><td>{esc(a)}</td><td>{esc(b)}</td><td>{esc(c)}</td><td>{esc(d)}</td><td>{esc(e)}</td><td>{esc(f)}</td></tr>' for a, b, c, d, e, f in rows) + '</table>')
parts.append('<p class="small">FETCHED = full page read. SNIPPET = known from search summary only, treat as Reported. PAYWALLED = headline or teaser only.</p>')

# ---------------- GAPS
parts.append(part('p13', 'Part 13. What we could not find', 'Honest gaps'))
parts.append('''<ul><li>Final closes for Real Estate Partners X and European Property Partners IV.</li>
<li>Harrison Street's fee terms on any fund.</li>
<li>Whether any Harrison Street entity holds its own FCA authorisation (the UK company is described in the SEC filing as a branch office employing staff for the US adviser ''' + S('F11') + ''').</li>
<li>The exact date "Investor Relations" became "Investor Solutions Group".</li>
<li>Recent (2025-26) named pension commitments to Harrison Street funds; the named ones in public minutes are from 2013 to 2022.</li>
<li>Redemption queue data for the Core Property Fund.</li>
<li>The interviewers, interview date and format: not supplied. A full interview pack (question bank, scenario playbook, interviewer briefing) can be built once those are known.</li>
<li>Primary text of AIFMD II on EUR-Lex did not load; dates rest on a law firm summary plus consistent secondary sources.</li></ul>
''')

# ---------------- ASSEMBLE
tochtml = '<h2 style="font-size:20pt;margin-bottom:10px">Contents</h2><div class="toc">' + ''.join(
    f'<div class="{"" if top else "sub"}"><span class="t"><a href="#{i}">{t}</a></span><span class="pg" data-for="{i}"></span></div>' for i, t, top in toc) + '</div>'
cover = '''<div class="cover"><div class="k">INTERVIEW EXPLAINER</div><h1>Real Estate Investor Relations, explained</h1>
<div class="sub">What the job is, who the client is, how it differs from every job near it, and the firm you would do it for: Harrison Street Asset Management, Investor Solutions Group, London.</div>
<div class="sub" style="font-size:10.5pt;margin-top:30px">For: Summer 2027 Investor Solutions Group Intern, London</div>
<div class="meta">Built 8 October 2026 from public sources only. Every non-obvious fact carries a source marker like [F8] that resolves in Part 12.
Confidence tags: <b style="color:#9fe0b3">Confirmed</b> primary source or two outlets; <b style="color:#ffd27a">Reported</b> one source or snippet; <b style="color:#c3cbf0">Inferred</b> author reasoning.</div></div>'''
body = ''.join(parts)
body = re.sub(r'<table([^>]*)><tr>(<th.*?</tr>)', r'<table\1><thead><tr>\2</thead>', body)
html = f'''<!doctype html><html><head><meta charset="utf-8"><title>Real Estate IR Explained</title><style>{open(SP+'style.css').read()}</style></head>
<body>{cover}{tochtml}{body}</body></html>'''
open(OUT + 'Real_Estate_Investor_Relations_Explained.html', 'w', encoding='utf-8').write(html)
print('ok', len(html), 'diagrams', html.count('<svg'))
