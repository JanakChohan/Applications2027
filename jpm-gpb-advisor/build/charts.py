from svg import *
S1="#2f6fb2"; S2="#c9932a"; S3="#1baf7a"; INK="#1c2330"; INK2="#52514e"; GRID="#e3e6eb"

def bars(title, cats, series, unit="", w=760, h=300, fmt=lambda v: f"{v:g}", ymax=None, note=None, colors=(S1,S2,S3)):
    """Grouped vertical bars. series: list of (name, [values])."""
    d=D(w,h)
    L,R,T,B=54,16,44,52
    pw=w-L-R; ph=h-T-B
    allv=[v for _,vals in series for v in vals if v is not None]
    ymax=ymax or max(allv)*1.15
    d.text(L,20,title,size=11.5,fill=NAVY,anchor="start",weight="bold")
    # grid
    for i in range(5):
        y=T+ph-ph*i/4; val=ymax*i/4
        d.line(L,y,L+pw,y,color=GRID,width=1)
        d.text(L-6,y+3.5,fmt(val)+unit,size=8,fill=INK2,anchor="end")
    n=len(cats); k=len(series); gw=pw/n; bw=min(34,(gw*0.72)/k)
    for i,c in enumerate(cats):
        x0=L+gw*i+(gw-bw*k-2*(k-1))/2
        for j,(name,vals) in enumerate(series):
            v=vals[i]
            if v is None: continue
            bh=ph*v/ymax; x=x0+j*(bw+2); y=T+ph-bh
            d.parts.append(f'<path d="M{x},{T+ph} L{x},{y+4} Q{x},{y} {x+4},{y} L{x+bw-4},{y} Q{x+bw},{y} {x+bw},{y+4} L{x+bw},{T+ph} Z" fill="{colors[j]}"/>')
            d.text(x+bw/2,y-4,fmt(v),size=8,fill=INK)
        d.text(L+gw*i+gw/2,T+ph+14,c,size=8.5,fill=INK2)
    d.line(L,T+ph,L+pw,T+ph,color="#b9c0cc",width=1)
    # legend
    if k>1:
        x=L
        for j,(name,_) in enumerate(series):
            d.parts.append(f'<rect x="{x}" y="{T+ph+26}" width="10" height="10" rx="2" fill="{colors[j]}"/>')
            d.text(x+14,T+ph+35,name,size=8.5,fill=INK2,anchor="start"); x+=14+len(name)*5.2+16
    if note: d.text(L+pw,T+ph+35,note,size=7.8,fill=INK2,anchor="end",italic=True)
    return d.svg()

def hbars(title, cats, vals, unit="", w=760, rowh=22, fmt=lambda v: f"{v:g}", color=S1, highlight=None, note=None):
    n=len(cats); L=190; R=70; T=34; h=T+n*rowh+30
    d=D(w,h); pw=w-L-R; vmax=max(vals)*1.08
    d.text(12,20,title,size=11.5,fill=NAVY,anchor="start",weight="bold")
    for i,(c,v) in enumerate(zip(cats,vals)):
        y=T+i*rowh; bh=rowh-6; bl=pw*v/vmax
        col = S2 if (highlight and c==highlight) else color
        d.parts.append(f'<path d="M{L},{y} L{L+bl-4},{y} Q{L+bl},{y} {L+bl},{y+4} L{L+bl},{y+bh-4} Q{L+bl},{y+bh} {L+bl-4},{y+bh} L{L},{y+bh} Z" fill="{col}"/>')
        d.text(L-8,y+bh/2+3.5,c,size=8.6,fill=INK,anchor="end",weight="bold" if c==highlight else "normal")
        d.text(L+bl+6,y+bh/2+3.5,fmt(v)+unit,size=8.3,fill=INK,anchor="start")
    if note: d.text(w-12,h-8,note,size=7.8,fill=INK2,anchor="end",italic=True)
    return d.svg()

def timeline(events, w=780):
    """events: list of (year_label, [ (text, kind) ])  kind in {'firm','awm','deal','macro'}"""
    col={'firm':NAVY,'awm':GOLD,'deal':S1,'macro':GREY}
    n=len(events); cw=(w-20)/n; rows=max(len(e[1]) for e in events)
    h=70+rows*46
    d=D(w,h)
    d.line(10,40,w-10,40,color=NAVY,width=2.5)
    for i,(yr,items) in enumerate(events):
        x=10+cw*i+cw/2
        d.circle(x,40,6,fill=NAVY)
        d.text(x,24,yr,size=11,fill=NAVY,weight="bold")
        for j,(t,k) in enumerate(items):
            y=58+j*46
            d.box(x-cw/2+4,y,cw-8,40,t,None,fill=WHITE,tfill=INK,stroke=col[k],tsize=7.6,tweight="normal",r=4)
    # legend
    lx=10; ly=h-8
    for k,lab in [('firm','Firm'),('awm','AWM / Private Bank'),('deal','Deal or investment'),('macro','Macro / regulatory')]:
        d.parts.append(f'<rect x="{lx}" y="{ly-9}" width="10" height="10" rx="2" fill="none" stroke="{col[k]}" stroke-width="1.5"/>')
        d.text(lx+14,ly,lab,size=8,fill=INK2,anchor="start"); lx+=14+len(lab)*5+16
    return d.svg()

def jcurve():
    d=D(700,300)
    L,T,W,H=60,30,600,220
    d.line(L,T+H*0.55,L+W,T+H*0.55,color="#b9c0cc",width=1)
    d.text(L-6,T+H*0.55+3,"break-even",size=8,fill=INK2,anchor="end")
    d.line(L,T,L,T+H,color="#b9c0cc",width=1); d.line(L,T+H,L+W,T+H,color="#b9c0cc",width=1)
    # curve: dips then rises
    path=f"M{L},{T+H*0.55} C{L+W*0.15},{T+H*0.95} {L+W*0.3},{T+H*0.9} {L+W*0.42},{T+H*0.55} S{L+W*0.75},{T+H*0.05} {L+W},{T+H*0.0}"
    d.parts.append(f'<path d="{path}" fill="none" stroke="{S1}" stroke-width="2.5"/>')
    for frac,lab in [(0,"Year 0: hire"),(0.42,"Year 3 or earlier: break-even"),(0.7,"Year 5: payback"),(1.0,"Mature advisor")]:
        x=L+W*frac; d.line(x,T,x,T+H,color=GRID,width=1,dash=True)
        d.text(x,T+H+14,lab,size=8.3,fill=INK2)
    d.text(L+W*0.2,T+H*0.98,"Training, salary, no book yet",size=8.3,fill=INK2,italic=True)
    d.text(L+W*0.78,T+H*0.18,"Referrals compound;",size=8.3,fill=INK2,italic=True)
    d.text(L+W*0.78,T+H*0.28,"revenue per banker rising",size=8.3,fill=INK2,italic=True)
    d.text(18,T+H/2,"Cumulative profit from one advisor",size=8.5,fill=INK2,anchor="middle")
    d.parts[-1]=d.parts[-1].replace('<text ','<text transform="rotate(-90 18 %d)" '%(T+H/2))
    d.text(L+W/2,T+H+40,"Erdoes (Investor Day 2022): 'productivity doubles after they've been here for a year... breakevens in year three or earlier... paybacks in year five'",size=8.2,fill=NAVY,italic=True)
    return d.svg()

def awm_hierarchy():
    d=D(780,470)
    d.box(280,10,220,50,"Mary Callahan Erdoes","CEO, Asset & Wealth Management (since 2009)",fill=NAVY)
    d.box(40,95,220,50,"George Gatch","CEO, Asset Management",fill=NAVY2)
    d.box(280,95,220,50,"David Frame","Global CEO, Global Private Bank (Jul 2025)",fill=GOLD)
    d.box(520,95,220,50,"Martin Marron","CEO, Wealth Management Solutions (advice and product platform for PB and Chase)",fill=NAVY2,bsize=7.8)
    for x in (150,390,630): d.arrow(390,60,x,95,color=GREY)
    # under GPB
    d.box(160,180,200,50,"Adam Tejpaul","CEO, International Private Bank (London)",fill=GOLD)
    d.box(400,180,200,50,"US Private Bank","(Frame retains oversight)",fill=WHITE,tfill=NAVY,stroke=GOLD)
    d.box(620,180,150,50,"Andrew L. Cohen","Exec Chairman GPB; head of 23 Wall",fill=WHITE,tfill=NAVY,stroke=GOLD,bsize=7.8)
    for x in (260,500,695): d.arrow(390,145,x,180,color=GREY)
    # regions
    regions=[("Pablo Garnica","CEO EMEA Private Bank (Madrid)"),("Harshika Patel","CEO Asia"),("Edinardo Figueiredo","CEO Latin America")]
    x=40
    for t,b in regions:
        d.box(x,265,200,46,t,b,fill=WHITE,tfill=NAVY,stroke=LINE); d.arrow(260,230,x+100,265,color=GREY); x+=230
    # UK under EMEA
    uk=[("Maricé Brown","Region Head UK, Channel Islands & Ireland (from Q3 2025)"),("Sarah Catania","Head of Continental Europe (Milan, Sep 2025)"),("Karim Rekik","Head of Middle East & Emerging Markets")]
    x=40
    for t,b in uk:
        d.box(x,350,200,46,t,b,fill=WHITE,tfill=NAVY,stroke=LINE,bsize=7.8); d.arrow(140,311,x+100,350,color=GREY); x+=230
    d.region(10,412,760,50,"",fill=BG,dash=False)
    d.text(390,430,"London team leads (60 Victoria Embankment): Diana Robinson (Investments & Advice UK) · Maya Prabhu (UK Domestic & Crown Dependencies)",size=8,fill=INK2)
    d.text(390,444,"Khayyam Jumani (UK North) · Paul Ferry (Financial Institutions, ex-Citi, Nov 2025) · Zeynep Ozturk Unlu (Institutional Wealth Group) · James Chilvers (UK Wealth Advisory)",size=8,fill=INK2)
    return d.svg()

def firm_leadership():
    d=D(780,300)
    d.box(280,10,220,50,"Jamie Dimon","Chairman & CEO (since 2005). Expects 'a few years' more, then Executive Chairman.",fill=NAVY,bsize=7.8)
    d.box(60,95,200,50,"Doug Petno","Co-President; CEO Commercial & Investment Bank (Jun 2026)",fill=NAVY2,bsize=7.8)
    d.box(290,95,200,50,"Troy Rohrbaugh","Co-President; CEO Consumer & Community Banking (Jun 2026)",fill=NAVY2,bsize=7.8)
    d.box(520,95,200,50,"Mary Callahan Erdoes","CEO Asset & Wealth Management (since 2009)",fill=GOLD,bsize=7.8)
    for x in (160,390,620): d.arrow(390,60,x,95,color=GREY)
    d.box(60,180,200,46,"Jennifer Piepszak","Chief Operating Officer (Jan 2025): tech, ops, data, strategy",fill=WHITE,tfill=NAVY,stroke=LINE,bsize=7.6)
    d.box(290,180,200,46,"Jeremy Barnum","Chief Financial Officer",fill=WHITE,tfill=NAVY,stroke=LINE)
    d.box(520,180,200,46,"Daniel Pinto","Vice Chairman; retiring end-2026",fill=WHITE,tfill=NAVY,stroke=LINE)
    d.text(390,262,"Marianne Lake (CEO CCB 2024 to Jun 2026) retired when the co-presidents were named. The two co-presidents are the visible successor candidates.",size=8.3,fill=INK2,italic=True)
    d.text(390,278,"Retention awards (June 2026): ~$30m each to Petno and Rohrbaugh; $20m each to Piepszak and Erdoes.",size=8.3,fill=INK2,italic=True)
    return d.svg()

def one_firm():
    d=D(760,400)
    cx,cy=380,200
    d.circle(cx,cy,62,fill=GOLD)
    d.text(cx,194,"GLOBAL",size=11,fill="#fff",weight="bold"); d.text(cx,208,"PRIVATE BANK",size=11,fill="#fff",weight="bold")
    nodes=[("Investment Bank","IPOs, company sales, founders and CEOs with new liquidity; 10b5-1 share programmes",cx,40),
           ("Commercial Bank","60,000 mid-sized company owners; 'innovation economy' founders; 42% of cap tables",cx+280,130),
           ("Chase branches","'2,000 private banking clients walk into those branches every day'; clients who outgrow Chase Wealth",cx+280,290),
           ("Asset Management","Funds, ETFs, alternatives and money-market products on the Private Bank shelf; institutional contacts",cx,360),
           ("Markets / Payments","Execution, structured notes, FX, custody, cross-border payments for private clients",cx-280,290),
           ("Workplace (Global Shares)","1.8m employee shareholders; $372bn of equity plans: tomorrow's wealthy clients",cx-280,130)]
    for t,b,x,y in nodes:
        d.box(x-110,y-30,220,60,t,b,fill=NAVY2,tsize=9.5,bsize=7.6)
        # arrows both ways
        dx,dy=cx-x,cy-y; L=(dx*dx+dy*dy)**0.5; ux,uy=dx/L,dy/L
        d.arrow(x+ux*40,y+uy*30,cx-ux*66,cy-uy*66,color=GOLD,marker="arrg",width=1.6)
    return d.svg()

def emea_map_list():
    d=D(760,150)
    groups=[("United Kingdom","London (HQ) · Manchester · Edinburgh · Glasgow · Bournemouth"),
            ("Continental Europe","Paris · Frankfurt · Munich · Hamburg · Berlin · Milan · Madrid · Luxembourg · Brussels · Amsterdam · Stockholm · Copenhagen · Athens"),
            ("Switzerland","Geneva · Zurich (J.P. Morgan (Suisse) SA booking centre)"),
            ("Middle East","Dubai (DIFC) · Riyadh (regional HQ licence Oct 2025) · Doha")]
    y=10
    for t,b in groups:
        d.box(10,y,150,30,t,None,fill=NAVY,tsize=9)
        d.box(170,y,580,30,b,None,fill=BG,tfill=INK,stroke=LINE,tsize=8.4,tweight="normal")
        y+=35
    return d.svg()

if __name__=="__main__":
    print(len(bars("t",["a","b"],[("x",[1,2]),("y",[2,3])])))
