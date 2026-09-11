from svg import *

def team_model():
    d=D(760,430)
    # client centre
    d.circle(380,215,58,fill=GOLD)
    d.text(380,208,"THE CLIENT",size=12,fill="#fff",weight="bold")
    d.text(380,224,"family, founder,\nfamily office",size=8.5,fill="#fff")
    # advisor ring
    d.parts.append(f'<circle cx="380" cy="215" r="150" fill="none" stroke="{LINE}" stroke-width="1.2" stroke-dasharray="6,4"/>')
    # Advisor at top
    d.box(290,20,180,70,"ADVISOR (Banker)","Relationship lead. Wins the client, owns the relationship, coordinates everyone below.",fill=NAVY)
    d.arrow(380,90,380,155,color=NAVY,marker="arrn")
    # specialists
    d.box(20,150,170,70,"INVESTOR","Investment specialist. Builds and runs the portfolio; talks markets with the client.",fill=NAVY2)
    d.box(570,150,170,70,"CAPITAL ADVISOR","Lending specialist. Mortgages, loans against portfolios, art, aircraft, company shares.",fill=NAVY2)
    d.box(60,320,190,70,"WEALTH ADVISOR","Trusts, estates, succession, tax-aware structuring, philanthropy.",fill=NAVY2)
    d.box(510,320,190,70,"CLIENT SERVICE / ASSOCIATE","Onboarding, KYC paperwork, payments, day-to-day execution.",fill=NAVY2)
    for (x1,y1) in [(190,185),(570,185),(250,335),(510,335)]:
        d.arrow(x1,y1,380+(x1-380)*0.35 if x1<380 else 380+(x1-380)*0.35, 215+(y1-215)*0.35, color=GREY)
    # specialists band bottom
    d.region(110,392,540,36,"",fill=BG,lsize=8,dash=False)
    d.text(380,406,"Specialists pulled in as needed: Alternatives · Structured products · FX · Trust company · Philanthropy",size=8,fill=GREY)
    d.text(380,418,"Sports & Entertainment · Founders & Executives · 23 Wall (family offices)",size=8,fill=GREY)
    return fig(d.svg(),"The integrated team around one client. The Advisor is the single point of accountability; the specialists are shared across a team's clients. The client experiences one relationship, not five product salespeople.")

def client_journey():
    d=D(780,300)
    steps=[("1. SOURCE","Referral from an existing client, the investment bank, commercial bank, a lawyer or accountant, or an event"),
           ("2. DISCOVER","Meetings to understand the family: goals, liquidity, assets, tax residency, fears, next generation"),
           ("3. PROPOSE","Investor + Advisor build a written proposal: allocation, lending, planning ideas, fees"),
           ("4. ONBOARD","KYC, source-of-wealth checks, suitability, account opening, transfer of assets"),
           ("5. IMPLEMENT","Portfolio built, loans drawn, trusts set up, cash and FX arranged"),
           ("6. REVIEW","Quarterly reviews, market calls, rebalancing, life events, new needs"),
           ("7. DEEPEN","More of the wallet, next generation, and the client refers others (back to step 1)")]
    x=10
    for i,(t,b) in enumerate(steps):
        d.box(x,70,100,150,t,b,fill=NAVY if i%2==0 else NAVY2,tsize=10.5,bsize=8.2)
        if i<6: d.arrow(x+100,145,x+112,145,color=GREY,width=2)
        x+=112
    d.poly([(748,222),(748,260),(60,260),(60,224)],color=GOLD,marker="arrg",width=1.8)
    d.text(400,255,"referrals and the next generation restart the cycle",size=9,fill=GOLD,italic=True)
    d.text(10,40,"Weeks to months",size=9,fill=GREY,anchor="start",italic=True)
    d.text(770,40,"Years to generations",size=9,fill=GREY,anchor="end",italic=True)
    d.line(10,50,770,50,color=LINE)
    d.text(390,25,"Time spent by the Advisor is heaviest in steps 1, 2 and 6",size=9.5,fill=NAVY,weight="bold")
    return fig(d.svg(),"The client journey from prospect to multi-generational relationship. Steps 1 to 3 are 'sales'; steps 4 to 7 are 'relationship management'. At J.P. Morgan the same Advisor owns both, which is the point of the role.")

def internal_workflow():
    d=D(780,470)
    d.region(10,10,760,60,"WHERE CLIENTS COME FROM (the 'one firm' referral engine)",fill=LBLUE,dash=False)
    srcs=[("Commercial & Investment Bank","founders selling companies, IPOs, executives"),("Chase / Wealth Management","clients who outgrow the affluent channel"),("Existing clients & advisers","word of mouth, lawyers, accountants"),("Asset Management","institutional contacts, family offices")]
    x=20
    for t,b in srcs:
        d.box(x,32,180,32,t,None,fill=WHITE,tfill=NAVY,tsize=9,stroke=LINE); x+=190
    d.arrow(390,70,390,105,color=NAVY,marker="arrn",width=2)
    # Advisor hub
    d.box(280,105,220,60,"ADVISOR / BANKER","Diagnoses the need, then pulls in the right internal team",fill=NAVY)
    # internal teams
    teams=[("Global Investment Strategy","house view, Outlook, Eye on the Market, LTCMA"),
           ("Manager Selection","chooses external and in-house funds; open architecture"),
           ("Alternatives","private equity, private credit, hedge funds, real assets"),
           ("Markets / Trading desks","execution, structured notes, FX, hedging"),
           ("Credit underwriting","structures and approves loans; risk appetite"),
           ("Trust & Estates / Wealth Planning","trusts, wills, cross-border structuring"),
           ("KYC / AML / Compliance","source of wealth, suitability, sanctions"),
           ("Product & Technology","platforms, reporting, digital tools")]
    cols=4; bw=180; bh=62; gx=190; gy=76; x0=20; y0=200
    for i,(t,b) in enumerate(teams):
        cx=x0+(i%cols)*gx; cy=y0+(i//cols)*gy
        d.box(cx,cy,bw,bh,t,b,fill=WHITE,tfill=NAVY,bfill=GREY,stroke=LINE,tsize=9.5,bsize=8)
        d.arrow(390,165,cx+bw/2,cy,color=GREY,width=1.1)
    d.region(10,365,760,95,"WHAT GOES BACK TO THE CLIENT",fill=BG,dash=False)
    outs=["Written investment proposal and allocation","Loan term sheet","Trust / estate plan","Ongoing reviews and market views"]
    x=20
    for o in outs:
        d.box(x,392,180,55,o,None,fill=GOLD,tsize=9.5); x+=190
    return fig(d.svg(),"How the Advisor works with the firm. The Advisor rarely 'does' the technical work; the job is to know the client well enough to bring the right specialist at the right time, and to own the answer that goes back.")

def firm_org():
    d=D(780,400)
    d.box(240,10,300,54,"JPMORGAN CHASE & CO.","Holding company. CEO Jamie Dimon. Four reportable segments.",fill=NAVY)
    lobs=[("CONSUMER & COMMUNITY BANKING (CCB)","'Chase'. Serves individuals and small businesses.",["Banking & Wealth Management","Home Lending","Card Services & Auto","(includes Chase UK, J.P. Morgan Wealth Management)"]),
          ("COMMERCIAL & INVESTMENT BANK (CIB)","Serves companies, governments and institutions.",["Banking: investment, corporate, commercial","Markets: fixed income, equities","Payments","Securities Services"]),
          ("ASSET & WEALTH MANAGEMENT (AWM)","Manages money and advises the wealthy.",["Asset Management (funds, ETFs, alternatives)","Global Private Bank","← the Advisor internship sits here"]),
          ("CORPORATE","Treasury and the Chief Investment Office; central functions.",["Treasury & CIO","Other corporate"])]
    x=10; w=185
    for i,(t,b,subs) in enumerate(lobs):
        fill = GOLD if i==2 else NAVY2
        d.box(x,110,w,70,t,b,fill=fill,tsize=9.5,bsize=8)
        d.arrow(390,64,x+w/2,110,color=GREY)
        y=195
        for s in subs:
            d.box(x+8,y,w-16,34,s,None,fill=WHITE,tfill=NAVY,stroke=GOLD if i==2 else LINE,tsize=8.4,tweight="normal"); y+=40
        x+=192
    return fig(d.svg(),"JPMorgan Chase's four lines of business as reported since the 2024 reorganisation. The Global Private Bank sits inside AWM. Chase's own wealth offering for less wealthy clients sits inside CCB, not AWM.")

def wealth_continuum(rows):
    """rows: list of (segment, threshold, where, model)"""
    d=D(780,60+len(rows)*58)
    d.text(390,22,"Client wealth →",size=9.5,fill=GREY,italic=True)
    for i,(seg,thr,where,model) in enumerate(rows):
        y=40+i*58
        shade = GOLD if "Private Bank" in seg or "23 Wall" in seg else NAVY2
        d.box(20,y,200,46,seg,thr,fill=shade,tsize=10,bsize=8.2)
        d.box(230,y,140,46,where,None,fill=WHITE,tfill=NAVY,stroke=LINE,tsize=9)
        d.box(380,y,380,46,model,None,fill=BG,tfill="#1c2330",stroke=LINE,tsize=8.6,tweight="normal")
        if i<len(rows)-1: d.arrow(120,y+46,120,y+58,color=GREY,width=1.4)
    return fig(d.svg(),"The wealth 'ladder' inside JPMorgan Chase. As a client's assets grow they move from a branch-based, scaled model in CCB to the bespoke, team-based Private Bank in AWM. Thresholds are indicative and vary by market.")

def pb_revenue():
    d=D(780,330)
    d.region(10,10,760,310,"HOW A PRIVATE BANK CLIENT TURNS INTO REVENUE",fill=BG,dash=False)
    items=[("INVESTMENTS","Advisory / discretionary fee: a % of assets each year (basis points). Plus commissions on trades and placement fees on alternatives.","Asset management fees, commissions"),
           ("DEPOSITS","Client keeps cash with the bank. Bank pays a rate, earns more by lending/investing it. The spread is net interest income.","Net interest income"),
           ("LOANS","Mortgages, loans secured on portfolios or other assets. Client pays interest above the bank's funding cost.","Net interest income"),
           ("PLANNING & TRUST","Trustee fees, estate administration, family office services.","Other fees")]
    x=20
    for t,b,l in items:
        d.box(x,42,180,150,t,b,fill=NAVY2,tsize=10.5,bsize=8.6)
        d.arrow(x+90,192,x+90,215,color=GREY)
        d.box(x,218,180,34,l,None,fill=WHITE,tfill=NAVY,stroke=LINE,tsize=8.8)
        x+=190
    d.box(20,268,740,40,"AWM revenue in the 10-K = asset management fees + commissions & other fees + net interest income + other income. The Advisor's job is to grow all four legs for each family, not just the first.",None,fill=GOLD,tsize=9.2,tweight="normal")
    return fig(d.svg(),"The four revenue legs of a private bank relationship. A client who only has an investment account is 'one-legged' and easy to lose; a client with investments, cash, lending and a trust is deeply embedded. This is what 'share of wallet' means in practice.")

def flywheel():
    d=D(700,360)
    cx,cy=350,180
    nodes=[("1. INVESTMENT PERFORMANCE","good outcomes for clients",cx,55),
           ("2. TALENT","hire and keep the best advisors and investors",cx+235,180),
           ("3. NEW CLIENTS","referrals and prospecting",cx,305),
           ("4. FLOWS","clients 'vote with their feet'",cx-235,180)]
    for t,b,x,y in nodes:
        d.box(x-105,y-32,210,64,t,b,fill=NAVY,tsize=10,bsize=8.6)
    d.arrow(cx+110,80,cx+235,140,color=GOLD,marker="arrg",width=2.2,curve=(cx+220,80))
    d.arrow(cx+235,220,cx+110,285,color=GOLD,marker="arrg",width=2.2,curve=(cx+220,285))
    d.arrow(cx-110,285,cx-235,220,color=GOLD,marker="arrg",width=2.2,curve=(cx-220,285))
    d.arrow(cx-235,140,cx-110,80,color=GOLD,marker="arrg",width=2.2,curve=(cx-220,80))
    d.text(cx,175,"Record revenue,",size=10.5,fill=NAVY,weight="bold")
    d.text(cx,190,"pre-tax income,",size=10.5,fill=NAVY,weight="bold")
    d.text(cx,205,"client assets",size=10.5,fill=NAVY,weight="bold")
    return fig(d.svg(),"Mary Erdoes' four 'ingredients for growth' drawn as the flywheel they actually are. Each one feeds the next; the Advisor sits squarely in ingredients 2 and 3 and is measured on ingredient 4.")

if __name__=="__main__":
    rows=[("Chase retail","everyday banking","CCB","Branches and app; mass market; scale economics"),
          ("Chase Private Client","~$150k+ (US)","CCB","Branch-based banker plus a J.P. Morgan advisor"),
          ("J.P. Morgan Private Client","~$750k+ (US, from 2024)","CCB","First Republic-style high-touch service in dedicated offices"),
          ("J.P. Morgan Wealth Management","broad range","CCB","Financial advisors, self-directed and robo (Wealth Plan)"),
          ("J.P. Morgan Private Bank","~$10m+ (US); ~$5m+ typical outside US","AWM","Team-based, global, lending and trust, bespoke"),
          ("23 Wall","the very largest families and family offices","AWM","Institutional-style coverage of the top few hundred families")]
    html_=open("style.css").read()
    body="".join([team_model(),client_journey(),internal_workflow(),firm_org(),wealth_continuum(rows),pb_revenue(),flywheel()])
    open("preview.html","w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{html_}</style></head><body>{body}</body></html>")
