import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np, os
D="/home/user/Applications2027/.raw/figs/"
NAVY="#12305c"; TEAL="#1f7a8c"; GOLD="#c8992e"; RED="#a6383a"; GREY="#6b7280"; LGREY="#d8dce3"; BG="#ffffff"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9,"axes.edgecolor":"#9aa2ad",
  "axes.labelcolor":"#1c2430","text.color":"#1c2430","xtick.color":"#48505c","ytick.color":"#48505c",
  "axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":BG,"axes.facecolor":BG})
def save(f,n):
    f.savefig(D+n,dpi=200,bbox_inches="tight",facecolor=BG); plt.close(f); print("wrote",n)

# FIG 1 — AUM growth by decade (log)
f,ax=plt.subplots(figsize=(7.2,3.4))
dec=["1970s","1980s","1990s","2000s","2010s","2020s\n(now)"]
val=[0.185,10.1,84.3,530.1,1300,2330]
b=ax.bar(dec,val,color=[LGREY,LGREY,TEAL,TEAL,NAVY,NAVY],width=.62)
ax.set_yscale("log"); ax.set_ylabel("AUM (US$ billions, log scale)")
ax.set_title("Figure 1  PIMCO assets under management by decade\nLog scale — each gridline is a 10× jump",loc="left",fontweight="bold",fontsize=10.5)
lab=["$185m","$10.1bn","$84.3bn","$530bn","$1.30tn","$2.33tn"]
for r,l in zip(b,lab): ax.text(r.get_x()+r.get_width()/2,r.get_height()*1.28,l,ha="center",fontsize=8.4,fontweight="bold")
ax.set_ylim(0.09,9000); ax.grid(axis="y",ls=":",color=LGREY,alpha=.9); ax.set_axisbelow(True)
ax.text(0,-.22,"Source: PIMCO 'About Us' decade milestones and PIMCO at a Glance, 30 June 2026. Accessed 31 Aug 2026.",
        transform=ax.transAxes,fontsize=7,color=GREY)
save(f,"fig01_aum_growth.png")

# FIG 2 — AUM by strategy
f,ax=plt.subplots(figsize=(7.2,4.6))
s=[("Income",23),("Credit",15),("Core",13),("Long Duration",9),("Global",8),("Enhanced Cash",6),
   ("Municipals",4),("Real Return",4),("Securitized",4),("Emerging Markets",4),("Equity",3),
   ("Alternatives",3),("Asset Allocation",3),("Absolute Return",1),("Cashflow Driven Inv.",0.4)]
n=[x[0] for x in s][::-1]; v=[x[1] for x in s][::-1]
cols=[NAVY if x>=13 else (TEAL if x>=4 else LGREY) for x in v]
ax.barh(n,v,color=cols,height=.68)
for i,x in enumerate(v):
    ax.text(x+.35,i,("<0.5%" if x<1 else f"{x:g}%"),va="center",fontsize=8.2,fontweight="bold")
ax.set_xlabel("% of third-party AUM"); ax.set_xlim(0,26)
ax.set_title("Figure 2  What PIMCO actually manages, by strategy\nShare of $1.92tn third-party assets, 30 June 2026",loc="left",fontweight="bold",fontsize=10.5)
ax.grid(axis="x",ls=":",color=LGREY); ax.set_axisbelow(True)
ax.text(0,-.13,"Income + Credit + Core = 51% of third-party assets. Source: PIMCO at a Glance, 30 June 2026.",
        transform=ax.transAxes,fontsize=7,color=GREY)
save(f,"fig02_aum_strategy.png")

# FIG 3 — Allianz AM segment 5yr
f,(a1,a2)=plt.subplots(1,2,figsize=(7.4,3.3),gridspec_kw={"wspace":.32})
yr=["2021","2022","2023","2024","2025"]
rev=[8.4,8.2,8.1,8.3,8.5]; op=[3.5,3.2,3.1,3.2,3.3]; cir=[58.4,61.2,61.3,61.1,60.7]
x=np.arange(5); w=.38
a1.bar(x-w/2,rev,w,label="Operating revenues",color=NAVY)
a1.bar(x+w/2,op,w,label="Operating profit",color=TEAL)
a1.set_xticks(x); a1.set_xticklabels(yr); a1.set_ylabel("€ billions"); a1.set_ylim(0,10)
a1.legend(fontsize=7.2,frameon=False,loc="upper center",ncol=2,bbox_to_anchor=(.5,1.02))
a1.grid(axis="y",ls=":",color=LGREY); a1.set_axisbelow(True)
for i,(r,o) in enumerate(zip(rev,op)):
    a1.text(i-w/2,r+.15,f"{r}",ha="center",fontsize=7.2); a1.text(i+w/2,o+.15,f"{o}",ha="center",fontsize=7.2)
a1.set_title("Revenue and profit (€bn)",fontsize=9,loc="left")
a2.plot(x,cir,"o-",color=RED,lw=2,ms=6)
a2.set_xticks(x); a2.set_xticklabels(yr); a2.set_ylabel("Cost-income ratio (%)"); a2.set_ylim(56,63)
for i,c in enumerate(cir): a2.text(i,c+.28,f"{c}%",ha="center",fontsize=7.4,fontweight="bold")
a2.grid(axis="y",ls=":",color=LGREY); a2.set_axisbelow(True)
a2.set_title("Cost-income ratio — lower is better",fontsize=9,loc="left")
a2.annotate("2022 bond crash:\ncosts stayed, revenue fell",xy=(1,61.2),xytext=(1.35,57.4),fontsize=6.8,color=RED,
            arrowprops=dict(arrowstyle="->",color=RED,lw=.9))
f.suptitle("Figure 3  Allianz Asset Management segment (PIMCO + AllianzGI), 2021–2025",
           fontweight="bold",fontsize=10.5,x=.011,ha="left",y=1.06)
f.text(.011,-.09,"2021 revenue is derived (operating profit ÷ (1 − CIR)) — see Assumptions Register A3. Segment combines PIMCO and Allianz Global Investors;\nAllianz does not publish a standalone PIMCO P&L. Source: Allianz FY earnings releases 2022–2026.",fontsize=6.8,color=GREY)
save(f,"fig03_allianz_segment.png")

# FIG 4 — flows vs markets
f,ax=plt.subplots(figsize=(7.2,3.4))
yr2=["2022","2023","2024","2025","1H 2026"]
flows=[-81.4,21,84.8,139,84]
ax.bar(yr2,flows,color=[RED if v<0 else TEAL for v in flows],width=.6)
ax.axhline(0,color="#333",lw=.9)
for i,v in enumerate(flows):
    ax.text(i,v+(7 if v>0 else -14),f"{v:+g}",ha="center",fontweight="bold",fontsize=8.6,
            color=RED if v<0 else NAVY)
ax.set_ylabel("Third-party net flows (€bn)"); ax.set_ylim(-105,165)
ax.set_title("Figure 4  Net flows are the number that matters\nAllianz Asset Management segment third-party net flows",loc="left",fontweight="bold",fontsize=10.5)
ax.grid(axis="y",ls=":",color=LGREY); ax.set_axisbelow(True)
ax.text(0,-.19,"2023 (+€21bn) is derived from Allianz's statement that 2024 inflows were 'almost four times the prior year level' — see Assumptions Register A4.\nSource: Allianz FY2022–FY2025 and 2Q 2026 earnings releases.",transform=ax.transAxes,fontsize=6.9,color=GREY)
save(f,"fig04_flows.png")

# FIG 5 — fee ladder
f,ax=plt.subplots(figsize=(7.3,4.4))
items=[("Money market (separate acct)",11.25,LGREY),("Municipal cash / short term",15.0,LGREY),
 ("Short Term",20.0,LGREY),("Low Duration / Mortgage / Real Return US",25.0,TEAL),
 ("Total Return — flagship core",30.0,TEAL),("Global Bond / Global IG",35.0,TEAL),
 ("Emerging Market Bonds",45.0,TEAL),("High Yield",50.0,TEAL),
 ("Credit Opportunities",60.0,NAVY),("Capital Securities",70.0,NAVY),
 ("PIMCO Income Fund (US mutual fund)",60.0,GOLD),
 ("Typical private credit fund\n(mgmt fee only, before carry)",150.0,RED)]
n=[i[0] for i in items][::-1]; v=[i[1] for i in items][::-1]; c=[i[2] for i in items][::-1]
ax.barh(n,v,color=c,height=.66)
for i,x in enumerate(v): ax.text(x+2.5,i,f"{x:g} bps",va="center",fontsize=8,fontweight="bold")
ax.set_xlabel("Annual fee, basis points (100 bps = 1.00%)"); ax.set_xlim(0,180)
ax.set_title("Figure 5  The fee ladder — why PIMCO's effort follows the money\nTop-tier institutional rack rates vs. retail fund vs. private credit",loc="left",fontweight="bold",fontsize=10.5)
ax.grid(axis="x",ls=":",color=LGREY); ax.set_axisbelow(True)
ax.text(0,-.155,"Grey/teal/navy = PIMCO Form ADV Appendix B separate-account rack rates (first tier), 2026 brochure. Gold = PIMCO Income Fund adjusted expense\nratio, 30 Jun 2026. Red = illustrative industry norm for private credit management fees, NOT a PIMCO-published rate — see Assumptions Register A6.",
        transform=ax.transAxes,fontsize=6.8,color=GREY)
save(f,"fig05_fee_ladder.png")
