"""Diagrams for the Inside Private Banking event brief."""
from svg import *
INK="#1c2330"

def scenario_flow():
    d=D(780,330)
    steps=[("1. Listen first","Who is in the room, what has changed, what do they want? Ask before you propose."),
           ("2. Both sides of the balance sheet","Assets and liabilities, liquid and illiquid, where the money sits today and what it is for."),
           ("3. Goals and time horizons","Lifestyle, growth, legacy, giving. Which money is for which goal, and when it is needed."),
           ("4. Bring in the seats","Investor, Capital Advisor, Wealth Advisor, Alternatives, Trusts, cross-border tax counsel."),
           ("5. Agree next steps","One or two concrete actions, who does what, and when you meet again. Never a product list.")]
    w=144
    for i,(t,b) in enumerate(steps):
        x=12+i*154
        d.box(x,24,w,120,t,b,fill=NAVY if i%2==0 else NAVY2,tsize=9.6,bsize=7.6)
        if i<4: d.arrow(x+w,84,x+154,84,color=GOLD,width=2)
    d.region(12,160,756,160,"What assessors are watching for in the room",fill=BG,lsize=10)
    items=[("Questions before answers","Did you find out what the client cares about before you spoke about markets or products?"),
           ("Structure","Did you organise the problem (liquidity, growth, legacy, risk) rather than list ideas?"),
           ("Teamwork","Did you bring others in, give the quieter person room, and build on their points?"),
           ("Commercial sense","Did you see how the bank earns and where the risk sits (lending against illiquid assets, concentration)?"),
           ("Empathy and judgment","Did you notice the human issue (a divorce, a child who does not want the business, a founder's identity)?")]
    for i,(t,b) in enumerate(items):
        x=22+i*150
        d.box(x,186,140,122,t,b,fill=WHITE,stroke=LINE,tfill=NAVY,bfill=GREY,tsize=8.8,bsize=7.4)
    return d.svg()

def family_balance_sheet():
    d=D(780,330)
    d.text(390,20,"A worked example: the founder who has just sold, £60m, London, two children, a house in Italy",size=11,fill=NAVY,weight="bold")
    d.region(12,34,370,200,"Assets",fill=BG,lsize=10)
    rows=[("Sale proceeds (cash, GBP)","£42m","liquid, earning deposit interest, taxed next January"),
          ("Retained stake in the buyer (listed, locked 12 months)","£9m","concentrated, cannot sell, can borrow against"),
          ("Family home, Hampstead","£8m","illiquid, no income, IHT exposure"),
          ("Villa, Tuscany","£3m","cross-border tax, succession under Italian law"),
          ("Pension, ISAs, art","£2m","mixed")]
    y=58
    for a,v,n in rows:
        d.text(22,y,a,size=8.4,fill=INK,anchor="start",maxw=190); d.text(250,y,v,size=8.6,fill=NAVY,anchor="end",weight="bold"); d.text(258,y,n,size=7.3,fill=GREY,anchor="start",maxw=118)
        y+=34
    d.region(398,34,370,200,"Liabilities, obligations and goals",fill=LBLUE,lsize=10)
    rows2=[("Capital gains tax due","£9m","January; must stay liquid"),
           ("Mortgage on the home","£2m","could be refinanced cheaper"),
           ("Lifestyle spend","£1m a year","for 40 years, inflation-linked"),
           ("Children, 19 and 23","gifts, education, a flat each","and a conversation about work"),
           ("Legacy and giving","unknown","no will updated since the sale")]
    y=58
    for a,v,n in rows2:
        d.text(408,y,a,size=8.4,fill=INK,anchor="start",maxw=170); d.text(630,y,v,size=8.6,fill=NAVY,anchor="end",weight="bold",maxw=100); d.text(638,y,n,size=7.3,fill=GREY,anchor="start",maxw=120)
        y+=34
    d.box(12,246,756,74,"What a good first answer sounds like","Before investing a pound: ring-fence the tax (£9m) and two years of spending in cash and gilts; refinance the mortgage against the portfolio rather than selling anything; hedge or lend against the locked stake rather than wait; get the will, the Italian succession and the children's plan started with the Wealth Advisor; only then build the long-term portfolio in stages, with alternatives sized to a liquidity budget. Ask the client what the money is for before any of it.",fill=GOLD2,stroke=GOLD,tfill=NAVY,bfill=NAVY,tsize=9.5,bsize=7.8)
    return d.svg()

def ladder():
    d=D(780,230)
    lv=[("Beginner","What a private bank is, who the clients are, the five seats, how the bank earns, the words on the floor.","Every candidate in the room should have this."),
        ("Intermediate","How the International Private Bank is organised from London, who runs it, the client journey, how a scenario is structured, the numbers.","Most candidates will have fragments of this."),
        ("Advanced","The strategy and its tensions: Europe share, growing advisors, alternatives and liquidity, AI, the UK tax shift, what the leaders have said and why. Questions that show you have read the filings and the interviews.","Almost no candidate will have this.")]
    for i,(t,b,n) in enumerate(lv):
        x=12+i*256; y=150-i*50
        d.box(x,y,244,60+i*50,t,b,fill=[NAVY2,NAVY,GOLD][i],tfill=(NAVY if i==2 else WHITE),bfill=(NAVY if i==2 else WHITE),tsize=11,bsize=7.8)
        d.text(x+122,218,n,size=8,fill=GREY,italic=True,maxw=240)
    return d.svg()

def event_day(slots):
    """slots: list of (time, what, your move)"""
    d=D(780,40+len(slots)*44)
    d.text(14,20,"The day, and your move in each part of it",size=11,fill=NAVY,weight="bold",anchor="start")
    for i,(t,w,m) in enumerate(slots):
        y=36+i*44
        d.box(14,y,90,38,t,None,fill=NAVY,tsize=9)
        d.box(112,y,300,38,w,None,fill=WHITE,stroke=LINE,tfill=INK,tsize=8.6,tweight="normal")
        d.box(420,y,346,38,m,None,fill=GOLD2,stroke=GOLD,tfill=NAVY,tsize=8.4,tweight="normal")
    return d.svg()

def org_chart(levels):
    """levels: list of rows; each row is list of (title, name, note). Draw rows of boxes with connector lines."""
    rowh=86; d=D(780,30+len(levels)*rowh)
    prev=None
    for r,row in enumerate(levels):
        n=len(row); w=min(180,(760-(n-1)*10)/n); total=n*w+(n-1)*10; x0=(780-total)/2
        cur=[]
        for i,(t,nm,note) in enumerate(row):
            x=x0+i*(w+10); y=16+r*rowh
            fill=[NAVY,NAVY2,BLUE,WHITE][min(r,3)]
            tf=WHITE if fill!=WHITE else NAVY; bf=WHITE if fill!=WHITE else GREY
            d.box(x,y,w,66,nm,f"{t}. {note}" if note else t,fill=fill,stroke=LINE if fill==WHITE else None,tfill=tf,bfill=bf,tsize=9,bsize=7.2)
            cur.append((x+w/2,y,x+w/2,y+66))
        if prev:
            py=prev[0][3]; my=py+8
            d.line(min(p[0] for p in prev),py,min(p[0] for p in prev),my,color=LINE)
            xs=[c[0] for c in cur]+[p[0] for p in prev]
            d.line(min(xs),my,max(xs),my,color=LINE)
            for p in prev: d.line(p[0],py,p[0],my,color=LINE)
            for c in cur: d.line(c[0],my,c[0],c[1],color=LINE)
        prev=cur
    return d.svg()
