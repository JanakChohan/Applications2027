import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np
D="/home/user/Applications2027/.raw/figs/"
NAVY="#12305c"; TEAL="#1f7a8c"; GOLD="#c8992e"; RED="#a6383a"; GREY="#6b7280"; LGREY="#d8dce3"; BG="#fff"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9,"figure.facecolor":BG,"axes.facecolor":BG,
 "axes.edgecolor":"#9aa2ad","axes.spines.top":False,"axes.spines.right":False})
def save(f,n): f.savefig(D+n,dpi=200,bbox_inches="tight",facecolor=BG); plt.close(f); print("wrote",n)
def box(ax,x,y,w,h,t,fc,ec,tc="white",fs=7.6,fw="bold"):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.012,rounding_size=0.02",
        fc=fc,ec=ec,lw=1.1,zorder=2))
    ax.text(x+w/2,y+h/2,t,ha="center",va="center",fontsize=fs,color=tc,fontweight=fw,zorder=3,linespacing=1.45)
def arr(ax,p1,p2,c=NAVY,lw=1.5,style="-|>"):
    ax.add_patch(FancyArrowPatch(p1,p2,arrowstyle=style,mutation_scale=13,color=c,lw=lw,zorder=1,
        shrinkA=1,shrinkB=1))

# FIG 6 — bond price/yield seesaw
f,(a1,a2)=plt.subplots(1,2,figsize=(7.3,3.0),gridspec_kw={"wspace":.28})
y=np.linspace(1,9,200); p=100*(1+ (5-y)/100*7)
a1.plot(y,p,color=NAVY,lw=2.4)
a1.axvline(5,color=LGREY,ls="--"); a1.axhline(100,color=LGREY,ls="--")
a1.plot([5],[100],"o",color=GOLD,ms=9,zorder=5)
a1.annotate("Bond issued at\n5% coupon, price 100",xy=(5,100),xytext=(5.9,112),fontsize=7,
  arrowprops=dict(arrowstyle="->",color=GREY,lw=.9))
a1.annotate("Yields RISE →\nprice FALLS",xy=(7.5,82),fontsize=7.4,color=RED,fontweight="bold")
a1.annotate("Yields FALL →\nprice RISES",xy=(1.6,113),fontsize=7.4,color=TEAL,fontweight="bold")
a1.set_xlabel("Market yield (%)"); a1.set_ylabel("Bond price"); a1.set_title("The see-saw: price vs yield",fontsize=9,loc="left",fontweight="bold")
a1.grid(ls=":",color=LGREY); a1.set_axisbelow(True)
dur=[2,6,10,20]; ch=[-2,-6,-10,-20]
a2.barh([f"{d}-year\nduration" for d in dur],ch,color=[LGREY,TEAL,NAVY,RED],height=.6)
for i,c in enumerate(ch): a2.text(c-.9,i,f"{c}%",va="center",ha="right",fontsize=8,fontweight="bold")
a2.set_xlabel("Approx. price change if yields rise by 1%"); a2.set_xlim(-25,2)
a2.axvline(0,color="#333",lw=.9)
a2.set_title("Duration = how much it hurts",fontsize=9,loc="left",fontweight="bold")
a2.grid(axis="x",ls=":",color=LGREY); a2.set_axisbelow(True)
f.suptitle("Figure 6  The two bond mechanics you must understand before an interview",fontweight="bold",fontsize=10.5,x=.011,ha="left",y=1.05)
f.text(.011,-.10,"Illustrative, not market data. Rule of thumb: price change ≈ −duration × change in yield. Author's illustration.",fontsize=6.9,color=GREY)
save(f,"fig06_bond_mechanics.png")

# FIG 7 — MONEY FLOW DIAGRAM
f,ax=plt.subplots(figsize=(7.4,7.4)); ax.set_xlim(-0.6,10); ax.set_ylim(0,15.4); ax.axis("off")
box(ax,.4,14.1,9.2,1.0,"UK PENSION FUND  •  £500 million mandate\n\"Global Aggregate bonds, benchmark-relative, ESG screen\"",NAVY,NAVY,fs=8.6)
arr(ax,(5,14.1),(5,13.5))
box(ax,.4,12.5,9.2,.95,"1.  WON  —  Consultant Relations + Client Management (London)\nRFP response, fee negotiation, investment management agreement signed",TEAL,TEAL,fs=7.5)
arr(ax,(5,12.5),(5,11.9))
box(ax,.4,10.9,9.2,.95,"2.  ONBOARDED  —  Legal, Compliance, Operations, Client Onboarding\nGuidelines coded into systems; custodian appointed; account opened",GOLD,GOLD,fs=7.5)
arr(ax,(5,10.9),(5,10.3))
box(ax,.4,9.05,9.2,1.15,"3.  INVESTED  —  Portfolio Management\nInvestment Committee house view → sector desks (rates, credit, mortgages, EM)\n→ portfolio manager builds the £500m portfolio → Trading desk executes",NAVY,NAVY,fs=7.5)
arr(ax,(5,9.05),(5,8.45))
box(ax,.4,7.2,9.2,1.15,"4.  MONITORED  —  Risk Management, Analytics, Investment Support\nDaily risk and guideline checks • performance and attribution calculated\n• Technology runs the systems all of this sits on",TEAL,TEAL,fs=7.5)
arr(ax,(5,7.2),(5,6.6))
box(ax,.4,5.25,9.2,1.15,"5.  BILLED  —  Finance / Billing\n£500m × 0.30% per annum ÷ 4  =  £375,000 invoiced this quarter\nBilled quarterly in arrears on market value  →  THIS IS PIMCO'S REVENUE",RED,RED,fs=7.8)
arr(ax,(5,5.25),(5,4.65))
box(ax,.4,3.5,9.2,1.05,"6.  SERVICED  —  Account Management + Product Strategy (London)\nQuarterly report, attribution, market outlook, review meeting\nGoal: client stays. Every year they stay, the fee repeats.",GOLD,GOLD,fs=7.5)
arr(ax,(5,3.5),(5,2.9))
box(ax,.4,1.85,9.2,.95,"7.  RECOGNISED  —  Allianz Asset Management segment\nRevenue → less costs (≈60%) → operating profit → Allianz Group accounts",NAVY,NAVY,fs=7.5)
# feedback loop
ax.add_patch(FancyArrowPatch((.4,4.02),(.10,4.02),arrowstyle="-",color=GREY,lw=1.2,ls="--"))
ax.add_patch(FancyArrowPatch((.10,4.02),(.10,13.0),arrowstyle="-",color=GREY,lw=1.2,ls="--"))
ax.add_patch(FancyArrowPatch((.10,13.0),(.4,13.0),arrowstyle="-|>",mutation_scale=13,color=GREY,lw=1.2,ls="--"))
ax.text(-.30,8.5,"RETENTION LOOP",rotation=90,fontsize=7.4,color=GREY,ha="center",va="center",fontweight="bold")
ax.text(.02,8.5,"good service and performance win the next mandate",rotation=90,fontsize=6.6,color=GREY,ha="center",va="center")
ax.text(0,.95,"Figure 7   Following one pound from a UK pension fund into PIMCO revenue",fontsize=11,fontweight="bold",color="#1c2430")
ax.text(0,.35,"Fee rate is PIMCO's published Total Return separate-account rack rate (first tier, Form ADV Appendix B, 2026 brochure). The £500m mandate,\nthe strategy and the £375,000 figure are a worked illustration by the author, not a real PIMCO client — see Assumptions Register A7.",
        fontsize=6.9,color=GREY)
save(f,"fig07_money_flow.png")

# FIG 8 — ORG MAP
f,ax=plt.subplots(figsize=(7.4,6.4)); ax.set_xlim(0,10); ax.set_ylim(0,11.2); ax.axis("off")
ax.text(0,10.85,"Figure 8   The firm mapped by how each division touches revenue",fontsize=11,fontweight="bold")
ax.text(0,10.45,"Colour = economic role. This is the honest version: only two groups actually bring money in.",fontsize=7.8,color=GREY)
# legend
for i,(c,l) in enumerate([(NAVY,"REVENUE CENTRE — wins or keeps the fee"),(TEAL,"REVENUE ENABLER — the fee is unearnable without it"),(GREY,"COST CENTRE — necessary, not billable")]):
    ax.add_patch(Rectangle((0.05+i*3.35,9.75),.28,.28,fc=c,ec=c)); ax.text(0.42+i*3.35,9.89,l,fontsize=6.6,va="center")
rows=[
 (8.6,[("Client Management /\nAccount Management",NAVY),("Global Wealth\nManagement",NAVY),("Consultant\nRelations",NAVY)]),
 (7.25,[("Product Strategy Group\n(130+ globally)",NAVY),("Portfolio Management\n+ sector desks",TEAL),("Investment Committee\n& Forums",TEAL)]),
 (5.9,[("Trading / Execution\n(8 desks, all time zones)",TEAL),("Analytics & Quantitative\nResearch",TEAL),("Client Solutions\n& Analytics",TEAL)]),
 (4.55,[("Risk Management",TEAL),("Technology &\nEngineering",TEAL),("Operations /\nInvestment Support",TEAL)]),
 (3.2,[("Legal & Compliance",GREY),("Finance / Billing",GREY),("HR / People\nOperations",GREY)]),
]
for y,items in rows:
    for j,(t,c) in enumerate(items):
        box(ax,.12+j*3.32,y,3.05,1.08,t,c,c,fs=7.2)
ax.text(0,2.35,"Where the four London 2027 internships sit:",fontsize=8.4,fontweight="bold",color=NAVY)
notes=[("Product Analyst","Product Strategy Group — revenue centre, one step from the client and the portfolio"),
 ("Account Analyst","Client Management — revenue centre, retention and cross-sell"),
 ("Alternatives Business Mgmt","Alternatives business operations — enabler wrapped around the highest-fee products"),
 ("Technology Analyst","Technology — enabler; internal-use systems for the trade floor")]
for i,(a,b) in enumerate(notes):
    ax.text(.12,1.92-i*.45,"▪ ",fontsize=8,color=GOLD,va="center")
    ax.text(.42,1.92-i*.45,a,fontsize=7.4,fontweight="bold",va="center")
    ax.text(3.05,1.92-i*.45,b,fontsize=7.0,color="#333",va="center")
ax.text(0,-.15,"Classification is the author's analytical judgement, applied consistently — it is not a PIMCO-published org chart. Team names and the\n'130+' Product Strategy Group figure are taken from PIMCO job postings and pimco.com. See Assumptions Register A8.",fontsize=6.8,color=GREY)
save(f,"fig08_org_map.png")
