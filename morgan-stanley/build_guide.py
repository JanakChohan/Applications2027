"""Builds the Morgan Stanley Aon online assessment guide PDF."""
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (PageBreak, Paragraph, SimpleDocTemplate, Spacer,
                                Table, TableStyle, KeepTogether)

OUT = "morgan-stanley/MS_Aon_Assessment_Guide.pdf"
NAVY = colors.HexColor("#0B2545")
ACCENT = colors.HexColor("#1B6CA8")
LIGHT = colors.HexColor("#EAF2FA")
WARN = colors.HexColor("#FFF4E0")

ss = getSampleStyleSheet()
H0 = ParagraphStyle("H0", parent=ss["Title"], textColor=NAVY, fontSize=24, leading=29)
SUB = ParagraphStyle("SUB", parent=ss["Normal"], alignment=TA_CENTER, textColor=ACCENT, fontSize=12, leading=16)
H1 = ParagraphStyle("H1", parent=ss["Heading1"], textColor=NAVY, fontSize=16, leading=20, spaceBefore=6, spaceAfter=6)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], textColor=ACCENT, fontSize=12.5, leading=16, spaceBefore=8, spaceAfter=4)
B = ParagraphStyle("B", parent=ss["Normal"], fontSize=10, leading=14, spaceAfter=5)
BUL = ParagraphStyle("BUL", parent=B, leftIndent=12, bulletIndent=2, spaceAfter=3)
SMALL = ParagraphStyle("SMALL", parent=B, fontSize=8.5, leading=11, textColor=colors.HexColor("#555555"))
CELL = ParagraphStyle("CELL", parent=B, fontSize=9, leading=12, spaceAfter=0)
CELLB = ParagraphStyle("CELLB", parent=CELL, fontName="Helvetica-Bold", textColor=colors.white)

story = []
P = lambda t, s=B: story.append(Paragraph(t, s))


def bullets(items):
    for i in items:
        story.append(Paragraph(i, BUL, bulletText="•"))


def table(rows, widths, header=True):
    data = [[Paragraph(str(c), CELLB if (header and r == 0) else CELL) for c in row]
            for r, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    style = [("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#B8C7D9")),
             ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
             ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]
    if header:
        style.append(("BACKGROUND", (0, 0), (-1, 0), NAVY))
        for r in range(1, len(rows)):
            if r % 2 == 0:
                style.append(("BACKGROUND", (0, r), (-1, r), LIGHT))
    t.setStyle(TableStyle(style))
    story.append(t)
    story.append(Spacer(1, 6))


def callout(title, text, bg=LIGHT):
    t = Table([[Paragraph(f"<b>{title}</b><br/>{text}", CELL)]], colWidths=[170 * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg),
                           ("BOX", (0, 0), (-1, -1), 0.8, ACCENT),
                           ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                           ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    story.append(KeepTogether([t, Spacer(1, 8)]))


# ---------------- Cover ----------------
story += [Spacer(1, 30 * mm)]
P("Morgan Stanley Online Assessment", H0)
P("The complete breakdown: Aon tests, scoring, integrity checks and how to pass", SUB)
story.append(Spacer(1, 8 * mm))
P("Role: 2027 Investment Management Off-Cycle Internship, UK Institutional Sales (London)", SUB)
P("Prepared for Janak Chohan, September 2026", SUB)
story.append(Spacer(1, 14 * mm))
callout("The 30-second version",
        "You have <b>48 hours</b> to sit one integrated Aon \"simulation\" with three parts: "
        "<b>Numerical Reasoning</b>, <b>Inductive Reasoning</b> and a <b>Situational Judgement Test (SJT)</b>. "
        "The reasoning parts are very short and very fast (roughly 5 to 12 minutes each), so practice matters more "
        "than raw intelligence. You are compared against other applicants (a percentile), not graded out of 100. "
        "There is no published pass mark, but as a rule of thumb, aim to be clearly above average (top 30 to 40%) on every part "
        "and don't bomb any single one. Do it alone, honestly, in one sitting: they can re-test you in person later.")
callout("How to use this guide",
        "Section 1 covers what the tests actually are. Section 2 covers scoring and ranking. Section 3 covers integrity and "
        "\"cheating\" checks. Section 4 covers whether they see your CV. Sections 5 to 7 cover strategy, practice resources and a 48-hour plan. "
        "Where something is <i>not officially published</i> by Morgan Stanley or Aon, it's labelled as an estimate.", WARN)
story.append(PageBreak())

# ---------------- 1. What the tests are ----------------
P("1. What you will actually sit", H1)
P("Morgan Stanley has used Aon (formerly <b>cut-e</b>) for campus assessments in EMEA since around 2019. Your email confirms "
  "the provider (the support address is @aon.com) and the three components. They're <b>integrated into one simulation</b>, "
  "so you'll see a single task in your Application Center. Inside it you'll move between the sections, each with an untimed "
  "practice section followed by a timed, scored section.")

table([
    ["Component", "Aon test (likely)", "What it looks like", "Typical timing*"],
    ["Numerical Reasoning", "scales numerical", "Tables, charts and short documents with financial or business data. Multiple choice. "
     "Questions often ask for a percentage change, ratio, difference or currency conversion. Screen switches between data tabs.",
     "Very short. Morgan Stanley versions are reported as around 6 to 12 min, with many questions (e.g. ~18 across 6 data sets). About 20 to 40 sec per question."],
    ["Inductive Reasoning", "scales ix (\"Discover Rules\")", "Abstract shapes. Common version: 9 figures, 8 follow a hidden rule, and you click the one that breaks it. "
     "Rules involve shape, count, shading, rotation, position or nesting. An alternative ix version asks you to sort figures into sets.",
     "About 5 min for 20 items (~15 sec each), or 12 min for 12 items in the set-sorting version."],
    ["Situational Judgement", "Aon SJT / messaging simulation", "Realistic workplace scenarios, often as emails or messages from colleagues, clients or managers. "
     "You rate or rank possible responses (most/least effective, or a scale).",
     "Usually untimed or generous. Reported as around 15 to 25 min."],
], [30 * mm, 28 * mm, 70 * mm, 42 * mm])
P("*Timings come from candidate reports and prep providers, not Morgan Stanley. The on-screen instructions are what count, so read them carefully. "
  "The whole thing typically takes <b>30 to 60 minutes</b>, which matches the email's 30 to 90 minute estimate.", SMALL)

P("1.1 Numerical: the details", H2)
bullets([
    "Data is spread across several tabs or documents. A big part of the difficulty is <b>finding the right number quickly</b>, not the maths itself.",
    "Core skills: percentages, percentage change, ratios, averages, proportions, unit or currency conversions, reading stacked or indexed charts.",
    "Some Aon numerical items are set up so that you <b>can't finish them all</b>. Speed and accuracy both count.",
    "An <b>on-screen or physical calculator is allowed</b>. The email itself tells you to have paper, a pencil and a calculator ready.",
    "Wrong answers typically score no worse than blanks on Aon speed tests, but <b>accuracy is also tracked</b>, so don't click randomly. "
    "The email says to skip rather than guess on ability questions when you're stuck.",
])
P("1.2 Inductive (scales ix): the details", H2)
bullets([
    "Pure pattern-spotting. No maths or language.",
    "Common rule families: number of sides or elements; shading or colour; orientation and rotation; position of a small shape relative to a large one; "
    "symmetry; inside versus outside; a count that stays constant.",
    "Difficulty rises as you go, and there are sometimes two properties at once.",
    "Technique: pick <b>one attribute at a time</b> (count, then shade, then rotation...) and scan all nine for it. The odd one out usually jumps out once you look at the right attribute.",
])
P("1.3 Situational Judgement: the details", H2)
bullets([
    "Measures fit with Morgan Stanley's values: <b>Do the right thing, Put clients first, Lead with exceptional ideas, "
    "Commit to diversity and inclusion, Give back</b>.",
    "Scenarios for a sales role often involve client requests, deadline clashes, a colleague's mistake, confidential information, or a manager being unavailable.",
    "There's no time pressure, so read every option in full.",
    "The email says to respond naturally. That's good advice, but do so with the firm's values and a junior employee's position in mind (see Section 5).",
])
story.append(PageBreak())

# ---------------- 2. Scoring ----------------
P("2. How you are scored and ranked", H1)
P("2.1 Raw score, then percentile", H2)
P("Your raw score (roughly, correct answers, with accuracy and speed factored in on the reasoning tests) is converted to a "
  "<b>percentile against a norm group</b>. That's a comparison population of similar candidates, such as graduate or financial services applicants. "
  "So a 70th percentile means you beat 70% of that group. You aren't marked \"out of 100%\".")
P("2.2 Is there a pass mark?", H2)
P("Morgan Stanley doesn't publish one, and it can differ by programme, year and number of applicants. In practice, banks usually do one of the following:")
bullets([
    "<b>Hard cut-off</b> on each test (commonly estimated around the 30th to 50th percentile of the norm group). Falling below it on any single test can end the application, whatever your other scores.",
    "<b>Combined or weighted score</b> across tests, sometimes merged with the SJT and CV screen into an overall ranking.",
    "<b>Relative ranking</b>: when there are many applicants and few places (an off-cycle IM sales internship is small), recruiters may simply take the top slice of candidates for the next stage.",
])
callout("Realistic target (estimate)",
        "Aim for the <b>top 30%</b> or better on each reasoning test and a solid, values-consistent SJT. "
        "The most common way strong candidates fail is <b>one weak test</b>, usually the timed numerical, because they meet the speed for the first time on the real thing. "
        "Consistency across all three matters more than one spectacular score.")
P("2.3 What the scores feed into", H2)
bullets([
    "Your test results sit in the applicant tracking system alongside your application form and CV.",
    "Passing gets you to the next stage. For Morgan Stanley EMEA that's typically a <b>HireVue / video interview</b>, then a <b>superday or assessment centre</b> with interviews.",
    "The email notes they <b>may re-test you under supervised conditions</b> at the assessment centre. A big gap between the two scores is a red flag.",
    "After completing, you can <b>download a feedback report</b> from the Aon portal. Do this, because it shows your relative bands.",
])
P("2.4 What the reasoning tests actually value", H2)
table([
    ["Factor", "Why it matters"],
    ["Accuracy", "Wrong answers pull down the quality of your score. Being fast and sloppy doesn't pay."],
    ["Speed", "Aon tests are short and time-pressured. More correct answers in the time equals a higher percentile."],
    ["Consistency", "No section should be far below the rest. A cut-off on any one test can knock you out."],
    ["Honesty (SJT)", "Answer patterns that contradict themselves, or that are all 'textbook extreme', can look unusual."],
], [40 * mm, 130 * mm])
story.append(PageBreak())

# ---------------- 3. Integrity ----------------
P("3. \"Cheating measures\": what they check, and why it's not worth it", H1)
P("Neither Morgan Stanley nor Aon publishes a full list of their security controls. Below are the measures that are standard or "
  "explicitly stated for online Aon assessments. The point of listing them is so you <b>understand the environment and don't accidentally "
  "trip anything</b>, not to game it. Honest preparation is both the rules and the best strategy.")
table([
    ["Measure", "How it works", "What it means for you"],
    ["Supervised re-testing", "Stated in your email. They may re-test you in person at the assessment centre and compare scores.",
     "A big drop between online and in-person scores can hurt or end your application. Help from someone else only delays failing."],
    ["Large randomised item banks", "Each candidate gets a different mix of questions drawn from a big pool, often in a different order.",
     "Leaked 'answers' are useless. Only the skill transfers."],
    ["Strict timers", "Seconds per question leave no time to look things up or ask someone.",
     "Outside help is slower than your own reasoning. Practise speed instead."],
    ["Response-pattern analytics", "Test providers can review response timing and pattern data, such as implausibly fast perfect answers or odd patterns.",
     "Work naturally. Don't worry about normal hesitation."],
    ["Browser and session logging", "Online platforms can typically record session data such as device, IP address and timestamps, and may detect the test window losing focus.",
     "Stay in the test window. Close other tabs and apps. Don't exit mid-timed-section. Use 'Relaunch Test' only between sections if you drop out."],
    ["SJT consistency checks", "Similar judgements can appear in different scenarios. Contradictory answers can reduce your score.",
     "Answer from a consistent set of principles (Section 5)."],
    ["Declaration / terms", "You agree to complete it alone. Breaching this can disqualify you from Morgan Stanley applications.",
     "The consequence is bigger than one application, and banks share the same test providers."],
], [36 * mm, 67 * mm, 67 * mm])
callout("Things that are completely fine",
        "Using a calculator, pen and paper (explicitly allowed). Doing the untimed practice questions as many times as you like. "
        "Taking breaks <i>between</i> sections. Practising on third-party sites beforehand. Contacting Aon support "
        "(morganstanley.emea.support@aon.com) about technical issues or adjustments (e.g. for dyslexia, ADHD or anxiety) <b>before</b> you continue.")
callout("If something goes wrong technically",
        "Stop. Screenshot the error. Email morganstanley.emea.support@aon.com from the address you applied with, within 48 hours, "
        "and don't continue the assessments until they reply. Doing this protects you: a documented tech issue can get you a reset, "
        "but a silent bad score can't be undone.", WARN)
story.append(PageBreak())

# ---------------- 4. CV ----------------
P("4. Do they even see your CV? Why do they do this?", H1)
P("4.1 Yes, your CV still matters", H2)
P("The assessment invite doesn't mean your CV was ignored. It sits in the same applicant tracking system as your test scores. "
  "The typical flow for a Morgan Stanley EMEA campus role looks like this:")
table([
    ["Stage", "What happens", "Who or what looks"],
    ["1. Application", "CV, application form, eligibility (right to work, graduation year), sometimes motivational questions.", "System filters, then recruiters"],
    ["2. Online assessment", "This Aon simulation. Often sent to most eligible applicants automatically.", "Aon scoring; cut-offs set by Morgan Stanley"],
    ["3. CV / application review", "Candidates who pass the tests are reviewed in more depth. Strong tests plus a strong CV move forward.", "Campus recruiters, sometimes business people"],
    ["4. Video interview", "HireVue-style recorded answers (motivation, competency, markets and Morgan Stanley IM knowledge).", "Recruiters and the business"],
    ["5. Superday / AC", "Interviews with the team. May include a supervised re-test and a case or pitch (e.g. pitch a fund or asset class).", "Institutional Sales team"],
], [34 * mm, 90 * mm, 46 * mm])
P("The exact order (whether the CV is screened before or after tests) varies. For many banks the tests act as the first large-volume filter, "
  "because they're cheap to run on thousands of applicants and the CV gets a closer human read afterwards. <b>Assume both count.</b>", SMALL)
P("4.2 Why banks use these tests", H2)
bullets([
    "<b>Volume</b>: thousands of applicants for a handful of places. The tests are an objective, scalable first filter.",
    "<b>Fairness</b>: they measure everyone the same way, whatever their university or network (a big diversity goal).",
    "<b>Job relevance</b>: Institutional Sales means reading fund performance tables, AUM, fees and flows quickly and accurately in front of clients (numerical). "
    "It also means spotting patterns in markets and new information (inductive) and handling clients and colleagues with judgement and integrity (SJT).",
    "<b>Prediction</b>: cognitive ability tests are among the better-evidenced predictors of early-career performance in research on hiring.",
])
story.append(PageBreak())

# ---------------- 5. How to pass ----------------
P("5. How to pass: strategy for each test", H1)
P("5.1 Numerical reasoning", H2)
bullets([
    "<b>Read the question first, then find the data.</b> Know exactly which number you need before you touch the tabs.",
    "Watch the <b>units</b> (thousands vs millions, %, currency) and the <b>time period</b> (Q1 vs full year, 2024 vs 2025). This is where most errors come from.",
    "Know these cold: % change = (new - old) / old; % of total; ratio a:b; average; compound growth; reversing a % (original = new / (1 + r)).",
    "<b>Estimate before calculating.</b> Answer options are often far enough apart that rounding gets you there quickly.",
    "Keep the calculator in your non-writing hand, and practise on the <b>same device</b> you'll test on.",
    "If a question takes more than about 40 seconds, move on (skip it if the format allows).",
])
P("5.2 Inductive reasoning", H2)
bullets([
    "Build a mental checklist and run it in the same order every time: <b>count, shape, shading/colour, size, rotation/direction, position, symmetry</b>.",
    "Look for what the <b>majority share</b>, not what's different. The odd one out is simply the one that lacks it.",
    "Don't overthink early items. They're easy on purpose. Save time for the harder, two-rule ones at the end.",
    "Do lots of short, timed sets. This test improves faster with practice than any other.",
])
P("5.3 Situational judgement (Institutional Sales lens)", H2)
P("Answer honestly, but through the lens of a <b>conscientious junior in a regulated, client-facing firm</b>. These principles resolve most scenarios:")
table([
    ["Principle", "Typically most effective", "Typically least effective"],
    ["Integrity & compliance", "Escalate conduct, confidentiality or regulatory concerns; follow procedure; be transparent about mistakes.", "Ignoring it, covering it up, or bending rules to please a client."],
    ["Client first, honestly", "Respond promptly, set realistic expectations, come back with accurate information.", "Promising what you can't deliver, or guessing an answer to a client."],
    ["Ownership", "Take responsibility, try to solve it yourself with the resources you have, then inform your manager.", "Waiting passively, or blaming others."],
    ["Teamwork & respect", "Speak to the person directly and constructively; offer help; include others.", "Going over someone's head first, public criticism, or excluding people."],
    ["Prioritisation", "Clarify urgency with stakeholders, communicate delays early, and renegotiate deadlines.", "Silently missing a deadline, or trying to do everything badly."],
], [36 * mm, 70 * mm, 64 * mm])
P("Balance matters. The 'best' answer is usually <b>proactive but within your authority</b>: not doing nothing, and not doing something drastic alone.", SMALL)
P("5.4 On the day", H2)
bullets([
    "Laptop or PC on Chrome, plugged in, on stable Wi-Fi, with notifications off and pop-ups enabled. Avoid a phone for numerical if you can, since tables are harder to read.",
    "Quiet room. Tell people not to disturb you. Allow 90 minutes.",
    "Have a calculator, pencil, scrap paper and water ready.",
    "Do <b>every practice question</b> first, because they show you the exact interface.",
    "Order: most people start sharpest. Do the reasoning sections while fresh; the SJT is less demanding.",
    "Afterwards, download your feedback report.",
])
story.append(PageBreak())

# ---------------- 6. Practice ----------------
P("6. Where to practise", H1)
table([
    ["Resource", "What it's good for", "Cost"],
    ["Aon official practice tasks (assessment.aon.com / aon.com talent practice pages, incl. the 'Practice Tasks: inductive reasoning ix' PDF)", "The real question styles for scales numerical, scales ix and others. Start here.", "Free"],
    ["Practice section inside your Morgan Stanley simulation", "The exact interface. Repeat it before starting the timed part.", "Free"],
    ["AssessmentDay (assessmentday.co.uk / .com, Aon page)", "Aon-style numerical and inductive tests with explanations.", "Free samples, paid packs"],
    ["Practice Aptitude Tests (practiceaptitudetests.com, cut-e / Aon section)", "Timed Aon-style tests and a Morgan Stanley employer profile.", "Free samples, paid"],
    ["JobTestPrep (Morgan Stanley and Aon scales ix / numerical packs)", "Closest simulation of the MS-specific format.", "Paid"],
    ["GraduatesFirst (Morgan Stanley numerical / job tests guides)", "MS-specific numerical practice and process guide.", "Free samples, paid"],
    ["Wall Street Oasis / The Student Room / Reddit (r/FinancialCareers, r/UKjobs)", "Recent candidate reports on timings and what came up.", "Free"],
], [70 * mm, 72 * mm, 28 * mm])
P("Tip: prep sites exaggerate difficulty and 'pass marks' to sell packs. Use them for <b>timed repetitions</b>, and treat their pass-mark claims as marketing.", SMALL)

# ---------------- 7. 48 hour plan ----------------
P("7. Your 48-hour plan", H1)
table([
    ["When", "Do this"],
    ["Hour 0 to 1", "Check the portal works on your device (Chrome, pop-ups on). Note the exact deadline. If you need adjustments, email Aon now."],
    ["Hours 1 to 4", "Numerical: revise % change, ratios, reverse %, and currency conversion. Do 2 or 3 timed Aon-style numerical sets. Review every mistake: was it the data, the units or the maths?"],
    ["Hours 4 to 6", "Inductive: learn the attribute checklist. Do 4 to 6 timed 'odd one out' sets of 5 minutes each. You should see fast improvement."],
    ["Hours 6 to 7", "SJT: read Morgan Stanley's core values and what IM Institutional Sales does (client coverage of pension funds, insurers and wealth platforms). Do one practice SJT and check your reasoning against Section 5.3."],
    ["Sleep", "Seriously. Tired reasoning-test scores drop noticeably."],
    ["Day 2 morning", "One quick warm-up set of each. Then sit the real simulation while fresh, in one sitting, with at least 12 hours of buffer before the deadline."],
    ["After", "Download the feedback report. Start HireVue prep (why MS IM, why Institutional Sales, a market view, and a fund or asset class you'd pitch)."],
], [30 * mm, 140 * mm])
callout("On nerves",
        "Feeling nervous is normal and even useful. Remember: (1) the tests measure a skill you can improve in hours, not days; "
        "(2) you only need to be above the cut-off, not perfect, and <i>nobody</i> finishes every Aon question comfortably; "
        "(3) skipping a hard question is a strategy, not a failure. Breathe, read carefully, keep moving.")

P("Sources and notes", H2)
P("Your Morgan Stanley invitation email (test list, 48-hour window, re-testing, calculator, support contact). Candidate and format reports: "
  "graduatesfirst.com (Morgan Stanley numerical test), jobtestprep.co.uk (Morgan Stanley assessment), practiceaptitudetests.com (Morgan Stanley and Aon/cut-e), "
  "forgeprep.io (Morgan Stanley and Aon scales ix), assessmentday.com (Aon), assets.aon.com (Practice Tasks: inductive reasoning ix). "
  "Timings, cut-offs and security details that Morgan Stanley and Aon don't publish are <b>estimates</b> and labelled as such. Always follow the on-screen instructions.", SMALL)


def on_page(c, d):
    c.saveState()
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.HexColor("#777777"))
    c.drawString(20 * mm, 10 * mm, "Morgan Stanley Aon Assessment Guide | Janak Chohan")
    c.drawRightString(190 * mm, 10 * mm, f"Page {d.page}")
    c.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
                        topMargin=18 * mm, bottomMargin=18 * mm,
                        title="Morgan Stanley Aon Assessment Guide", author="Janak Chohan")
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print("wrote", OUT)
