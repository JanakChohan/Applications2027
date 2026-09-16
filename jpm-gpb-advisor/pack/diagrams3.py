"""Diagrams for the evergreen private credit explainer."""
from svg import *
INK="#1c2330"

def structures():
    d=D(780,330)
    # left: closed-end drawdown
    d.region(10,10,375,310,"A. Traditional closed-end 'drawdown' fund (the old model)",fill=BG,lsize=10)
    L,R,Y=40,360,150
    d.line(L,Y,R,Y,color=NAVY,width=2.5)
    for i,yr in enumerate(["Yr 0","Yr 2","Yr 4","Yr 6","Yr 8","Yr 10"]):
        x=L+(R-L)*i/5; d.circle(x,Y,4,fill=NAVY); d.text(x,Y+16,yr,size=8,fill=GREY)
    # capital calls down arrows (investor pays in) years 0-3
    for i in range(4):
        x=L+(R-L)*(i*0.6)/5+10
        d.arrow(x,80,x,Y-8,color=RED,width=1.6)
    d.text(105,70,"Capital calls: investor pays in over ~3 years",size=8.5,fill=RED,weight="bold")
    # distributions up arrows years 4-10
    for i in range(5):
        x=L+(R-L)*(2.6+i*0.6)/5
        d.arrow(x,Y+8,x,Y+70,color=GREEN,width=1.6)
    d.text(255,240,"Distributions: money returned as loans repay, years 4 to 10",size=8.5,fill=GREEN,weight="bold",maxw=230)
    d.box(30,262,335,48,"No redemptions. Ever.","Money is locked for the life of the fund. To exit early you sell your stake on the secondary market, usually at a discount. Investors: pension funds, insurers, endowments.",fill=WHITE,stroke=NAVY,tfill=NAVY,bfill=GREY,tsize=9.5,bsize=7.6)
    # right: evergreen
    d.region(395,10,375,310,"B. Evergreen / semi-liquid fund (the new model)",fill=LBLUE,lsize=10)
    L2,R2=425,745
    d.line(L2,Y,R2,Y,color=NAVY,width=2.5)
    d.text(585,Y+16,"no end date: the fund runs indefinitely",size=8,fill=GREY,italic=True)
    d.parts.append(f'<path d="M{R2},{Y} l-8,-5 l0,10 z" fill="{NAVY}"/>')
    # monthly subscriptions
    for i in range(10):
        x=L2+8+i*32
        d.arrow(x,88,x,Y-8,color=RED,width=1.3)
    d.text(585,70,"Monthly subscriptions: anyone can buy in at this month's NAV",size=8.5,fill=RED,weight="bold",maxw=300)
    # quarterly tender up arrows, small
    for i in range(4):
        x=L2+40+i*80
        d.arrow(x,Y+8,x,Y+50,color=GREEN,width=1.6)
        d.text(x,Y+62,"Q"+str(i+1),size=7.5,fill=GREEN)
    d.text(585,228,"Quarterly repurchase offers: the fund buys back up to ~5% of its shares each quarter, if the board chooses to",size=8.5,fill=GREEN,weight="bold",maxw=310)
    d.box(415,262,335,48,"Redemptions capped, not promised","5% of NAV per quarter, about 20% a year, at the manager's discretion. Investors: wealthy individuals via private banks and advisers, $2,500 to $25,000 minimums.",fill=WHITE,stroke=NAVY,tfill=NAVY,bfill=GREY,tsize=9.5,bsize=7.6)
    return d.svg()

def chain():
    d=D(780,275)
    xs=[20,215,410,605]; w=155
    d.box(xs[0],40,w,100,"1. Private companies","Mid-sized firms, often owned by private equity, that borrow instead of issuing bonds. Loans of $50m to $1bn+, floating rate, senior secured.",fill=NAVY,bsize=7.8)
    d.box(xs[1],40,w,100,"2. The evergreen fund","Run by a manager (Blue Owl, Blackstone, Ares, Apollo, Partners Group). Holds hundreds of loans. Strikes a NAV monthly.",fill=NAVY2,bsize=7.8)
    d.box(xs[2],40,w,100,"3. The distributor","Private banks, wirehouses, wealth platforms. Runs due diligence, approves the fund for its shelf, and its advisors recommend it.",fill=GOLD,bsize=7.8,tfill=NAVY,bfill=NAVY)
    d.box(xs[3],40,w,100,"4. The investor","A wealthy individual or family. Buys monthly, receives ~9 to 11% income, expects to be able to sell back quarterly.",fill=NAVY,bsize=7.8)
    for i in range(3):
        d.arrow(xs[i]+w,70,xs[i+1],70,color=GREEN,width=2)
        d.arrow(xs[i+1],110,xs[i]+w,110,color=RED,width=2)
    d.text(400,26,"Interest and repayments flow left to right; cash and redemption requests flow right to left",size=8.5,fill=GREY,italic=True)
    d.text(xs[0]+w+30,64,"interest",size=7.5,fill=GREEN,anchor="middle")
    d.text(xs[0]+w+30,122,"loan",size=7.5,fill=RED)
    d.text(xs[1]+w+30,64,"income",size=7.5,fill=GREEN)
    d.text(xs[1]+w+30,122,"capital",size=7.5,fill=RED)
    d.text(xs[2]+w+30,64,"distributions",size=7.5,fill=GREEN)
    d.text(xs[2]+w+30,122,"subscription",size=7.5,fill=RED)
    d.box(20,160,740,50,"Who earns what along the chain","Manager: ~1.25% management fee on assets plus ~12.5% of income. Distributor: a placement fee and/or an ongoing servicing fee. Investor: whatever is left, historically 9 to 11% a year in income. The manager's fee is on assets under management, so redemptions cut its revenue directly.",fill=WHITE,stroke=LINE,tfill=NAVY,bfill=GREY,tsize=9.5,bsize=7.8)
    d.box(20,218,740,50,"Where J.P. Morgan sits","Box 3. The Private Bank chooses which evergreen funds to put on its shelf, sizes them inside client portfolios, and its advisors own the conversation when a client cannot get money out. It also sits in box 1 and 2 through its own direct-lending and asset-management arms.",fill=GOLD2,stroke=GOLD,tfill=NAVY,bfill=NAVY,tsize=9.5,bsize=7.8)
    return d.svg()

def gate(req=20, cap=5):
    """Bar picture: requests vs what gets paid, then the queue over time."""
    d=D(780,300)
    d.text(200,22,"Quarter 1: requests exceed the cap",size=11,fill=NAVY,weight="bold")
    # bars
    base=200; scale=6
    d.parts.append(f'<rect x="60" y="{base-req*scale}" width="110" height="{req*scale}" fill="{RED}" opacity="0.85"/>')
    d.text(115,base-req*scale-6,f"Requests: {req}% of NAV",size=9,fill=RED,weight="bold")
    d.parts.append(f'<rect x="220" y="{base-cap*scale}" width="110" height="{cap*scale}" fill="{GREEN}"/>')
    d.text(275,base-cap*scale-6,f"Paid: {cap}% cap",size=9,fill=GREEN,weight="bold")
    d.line(50,base,350,base,color=GREY,width=1)
    d.text(200,220,f"Everyone who asked gets {cap}/{req} = {int(cap/req*100)}% of what they asked for, pro rata. The rest is not queued: you must ask again next quarter.",size=8.5,fill=INK,maxw=300)
    # right: the queue
    d.text(580,22,"If everyone keeps asking, how long to get out?",size=11,fill=NAVY,weight="bold")
    x0=420; y=60
    d.text(x0,y,"Quarter",size=8.5,fill=GREY,anchor="start",weight="bold"); d.text(x0+120,y,"Paid this quarter",size=8.5,fill=GREY,anchor="start",weight="bold"); d.text(x0+250,y,"Still inside",size=8.5,fill=GREY,anchor="start",weight="bold")
    inside=100.0
    for q in range(1,7):
        paid=min(cap,inside); inside-=paid
        yy=y+18*q
        d.text(x0,yy,f"Q{q}",size=8.5,fill=INK,anchor="start")
        d.text(x0+120,yy,f"{paid:.0f}% of original NAV",size=8.5,fill=INK,anchor="start")
        d.text(x0+250,yy,f"{inside:.0f}%",size=8.5,fill=INK,anchor="start")
        d.parts.append(f'<rect x="{x0+290}" y="{yy-8}" width="{inside*0.6}" height="10" fill="{NAVY}" opacity="0.8"/>')
    d.text(x0,y+18*7+4,"At the full 5% cap it takes five years to exit entirely. In practice the cap is a share of NAV, and NAV shrinks as money leaves and as the manager sells its most liquid loans first to pay people, so the remaining investors are left holding the harder-to-sell assets.",size=8.5,fill=INK,anchor="start",maxw=340)
    return d.svg()

def mismatch():
    d=D(780,290)
    d.region(15,12,360,265,"What the fund owns (assets)",fill=BG,lsize=10)
    d.box(35,42,320,66,"Private loans, 5 to 7 year terms","Cannot be sold quickly except at a discount. Valued by the manager (with a third-party check) once a month, not by a market price every second.",fill=NAVY,bsize=7.8)
    d.box(35,116,320,52,"Cash and liquid securities, 5 to 15%","The buffer that pays normal redemptions and new loans.",fill=NAVY2,bsize=7.8)
    d.box(35,176,320,52,"Borrowing capacity (credit lines, bonds)","Used to fund loans, and in a squeeze, redemptions.",fill=NAVY2,bsize=7.8)
    d.text(195,250,"Slow to turn into cash",size=9.5,fill=RED,weight="bold")
    d.region(405,12,360,265,"What the fund has promised (liabilities)",fill=LBLUE,lsize=10)
    d.box(425,42,320,66,"Investors who can ask for cash quarterly","Thousands of individuals, each of whom can change their mind at once when the news turns.",fill=GOLD,tfill=NAVY,bfill=NAVY,bsize=7.8)
    d.box(425,116,320,52,"The 5% cap is the release valve","Designed so a rush for the exit cannot force fire sales. It protects those who stay by slowing those who leave.",fill=WHITE,stroke=GOLD,tfill=NAVY,bfill=GREY,bsize=7.8)
    d.box(425,176,320,52,"But the cap was sold as a formality","Marketing implied you could get out. The cap binding is the moment the promise and the product diverge.",fill=WHITE,stroke=RED,tfill=RED,bfill=GREY,bsize=7.8)
    d.text(585,250,"Fast to be demanded",size=9.5,fill=RED,weight="bold")
    d.arrow(375,140,405,140,color=GREY,width=2)
    return d.svg()

def sources_of_cash():
    d=D(780,120)
    items=[("1. Cash on hand","first line"),("2. New subscriptions","new money pays old money out"),("3. Loan repayments","borrowers refinancing"),("4. Credit lines and bonds","borrow to pay redemptions"),("5. Sell loans","secondary sale, often at a discount"),("6. Shrink the cap or suspend","last resort")]
    w=118
    for i,(t,s) in enumerate(items):
        x=12+i*128
        fill=NAVY if i<3 else (GOLD if i<5 else RED)
        d.box(x,20,w,70,t,s,fill=fill,tsize=8.8,bsize=7.4,tfill=(NAVY if fill==GOLD else WHITE),bfill=(NAVY if fill==GOLD else WHITE))
        if i<5: d.arrow(x+w,55,x+128,55,color=GREY,width=1.6)
    d.text(390,108,"The order in which a manager pays redemptions. Each step to the right costs the remaining investors more.",size=8.5,fill=GREY,italic=True)
    return d.svg()

def requests_chart(rows, cap=5.0, title="Q2 2026 redemption requests as % of fund NAV, against the 5% quarterly cap"):
    """rows: list of (label, pct, paid_pct_or_None)"""
    n=len(rows); L=250; R=60; T=48; rowh=24; w=780; h=T+n*rowh+40
    d=D(w,h); pw=w-L-R; vmax=max(r[1] for r in rows)*1.08
    d.text(12,20,title,size=11,fill=NAVY,anchor="start",weight="bold")
    for i,(c,v,paid) in enumerate(rows):
        y=T+i*rowh; bh=rowh-7; bl=pw*v/vmax
        col = GREEN if v<=cap else RED
        d.parts.append(f'<rect x="{L}" y="{y}" width="{bl}" height="{bh}" rx="3" fill="{col}" opacity="0.85"/>')
        if paid is not None:
            d.parts.append(f'<rect x="{L}" y="{y}" width="{pw*paid/vmax}" height="{bh}" rx="3" fill="{NAVY}"/>')
        d.text(L-8,y+bh/2+3.5,c,size=8.6,fill=INK,anchor="end")
        d.text(L+bl+6,y+bh/2+3.5,f"{v:g}%",size=8.3,fill=INK,anchor="start")
    cx=L+pw*cap/vmax
    d.line(cx,T-6,cx,T+n*rowh,color=GOLD,width=2,dash=True)
    d.text(cx+4,T-10,"5% cap",size=8.5,fill=GOLD,anchor="start",weight="bold")
    ly=h-12
    d.parts.append(f'<rect x="{L}" y="{ly-9}" width="10" height="10" rx="2" fill="{NAVY}"/>'); d.text(L+14,ly,"paid (dark)",size=8,fill=GREY,anchor="start")
    d.parts.append(f'<rect x="{L+90}" y="{ly-9}" width="10" height="10" rx="2" fill="{RED}" opacity="0.85"/>'); d.text(L+104,ly,"requested, above cap",size=8,fill=GREY,anchor="start")
    d.parts.append(f'<rect x="{L+230}" y="{ly-9}" width="10" height="10" rx="2" fill="{GREEN}" opacity="0.85"/>'); d.text(L+244,ly,"requested, within cap (paid in full)",size=8,fill=GREY,anchor="start")
    return d.svg()
