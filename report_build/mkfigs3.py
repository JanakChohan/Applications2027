import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np
D="/home/user/Applications2027/.raw/figs/"
NAVY="#12305c"; TEAL="#1f7a8c"; GOLD="#c8992e"; RED="#a6383a"; GREY="#6b7280"; LGREY="#d8dce3"; BG="#fff"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9,"figure.facecolor":BG,"axes.facecolor":BG,
 "axes.edgecolor":"#9aa2ad","axes.spines.top":False,"axes.spines.right":False})
def save(f,n): f.savefig(D+n,dpi=200,bbox_inches="tight",facecolor=BG); plt.close(f); print("wrote",n)

# FIG 9 — AUM share vs revenue share divergence
f,ax=plt.subplots(figsize=(7.3,4.2))
fam=["Core & Long Duration\n+ Enhanced Cash","Income","Credit & EM\n& High Yield","Alternatives\n& Real Estate","Everything else"]
aum=[28,23,23,4,22]; rev=[14,24,26,25,11]
x=np.arange(len(fam)); w=.38
ax.bar(x-w/2,aum,w,label="Share of AUM (%)",color=LGREY,edgecolor="#aab0b8")
ax.bar(x+w/2,rev,w,label="Share of revenue (%) — ESTIMATED",color=NAVY)
for i,(a,r) in enumerate(zip(aum,rev)):
    ax.text(i-w/2,a+.7,f"{a}%",ha="center",fontsize=7.6)
    ax.text(i+w/2,r+.7,f"{r}%",ha="center",fontsize=7.6,fontweight="bold",color=NAVY)
ax.set_xticks(x); ax.set_xticklabels(fam,fontsize=7.4); ax.set_ylabel("Percent"); ax.set_ylim(0,34)
ax.legend(fontsize=7.6,frameon=False,loc="upper right")
ax.grid(axis="y",ls=":",color=LGREY); ax.set_axisbelow(True)
ax.set_title("Figure 9  Why AUM and revenue rank differently\nAlternatives are ~4% of assets but roughly a quarter of revenue; cheap core bonds are the mirror image",
             loc="left",fontweight="bold",fontsize=10.5)
ax.annotate("",xy=(3.19,25),xytext=(2.81,4),arrowprops=dict(arrowstyle="<->",color=RED,lw=1.6))
ax.text(3.3,15,"6× uplift",fontsize=8,color=RED,fontweight="bold")
ax.text(0,-.30,"AUM shares are from PIMCO at a Glance (30 Jun 2026) regrouped by the author. REVENUE SHARES ARE THE AUTHOR'S ESTIMATE, built by applying\npublished fee rates to each bucket. PIMCO does NOT publish revenue by product. Treat the revenue bars as illustrative of DIRECTION AND ROUGH\nMAGNITUDE ONLY, not as reported figures — see Assumptions Register A5.",transform=ax.transAxes,fontsize=6.8,color=GREY)
save(f,"fig09_aum_vs_revenue.png")

# FIG 10 — role comparison heatmap
f,ax=plt.subplots(figsize=(7.3,4.1))
roles=["Product Analyst\n(R106780)","Account Analyst\n(R106802)","Alternatives Bus.\nMgmt (R106783)","Technology Analyst\n(R106800)"]
crit=["Quantitative\nintensity","Client-facing\n(vs internal)","Coding\nrequirement","Proximity to\ninvestment\ndecisions","Breadth\n(vs depth)","Exit\noptionality"]
M=np.array([[3,3,2,4,4,4],[3,5,1,3,3,3],[3,2,3,3,4,3],[4,1,5,2,2,5]])
im=ax.imshow(M,cmap="YlGnBu",vmin=0,vmax=5,aspect="auto")
ax.set_xticks(range(len(crit))); ax.set_xticklabels(crit,fontsize=7.0,linespacing=1.35)
ax.set_yticks(range(len(roles))); ax.set_yticklabels(roles,fontsize=7.5,linespacing=1.35)
ax.tick_params(axis="x",pad=4); ax.tick_params(axis="y",pad=3)
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        ax.text(j,i,M[i,j],ha="center",va="center",fontsize=11,fontweight="bold",
                color="white" if M[i,j]>=4 else "#12305c")
ax.set_xticks(np.arange(-.5,6,1),minor=True); ax.set_yticks(np.arange(-.5,4,1),minor=True)
ax.grid(which="minor",color="white",lw=2.4); ax.tick_params(which="minor",length=0)
for sp in ax.spines.values(): sp.set_visible(False)
cb=f.colorbar(im,ax=ax,shrink=.68,pad=.025,ticks=[1,2,3,4,5])
cb.ax.set_title("score",fontsize=6.8,color=GREY,pad=6)
cb.ax.tick_params(labelsize=7,length=0)
cb.ax.set_xlabel("1 = low\n5 = high",fontsize=6.6,color=GREY,labelpad=7)
cb.outline.set_visible(False)
ax.set_title("Figure 10  The four London roles, scored side by side",loc="left",fontweight="bold",fontsize=10.5,pad=12)
ax.text(0,-.50,"Scores are the AUTHOR'S JUDGEMENT, derived by reading the four job descriptions closely against the business\nmodel in Part 3. A comparison aid, not a PIMCO rating \u2014 see Assumptions Register A9.",
        transform=ax.transAxes,fontsize=6.8,color=GREY)
save(f,"fig10_role_matrix.png")

# FIG 11 — recruitment funnel/timeline
f,ax=plt.subplots(figsize=(7.4,3.5)); ax.set_xlim(0,10); ax.set_ylim(0,5.2); ax.axis("off")
ax.text(0,4.95,"Figure 11  What PIMCO actually runs — and what it does not",fontsize=11,fontweight="bold")
stages=[("1\nAPPLY","CV upload via\nWorkday. Rolling,\nphased review.","No cover letter\nis requested.",NAVY),
        ("2\nONE-WAY VIDEO","Recorded video\ninterview +\nassessment.","\"interests, skills,\nand personality\"",TEAL),
        ("3\nFINAL ROUND","Live interviews\nby VIDEO\nCONFERENCE.","\"both behavioral\nand technical\"",GOLD),
        ("4\nOFFER","10 weeks,\nearly June –\nmid-August 2027.","Week 1: PIMCO\nFundamentals Training",RED)]
for i,(t,d,n,c) in enumerate(stages):
    x=.15+i*2.48
    ax.add_patch(FancyBboxPatch((x,2.55),2.2,1.6,boxstyle="round,pad=.02,rounding_size=.05",fc=c,ec=c))
    ax.text(x+1.1,3.82,t,ha="center",va="center",fontsize=8.4,color="white",fontweight="bold",linespacing=1.3)
    ax.text(x+1.1,3.05,d,ha="center",va="center",fontsize=7.1,color="white",linespacing=1.45)
    ax.text(x+1.1,2.15,n,ha="center",va="center",fontsize=6.8,color="#333",style="italic",linespacing=1.4)
    if i<3: ax.add_patch(FancyArrowPatch((x+2.22,3.35),(x+2.44,3.35),arrowstyle="-|>",mutation_scale=13,color=GREY,lw=1.6))
ax.add_patch(FancyBboxPatch((.15,.55),9.7,1.05,boxstyle="round,pad=.02,rounding_size=.04",fc="#fdf3f3",ec=RED,lw=1.2))
ax.text(.42,1.29,"NOT mentioned anywhere in PIMCO's own postings:",fontsize=8,fontweight="bold",color=RED)
ax.text(.42,.86,"no numerical/aptitude test  ·  no assessment centre  ·  no in-person superday  ·  no published application deadline  ·  no stated salary",
        fontsize=7.4,color="#5a2426")
ax.text(0,.05,"Verbatim from all four London 2027 postings on PIMCO's Workday portal, accessed 31 Aug 2026. If a forum tells you there is an assessment centre,\nthat is unverified — PIMCO's own text says the final round is a video conference.",fontsize=6.8,color=GREY)
save(f,"fig11_recruitment.png")

# FIG 12 — competitor scatter
f,ax=plt.subplots(figsize=(7.3,4.8))
firms=[("BlackRock",15340,8,"giant",(0,9)),("Vanguard",12000,4,"giant",(0,-15)),
 ("LGIM",1617,15,"uk",(0,9)),("PIMCO",2330,42,"pimco",(0,12)),("Amundi",2600,17,"giant",(6,-15)),
 ("Schroders",1120,45,"uk",(-4,10)),("M&G",480,42,"uk",(0,-15)),
 ("Apollo",600,88,"pc",(14,-4)),("Ares",464,95,"pc",(12,2)),
 ("Blackstone Credit",354,102,"pc",(0,10)),("Oaktree",189,92,"pc",(-2,-15)),("HPS",148,80,"pc",(0,-15))]
colmap={"giant":LGREY,"uk":TEAL,"pimco":RED,"pc":GOLD}
for n,a,fee,k,off in firms:
    ax.scatter(a,fee,s=(300 if k=="pimco" else 140),color=colmap[k],
               edgecolor="white" if k=="pimco" else "#8b929c",lw=1.5,zorder=3)
    ax.annotate(n,(a,fee),xytext=off,textcoords="offset points",ha="center",
                fontsize=7.3,fontweight="bold" if k=="pimco" else "normal",
                color=RED if k=="pimco" else "#2b3440",zorder=4)
ax.set_xscale("log"); ax.set_xlabel("Assets under management (US$bn equivalent, log scale)")
ax.set_ylabel("Approximate blended fee level (bps)")
ax.set_xlim(90,30000); ax.set_ylim(-14,132)
ax.grid(ls=":",color=LGREY); ax.set_axisbelow(True)
ax.set_title("Figure 12  The strategic map — PIMCO sits between the cheap giants and the expensive private-credit houses",
             loc="left",fontweight="bold",fontsize=9.6)
h=[plt.Line2D([],[],marker='o',ls='',color=colmap[k],ms=8,label=l) for k,l in
   [("giant","Scale / passive giants"),("uk","UK & European actives"),("pimco","PIMCO"),("pc","Private credit specialists")]]
ax.legend(handles=h,fontsize=7,frameon=True,facecolor="white",edgecolor=LGREY,loc="lower left",framealpha=.95)
ax.annotate("PIMCO's strategic problem in one picture:\nit must defend the middle — too expensive to\nwin on price, too big to be a boutique",
            xy=(2330,42),xytext=(4300,62),fontsize=6.9,color="#2b3440",
            arrowprops=dict(arrowstyle="->",color=GREY,lw=.9),
            bbox=dict(boxstyle="round,pad=.4",fc="#f7f8fa",ec=LGREY,lw=.8))
ax.text(0,-.215,"AUM: PIMCO 30 Jun 2026 (primary); others from company results and trade press of varying dates 2024–2026 — see the source list for each. FEE LEVELS\nON THE VERTICAL AXIS ARE THE AUTHOR'S ESTIMATES, not published blended rates; they position firms by business model, not by measured revenue\nyield. Private credit firms are plotted on private-credit AUM only, not firm-wide AUM. See Assumptions Register A10.",
        transform=ax.transAxes,fontsize=6.7,color=GREY)
save(f,"fig12_competitors.png")
