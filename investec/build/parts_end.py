from lib import *
import playbook as pb

QB = {
'Motivation and fit': [
 ('Why Investec?','Have you understood what is distinctive about this firm, as a mechanism?','30-second version from Part 12: one bank for the founder and the company; mid-market; a business being built.','"Only integrated and diversified mid-market focused specialist bank" [S121]; new Corporate Bank 2026 [S268]; private-client plan [S89].','Adjectives ("prestigious", "entrepreneurial") with no fact behind them.'),
 ('Why banking, and why now?','Motivation and self-knowledge.','One moment that drew you in, what you tested since, why an internship is the right next test.','FT session in the JD [S1].','"Because it pays well."'),
 ('Why would you give up your summer for an internship?','Reported HireVue question [S41]: energy and honesty.','What you want to learn, why eight weeks inside a team beats reading about it.','"Real responsibilities" [S1].','Sounding reluctant.'),
 ('Which three teams would you like to join, and why?','Reported HR-round question [S41]. Research depth.','Rank three; for each, what the team does and why it fits you.','Fund Solutions, Corporate Banking, Private Bank, a lending niche (Part 1 table).','Naming Wealth & Investment (now Rathbones) [S78].'),
 ('Why not a bulge-bracket bank?','Did you choose Investec?','Placement in one team, small enough to see seniors, mid-market clients.','Bank of about 2,400 [S278].','Badmouthing big banks.'),
 ('Why not Close Brothers or Shawbrook?','Competitive knowledge.','They lend; Investec lends, advises, brokers and banks the founder. Admit their efficiency.','S140, S142, S121.','Claiming Investec has higher returns. It does not.'),
 ('What does "Out of the Ordinary" mean to you?','Have you looked past the slogan?','Link to the consensus-veto story and to "material ownership" culture.','S83, S278.','Reciting the tagline.'),
 ('Tell us about yourself.','Structure and story.','Present, past, why here, in 60 to 90 seconds.','One Investec-specific line at the end.','A chronological CV recital.')],
'Strengths and behaviour (JD lines)': [
 ('Tell us about a project you made your own.','Self-starter [S1].','STAR with numbers and what you personally did.','"Take a project and make it your own" [S1].','"We" throughout.'),
 ('Give us a fresh idea for Investec.','Entrepreneurial thinker [S1].','Who it helps, the problem, the smallest test, the measure.','Private-client launch H2 2027 [S225]; mid-market build [S226].','"Use AI more."'),
 ('Tell us about a time you juggled several deadlines.','Reported team-round question [S41].','Situation, how you prioritised, who you told, outcome.','Priority order (Part 11).','Saying you never miss deadlines.'),
 ('Tell us one thing about yourself we would not think to ask.','Reported HireVue question [S41]. Be you.','A specific, true passion with one detail.','"Bring your whole self" [S1].','A humblebrag.'),
 ('Who inspires you, and why?','Reported HireVue question [S41]. Values.','One person, one quality, one way you act on it.','Values: dedicated partnership, cast-iron integrity [S106].','A celebrity with no reason.'),
 ('If you could have dinner with anyone, who?','Reported HireVue question [S41]. Curiosity.','Who, what you would ask, why it matters to you.','-','Overthinking it.'),
 ('Tell us about a time you failed.','Honesty and learning.','Real failure, your part in it, what you changed.','Kensington as the firm\'s own lesson (Part 2).','A disguised strength.'),
 ('Tell us about a time you disagreed with someone.','Respectful challenge.','The disagreement, how you raised it, the outcome.','Consensus culture [S83].','Making the other person the villain.'),
 ('Tell us about working in a team.','Dedicated partnership.','Your role, a conflict or problem, what you did.','Value names [S106].','Describing a team where nothing went wrong.'),
 ('What would your friends say is your weakness?','Self-awareness.','Real weakness, evidence you are working on it.','-','"I\'m a perfectionist."')],
'Commercial awareness': [
 ('What news story have you followed recently?','Commercial awareness; the JD names the FT [S1].','What happened, why it matters to Investec, your view, what would change it.','Part 7 cards.','A headline with no view.'),
 ('How does Investec make money?','Basic bank economics.','NII 58.6%, non-interest revenue 41.4%; costs; credit losses; profit £951.0m.','S70.','Guessing numbers.'),
 ('How do interest rates affect Investec?','Two-sided thinking.','Margin up when rates rise; credit stress and deposit cost too. NII fell 1.6% in FY26.','S70, S230.','"Higher rates are good for banks", full stop.'),
 ('What is the biggest risk to Investec\'s UK business?','Judgement.','Pick one (credit in niches, execution of the investment programme, Rathbones conduct); give evidence.','UK CLR 57bps; FY27 peak investment year; Rathbones remediation [S70, S81].','Listing five risks with no ranking.'),
 ('What is private credit, and is it a threat?','Industry knowledge.','Define; threat to leveraged lending; opportunity in fund finance.','FSB $1.5-2tn; ~$220bn+ bank lines [S188].','Calling it purely a threat.'),
 ('What do you think of the UK IPO market?','Capital markets awareness.','Recovering from a low base; listing reforms; matters to broking and ECM.','H1 2026 +215%, £577m [S183]; Extel #1 [S130].','Overclaiming a boom.'),
 ('What is the motor finance issue?','Regulation and conduct.','Hidden commissions; Supreme Court Aug 2025; FCA scheme £9.1bn; tribunal suspension; Investec £30m.','S169, S172, S70.','Getting the dates wrong.'),
 ('What is Basel 3.1?','Technical depth.','Capital rules; PS1/26; from 1 Jan 2027; standardised vs IRB.','S157, S174.','Saying it starts in 2025 or 2026.'),
 ('Should banks pay a windfall tax?','Balanced opinion.','Both sides; your view; label it as a view.','S246 (reported only).','Stating it as decided policy.'),
 ('What is happening to UK bank consolidation?','Market structure.','TSB, Virgin, Co-op, Tesco Bank; why scale matters.','S193-S196, S242.','Inventing deals.'),
 ('Compare Investec with one competitor.','Analysis.','One axis at a time: model, returns, cost, clients.','Part 4 table.','A list of facts with no conclusion.'),
 ('What is the Rathbones relationship?','Firm knowledge.','2023 combination; 41% economic, 29.9% votes; profit share; advice model evolving.','S78, S80, S120.','Saying Investec owns Rathbones.')],
'Situational': [
 ('Two people give you urgent work due at the same time. What do you do?','Collision handling.','Tell both, let the senior or your manager order it, deliver, update.','Part 11 card D3.3.','Choosing silently.'),
 ('You spot a mistake in work already sent. What do you do?','Integrity and accuracy.','Decision tree in Part 11.','Cast-iron integrity [S106].','Hoping nobody notices.'),
 ('A senior asks you to send client data to your personal email.','Bright lines.','Polite no; offer an alternative; tell your manager.','Confidentiality rules.','Doing it "this once".'),
 ('You overhear what might be inside information.','Market abuse awareness.','Do not act, repeat or write it down; tell compliance.','Part 3 walls figure.','Telling a friend.'),
 ('You are given a vague task. How do you start?','Self-starter in ambiguity.','Ask what decision it informs; send a one-page plan.','Part 11 card D9.3.','Starting without scope.'),
 ('Your manager is away and the client wants an answer.','Judgement.','Never give advice yourself; find the next senior person; tell the client when they will hear back.','-','Improvising an answer.')],
'Technical-lite (be ready, not expected)': [
 ('What is net interest margin?','Vocabulary.','Spread between interest earned and paid, as a share of earning assets.','Glossary.','-'),
 ('What is a covenant?','Credit basics.','A promise in a loan agreement, e.g. debt below 4x EBITDA.','Glossary.','-'),
 ('What is loan-to-value?','Real estate lending.','Loan divided by property value; lower is safer.','Glossary.','-'),
 ('What does a CET1 ratio of 13% mean?','Capital basics.','Highest-quality capital is 13% of risk-weighted assets.','Investec plc 13.0% [S70].','-'),
 ('Walk me through a company\'s three statements.','Accounting basics.','P&L, balance sheet, cash flow, and how profit flows into each.','-','Bluffing.')],
'Curveballs': [
 ('If you ran Investec UK, what would you change?','Strategic judgement under limits.','Admit limits; name the test (return over cost of capital); pick one area with public evidence.','Part 11 card D4.3.','Pretending to know internal numbers.'),
 ('Sell me Investec in one sentence.','Concision.','The 30-second line, cut to one sentence.','Part 12.','Rambling.'),
 ('What would make you turn down an offer from us?','Honesty.','A real factor (e.g. no chance to own work), handled positively.','-','"Nothing."'),
 ('What do you think we do badly?','Courage with tact.','A sourced weakness: cost-to-income 54%, UK returns below range.','S70.','Personal criticism.')],
}

ASK = ['How are intern host teams chosen each year, and how many interns will there be in 2027?',
 'The UK graduate programme is reported as paused while early careers is redesigned. How do interns usually return, and what does that redesign look like?',
 'You have called FY27 the peak investment year. What would tell you by FY28 that the UK private client and mid-market investments are working?',
 'How does a team like Lending Operations or the Mumbai Credit Hub scale for a new Corporate Bank aiming at about 1,000 clients?',
 'With Rathbones moving to an assets-under-advice model led by Investec, how does a private banker\'s day change?',
 'How is your team thinking about private credit: as a competitor, a client through fund finance, or both?',
 'How does the move from the standardised approach toward IRB change how the UK bank prices loans?',
 'What does an intern in your team typically own by week eight?',
 'How do London teams work day to day with the Mumbai hub?',
 'What does "material ownership" look like for the most junior person on your team?']

def fig_funnel():
    st = [('Application (CV, eArcu portal)','09:00 5 Oct 2026, 24 hours, subject to volume','C'),('Video interview (HireVue)','3 questions, 1 min prep, 1 min answer','R'),
          ('HR interview with Early Careers','~30 min, two people; pick your top 3 teams','R'),('Team panel interview','~30 min, 1-2 people from the matched team; situational','R'),('Offer','Reported ~3 weeks to 52 days end to end','R'),('Internship, July 2027','8 weeks, one team in the Specialist Bank','C')]
    b = ''
    for i,(t,d,c) in enumerate(st):
        w = 680 - i*60; x = (720-w)/2; y = 8 + i*52
        f = NAVY if i==0 else (ACC if i<5 else GRN)
        b += f'<path d="M{x},{y} L{x+w},{y} L{x+w-30},{y+46} L{x+30},{y+46} Z" fill="{f}" opacity="{1 if i==0 else .9}"/>'
        b += text(360, y+20, t, 11.5, '#fff', 'middle', 'bold') + text(360, y+36, d + f'  [{ {"C":"Confirmed","R":"Reported"}[c] }]', 9, '#fff', 'middle')
    b += text(600, 30, '◀ YOU ARE HERE', 10, RED, 'start', 'bold') if False else ''
    b += f'<rect x="8" y="10" width="78" height="20" rx="4" fill="{RED}"/>' + text(47, 24, 'YOU: TODAY', 9, '#fff', 'middle', 'bold')
    return svg(720, 322, b)

def build9():
    o = part('p9', 'Part 9', 'The interview: process, question bank, questions to ask', 'What each stage looks like, 45 questions with what they test, and ten questions only a researcher could ask.')
    o += fig('The 2027 process, with your position marked', fig_funnel(), 'Sources: S1 (window, Confirmed); S7, S8 (official stages, investec.com snippets, Reported); S40, S41, S44 (Glassdoor and WSO anecdotes, Reported). No source mentions online tests or an assessment centre; one aggregator that does is unreliable [S26].')
    o += P('**Stages** [R] [S7, S8]: "You submit your CV on the application portal... If shortlisted, you will receive a link to complete a video application. Selected candidates are then invited to an interview with the Early Careers Lead, followed by a panel interview with the respective team you have chosen to join."',
           '**Reported texture** [R] [S40, S41]: video questions are "mostly strengths based with no technical questions"; the HR round is "general motivational questions and personality questions"; the team round is "nothing technical, just situational questions"; "more of a conversation than an interview". Glassdoor difficulty 2.1 out of 5; average 52 days to hire. These are forum anecdotes.',
           '**Timeline** [I]: HireVue invitations in October; HR and team interviews likely late October to December 2026. That puts the Budget (28 Oct), the MPC (5 Nov) and Investec\'s interim results (19 Nov) inside your window.')
    o += box('note', 'Since today is application day, the order of work is: (1) submit the application now; (2) prepare five HireVue answers (Part 11 and the questions below marked HireVue); (3) build your top-three teams answer; (4) read Parts 2, 3 and 12.', 'Priority')
    o += h2('p9a', 'The question bank')
    n = 0
    for grp, qs in QB.items():
        o += h3(grp)
        for q in qs:
            n += 1; o += qa(f'{n}. {q[0]}', *q[1:])
    o += h2('p9b', 'Questions to ask them')
    o += OL(*ASK)
    o += box('dont', 'Do not ask about pay, hours or holiday in the interview. Do not ask anything answered on the posting.')
    o += END
    return o

def build10():
    o = part('p10', 'Part 10', 'Interviewer briefing', 'No interviewers are named. Here is who you are likely to meet, from public professional information only.')
    o += table(['Person (public professional info)','Role','Evidence','Confidence'],[
      ['Ellis Wadsworth','Named "Meet the recruiter" on req 14049 and 14116; Talent Partner delivered by Chapter 2 (an outsourced recruitment firm) since Sept 2024; earlier recruitment roles at hackajob and insightsoftware','S1, S2 (Confirmed); S45, S46 (profiles, Reported)','High that this is the named recruiter; career details medium'],
      ['Early Careers Lead (publicly associated: Shaleen Aslam)','Runs the HR interview per investec.com; a LinkedIn headline reads "Early Careers Lead and Recruitment Programme Consultant", Investec Bank plc','S7 (Reported); S47, S48 (snippets)','Currency not verified: may not be in role in Oct 2026. Do not name them unless they introduce themselves'],
      ['UK Head of People & Organisation','Reported as Jason Spivey, joined Feb 2026','S290 (snippet only)','Low. Use the title, not the name'],
      ['Your team panel','1 or 2 people from the matched team, sometimes an analyst','S41 (Reported)','Practitioners: pitch answers to the work']])
    o += h2('p10a', 'Reading the interviewer live')
    o += table(['Type','How to tell','How to pitch'],[
      ['Early-careers / HR','Asks about motivation, values, teams you want; takes notes against a scorecard','Clear structure; values language; show you read the JD; be warm'],
      ['Business practitioner','Asks about deals, clients, the market; follows up on detail','Concrete examples; one opinion with a source; ask about their work'],
      ['Analyst on the panel','Close to your age; asks how you would handle the work','Show you would be easy to work with: clarity, accuracy, asking early'],
      ['Silent or hard to read','Few signals','Keep answers to 60 to 90 seconds; check "Would you like more detail on any part?"']])
    o += box('dont', 'Do not mention that you looked anyone up unless they bring it up. Never refer to anything personal. If you are unsure whether a name is right, use the job title.')
    o += END
    return o

def build11():
    o = part('p11', 'Part 11', 'The scenario playbook', 'A method for holding your frame under pressure, three scenarios for every line of the job description, a composure set and a CV grill.')
    o += h2('p11a', 'The four-step protocol')
    o += fig('The four-step answer protocol', pb.fig_protocol(), 'Method by the author [I].')
    o += table(['Step','Phrases that execute it'],[
      ['Steady','"Let me make sure I have this right..." · "So the situation is..." · one breath before you start'],
      ['Sort','"There are two things in tension: X and Y." · "What matters most here is..."'],
      ['Act','"First I would... then..." · "I would tell [manager/compliance] because..." · "By [time] I would..."'],
      ['Close','"The principle I would hold to is..." · "So in short: integrity and accuracy first, then speed."']])
    o += fig('The priority order when good things collide', pb.fig_priority(), 'Method by the author [I], anchored to Investec\'s stated value "cast-iron integrity" [S106] and the FCA Consumer Duty [S168].')
    o += fig('Eight ways interviewers break a frame, and the counter to each', pb.fig_tactics(), 'Method by the author [I].')
    o += h3('Staying calm physically')
    o += UL('Before: feet flat, slow breath out (longer out than in), water nearby, notes face-down.',
            'During: pause before answering; it reads as thought, not panic. Write the question\'s key word on paper.',
            'On video: look at the camera when making your key point; keep hands visible; light in front of you.',
            'If you blank: "Can I take a moment?" Then use the protocol from step 1.')
    o += h2('p11b', 'The scenario ladder')
    o += fig('Every JD line, three rungs', pb.fig_ladder(), 'Ladder built from the eleven JD lines in Part 1 [S1].')
    for code, line in pb.DUTIES:
        o += f'<h3>{code}. {esc(line)}</h3>'
        cards = pb.SC[code]
        for j,c in enumerate(cards):
            o += c.replace('<h4>', f'<h4>{code}.{j+1} ', 1)
    o += h2('p11c', 'The composure set')
    for t,s,a in pb.COMPOSURE:
        o += card('hard', t, s, 'Panicking, hiding it, or acting alone outside your role.', a, 'Holds the priority order: rules and the client first, accuracy, then speed. Tells the right person early.', 'They escalate: "The MD says do it anyway." Hold: same answer, calmly, and tell your manager.')
    t1, t2 = pb.fig_trees()
    o += fig('Decision tree: a senior asks you to skip a control', t1, 'Method by the author [I]. Draw it from memory: rule, grey area, habit.')
    o += fig('Decision tree: a mistake you made', t2, 'Method by the author [I]. Draw it from memory: not yet acted on, acted on internally, seen by a client.')
    o += h2('p11d', 'The CV grill')
    o += P('A three-levels-deep attack goes: **what** you did, then **why** you did it that way, then **what if** it had gone differently or **what would you change**. Each level tests whether you really did it.')
    grill = [('"Talk me through this bullet."','State the situation in one line, your action, the result with a number.'),
             ('"What exactly did YOU do?"','Name your part with verbs: I built, I wrote, I chased. Credit the team once.'),
             ('"Why did you do it that way?"','Give the alternative you rejected and why.'),
             ('"That number sounds high. How did you measure it?"','Explain the measure plainly; if it was an estimate, say so.'),
             ('"What went wrong?"','A real problem and what you changed.'),
             ('"What would you do differently?"','One specific change, not "nothing".'),
             ('"How is this relevant to banking?"','One transferable skill: analysis, accuracy, clients, deadlines.'),
             ('"This looks like a gap / short stint."','A short factual reason, then what you did with the time.')]
    o += table(['Attack','Frame-holding answer'], grill)
    o += box('note', '<b>Four-line drill for every CV bullet.</b> (1) What I did, in one sentence. (2) The number and how I know it. (3) The hardest moment and what I did. (4) What it shows that matters at Investec.', 'Drill')
    o += END
    return o

def fig_why():
    b = rect(5, 5, 710, 60, NAVY, NAVY) + text(360, 32, 'WHY INVESTEC, IN ONE PAGE', 15, '#fff', 'middle', 'bold') + text(360, 52, 'Mechanism, not adjectives', 10.5, ACC, 'middle', 'bold')
    cols = [('1. The structure','One bank for the founder and the company: private bank + mid-market lending + advisory and broking. Lenders don\'t advise; brokers don\'t lend.','S121, S125'),
            ('2. The moment','FY27 is the peak investment year: a new Corporate Bank (launching 2026) and a full UK private bank (H2 2027). Interns join a build.','S70, S89, S268'),
            ('3. The scale','A UK bank of ~2,400 people: one team, real work, seniors you meet. Not a rotation.','S278, S1'),
            ('4. The culture','Founders\' consensus-after-challenge rule; "material ownership, freedom to operate with accountability".','S83, S278')]
    for i,(t,d,s) in enumerate(cols):
        x = 5 + i*178
        b += rect(x, 78, 170, 190, [TEALS,ACCS,GRNS,SIGS][i], [TEAL,ACC,GRN,SIG][i], 6)
        b += text(x+10, 100, t, 11.5, NAVY, 'start', 'bold') + text(x+10, 122, d, 9.4, NAVY, width=31, lh=12) + text(x+10, 258, s, 8, MUT)
    b += rect(5, 280, 710, 52, '#fff', RED, 6) + text(15, 300, 'Honest limits: UK RoTE 13.7% (below Shawbrook, OakNorth, Coutts); cost-to-income 54%; UK H1 profit guided 2-6% lower;', 9.4, RED) + text(15, 316, 'no published UK cross-sell figure. Say "distinctive", never "best".', 9.4, RED)
    return svg(720, 340, b)

def build12():
    o = part('p12', 'Part 12', '"Why Investec" in three lengths, and the counter-case', 'Built from mechanism. Each version could not be said about a rival without changing the words.')
    o += fig('Why Investec on one page', fig_why(), 'Sources as marked in each column; full detail in Parts 2 to 4.')
    o += h2('p12a', 'Thirty seconds')
    o += box('say', '"Investec is the one bank I found that serves both the entrepreneur and the business they own: a private bank, mid-market lending, and its own advisory and broking arm under one roof. Its UK business is in its peak investment year, building a new corporate bank and a full private bank, so an intern joins something being built. And at about 2,400 people in the UK bank, I would be in one team doing real work, not on a rotation."')
    o += h2('p12b', 'Two minutes')
    o += box('say', '"Three reasons, and they are about how the firm works rather than adjectives.<br><br>First, the structure. Most UK competitors do one thing. Close Brothers, Shawbrook and OakNorth lend. Peel Hunt and Numis advise. Coutts runs a private bank. Investec describes itself as the only integrated mid-market specialist bank, and the reason that matters is the client lifecycle: a founder needs growth debt, then advice on a sale or listing, then a mortgage and somewhere to put the money. One bank can serve each stage, and Investec ranks first among UK small and mid-cap brokers while also lending.<br><br>Second, the moment. Management calls FY27 the peak investment year. The UK is building a corporate bank that Andy Hart says should feel like private banking, and launching current accounts and cards for private clients in the second half of 2027. UK returns are below the target range right now, which is exactly why the next two years are interesting.<br><br>Third, the culture has a mechanism. Ian Kantor says the founders each had a veto, so anything was possible with consensus. Today\'s annual report describes material ownership and freedom to operate with accountability. In a UK bank of about 2,400 people, that means an intern in one team, owning real work, close to senior people.<br><br>I am realistic: Shawbrook and OakNorth earn higher returns at lower cost. Investec\'s bet is depth of relationship, and I want to see how that is built."')
    o += h2('p12c', 'The close: one specific thing')
    o += box('say', '"If I could choose, I would most like to work on [Fund Solutions / the new Corporate Bank / the private client launch], because [it sits where private credit and banks meet / it is being built right now / it turns a mortgage lender into a primary bank]. By week eight I would want to have owned one piece of work the team actually used."')
    o += h2('p12d', 'What most candidates say vs what you can say')
    o += table(['Most candidates','You'],[
      ['"Entrepreneurial culture"','Kantor\'s consensus-veto rule; "material ownership, freedom to operate with accountability" [S83, S278]'],
      ['"Out of the ordinary"','The UK bank is converting from specialist lender to primary bank for two client types [S89, S90]'],
      ['"Prestigious, global bank"','A UK bank of 2,425 people inside a DLC with South Africa [S278, S120]'],
      ['"Great private bank"','Income- and founder-led client definition; 8,200 UK clients, growing [S123, S124]'],
      ['"Strong financial results"','£951.0m profit, but UK RoTE 13.7% and guided lower; peak investment year [S70, S71]'],
      ['"I want to learn about finance"','I want to own one piece of work in [named team] and see how One Investec works in practice']])
    o += h2('p12e', 'The honest counter-case')
    o += UL('Returns: UK below Shawbrook, OakNorth, Coutts, Barclays PBWM [S120, S140-S148].', 'Efficiency: cost-to-income 54% vs 26 to 36% at lean peers [S120, S144, S240].',
            'Integration unproven by public data: no UK cross-holding figure [S120]; HSBC also grows cross-referrals [S149].', 'Rathbones, the investment engine of the private client plan, is under FCA-prompted remediation [S81].',
            'Graduate programme paused: return routes are ad hoc [S8].', 'Execution risk: UK H1 profit guided 2 to 6% lower while spending continues [S71].')
    o += END
    return o

def fig_cheat():
    b = rect(0,0,720,40,NAVY,NAVY,0) + text(360, 26, 'INVESTEC SUMMER INTERNSHIP 2027 · ONE-PAGE CHEAT SHEET', 14, '#fff', 'middle', 'bold')
    blocks = [
     (10, 50, 345, 150, 'PROTOCOL (45-75 sec)', ['1 STEADY: restate in one line','2 SORT: "two things in tension..."','3 ACT: steps, real people, times','4 CLOSE: one principle. Stop.'], TEAL),
     (365, 50, 345, 150, 'PRIORITY ORDER', ['1 Rules, confidentiality, Investec\'s name','2 The client and team commitments','3 Accuracy and the record','4 Speed','"Never trade integrity or accuracy for speed."'], RED),
     (10, 210, 345, 165, 'NUMBERS IF ASKED (FY26, to 31 Mar 26)', ['Group adj. op. profit £951.0m (+3.4%)','ROE 13.6% · C/I 52.9% · CLR 36bps','NII 58.6% / non-interest 41.4%','UK SB profit £401.6m; loans £17.8bn','Investec plc RoTE 13.7%; CET1 13.0%','IBP staff 2,425; group 8,000+'], NAVY2),
     (365, 210, 345, 165, 'DATES', ['Founded 1974 Jo\'burg · DLC 2002','Rathbones 2023 (41% econ / 29.9% votes)','Bank Rate 3.75%; MPC 5 Nov','Budget 28 Oct · Interims 19 Nov','Basel 3.1 (PS1/26) from 1 Jan 2027','FSCS £120k since 1 Dec 2025'], ACC),
     (10, 385, 345, 160, 'COUNTERS', ['Interrupted: "Of course." Answer, then finish.','Contradicted: "Which part?"','Silence: wait; offer depth','Authority squeeze: help + check first','False choice: answer, then name option C','Knowledge trap: "I don\'t know precisely; here\'s how I\'d reason"'], SIG),
     (365, 385, 345, 160, 'NEVER', ['Claim "best" or "highest returns"','Name Wealth & Investment as a team','Raise cum-ex or fines unprompted','Quote the windfall tax as policy','Send client data outside the bank','Bluff a number'], RED),
     (10, 555, 700, 105, 'LINES READY', ['"One bank for the founder and the company: private bank, mid-market lending, advisory and broking."','"FY27 is the peak investment year: a new Corporate Bank and a full UK private bank. I\'d join a build."','"Material ownership, freedom to operate with accountability: that\'s what I want in eight weeks."','ASK: "What would tell you by FY28 that the UK investments are working?"'], GRN)]
    for x,y,w,h,t,items,c in blocks:
        b += rect(x, y, w, h, '#fff', c, 6, 1.6) + rect(x, y, w, 22, c, c, 6) + text(x+10, y+16, t, 10.5, '#fff', 'start', 'bold')
        for i,it in enumerate(items):
            b += text(x+12, y+40+i*(19 if h>110 else 19), it, 9.6, NAVY)
    return svg(720, 668, b)

def build13():
    o = part('p13', 'Part 13', 'Cheat sheet', 'Everything you need in the five minutes before you join the call.')
    o += fig('The cheat sheet on one page', fig_cheat(), 'Figures: S70, S120, S278, S282 (Confirmed). Dates: S78, S80, S157, S176, S222, S230, S244. Also saved separately as Cheat_Sheet.pdf.')
    o += END
    return o

GLOSS_EXTRA = [('Adjusted operating profit','Profit before tax, after stripping out items management considers one-off; Investec\'s headline profit measure.'),
 ('Associate','A company in which a group owns a big stake (often 20-50%) but not control; it books its share of profit. Rathbones is Investec\'s.'),
 ('DLC (dual-listed company)','Two listed parents run as one group with one board: Investec plc (London) and Investec Limited (Johannesburg).'),
 ('IBP','Investec Bank plc, the main UK banking subsidiary of Investec plc.'),('IGSI','Investec Global Services India, the Mumbai service hub.'),
 ('One Investec','Investec\'s term for serving a client across its businesses.'),('Pre-close statement','A trading update just before a reporting period ends.'),
 ('RNS','Regulatory News Service: the official channel for listed-company announcements in London.'),('HireVue','A one-way video interview platform: you record answers to set questions.'),
 ('Information barrier','Controls that stop inside information passing between teams; also called a Chinese wall.'),('Inside information','Precise non-public information likely to move a listed share price if known.'),
 ('Relationship manager (RM)','The banker who owns a client relationship and routes needs to product teams.'),('Wall crossing','Formally bringing a public-side person inside on a deal, approved and logged by compliance.'),
 ('Specialist bank','A bank focused on specialist lending niches rather than mass-market products.'),('Subscription line','A loan to a fund secured on investors\' promises to invest.'),
 ('NAV loan','A loan to a fund secured on the value of its investments.'),('Windfall tax','A one-off tax on profits seen as unearned luck.'),('Bank surcharge','An extra corporation tax that only banks pay (3%).'),
 ('Through the cycle','Averaged over good and bad years of the economy.'),('Basis point','One hundredth of one percent.')]

def build14(glossary):
    o = part('p14', 'Part 14', 'Glossary', f'{len(glossary)} terms in plain English.')
    o += '<dl class="gl">' + ''.join(f'<dt>{esc(t)}</dt><dd>{md(d)}</dd>' for t,d in glossary) + '</dl>'
    o += END
    return o

def build15(rows):
    o = part('p15', 'Part 15', 'Source table', 'Every [Sxx] marker resolves here. Accessed 5 October 2026 unless noted. Status: FETCHED (read in full), SNIPPET (search result only), PAYWALLED-NOT-READ.')
    o += P('<span class="small">Duplicate IDs: S70, S120, S174, S220 and S282 are the same document (Investec FY26 results RNS, 21 May 2026), cited by different workstreams. S71 and S222 are the same pre-close statement. S1 and S263 are the same posting.</span>')
    body = [[f'S{n}', esc(r[1]), esc(r[2]), esc(r[3]), f'<span style="word-break:break-all">{esc(r[4])}</span>', esc(r[5]), esc(r[6])] for n,r in sorted(rows.items())]
    h = ''.join(f'<th>{c}</th>' for c in ['ID','Outlet','Title','Published','URL','Status','Note'])
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in body)
    o += f'<table class="src"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'
    o += END
    return o

def build16():
    o = part('p16', 'Part 16', 'Gaps and open questions', 'What could not be established, and how to close each gap before your interview.')
    o += table(['Gap','Why it matters','How to close it'],[
      ['investec.com was blocked (HTTP 403) to automated reading','Values wording, careers pages, press releases came from snippets','Open the pages in a browser yourself: About us, Careers > Graduates, Press'],
      ['2027 host teams not published','The "top three teams" answer','Ask at the HR interview; read Investec LinkedIn posts from summer 2026'],
      ['Intern cohort size and pay','Expectations','Ask early careers; Glassdoor figures are unreliable (£21k-£32k range)'],
      ['UK cross-holding figure (clients using two or more businesses)','Proof of One Investec','Investor presentations of 20 Nov 2025 and 21 May 2026'],
      ['UK private client targets conflict (City AM 16,000 households vs Reuters +5,000 clients)','Avoid quoting a wrong number','Investec press release of 21 May 2026'],
      ['FTSE 100 or FTSE 250 membership','Basic fact','FTSE Russell constituents list'],['JSE listing year (1986 or 1988)','History','Investec "Our history" page'],
      ['Net interest margin','A common technical question','FY26 results presentation'],['Investec Bank plc full-year FY26 figures','UK-bank-only numbers','IBP 2026 annual report (Companies House)'],
      ['Current risk appetite limits','Credit discussion','FY26 risk management report'],['Cum-ex outcome after 2021','Skeleton completeness','FY26 contingent liabilities note'],
      ['Ninety One residual stake','History','Investec annual report'],['UK executive committee beyond the board','Who runs which business','investec.com leadership page'],
      ['Current Early Careers Lead and UK Head of P&O','Interviewer briefing','LinkedIn; do not name unless confirmed'],
      ['Ring-fencing status of IBP in a primary source','Avoid overclaiming','IBP annual report regulatory section'],
      ['FT and Bloomberg coverage','Commentary on results and the Budget','University library access'],
      ['Shawbrook post-IPO share price; OakNorth US bank deal; NatWest-Evelyn completion date','Peer detail','Company releases'],
      ['Search budget ran out in three workstreams','Some Reddit, LinkedIn and eFinancialCareers content unchecked','Not material to the interview']])
    o += h2('p16a', 'Final self-check')
    o += table(['Check','Status'],[
      ['Every figure has a source and date; estimates labelled on charts','Done. Charts state period, source and measure; mixed measures labelled'],
      ['A beginner can read Parts 1, 2 and 5 alone','Done. Terms defined in line and in the glossary'],
      ['"Why Investec" is mechanism, not adjectives, and not transplantable','Done. Part 12 cites structure, timing, scale and culture with sources'],
      ['Regulatory section current and dated','Done. Dates checked against BoE, PRA, FCA, HMT pages (Part 6); two minor date uncertainties flagged'],
      ['Team section goes beyond the JD with method shown','Done, with thin evidence admitted: no host-team list and no cohort size exist publicly'],
      ['Every JD line has three scenarios; composure set has decision trees','Done: 11 lines x 3 cards; 5 composure cards; 2 trees'],
      ['People sections: public professional information only, uncertainty flagged','Done'],
      ['PDF rendered, contents page numbers correct, figures checked for clipping','See build log; contents numbers produced by a two-pass render'],
      ['What could not be found is listed','This page']])
    o += END
    return o

def fig_master():
    b = ''
    b += rect(5, 5, 230, 300, TEALS, TEAL) + text(120, 26, 'THE INDUSTRY', 12, TEAL, 'middle', 'bold')
    for i,t in enumerate(['Rates held at 3.75%, hike debate','Private credit: rival and client','Consolidation of mid-tier banks','Basel 3.1 from 1 Jan 2027','IPO market recovering','Budget 28 Oct: bank tax risk']):
        b += rect(15, 40+i*42, 210, 34, '#fff', LINE, 4) + text(120, 61+i*42, t, 9.2, NAVY, 'middle')
    b += rect(245, 5, 230, 300, ACCS, ACC) + text(360, 26, 'THE FIRM', 12, '#9a5e10', 'middle', 'bold')
    for i,t in enumerate(['Founded 1974; DLC London + Jo\'burg','FY26 profit £951m; UK RoTE 13.7%','Private Bank + mid-market CIB','Advisory and broking (Extel #1 SMID)','Rathbones 41% stake','FY27 peak investment year']):
        b += rect(255, 40+i*42, 210, 34, '#fff', LINE, 4) + text(360, 61+i*42, t, 9.2, NAVY, 'middle')
    b += rect(485, 5, 230, 300, GRNS, GRN) + text(600, 26, 'THE ROLE', 12, GRN, 'middle', 'bold')
    for i,t in enumerate(['8 weeks, one team, July 2027','Matched at HR interview: top 3 teams','Real work: research, models, papers','FT, analysis, Excel training','Entrepreneurial, self-starter, be you','Return route: ad hoc entry roles']):
        b += rect(495, 40+i*42, 210, 34, '#fff', LINE, 4) + text(600, 61+i*42, t, 9.2, NAVY, 'middle')
    for y in [57, 141, 225]:
        b += arrow(226, y, 253, y, accent=True) + arrow(466, y, 493, y, accent=True)
    b += rect(5, 318, 710, 46, NAVY, NAVY) + text(360, 338, 'YOUR ANSWER CONNECTS ALL THREE', 11, ACC, 'middle', 'bold') + text(360, 354, 'Industry pressure → Investec\'s integrated, relationship-led bet → why an intern in a team being built learns fastest', 10, '#fff', 'middle')
    return svg(720, 370, b)

def build0():
    o = part('p0', 'Part 0', 'How to use this pack, and the 10-minute version', 'Today is 5 October 2026, application day. The interview will probably fall in late October to December.')
    o += box('unc', '<b>Apply first.</b> The 2027 window opened at 09:00 on 5 October 2026 for 24 hours and may close early "subject to volume of applications" [C] [S1]. Everything else in this pack can wait an hour.')
    o += h2('p0a', 'The 10-minute emergency version')
    o += OL('**What it is:** an 8-week summer internship in one team of Investec\'s UK Specialist Bank, chosen with you at the HR interview. Any degree; penultimate or final year [S1].',
            '**The process:** CV, then a HireVue (three strengths questions, one minute each), then a 30-minute HR interview (name your top three teams), then a 30-minute team panel (situational). Reported, not official detail [S7, S41].',
            '**The firm in one line:** a UK/South African specialist bank and wealth group, founded 1974, that combines a private bank with mid-market lending, advisory and broking [S120, S121].',
            '**Numbers:** FY26 group profit £951.0m; ROE 13.6%; UK RoTE 13.7%, below target; FY27 is the "peak investment year" [S70].',
            '**What is changing:** a new UK Corporate Bank launching 2026; UK private bank adding current accounts and cards in H2 2027; Rathbones (41% owned) moving to Investec-led advice [S89, S120, S268].',
            '**Your why:** one bank for the founder and the company; a business being built; a bank small enough to own real work (Part 12).',
            '**The macro:** Bank Rate 3.75%, three MPC members voting to hike; Budget 28 Oct; Basel 3.1 from 1 Jan 2027 [S150, S157, S244].',
            '**The method under pressure:** steady, sort, act, close; integrity and accuracy before speed (Part 11).',
            '**Never:** say "best"; name Wealth & Investment as a team; quote the windfall tax as policy.',
            '**Ask:** "What would tell you by FY28 that the UK investments are working?"')
    o += h2('p0b', 'How to use the pack')
    o += table(['If you have','Read'],[['10 minutes','This page and the cheat sheet (Part 13)'],['1 hour','Parts 12, 2, 1, then the HireVue questions in Part 9'],['An evening','Parts 0 to 4, 9 and 11'],['A week','Everything, then re-read Part 7 the night before and check the dates']])
    o += P('Confidence tags: <span class="c cC">Confirmed</span> primary source or two credible outlets; <span class="c cR">Reported</span> one source or a search snippet; <span class="c cI">Inferred</span> the author\'s reasoning. Every [Sxx] resolves in Part 15.')
    o += fig('The master map: industry, firm and role, connected', fig_master(), 'Summary of Parts 1 to 7; sources there.')
    o += END
    return o
