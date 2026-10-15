import re, json, subprocess, sys, pymupdf
import diagrams as dg, diagrams4 as d4, event_sources
from svg import fig
def strip(f): return f.split('<div class="cap">')[0].replace('<div class="fig">','')
n=[0]
def F(svg,cap):
    n[0]+=1; return f'<div class="fig">{svg}<div class="cap"><b>Figure {n[0]}.</b> {cap}</div></div>'
css=open("pack_style.css").read()+"""
body{font-size:10.3pt} .big{font-size:11.8pt;line-height:1.5;color:#0b2545}
.tl td:first-child{white-space:nowrap;font-weight:700;color:#0b2545;width:12%}
table.src td:first-child{white-space:nowrap} table.src td{overflow-wrap:anywhere;word-break:normal} table.src{font-size:7pt}
.s{margin-left:1pt} .card{font-size:9.3pt} .card .h{font-size:10pt}
h3{margin-top:12pt}
.keep{break-inside:avoid}
.toc table{font-size:9.6pt} .toc tr.l1 td{padding-top:6pt}
"""
S=event_sources.load()
def build_figs():
    n[0]=0
    wealth_rows=[("Chase UK / J.P. Morgan Personal Investing","from £0; relationship manager above £250,000 (UK)","CCB","App-based banking and investing; the UK version of 'Bank with Chase, Invest with J.P. Morgan'"),
     ("J.P. Morgan Private Client","$750,000+ (US)","CCB","Dedicated banker; First Republic model"),
     ("J.P. Morgan Private Bank","~$10m+ (US); ~£10m UK indicative","AWM","Five-seat team, lending, trusts; ~4,100 advisors"),
     ("International Private Bank","&gt;$20m liquid, per Tejpaul","AWM","Same model run from London, Luxembourg and Switzerland booking centres"),
     ("23 Wall","~700 families, &gt;$4.5tn in aggregate","AWM","Institutional-style coverage, a JV of the investment bank and the Private Bank")]
    slots=[("09:15","Registration, coffee, welcome","Arrive 08:50. Learn two names at your table and what they study. Find out who at the table has applied."),
           ("Morning","Senior leaders on the International Private Bank and the 2027 opportunities","One written question ready (Part 4). Note every number they quote; they will be the ones that matter in the HireVue."),
           ("Late morning","Bankers, investors, specialists: panels and small groups","Ask the banker where their last three clients came from. Ask the investor about the Q3 house view. Write names down."),
           ("Midday","The interactive client scenario","Listen first; both sides of the balance sheet; name the seats; two next steps. Bring the quiet person in."),
           ("Afternoon","Networking, recruiting process, close","Three short conversations beat one long one. Ask the recruiting team what comes next and when. Leave with five names."),
           ("Evening","Home","Write up every name and one line each. Send the thank-you on Tuesday morning, naming one thing one person said.")]
    org=[[("CEO, Asset & Wealth Management","Mary Callahan Erdoes","since 2009")],
         [("Global CEO, Global Private Bank","David Frame","since Jul 2025, New York"),("Exec Chairman GPB; head of 23 Wall","Andrew L. Cohen",""),("CEO, Wealth Management Solutions","Martin Marron","")],
         [("CEO, International Private Bank","Adam Tejpaul","London"),("CEO, Asia Private Bank","Harshika Patel","Hong Kong"),("CEO, EMEA Private Bank","Pablo Garnica","Madrid"),("CEO, Latin America","Edinardo Figueiredo","New York")],
         [("UK, Channel Islands & Ireland","Maricé Brown","since Jun 2025"),("Continental Europe","Sarah Catania","Milan, since Sep 2025"),("Switzerland, Middle East & EM","Karim Rekik","Dubai")],
         [("Investments & Advice","Diana Robinson","London"),("Institutional Wealth Group","Zeynep Ozturk Unlu","London"),("UK North","Khayyam Jumani",""),("FIG","Paul Ferry","from Citi, Nov 2025"),("Team Head","Deepak Chander","team not public"),("Scotland","Gillian Murray","Edinburgh")]]
    return {
     "event_day":F(d4.event_day(slots),"A working plan for the day. The agenda is not public, so the left column is the shape the listing implies; the right column is yours [S700]."),
     "ladder":F(d4.ladder(),"How this document is organised, and what it buys you."),
     "ladder_wealth":F(strip(dg.wealth_continuum(wealth_rows)),"The wealth ladder inside JPMorgan Chase, UK version. Thresholds are indicative; the bank publishes none for the UK [S835][S812][S704][S816]."),
     "firm_org":F(strip(dg.firm_org()),"Where the Private Bank sits: the wealth half of Asset & Wealth Management, next to Asset Management, inside a three-business firm [S900]."),
     "team_model":F(strip(dg.team_model()),"One client, five seats, one owner. The Banker is accountable; the specialists are shared across a team's book [S801][S808]."),
     "pb_revenue":F(strip(dg.pb_revenue()),"The four revenue legs on one client. AWM's 2025 revenue was 72% fees and other income, 28% net interest [S900]."),
     "org":F(d4.org_chart(org),"The International Private Bank as run from London, October 2026. Reporting lines simplified; functional heads (lending, wealth advisory, alternatives, strategy) run across the regions and are listed in the table [S701][S702][S705][S708][S709]."),
     "journey":F(strip(dg.client_journey()),"The client journey from referral to review. The analyst's work sits in discovery preparation, proposals, onboarding and reviews [S575][S810][S830]."),
     "scenario":F(d4.scenario_flow(),"The structure of a client scenario and what the assessors watch. Synthesised from the bank's own planning pages and the documented formats of its student case competitions [S804][S808][S744][S821][S824]."),
     "family":F(d4.family_balance_sheet(),"A worked example of the kind of case a scenario uses. Figures invented for illustration; the logic follows the bank's Private Business Advisory and concentrated-stock pages [S810][S809][S826]."),
     "flywheel":F(strip(dg.flywheel()),"Erdoes' four ingredients for growth (performance, talent, new clients, flows) drawn as the loop they are. A new banker sits in 'talent' and is measured on 'new clients' and 'flows' [S901]."),
    }
ORDER=["p0","p1","p2","p3","p4","p5"]
HEADS=[]
def assemble(pages=None):
    figs=build_figs()
    body=""
    for p in ORDER:
        body+=open(f"event_parts/{p}.html",encoding="utf-8").read()+"\n"
    for k,v in figs.items(): body=body.replace("{{FIG:"+k+"}}",v)
    missing=re.findall(r"\{\{FIG:(\w+)\}\}",body)
    if missing: print("MISSING FIGS",missing,file=sys.stderr)
    # heads for TOC
    heads=[]
    for m in re.finditer(r'<div class="partband" id="(\w+)"><div class="k">(.*?)</div><h1>(.*?)</h1>',body): heads.append((1,m.group(1),m.group(2)+": "+m.group(3)))
    for m in re.finditer(r'<h2 id="(\w+)">(.*?)</h2>',body): heads.append((2,m.group(1),m.group(2)))
    order={i:k for k,(lvl,i,t) in enumerate(heads)}
    # keep document order
    pos=[(body.find(f'id="{i}"'),lvl,i,t) for lvl,i,t in heads]; pos.sort(); heads=[(l,i,t) for _,l,i,t in pos]
    toc="".join(f'<tr class="l{lvl}"><td>{re.sub("<.*?>","",t)}</td><td class="pg">{(pages or {}).get(i,"")}</td></tr>' for lvl,i,t in heads)
    # sources
    used=sorted(set(re.findall(r"\[(S\d+)\]",body)),key=lambda s:int(s[1:]))
    miss=[u for u in used if u not in S]
    if miss: print("WARNING missing source",miss,file=sys.stderr)
    rows="".join(f"<tr><td>{k}</td><td>{S[k][0]}</td><td>{S[k][1]}</td><td>{S[k][2]}</td><td><a href='{S[k][3]}'>{S[k][3]}</a></td><td>{S[k][4]}</td><td>{S[k][5]}</td></tr>" for k in used if k in S)
    src=f'<div class="partband" id="p6"><div class="k">Part 6</div><h1>Sources</h1><div class="d">{len(used)} sources. READ means the page was fetched and read; Snippet only means only a search excerpt was available; PAYWALLED-NOT-READ means headline and date recorded from a public mirror. Confidence reflects how directly the source supports the figures cited.</div></div><table class="src"><tr><th>ID</th><th>Outlet</th><th>Title</th><th>Date</th><th>URL</th><th>Status</th><th>Conf.</th></tr>{rows}</table>'
    body+=src
    cover=f"""<div class="cover" style="height:252mm">
<div class="band"><div class="kicker">Event brief · Inside Private Banking, London · 19 October 2026</div>
<h1>J.P. Morgan's International Private Bank, from the ground up</h1>
<div class="sub">What the Private Bank is, how it is run from London, who runs it, how it makes money, what its strategy is and where it is under strain, what happened this month, how the client scenario works, and the questions to ask each kind of host. Beginner to advanced, with {len(figs)} diagrams and {len(used)} dated sources.</div></div>
<div class="meta"><p><strong>Prepared:</strong> 15 October 2026 for Janak Chohan, penultimate-year Economics, UEA. Public sources only; every number carries a marker that resolves in Part 6. People are described by public professional title only.</p>
<p><strong>Honesty notes:</strong> no account of a previous "Inside Private Banking" day exists in public, so the agenda in Part 0 is inferred from the listing and from the bank's other student events. The London web page still lists Maya Prabhu, who was moved to Asia on 6 October; her UK successor is not verified. Two figures (the 1,900 relationship-manager ambition and the $2bn-a-month alternatives pace) come from single interviews or transcripts and are attributed as such.</p></div></div>
<div class="toc" style="break-after:page"><h2 style="margin-top:0">Contents</h2><table>{toc}</table></div>"""
    svgs=[]
    def keep(m): svgs.append(m.group(0)); return f"@@SVG{len(svgs)-1}@@"
    html=cover+body
    html=re.sub(r"<svg.*?</svg>", keep, html, flags=re.S)
    html=re.sub(r"\[(S\d+)\]", lambda m:f'<span class="s">[{m.group(1)}]</span>', html)
    html=re.sub(r"@@SVG(\d+)@@", lambda m: svgs[int(m.group(1))], html)
    html=re.sub(r'<(?:div class="partband"|h2) id="(\w+)">', lambda m:m.group(0)+f'<span class="anchor">⟦{m.group(1)}⟧</span>', html)
    return f"<!doctype html><html><head><meta charset='utf-8'><title>Inside Private Banking London: Event Brief</title><style>{css}</style></head><body>{html}</body></html>", heads
def find_pages(pdf,heads):
    doc=pymupdf.open(pdf); pages={}
    for lvl,i,t in heads:
        for pno,page in enumerate(doc):
            if page.search_for(f"⟦{i}⟧"): pages[i]=pno+1; break
    return pages
HDR="Inside Private Banking London · event brief"; PREP="Prepared 15 October 2026 · public sources only"
if __name__=="__main__":
    html,heads=assemble()
    open("event_pass1.html","w").write(html)
    subprocess.run(["node","topdf_short.js","event_pass1.html","event_pass1.pdf",HDR,PREP],check=True,capture_output=True)
    pages=find_pages("event_pass1.pdf",heads); print("anchors",len(pages),"of",len(heads))
    html,heads=assemble(pages)
    out="Inside_Private_Banking_London_Event_Brief"
    open(out+".html","w").write(html)
    subprocess.run(["node","topdf_short.js",out+".html",out+".pdf",HDR,PREP],check=True,capture_output=True)
    print("pages",pymupdf.open(out+".pdf").page_count)
