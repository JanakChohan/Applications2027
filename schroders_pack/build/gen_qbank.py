#!/usr/bin/env python3
"""Question bank (Part 9), Cappfinity video prompts and work simulation scenarios (Part 9B)."""
import html, os

ROOT = os.path.dirname(os.path.abspath(__file__))
e = lambda s: html.escape(s, quote=False)

# (question, testing, structure, facts, trap)
QB = {
"A. Motivation: why this, why here, why now": [
 ("Why asset management?", "Genuine interest versus a generic finance choice.", "One moment you got interested; what the industry does for real people; why the client side.", "UK industry manages £10trn, half for overseas clients [S150]; retail now the largest client group [S150].", "\"I like markets\" with no link to clients."),
 ("Why Schroders?", "Mechanism, not adjectives; up to date on the deal.", "Structure (central Client Group), economics (margin mix), moment (Nuveen). See Part 12.", "Client Group model [S72]; margins 6 to 57bp [S71]; Nuveen effective 1 Oct 2026 [S75].", "\"Prestigious family firm since 1804.\" Out of date this week."),
 ("Why Client Group rather than an investment team?", "Whether you understand the client side is a career, not a consolation.", "What energises you (explaining, relationships); what the three pillars do; one example of you doing it.", "Three pillars [S263]; Oomen's remit [S306].", "Implying sales is a back-up for failing to get into investment."),
 ("Why sales specifically, rather than product or marketing?", "Self-knowledge.", "Name the activity you enjoy most (conversations, winning trust); acknowledge the others; show you know they are colleagues.", "Product, Marketing and Sales under one head [S306].", "Dismissing the other teams."),
 ("What do you think a Sales intern here does day to day?", "Realism.", "Meeting packs, RFP and DDQ support, CRM, events, client requests, a project.", "Zurich Sales Activation posting [S7].", "\"Pitching to clients.\""),
 ("Where do you see yourself in five years?", "Ambition that fits the programme.", "Graduate programme, CFA Level 1, a client-facing seat, a specialism.", "Graduate programme and CFA support [S15].", "A plan that leaves Schroders in year two."),
 ("Why now: what has changed at Schroders that makes this a good time?", "Current awareness.", "Client Group rebuilt 2025; Nuveen shelf; retail rule changes in 2027.", "[S72, S75, S168, S187].", "Speculating about job cuts."),
],
"B. The firm": [
 ("What do you know about Schroders' recent results?", "Whether you read primary sources.", "One headline, one strength, one weakness, one so-what.", "H1 2026: AUM £867.8bn, profit +46%, net outflows £8.3bn incl. one £6.6bn mandate [S70].", "Quoting outflows without the context."),
 ("What does the Nuveen deal mean for clients?", "Calm, accurate messaging.", "What stays (brand, London, CEO, standalone year); what grows (shelf); what to watch.", "[S76, S309].", "Promising nothing will change, or guessing at integration."),
 ("How does Schroders make money?", "Commercial basics.", "Fee rate times assets, by business; costs; profit.", "NOR £2,504.3m; margins by business [S71].", "Saying \"commission\" or \"trading profits\"."),
 ("What are Schroders' three businesses?", "Map of the firm.", "Public Markets, Schroders Capital, Wealth Management; Client Group sells across them.", "[S71].", "Forgetting wealth."),
 ("Who is Schroders' biggest competitor?", "Judgement about competition.", "Depends on channel: BlackRock/L&G in passive and DC; M&G, aberdeen, Jupiter in UK wholesale; private markets firms in alternatives.", "Part 4 table [S130 to S140].", "One name with no reasoning."),
 ("What is one weakness at Schroders?", "Honesty without disloyalty.", "Flows; context; what Client Group can do.", "[S70, S71].", "Badmouthing or refusing to answer."),
 ("What are Schroders' values?", "Whether you read the annual report.", "Excellence, innovation, teamwork, passion, integrity; one example of each you can show.", "[S72].", "Leaving out teamwork."),
],
"C. Markets and the industry": [
 ("Tell us about a market story you are following.", "Genuine interest and the event-to-client chain.", "Event, number, mechanism, client, what you would watch.", "BoE 3.75%, 3 votes to raise [S232]; Schroders house view [S242].", "A headline you can't explain two levels down."),
 ("What happens to bond prices when rates rise, and why?", "Basic finance.", "Fixed coupon; new bonds pay more; old bond price falls until yields match.", "30-year gilts highest since 1998 [S237] [Reported].", "Getting the direction wrong under pressure."),
 ("Active or passive: which would you choose for your own pension?", "A reasoned view.", "Depends on asset class; low-cost core plus active where it adds value.", "[S152, S319].", "Dogma either way."),
 ("What is the biggest risk to markets right now?", "Macro awareness.", "Name one risk, its channel, what would show it's happening.", "Long-term yields spike [S242]; concentration [S241].", "Listing five risks with no depth."),
 ("How would you explain inflation to a new client?", "Communication.", "Plain words; one picture; what it does to their savings.", "CPI 3.1% Aug 2026 [S232].", "Jargon."),
 ("What is a private market asset and why would a pension want one?", "Industry vocabulary.", "Unlisted companies, loans, property; illiquidity premium; long horizon.", "Mansion House 10% aim [S181].", "Ignoring liquidity risk [S196]."),
 ("What is an ETF, and what is an active ETF?", "Product literacy.", "Exchange-traded fund; active version has a manager; cheaper wrapper.", "Schroders active ETFs $4.3bn [S230].", "Saying ETFs are always passive."),
 ("What will the industry look like in five years?", "Structured thinking.", "Pick one of four views; evidence; counter-view.", "Part 5.7 [S154, S181, S196].", "Vague \"technology will change everything\"."),
],
"D. The role and commercial sense": [
 ("A client says our fees are too high. What do you say?", "Value, not defensiveness.", "Acknowledge; ask what they compare with; explain value; offer the published assessment of value; escalate pricing to the RM.", "Assessment of Value rules [S163, S164].", "Offering a discount you can't authorise."),
 ("Why does a £6.6bn redemption hurt less than it sounds?", "Margin thinking.", "It was core solutions at about 6bp; revenue lost is about £4m a year.", "[S70, S71] [Inferred].", "Treating all assets as equal."),
 ("How would you prepare for a first meeting with a pension scheme?", "Preparation and client empathy.", "Public papers, size, liabilities, consultant, current managers, our relevant capabilities, one question to ask.", "600+ UK pension clients [S27].", "Leading with our products."),
 ("How would you measure whether a client event worked?", "Data-driven Delivery thinking.", "Attendance, follow-up meetings, pipeline, flows over a year; feedback.", "Salesforce campaign tracking [S7].", "Counting attendees only."),
 ("What makes a good salesperson in asset management?", "Values.", "Listening, knowing the product and its limits, honesty, follow-through, patience over years.", "Client duration 4.6 years [S72].", "\"Being persuasive\" alone."),
 ("How would you prioritise three urgent requests?", "Organisation.", "Deadline, consequence, owner; renegotiate out loud; confirm in writing.", "JD \"manages expectations\" [S263].", "Doing them in the order received."),
 ("What rules would you need to know in your first week?", "Compliance maturity.", "Fair, clear, not misleading; approvals; professional vs retail; hospitality limits; inside information; data.", "[S401, S39, S40, S402, S403].", "\"Compliance handles that.\""),
],
"E. Competency and strengths (answer with energy, then evidence)": [
 ("Tell us about a time you had to build a relationship with someone very different from you.", "Rapport and relationship building.", "Energy line; STAR; what you learned about them; link to clients.", "JD \"trust-based relationships\" [S263].", "A story where you did all the talking."),
 ("Tell us about a time you explained something complex to a non-expert.", "Explainer strength.", "The concept; how you tested understanding; the result.", "JD \"adapt style\" [S263].", "No check that they understood."),
 ("Describe a project or event you organised.", "Planning, coordination.", "Scale with numbers; your plan; a problem; how you fixed it.", "JD \"event or project coordination\" [S263].", "Group achievement with no \"I\"."),
 ("Tell us about a time you were under pressure.", "Composure and method.", "What was at stake; your method; the outcome; what you would repeat.", "JD \"composure\" [S263].", "A story where pressure was self-inflicted and unresolved."),
 ("Tell us about something you started from scratch.", "Self-starter.", "The gap you saw; what you did first; who you brought in; result.", "JD \"leading or launching projects\" [S263].", "Something you merely joined."),
 ("Tell us about a mistake you made.", "Honesty and learning.", "Real mistake; your part; fix; what changed after.", "Cappfinity values authentic reflection [S285].", "A fake weakness."),
 ("Tell us about a time you disagreed with a teammate.", "Collaboration.", "Their view fairly stated; how you resolved it; the relationship after.", "AC group criteria: listen, collaborate [S262].", "Winning the argument as the point."),
 ("What energises you, and what drains you?", "Strengths fit.", "Honest energiser linked to the role; a drainer you manage.", "Strengths Profile method [S283].", "Saying nothing drains you."),
 ("Tell us about a time you used a creative approach to overcome a challenge.", "Resourcefulness. Reported as asked at Schroders [S290].", "Constraint; your idea; result.", "[S290] [Reported].", "Creative but pointless."),
 ("Tell us about feedback that changed how you work.", "Coachability.", "Feedback; how you felt; what you changed; evidence it stuck.", "Buddy and training culture [S263].", "Feedback you disagreed with and ignored."),
],
"F. Curveballs": [
 ("Sell me this pen.", "Listening before pitching.", "Ask what they need it for; match one feature to that need; close.", "", "Listing features without questions."),
 ("What would you do if you finished your work early?", "Initiative inside priorities.", "Ask the team, read, offer help, tell your manager.", "", "\"Go home early.\""),
 ("What is something you believe that most people disagree with?", "Independent thinking with reasons.", "Claim, reason, number, counter.", "Part 8.", "Something controversial and off-topic."),
 ("If you were CEO of Schroders tomorrow, what would you do first?", "Strategic sense and humility.", "Clients through the integration; flows in equities; one idea.", "[S70, S76].", "A radical plan with no evidence."),
 ("What would you do if a client asked you for a stock tip?", "Rules and courtesy.", "Politely decline; explain you can share published views; refer to the RM.", "COBS 4; MAR [S401, S402].", "Giving one."),
],
}

ASK = [
 ("Since Client Group moved to \"fewer core propositions\", how do regional sales feed what they hear from clients back into Value Proposition?", "[S72]"),
 ("How has the Client Group operating model changed a UK salesperson's week since 2025?", "[S72, S306]"),
 ("Clients paused some long-dated commitments before completion. What are UK institutional clients asking about the Nuveen combination now?", "[S70]"),
 ("After the first standalone year, which Nuveen capabilities do you think UK and European clients will want first?", "[S76]"),
 ("With DC megafunds and six LGPS pools, does UK Institutional now sell whole-portfolio partnerships rather than single strategies?", "[S23, S183]"),
 ("Where do active ETFs sit in an intermediary sales conversation compared with the fund version of the same strategy?", "[S230]"),
 ("How does the Schroders Capital specialist sales team work alongside generalist relationship managers on a pension client?", "[S71]"),
 ("CCI product summaries become mandatory a week before the internship starts. How much of that lands on Client Group?", "[S168]"),
 ("What does sales effectiveness look like in Salesforce terms here?", "[S72, S7]"),
 ("What distinguishes interns who convert to the 2028 graduate programme?", "[S263, S260]"),
]

# Cappfinity video prompts: (prompt, type, what it tests, scaffold)
VIDEO = [
 ("Why are you interested in a career in asset management?", "Motivation", "Genuine, specific interest", "Moment it clicked; what asset managers do for savers; why the client side; one current fact."),
 ("Why Schroders, and why Client Group rather than an investment team?", "Motivation", "Research and fit", "Structure, economics, moment (Part 12); energy for client work."),
 ("What do you think a Sales intern in Client Group does day to day, and which part appeals most?", "Motivation", "Realistic job preview", "Three real tasks [S7]; the one you would enjoy and why; a time you did something similar."),
 ("Tell us about a recent market or economic event and how it might affect what our clients ask us.", "Commercial", "Event-to-client chain", "Event, number, mechanism, which client, what they would ask, what you would do."),
 ("What have you done to learn about this industry, and what surprised you?", "Motivation", "Curiosity, initiative", "Two concrete actions; one surprise with a number; how it changed your view."),
 ("Where do you see yourself in five years, and how would this internship help?", "Motivation", "Fit with the programme", "Graduate programme, qualification, client seat; what you would learn here first."),
 ("What does a great day look like for you?", "Strengths", "Energisers", "A real day; what made it great; the strength behind it; where Client Group offers that."),
 ("What energises you, and what drains you?", "Strengths", "Self-awareness, fit", "Honest energiser linked to the role; honest drainer and how you manage it."),
 ("Tell us about something you learned recently purely because you were curious.", "Strengths", "Curiosity", "What, why, how you went about it, what you did with it."),
 ("Do you prefer starting things or finishing them?", "Strengths", "Consistency and reasons", "Pick one honestly; why; how you cover the other side."),
 ("Do you prefer the big picture or the detail?", "Strengths", "Consistency and reasons", "Pick one; example; how you guard against the weakness."),
 ("What do you find easy that other people seem to find hard?", "Strengths", "Natural strengths", "One thing; evidence others noticed; how it would help in sales."),
 ("What tasks tend to stay at the bottom of your to-do list?", "Strengths", "Honesty about drains", "A real task; why; what system stops it slipping."),
 ("When have you felt most in your element?", "Strengths", "Energy", "Scene, what you were doing, why it felt natural."),
 ("How would friends or teammates describe you, and would you agree?", "Strengths", "Self-awareness", "Three words others use; one you agree with and one you'd nuance."),
 ("What achievement are you most proud of, and why that one?", "Strengths", "Values", "The achievement; why it mattered to you, not just the result."),
 ("Tell us about a time you built a relationship with someone very different from you.", "Relationships", "Rapport Builder", "Energy line; how you found common ground; what it led to."),
 ("Describe a time you explained something complex to someone with no background in it.", "Relationships", "Explainer", "Concept; your analogy; how you checked understanding."),
 ("Tell us about a time you changed someone's mind.", "Relationships", "Persuasion with integrity", "Their view; your evidence; listening; the outcome; respecting their choice."),
 ("Tell us about a time you dealt with an unhappy customer or member of the public.", "Relationships", "Composure, client focus", "Listen, acknowledge, act, follow up; what you learned."),
 ("How do you keep in touch with and maintain a network?", "Relationships", "Relationship Deepener", "Your actual habit; an example where it paid off for both sides."),
 ("Tell us about a time you had several competing deadlines.", "Organisation", "Planful, Time Optimiser", "The list; how you ranked; who you told; result."),
 ("Describe an event, project or society activity you coordinated. What would you do differently?", "Organisation", "Coordination", "Scale in numbers; plan; problem; fix; the change next time."),
 ("Tell us about a setback and what you did next.", "Resilience", "Bounceback", "What went wrong; first action; what you changed; later result."),
 ("When have you had to stay calm when things were going wrong?", "Resilience", "Centred", "What was at stake; your method; the outcome."),
 ("Tell us about a time you took the initiative without being asked.", "Drive", "Self-starter", "The gap; your first step; who you involved; result."),
 ("Tell us about feedback that changed how you work.", "Growth", "Coachability", "Feedback; reaction; change; evidence."),
 ("Describe a time you contributed to a team's success. What was your role?", "Teamwork", "Collaboration", "Team goal; your specific part; how you helped others."),
 ("Tell us about a time you used a creative approach to overcome a challenge.", "Resourcefulness", "Reported at Schroders [S290]", "Constraint; idea; test; result."),
 ("How has your thinking changed over the past year about something that matters to you?", "Growth", "Official phrasing hint [S262]", "Old view; what changed it; new view; what you do differently."),
]

# Work simulation scenarios: (title, setup, options (4), best order, why)
SIM = [
 ("Client complaint email",
  "An IFA emails you: the Q3 factsheet for a fund they use is late and their client review is tomorrow. They are annoyed.",
  ["A. Reply immediately with last quarter's factsheet so they have something.",
   "B. Acknowledge, apologise for the delay, check with the reporting team when the Q3 factsheet will be ready, and tell the IFA a time. Copy the relationship manager.",
   "C. Forward the email to the relationship manager and do nothing else.",
   "D. Reply saying factsheets are produced by another team and are not your responsibility."],
  "B, C, A, D",
  "B owns the client experience inside the rules. C is safe but slow. A sends out-of-date information that could mislead. D abandons the client."),
 ("Three requests by 2pm",
  "It is 11am. RM1 wants a pitch book updated by 2pm for a final-round presentation. RM2 wants CRM notes from yesterday's meeting logged today. Your manager wants an event guest list by 5pm.",
  ["A. Do them in the order they arrived.",
   "B. Start the pitch book, tell RM2 the notes will be done by 4pm, confirm the guest list for 5pm, and flag if the pitch book runs over.",
   "C. Ask your manager to choose the order for you before starting anything.",
   "D. Do the quick CRM notes first to clear your list, then the pitch book."],
  "B, D, C, A",
  "B ranks by deadline and stakes and manages expectations early. D is reasonable if the notes truly take minutes, but risks the fixed deadline. C is over-escalation for a clear call. A ignores stakes."),
 ("The wrong number in the pack",
  "Twenty minutes before a client meeting you spot that a performance figure in the pack you built is for the wrong share class.",
  ["A. Say nothing; the difference is small.",
   "B. Correct the slide yourself and reprint without telling anyone.",
   "C. Tell the RM immediately, give the correct approved figure and its source, and let them decide how to handle it in the meeting.",
   "D. Tell the RM after the meeting."],
  "C, B, D, A",
  "C is honest, fast and keeps the decision with the owner. B fixes the error but bypasses the record and approval. D lets the client see wrong data. A is misleading."),
 ("Speaker drops out",
  "The day before an adviser seminar with 40 guests, the fund manager speaker cancels.",
  ["A. Cancel the event and email guests.",
   "B. Tell your manager now with two options: a named replacement from the same team, or a recorded update plus live Q&amp;A. Draft the guest message for approval.",
   "C. Find a replacement yourself and tell your manager once it is sorted.",
   "D. Run the event with no change and hope guests don't mind."],
  "B, C, A, D",
  "B solves and escalates with options. C shows initiative but skips the owner. A is a last resort. D ignores the client experience."),
 ("A client wants a view",
  "On a volatile day, a family office client emails: \"Should we sell our equity funds now?\"",
  ["A. Reply with your own view on whether to sell.",
   "B. Acknowledge, share the firm's latest published market commentary, and arrange a call with the RM and investment specialist.",
   "C. Tell them you can't discuss markets.",
   "D. Forward to the RM with no reply to the client."],
  "B, D, C, A",
  "B is helpful within the rules: published views, the right people, no personal advice. D is safe but leaves the client waiting. C is unhelpful. A risks unsuitable advice."),
 ("Double-booked senior",
  "Two senior RMs both booked the same fund manager for the same Thursday hour.",
  ["A. Keep the first booking and tell the second RM.",
   "B. Lay out both requests with client, stage and deadline, and ask the person who owns the fund manager's diary to decide today. Offer alternative slots.",
   "C. Pick the one with the bigger client.",
   "D. Leave them to sort it out."],
  "B, A, C, D",
  "B makes the process fair and fast. A is a defensible rule but ignores stakes. C is you judging. D abdicates."),
 ("Teammate not contributing",
  "On an intern group project due Friday, one member has missed two check-ins.",
  ["A. Do their part yourself.",
   "B. Message them privately, ask if something is wrong, agree a smaller piece they can deliver, and tell the group the plan.",
   "C. Report them to the programme manager straight away.",
   "D. Mention it in the final presentation."],
  "B, A, C, D",
  "B is fair, direct and keeps the team on track. A delivers but hides the problem. C escalates too early. D is public blame."),
 ("CRM duplicates before a mail-out",
  "Before a campaign email, you notice duplicate and out-of-date contacts in the list.",
  ["A. Send anyway; duplicates are harmless.",
   "B. Flag it to the campaign owner, suggest a quick clean using agreed rules, and send once fixed.",
   "C. Delete records you think are wrong.",
   "D. Export the list to your laptop to fix it in Excel."],
  "B, C, A, D",
  "B protects data quality and the client experience. C is well meant but unilateral. A irritates clients. D takes personal data out of approved systems."),
 ("Compliance-sensitive request",
  "A client asks by email for this month's unpublished performance number and \"any hot ideas\".",
  ["A. Send what you have; it's only a few days early.",
   "B. Explain politely that you can share published figures now and the month-end figure once released, and offer a call with the RM on market views.",
   "C. Ignore the email.",
   "D. Ask a colleague in the investment team for their ideas and pass them on."],
  "B, C, D, A",
  "B is courteous and inside the rules. C is poor service but no breach. D and A share unapproved information."),
 ("A day-in-the-life video",
  "You watch a short clip of a Schroders salesperson describing a day, then rate how much you would enjoy each task.",
  ["Rate: client meetings; RFP writing; CRM updates; event logistics; market reading."],
  "No right order",
  "This tests consistency with Stage 2 and authenticity. Answer honestly. Say what energises you and show you know the dull parts exist."),
]


def qbank_html():
    out = ['<!--SPIN:qb--><div class="spinhead"></div>']
    n = 0
    for grp, qs in QB.items():
        out.append(f"<h3>{e(grp)}</h3>")
        for q, t, s, f, tr in qs:
            n += 1
            fx = f'<br><span class="ql">Weave in</span> {e(f)}' if f else ""
            out.append(f'<div class="q"><span class="qn">Q{n}</span><span class="qt">{e(q)}</span><br>'
                       f'<span class="ql">Tests</span> {e(t)} <span class="ql">&nbsp;Structure</span> {e(s)}{fx}'
                       f'<br><span class="ql" style="color:#B23A3A">Trap</span> {e(tr)}</div>')
    out.append("<!--/SPIN:qb-->")
    return "\n".join(out), n


def ask_html():
    rows = "".join(f"<li>{e(q)} <span class=\"small\">{s}</span></li>" for q, s in ASK)
    return f"<ol>{rows}</ol>"


def video_html():
    out = ['<!--SPIN:qb--><h3>Likely Cappfinity video prompts (none confirmed as Schroders questions)</h3>',
           '<table><thead><tr><th style="width:4%">#</th><th style="width:36%">Prompt</th><th style="width:13%">Type</th><th style="width:16%">Tests</th><th>Scaffold (energy, evidence, learning, link)</th></tr></thead><tbody>']
    for i, (p, t, te, sc) in enumerate(VIDEO, 1):
        out.append(f"<tr><td>{i}</td><td><b>{e(p)}</b></td><td>{e(t)}</td><td>{te}</td><td>{e(sc)}</td></tr>")
    out.append("</tbody></table><!--/SPIN:qb-->")
    return "\n".join(out)


def sim_html():
    out = ['<!--SPIN:qb--><h3>Likely work simulation scenarios, with a suggested ranking</h3>']
    for i, (t, setup, opts, best, why) in enumerate(SIM, 1):
        ol = "".join(f"<li style='list-style:none'>{o}</li>" for o in opts)
        out.append(f'<div class="card medium"><div class="ch"><span class="ct">S{i}. {e(t)}</span><span class="lvl">rank</span></div>'
                   f'<dl><dt>Setup</dt><dd>{e(setup)}</dd><dt>Options</dt><dd><ul style="padding-left:0;margin:0">{ol}</ul></dd>'
                   f'<dt>Best order</dt><dd><b>{best}</b></dd><dt>Why</dt><dd>{why}</dd></dl></div>')
    out.append("<!--/SPIN:qb-->")
    return "\n".join(out)


if __name__ == "__main__":
    qb, n = qbank_html()
    open(os.path.join(ROOT, "fragments", "qbank.html"), "w").write(qb)
    open(os.path.join(ROOT, "fragments", "ask.html"), "w").write(ask_html())
    open(os.path.join(ROOT, "fragments", "video.html"), "w").write(video_html())
    open(os.path.join(ROOT, "fragments", "sim.html"), "w").write(sim_html())
    print(n, "questions;", len(VIDEO), "video prompts;", len(SIM), "sims;", len(ASK), "asks")
