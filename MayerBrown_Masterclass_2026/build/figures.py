"""Figure registry. Each fig_* returns (svg, caption, full_page)."""
from svglib import *
import importlib
REG={}
def fig(key,full=False):
    def deco(fn):
        REG[key]=(fn,full); return fn
    return deco
def get(key):
    fn,full=REG[key]
    svg_,cap=fn()
    return svg_,cap,full

# ---------- Playbook figures (method, not facts) ----------
@fig("protocol")
def _():
    w,h=760,250
    steps=[("1 STEADY","Breathe once. Repeat the core of the question back in one line.","\"So the question is whether I'd... \"",GRN),
           ("2 SORT","Name what is in tension and rank it with your priority order.","\"Two things matter here: X and Y. X comes first because...\"",BLU),
           ("3 ACT","Say the concrete next step, who you tell, and by when.","\"I'd flag it to my supervising associate now, with...\"",ACC),
           ("4 CLOSE","Land the principle in one sentence and stop talking.","\"So: rules first, then the client, then speed.\"",SIG)]
    s=""
    bw=178
    for i,(t,d,q,c) in enumerate(steps):
        x=i*(bw+16)
        s+=f'<rect x="{x}" y="10" width="{bw}" height="190" rx="8" fill="#fff" stroke="{c}" stroke-width="2"/>'
        s+=f'<rect x="{x}" y="10" width="{bw}" height="34" rx="8" fill="{c}"/><rect x="{x}" y="34" width="{bw}" height="10" fill="{c}"/>'
        s+=text(x+bw/2,32,t,13,WHITE,"middle",800)
        s+=text(x+10,64,d,10.5,NAVY,weight=600,maxw=bw-20)
        s+=text(x+10,134,q,9.8,GREY,maxw=bw-20,italic=True)
        if i<3: s+=arrow(x+bw+1,105,x+bw+15,105,NAVY)
    s+=f'<rect x="0" y="212" width="{w}" height="30" rx="6" fill="{TINT}"/>'
    s+=text(w/2,232,"Timing: 5 s steady · 15 s sort · 25-40 s act · 5-10 s close  =  45 to 75 seconds in total",11,NAVY,"middle",700)
    return svg(w,h,s),"The four-step answer protocol for any scenario or hypothetical. <b>Source:</b> author's method [Inferred]."

@fig("priority")
def _():
    w,h=760,300
    tiers=[("1","Professional conduct and the firm's name","SRA Principles, confidentiality, conflicts, honesty. Never traded for anything.",RED),
           ("2","The client's interest, served fairly","Every client and every internal team gets accurate work and honest status.",ACC),
           ("3","The process and the record","Checklists, version control, file notes, telling your supervisor. The audit trail.",BLU),
           ("4","Speed and convenience","Deadlines matter, but only after 1 to 3 are safe.",GRN)]
    s=""
    for i,(n,t,d,c) in enumerate(tiers):
        inset=i*40; y=10+i*62
        s+=f'<rect x="{inset}" y="{y}" width="{w-2*inset}" height="54" rx="7" fill="{c}" fill-opacity="0.12" stroke="{c}" stroke-width="1.6"/>'
        s+=f'<circle cx="{inset+28}" cy="{y+27}" r="15" fill="{c}"/>'+text(inset+28,y+32,n,14,WHITE,"middle",800)
        s+=text(inset+54,y+23,t,12,NAVY,weight=700)
        s+=text(inset+54,y+41,d,9.8,GREY,maxw=w-2*inset-70)
    s+=text(w/2,h-8,"\"I'd protect the rules and the client first, keep the record straight, and then go as fast as that allows.\"",11,SIG,"middle",700,italic=True)
    return svg(w,h,s),"The priority order when good things collide in a trainee seat, and the one sentence that holds every frame. <b>Basis:</b> the SRA Principles put integrity, independence and acting in the client's best interests above convenience; see Part 6 [Inferred ordering]."

@fig("tactics")
def _():
    w,h=760,470
    T=[("Interruption","They cut you off mid-answer.","Stop. \"Sure.\" Answer the new point, then: \"To finish my earlier point in one line...\""),
       ("Flat contradiction","\"That's wrong.\"","\"Which part? ...If X is true, then I'd change my view to Y.\" Update on facts, not on pressure."),
       ("Silence","They say nothing after you finish.","Do not fill it with a new answer. \"Happy to go deeper on any part of that.\""),
       ("Escalation","\"Now the client is shouting and it's 11pm.\"","Same priority order, faster action. Name who you call and what you send."),
       ("Authority squeeze","\"The partner says just do it.\"","\"I'd do it, and I'd also raise the concern with them directly first.\""),
       ("False choice","\"Client or firm: pick one.\"","\"I don't think those conflict here, because... if they truly did, the rules decide.\""),
       ("Knowledge trap","A fact or term you don't know.","\"I don't know that yet. My guess from first principles is... and I'd check X.\""),
       ("Invite to badmouth","\"Isn't [rival firm] better?\"","Praise the rival precisely, then say what fits you here. Never knock anyone.")]
    s=""
    cw,ch=372,108
    for i,(n,a,c) in enumerate(T):
        col=i%2; row=i//2
        x=col*(cw+16); y=row*(ch+8)
        s+=f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="7" fill="#fff" stroke="{LINE}" stroke-width="1.2"/>'
        s+=f'<rect x="{x}" y="{y}" width="6" height="{ch}" rx="3" fill="{RED}"/>'
        s+=text(x+16,y+19,f"{i+1}. {n}",11.5,NAVY,weight=800)
        s+=text(x+16,y+36,a,9.6,RED,weight=600,maxw=cw-26)
        s+=text(x+16,y+56,"Counter: "+c,9.6,GREEN if False else GRN,weight=500,maxw=cw-26)
    return svg(w,h,s),"Eight ways an interviewer or networking contact breaks your frame, and the counter to each. <b>Source:</b> author's method [Inferred]."

@fig("ladder", full=False)
def _():
    rows=[("A1","Application form (SEO, by 26 Oct)"),("A2","Firm overview session"),("A3","Trainee panel"),("A4","Practice deep dive"),
          ("A5","Applications overview"),("A6","Networking"),("T1","Legal research and notes"),("T2","Drafting"),("T3","Due diligence and document review"),
          ("T4","Running a deal: CPs, signing, closing"),("T5","Disputes support: disclosure, bundles, hearings"),("T6","Client and team communication"),("T7","Knowledge, BD and pro bono")]
    w=760; rh=29; top=34; h=top+len(rows)*rh+8
    s=text(0,14,"Duty line",11,NAVY,weight=800)+text(300,14,"Easy",11,GRN,"middle",800)+text(470,14,"Medium",11,AMB,"middle",800)+text(640,14,"Hard",11,RED,"middle",800)
    for i,(c,l) in enumerate(rows):
        y=top+i*rh
        s+=f'<rect x="0" y="{y}" width="{w}" height="{rh-3}" rx="4" fill="{TINT if i%2==0 else WHITE}"/>'
        s+=text(6,y+17,c,10,ACC,weight=800)+text(34,y+17,l,10,NAVY,weight=600)
        for j,(cx,col) in enumerate(((300,GRN),(470,AMB),(640,RED))):
            s+=f'<rect x="{cx-58}" y="{y+4}" width="116" height="{rh-11}" rx="9" fill="{col}" fill-opacity="0.16" stroke="{col}"/>'
            s+=text(cx,y+17,f"Card {c}.{j+1}",9.2,col,"middle",700)
        s+=arrow(360,y+13,410,y+13,GREY,1)+arrow(530,y+13,580,y+13,GREY,1)
    return svg(w,h,s),"The scenario ladder: every duty line from the event page and the trainee role, three rungs each, easy to hard. The cards follow in the same order. <b>Source:</b> duty lines from the SEO event page and Mayer Brown's trainee description (Part 1)."

@fig("tree_control")
def _():
    w,h=760,400
    s=""
    s+=box(250,0,260,44,"Senior colleague asks you to skip a step",NAVY,NAVY,WHITE,11)
    s+=arrow(380,44,380,66)
    s+=box(230,66,300,48,"Is the step a legal or regulatory requirement, or would skipping it mislead anyone?",AMBS,AMB,NAVY,10)
    s+=arrow(300,114,150,150,RED,label="Yes / not sure",loff=(-30,-2))
    s+=arrow(460,114,610,150,GRN,label="No, it's internal habit",loff=(40,-2))
    s+=box(10,150,280,64,"Do not skip. Say so calmly: \"I don't think I can do that without X. Can we check with [supervisor]?\"",REDS,RED,NAVY,9.6,500)
    s+=box(470,150,280,64,"Ask why, do it their way if they own the decision, and note it on the file.",GRNS,GRN,NAVY,9.6,500)
    s+=arrow(150,214,150,246,RED)
    s+=box(10,246,280,58,"Still pressed? Escalate to supervising partner or risk/compliance (General Counsel's office). Record what was asked.",REDS,RED,NAVY,9.6,500)
    s+=arrow(610,214,610,246,GRN)
    s+=box(470,246,280,58,"Close the loop: \"Done, and I've noted why on the file.\"",GRNS,GRN,NAVY,9.6,500)
    s+=box(110,326,540,62,"Bright lines a trainee never crosses: backdating, altering a signed document, misleading a court or the other side, releasing signature pages without authority, sharing client confidential information.",SIGS,SIG,NAVY,9.8,600)
    return svg(w,h,s),"Decision tree 1: a senior person asks you to skip a control. <b>Basis:</b> SRA Principles [S341] and Code of Conduct for Solicitors [S342] on integrity, honesty and not misleading others; see Part 6 [Confirmed for the rules, Inferred for the tree]."

@fig("tree_info")
def _():
    w,h=760,380
    s=""
    s+=box(230,0,300,44,"You hear something that may be confidential or price-sensitive",NAVY,NAVY,WHITE,10.5)
    s+=arrow(380,44,380,66)
    s+=box(230,66,300,44,"Does it concern a client, a deal, or a listed company?",AMBS,AMB,NAVY,10)
    s+=arrow(300,110,150,140,RED,label="Yes / maybe",loff=(-26,-2))
    s+=arrow(460,110,610,140,GRN,label="Clearly public",loff=(36,-2))
    s+=box(10,140,280,58,"Treat as confidential and as possible inside information. Do not repeat it, trade on it or tip anyone.",REDS,RED,NAVY,9.6,500)
    s+=box(470,140,280,58,"Fine to discuss, but say where you read it (\"the FT reported...\").",GRNS,GRN,NAVY,9.6,500)
    s+=arrow(150,198,150,226,RED)
    s+=box(10,226,280,62,"Were you meant to hear it? If not, say so to the person, stop listening, and tell your supervisor / compliance.",REDS,RED,NAVY,9.6,500)
    s+=arrow(150,288,150,314,RED)
    s+=box(10,314,280,50,"Write a short note of what happened and when. Then let compliance decide.",REDS,RED,NAVY,9.6,500)
    s+=box(330,226,420,138,"Why: insider dealing is a criminal offence under Part V of the Criminal Justice Act 1993; unlawful disclosure of inside information is prohibited by UK MAR (Articles 10 and 14). Client confidentiality is a professional duty under the SRA Code of Conduct (paragraph 6.3). At a masterclass, the same rule applies to anything a speaker says off the record.",TINT,NAVY2,NAVY,9.6,500,align="start")
    return svg(w,h,s),"Decision tree 2: hearing something that might be confidential or inside information. <b>Sources:</b> Criminal Justice Act 1993 Part V [S343]; UK Market Abuse Regulation Arts 10 and 14 [S344]; SRA Code of Conduct for Solicitors para 6.3 [S342]. See Part 6 and the source table [Confirmed for the law; tree is Inferred]."

# ---------- Part 5/6: industry and regulation ----------
@fig("pyramid")
def _():
    w,h=760,330
    s=""
    levels=[("Equity partners","own the firm, share the profit",NAVY,WHITE),("Non-equity partners and counsel","senior, paid mainly by salary",NAVY2,WHITE),
            ("Senior associates and associates","run the work day to day",BLU,WHITE),("Trainees and paralegals","do the first drafts, checklists, research",ACC,WHITE)]
    cx=200; top=10; lh=64
    for i,(t,sub,c,tc) in enumerate(levels):
        half=40+i*55; y=top+i*lh
        nh=40+(i+1)*55
        s+=f'<path d="M{cx-half},{y} L{cx+half},{y} L{cx+nh},{y+lh-4} L{cx-nh},{y+lh-4} Z" fill="{c}"/>'
        s+=text(cx,y+26,t,10.5,tc,"middle",700,maxw=2*half+40)
        s+=text(cx,y+44,sub,8.8,tc,"middle",400)
    x0=440
    s+=box(x0,10,320,70,"Revenue = hours billed × hourly rate × realisation",TINT,NAVY,NAVY,11,700,sub="(realisation = share of recorded time actually paid)")
    s+=arrow(x0+160,80,x0+160,100)
    s+=box(x0,100,320,60,"Profit = revenue − salaries, rent, tech, insurance",TINT,NAVY,NAVY,11,700)
    s+=arrow(x0+160,160,x0+160,180)
    s+=box(x0,180,320,64,"PEP = profit ÷ number of equity partners",ACCS,ACC,NAVY,11.5,800,sub="Mayer Brown FY2025: $3.196m [S220]")
    s+=box(x0,258,320,62,"Leverage: more people per partner means more billable hours per partner, so more profit per partner",BLUS,BLU,NAVY,9.8,500)
    return svg(w,h,s),"How a law firm makes money: the pyramid and the profit chain. Mayer Brown FY2025 figures from the American Lawyer as reprinted by the firm [S220] <span class='conf c-conf'>Confirmed</span>; the formulas are standard definitions [S212] <span class='conf c-rep'>Reported</span>."

@fig("firm_types")
def _():
    w,h=760,330
    s=""
    cols=[("Magic Circle","London-headquartered elite: Clifford Chance, A&O Shearman, Freshfields, Linklaters, Slaughter and May",NAVY),
          ("US firms in London","Kirkland, Latham, Sidley, White & Case, Mayer Brown (founded Chicago 1881)",ACC),
          ("Transatlantic mergers","A&O Shearman (2024), HSF Kramer (2025), Hogan Lovells Cadwalader and Ashurst Perkins Coie (2026)",SIG),
          ("Global / international","Norton Rose Fulbright, Baker McKenzie, Dentons, DLA Piper",BLU),
          ("Mid-tier, national, boutique","Compete on price or specialism, e.g. Sackers in pensions",GRN)]
    bw=144
    for i,(t,d,c) in enumerate(cols):
        x=i*(bw+10)
        s+=f'<rect x="{x}" y="0" width="{bw}" height="190" rx="7" fill="{c}" fill-opacity="0.1" stroke="{c}" stroke-width="1.5"/>'
        s+=f'<rect x="{x}" y="0" width="{bw}" height="40" rx="7" fill="{c}"/>'
        s+=text(x+bw/2,17,t,10.5,WHITE,"middle",700,maxw=bw-10)
        s+=text(x+8,60,d,9.4,NAVY,maxw=bw-16)
    s+=box(0,206,370,52,"Also selling legal work: barristers (advocates, instructed by solicitors), in-house teams, Big Four legal arms and ALSPs",TINT,GREY,NAVY,9.4,500)
    s+=box(390,206,370,52,"New entrants: AI-native firms (Garfield.Law, SRA-authorised 6 May 2025) and AI vendors (Harvey, Legora)",SIGS,SIG,NAVY,9.4,500)
    s+=text(0,282,"Mayer Brown sits in the US-firm column, but its London office comes from a UK firm (Rowe & Maw, 2002) and its NQ pay matches the Magic Circle.",10,ACC,weight=700,maxw=760)
    return svg(w,h,s),"Who sells commercial legal services in London. Categories are industry convention [Inferred]; examples and dates from [S164][S168][S159][S240] <span class='conf c-rep'>Reported</span>."

@fig("nq_pay")
def _():
    data=[("Quinn Emanuel",189000),("Paul Weiss / Davis Polk",180000),("Sidley, Kirkland, W&C",175000),("Latham",173077),("Ropes & Gray",170000),
          ("Mayer Brown",150000),("Magic Circle",150000),("Baker McKenzie",150000),("Hogan Lovells Cadwalader",145000),("Norton Rose Fulbright",140000),("Legal Cheek average",119000)]
    return hbar(data,unit="",valfmt="£{:,.0f}",hl=("Mayer Brown",),labw=200,maxv=200000), "London newly qualified (NQ) solicitor salaries, latest reported, mid to late 2026. <b>Sources:</b> Legal Cheek NQ table, Sep 2026 [S120]; Legal Cheek 21 Jul 2026 [S235]; Paul Weiss/Davis Polk/Ropes figures [S168][S171] <span class='conf c-rep'>Reported</span>. Pay changes often; re-check before quoting."

@fig("sqe_route")
def _():
    w,h=760,250
    s=""
    steps=[("Degree","any subject",TINT),("PGDL","non-law only; Mayer Brown grant £15k",BLUS),("SQE1","two multiple-choice exams (FLK1, FLK2)",BLUS),("SQE2","practical skills: drafting, advocacy, interviewing",BLUS),("Training contract","two years = QWE; four 6-month seats",ACCS),("Admission","solicitor of England and Wales",GRNS)]
    bw=116
    for i,(t,d,c) in enumerate(steps):
        x=i*(bw+12)
        s+=box(x,20,bw,96,t,c,NAVY,NAVY,11.5,800,sub=d,subfs=9)
        if i<5: s+=arrow(x+bw+1,68,x+bw+11,68,NAVY)
    s+=f'<rect x="{bw+12}" y="128" width="{3*bw+24}" height="26" rx="5" fill="{ACC}" fill-opacity="0.15"/>'
    s+=text(bw+12+(3*bw+24)/2,145,"At Mayer Brown: done before the TC, at BPP, SQE grant £20k [S2]",10,ACC,"middle",700)
    s+=text(0,186,"Key dates: SQE introduced 1 Sep 2021 [S152]. LPC-route candidates must apply for admission by 31 Dec 2032 [S150].",10,NAVY,weight=600)
    s+=text(0,204,"July 2026 SQE1 pass rate: 42% overall, 47% first time [S155]. 2026/27 fees: SQE1 £2,006, SQE2 £3,086 [S158].",10,NAVY,weight=600)
    s+=text(0,222,"QWE: two years full-time equivalent, confirmed by a solicitor [S151]. Character and suitability checks also apply.",10,NAVY,weight=600)
    return svg(w,h,s),"How you qualify as a solicitor in England and Wales today, and where Mayer Brown fits in. <span class='conf c-conf'>Confirmed</span> for SRA dates [S150][S151][S152]; firm funding from the firm's training contract page [S2]; pass rate and fees <span class='conf c-rep'>Reported</span> [S155][S158]."

@fig("securitisation_how")
def _():
    w,h=760,330
    s=""
    s+=box(0,60,150,80,"Originator (e.g. a bank or car lender)",BLUS,NAVY,NAVY,10.5,700,sub="has a pool of loans")
    s+=box(230,60,170,80,"SPV (special purpose vehicle)",ACCS,ACC,NAVY,10.5,800,sub="a company that only owns the loans")
    s+=box(500,20,120,46,"Senior notes",GRNS,GRN,NAVY,10,700,sub="safest, lowest yield",subfs=8.5)
    s+=box(500,76,120,46,"Mezzanine",AMBS,AMB,NAVY,10,700,sub="middle",subfs=8.5)
    s+=box(500,132,120,46,"Junior / equity",REDS,RED,NAVY,10,700,sub="first loss",subfs=8.5)
    s+=box(650,60,110,80,"Investors",TINT,NAVY,NAVY,10.5,700,sub="insurers, funds, banks")
    s+=arrow(150,85,230,85,NAVY,label="sells loans",fs=9,loff=(0,-6))
    s+=arrow(230,115,150,115,GRN,label="pays cash",fs=8.5,loff=(0,14))
    s+=arrow(400,100,500,43,NAVY); s+=arrow(400,100,500,99,NAVY); s+=arrow(400,100,500,155,NAVY)
    s+=arrow(620,100,650,100,NAVY)
    s+=box(0,190,150,46,"Borrowers keep paying",TINT,GREY,NAVY,9.5,600)
    s+=arrow(75,190,75,140,GREY)
    s+=box(230,190,170,46,"Servicer collects and passes cash on",TINT,GREY,NAVY,9.5,600)
    s+=arrow(315,190,315,140,GREY)
    s+=box(0,254,760,70,"What the lawyers do: check the sale is a true sale (the loans are safe if the originator goes bust), draft the transaction documents, apply the UK Securitisation Regulations 2024 (5% risk retention, due diligence, transparency), get ratings and listing right. Regulators consulted on loosening these rules on 17 Feb 2026 [S194].",SIGS,SIG,NAVY,9.8,500,align="start")
    return svg(w,h,s),"How a securitisation works, from zero. Mechanics are standard market structure [Inferred]; UK rules from SI 2024/102 [S192] and the 2026 reform consultation as summarised by Mayer Brown [S194] <span class='conf c-conf'>Confirmed</span>."

@fig("buyin_how")
def _():
    w,h=760,250
    s=""
    s+=box(0,30,170,80,"Employer",TINT,NAVY,NAVY,11,700,sub="sponsors a final salary scheme")
    s+=box(260,30,200,80,"Pension scheme trustees",BLUS,BLU,NAVY,11,700,sub="owe members their pensions")
    s+=box(560,30,200,80,"Insurer (e.g. Royal London)",ACCS,ACC,NAVY,11,700,sub="takes on the longevity and investment risk")
    s+=arrow(170,70,260,70,NAVY,label="funds",fs=9)
    s+=arrow(460,55,560,55,GRN,label="lump-sum premium",fs=9)
    s+=arrow(560,90,460,90,NAVY,label="policy that pays the pensions",fs=9,loff=(0,16))
    s+=box(0,140,370,96,"Buy-in: the policy is an asset of the scheme. Buy-out: members become the insurer's policyholders and the scheme can wind up.",TINT,GREY,NAVY,9.8,500,align="start")
    s+=box(390,140,370,96,"Market: 2025 record 367 buy-ins, £38.2bn [S201]; H1 2026 £10.2bn [S237]. Mayer Brown advised Royal London on £213m (Jan 2026) and £208m (Jul 2026) deals [S223][S224]. Pension Schemes Act 2026, Royal Assent 29 Apr 2026 [S200].",ACCS,ACC,NAVY,9.6,500,align="start")
    return svg(w,h,s),"How a pension buy-in works, and why it is London work for Mayer Brown. Market figures from LCP [S201] and Hymans Robertson via Pensions Age [S237] <span class='conf c-conf'>Confirmed</span>; Mayer Brown deals from firm releases."

@fig("reg_timeline")
def _():
    ev=[("25 Nov 2019","SRA Standards and Regulations replace the SRA Handbook [S154]",False),
        ("1 Sep 2021","SQE introduced; first SQE1 sat Nov 2021 [S152]",True),
        ("26 Oct 2023","Economic Crime and Corporate Transparency Act 2023: Royal Assent [S205]",False),
        ("29 Jan 2024","Securitisation Regulations 2024 (SI 2024/102) made [S192]",False),
        ("Jul 2024","Virgin Media v NTL [2024] EWCA Civ 843: pension amendments void without actuarial confirmation [S214]",False),
        ("30 Sep 2024","UK EMIR Refit reporting live; final synthetic USD LIBOR published, LIBOR ends [S196][S197]",False),
        ("1 Nov 2024","New UK securitisation regime in force [S192][S193]",True),
        ("6 May 2025","SRA authorises Garfield.Law, first AI-driven law firm [S159]",False),
        ("1 Sep 2025","Failure to prevent fraud offence in force [S203]",False),
        ("4 Dec 2025","Bank of England launches private markets stress exercise [S208]",False),
        ("20 Jan 2026","PRA PS1/26: Basel 3.1 final rules [S190]",False),
        ("17 Feb 2026","FCA CP26/6 and PRA CP2/26: securitisation reform consultation (closed 18 May) [S194]",True),
        ("29 Apr 2026","Pension Schemes Act 2026: Royal Assent; Virgin Media fix in force [S200]",True),
        ("H2 2026","FCA final securitisation rules expected (not confirmed published by 8 Oct) [S194]",False),
        ("1 Jan 2027","Basel 3.1 takes effect [S190]",True),
        ("Q2 2027","PRA securitisation changes anticipated [S194]",False),
        ("1 Jan 2028","Market risk internal models (FRTB-IMA) take effect [S190]",False),
        ("2028","Permanent DB superfund regime expected [S200]",False),
        ("31 Dec 2032","Last date to apply for admission via the LPC route [S150]",False)]
    return timeline(ev,label_w=110),"The regulation timeline for a trainee at Mayer Brown London: how solicitors qualify, and the rules shaping the firm's core finance and pensions work. Highlighted rows matter most. <span class='conf c-conf'>Confirmed</span> where the source is primary; see Part 15."

@fig("basel_chain")
def _():
    w,h=760,150
    s=""
    items=[("Basel 3.1 live 1 Jan 2027","PRA PS1/26 [S190]",NAVY),("Banks need more capital per loan","",BLU),("Banks transfer credit risk","SRT, synthetic securitisation",ACC),("Lawyers structure and document the trades","Mayer Brown: GlobalCapital SRT Law Firm of the Year 2026 [S148]",SIG)]
    bw=176
    for i,(t,d,c) in enumerate(items):
        x=i*(bw+18)
        s+=box(x,10,bw,110,t,c,c,WHITE,11,700,sub=d if d else None,subfs=9)
        if i<3: s+=arrow(x+bw+1,65,x+bw+17,65,NAVY)
    return svg(w,h,s),"From a bank capital rule to legal work: why Basel 3.1 matters to Mayer Brown. Chain of reasoning is the author's [Inferred]; dates and award from [S190][S148]."

@fig("shift_map")
def _():
    w,h=760,420
    s=text(0,14,"Force",11,NAVY,weight=800)+text(260,14,"What it does to law firms",11,NAVY,weight=800)+text(540,14,"What it means at Mayer Brown",11,ACC,weight=800)
    rows=[("Generative AI","Fewer junior hours on first drafts and review; clients expect firms to use it [S167]","GenAI curriculum for ~1,800 lawyers, Harvey and Copilot [S230]"),
          ("Transatlantic mergers","Bigger platforms; rivals gain scale [S240]","Grows by lateral teams, not merger [S220]"),
          ("US firms' London growth","US firms grew London revenue 14.7% vs 7.1% for UK firms [S168]","London revenue up 20.5% in 2025 [S222]"),
          ("Pay war","NQ pay £140k-£189k; costs rise [S120]","£150k NQ, Magic Circle level [S234]"),
          ("Private credit boom","Lending moves from banks to funds; regulators watch [S208]","Private credit cited as a London growth driver [S220]"),
          ("Bank capital rules","Basel 3.1 from 1 Jan 2027 [S190]","Risk transfer and securitisation work [S148]"),
          ("Pensions endgame","Record buy-ins; Pension Schemes Act 2026 [S200][S201]","Insurer-side buy-in work [S223]"),
          ("Clients buy judgement","\"Expertise is the price of entry\" [S167]","\"Go deeper with fewer clients\" [S220]")]
    rh=48
    for i,(a,b,c) in enumerate(rows):
        y=26+i*rh
        s+=f'<rect x="0" y="{y}" width="{w}" height="{rh-6}" rx="5" fill="{TINT if i%2==0 else WHITE}"/>'
        s+=text(8,y+25,a,10.5,NAVY,weight=700)
        s+=text(260,y+17,b,9.4,NAVY,maxw=260)
        s+=text(540,y+17,c,9.4,ACC,weight=600,maxw=215)
        s+=arrow(225,y+20,252,y+20,GREY,1.2)+arrow(512,y+20,534,y+20,GREY,1.2)
    return svg(w,h,s),"The industry shift map: eight forces, what they do to law firms, and Mayer Brown's position on each. Each cell is sourced; the links between columns are the author's reasoning [Inferred]."

@fig("news_map")
def _():
    w,h=760,330
    groups=[("Mayer Brown itself",NAVY,["1 New London MP, 1 Oct 2026","2 FY2025: $2.17bn, PEP $3.196m","3 Lateral team hires","4 Royal London buy-ins","5 GenAI curriculum","6 Nigeria ports; AI loan"]),
            ("Legal sector",SIG,["7 NQ pay: £150k benchmark","8 Transatlantic mergers","9 SQE1 pass rate 42%"]),
            ("Markets",ACC,["10 Securitisation reform; private credit","11 Bank Rate 3.75%, 6-3","12 Basel 3.1; London IPOs"])]
    s=""; bw=242
    for i,(t,c,items) in enumerate(groups):
        x=i*(bw+17)
        s+=f'<rect x="{x}" y="0" width="{bw}" height="34" rx="6" fill="{c}"/>'+text(x+bw/2,22,t,12,WHITE,"middle",800)
        for j,it in enumerate(items):
            y=44+j*46
            s+=f'<rect x="{x}" y="{y}" width="{bw}" height="38" rx="6" fill="{c}" fill-opacity="0.09" stroke="{c}"/>'
            s+=text(x+10,y+24,it,10.4,NAVY,weight=600)
    s+=f'<rect x="{bw+17}" y="196" width="{2*bw+17}" height="120" rx="6" fill="{TINT}"/>'
    s+=text(bw+27,218,"The common thread",11,NAVY,weight=800)
    s+=text(bw+27,238,"Finance-led growth (stories 2, 3, 10, 12), a firm choosing focus over merger (2, 8), and AI changing junior work (5, 9). Rates and energy (11) touch every practice. Re-check 7, 8, 10, 11 in the week before 2 Nov.",10,NAVY,maxw=2*bw-10)
    return svg(w,h,s),"Twelve stories, April to October 2026, grouped. Details and sources on the cards that follow [S220]-[S244]."

# ---------- Part 2: the firm as a business ----------
@fig("money_flow", full=True)
def _():
    w,h=760,1000
    s=text(0,18,"Global firm, calendar 2025 (American Lawyer figures, reprinted by the firm)",13,NAVY,weight=800)
    s+=box(0,34,760,70,"Clients: banks, funds, insurers, pension schemes, corporates",BLUS,BLU,NAVY,13,800,sub="6,316 clients billed in 2025, down from 7,600: \"go deeper with fewer clients\" [S220]")
    s+=arrow(380,104,380,134,NAVY,2.5,label="fees: about 2.8m billed hours at rates up >10%",fs=10,loff=(150,4))
    s+=box(180,134,400,70,"Revenue $2.17bn",NAVY,NAVY,WHITE,18,800,sub="+~10%; revenue per lawyer $1.25m [S220]")
    s+=arrow(300,204,150,250,GREY,2,label="costs",fs=10,loff=(-20,0))
    s+=arrow(460,204,610,250,GRN,2.5,label="profit",fs=10,loff=(20,0))
    s+=box(0,250,300,120,"Costs ≈ $1.41bn (inferred: revenue minus net income)",TINT,GREY,NAVY,12,700,sub="associates and counsel, non-equity partners (pool $324.7m in FY2024 [S72]), business services staff, rent, technology, insurance",subfs=9.5)
    s+=box(460,250,300,120,"Net income $762.5m",GRNS,GRN,NAVY,15,800,sub="+19.2% [S220]; about 35% of revenue (inferred)")
    s+=arrow(610,370,610,400,GRN,2.5)
    s+=box(460,400,300,90,"÷ about 239 equity partners",GRNS,GRN,NAVY,13,700,sub="= PEP $3.196m (+14.5%) [S220]")
    s+=box(0,400,420,90,"Leverage: about 1,736 lawyers (inferred: $2.17bn ÷ $1.25m) for 239 equity partners, so roughly 86% of lawyers are not equity partners",ACCS,ACC,NAVY,10.5,600)
    s+=f'<line x1="0" y1="520" x2="760" y2="520" stroke="{LINE}" stroke-width="2" stroke-dasharray="6 4"/>'
    s+=text(0,550,"The English entity: Mayer Brown International LLP, year to 30 April 2025 (audited accounts at Companies House)",13,NAVY,weight=800)
    s+=box(180,566,400,64,"Turnover £185.7m",NAVY,NAVY,WHITE,17,800,sub="up from £163.3m (+13.7%) [S78]")
    s+=arrow(260,630,110,680,GREY,2); s+=arrow(380,630,380,680,GREY,2); s+=arrow(500,630,650,680,GRN,2.5)
    s+=box(0,680,220,80,"Staff costs £62.8m",TINT,GREY,NAVY,12,700,sub="429 staff: 227 office and management, 202 professional [S78]",subfs=9)
    s+=box(270,680,220,80,"Other operating costs £43.7m",TINT,GREY,NAVY,12,700,sub="rent, IT, insurance and more [S78]",subfs=9)
    s+=box(540,680,220,80,"Profit for members £79.2m",GRNS,GRN,NAVY,12.5,800,sub="+33%; margin ~43% (inferred)",subfs=9)
    s+=arrow(650,760,650,790,GRN,2.5)
    s+=box(500,790,260,84,"92 members: average £861k; highest £3.38m",GRNS,GRN,NAVY,11.5,700,sub="variable profits allocated on \"the performance of the business and the individual\" [S78]",subfs=8.8)
    s+=box(0,790,470,84,"Why the two halves differ: the LLP covers England and Japan only; \"profit per member\" counts all 92 members, PEP counts equity partners only. Do not compare them directly.",SIGS,SIG,NAVY,10.2,500,align="start")
    s+=box(0,894,760,90,"Estimates on this page: costs, margin, implied lawyer count and leverage are arithmetic from the sourced totals, labelled (inferred). American Lawyer figures are self-reported by the firm and not audited; the LLP accounts are audited by RSM UK Audit LLP [S78].",AMBS,AMB,NAVY,10.2,500,align="start")
    return svg(w,h,s),"How money flows through Mayer Brown: the global firm (top) and its English LLP (bottom). <b>Sources:</b> American Lawyer via mayerbrown.com, 25 Mar 2026 [S220]; Mayer Brown International LLP accounts to 30 Apr 2025, filed 16 Jan 2026 [S78]. <span class='conf c-conf'>Confirmed</span> totals; derived figures marked (inferred)."

@fig("history")
def _():
    ev=[("1881","Adolf Kraus and Levy Mayer form a partnership in Chicago [S70]",False),
        ("1895","Rowe & Maw founded in London: the root of today's London office [S70]",True),
        ("1909","Mayer, Meyer, Austrian & Platt [S70]",False),
        ("1970","Mayer, Brown & Platt; Washington DC office opens [S70]",False),
        ("1998","Merger with Blanchfield Cordle & Moore (Charlotte, North Carolina) [S70]",False),
        ("2001","Mergers with Lambert & Lee (Paris) and Gaedertz (Germany) [S70]",False),
        ("2002","Mayer, Brown & Platt combines with Rowe & Maw: Mayer, Brown, Rowe & Maw [S70]",True),
        ("2007","Name shortened to Mayer Brown [S70]",False),
        ("2008","Combination with Johnson Stokes & Master, Hong Kong (about 260 lawyers) [S87]",False),
        ("2009","Association with Tauil & Chequer, Brazil [S70]",False),
        ("2021","Jon Van Gorp becomes Chair (re-elected June 2024) [S73]",False),
        ("2024","Mexico City closes (Oct); JSM becomes independent again (around Dec) [S70][S72]",True),
        ("2025","Revenue $2.17bn; London revenue +20.5% to a record; 56 lateral partners [S220][S84]",True),
        ("Apr 2026","Firmwide GenAI curriculum [S230]",False),
        ("1 Oct 2026","Chris Harvey becomes London Managing Partner [S222]",True)]
    return timeline(ev,label_w=90),"Growth of the firm over time: the mergers that made Mayer Brown, and the 2024 to 2026 repositioning. <b>Source:</b> the firm's own history page [S70] and dated releases <span class='conf c-conf'>Confirmed</span>. Note: Brown &amp; Wood merged with Sidley in 2001, not with Mayer Brown [S92][S339]."

@fig("rev_bars")
def _():
    w,h=760,250
    s=""
    data=[("FY2023",1.9,2.5),("FY2024",1.98,2.8),("FY2025",2.17,3.196)]
    s+=text(0,16,"Revenue ($bn)",12,NAVY,weight=800)+text(400,16,"Profit per equity partner ($m)",12,NAVY,weight=800)
    for k,(off,idx,mx,col) in enumerate(((0,1,2.4,NAVY),(400,2,3.5,ACC))):
        for i,d in enumerate(data):
            v=d[idx]; bh=160*v/mx; x=off+30+i*110; y=210-bh
            s+=f'<rect x="{x}" y="{y:.1f}" width="70" height="{bh:.1f}" rx="3" fill="{col}"/>'
            s+=text(x+35,y-6,(f"${v:.2f}bn" if idx==1 else f"${v:.2f}m").replace(".90bn",".9bn").replace(".50m",".5m").replace(".80m",".8m"),10.5,NAVY,"middle",700)
            s+=text(x+35,228,d[0],10,GREY,"middle",600)
    s+=text(0,246,"FY2023 figures are the firm's rounded \"$1.9 billion\" and \"nearly $2.5 million\" [S73]; FY2024 [S72]; FY2025 [S220].",9,GREY)
    return svg(w,h,s),"Three years of results: revenue up about 14%, PEP up about 28% (inferred from the figures shown), while billed hours fell. <b>Sources:</b> [S73][S72][S220] <span class='conf c-conf'>Confirmed</span> (self-reported to the American Lawyer)."

@fig("op_model")
def _():
    w,h=760,470
    s=""
    s+=box(0,0,760,70,"CLIENTS: banks, funds and asset managers, insurers, pension trustees, corporates, ISDA",BLUS,BLU,NAVY,12,800,sub="buy: deal documentation, programme counsel, opinions, disputes, regulatory advice",subfs=10)
    s+=arrow(250,70,250,100,NAVY,2,label="instructions, fees",fs=9,loff=(-60,4)); s+=arrow(510,100,510,70,NAVY,2,label="advice, executed deals",fs=9,loff=(70,4))
    s+=f'<rect x="0" y="100" width="760" height="170" rx="8" fill="{ACCS}" stroke="{ACC}"/>'
    s+=text(10,120,"FRONT LINE: London practice groups (fee earners: partners, counsel, associates, trainees)",11,ACC,weight=800)
    pr=["Banking & Finance (9 subgroups)","Structured finance & securitisation","Derivatives","Pensions & insurance","Real estate","Disputes & construction","Corporate, PE, tax, employment"]
    for i,p in enumerate(pr):
        x=10+(i%4)*186; y=132+(i//4)*64
        s+=box(x,y,176,56,p,WHITE,ACC,NAVY,10,700)
    s+=arrow(250,270,250,300,NAVY,2,label="draw services",fs=9,loff=(-55,4)); s+=arrow(510,300,510,270,NAVY,2,label="fund from revenue",fs=9,loff=(65,4))
    s+=f'<rect x="0" y="300" width="760" height="96" rx="8" fill="{TINT}" stroke="{NAVY2}"/>'
    s+=text(10,320,"CENTRE: business services (~227 office and management staff in the LLP [S78])",11,NAVY2,weight=800)
    bs=["Business Intake & Conflicts","Knowledge Management","IT and legal innovation","BD & Marketing","HR and graduate recruitment","Accounting & Analysis","Risk & compliance (COLP, COFA)","Facilities, secretarial, paralegal"]
    for i,b in enumerate(bs):
        x=10+(i%4)*186; y=330+(i//4)*32
        s+=box(x,y,176,26,b,WHITE,GREY,NAVY,8.8,600,rx=4)
    s+=box(0,410,760,54,"CAPITAL AND OWNERSHIP: members' capital \"treated as debt and is repaid in full on retirement\" [S78]; equity partners take the residual profit; global firm is \"associated legal practices that are separate entities\" [S75]",GRNS,GRN,NAVY,9.8,600)
    return svg(w,h,s),"The operating model as layers: clients, the front line, the centre, and capital. Practice list from the firm and Chambers Student [S79][S16]; business services departments from the firm's careers page [S331]; capital terms from the LLP accounts [S78] <span class='conf c-conf'>Confirmed</span>. The arrows are the author's simplification [Inferred]."

@fig("contracts")
def _():
    w,h=760,300
    rows=[("Equity partners","Bring and keep clients; supervise; put in capital","Share of residual profit; banded pay with \"more room at the top\" [S72]",NAVY),
          ("Clients","Instructions, fees at rates up >10% in 2025","Specialist, cross-border execution; fewer clients, deeper service [S220]",BLU),
          ("Associates and counsel","Billable work, supervision of juniors","Salary (NQ £150k), training, partner track [S234]",ACC),
          ("Trainees","Two years of work across four seats","£56k/£61k, SQE funding, a route to NQ (80% retention) [S2][S16]",SIG),
          ("Business services","Intake, conflicts, KM, IT, BD, HR, finance","Salary; career in a professional firm [S331]",GRN)]
    s=text(130,14,"Gives",11,NAVY,weight=800)+text(450,14,"Gets",11,NAVY,weight=800)
    for i,(a,b,c,col) in enumerate(rows):
        y=24+i*54
        s+=box(0,y,120,46,a,col,col,WHITE,10,700)
        s+=box(130,y,300,46,b,TINT,LINE,NAVY,9.4,500)
        s+=arrow(432,y+23,446,y+23,GREY,1.4)
        s+=box(450,y,310,46,c,TINT,LINE,NAVY,9.4,500)
    return svg(w,h,s),"The \"contracts\" the business is made of: what each group gives and gets. Each cell sourced as marked; the framing is the author's [Inferred]."

@fig("risk_arch")
def _():
    w,h=760,250
    steps=[("New client or matter","",BLUS),("KYC and anti-money laundering checks","Money Laundering Regulations 2017",BLUS),("Conflicts search","SRA Code for Firms 6.2",AMBS),("Engagement letter","scope, fees, complaints route",BLUS),("Work under supervision","Code 3.5; information barriers 6.5",ACCS),("Billing and file closure","client money rules 5.2",GRNS)]
    s=""; bw=116
    for i,(t,d,c) in enumerate(steps):
        x=i*(bw+12)
        s+=box(x,10,bw,92,t,c,NAVY,NAVY,10.2,700,sub=d if d else None,subfs=8.6)
        if i<5: s+=arrow(x+bw+1,56,x+bw+11,56,NAVY)
    s+=box(0,122,370,116,"Who sets the limits: the SRA (rules), the firm's COLP and COFA (compliance officers who must take \"all reasonable steps\" [S110]), the General Counsel and risk team, and the insurer: professional indemnity cover from Liberty Mutual Insurance Europe, worldwide [S76].",TINT,NAVY2,NAVY,9.6,500,align="start")
    s+=box(390,122,370,116,"What happens on a breach: report to the SRA if serious (Code 7.7), notify insurers, fix and record. The firm's history shows why this exists: Refco (2005) and the GM filing error (2008). See \"Skeletons\" below.",REDS,RED,NAVY,9.6,500,align="start")
    return svg(w,h,s),"The risk and control architecture of a law firm: the life of a matter through the controls. Rules from the SRA Code of Conduct for Firms [S110] and for Solicitors [S342]; insurer from the firm's legal notices [S76] <span class='conf c-conf'>Confirmed</span>. Sequence is standard practice [Inferred]."

@fig("leadership")
def _():
    w,h=760,330
    s=""
    s+=box(260,0,240,52,"Chair: Jon Van Gorp",NAVY,NAVY,WHITE,12,800,sub="since 2021; structured finance background [S73]",subfs=9)
    s+=arrow(380,52,380,72)
    s+=box(120,72,520,52,"Management Committee: Frederick Fisher, Dominic Griffiths (London), Matthew Ingber, Britt Miller, Lauren Pryor, Eric Reilly; CFO ex officio [S74]",NAVY2,NAVY2,WHITE,9.6,600)
    s+=arrow(250,124,130,154); s+=arrow(380,124,380,154); s+=arrow(510,124,630,154)
    s+=box(0,154,250,62,"Managing Partner: Jeremy Clay",BLUS,BLU,NAVY,11,700,sub="also a designated member of the English LLP [S78]",subfs=8.8)
    s+=box(270,154,220,62,"C-suite",BLUS,BLU,NAVY,11,700,sub="COO Brian Schare; CIO Evette Pastoriza Clift; CCO Michelle Stokes; CTPO Erica Murphy [S74]",subfs=8.4)
    s+=box(510,154,250,62,"London Managing Partner: Chris Harvey",ACCS,ACC,NAVY,11,800,sub="from 1 Oct 2026; real estate [S222]",subfs=8.8)
    s+=arrow(635,216,635,244)
    s+=box(510,244,250,76,"London practice heads, graduate recruitment, training principal (Miriam Bruce [S16])",ACCS,ACC,NAVY,9.6,600)
    s+=box(0,244,490,76,"Business services leadership groups (careers page): Accounting & Analysis, BD & Marketing, Business Intake & Conflicts, Facilities, HR, IT, Knowledge Management, Paralegal, Secretarial [S331]",TINT,GREY,NAVY,9.4,500,align="start")
    return svg(w,h,s),"The centre as the firm publishes it: leadership and business services groupings, as at 8 Oct 2026. <b>Sources:</b> firm leadership page [S74], careers page [S331], release of 28 Sep 2026 [S222] <span class='conf c-conf'>Confirmed</span>."

@fig("skeletons")
def _():
    ev=[("2005","Refco collapses; Mayer Brown partner Joseph Collins was its primary outside counsel [S94]",True),
        ("2008","GM closing papers wrongly include termination of a $1.5bn term loan's security filing [S102]",False),
        ("Nov 2012","Collins convicted at retrial on 7 of 10 counts (first conviction vacated Jan 2012) [S94][S96]",False),
        ("Jun 2013","Firm settles with Refco trustee for an undisclosed sum [S99]",False),
        ("Jul 2013","Collins sentenced to one year and one day [S95]",False),
        ("2015","2nd Circuit: the GM term loan security was terminated [S103]",False),
        ("Jun 2017","7th Circuit: Mayer Brown owed the lenders no duty; their suit fails [S102]",True),
        ("Oct 2021","Firm stops acting for Hong Kong University on 'Pillar of Shame' statue removal after criticism [S111]",False),
        ("Aug 2026","Documents mistakenly sent to an impostor; firm says its systems were not accessed [S105]",False)]
    return timeline(ev,label_w=80),"The skeletons, told straight. <b>Sources:</b> US Department of Justice releases [S94][S95]; court rulings [S102][S103]; press [S96][S99][S105][S111]. <span class='conf c-conf'>Confirmed</span> for court and DOJ facts; others <span class='conf c-rep'>Reported</span>."

# ---------- Part 1: the role and the team ----------
@fig("funnel")
def _():
    w,h=760,400
    st=[("SEO application","closes 26 Oct 2026, 11:59pm (may close early) [S340]",True),
        ("Masterclass, 2 Nov 2026","60 SEO candidates, 2pm to 6pm, London [S340]",True),
        ("Vacation scheme application","opened 1 Sep, closes 4 Dec 2026 [S1]",False),
        ("Immersive Assessment","behavioural, numerical and verbal reasoning, 4 video questions; benchmark scores [S1][S17]",False),
        ("Assessment centre","Jan to Feb 2027, London: written, group, fact-find, interview [S1][S2]",False),
        ("Vacation scheme","30 places; spring 12-23 Apr, summer 21 Jun-2 Jul 2027 [S17][S13]",False),
        ("Training contract offer","about 15 a year from about 3,500 applications [S18]; starts 2029",False)]
    s=""
    for i,(t,d,me) in enumerate(st):
        y=i*54; inset=i*26; bw=w-2*inset-0
        c=ACC if me else NAVY
        s+=f'<path d="M{inset},{y} L{w-inset},{y} L{w-inset-26},{y+48} L{inset+26},{y+48} Z" fill="{c}" fill-opacity="{0.95-i*0.08 if not me else 1}"/>'
        s+=text(w/2,y+20,t,11.5,WHITE,"middle",800)
        s+=text(w/2,y+37,d,9,WHITE,"middle",500)
    s+=text(w-110,30,"YOU ARE HERE",10,ACC,"middle",800)
    s+=f'<polygon points="{w-40},{60} {w-30},{75} {w-50},{75}" fill="{ACC}"/>'
    return svg(w,h,s),"The process funnel, with your position marked (orange). The masterclass sits about one month before the vacation scheme deadline; the firm calls vacation schemes \"the main pipeline\" for training contracts [S17]. <span class='conf c-conf'>Confirmed</span> dates from the firm [S1][S2] and the event page [S340]; numbers <span class='conf c-rep'>Reported</span>."

@fig("value_chain")
def _():
    w,h=760,250
    st=[("Client need","a bank wants a loan documented",BLUS),("Partner","wins and scopes the matter; owns the advice",NAVY),("Associate","plans the work; drafts the main documents",BLU),
        ("Trainee","CP checklist, ancillaries, research, diligence, notes",ACC),("Review","associate checks; partner signs off (Code 3.5)",SIGS),("Outcome","signed, closed, filed; client billed",GRNS)]
    s=""; bw=116
    for i,(t,d,c) in enumerate(st):
        x=i*(bw+12); tc=WHITE if c in (NAVY,BLU,ACC) else NAVY
        s+=box(x,10,bw,110,t,c,NAVY,tc,12,800,sub=d,subfs=9)
        if i<5: s+=arrow(x+bw+1,65,x+bw+11,65,NAVY)
    s+=path_arrow("M 572 125 C 572 175, 445 175, 445 125",ACC,1.6,dash=True)
    s+=text(508,190,"feedback, corrections",9.5,ACC,"middle",700)
    s+=box(0,205,760,40,"Where a trainee adds value: accuracy on the detail, a clean record of what's outstanding, and telling people early when something is wrong.",TINT,GREY,NAVY,10,600)
    return svg(w,h,s),"The role's value chain: from a client's need to a closed deal, and where the trainee sits. Trainee tasks from a Mayer Brown finance trainee's account [S18] and Chambers Student [S16] <span class='conf c-rep'>Reported</span>; supervision rule from the SRA Code para 3.5 [S12]."

@fig("channels")
def _():
    w,h=760,300
    s=""
    s+=box(0,0,370,40,"Transactional (non-contentious) seats",NAVY,NAVY,WHITE,12,800)
    s+=box(390,0,370,40,"Contentious seats (max two)",SIG,SIG,WHITE,12,800)
    L=["Banking & Finance: 9 subgroups incl. leveraged finance, securitisation, trade and emerging markets, receivables [S16]","Corporate and securities; private equity","Real estate: Land Registry, SDLT, leases [S16]","Pensions, employment, tax, competition, IP/IT [S17][S25]"]
    R=["Commercial dispute resolution: disclosure, research, bundles [S16]","Construction litigation: chronologies, document management [S16]","International arbitration (Paris secondment) [S16]","Restructuring sits between the two"]
    for i,t in enumerate(L): s+=box(0,50+i*50,370,44,t,TINT,LINE,NAVY,9.6,500,align="start")
    for i,t in enumerate(R): s+=box(390,50+i*50,370,44,t,SIGS,LINE,NAVY,9.6,500,align="start")
    s+=box(0,256,760,40,"Rule: at least one transactional seat; contentious seats capped at two; rank up to five choices each rotation; business need decides [S16]",ACCS,ACC,NAVY,10,700)
    return svg(w,h,s),"The two channels through which a trainee's work is done, and the seat rules. <b>Sources:</b> Chambers Student 2027 review [S16]; LawCareers.Net [S17]; Bright Network [S25] <span class='conf c-rep'>Reported</span>."

@fig("day")
def _():
    rows=[("8:30","Emails on the phone before arriving; arrive about 9am [S18]"),
          ("9:30","Update CP checklists on live deals; chase signatories and local counsel [S18]"),
          ("11:00","Training session; early in a seat \"you are almost always training every day\" [S16]"),
          ("12:30","Lunch; office attendance 60% with anchor days [S16]"),
          ("14:00","Draft ancillaries: NDAs, powers of attorney, resolutions, notices of security [S18]"),
          ("16:00","Client call: take the note, circulate within the hour [S16]"),
          ("17:30","Review associate's comments; turn the draft [S16]"),
          ("18:30-19:30","Leave; \"often logs back on from home\" [S18]; survey average finish 8:20pm [S15]")]
    return timeline([(a,b,False) for a,b in rows],label_w=90),"A worked day in a Banking &amp; Finance seat. Built from one Mayer Brown trainee's published account [S18], Chambers Student [S16] and Legal Cheek's 2026 hours survey (average 9:26am to 8:20pm) [S15] <span class='conf c-rep'>Reported</span>; the hour-by-hour layout is [Inferred]. Around a signing or closing it runs much later."

@fig("orgchart")
def _():
    w,h=760,520
    s=""
    def b(x,y,ww,hh,t,conf,sub=None,fs=9.6):
        col={"c":GRN,"r":AMB,"i":SIG}[conf]; fill={"c":GRNS,"r":AMBS,"i":SIGS}[conf]
        return box(x,y,ww,hh,t,fill,col,NAVY,fs,700,sub=sub,subfs=8.2,sw=1.6)
    s+=b(250,0,260,44,"Chair: Jon Van Gorp","c",sub="global; Management Committee incl. Griffiths, Harvey")
    s+=arrow(380,44,380,62)
    s+=b(230,62,300,48,"London Managing Partner: Chris Harvey","c",sub="from 1 Oct 2026; Real Estate co-leader [S222][S64]")
    s+=arrow(380,110,380,128)
    s+=f'<line x1="60" y1="128" x2="700" y2="128" stroke="{GREY}" stroke-width="1.4"/>'
    groups=[("Banking & Finance","c","Alex Dell (global co-head) [S66]; ABL, trade, receivables; securitisation: Griffiths, McGarry, O'Connor; lev fin: Butler, Miles, Mathews, Bierwirth, Goodwin [S55][S68]"),
            ("Derivatives & Structured Products","c","Edmund Parker (leader) [S67]; Nanak Keswani [S55]"),
            ("Real Estate","c","Harvey, Jeremy Clay, Iain Roberts, Caroline Humble, Rajbenbach [S55]"),
            ("Construction & Disputes","r","Sally Davies, Sarkodie, Stone, Morris; Ian McDonald, Abu-Manneh [S55]"),
            ("Corporate / PE","i","James West (reported PE head) [S280]; Ball-Dodd, Agar, Evans [S55]"),
            ("Employment, Pensions, Insurance","r","Miriam Bruce, C Fisher; Doraisamy, Watson; Scagell, Shah; MacAulay [S55][S313]")]
    for i,(t,cf,sub) in enumerate(groups):
        x=(i%3)*258; y=140+(i//3)*120
        s+=arrow(x+120,128,x+120,140,GREY,1.2,head=False)
        s+=b(x,y,244,108,t,cf,sub=sub,fs=10.2)
    s+=b(0,390,370,70,"Training Principal: Miriam Bruce","c",sub="partner, Employment; trainee 2005, partner 2020 [S62][S63]",fs=10.5)
    s+=b(390,390,370,70,"Graduate Recruitment & Development","r",sub="Coordinator Kieran Bennett [S61]; Manager role advertised Mar 2026 (holder unknown) [S297]",fs=10.5)
    s+=legend([("Confirmed",GRN),("Reported",AMB),("Inferred / thin",SIG)],0,490,9.5,160)
    s+=text(500,494,"Headcount estimate: ~264 lawyers; ~520-560 people",9.5,NAVY,weight=700)
    return svg(w,h,s),"The reconstructed London org chart, colour-coded by confidence. No official chart is published. Built from Legal 500 UK 2027 individual rankings [S55], firm releases and bios [S62]-[S68][S222], Companies House [S41] and directories [S61]. Practice \"lead\" labels are confirmed only for Harvey, Dell, Parker and Griffiths; the rest are inferred from rankings."

@fig("hub")
def _():
    w,h=760,300
    s=text(180,16,"Without a centre: every partner chases trainees",11,RED,"middle",800)+text(570,16,"With graduate recruitment as the hub",11,GRN,"middle",800)
    import math
    pts=[(180+110*math.cos(a),150+105*math.sin(a)) for a in [i*2*math.pi/7 for i in range(7)]]
    for i,(x,y) in enumerate(pts):
        for j,(x2,y2) in enumerate(pts):
            if j>i: s+=f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{RED}" stroke-opacity="0.35"/>'
    labs=["B&F","Deriv.","RE","Constr.","Corp","Pens.","Trainees"]
    for (x,y),l in zip(pts,labs): s+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="22" fill="{REDS}" stroke="{RED}"/>'+text(x,y+4,l,9,NAVY,"middle",700)
    pts2=[(570+115*math.cos(a),150+105*math.sin(a)) for a in [i*2*math.pi/6 for i in range(6)]]
    for (x,y),l in zip(pts2,labs[:6]):
        s+=f'<line x1="570" y1="150" x2="{x:.0f}" y2="{y:.0f}" stroke="{GRN}" stroke-width="2"/>'
        s+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="22" fill="{GRNS}" stroke="{GRN}"/>'+text(x,y+4,l,9,NAVY,"middle",700)
    s+=f'<circle cx="570" cy="150" r="42" fill="{GRN}"/>'+text(570,146,"Grad recruitment",8.6,WHITE,"middle",800)+text(570,160,"+ trainees",8.6,WHITE,"middle",700)
    s+=text(380,290,"Mid-seat meetings with graduate recruitment; trainees rank up to five seats; business need decides [S16]",9.5,NAVY,"middle",600)
    return svg(w,h,s),"Why a central function exists: about 15 trainees a year across many practice groups. Without a hub, every group negotiates with every trainee; with one, preferences and business need meet in one place. Mechanism from Chambers Student [S16]; diagram is [Inferred]."

@fig("life_task")
def _():
    w,h=760,190
    st=[("Ask","associate emails a task"),("Clarify","scope, format, deadline, matter number"),("Plan","precedent? who to ask? check-in time"),("Do","draft or research; square-bracket doubts"),("Check","re-read against the instructions"),("Deliver","answer first, then reasoning"),("Record","time to the matter; file note"),("Learn","ask for feedback")]
    s=""; bw=86
    for i,(t,d) in enumerate(st):
        x=i*(bw+9.7)
        c=ACC if t in ("Clarify","Check") else NAVY
        s+=box(x,10,bw,110,t,c,c,WHITE,11.5,800,sub=d,subfs=8.6)
        if i<7: s+=arrow(x+bw+1,65,x+bw+9,65,NAVY,1.2)
    s+=text(380,150,"Orange steps are where most trainee errors are prevented. The GM case (Part 2) is what happens when nobody checks what a document actually does.",9.8,ACC,"middle",700)
    s+=text(380,172,"Time recording: trainees log about 7.2 hours a day with no billable target [S16].",9.6,NAVY,"middle",600)
    return svg(w,h,s),"The life of a request through a trainee. Steps are standard good practice [Inferred]; time-recording norm from Chambers Student [S16] <span class='conf c-rep'>Reported</span>."

@fig("scarce")
def _():
    w,h=760,250
    s=""
    s+=box(0,20,200,70,"Associate A: signing tonight",REDS,RED,NAVY,11,700,sub="needs CP checklist from 6pm")
    s+=box(0,150,200,70,"Associate B: client draft due 9am",REDS,RED,NAVY,11,700,sub="needs research note tonight")
    s+=box(290,85,180,70,"You: one evening",ACC,ACC,WHITE,13,800)
    s+=arrow(200,55,290,105,RED); s+=arrow(200,185,290,135,RED)
    s+=arrow(470,120,540,120,NAVY,2)
    s+=box(540,10,220,64,"1. Tell both, with facts",GRNS,GRN,NAVY,10.5,700,sub="what each needs, by when")
    s+=box(540,84,220,64,"2. They agree, or the person who staffs you decides",GRNS,GRN,NAVY,10,700)
    s+=box(540,158,220,64,"3. Do it; confirm to both; ask for help on the other",GRNS,GRN,NAVY,10,700)
    return svg(w,h,s),"The scarce-resource collision in a trainee seat: your time. Allocation by transparency and escalation, not by saying yes twice. Method is [Inferred]; see composure scenario 1 in Part 11."

@fig("walls")
def _():
    w,h=760,300
    s=""
    s+=f'<rect x="230" y="90" width="300" height="120" rx="10" fill="{ACCS}" stroke="{ACC}" stroke-width="2"/>'+text(380,145,"You, on a client matter",13,NAVY,"middle",800)+text(380,165,"inside the deal team",10,GREY,"middle",500)
    walls=[(0,0,"Other clients' teams","Information barrier where needed (Code for Firms 6.5) [S110]. Nothing crosses without clearance."),
           (530,0,"Friends, family, social media","Confidentiality (Code 6.3) [S342]. Nothing crosses. Not even \"we're busy on a deal\"."),
           (0,220,"Markets","Inside information: no dealing, no tipping (CJA 1993; UK MAR) [S343][S344]."),
           (530,220,"The other side and the court","Only what the client authorises; never mislead (Code 1.4) [S342]. Privileged advice stays in.")]
    for x,y,t,d in walls:
        s+=box(x,y,230,80,t,TINT,NAVY2,NAVY,10.5,800,sub=d,subfs=8.6)
    for (x1,y1,x2,y2) in ((230,120,175,80),(530,120,585,80),(230,190,175,220),(530,190,585,220)):
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{RED}" stroke-width="3" stroke-dasharray="2 3"/>'
    return svg(w,h,s),"The walls around a trainee and what may cross each. <b>Sources:</b> SRA Code of Conduct for Firms 6.5 [S110]; Code for Solicitors 1.4 and 6.3 [S342]; Criminal Justice Act 1993 Part V [S343]; UK MAR [S344] <span class='conf c-conf'>Confirmed</span>."

@fig("laterals")
def _():
    data=[("Leveraged finance / private capital",7),("Private equity",2),("Real estate",2),("Insurance / PRT",1)]
    return hbar(data,labw=230,valfmt="{:.0f}",unit=" partners",maxv=9),"Named hires: leveraged finance: Butler and Miles (Dechert, 2025), Goodwin (Kirkland, 2026), Mathews, Becker and Bierwirth (Baker McKenzie, 2026), Clarke (Baker McKenzie, 2026); PE: Agar (Goodwin, 2025), Evans (Dechert, 2025); real estate: Rajbenbach and Butcher (2026); insurance: MacAulay (from L&amp;G, 2024). What the firm is hiring for: London lateral partner arrivals named in press releases, 2024 to Sep 2026, by practice. <b>Sources:</b> [S68][S69][S280][S282][S313][S226][S227][S228][S229] cross-checked with Companies House [S42] <span class='conf c-rep'>Reported</span>. Firm-wide, 56 lateral partners joined in 2025 [S84]. The count is of named hires found, not a complete list."

# ---------- Part 3/4 ----------
@fig("model_compare")
def _():
    w,h=760,330
    s=""
    s+=box(0,0,370,44,"Mayer Brown London: finance-product depth",ACC,ACC,WHITE,12,800)
    s+=box(390,0,370,44,"Alternative: PE / M&A-led US model (e.g. Kirkland)",NAVY,NAVY,WHITE,12,800)
    L=[("Core client","banks, lenders, insurers, issuers, ISDA [S316]"),("Top rankings","Tier 1: ABL, derivatives, trade finance, real estate occupiers, construction [S139]"),("Growth move","buy in PE / lev fin teams; organic finance [S226][S327]"),("Cohort","~15 trainees, Magic Circle pay [S16][S234]"),("Revenue","$2.17bn global; London $268.2m [S220][S302]")]
    R=[("Core client","private equity sponsors [S131]"),("Top rankings","M&A, private equity, leveraged finance (sponsor side)"),("Growth move","organic plus aggressive laterals"),("Cohort","up to 15 trainees, US pay £175k NQ [S131][S120]"),("Revenue","$10.6bn global [S125]")]
    for i,((a,b),(c,d)) in enumerate(zip(L,R)):
        y=54+i*54
        s+=box(0,y,370,48,"",ACCS,LINE,NAVY)+text(10,y+19,a,9.6,ACC,weight=800)+text(10,y+36,b,9.4,NAVY,maxw=350)
        s+=box(390,y,370,48,"",TINT,LINE,NAVY)+text(400,y+19,c,9.6,NAVY,weight=800)+text(400,y+36,d,9.4,NAVY,maxw=350)
    return svg(w,h,s),"The two models side by side. Mayer Brown London leads in asset-focused finance and is buying into PE; a PE-led firm starts from the sponsor. Sources as marked; Kirkland rankings characterised from public reputation [Inferred] and its Legal Cheek profile [S131]."

@fig("unit_anatomy")
def _():
    w,h=760,330
    s=""
    s+=f'<rect x="200" y="20" width="360" height="210" rx="10" fill="{ACCS}" stroke="{ACC}" stroke-width="2"/>'
    s+=text(380,44,"One practice group: London Banking & Finance",12,NAVY,"middle",800)
    subs=["Leveraged finance","Securitisation","Global trade & emerging markets","Receivables / ABL","Real estate finance","Debt capital markets","Private credit / capital solutions","Restructuring links","(9 subgroups in all)"]
    for i,t in enumerate(subs):
        x=212+(i%3)*116; y=58+(i//3)*52
        s+=box(x,y,108,44,t,WHITE,ACC,NAVY,8.8,600)
    s+=text(380,222,"partners, counsel, associates, ~3-4 trainees at a time [Inferred]",9,GREY,"middle",500)
    left=[("Knowledge lawyers","precedents, know-how"),("Business Intake & Conflicts","new matters"),("IT / legal innovation","Harvey, Copilot")]
    right=[("New York finance","NY-law high yield, US ABS"),("Derivatives team","hedging on deals"),("Local counsel","other jurisdictions")]
    for i,(t,d) in enumerate(left):
        y=20+i*72; s+=box(0,y,170,60,t,TINT,GREY,NAVY,9.6,700,sub=d,subfs=8.4); s+=arrow(170,y+30,200,y+30,GREY)
    for i,(t,d) in enumerate(right):
        y=20+i*72; s+=box(590,y,170,60,t,BLUS,BLU,NAVY,9.6,700,sub=d,subfs=8.4); s+=arrow(590,y+30,560,y+30,BLU,both=True)
    s+=box(0,250,760,70,"Draws from the centre (left): precedents, conflicts clearance, AI tools, BD. Works with other front-line teams (right): \"a fully integrated platform for New York and English law debt and equity solutions\" [S328]; 96 London-New York deals in 2025 [S302].",TINT,NAVY2,NAVY,9.8,500,align="start")
    return svg(w,h,s),"Anatomy of one front-line unit and what it draws from the centre. Subgroups: Chambers Student says nine, including leveraged finance, securitisation, global trade &amp; emerging markets, and receivables [S16]; others from a trainee's account [S18] <span class='conf c-rep'>Reported</span>; private credit and restructuring boxes, and the links, are [Inferred] except where cited."

@fig("pensions_finance")
def _():
    w,h=760,300
    s=""
    teams=[("Pensions","trustee relationships; Andrew Block (relationship partner) [S310]",BLU,0,0),("Insurance","insurer side; Tom MacAulay (hired from L&G, 2024) [S313]",ACC,0,1),
           ("Derivatives","longevity swaps and hedging [S314]",SIG,1,0),("Finance and regulatory","collateral, security, PRA rules [S314]",GRN,1,1)]
    for t,d,c,col,row in teams:
        x=0 if col==0 else 560; y=10+row*130
        s+=box(x,y,200,110,t,c,c,WHITE,12,800,sub=d,subfs=9)
        s+=arrow(x+200 if col==0 else x,y+55,330 if col==0 else 430,150,c,2)
    s+=f'<circle cx="380" cy="150" r="70" fill="{NAVY}"/>'
    s+=text(380,140,"One buy-in",12,WHITE,"middle",800)+text(380,158,"e.g. Ford £4.6bn",10,WHITE,"middle",600)+text(380,174,"Oct 2025 [S310]",9,WHITE,"middle",500)
    s+=text(380,270,"The firm calls its Pensions Finance practice a \"one-stop shop\" [S314]. A firm that had only one of these four teams could not run the deal alone.",10,NAVY,"middle",700,maxw=740)
    return svg(w,h,s),"Why the structure works: a product that needs four teams at once. Ford Pension Schemes £4.6bn buy-in with Legal &amp; General, the largest UK pension risk transfer deal announced in 2025 [S310]; Royal London deals [S223][S312]; practice description [S314]. <span class='conf c-conf'>Confirmed</span> (firm sources)."

@fig("boundary")
def _():
    w,h=760,260
    s=""
    s+=box(0,0,370,40,"Shared freely across practices and offices",GRN,GRN,WHITE,12,800)
    s+=box(390,0,370,40,"Never shared (or only through controls)",RED,RED,WHITE,12,800)
    L=["Precedents and know-how (Knowledge Management) [S331]","Client relationships: a pensions partner can bring in insurance colleagues [S310]","Cross-office teams on one deal: London, New York, Singapore, Dubai [S231]","Training, AI tools and prompt libraries [S230]"]
    R=["Confidential information of one client with a team acting against them (barrier, Code for Firms 6.5) [S110]","Inside information, to anyone outside the deal team [S343][S344]","Matters with a conflict of interest (Code 6.2) [S110]","Personal data beyond what the matter needs"]
    for i,t in enumerate(L): s+=box(0,50+i*50,370,44,t,GRNS,LINE,NAVY,9.4,500,align="start")
    for i,t in enumerate(R): s+=box(390,50+i*50,370,44,t,REDS,LINE,NAVY,9.4,500,align="start")
    return svg(w,h,s),"The boundary between teams: what is shared, what is never shared, and why. Rules from the SRA Code for Firms [S110] and insider dealing law [S343][S344] <span class='conf c-conf'>Confirmed</span>; examples from firm releases."

@fig("client_view")
def _():
    w,h=760,320
    s=""
    rows=[("Bank (derivatives)","ISDA netting opinions; risk participation; SRT notes","ANZ, Barclays, BNP Paribas, JP Morgan, ISDA... [S316]"),
          ("Lender (asset-based lending)","cross-border ABL across England, US, Germany","Santander, Barclays, Citigroup, Wells Fargo... [S318]"),
          ("Issuer / arranger (securitisation)","master trust and auto ABS; CLO platforms","Standard Chartered (with Apollo) [S325]; Capital on Tap deals [S317]"),
          ("Insurer / trustee (pensions)","buy-ins and buy-outs","Royal London; Ford trustees [S310][S312]"),
          ("Contractor (construction)","cladding and fire-safety disputes","Shepherd, Wates, Tamdown [S319]")]
    s+=text(0,14,"Client",11,NAVY,weight=800)+text(220,14,"What they buy",11,NAVY,weight=800)+text(500,14,"Named clients (Legal 500 UK 2027 / firm)",11,NAVY,weight=800)
    for i,(a,b,c) in enumerate(rows):
        y=24+i*58
        s+=f'<rect x="0" y="{y}" width="{w}" height="52" rx="5" fill="{TINT if i%2==0 else WHITE}" stroke="{LINE}"/>'
        s+=text(8,y+30,a,10,NAVY,weight=700,maxw=205)
        s+=text(220,y+22,b,9.6,NAVY,maxw=270)
        s+=text(500,y+22,c,9.2,GREY,maxw=255)
    return svg(w,h,s),"The client's view: who buys what from Mayer Brown London. Named clients are as listed on the Legal 500 UK 2027 pages [S316]-[S319] and firm releases [S310][S312][S325] <span class='conf c-conf'>Confirmed</span>. These clients also instruct rivals; the relationships are not exclusive."

@fig("london_growth")
def _():
    w,h=760,250
    s=""
    s+=box(0,0,240,110,"$268.2m",NAVY,NAVY,WHITE,22,800,sub="London revenue 2025, a record, +20.5% [S302]")
    s+=box(260,0,240,110,"96",ACC,ACC,WHITE,22,800,sub="deals done jointly by London and New York lawyers in 2025 [S302]")
    s+=box(520,0,240,110,"+95%",SIG,SIG,WHITE,22,800,sub="London PE deal volumes in 2025 [S301]")
    s+=box(0,130,240,110,"£185.7m",TINT,NAVY,NAVY,20,800,sub="English LLP turnover, year to Apr 2025, +13.7%; structured finance matters +14.8% [S78][S301]",subfs=9.5)
    s+=box(260,130,240,110,"8",TINT,NAVY,NAVY,20,800,sub="London lateral partner hires in 2025 [S302]")
    s+=box(520,130,240,110,"6,316",TINT,NAVY,NAVY,20,800,sub="clients billed firm-wide in 2025, from 7,600 [S220]")
    return svg(w,h,s),"London's 2024 to 2026 stability and growth in six numbers. <b>Sources:</b> Non-Billable 27 Apr 2026 [S302] and Solicitors Journal 8 May 2026 [S301], both relaying firm figures <span class='conf c-rep'>Reported</span>; Companies House [S78] and American Lawyer [S220] <span class='conf c-conf'>Confirmed</span>."

@fig("people_mix")
def _():
    w,h=760,230
    vals=[("Members (partners)",92,NAVY),("Professional staff",202,ACC),("Office and management",227,GRY) if False else ("Office and management",227,GREY)]
    tot=sum(v for _,v,_ in vals); x=0; s=""
    for lab,v,c in vals:
        bw=760*v/tot
        s+=f'<rect x="{x:.1f}" y="20" width="{bw:.1f}" height="60" fill="{c}"/>'
        s+=text(x+bw/2,56,f"{v}",16,WHITE,"middle",800)
        s+=text(x+bw/2,100,lab,10,NAVY,"middle",700)
        s+=text(x+bw/2,116,f"{100*v/tot:.0f}%",10,GREY,"middle",600)
        x+=bw
    s+=box(0,140,760,80,"Reading: business services are about 44% of everyone in the English LLP, about 0.77 per fee-earner (estimate: 227 ÷ (202 + 92)). Categories are not defined in the accounts; \"professional\" probably includes trainees and paralegals. No peer comparison was available on the same basis.",AMBS,AMB,NAVY,9.8,500,align="start")
    return svg(w,h,s),"Size of the non-fee-earning side: average headcount in Mayer Brown International LLP, year to 30 April 2025. <b>Source:</b> audited accounts, notes 5 and 6 [S78] <span class='conf c-conf'>Confirmed</span>; percentages and ratio are estimates (labelled)."

@fig("wiring")
def _():
    w,h=760,280
    s=""
    s+=box(280,100,200,80,"Practice group (e.g. Banking & Finance)",ACC,ACC,WHITE,11,800)
    items=[(0,0,"Embedded","Paralegals and secretaries in the team; knowledge lawyers per practice [S331]",GRN),
           (0,190,"Connective","Business Intake & Conflicts; BD & Marketing pitches; graduate recruitment for trainee seats [S331]",BLU),
           (560,0,"Utility (firm-wide)","IT, AI tools (Harvey, Copilot) and \"AI Champions\" [S230]; facilities; HR",SIG),
           (560,190,"Control","Risk & compliance, COLP/COFA, accounts and billing [S110][S78]",RED)]
    for x,y,t,d,c in items:
        s+=box(x,y,200,90,t,c,c,WHITE,11,800,sub=d,subfs=8.6)
        s+=arrow(x+100 if x==0 else x+100,y+90 if y==0 else y,380+(-60 if x==0 else 60),100 if y==0 else 180,c,1.8)
    return svg(w,h,s),"How a front-line unit is wired into the centre: embedded, connective, utility and control roles. Department names from the firm's business services careers page [S331] and GenAI release [S230] <span class='conf c-conf'>Confirmed</span>; the four-way classification is [Inferred]. No offshore shared-services centre was found."

@fig("spectrum")
def _():
    ax=[("UK-headquartered","US-headquartered",[("Clifford Chance",0.05),("A&O Shearman",0.18),("NRF",0.35),("Baker McKenzie",0.55),("HLC",0.48),("Mayer Brown",0.72),("Sidley",0.9),("Kirkland",0.98)]),
        ("Magic Circle pay (£150k NQ or less)","US pay (£173k+ NQ)",[("NRF",0.0),("HLC",0.1),("Mayer Brown",0.25),("Clifford Chance",0.3),("Baker McKenzie",0.38),("Latham",0.85),("Sidley",0.93),("Kirkland",1.0)]),
        ("Small cohort (~15)","Large cohort (70-100)",[("Kirkland",0.0),("Mayer Brown",0.06),("Sidley",0.1),("Latham",0.3),("HLC",0.45),("NRF",0.55),("A&O Shearman",0.75),("Clifford Chance",1.0)]),
        ("Finance-product led","PE / M&A led",[("Mayer Brown",0.15),("NRF",0.25),("Clifford Chance",0.4),("A&O Shearman",0.42),("Latham",0.8),("Kirkland",0.97)]),
        ("Grows by lateral teams","Grows by merger",[("Kirkland",0.05),("Mayer Brown",0.15),("Sidley",0.22),("Latham",0.3),("A&O Shearman",0.9),("HLC",0.97)])]
    return spectrum(ax),"The competitive spectrum: five design axes and where each rival sits. Pay and cohort from Legal Cheek profiles and NQ table [S120][S129]-[S137]; merger facts [S126][S174]; finance vs PE positioning from Legal 500 tiers [S141]-[S146]. Firms on the same pay or cohort are spread slightly for legibility. Positions on the finance/PE axis are the author's judgement <span class='conf c-inf'>Inferred</span>."

@fig("peer_scatter")
def _():
    w,h=760,380
    pts=[("Mayer Brown",15,150),("Kirkland",15,175),("Sidley",19,175),("Latham",32,173.077),("Baker McKenzie",40,150),("HLC",45,145),("White & Case",50,175),("NRF",50,140),("A&O Shearman",70,150),("Clifford Chance",100,150)]
    x0,y0,pw,ph=70,20,660,300
    def X(v): return x0+pw*v/110
    def Y(v): return y0+ph-(v-135)/(180-135)*ph
    s=f'<rect x="{x0}" y="{y0}" width="{pw}" height="{ph}" fill="{TINT}"/>'
    for v in (140,150,160,170,180):
        s+=f'<line x1="{x0}" y1="{Y(v):.0f}" x2="{x0+pw}" y2="{Y(v):.0f}" stroke="{LINE}"/>'+text(x0-6,Y(v)+4,f"£{v}k",9,GREY,"end")
    for v in (0,20,40,60,80,100):
        s+=text(X(v),y0+ph+16,str(v),9,GREY,"middle")
    s+=text(x0+pw/2,y0+ph+34,"London trainee intake per year",10,NAVY,"middle",700)
    s+=f'<text x="20" y="{y0+ph/2}" font-size="10" fill="{NAVY}" text-anchor="middle" font-weight="700" transform="rotate(-90 20 {y0+ph/2})">NQ pay</text>'
    offs={"Kirkland":(0,-12),"Sidley":(28,4),"Latham":(0,-12),"White & Case":(0,-12),"NRF":(0,16),"HLC":(0,16),"Baker McKenzie":(0,-12),"A&O Shearman":(0,-12),"Clifford Chance":(-10,-12),"Mayer Brown":(48,4)}
    for n,a,b in pts:
        hl=n=="Mayer Brown"
        s+=f'<circle cx="{X(a):.0f}" cy="{Y(b):.0f}" r="{8 if hl else 6}" fill="{ACC if hl else NAVY}"/>'
        dx,dy=offs.get(n,(0,-12))
        s+=text(X(a)+dx,Y(b)+dy,n,9.5 if not hl else 10.5,ACC if hl else NAVY,"middle",800 if hl else 600)
    s+=f'<rect x="{X(8):.0f}" y="{Y(153):.0f}" width="{X(25)-X(8):.0f}" height="{Y(147)-Y(153):.0f}" fill="none" stroke="{ACC}" stroke-dasharray="4 3"/>'
    return svg(w,h,s),"Size against staffing: trainee intake against NQ pay for Mayer Brown and nine peers. Mayer Brown is alone in the small-cohort, Magic Circle-pay corner. <b>Sources:</b> Legal Cheek profiles and NQ table, Sep 2026 [S120][S121][S129]-[S137]; Chambers Student [S149] <span class='conf c-rep'>Reported</span>. HLC = Hogan Lovells Cadwalader."

@fig("peer_rev")
def _():
    data=[("Kirkland & Ellis",10.556),("Latham & Watkins",8.3),("Sidley Austin",3.74),("A&O Shearman",3.7),("Hogan Lovells Cadwalader",3.6,True),("Baker McKenzie",3.6),("White & Case",3.6),("Clifford Chance",3.5),("Norton Rose Fulbright",2.8),("Mayer Brown",2.17)]
    return hbar(data,valfmt="${:.2f}bn",hl=("Mayer Brown",),labw=210,maxv=11.5),"Global revenue, latest year (mostly FY2025). Mayer Brown is the smallest in this peer set. Hogan Lovells Cadwalader is a combined figure (\"over $3.6bn\") shown dashed as an estimate. <b>Sources:</b> [S122][S125][S126][S129]-[S137] <span class='conf c-rep'>Reported</span>; currency conversions by the outlets."

@fig("unique")
def _():
    w,h=760,400
    U=[("1","Only firm in the peer set top tier in London for both derivatives and asset-based lending","Legal 500 UK 2027 [S142][S144]"),
       ("2","Only US-founded firm in the London derivatives top tier","[S142]"),
       ("3","Six years running GlobalCapital US ABS Law Firm of the Year, plus SRT Law Firm of the Year 2026","[S148]"),
       ("4","Magic Circle pay with a cohort of about 15","[S120][S16]"),
       ("5","A pensions-insurance-derivatives \"one-stop shop\" that ran the largest UK buy-in of 2025","[S310][S314]"),
       ("6","A 130-year-old English practice inside a Chicago firm; construction negligence top tier 19 years","[S70][S140]")]
    s=""
    for i,(n,t,src) in enumerate(U):
        y=i*64
        s+=f'<circle cx="24" cy="{y+28}" r="20" fill="{ACC}"/>'+text(24,y+34,n,15,WHITE,"middle",800)
        s+=f'<rect x="56" y="{y+2}" width="704" height="54" rx="6" fill="{TINT}"/>'
        s+=text(68,y+24,t,10.6,NAVY,weight=700,maxw=680)
        s+=text(68,y+46,src,9,GREY)
    return svg(w,h,s),"What Mayer Brown can claim that no rival in the peer set can. Each claim is limited to the nine-firm peer set and sources read on 8 Oct 2026. Claim 6 is \"unusual for a US firm\", not proven unique."

@fig("why_onepage", full=True)
def _():
    w,h=760,1000
    s=text(380,24,"Why Mayer Brown, on one page",20,NAVY,"middle",800)
    s+=box(0,44,760,70,"The mechanism: a Chicago finance firm built on a 130-year-old London practice, concentrated in finance products for institutions, choosing focus and lateral teams over merger.",NAVY,NAVY,WHITE,12.5,700)
    cols=[("STRUCTURE",ACC,["Associated practices: US LLP + English LLP [S75]","London = Rowe & Maw, 1895 [S70]","Not merging; hiring teams [S220][S84]","~15 trainees, Magic Circle pay [S16][S234]"]),
          ("PRODUCTS",BLU,["Top tier: derivatives, ABL, trade finance [S139]","US ABS firm of the year x6; SRT 2026 [S148]","Pensions-insurance one-stop shop: Ford £4.6bn [S310]","Construction disputes top band 19 years [S140]"]),
          ("MOMENT",SIG,["London revenue +20.5%, record $268.2m [S302]","\"Deeper with fewer clients\" [S220]","Basel 3.1 1 Jan 2027 → risk transfer work [S190]","GenAI with mandatory human review [S230]"])]
    for i,(t,c,items) in enumerate(cols):
        x=i*258
        s+=box(x,130,244,40,t,c,c,WHITE,13,800)
        for j,it in enumerate(items):
            s+=box(x,178+j*70,244,62,it,TINT,c,NAVY,10,600)
    s+=box(0,470,760,40,"Three lengths (full text in Part 12)",TINT,NAVY2,NAVY,12,800)
    s+=box(0,518,250,200,"30 seconds",ACCS,ACC,NAVY,11.5,800,sub="Finance products for institutions where the firm is top tier; a London practice with real depth; a cohort of 15 where trainees do real work.",subfs=9.6)
    s+=box(255,518,250,200,"2 minutes",BLUS,BLU,NAVY,11.5,800,sub="Add: why focus not merger; one deal (Ford buy-in or Nigeria ports); Basel 3.1 and SRT; what you learned at the masterclass.",subfs=9.6)
    s+=box(510,518,250,200,"The close",SIGS,SIG,NAVY,11.5,800,sub="\"The thing I most want to work on is [derivatives / risk transfer / buy-ins], because...\" One reason from your own experience.",subfs=9.6)
    s+=box(0,734,370,250,"Most candidates say",REDS,RED,NAVY,12,800,sub="\"Global firm with a diverse client base.\" \"Strong in finance.\" \"Friendly culture.\" \"Great training.\" \"Matches Magic Circle pay.\" (All true of many firms; one is the event page's own sentence.)",subfs=10)
    s+=box(390,734,370,250,"You can say",GRNS,GRN,NAVY,12,800,sub="\"Top tier in London for both derivatives and asset-based lending, which no other firm I'm applying to is.\" \"London grew 20% by going deeper with fewer clients.\" \"The Ford buy-in needed pensions, insurance and derivatives lawyers in one team.\" \"Basel 3.1 makes risk transfer work grow from January.\"",subfs=10)
    return svg(w,h,s),"\"Why Mayer Brown\" on one page: structure, products and moment, the three lengths, and the contrast with what most candidates will say. Sources as marked; synthesis is the author's [Inferred]."

@fig("master", full=True)
def _():
    w,h=760,1000
    s=text(380,22,"The master diagram: industry, firm, role",19,NAVY,"middle",800)
    s+=box(0,40,760,150,"",TINT,NAVY2,NAVY)
    s+=text(12,62,"INDUSTRY FORCES (Part 5, 6, 7)",11,NAVY2,weight=800)
    forces=["GenAI","Mergers","US firms in London","Pay war £150-189k","Private credit","Basel 3.1 (1 Jan 2027)","Securitisation reform","Pensions endgame"]
    for i,f in enumerate(forces):
        s+=box(12+(i%4)*186,72+(i//4)*54,176,46,f,WHITE,GREY,NAVY,10,700)
    s+=arrow(380,190,380,222,NAVY,2.5,label="shape demand for",fs=10,loff=(70,4))
    s+=box(0,222,760,290,"",ACCS,ACC,NAVY)
    s+=text(12,244,"MAYER BROWN (Parts 2, 3, 4)",11,ACC,weight=800)
    s+=box(12,256,360,80,"Clients: banks, funds, insurers, trustees, ISDA",WHITE,ACC,NAVY,10.5,700,sub="fewer, deeper: 6,316 billed [S220]",subfs=9)
    s+=box(388,256,360,80,"Products: derivatives, ABL, trade finance (T1); securitisation, pensions (T2)",WHITE,ACC,NAVY,10.5,700,sub="[S139][S141][S145]",subfs=9)
    s+=box(12,346,360,80,"Money: $2.17bn; PEP $3.196m; London $268.2m",WHITE,ACC,NAVY,10.5,700,sub="[S220][S302]",subfs=9)
    s+=box(388,346,360,80,"Strategy: no merger; lateral teams; AI with human review",WHITE,ACC,NAVY,10.5,700,sub="[S220][S84][S230]",subfs=9)
    s+=box(12,436,736,66,"Structure: associated practices; London = Rowe & Maw 1895; business services ~44% of LLP headcount; controls: conflicts, confidentiality, supervision",WHITE,ACC,NAVY,10,600,sub="[S75][S70][S78][S110]",subfs=9)
    s+=arrow(380,512,380,544,NAVY,2.5,label="creates the work in",fs=10,loff=(70,4))
    s+=box(0,544,760,190,"",BLUS,BLU,NAVY)
    s+=text(12,566,"THE ROLE: trainee, London (Part 1)",11,BLU,weight=800)
    seats=["Banking & Finance","Derivatives / SF","Real estate","Disputes / construction","Corporate / PE","Pensions / insurance"]
    for i,t in enumerate(seats):
        s+=box(12+(i%3)*248,578+(i//3)*56,236,48,t,WHITE,BLU,NAVY,10.5,700)
    s+=text(380,712,"Four 6-month seats · ≥1 transactional · ≤2 contentious · ~15 a year [S16]",10,NAVY,"middle",700)
    s+=arrow(380,734,380,766,NAVY,2.5,label="you get in through",fs=10,loff=(70,4))
    s+=box(0,766,760,110,"",SIGS,SIG,NAVY)
    s+=text(12,788,"THE PROCESS (Part 9)",11,SIG,weight=800)
    st=["SEO form 26 Oct","Masterclass 2 Nov","Vac scheme app 4 Dec","Assessment Jan-Feb","Vac scheme Apr / Jun","TC 2029"]
    for i,t in enumerate(st):
        x=12+i*124
        s+=box(x,800,112,60,t,ACC if i<2 else WHITE,SIG,WHITE if i<2 else NAVY,9.6,700)
    s+=box(0,894,760,90,"Your edge (Parts 11, 12): one stable frame (rules → client → record → speed), one mechanism-based reason for this firm, and one current fact (Basel 3.1, securitisation reform, or the Ford buy-in) you can explain to a partner.",NAVY,NAVY,WHITE,11,600)
    return svg(w,h,s),"The master diagram: how industry forces create Mayer Brown's work, how that work becomes a trainee's seats, and how you get in. Sources as marked in each box."
