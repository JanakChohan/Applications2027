#!/usr/bin/env python3
"""Figures for Parts 1, 3, 6, 9, 12 and the master diagram (role, team, process)."""
import os
from svglib import *

ROOT = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(ROOT, "fragments")


def save(name, s):
    open(os.path.join(FR, f"fig_{name}.html"), "w").write(s)


def valuechain():
    out = [arrow_defs("vc")]
    steps = [("Client need", "a DC scheme wants private assets in its default fund", WASH, INK),
             ("Value Proposition", "reads trends and rivals; shapes the offer with investment teams (e.g. an LTAF)", S[1], "#fff"),
             ("Approval", "Product governance, target market, compliance sign-off on materials", HARD, "#fff"),
             ("Sales Activation", "RM and consultant meetings, RFP and DDQ, pitch, events", S[0], "#fff"),
             ("Delivery", "Salesforce pipeline, data, reporting, campaign tracking", S[2], "#fff"),
             ("Outcome", "mandate won, assets retained, client served; NNB and revenue", NAVY, "#fff")]
    w = 104
    for i, (t, sub, col, tc) in enumerate(steps):
        x = 4 + i * (w + 10)
        out.append(box(x, 16, w, 132, t, col, col if col != WASH else LINE, tc, 11, 700, sub=sub, subsize=9, subcol=tc if tc == "#fff" else INK2))
        if i < 5:
            out.append(line(x + w + 1, 82, x + w + 9, 82, "vc"))
    out.append(path("M620,150 C620,200 60,200 60,152", "vc", ACC, 1.4, dash="5 3", accent=True))
    out.append(text(340, 196, "Feedback loop: what clients say in meetings goes back into the next proposition", 10, ACC, "middle", 600)[0])
    out.append(text(340, 222, "Intern touchpoints: competitor screens, pitch-book updates, DDQ chasing, meeting notes into Salesforce, event logistics", 9.5, INK2, "middle")[0])
    save("valuechain", figure(svg(680, 230, "".join(out)),
        "The role's value chain, from client need to outcome, using the JD's three pillars [S263]. The LTAF example is modelled on the Mercer mandate [S71]; the sequence is the author's [Inferred]."))


def channels():
    out = [arrow_defs("ch")]
    out.append(box(250, 6, 180, 40, "Schroders Client Group", S[1], S[1], "#fff", 12, 700))
    chans = [("Institutional", "64% of AUM", "Direct and via consultants: DB, DC, LGPS pools, insurers, official institutions", S[0]),
             ("Intermediary", "19% of AUM", "Wealth managers, DFMs, private banks, platforms, IFAs, model portfolios", S[1]),
             ("Wealth (own)", "17% of AUM", "Cazenove Capital advisers to families, charities (own client model)", S[2]),
             ("Listed / direct", "small", "Active ETFs on exchanges; direct platforms", "#6B7A8F")]
    for i, (t, share, sub, col) in enumerate(chans):
        x = 4 + i * 170
        out.append(line(340, 46, x + 81, 76, "ch", MUTED, 1.1))
        out.append(box(x, 78, 162, 44, t, col, col, "#fff", 12, 700, sub=share, subsize=9.5, subcol="#fff"))
        out.append(box(x, 128, 162, 64, sub, "#fff", col, INK, 9.5))
        out.append(line(x + 81, 192, x + 81, 212, "ch", MUTED, 1.1))
    out.append(box(4, 214, 672, 30, "End savers and beneficiaries: pension members, policyholders, citizens, families", WASH, LINE, INK, 10.5, 600))
    save("channels", figure(svg(680, 250, "".join(out)),
        "The channels through which Client Group's work reaches clients. AUM shares FY25 from the annual report [S72]; ETF size [S230]. Wealth is shown for completeness: Cazenove runs its own adviser model [Inferred]."))


def day():
    slots = [("07:45", "Market read: 3 moves, 3 client implications; check team inbox", S[0]),
             ("08:30", "Team huddle: Salesforce pipeline, today's meetings, open RFPs", S[1]),
             ("09:00", "Build meeting pack: approved figures, labels, disclaimers, sign-off", S[0]),
             ("10:30", "RFP/DDQ: chase owners, quality-check numbers", S[3]),
             ("11:30", "Competitor snapshot for Value Proposition", S[1]),
             ("12:00", "Lunch; buddy or Coffee Hour", "#6B7A8F"),
             ("13:00", "Shadow a client call; log notes and actions in Salesforce", S[0]),
             ("14:00", "Event logistics: invites, RSVPs, hospitality within limits", S[2]),
             ("15:00", "Client requests: performance queries, documents, reporting tracker", S[0]),
             ("16:00", "Intern project (for the end-of-programme presentation)", S[3]),
             ("17:00", "Follow-ups, CRM updates, tomorrow's list", S[2])]
    out = []
    for i, (t, d, col) in enumerate(slots):
        y = 6 + i * 30
        out.append(text(52, y + 17, t, 11, NAVY, "end", 700)[0])
        out.append(f'<rect x="62" y="{y+3}" width="8" height="22" rx="2" fill="{col}"/>')
        out.append(text(80, y + 18, d, 10.5, INK)[0])
    save("day", figure(svg(680, 6 + len(slots) * 30 + 4, "".join(out)),
        "A worked day for a Sales intern in UK Client Group. Built from Schroders' Zurich and Madrid sales-intern task lists and London marketing and consultant-database postings [S7, S8, S5, S9] [Inferred]: no first-person London account was found."))


def orgchart():
    C, R, I, G = CONF, REP, INF, "#9AA3AF"
    out = [arrow_defs("oc")]
    def node(x, y, w, h, t, sub, col, dash=None):
        out.append(box(x, y, w, h, t, "#fff", col, INK, 9.5, 700, sub=sub, subsize=8, subcol=INK2, sw=2, dash=dash))
    node(230, 4, 220, 38, "Nuveen (TIAA), owner from 1 Oct 2026", "William Huffman, CEO", R)
    node(230, 58, 220, 38, "Richard Oldfield, Group CEO", "since 8 Nov 2024", C)
    out.append(line(340, 42, 340, 56, "oc", MUTED, 1))
    node(472, 58, 204, 38, "Karine Szenberg, Exec Vice Chair", "partnerships, Global Financial Clients", C)
    node(230, 112, 220, 38, "Matt Oomen, Global Head of Client Group", "since Aug 2025; on ExCo", C)
    out.append(line(340, 96, 340, 110, "oc", MUTED, 1))
    tops = [(4, "Strategy Execution & Delivery", "Ed Mitchell (Sep 2025); JD 'Delivery'?", C),
            (140, "Product (Value Proposition?)", "Strategy and Development teams; head not found", I),
            (276, "Central Global Marketing", "3 pillars + regional hubs; head not found", C),
            (412, "Client Service Hubs", "exist; head not found", I),
            (548, "Regional Client Groups", "= Sales Activation? UK, Europe, Asia, Americas", I)]
    for x, t, s_, col in tops:
        out.append(line(340, 150, x + 64, 170, "oc", MUTED, 1))
        node(x, 172, 128, 60, t, s_, col, "4 3" if col == I else None)
    node(4, 250, 128, 50, "Salesforce / CRM platform team", "live hiring: reqs 1993, 1995, 2067", C)
    out.append(line(68, 232, 68, 248, "oc", MUTED, 1))
    for j, t in enumerate(["Proposition & Campaigns", "Strategic Brand & Digital", "Mktg & BD Services: RFPs, DDQs, Consultant DB"]):
        node(276, 250 + j * 44, 128, 38, t, "", C)
    out.append(line(340, 232, 340, 248, "oc", MUTED, 1))
    regions = [("UK: Phil Middleton, Head of UK", C), ("Europe: Patrick Schwyzer (Apr 2026)", C), ("Asia: Gopi Mirchandani", C), ("Americas: head not found", G)]
    for j, (t, col) in enumerate(regions):
        node(548, 250 + j * 44, 128, 38, t, "", col, "4 3" if col == G else None)
    out.append(line(612, 232, 612, 248, "oc", MUTED, 1))
    uk = [("UK Institutional: Rachel Harris (Mar 2026)", "600+ UK pension schemes and insurers", C),
          ("UK Wealth (intermediary): Jamie Fowler", "Advisory | DFMs and wealth | Inv. trusts | BD desk", C),
          ("Consultant relations / FIs", "heads not found", G),
          ("SALES INTERN 2027 (London)", "Dept 'Sales (within Client Group)'", ACC)]
    out.append(path("M548,269 L530,269 L530,420", "oc", MUTED, 1, arrow=False))
    out.append(f'<line x1="80" y1="420" x2="636" y2="420" stroke="{MUTED}" stroke-width="1"/>')
    for j, (t, s_, col) in enumerate(uk):
        x = 4 + j * 170
        out.append(line(x + 80, 420, x + 80, 432, "oc", MUTED, 1))
        node(x, 434, 160, 52, t, s_, col, "4 3" if col == G else None)
    node(140, 250, 128, 60, "Schroders Capital BD (40 people)", "specialist private-markets sales; reporting line uncertain", R, "4 3")
    ly = 504
    for i, (lab, col) in enumerate([("Confirmed in primary source", C), ("Reported (press/snippet)", R), ("Inferred mapping", I), ("Not found", G), ("Your seat", ACC)]):
        x = 6 + i * 134
        out.append(f'<rect x="{x}" y="{ly}" width="14" height="14" fill="#fff" stroke="{col}" stroke-width="2"/>')
        out.append(text(x + 20, ly + 11, lab, 9, INK2)[0])
    save("orgchart", figure(svg(680, 526, "".join(out)),
        "Reconstructed Client Group org chart, colour-coded by confidence. Built from the ExCo page, appointment releases and live job postings [S17, S18, S20, S21, S22, S23, S24, S25, S5, S9, S10, S12, S71]. No official org chart is published; mapping of teams to the JD's three pillars is inferred."))


def hub():
    out = [arrow_defs("hb")]
    import math
    spokes = ["Pension client", "Consultant", "Fund selector", "Equities PMs", "Credit PMs", "Schroders Capital", "Compliance", "Marketing", "Operations", "Wealth (Cazenove)"]
    # left tangle
    out.append(text(160, 16, "Without a hub", 11, HARD, "middle", 700)[0])
    pts = []
    for i, s in enumerate(spokes):
        a = 2 * math.pi * i / len(spokes)
        pts.append((160 + 118 * math.cos(a), 160 + 118 * math.sin(a)))
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            if (i + j) % 3 != 0:
                out.append(f'<line x1="{pts[i][0]:.0f}" y1="{pts[i][1]:.0f}" x2="{pts[j][0]:.0f}" y2="{pts[j][1]:.0f}" stroke="{HARD}" stroke-opacity="0.35" stroke-width="0.8"/>')
    for (x, y), s in zip(pts, spokes):
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="{INK2}"/>')
    out.append(text(160, 300, "10 parties: up to 45 pairwise links", 10, HARD, "middle", 600)[0])
    # right wheel
    out.append(text(510, 16, "With Client Group as hub", 11, EASY, "middle", 700)[0])
    out.append(f'<circle cx="510" cy="160" r="40" fill="{S[1]}"/>')
    out.append(text(510, 156, "Client", 11, "#fff", "middle", 700)[0])
    out.append(text(510, 170, "Group", 11, "#fff", "middle", 700)[0])
    for i, s in enumerate(spokes):
        a = 2 * math.pi * i / len(spokes)
        x, y = 510 + 110 * math.cos(a), 160 + 110 * math.sin(a)
        out.append(f'<line x1="{510 + 42*math.cos(a):.0f}" y1="{160 + 42*math.sin(a):.0f}" x2="{x - 8*math.cos(a):.0f}" y2="{y - 8*math.sin(a):.0f}" stroke="{EASY}" stroke-width="1.2"/>')
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="{INK2}"/>')
        anchor = "start" if math.cos(a) > 0.2 else ("end" if math.cos(a) < -0.2 else "middle")
        dx = 9 if anchor == "start" else (-9 if anchor == "end" else 0)
        dy = 4 if anchor != "middle" else (16 if math.sin(a) > 0 else -9)
        out.append(text(f"{x+dx:.0f}", f"{y+dy:.0f}", s, 8.8, INK, anchor)[0])
    out.append(text(510, 300, "10 links, one owner of the client relationship", 10, EASY, "middle", 600)[0])
    out.append(text(340, 324, "n parties need n(n-1)/2 direct links; a hub needs n. Madrid's intern posting routes local requests \"to the London HQ\" [S8].", 9.5, INK2, "middle")[0])
    save("hub", figure(svg(680, 332, "".join(out)),
        "Why a central function exists: the tangle without it and the wheel with it. The arithmetic is standard; the application to Client Group is the author's [Inferred], supported by Schroders' \"fewer core propositions\" model [S72]."))


def request():
    out = [arrow_defs("rq")]
    steps = [("1. Request arrives", "RM: \"client wants Q3 performance and a view on gilts by 3pm\""),
             ("2. Clarify", "which fund, share class, period, audience (professional or retail)?"),
             ("3. Source", "approved performance from the data team; house view from published insights"),
             ("4. Check", "labels, disclaimers, is anything new? If yes, compliance approval"),
             ("5. Send", "via the RM, on time; state any gap honestly"),
             ("6. Record", "log in Salesforce; note follow-up; close the loop with the RM")]
    for i, (t, d) in enumerate(steps):
        y = 6 + i * 50
        col = [S[0], S[1], S[2], HARD, S[0], S[3]][i]
        out.append(f'<rect x="10" y="{y}" width="190" height="40" rx="4" fill="{col}"/>')
        out.append(text(22, y + 25, t, 12, "#fff", weight=700)[0])
        out.append(text(214, y + 25, d, 10.5, INK)[0])
        if i < 5:
            out.append(line(105, y + 40, 105, y + 48, "rq"))
    out.append(box(10, 306, 660, 34, "Stop point at step 4: new or changed client material is not sent until approved [S401]", "#F9E7E7", HARD, INK, 10.5, 700))
    save("request", figure(svg(680, 346, "".join(out)),
        "The life of a request through Client Group, from an RM's ask to a logged outcome. Built from the Zurich and Madrid postings [S7, S8] and COBS 4 [S401]; step names are the author's [Inferred]."))


def collision():
    out = [arrow_defs("co")]
    out.append(box(8, 10, 200, 50, "Senior RM A", S[0], S[0], "#fff", 11, 700, sub="large DB scheme, final-round pitch", subsize=9, subcol="#fff"))
    out.append(box(8, 110, 200, 50, "Senior RM B", S[3], S[3], "#fff", 11, 700, sub="wealth manager, new relationship", subsize=9, subcol="#fff"))
    out.append(box(250, 60, 180, 50, "Scarce resource", ACC, ACC, "#fff", 12, 700, sub="the fund manager's one free hour on Thursday", subsize=9, subcol="#fff"))
    out.append(line(210, 35, 248, 75, "co", HARD))
    out.append(line(210, 135, 248, 98, "co", HARD))
    crit = ["Is there a written rule or rota?", "Deadline: whose is fixed?", "Stakes: size, stage, revenue at risk", "Can it be split or substituted?", "Who owns the diary? They decide."]
    for i, c in enumerate(crit):
        out.append(box(470, 6 + i * 34, 202, 28, f"{i+1}. {c}", "#fff", NAVY, INK, 9.5, 600, align="start"))
    out.append(line(432, 85, 466, 85, "co"))
    out.append(box(8, 190, 664, 40, "You are the process, not the judge: lay out both cases in writing, send to the owner, tell both RMs when they'll hear.", EASY, EASY, "#fff", 11, 700))
    save("collision", figure(svg(680, 238, "".join(out)),
        "The scarce-resource collision and how it is allocated. The scenario and allocation test are the author's construction [Inferred], matching the JD's \"diary management\" and \"manages expectations\" lines [S263]."))


def walls():
    out = []
    out.append(f'<rect x="232" y="132" width="216" height="92" rx="6" fill="{S[1]}"/>')
    out.append(text(340, 172, "CLIENT GROUP", 14, "#fff", "middle", 700)[0])
    out.append(text(340, 192, "Sales, Client Service, Product, Marketing", 9.5, "#fff", "middle")[0])
    out.append(f'<rect x="226" y="126" width="228" height="104" rx="8" fill="none" stroke="{HARD}" stroke-width="2.5" stroke-dasharray="7 4"/>')
    walls = [("Investment teams", "Crosses: approved views, performance, product input", "Never: trade intentions ahead of execution", 232, 6),
             ("Compliance", "Crosses: every new client-facing material; gifts and hospitality", "Never: skipped for speed", 466, 130),
             ("Clients (external)", "Crosses: approved, fair, clear, not misleading material", "Never: another client's data; inside information", 232, 254),
             ("Wealth (Cazenove)", "Crosses: product shelf, research", "Never: private clients' personal data without a basis", 4, 130)]
    for t, cr, nv, x, y in walls:
        out.append(f'<rect x="{x}" y="{y}" width="210" height="100" rx="4" fill="#fff" stroke="{NAVY}" stroke-width="1.5"/>')
        out.append(text(x + 8, y + 17, t, 10.5, NAVY, weight=700)[0])
        s1, n1 = text(x + 8, y + 34, cr, 8.8, EASY, width=42)
        out.append(s1)
        out.append(text(x + 8, y + 34 + n1 * 11 + 6, nv, 8.8, HARD, width=42)[0])
    save("walls", figure(svg(680, 360, "".join(out)),
        "The walls around Client Group and what crosses each (green) or never crosses (red). Rules from COBS 4, COBS 2.3A, UK MAR and UK GDPR [S401, S40, S402, S403]; layout is the author's [Inferred]."))


def hiring():
    groups = [("Sales and client coverage", [("London", "Sales Intern 2027 (req 1943)"), ("Zurich", "Sales Activation intern (2049)"), ("Madrid", "Sales Support intern (2046)"),
                                            ("Hong Kong", "Client Director, Wealth"), ("Taipei", "Client Manager"), ("Cape Town", "Senior BD Manager")], S[0]),
              ("Product and marketing", [("London", "Product Intern 2027 (1952)"), ("London", "Marketing Intern 2027"), ("Singapore", "Head of Intermediary Marketing"),
                                         ("Gtr Manchester", "Events Manager"), ("London", "Consultant Database Specialist (1796)")], S[1]),
              ("Delivery: data and CRM", [("n/c", "Principal BA, CRM Platforms (2067)"), ("n/c", "Salesforce Platform Architect (1993)"), ("n/c", "Principal Salesforce Engineer (1995)")], S[2]),
              ("Control of distribution", [("Luxembourg", "Due diligence, Distribution Control (1978)"), ("London", "Business Risk Manager, Suitability")], HARD),
              ("Client service", [("New York", "Client Service Intern 2027")], S[3])]
    out = []
    y = 6
    for g, items, col in groups:
        out.append(f'<rect x="4" y="{y}" width="6" height="{len(items)*20+22}" fill="{col}"/>')
        out.append(text(16, y + 14, f"{g} ({len(items)})", 11, NAVY, weight=700)[0])
        for j, (city, role) in enumerate(items):
            out.append(text(28, y + 34 + j * 20, city, 9.5, col, weight=700)[0])
            out.append(text(130, y + 34 + j * 20, role, 9.5, INK)[0])
        y += len(items) * 20 + 30
    out.append(text(8, y + 6, "Named postings read on 29 Sep 2026 (a sample). Oracle search counts that day: 42 results for \"client group\", 17 \"sales\", 63 \"client service\" (overlapping). n/c = city not captured.", 8.8, MUTED)[0])
    save("hiring", figure(svg(680, y + 14, "".join(out)),
        "What Schroders is hiring for around Client Group, by department and city. Source: Schroders' Oracle recruiting site and Voyse early-careers board, 29 Sep 2026 [S1, S2, S4, S5, S7, S8, S9, S10, S11, S12] [Confirmed]."))


def wiring():
    out = [arrow_defs("wr")]
    out.append(box(240, 110, 200, 60, "Front-line capability", NAVY, NAVY, "#fff", 12, 700, sub="e.g. Global Credit team", subsize=9.5, subcol="#DDE4EF"))
    kinds = [("EMBEDDED", "Investment specialists who travel with sales; product manager assigned to the strategy", 20, 20, S[0]),
             ("CONNECTIVE", "Relationship managers, Sales Support Specialists, Consultant DB team linking clients to the capability", 460, 20, S[1]),
             ("UTILITY", "Salesforce platform, marketing hubs, BD Services (RFP/DDQ), client service hubs, UST operations", 20, 200, S[2]),
             ("CONTROL", "Compliance approvals, Distribution Control (KYD/AML), suitability oversight", 460, 200, HARD)]
    for t, d, x, y, col in kinds:
        out.append(box(x, y, 200, 78, t, "#fff", col, col, 11, 700, sub=d, subsize=9, subcol=INK, sw=2))
        out.append(line(x + (200 if x < 300 else 0), y + 39, 240 if x < 300 else 440, 140, "wr", col, 1.3))
    out.append(text(340, 300, "\"support Relationship Managers and their Sales Support Specialist as well as internal stakeholders across investment, client service, product and marketing\" [S7]", 9.2, INK2, "middle", italic=True, width=120)[0])
    save("wiring", figure(svg(680, 326, "".join(out)),
        "How a front-line unit is wired into the centre: embedded, connective, utility and control roles. Role types from Schroders postings [S4, S7, S9, S10, S11]; the four-way classification is the author's [Inferred]."))


def funnel():
    out = []
    st = [("Application form", "closed 16 Sep 2026 (req 1943 still showed live on 29 Sep)", 640), ("Stage 1: Cognitive", "numerical, critical, diagrammatic; ~20 min, untimed", 580),
          ("Stage 2: Behavioural & Motivational", "questionnaire; ~20 min, untimed", 520), ("Stage 3: Work Simulation + Video", "rank responses + short timed video; ~30 min; no retakes", 460),
          ("Assessment centre", "group exercise, presentation, competency interview; 4 to 5 hours", 400), ("Offer", "internship 14 Jun to 20 Aug 2027", 340)]
    for i, (t, s, w) in enumerate(st):
        x = (680 - w) / 2
        y = 6 + i * 50
        col = NAVY if i != 3 else ACC
        out.append(box(x, y, w, 42, t, col, col, "#fff", 11.5, 700, sub=s, subsize=9, subcol="#fff" if i != 3 else "#fff"))
    out.append(box(560, 156, 116, 36, "LIKELY YOU ARE HERE", ACC_L, ACC, INK, 9, 700))
    out.append(text(340, 318, "Feedback report within about 24 hours of each online stage. No single pass mark; humans make all decisions [S260, S262].", 9.5, INK2, "middle")[0])
    save("funnel", figure(svg(680, 326, "".join(out)),
        "The Schroders 2027 recruitment funnel and the candidate's likely position. Stages from the advert and Schroders' Cappfinity Candidate Zone [S263, S262, S260] [Confirmed]; \"you are here\" is inferred from the date."))


def stage3():
    out = [arrow_defs("s3")]
    parts = [("Practice question", "not assessed; test camera and timing", "#6B7A8F"),
             ("Workplace scenarios", "read an email, a chart, a request; rank 4 or so responses", S[0]),
             ("Staff video clips", "day-in-the-life context (typical of Cappfinity)", S[1]),
             ("Video question(s)", "short prep, timed answer, no pause, no retake", ACC),
             ("Submit", "feedback report ~24h", EASY)]
    for i, (t, s, col) in enumerate(parts):
        x = 4 + i * 136
        out.append(box(x, 10, 126, 76, t, col, col, "#fff", 11, 700, sub=s, subsize=9, subcol="#fff"))
        if i < 4:
            out.append(line(x + 127, 48, x + 134, 48, "s3"))
    out.append(text(340, 110, "Known: ~30 min; timed video; auto-advance; 25% max extra time; own words only (AI use prohibited) [S262].", 10, INK, "middle", 600)[0])
    out.append(text(340, 128, "Not published: number of video questions, prep seconds, answer length. Plan for 30 to 60 s prep, 1 to 3 min answers [Inferred] [S289, S290].", 10, INK2, "middle")[0])
    save("stage3", figure(svg(680, 138, "".join(out)),
        "Anatomy of Stage 3, the Cappfinity Work Simulation and Video Interview. Order of parts is indicative; Schroders publishes the elements, not the running order [S262, S276, S277]."))


def answer_shape():
    out = [arrow_defs("as")]
    beats = [("ENERGY", "0 to 20 s", "What you enjoy and why. \"The part I genuinely enjoy is...\"", S[1]),
             ("EVIDENCE", "20 to 80 s", "One real example, STAR-light: situation in one line, what you did, result with a number.", S[0]),
             ("LEARNING", "80 to 100 s", "What changed in how you think or work.", S[2]),
             ("LINK", "100 to 120 s", "Why it matters in Client Group Sales at Schroders.", OPI)]
    for i, (t, tm, d, col) in enumerate(beats):
        x = 4 + i * 170
        out.append(f'<rect x="{x}" y="8" width="160" height="120" rx="5" fill="#fff" stroke="{col}" stroke-width="2"/>')
        out.append(f'<rect x="{x}" y="8" width="160" height="28" rx="5" fill="{col}"/>')
        out.append(text(x + 10, 27, t, 12, "#fff", weight=700)[0])
        out.append(text(x + 150, 27, tm, 9, "#fff", "end")[0])
        out.append(text(x + 10, 54, d, 10, INK, width=28)[0])
        if i < 3:
            out.append(line(x + 161, 68, x + 168, 68, "as"))
    save("answer_shape", figure(svg(680, 136, "".join(out)),
        "The shape of a strengths-based video answer: energy first, then evidence, learning and link. Built from Cappfinity's strengths method (energy, performance, use) and Schroders' own guidance to explain \"what you enjoy\" [S262, S283, S285] [Inferred]."))


def why_page():
    out = [arrow_defs("wy")]
    out.append(box(210, 6, 260, 44, "Why Schroders, Client Group, now", NAVY, NAVY, "#fff", 13, 700))
    cols = [("STRUCTURE", S[1], ["One central Client Group owns sales, service, product, marketing [S306]", "Refocused in 2025 on \"fewer core propositions\" [S72]", "Three pillars: Value Proposition, Sales Activation, Delivery [S263]"]),
            ("ECONOMICS", S[0], ["Margins from 6bp (core solutions) to 57bp (private markets) [S71]", "So the mix Client Group sells drives revenue, not just AUM", "Intermediary gross inflows up 40%+ in H1 2026 [S70]"]),
            ("MOMENT", OPI, ["Nuveen completes 1 Oct 2026: ~$2.5trn, London the non-US HQ [S75, S76]", "Brand kept; standalone at least 12 months [S76]", "Client Group gets a bigger public-to-private shelf to sell [Inferred]"])]
    for i, (t, col, items) in enumerate(cols):
        x = 4 + i * 226
        out.append(line(340, 50, x + 109, 70, "wy", MUTED, 1))
        out.append(f'<rect x="{x}" y="72" width="218" height="200" rx="4" fill="#fff" stroke="{col}" stroke-width="2"/>')
        out.append(f'<rect x="{x}" y="72" width="218" height="28" rx="4" fill="{col}"/>')
        out.append(text(x + 109, 91, t, 12, "#fff", "middle", 700)[0])
        for j, it in enumerate(items):
            out.append(text(x + 10, 120 + j * 52, it, 9.8, INK, width=40)[0])
    out.append(box(4, 282, 672, 44, "Close: \"The thing I most want to work on is how a proposition like the Mercer LTAF goes from an idea with the investment team to a mandate, and what Sales Activation learns from the client that shapes the next one.\"", ACC_L, ACC, INK, 10, 600))
    save("why", figure(svg(680, 332, "".join(out)),
        "\"Why Schroders\" on one page: structure, economics, moment, and a specific close. Each fact sourced in the box; the argument is the author's [Inferred]."))


def master():
    out = [arrow_defs("ms")]
    # three columns: Industry | Firm | Role, linked
    out.append(text(102, 16, "THE INDUSTRY", 11, S[2], "middle", 700)[0])
    out.append(text(340, 16, "THE FIRM", 11, NAVY, "middle", 700)[0])
    out.append(text(578, 16, "THE ROLE", 11, S[1], "middle", 700)[0])
    ind = ["Passive and fee pressure (UK margin 18%)", "Fewer, bigger buyers (megafunds, 6 LGPS pools)", "Private markets for DC and wealth", "Retail push: ISA reform, targeted support", "Active ETFs; AI cost reset", "Rules: Consumer Duty, COBS 4, SDR, CCI"]
    firm = ["Active-only, 9 leading capabilities", "Schroders Capital: 57bp private markets", "Cazenove Capital: wealth, 48bp", "Cost:income 75% to 68%", "Central Client Group, fewer propositions", "Nuveen owner from 1 Oct 2026"]
    role = ["Value Proposition: what to sell", "Sales Activation: who, where, how", "Delivery: data, CRM, efficiency", "Scenario: approvals before speed", "Skill: explain macro to a client", "Output: NNB, revenue, retention"]
    for i in range(6):
        y = 30 + i * 50
        out.append(box(4, y, 196, 40, ind[i], "#E8F4EE", S[2], INK, 9.8))
        out.append(box(242, y, 196, 40, firm[i], "#EEF3FA", NAVY, INK, 9.8))
        out.append(box(480, y, 196, 40, role[i], "#FBF1E6", S[1], INK, 9.8))
    links = [(0, 0), (1, 5), (2, 1), (3, 2), (4, 4), (5, 3)]
    for a, b in links:
        out.append(line(201, 50 + a * 50, 240, 50 + b * 50, "ms", MUTED, 0.9))
    links2 = [(0, 4), (1, 0), (2, 0), (4, 2), (5, 1), (3, 5)]
    for a, b in links2:
        out.append(line(439, 50 + a * 50, 478, 50 + b * 50, "ms", MUTED, 0.9))
    out.append(box(4, 336, 672, 40, "One sentence: an active manager under fee pressure, now inside a $2.5trn group, has centralised selling so that a small number of propositions reach the right clients fast and within the rules. The intern's seat is where that happens.", NAVY, NAVY, "#fff", 10, 600))
    save("master", figure(svg(680, 382, "".join(out)),
        "The master diagram: industry forces, the firm's response and the role, connected. Every box is sourced elsewhere in the pack (Parts 2, 5, 6); the links are the author's synthesis [Inferred]."))


def rfp():
    out = [arrow_defs("rf")]
    st = [("Objective", "trustees set goal"), ("Consultant screen", "rated managers only"), ("RFP + DDQ", "team, process, risk, fees, ESG"), ("Shortlist", "3 to 6"),
          ("Finals", "presentation"), ("Fees + IMA", "negotiate, sign"), ("Onboard + keep", "report, meet, retain")]
    for i, (t, s) in enumerate(st):
        x = 4 + i * 96
        col = S[0] if i not in (2, 6) else ACC
        out.append(box(x, 10, 88, 62, t, col, col, "#fff", 10.5, 700, sub=s, subsize=8.5, subcol="#fff"))
        if i < 6:
            out.append(line(x + 89, 41, x + 95, 41, "rf"))
    out.append(text(340, 94, "Typical cycle 6 to 18 months [S150]. Orange = where interns most often help (DDQ coordination, reporting) [S7, S9].", 9.5, INK2, "middle")[0])
    save("rfp", figure(svg(680, 102, "".join(out)),
        "How an institutional mandate is typically won. General industry practice [Inferred]; consultant gatekeeping and the CMA Order in Part 6.2 [S179, S198]."))


if __name__ == "__main__":
    for f in (valuechain, channels, day, orgchart, hub, request, collision, walls, hiring, wiring, funnel, stage3, answer_shape, why_page, master, rfp):
        f()
    print("role figs done")
