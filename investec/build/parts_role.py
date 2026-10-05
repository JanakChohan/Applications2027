from lib import *

JD = [
 ('"Become part of a team within our Specialist Bank (we will discuss the best aligned team for you during your HR interview from the range of business areas hosting an Internship position)"',
  'You are not on a rotation. You join one team for eight weeks. Which team is decided with you at the HR interview, from whichever areas have put up an intern position that year [C] [S1]. Candidates report being asked for their top three teams and why [R] [S40, S41].',
  'The early-careers team, then the hiring manager of the host team.',
  'A ranked, reasoned list of three teams, each tied to what the team actually does.',
  'The bank is a set of specialist teams that each hire for themselves. No central analyst pool [I].'),
 ('"You will gain insight into our culture and the opportunity will provide you with exposure to our senior leaders"',
  'Talks and Q&As with senior people; in a bank of about 2,400 people you will see the CEO and heads of business in person [C] [S278] [I].',
  'Senior leaders, programme organisers.',
  'One good question per session; a short note afterwards.',
  'Scale: the UK bank is small enough that seniors meet interns [I].'),
 ('"As an intern, you will be given real responsibilities and have an opportunity to contribute and deliver to whichever team you join"',
  'Day-to-day work for the team: research, spreading financial statements into models, sections of credit papers, client meeting packs, data clean-up, a project to present at the end [I].',
  'Analysts and associates on your team; your manager; sometimes a client-facing banker.',
  'Accurate work, delivered on time, with your assumptions stated. Asking early when unclear.',
  'Teams are lean; an extra pair of hands matters [I].'),
 ('"Although embedded into one team we aim to provide you with a clear overview of our entire business"',
  'Speaker sessions, shadowing, and conversations across Private Banking, Corporate & Investment Banking and the centre [C] [S1] [I].',
  'Other interns; people in other teams.',
  'You can explain how your team fits into the bank and its money flow (Part 2).',
  'One Investec: the firm wants people who see across businesses [C] [S120].'),
 ('"Presentations and talks from experienced Investec employees across our business... a number of networking opportunities"',
  'A speaker series and social events through the summer [C] [S1].',
  'Speakers, other interns, alumni of past cohorts.',
  'Prepared questions; follow-ups within a day.',
  'Relationship culture: networking is part of the job, as it is with clients [I].'),
 ('"Gain insight into how you can absorb complex information easily from the Financial Times and how to immerse yourself in financial analysis"',
  'A session on reading the FT efficiently, and a session on financial analysis [C] [S1].',
  'Trainers; your team.',
  'A daily habit: one story, why it matters to Investec, your view.',
  'The firm expects commercial awareness from day one [I].'),
 ('"Don\'t forget the fun and engaging Excel courses"',
  'Excel training: formulas, lookups, pivot tables, probably simple modelling [C] [S1] [I].',
  'Trainers.',
  'Clean, labelled spreadsheets with inputs separate from calculations.',
  'Excel is still the working tool of credit and finance teams [I].'),
 ('"Entrepreneurial thinker: we want to hear your fresh ideas!"',
  'In interviews: evidence you have started or changed something. In the internship: suggesting a better way to do a task [C] [S1].',
  'Interviewers; your manager.',
  'An idea that is small, testable and specific.',
  'Founded by entrepreneurs; culture of "material ownership" and "freedom to operate with accountability" [C] [S278].'),
 ('"Self-starter: show us your ability to take a project and make it your own!"',
  'Owning a task end to end without being chased [C] [S1].',
  'Your manager.',
  'You scope it, you chase inputs, you deliver, you report back.',
  'Flat structure: less hand-holding than a big bank [R] [S132, S277].'),
 ('"Be you: bring your whole self to work. We want to know about your passions and interests!"',
  'The interviewers will ask about you as a person. HireVue questions reported include "Tell us one thing about yourself that we wouldn\'t think to ask" [R] [S41].',
  'Interviewers.',
  'A true, specific passion, told briefly.',
  'Reviewers say Investec cares about "how you will fit into the Investec team" more than "what you have on paper" [R] [S41].'),
 ('"All interns must be in their penultimate or final year of University study"',
  'Eligibility. UK work permission is needed; no sponsorship reported [R] [S7].',
  'Early-careers team.',
  'Know where you would go next: the rotational graduate scheme is reported paused; return routes are ad hoc entry-level roles [R] [S8, S9].',
  'Early careers is being redesigned [R] [S8].'),
]

def fig_chain():
    st = [('Team need','A banker needs a company profile before a client call'),('Brief','Manager tells you: what, by when, what format'),
          ('Research and build','Annual reports, Companies House, data; model in Excel'),('Check','You check your numbers; analyst reviews'),
          ('Deliver','Short pack or one-page note, assumptions listed'),('Outcome','Banker uses it; you get feedback; next task is bigger')]
    b = ''
    for i,(t,d) in enumerate(st):
        x = 6 + i*119
        b += node(x, 20, 108, 110, t, d, fill=[TEALS,TEALS,ACCS,ACCS,GRNS,GRNS][i], stroke=[TEAL,TEAL,ACC,ACC,GRN,GRN][i], size=11, subsize=9, subw=20)
        if i < 5: b += arrow(x+109, 75, x+118, 75)
    b += text(360, 160, 'The loop repeats several times a week. Speed of the loop and accuracy of step 4 are what you are judged on.', 10, NAVY, 'middle', 'bold')
    return svg(720, 175, b)

def fig_channels():
    b = rect(5, 5, 350, 250, TEALS, TEAL) + rect(365, 5, 350, 250, ACCS, ACC)
    b += text(180, 30, 'PRIVATE BANKING', 13, TEAL, 'middle', 'bold') + text(540, 30, 'CORPORATE & INVESTMENT BANKING', 13, '#9a5e10', 'middle', 'bold')
    pb = ['Client: high-income professional or entrepreneur','Product: mortgage, lending, savings; soon current account and card','Unit of work: a client request','Typical intern task: analyse a client\'s income and assets; prepare a meeting pack; KYC checklist','Rules that bind: Consumer Duty, mortgage rules, KYC/AML']
    cb = ['Client: mid-market company, PE sponsor, fund','Product: loan, fund finance, hedge, advice, IPO, broking','Unit of work: a deal','Typical intern task: spread financials, comparable companies, a section of a credit paper or pitch','Rules that bind: credit policy, market abuse and inside information, conflicts']
    for i,(a,c) in enumerate(zip(pb,cb)):
        b += text(20, 58+i*40, a, 9.6, NAVY, width=60, lh=11.5) + text(380, 58+i*40, c, 9.6, NAVY, width=60, lh=11.5)
    return svg(720, 262, b)

def fig_day():
    rows = [('08:30','Arrive; read the FT and the team\'s news alerts; note one story'),('09:00','Team check-in: what is due today'),
            ('09:30','Main task: spread three years of accounts for a borrower into the credit model'),('11:30','Ask the analyst two questions you saved up'),
            ('12:30','Lunch, sometimes an intern speaker session'),('13:30','Fix the model after review; write the summary paragraph'),
            ('15:00','Sit in on a client call or internal credit discussion (listen, take notes)'),('16:00','Excel course or networking coffee'),
            ('17:00','Send the work with a note: what you did, what you assumed, what is open'),('18:00','Log the day: what you learned, what to ask tomorrow')]
    b = ''
    for i,(t,d) in enumerate(rows):
        y = 8 + i*27
        b += rect(10, y, 70, 22, NAVY, NAVY, 4) + text(45, y+15, t, 10, '#fff', 'middle', 'bold')
        b += rect(86, y, 624, 22, SOFT if i%2 else '#fff', LINE, 4) + text(96, y+15, d, 9.8, NAVY)
    return svg(720, 284, b)

def fig_orgchart():
    b = ''
    def nd(x,y,w,h,t,s,conf):
        f,st = {'C':(GRNS,GRN),'R':(ACCS,ACC),'I':(SIGS,SIG)}[conf]
        return node(x,y,w,h,t,s,fill=f,stroke=st,size=9.6,subsize=8.4)
    b += nd(250,8,220,44,'Group P&O (global head)','Lesley-Anne Gatter per press snippet','R')
    b += nd(250,72,220,44,'UK People & Organisation','Owns req 14049 [S1]. UK head reported as Jason Spivey (snippet)','C')
    b += nd(40,140,200,48,'Resourcing / Talent Acquisition','"a member of the resourcing team will be in touch" [S4]','C')
    b += nd(260,140,200,48,'Early Careers team','"look after apprenticeship, internship and all entry-level roles" [S4]','C')
    b += nd(480,140,200,48,'Chapter 2 (outsourced recruiters)','Ellis Wadsworth named recruiter on 14049 [S1]','C')
    b += nd(260,210,200,48,'Early Careers Lead','Runs the HR interview [S7]; publicly associated: Shaleen Aslam (unverified currency)','R')
    b += nd(40,290,640,44,'Host teams in the Specialist Bank (2027 list not published)','Fund Solutions (only team with a named past intern), Corporate Banking, lending niches, Private Bank, Treasury, central functions','I')
    for x1,y1,x2,y2 in [(360,52,360,72),(360,116,140,140),(360,116,360,140),(360,116,580,140),(360,188,360,210),(360,258,360,290)]:
        b += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{MUT}" stroke-width="1.3"/>'
    for i,(c,l) in enumerate([('C','Confirmed'),('R','Reported'),('I','Inferred')]):
        f,st = {'C':(GRNS,GRN),'R':(ACCS,ACC),'I':(SIGS,SIG)}[c]
        b += rect(40+i*120, 348, 16, 12, f, st, 2) + text(62+i*120, 358, l, 9.5, NAVY)
    return svg(720, 368, b)

def fig_request():
    st = [('Request','Banker emails: "Can you pull together X by Thursday?"'),('Clarify','You repeat back: scope, deadline, format, example'),
          ('Plan','15-minute outline sent back for a yes'),('Do','Research, model, draft'),('Self-check','Totals tie? Sources cited? Spelling of client name?'),
          ('Review','Analyst or associate reviews; you fix'),('Sign-off','Senior uses it; it may go to a client'),('Record','Saved in the right folder; version labelled')]
    b = ''
    for i,(t,d) in enumerate(st):
        col = i % 4; row = i // 4
        x = 8 + col*178; y = 10 + row*110
        b += node(x, y, 165, 90, t, d, fill=[TEALS,ACCS][row], stroke=[TEAL,ACC][row], size=11, subw=30)
        if col < 3: b += arrow(x+166, y+45, x+177, y+45)
    b += path('M700,55 L712,55 L712,108 L90,108 L90,118', MUT)
    return svg(720, 225, b)

def build():
    o = part('p1', 'Part 1', 'The role, decoded line by line, and the team mapped', 'What each sentence of the job description really means, a day in the seat, and the people behind the process.')
    o += h2('p1a', 'The job description, line by line')
    o += P('The 2027 posting is requisition 14049, London, 30 Gresham Street; Department People & Organisation; Division IBP Business Enablement; eight weeks from July; any degree; penultimate or final year [C] [S1, S7]. A parallel posting (14116) runs the same programme with the 10,000 Interns Foundation for Black students [C] [S2]. The body text is almost identical to the 2025 edition [C] [S12, S1], so past candidates\' reports are a fair guide.')
    o += box('unc', 'The application window opened at 09:00 on 5 October 2026 for 24 hours "subject to volume of applications" [C] [S1]. In the 2025 cycle it ran a week (7 to 13 October 2024) [R] [S12]. The window is shrinking, which points to rising volume [I]. Apply first, prepare second.')
    for i,(line, what, who, good, reveals) in enumerate(JD):
        o += f'<div class="avoid"><h3>D{i+1}. {md(line)}</h3>'
        o += table(['What it really means','Counterparties','What good looks like','What it reveals about the firm'], [[what, who, good, reveals]]) + '</div>'
    o += h2('p1b', 'The work: value chain, channels and a day')
    o += fig('The intern\'s value chain: from team need to outcome', fig_chain(), 'Illustrative [I], based on the JD [S1] and standard junior tasks in credit and private banking [S203].')
    o += fig('The two channels through which an intern\'s work is done', fig_channels(), 'Business lines from Investec results [S120, S121]; rules from FCA and PRA sources [S167, S168]; intern tasks illustrative [I].')
    o += fig('A worked day in the seat (a corporate lending team, week four)', fig_day(), 'Illustrative [I]. Office pattern of four days in, one remote is stated in other Investec postings [C] [S19, S277]; not stated in the internship posting.')
    o += fig('The life of a request through an intern', fig_request(), 'Illustrative [I].')
    o += h2('p1c', 'The full taxonomy of what interns do')
    o += table(['Activity','Format','Typical team'],[
      ['Company and sector research','One-page profile, slide','Any CIB team, Advisory'],['Spreading financial statements','Excel template','Credit, lending niches'],
      ['Comparable companies / precedent deals','Excel + slide','Advisory, ECM, broking'],['Credit paper sections','Word memo','Lending, Fund Solutions'],
      ['Client meeting packs','Slides, PDF','Private Bank, Corporate Banking'],['KYC and onboarding support','Checklists, systems','Private Bank, Operations'],
      ['Market and rate monitoring','Daily note','Treasury, Treasury Risk Solutions'],['Data clean-up and dashboards','Excel, BI tools','Central functions'],
      ['Process improvement idea','Short proposal','Any (this is the "entrepreneurial thinker" test)'],['End-of-internship presentation','Slides, 10 minutes','Programme-wide (Inferred)']])
    o += P('<span class="small">All rows [I], built from the JD [S1], live postings [S269, S274, S277] and standard junior tasks [S203]. The end-of-internship presentation is common across banks but not stated in the posting.</span>')
    o += h2('p1d', 'What the team judges, the control dimension, and the path')
    o += UL('**Judged on:** accuracy, reliability (do what you said, by when you said), judgement about when to ask, attitude with the whole team, and one piece of work people remember [I].',
            '**Bright lines** that bind even an intern: confidentiality of client information (UK GDPR; the bank\'s own policies); inside information about listed companies (UK Market Abuse Regulation); anti-money-laundering rules (KYC); the FCA Consumer Duty for retail clients; personal account dealing rules (you may need to get approval before trading shares) [I] [S167, S168].',
            '**Say unprompted:** "I know I may see confidential or inside information. I would never discuss a client outside the team, and if unsure whether something is inside information I would ask compliance before doing anything."',
            '**Career path:** the UK rotational graduate programme is reported paused while early careers is redesigned. Interns have returned into specific entry-level roles, for example a 2022 intern who came back as a Fund Solutions analyst [R] [S8, S9, S24]. So the realistic path is: internship, then a return offer into a named team if one has a vacancy, then analyst, associate [I].')
    o += h2('p1e', 'The team, mapped')
    o += P('Investec publishes no org chart for early careers. This reconstruction uses the posting, the careers site and public profiles. Colour shows confidence.')
    o += fig('Reconstructed early-careers structure and host teams', fig_orgchart(), 'Sources: S1, S4, S7 (Investec, Confirmed/Reported); S45-S48 (profiles, Reported); S290, S291 (P&O leaders, search snippets only, Reported). Names are public professional information; identity and currency flagged where uncertain.')
    o += table(['Business area','Evidence it exists in the UK Specialist Bank','Evidence it hosts interns','Confidence'],[
      ['Fund Solutions (fund finance)','Investec team pages; Credit Hub posting supports "the wider Fund Solutions franchise" [S22, S274]','A 2022 intern returned as a Fund Solutions analyst [S24]','Reported'],
      ['Corporate Banking (mid-market)','8 live roles; new Corporate Bank launching 2026 [S3, S268]','None found','Inferred'],
      ['Lending niches: Direct Lending, Real Estate, Aviation, Energy & Infrastructure, Asset Finance','Investec sector pages; Aviation credit roles [S20, S22]','None found','Inferred'],
      ['Advisory, ECM, corporate broking','About 110 listed clients; Extel #1 SMID broker 2026 [S129, S130]','None found','Inferred'],
      ['Private Bank','4 live roles; 8,200 UK clients [S3, S124]','None found','Inferred'],
      ['Treasury and Bank Funding Group','Dealer and funding roles live [S21, S272]','None found','Inferred'],
      ['Central functions','Business Enablement 19 open roles by site category [S3]','Springpod module on Technology in Banking [S16]','Inferred']])
    o += P('**Headcount estimate for "the team".** There is no single intern team. The relevant numbers: Investec Bank plc employs 2,425 people [C] [S278]; the summer cohort size is not published [S131]. Method tried [I]: no public count of host teams or past cohorts exists, so any number would be invented. The honest answer is "a small cohort inside a 2,400-person bank". Ask at the HR interview how many interns there will be.',
           '**Do the interviewers sit on the team?** Round one (HR interview) is with early careers, reported as two people for about 30 minutes. Round two is with one or two people from the team you are matched to, sometimes including an analyst [R] [S41]. So the second interviewer may be your future manager.',
           '**Benchmark.** Close Brothers runs six-week placements with upReach for students from lower socio-economic backgrounds [R] [S141]. No peer publishes cohort sizes [S131].')
    o += END
    return o
