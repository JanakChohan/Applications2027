from svg import *
S1="#2f6fb2"; S2="#c9932a"; INK="#1c2330"; INK2="#52514e"; SIG="#7a3e9d"; LGREEN="#dff1e6"; LRED="#f9ecec"; LGOLD="#fff8e8"

def src(d, x, y, text, anchor="start"):
    d.text(x, y, text, size=7.4, fill=INK2, anchor=anchor, italic=True, maxw=d.w-x-10, lh=1.3)

def money_flow():
    d=D(780,640)
    d.text(390,22,"WHERE THE MONEY COMES FROM AND WHERE IT GOES, FY2025 (managed basis, $bn)",size=11,fill=NAVY,weight="bold")
    # customers column
    d.region(10,40,180,330,"WHO PAYS",fill=LBLUE,dash=False)
    custs=[("Consumers & small businesses","deposits, card spend, mortgages, auto"),("Companies, governments, institutions","advice, capital raising, trading, payments, custody"),("Wealthy families & institutions","fees on assets, deposits, loans, alternatives")]
    for i,(t,b) in enumerate(custs):
        d.box(20,70+i*95,160,80,t,b,fill=WHITE,tfill=NAVY,stroke=LINE,tsize=9,bsize=7.6)
    # segments
    d.region(215,40,200,330,"OPERATING UNITS (revenue / net income)",fill=BG,dash=False)
    segs=[("CCB (Chase)","$76.0 / $18.2"),("CIB","$78.5 / $27.8"),("AWM","$24.1 / $6.5"),("Corporate","$7.0 / $4.5")]
    for i,(t,b) in enumerate(segs):
        fill= GOLD if t=="AWM" else NAVY2
        d.box(225,70+i*72,180,58,t,b,fill=fill,tsize=10,bsize=9)
    d.arrow(180,110,225,99,color=GREY); d.arrow(180,205,225,171,color=GREY); d.arrow(180,300,225,243,color=GREY)
    # revenue types
    d.region(440,40,150,330,"REVENUE TYPE",fill=BG,dash=False)
    d.box(450,70,130,110,"Net interest income","$95.4 (51%)\nspread between what the bank earns on loans and securities and pays on deposits",fill=NAVY,tsize=9,bsize=7.4)
    d.box(450,195,130,150,"Noninterest revenue","$90.1 (49%)\nfees: investment banking, asset management, card, payments; plus trading (principal transactions)",fill=NAVY,tsize=9,bsize=7.4)
    for y in (99,171,243,315): d.arrow(405,y,450,y if y<200 else 270,color=GREY,width=1)
    # total
    d.box(615,40,155,60,"TOTAL REVENUE","$185.6",fill=GOLD,tsize=10,bsize=12)
    d.arrow(580,125,615,80,color=GOLD,marker="arrg"); d.arrow(580,270,615,90,color=GOLD,marker="arrg")
    # costs
    d.box(615,120,155,54,"Expenses","$95.6 (people ~half; technology ~$18)",fill=WHITE,tfill=RED,stroke=RED,tsize=9,bsize=7.6)
    d.box(615,184,155,44,"Credit costs","$11.5 (loan losses and reserves)",fill=WHITE,tfill=RED,stroke=RED,tsize=9,bsize=7.6)
    d.box(615,238,155,44,"Tax","$21.5",fill=WHITE,tfill=RED,stroke=RED,tsize=9,bsize=7.6)
    d.box(615,296,155,60,"NET INCOME","$57.0",fill=NAVY,tsize=10,bsize=12)
    for y in (100,): d.arrow(692,y,692,120,color=GREY)
    d.arrow(692,174,692,184,color=GREY); d.arrow(692,228,692,238,color=GREY); d.arrow(692,282,692,296,color=GREY)
    # bottom: capital
    d.region(10,390,760,150,"WHAT HAPPENS TO THE PROFIT",fill=BG,dash=False)
    d.box(30,420,220,100,"Returned to shareholders","~$46 in 2025: dividends ~$17 and net buybacks ~$29",fill=NAVY2,tsize=9.5,bsize=8)
    d.box(280,420,220,100,"Retained as capital","builds the fortress: CET1 $288bn (14.5%); ~$40bn 'excess' earning ~4% after tax",fill=NAVY2,tsize=9.5,bsize=8)
    d.box(530,420,220,100,"Reinvested in growth","branches (+500 planned), bankers and advisors (PB advisors 2,500 to 4,101 in five years), technology (~$20bn in 2026)",fill=GOLD,tsize=9.5,bsize=8)
    d.arrow(692,356,692,390,color=NAVY,marker="arrn",width=2)
    src(d,10,565,"Sources: JPMorgan Chase FY2025 Form 10-K [S300]; 4Q25 earnings release [S304]; Dimon 2025 letter [S311]. Credit costs = provision for credit losses; tax = income tax expense. Rounded.")
    src(d,10,580,"AWM detail: asset management fees $15.5, commissions $1.2, NII $6.8, other $0.6 = $24.1; expense $15.3; pretax $8.6; net income $6.5 [S300].")
    src(d,10,595,"Buyback and dividend split is approximate from the 10-K capital actions; 'excess capital' per Dimon 2025 letter [S311].")
    return d.svg()

def operating_layers():
    d=D(780,420)
    d.region(10,10,760,110,"CUSTOMERS AND CAPITAL",fill=LBLUE,dash=False)
    for i,(t,b) in enumerate([("94m US consumers and small businesses","Chase"),("80,000 companies and institutions","CIB"),("Wealthy families, family offices, institutions","AWM: $7.1tn client assets"),("Shareholders and depositors","$362bn equity; $2.6tn deposits")]):
        d.box(20+i*188,38,178,70,t,b,fill=WHITE,tfill=NAVY,stroke=LINE,tsize=8.6,bsize=7.6)
    d.region(10,140,760,110,"FRONT LINE (people who face customers)",fill=BG,dash=False)
    for i,(t,b) in enumerate([("Branch bankers and Chase advisors","5,083 branches; 6,049 advisors"),("Investment, corporate and commercial bankers; traders; payments sales","~4,000 senior bankers, 220 cities"),("Private Bank advisors, investors, capital and wealth advisors","4,101 PB advisors"),("Asset Management client-facing staff","842")]):
        d.box(20+i*188,168,178,70,t,b,fill=NAVY2,tsize=8.6,bsize=7.6)
    d.region(10,270,760,110,"THE CENTRE (shared platforms and control)",fill=BG,dash=False)
    for i,(t,b) in enumerate([("Technology and data","~$20bn a year; 60,000 technologists; LLM Suite; SpectrumIQ; Connect Coach"),("Risk, compliance, legal, audit","three lines of defence; CRO reports to the CEO and board"),("Treasury and CIO","funding, liquidity, capital; $1.5tn cash and securities"),("Operations and corporate centres","~80,000 in operations and call centres; India and Philippines hubs")]):
        d.box(20+i*188,298,178,70,t,b,fill=WHITE,tfill=NAVY,stroke=LINE,tsize=8.6,bsize=7.4)
    for x in (109,297,485,673):
        d.arrow(x,108,x,140,color=GOLD,marker="arrg",width=1.6); d.arrow(x,238,x,270,color=GREY,width=1.4)
    d.text(390,400,"What flows down: money, trust, referrals. What flows up: advice, credit, execution, service. The centre supplies the front line with platforms, limits and control.",size=8.6,fill=INK2,italic=True)
    src(d,10,414,"Sources: FY2025 10-K [S300]; Investor Day 2025 decks [S320][S321]; Company Update Feb 2026 [S322].")
    return d.svg()

def team_vs_alternative():
    d=D(780,360)
    d.region(10,10,375,320,"MODEL A: THE INTEGRATED TEAM (J.P. Morgan Private Bank)",fill=LGOLD,dash=False)
    d.circle(197,150,34,fill=GOLD); d.text(197,147,"Client",size=10,fill="#fff",weight="bold"); d.text(197,160,"one relationship",size=7.4,fill="#fff")
    for (t,x,y) in [("Advisor",197,60),("Investor",80,150),("Capital Advisor",314,150),("Wealth Advisor",110,250),("Client Service",290,250)]:
        d.box(x-50,y-18,100,36,t,None,fill=NAVY2,tsize=8.6)
        dx,dy=197-x,150-y; L=(dx*dx+dy*dy)**0.5
        d.arrow(x+dx/L*40,y+dy/L*18,197-dx/L*40,150-dy/L*40,color=GREY,width=1.2)
    d.text(197,300,"Banker paid on team results and salary plus bonus; specialists shared across clients;",size=7.8,fill=INK2)
    d.text(197,312,"the firm, not the banker, owns the client. Erdoes: 'my client... It's our client.'",size=7.8,fill=INK2)
    d.region(395,10,375,320,"MODEL B: THE LONE BANKER OR WIREHOUSE GRID (many rivals)",fill=BG,dash=False)
    d.circle(582,150,34,fill=GREY); d.text(582,147,"Client",size=10,fill="#fff",weight="bold"); d.text(582,160,"belongs to the adviser",size=7.4,fill="#fff")
    d.box(532,42,100,36,"Adviser / RM",None,fill=NAVY2,tsize=8.6)
    d.arrow(582,78,582,112,color=GREY,width=1.2)
    for (t,x) in [("Product desk",450),("Product desk",582),("Product desk",714)]:
        d.box(x-48,232,96,34,t,None,fill=WHITE,tfill=NAVY,stroke=LINE,tsize=8.4,tweight="normal")
        d.arrow(582,184,x,232,color=GREY,width=1,dash=True)
    d.text(582,300,"Adviser paid a grid percentage of revenue; moves firms with the book;",size=7.8,fill=INK2)
    d.text(582,312,"specialists are order-takers; the client follows the person, not the platform.",size=7.8,fill=INK2)
    src(d,10,348,"Sources: Garnica on the five-role team [S28]; JPM UK Client Advisor posting [S13]; Erdoes Investor Day 2022 on 'not the brokerage business model' [S317]. Model B is the author's stylisation of the US wirehouse grid model.")
    return d.svg()

def unit_anatomy():
    d=D(780,400)
    d.region(10,10,420,300,"ONE UK BANKER TEAM (typical, reconstructed)",fill=LGOLD,dash=False)
    rows=[("Team lead: Managing Director or Executive Director banker","carries the largest relationships; 'plays and manages'",40),
          ("Vice President banker(s)","own mid-sized relationships; prospect",100),
          ("Associate(s)","proposals, pitches, client analysis; chosen Banker or Investor track",160),
          ("Analyst(s) and summer interns","research, prospect lists, meeting prep, CRM, KYC packs",220)]
    for t,b,y in rows:
        d.box(20,y,400,50,t,b,fill=NAVY2 if y==40 else WHITE,tfill=WHITE if y==40 else NAVY,stroke=LINE,tsize=8.8,bsize=7.6)
        if y>40: d.arrow(220,y-10,220,y,color=GREY,width=1)
    d.text(220,292,"Shared with other teams in the market group: Investor, Capital Advisor, Wealth Advisor, Client Service Associates",size=7.8,fill=INK2,italic=True)
    d.region(450,10,320,300,"WHAT THE TEAM DRAWS FROM THE CENTRE",fill=BG,dash=False)
    items=["Global Investment Strategy: house view, Outlook, Eye on the Market","Manager selection and Alternatives platform (850+ external managers)","Credit underwriting and the balance sheet","Trust company; wealth planning specialists","KYC and onboarding operations; compliance","Connect Coach (AI next-best-action); CRM; reporting","Events, marketing, thought leadership","Referral flow from CIB, Chase and Asset Management"]
    for i,it in enumerate(items):
        d.box(460,38+i*33,300,28,it,None,fill=WHITE,tfill=INK,stroke=LINE,tsize=7.8,tweight="normal")
        d.arrow(460,52+i*33,432,52+i*33,color=GOLD,marker="arrg",width=1.1)
    src(d,10,335,"Reconstruction. Team shape from JPM postings for Client Advisor (ED), Client Advisor Support Associate and Analyst roles [S13][S14][S17] and forum accounts of the analyst-to-associate track [S357] (anecdote).")
    src(d,10,349,"Centre functions from the EMEA services pages [S3][S4][S5], Euromoney alternatives write-up [S25], Erdoes 2025 letter on Connect Coach [S316]. Headcount per team not published.")
    return d.svg()

def boundaries():
    d=D(780,330)
    d.box(30,40,200,90,"GLOBAL PRIVATE BANK","serves the family",fill=GOLD)
    d.box(550,40,200,90,"INVESTMENT BANK / MARKETS","serves the company",fill=NAVY2)
    d.box(290,150,200,70,"ASSET MANAGEMENT","manufactures products",fill=NAVY2)
    d.region(240,20,300,120,"",fill=LGREEN,dash=False)
    d.text(390,42,"CROSSES THE LINE (shared)",size=8.6,fill=GREEN,weight="bold")
    for i,t in enumerate(["Referrals both ways (no internal pricing)","Research and the house view","The balance sheet and execution desks","Stadium, sports and founder financing done jointly"]):
        d.text(390,60+i*15,t,size=8,fill=INK)
    d.region(240,235,300,80,"",fill=LRED,dash=False)
    d.text(390,255,"NEVER CROSSES (walled)",size=8.6,fill=RED,weight="bold")
    for i,t in enumerate(["Material non-public information about a deal or issuer","A private client's confidential affairs","Trading positions and flows"]):
        d.text(390,273+i*14,t,size=8,fill=INK)
    d.arrow(230,85,290,85,color=GREEN,width=1.6); d.arrow(550,85,490,85,color=GREEN,width=1.6)
    d.line(390,140,390,235,color=RED,width=2,dash=True)
    d.text(392,200,"information barrier",size=7.6,fill=RED,anchor="start",italic=True)
    src(d,10,325,"Sources: Erdoes on referrals and 'no side accounting groups' [S320]; firmwide conduct and information-barrier framework per 10-K risk management [S300]. Specific wall procedures are not public; the categories are standard bank practice [Inferred].")
    return d.svg()

def spectrum(peers):
    """peers: dict axis_label -> list of (name, position 0..1). Draw 4 axes."""
    d=D(780,60+len(peers)*70)
    y=30
    for (left,right),items in peers.items():
        d.text(20,y+6,left,size=8.6,fill=NAVY,anchor="start",weight="bold"); d.text(760,y+6,right,size=8.6,fill=NAVY,anchor="end",weight="bold")
        d.line(20,y+22,760,y+22,color=LINE,width=2)
        for name,pos in items:
            x=20+740*pos
            col = GOLD if name.startswith("JPM") else NAVY2
            d.circle(x,y+22,5,fill=col)
            d.text(x,y+40,name,size=7.4,fill=INK)
        y+=70
    src(d,10,y-10,"Positions are the author's judgement [Inferred] from the peer table in Part 4 and each firm's own description of its model. Gold = J.P. Morgan.")
    return d.svg()

def size_vs_staff(points):
    """points: list of (name, client_assets_tn, advisors_k)"""
    d=D(760,340); L,T,W,H=70,30,640,240
    xmax=max(p[1] for p in points)*1.15; ymax=max(p[2] for p in points)*1.2
    for i in range(5):
        x=L+W*i/4; y=T+H-H*i/4
        d.line(x,T,x,T+H,color=GRID if False else "#e3e6eb",width=1); d.line(L,y,L+W,y,color="#e3e6eb",width=1)
        d.text(x,T+H+12,f"{xmax*i/4:.1f}",size=7.6,fill=INK2); d.text(L-6,y+3,f"{ymax*i/4:.0f}k",size=7.6,fill=INK2,anchor="end")
    d.text(L+W/2,T+H+26,"Client assets or invested assets ($tn)",size=8.4,fill=INK2)
    for name,a,s in points:
        x=L+W*a/xmax; y=T+H-H*s/ymax
        col=GOLD if name.startswith("J.P.") else S1
        d.circle(x,y,6,fill=col,stroke="#fff"); d.text(x+9,y+3,name,size=7.8,fill=INK,anchor="start")
    d.text(18,T+H/2,"Advisors (thousands)",size=8.4,fill=INK2)
    d.parts[-1]=d.parts[-1].replace('<text ','<text transform="rotate(-90 18 %d)" '%(T+H/2))
    src(d,10,330,"Sources: firm FY2025 reports [S150]-[S161][S300][S316]; Morgan Stanley and UBS adviser counts are press estimates. Definitions of 'client assets' differ; directional only.")
    return d.svg()

def customer_view():
    d=D(780,300)
    items=[("22 consecutive years","of positive net client asset flows (2004 to 2025)","[S316]"),("$1.04tn","of net new client assets in 2024 and 2025 combined","[S316]"),("83%","of 10-year active fund assets above the peer median (2025)","[S316]"),("40% ROE, 36% margin","AWM 2025 versus a peer range of 12 to 28% ROE cited for 2024","[S315][S300]"),(">95%","of Private Bank clients retained in a year (Investor Day 2023)","[S318]"),("1bp","ten-year average net charge-off rate on Private Bank loans","[S319]")]
    for i,(v,l,s) in enumerate(items):
        x=15+(i%3)*255; y=20+(i//3)*120
        d.box(x,y,240,100,v,l+"  "+s,fill=NAVY if i%2==0 else NAVY2,tsize=13,bsize=8)
    src(d,10,270,"What a client is buying: durability and consistency rather than the highest return in any one year. The counter-case (fees, house product, size) is in Part 8.")
    return d.svg()

def stability_timeline():
    yrs=list(range(2012,2026)); flows=[None]*6+[None,None,None,389,49,490,486,553]
    # only 2021-2025 known reliably; show client assets 2021-2025 and flows
    d=D(780,260); L,T,W,H=60,30,690,160
    ca={2021:4.3,2022:4.0,2023:5.0,2024:5.9,2025:7.1}; fl={2021:389,2022:49,2023:490,2024:486,2025:553}
    xs=[2021,2022,2023,2024,2025]
    for i in range(5):
        y=T+H-H*i/4; d.line(L,y,L+W,y,color="#e3e6eb",width=1); d.text(L-6,y+3,f"{i*2}",size=7.6,fill=INK2,anchor="end")
    for i,yr in enumerate(xs):
        x=L+40+i*150; h=H*ca[yr]/8
        d.parts.append(f'<rect x="{x}" y="{T+H-h}" width="60" height="{h}" rx="3" fill="{S1}"/>')
        d.text(x+30,T+H-h-5,f"${ca[yr]}tn",size=8,fill=INK)
        d.text(x+30,T+H+14,str(yr),size=8.4,fill=INK2)
        d.text(x+30,T+H+28,f"flows ${fl[yr]}bn",size=7.6,fill=GOLD,weight="bold")
    d.text(L,18,"AWM client assets ($tn, bars) and net client asset flows ($bn, gold), 2021 to 2025",size=9.5,fill=NAVY,anchor="start",weight="bold")
    src(d,10,250,"Sources: Erdoes letters 2021 to 2025 [S312]-[S316]; FY2025 10-K [S300]. 2022 flows per the chart in the 2025 letter. Flows are firm-reported and include liquidity products.")
    return d.svg()

def centre_org():
    d=D(780,300)
    d.box(290,10,200,46,"Mary Callahan Erdoes","CEO, AWM",fill=NAVY)
    items=[("Ben Hesse","Head of Finance & Strategy (CFO; M&A)"),("Mike Urciuoli","Chief Information Officer & Chief Data and Analytics Officer"),("Julie Harris","Global Operations"),("Nelli Childs","Human Resources"),("Gregg Gunselman","Risk (reports into firmwide CRO Ashley Bacon)"),("Martin Marron","CEO Wealth Management Solutions (advice and product platform)"),("Legal & Compliance","(names not public on fetched pages)"),("Marketing & Communications","(names not public on fetched pages)")]
    for i,(t,b) in enumerate(items):
        x=15+(i%4)*190; y=90+(i//4)*95
        d.box(x,y,180,75,t,b,fill=WHITE if "not public" in b else NAVY2,tfill=NAVY if "not public" in b else WHITE,stroke=LINE,tsize=8.8,bsize=7.6)
        d.arrow(390,56,x+90,y,color=GREY,width=1)
    src(d,10,290,"Sources: names from the Feb 2026 Company Update and Investor Day 2025 materials [S320][S322] and JPM leadership pages [S6]; reporting line for risk per the 10-K risk governance section [S300]. Two boxes are placeholders where no name was verified.")
    return d.svg()

def wiring():
    d=D(780,330)
    d.box(290,120,200,80,"UK BANKER TEAM","Advisor, associates, analysts",fill=GOLD)
    emb=[("Client Service Associate","embedded: sits with the team"),("Business manager","embedded: runs the P&L, headcount, controls")]
    con=[("Investor / Capital Advisor / Wealth Advisor","connective: shared across teams in the market"),("Wealth Management Solutions","connective: builds advice and product for PB and Chase")]
    uti=[("KYC / onboarding operations","utility: firm-wide"),("Technology, data, Connect Coach","utility: firm-wide"),("Research, Global Investment Strategy","utility: firm-wide"),("Risk, compliance, legal","utility: firm-wide")]
    for i,(t,b) in enumerate(emb):
        d.box(20,30+i*70,220,56,t,b,fill=NAVY2,tsize=8.6,bsize=7.6); d.arrow(240,58+i*70,290,140+i*20,color=GOLD,marker="arrg",width=1.6)
    for i,(t,b) in enumerate(con):
        d.box(540,30+i*70,220,56,t,b,fill=NAVY2,tsize=8.6,bsize=7.6); d.arrow(540,58+i*70,490,140+i*20,color=NAVY,marker="arrn",width=1.6,dash=True)
    for i,(t,b) in enumerate(uti):
        x=20+i*190; d.box(x,240,175,56,t,b,fill=WHITE,tfill=NAVY,stroke=LINE,tsize=8.4,bsize=7.4); d.arrow(x+87,240,390-100+i*60,200,color=GREY,width=1.1)
    d.text(390,110,"solid gold = embedded · dashed navy = connective · grey = utility",size=7.8,fill=INK2,italic=True)
    src(d,10,320,"Sources: Client Advisor Support Associate posting [S14]; Paris Wealth Advisor posting ('partner with Bankers, Investors and Lending Advisors') [S18]; Erdoes on Wealth Management Solutions [S320]. Business-manager role is standard at JPM lines of business [Inferred].")
    return d.svg()

def value_chain():
    d=D(780,200)
    steps=[("Demand","a referral, an event, a news item, a cold call"),("Qualify","is this family a fit? size, complexity, source of wealth"),("Discover","the four lenses; the whole balance sheet"),("Propose","allocation, credit, planning, fees; the Solutions team"),("Onboard","KYC, suitability, entity, accounts"),("Deliver","assets in, loans drawn, trusts settled"),("Deepen","share of wallet, next generation, referrals out")]
    x=10
    for i,(t,b) in enumerate(steps):
        d.box(x,30,100,110,t,b,fill=NAVY if i%2==0 else NAVY2,tsize=9.5,bsize=7.6)
        if i<6: d.arrow(x+100,85,x+110,85,color=GREY,width=2)
        x+=110
    d.text(390,165,"Measured at the front: new clients, net new assets. Measured at the back: revenue on book, retention, share of wallet.",size=8.4,fill=INK2,italic=True)
    src(d,10,190,"Sources: JD [S1]; Erdoes Investor Day 2023 and 2024 on client metrics [S318][S319]; Client Advisor posting duties [S13].")
    return d.svg()

def two_channels():
    d=D(780,300)
    d.region(10,10,375,260,"CHANNEL 1: NEW CLIENTS (hunting)",fill=LGOLD,dash=False)
    for i,t in enumerate(["Internal referrals: CIB founders, Commercial Bank owners, Chase, Workplace","External referrals: existing clients, lawyers, accountants","Events and thought leadership","Direct prospecting (lists, news, networks)"]):
        d.box(20,40+i*52,355,44,t,None,fill=WHITE,tfill=NAVY,stroke=GOLD,tsize=8.4,tweight="normal")
    d.text(197,258,"Measured by new clients and net new assets",size=8,fill=INK2,italic=True)
    d.region(395,10,375,260,"CHANNEL 2: EXISTING CLIENTS (farming)",fill=BG,dash=False)
    for i,t in enumerate(["Reviews, rebalancing, market calls (Connect Coach prompts)","Adding legs: lending, deposits, trust, alternatives","Life events: sale, move, divorce, succession","Next generation and family office services; referrals back to channel 1"]):
        d.box(405,40+i*52,355,44,t,None,fill=WHITE,tfill=NAVY,stroke=LINE,tsize=8.4,tweight="normal")
    d.text(582,258,"Measured by share of wallet, revenue per client, retention",size=8,fill=INK2,italic=True)
    src(d,10,290,"Sources: Erdoes Investor Day 2025 on referral sources [S320]; Investor Day 2024 on '+65% assets and revenue when clients actively bank with us' [S319]; JD [S1].")
    return d.svg()

def worked_day():
    d=D(780,420)
    slots=[("07:30","Read overnight markets; Top Market Takeaways; Eye on the Market if new"),("08:00","Team huddle; morning markets meeting; Connect Coach flags three clients under-exposed to a theme"),("08:45","Prep for 10:00: pull portfolio report, check the loan-to-value on the Lombard facility, update the meeting brief"),("10:00","Client meeting with the banker and investor: quarterly review; the client raises a house purchase"),("11:30","Debrief; open a credit request; email the Capital Advisor; log notes in CRM"),("12:30","Lunch with an associate; or a learning session (alternatives, trusts)"),("14:00","Prospect research: three families in the news; a founder whose company the investment bank just sold"),("15:30","KYC: chase a source-of-wealth document; suitability form for a new mandate"),("16:30","Build two slides for tomorrow's pitch; check figures with the Investor"),("18:00","Event: the team hosts a founders' dinner; the intern takes names and follow-ups"),("20:00","Home. Read the Outlook chapter you were asked about.")]
    for i,(t,b) in enumerate(slots):
        y=15+i*36
        d.box(10,y,70,30,t,None,fill=NAVY,tsize=9)
        d.box(88,y,682,30,b,None,fill=BG if i%2 else WHITE,tfill=INK,stroke=LINE,tsize=8.2,tweight="normal")
    src(d,10,415,"Illustrative composite [Inferred] from the JD [S1], Client Advisor Support Associate duties [S14], Connect Coach description [S316] and forum accounts of London hours (~08:00 to 18:30) [S357] (anecdote).")
    return d.svg()

def hub():
    d=D(780,300)
    d.region(10,10,375,260,"WITHOUT A SINGLE OWNER",fill=LRED,dash=False)
    pts=[(60,60),(330,60),(60,240),(330,240),(197,40),(197,255),(60,150),(330,150)]
    labs=["Investor","Lender","Trust lawyer","Compliance","Client","Tax adviser","Trader","Family office"]
    for (x,y),l in zip(pts,labs):
        d.circle(x,y,16,fill=GREY); d.text(x,y+28 if y<200 else y-22,l,size=7.4,fill=INK)
    import itertools
    for (a,b) in itertools.combinations(pts,2):
        d.line(a[0],a[1],b[0],b[1],color="#c9a3a3",width=0.8)
    d.text(197,150,"28 conversations",size=9,fill=RED,weight="bold")
    d.region(395,10,375,260,"WITH THE ADVISOR AS HUB",fill=LGREEN,dash=False)
    cx,cy=582,150; d.circle(cx,cy,26,fill=GOLD); d.text(cx,cy+3,"Advisor",size=8.6,fill="#fff",weight="bold")
    pts2=[(cx+dx,cy+dy) for dx,dy in [(-150,-90),(150,-90),(-150,90),(150,90),(0,-110),(0,110),(-160,0),(160,0)]]
    for (x,y),l in zip(pts2,labs):
        d.circle(x,y,16,fill=NAVY2); d.text(x,y+28 if y<=cy else y-22,l,size=7.4,fill=INK)
        d.line(x,y,cx,cy,color=GOLD,width=1.4)
    d.text(cx,cy+60,"8 conversations, one owner",size=9,fill=GREEN,weight="bold")
    src(d,10,290,"Why the relationship role exists: the client needs one accountable person who holds the whole picture. Counterparty list from the JD and services pages [S1][S3][S5].")
    return d.svg()

def request_life():
    d=D(780,230)
    steps=[("Client asks","'I want £15m to buy a house without selling.'"),("Advisor frames","need, timing, collateral, the client's whole balance sheet"),("Capital Advisor structures","Lombard vs mortgage; LTV; currency; term"),("Credit underwriting","two ways out; concentration; margin-call rules"),("Compliance & legal","KYC refresh; suitability; documentation"),("Term sheet back","Advisor presents; client signs"),("Draw and monitor","LTV monitored daily; Advisor owns the relationship")]
    x=10
    for i,(t,b) in enumerate(steps):
        d.box(x,30,100,120,t,b,fill=NAVY if i%2==0 else NAVY2,tsize=8.6,bsize=7.4)
        if i<6: d.arrow(x+100,90,x+110,90,color=GREY,width=2)
        x+=110
    d.text(390,175,"The Advisor touches step 2 and step 6 and is accountable for all seven. Speed here is a selling point: 'a term sheet in days'.",size=8.4,fill=INK2,italic=True)
    src(d,10,200,"Sources: EMEA lending page [S4]; Erdoes on 'two ways out' and collateralised lending [S318][S319]; Lombard mechanics [S196][S197]. Internal approval steps are standard bank practice [Inferred].")
    return d.svg()

def collision():
    d=D(780,260)
    d.box(290,20,200,50,"SCARCE RESOURCE","the Investor's afternoon; credit capacity; the MD's time",fill=GOLD,bsize=7.6)
    for i,(t,b) in enumerate([("Banker A","'my £200m client needs the proposal by 9am'"),("Banker B","'my new £50m prospect is deciding tomorrow'"),("Compliance","'the KYC refresh is overdue on both'")]):
        x=40+i*260; d.box(x,110,220,50,t,b,fill=NAVY2,tsize=8.8,bsize=7.6); d.arrow(x+110,110,390,70,color=GREY,width=1.2)
    d.box(120,190,540,50,"HOW IT IS ALLOCATED","by the rule, then by client harm avoided, then by revenue, then by who asked first; escalate to the team lead, never decide alone as an intern",fill=WHITE,tfill=NAVY,stroke=GOLD,tsize=8.8,bsize=7.6)
    src(d,10,255,"The priority order is the author's synthesis of Business Principle 5 (risk discipline) and 1 (focus on the customer) [S323] and the Consumer Duty's 'good outcomes' standard [S206] [Inferred].")
    return d.svg()

def walls():
    d=D(780,330)
    cx,cy=390,165
    d.circle(cx,cy,48,fill=GOLD); d.text(cx,160,"The Advisor's",size=8.6,fill="#fff",weight="bold"); d.text(cx,173,"work",size=8.6,fill="#fff",weight="bold")
    rings=[("CLIENT CONFIDENTIALITY","crosses: what the client permits; never: gossip, other clients' names",NAVY),("SUITABILITY AND CONSUMER DUTY","crosses: advice that fits the client's objectives and risk; never: a product because it pays more",NAVY2),("INFORMATION BARRIER","crosses: public research, referrals; never: deal information, inside information",RED),("CREDIT AND RISK LIMITS","crosses: collateralised loans within appetite; never: a promise the credit committee has not made",GREEN)]
    for i,(t,b,c) in enumerate(rings):
        r=70+i*28
        d.parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c}" stroke-width="2" stroke-dasharray="6,4"/>')
    for i,(t,b,c) in enumerate(rings):
        y=30+i*70; x=20 if i%2==0 else 560
        d.box(x,y,200,58,t,b,fill=WHITE,tfill=c,stroke=c,tsize=7.8,bsize=7)
    src(d,10,320,"Sources: FCA Consumer Duty [S206]; MiFID II suitability [S215]; JPM Business Principles [S323]; standard bank information-barrier practice [Inferred].")
    return d.svg()

def reg_timeline(items):
    """items: list of (year_label, text, colour_kind)"""
    import textwrap
    wrapped=[(yr,textwrap.wrap(t,120),k) for yr,t,k in items]
    total=sum(len(w) for _,w,_ in wrapped)
    H=40+total*13+len(items)*10
    d=D(780,H+40)
    d.line(120,20,120,H,color=NAVY,width=2.5)
    y=30
    for yr,lines,k in wrapped:
        d.circle(120,y,5,fill=GOLD if k=="tax" else (RED if k=="conduct" else NAVY))
        d.text(112,y+3,yr,size=8.4,fill=NAVY,anchor="end",weight="bold")
        for j,l in enumerate(lines):
            d.text(134,y+3+j*13,l,size=8.2,fill=INK,anchor="start")
        y+=len(lines)*13+10
    y=H
    d.text(134,y+12,"navy = market and conduct regulation · red = financial crime and enforcement · gold = tax",size=7.6,fill=INK2,anchor="start",italic=True)
    return d.svg()

def shift_map(forces):
    d=D(780,60+((len(forces)+1)//2)*95)
    for i,(t,b,dirn) in enumerate(forces):
        x=15+(i%2)*380; y=15+(i//2)*95
        col = GREEN if dirn=="up" else (RED if dirn=="down" else NAVY2)
        d.box(x,y,365,82,t,b,fill=WHITE,tfill=col,stroke=col,tsize=9,bsize=7.6)
    src(d,10,50+((len(forces)+1)//2)*95,"Green = tailwind for a private bank advisor · red = headwind · navy = double-edged. Sources in Part 5.")
    return d.svg()

def funnel():
    d=D(780,260)
    stages=[("Online application","CV + questions; rolling; closes 1 Nov 2026",0),("HireVue video","3 to 5 questions; ~2 min answers; AI-scored then human",1),("Assessment / interviews","reported: three ~30-min interviews, behavioural and commercial",2),("Offer","for summer 2027 (9 weeks, June to August)",3),("Internship","project, reviews, conversion decision",4),("Full-time Advisor Analyst","5-week global training; London/Manchester/Edinburgh",5)]
    for i,(t,b,k) in enumerate(stages):
        w=740-i*80; x=20+i*40; y=15+i*38
        d.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="4" fill="{NAVY if i%2==0 else NAVY2}"/>')
        d.text(x+10,y+13,t,size=8.8,fill="#fff",anchor="start",weight="bold"); d.text(x+10,y+25,b,size=7.4,fill="#d8dfe9",anchor="start")
    d.circle(20,31,8,fill=GOLD); d.text(20,60,"YOU ARE HERE",size=7.6,fill=GOLD,weight="bold")
    src(d,10,250,"Sources: JD [S1]; JPM programme pages [S360][S361]; reported process from coaching sites and forums [S353]-[S358] (reported/anecdotal). Confidence per stage in Part 9.")
    return d.svg()

def protocol():
    d=D(780,220)
    steps=[("1. STEADY","0 to 10 seconds","Breathe out. 'Let me make sure I understand.' Restate the situation in one sentence."),("2. SORT","10 to 25 seconds","Name the rule, then the client, then the process, then speed. 'First, is anything here I can't do?'"),("3. ACT","25 to 60 seconds","Say what you would do, in order, with who you would involve. Concrete verbs."),("4. CLOSE","60 to 75 seconds","'And I'd log it and tell my team lead.' Then stop talking.")]
    x=10
    for i,(t,tm,b) in enumerate(steps):
        d.box(x,20,185,150,t,tm+"\n"+b,fill=NAVY if i%2==0 else NAVY2,tsize=10,bsize=8)
        if i<3: d.arrow(x+185,95,x+193,95,color=GOLD,marker="arrg",width=2)
        x+=193
    d.text(390,195,"Total 45 to 75 seconds. Longer answers invite the interruption; shorter ones invite the follow-up you want.",size=8.4,fill=INK2,italic=True)
    src(d,10,214,"Author's method; the priority order in step 2 follows the Business Principles [S323] and the Consumer Duty [S206].")
    return d.svg()

def priority():
    d=D(780,230)
    items=[("1. The rules and the firm's name","regulation, conduct, confidentiality. Non-negotiable."),("2. The client's outcome","and fair treatment of every internal client and colleague."),("3. The process and the record","the right approval, the note in the file, the escalation."),("4. Speed","last, and only within 1 to 3.")]
    for i,(t,b) in enumerate(items):
        w=740-i*120; x=20+i*60; y=15+i*45
        d.box(x,y,w,38,t,b,fill=[RED,GOLD,NAVY2,GREY][i],tsize=9.2,bsize=7.8)
    d.text(390,215,"The one sentence that holds every frame: 'I'd rather be slow and right than fast and wrong, and I'd tell you that to your face.'",size=8.6,fill=NAVY,weight="bold")
    return d.svg()

def frame_tactics():
    d=D(780,330)
    items=[("Interruption","Stop, let them finish, 'Good point, and...' resume from your last verb."),("Flat contradiction","'You may be right. Here is why I'd still start there.' Hold once; concede on facts, not on rules."),("Silence","Count to three. Then: 'Would it help if I went deeper on any part?'"),("Escalation ('the client is furious')","Acknowledge the emotion, restate the rule, offer the path: 'I'd get my team lead on the call today.'"),("Authority squeeze ('I'm the MD, just do it')","'Understood. I'll do it the moment we have X. Can I get that from you now?'"),("False choice ('lose the client or break the rule')","Reject the frame: 'I don't think those are the only two options.' Offer the third."),("Knowledge trap","'I don't know that figure. My understanding is X; I'd check before acting.'"),("Invitation to badmouth","Decline warmly: 'I'd rather tell you what I'd do differently than criticise them.'")]
    for i,(t,b) in enumerate(items):
        x=15+(i%2)*380; y=15+(i//2)*72
        d.box(x,y,365,62,t,b,fill=WHITE,tfill=RED,stroke=LINE,tsize=8.8,bsize=7.6)
    src(d,10,320,"Author's method. The counters keep the priority order intact and never concede on rules or confidentiality.")
    return d.svg()

def ladder(bullets):
    d=D(780,40+len(bullets)*56)
    d.text(140,18,"JD duty",size=8.6,fill=NAVY,weight="bold"); 
    for j,l in enumerate(["Easy","Medium","Hard"]):
        d.text(340+j*150,18,l,size=8.6,fill=[GREEN,"#c9932a",RED][j],weight="bold")
    for i,(b,rungs) in enumerate(bullets):
        y=30+i*56
        d.box(10,y,255,48,b,None,fill=NAVY2,tsize=7.8,tweight="normal")
        for j,r in enumerate(rungs):
            d.box(275+j*150,y,140,48,r,None,fill=[LGREEN,LGOLD,LRED][j],tfill=INK,stroke=[GREEN,"#c9932a",RED][j],tsize=7.2,tweight="normal")
    return d.svg()

def decision_tree(title, root, branches):
    """branches: list of (condition, action) shown as two-level tree."""
    d=D(780,300)
    d.text(390,18,title,size=10,fill=NAVY,weight="bold")
    d.box(290,30,200,50,root,None,fill=GOLD,tsize=8.8)
    n=len(branches); w=740/n
    for i,(cond,act,nxt) in enumerate(branches):
        x=20+i*w+w/2
        d.box(x-w/2+8,120,w-16,50,cond,None,fill=NAVY2,tsize=8,tweight="normal")
        d.arrow(390,80,x,120,color=GREY)
        d.box(x-w/2+8,195,w-16,60,act,nxt,fill=WHITE,tfill=NAVY,stroke=LINE,tsize=8,bsize=7.2)
        d.arrow(x,170,x,195,color=GOLD,marker="arrg")
    src(d,10,290,"Author's method, consistent with Business Principles 5, 11 and 12 [S323] and the Consumer Duty [S206].")
    return d.svg()

def why_firm_one_page():
    d=D(780,520)
    d.text(390,24,"WHY J.P. MORGAN PRIVATE BANK: THE MECHANISM ON ONE PAGE",size=12,fill=NAVY,weight="bold")
    d.circle(390,260,60,fill=GOLD); d.text(390,252,"The client's",size=9.5,fill="#fff",weight="bold"); d.text(390,266,"whole balance sheet,",size=9.5,fill="#fff",weight="bold"); d.text(390,280,"one owner",size=9.5,fill="#fff",weight="bold")
    nodes=[("The referral engine","IB founders, Commercial Bank owners, Chase, Workplace: '2,000 PB clients walk into the branches every day'; 95% of top clients use other LOBs [S320][S316]",390,80),
           ("The balance sheet","$266bn PB loans; 97% collateralised; 1bp losses; largest sports and jumbo-mortgage lender [S300][S318][S319]",660,190),
           ("The apprenticeship","'we seed books, we don't buy them'; half of advisors home-grown; break-even year 3; 4,101 advisors, +64% in five years [S317][S320][S316]",660,340),
           ("The fiduciary stance","'north star'; open shelf with 850+ managers; 83% of active funds beat peers over 10 years [S315][S316][S320]",390,440),
           ("The uniform global model","'the only private bank with a uniform business model globally'; London runs the international bank; Europe named as biggest share opportunity [S316][S24]",120,340),
           ("The economics","36% margin, 40% ROE; targets never raised; investment spend $2.7bn; hiring peaks now and 'normalizes later this decade' [S316][S320]",120,190)]
    for t,b,x,y in nodes:
        d.box(x-120,y-40,240,80,t,b,fill=NAVY2,tsize=9,bsize=6.9)
        dx,dy=390-x,260-y; L=(dx*dx+dy*dy)**0.5
        if L>0: d.arrow(x+dx/L*90,y+dy/L*40,390-dx/L*64,260-dy/L*64,color=GOLD,marker="arrg",width=1.4)
    d.text(390,505,"Every box is a mechanism with a number and a source. None of them can be said of UBS, Goldman, Coutts or Morgan Stanley in the same words.",size=8.4,fill=INK2,italic=True)
    return d.svg()

def master():
    d=D(780,560)
    d.text(390,22,"THE MASTER DIAGRAM: FIRM, INDUSTRY, ROLE",size=12,fill=NAVY,weight="bold")
    d.region(10,40,760,150,"THE INDUSTRY: forces on private banking (Part 5)",fill=BG,dash=False)
    for i,t in enumerate(["Great wealth transfer: $124tn US by 2048; £5.5tn UK by 2047","UHNW population +14% in 2025; 80% self-made","Alternatives into private wealth; evergreen funds","AI: advisors handle more clients; ops shrink","Fee pressure below £5m; resilience above","Tax migration: non-dom abolition; Gulf and Italy pull"]):
        d.box(20+(i%3)*250,68+(i//3)*58,240,50,t,None,fill=WHITE,tfill=INK,stroke=LINE,tsize=7.6,tweight="normal")
    d.arrow(390,190,390,215,color=NAVY,marker="arrn",width=2)
    d.region(10,215,760,170,"THE FIRM: how JPMorgan answers them (Parts 2 to 4)",fill=LGOLD,dash=False)
    for i,t in enumerate(["Fortress balance sheet: lend, stay, buy in crises","Completeness: referrals across CCB, CIB, AWM with no internal pricing","Apprenticeship: seed books; train; AI shortens the J-curve","Uniform global model; London runs the international bank","Fiduciary stance and open shelf; performance as arbiter","Invest through the cycle: advisors +64%; $2.7bn AWM investment"]):
        d.box(20+(i%3)*250,243+(i//3)*66,240,58,t,None,fill=NAVY2,tsize=7.8,tweight="normal")
    d.arrow(390,385,390,410,color=NAVY,marker="arrn",width=2)
    d.region(10,410,760,130,"THE ROLE: what the Advisor intern does inside that (Part 1)",fill=LGREEN,dash=False)
    for i,t in enumerate(["Learn the whole balance sheet of a family","Find and qualify prospects through the referral engine","Assemble proposals with the Investor and specialists","Hold the rules: KYC, suitability, confidentiality, barriers","Own the answer that goes back to the client"]):
        d.box(20+i*150,438,140,90,t,None,fill=WHITE,tfill=NAVY,stroke=GREEN,tsize=7.6,tweight="normal")
    src(d,10,555,"Sources: Parts 1 to 5 of this pack; each box is expanded with sources in the relevant part.")
    return d.svg()
