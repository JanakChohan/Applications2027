from svg import *
from diagrams2 import src, S1, S2, INK, INK2, LGREEN, LGOLD, LRED
import charts as ch, diagrams2 as d2

def team_org():
    d=D(780,520)
    C="#2e7d5b"; A="#c9932a"; G="#8a93a3"
    def box(x,y,w,h,t,b,conf):
        col={"c":C,"r":A,"i":G}[conf]
        d.box(x,y,w,h,t,b,fill=WHITE,tfill=NAVY,stroke=col,tsize=8.4,bsize=7.2)
        d.parts.append(f'<rect x="{x}" y="{y}" width="6" height="{h}" fill="{col}"/>')
    box(280,10,220,44,"Adam Tejpaul","CEO International Private Bank (London)","c")
    box(280,74,220,44,"Pablo Garnica","CEO EMEA Private Bank (Madrid)","c")
    d.arrow(390,54,390,74,color=GREY)
    box(20,140,220,44,"Maricé Brown","Region Head UK, Channel Islands & Ireland","c")
    box(280,140,220,44,"Sarah Catania","Head of Continental Europe (Milan)","c")
    box(540,140,220,44,"Karim Rekik","Switzerland, Middle East & Emerging Markets","c")
    for x in (130,390,650): d.arrow(390,118,x,140,color=GREY)
    # UK teams
    teams=[("UK Team (London & South)","ED banker req open Apr 2026","c"),("UK Domestic & Crown Dependencies","Maya Prabhu, Team Head","c"),("UK North (Manchester)","Khayyam Jumani, Team Head","c"),("Entrepreneurs & Executives","Sr Associate banker req Jun 2026","c"),("Financial Institutions Group","Paul Ferry, Team Head (ex-Citi)","r"),("Institutional Wealth Group","Zeynep Ozturk Unlu, Team Head","c"),("Team (coverage unknown)","Deepak Chander, Team Head","r"),("Scotland (Edinburgh/Glasgow)","advisor team since Feb 2024","c")]
    for i,(t,b,cf) in enumerate(teams):
        x=20+(i%4)*190; y=210+(i//4)*58
        box(x,y,178,48,t,b,cf); d.arrow(130,184,x+89,y,color=GREY,width=0.9)
    # shared bench
    d.region(20,335,740,70,"SHARED SPECIALIST BENCH (per market)",fill=LGOLD,dash=False)
    for i,(t,b,cf) in enumerate([("Investors","Diana Robinson, Head of Investments & Advice UK","c"),("Lending / Capital Advisors","Lending Advisor reqs UK and MENAT; mortgage specialist","c"),("Wealth Advisory","James Chilvers (UK); Chris Ottenritter (EMEA)","c"),("Client service; business mgmt","not found in London postings","i")]):
        box(30+i*183,358,172,42,t,b,cf)
    # London MENAT desk
    box(540,210,220,44,"MENAT desk (London-booked)","VP banker and VP lending advisor reqs 2026","c")
    d.arrow(650,184,650,210,color=GREY,width=0.9)
    # pyramid
    d.region(20,420,740,60,"PYRAMID INSIDE A TEAM (from postings)",fill=BG,dash=False)
    d.text(390,448,"MD Team Head / Market Manager → ED and VP Private Bankers → Senior Associate / Associate → Advisor Analysts (2-year programme) → summer interns",size=8.4,fill=INK)
    d.text(390,464,"Investment Solutions analysts sit with the specialists, not the bankers",size=8,fill=INK2,italic=True)
    # legend
    for i,(cf,l) in enumerate([("c","confirmed by the firm's pages"),("r","reported by a single source"),("i","inferred from postings")]):
        col={"c":C,"r":A,"i":G}[cf]; x=20+i*240
        d.parts.append(f'<rect x="{x}" y="{492}" width="10" height="10" fill="{col}"/>'); d.text(x+14,501,l,size=7.8,fill=INK2,anchor="start")
    src(d,20,516,"Sources: London office page [S55]; leadership page [S54]; bios [S56]-[S60]; postings [S40]-[S53]; press [S64][S65][S377]. Reconstruction; no org chart is published.")
    return d.svg()

def hiring_map():
    rows=[("Private Banker (ED/VP/Sr Assoc)","London",5),("Lending / Capital Advisor (VP)","London",2),("Mortgage Solutions Specialist (VP)","London",1),("Marketing (Head EMEA; Channel Lead VP)","London",2),("Advisor Analyst Programme 2027","London, Manchester, Edinburgh",1),("Investment Solutions Analyst 2027","London",1),("Summer internships 2027 (Advisor; Investment Solutions)","London",2),("Regulatory Control Lead (AWM)","Glasgow",1),("Product Designer, Advisor Experience","London / Glasgow",1),("Marketing (Head EMEA; Channel Lead VP)","London",0)]
    rows=[r for r in rows if r[2]>0]
    d=D(780,60+len(rows)*26+40)
    d.text(12,20,"Open J.P. Morgan Private Bank postings touching the UK, 11 September 2026 (count of requisitions)",size=10,fill=NAVY,anchor="start",weight="bold")
    for i,(t,c,n) in enumerate(rows):
        y=40+i*26
        d.text(12,y+13,t,size=8.4,fill=INK,anchor="start")
        d.text(420,y+13,c,size=8,fill=INK2,anchor="start")
        for k in range(n):
            d.parts.append(f'<rect x="{590+k*30}" y="{y}" width="26" height="18" rx="3" fill="{GOLD if "Analyst" in t or "intern" in t else NAVY2}"/>')
        d.text(590+n*30+6,y+13,str(n),size=8.4,fill=INK,anchor="start")
    src(d,12,40+len(rows)*26+22,"Source: requisitions read via the careers system's public data feed [S40]-[S51]. Gold = campus programmes. Counts are at one date and change daily.")
    return d.svg()

def why_works():
    d=D(780,300)
    d.text(390,22,"WHY THE STRUCTURE WORKS: THE SHARE-OF-WALLET ARITHMETIC THE FIRM DISCLOSES",size=10.5,fill=NAVY,weight="bold")
    items=[("Investment-only client","1 leg","index 100","#c9d3e2"),("+ actively banks (deposits)","2 legs","assets and revenue +65% on average","#8fb0d9"),("+ lending","3 legs","only 2% of clients are credit-only; loans make clients hard to lose","#2f6fb2"),("+ trust and next generation","4 legs","retention >95%; relationship spans generations",NAVY)]
    for i,(t,l,b,c) in enumerate(items):
        x=15+i*190; h=90+i*40
        d.parts.append(f'<rect x="{x}" y="{240-h}" width="175" height="{h}" rx="5" fill="{c}"/>')
        d.text(x+87,240-h+16,t,size=8.6,fill="#fff" if i>0 else INK,weight="bold")
        d.text(x+87,240-h+30,l,size=8,fill="#fff" if i>0 else INK)
        d.text(x+87,258,b,size=7.4,fill=INK2,maxw=170)
    src(d,12,292,"Sources: Investor Day 2024 ('+65% assets and revenue when US Private Bank clients actively bank with us'; '2% credit-only clients') [S319]; Investor Day 2023 ('>95% don't leave') [S318]. Illustrative heights.")
    return d.svg()

def spectrum():
    peers={("Local heritage bank","Uniform global model"):[("Coutts",0.05),("Barclays PB",0.2),("HSBC GPB",0.45),("Citi PB",0.7),("UBS GWM",0.88),("JPM Private Bank",0.95)],
           ("Asset-light adviser","Balance-sheet heavy"):[("Independent adviser",0.05),("Pictet / Lombard Odier",0.3),("Goldman PWM",0.5),("Morgan Stanley",0.6),("UBS",0.8),("JPM Private Bank",0.92)],
           ("Adviser owns the client (grid pay)","Firm owns the client (team, salary+bonus)"):[("Merrill / Morgan Stanley (US)",0.1),("Julius Baer",0.5),("Goldman PWM",0.6),("UBS",0.75),("JPM Private Bank",0.9)],
           ("Proprietary product","Open shelf"):[("Some Swiss houses",0.3),("Goldman",0.4),("Morgan Stanley",0.6),("JPM Private Bank",0.7),("UBS",0.75),("Independent adviser",0.95)]}
    return d2.spectrum(peers)

def reg_timeline():
    items=[("1986","Financial Services Act 1986: statutory framework via the SIB and self-regulating bodies","reg"),
           ("2001","FSMA 2000 in force (1 Dec): the FSA as single regulator; 'regulated activities'","reg"),
           ("2002","Proceeds of Crime Act: duty to report suspected money laundering (s.330)","conduct"),
           ("2011","Bribery Act in force (1 Jul); s.7 failure to prevent bribery","conduct"),
           ("2012","Retail Distribution Review (31 Dec): commission ban, adviser charging, Level 4","reg"),
           ("2013","FCA and PRA created (1 Apr); FCA fines J.P. Morgan International Bank £3.1m for wealth record-keeping (May)","reg"),
           ("2016","Senior Managers regime for banks (7 Mar); UK Market Abuse Regulation (Jul)","reg"),
           ("2017","Money Laundering Regulations 2017 (26 Jun)","conduct"),
           ("2018","MiFID II applies (3 Jan): suitability, costs, product governance, call recording","reg"),
           ("2019","SM&CR extended to all FCA firms (9 Dec)","reg"),
           ("2021","End of MiFID passport (31 Dec 2020); ESMA reverse-solicitation warning (13 Jan)","reg"),
           ("2023","Consumer Duty in force (31 Jul); FCA Dear CEO letter to wealth managers (8 Nov)","reg"),
           ("2024","Consumer Duty for closed books (31 Jul); domestic PEPs lower-risk (10 Jan); CGT 18%/24% (30 Oct)","tax"),
           ("2025","Non-dom regime abolished (6 Apr); ring-fencing threshold £35bn (4 Feb); ongoing-advice review (24 Feb); FG25/3 on PEPs (7 Jul); failure-to-prevent-fraud offence (1 Sep); Autumn Budget (26 Nov); CP25/36 £10m opt-up (8 Dec); CCI rules (8 Dec)","tax"),
           ("2026","Basel 3.1 final rules (20 Jan); Consumer Investments priorities (4 Mar); targeted support live (6 Apr); dividend tax +2pp (6 Apr); APR/BPR £1m cap (6 Apr); SM&CR reform PS26/6 (22 Apr); account-closure notice rules (28 Apr); non-financial misconduct rules (1 Sep)","reg"),
           ("2027","Basel 3.1 live (1 Jan); savings and property income +2pp (6 Apr); pensions into IHT (6 Apr); CCI mandatory (8 Jun)","tax"),
           ("2028","High Value Council Tax Surcharge on £2m+ homes (1 Apr); market-risk internal models (1 Jan)","tax")]
    return d2.reg_timeline(items)+ '<div class="small">Sources: [S120]-[S149][S370]. Dates verified against FCA, PRA, HMRC and legislation.gov.uk pages on 11 September 2026; see Part 6.</div>'

def shift_map():
    forces=[("Great wealth transfer","$124tn in the US through 2048; £5.5tn in the UK by 2047; heirs switch advisers, so next-generation work grows [S190][S191]","up"),
            ("UHNW population growth","556,850 individuals in 2025, +14%; 80% of North American UHNW self-made: more founders, more liquidity events [S192]","up"),
            ("Alternatives into private wealth","UHNW at ~22% and rising; evergreen funds $644bn; but 2026 redemption gates and valuation doubts [S203][S202][S257]","mixed"),
            ("AI in the adviser's seat","Prep and admin shrink (Connect Coach; 95% faster information); books can grow 50%; operations jobs cut 30 to 40% in places [S213][S336][S232]","mixed"),
            ("Fee compression below, resilience above","83% of US advisers expect sub-1% fees for $5m+; UHNW value comes from lending, structuring and access [S204]","mixed"),
            ("Regulation","Consumer Duty, MiFID II suitability, the £10m opt-up, financial-crime enforcement: more documentation, more protection for the client, more work per relationship [S146][S121][S124]","mixed"),
            ("Tax migration from the UK","Non-dom abolition; Henley scores the UK 68.3 vs the UAE 85.3; families split assets across London, Dubai, Milan, Geneva [S243][S244]","down"),
            ("Talent movement and consolidation","Bankers move with books; Coutts absorbs Evelyn; UBS constrained by Swiss capital rules: openings for a hiring firm [S214][S256][S253]","up")]
    return d2.shift_map(forces)

def ladder():
    bullets=[("Understand client needs and examine market activities to develop and execute strategies",["The morning brief","The concentrated position","House view vs client vs banker"]),
             ("Work with a team of bankers, investment specialists, wealth advisors and lending specialists",["The wrong specialist","Two specialists disagree","A specialist not responding"]),
             ("Collaborate with market strategy, equity and alternatives teams as part of a Solutions Team",["The project brief","The number you can't verify","Private credit after the gates"]),
             ("Bring in new clients and serve existing ones",["The prospect list","The first meeting","The client who wants to leave"]),
             ("Good judgment and discretion with confidential information",["The friend","The document on the printer","The inside information"])]
    return d2.ladder(bullets)

def cheat():
    d=D(780,300)
    d.text(390,22,"THE CHEAT SHEET IN ONE PICTURE",size=11,fill=NAVY,weight="bold")
    d.box(20,40,230,110,"PROTOCOL","Steady → Sort → Act → Close\n45 to 75 seconds",fill=NAVY,tsize=10,bsize=8.4)
    d.box(275,40,230,110,"PRIORITY ORDER","1 rules and the firm's name\n2 the client's outcome\n3 process and record\n4 speed",fill=GOLD,tsize=10,bsize=8.4)
    d.box(530,40,230,110,"THE SENTENCE","'I'd rather be slow and right than fast and wrong, and I'd tell you that to your face.'",fill=NAVY2,tsize=10,bsize=8.4)
    d.box(20,170,360,110,"THE MECHANISM","Referral engine with no credit-counting · balance sheet, two ways out · seeded books, home-grown advisors · uniform global model, Europe the share target",fill=WHITE,tfill=NAVY,stroke=GOLD,tsize=10,bsize=8.2)
    d.box(400,170,360,110,"THE NEVERS","Confirm a client · open before KYC · act on or repeat inside information · promise a loan or return · give advice as an intern · badmouth anyone · say 'biggest and best'",fill=WHITE,tfill=RED,stroke=RED,tsize=10,bsize=8.2)
    return d.svg()

def define2(F, dg, ch_, d2_, strip):
    F("team_org", team_org(), "Reconstructed UK Private Bank org chart, colour-coded by confidence (green: confirmed by the firm's pages; amber: reported by a single source; grey: inferred from postings).")
    F("hiring_map", hiring_map(), "What the Private Bank is hiring for in the UK: open requisitions by function and city on 11 September 2026 [S40]-[S51].")
    F("why_works", why_works(), "Why the structure works: each additional 'leg' of a relationship raises assets, revenue and retention, in the firm's disclosed numbers [S318][S319].")
    F("spectrum", spectrum(), "The competitive spectrum: four design axes and where each rival sits. Positions are the author's judgement from the firms' own descriptions [Inferred].")
    F("reg_timeline", reg_timeline(), "The regulation and tax timeline for UK private banking, 1986 to 2028.")
    F("shift_map", shift_map(), "The industry shift map: eight forces and which way each pushes a private bank advisor in London.")
    F("ladder", ladder(), "The scenario ladder: every duty in the posting, three rungs.")
    F("cheat", cheat(), "The cheat sheet on one page; the text version follows.")
    F("timeline", ch_.timeline([("2021",[("Record profit $48bn","firm"),("Chase UK launches; Nutmeg, 55ip, OpenInvest bought","deal"),("AWM: four ingredients; $389bn flows","awm")]),
        ("2022",[("$15bn investment plan; 'good expenses'","firm"),("Rates surge; 'hurricane'","macro"),("AWM passes 3,000 PB advisors; Global Shares bought","awm")]),
        ("2023",[("SVB and First Republic fail; JPM buys FRC (1 May)","deal"),("Record $162bn revenue; Basel fight","firm"),("AWM: $490bn flows; 'four $100m clients a day'","awm")]),
        ("2024",[("CB merged into CIB (Jan); LLM Suite to 200k staff","firm"),("$54bn excess capital; no buybacks 'at these prices'","firm"),("AWM ROE 34%; #1 active ETF flows; six new offices","awm")]),
        ("2025",[("Security & Resiliency plan (Oct); Apple Card (Jan 2026); 270 Park","deal"),("8th record year; ROTCE 20%; Piepszak COO","firm"),("AWM $553bn flows; 4,101 advisors; Frame; Brown UK head","awm")]),
        ("2026",[("Basel rescinded (Mar); Chase Germany (May); co-presidents (Jun)","firm"),("Hormuz oil shock; gilts 5.36%; BoE 6-3 hold","macro"),("Q2: AWM $7.7tn; Europe 'biggest share opportunity'","awm")])]), "Six years in one line: firm, AWM and Private Bank events, deals and macro [S300]-[S322][S220]-[S259].")
