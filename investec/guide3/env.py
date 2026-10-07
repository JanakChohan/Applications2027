import sys, importlib.util
sys.path.insert(0, '/home/user/Applications2027/investec/build')
from lib import *
import lib

SRC = {
 1:('Investec careers','Private Client Relationship Manager (13796)','live Oct 2026','https://careers.investec.co.uk/jobs/vacancy/private-client-relationship-manager-13796-london---30-gresham-street/13814/description/'),
 2:('Investec careers','Corporate Banking Relationship Director (13005)','live Oct 2026','https://careers.investec.co.uk/jobs/vacancy/corporate-banking---relationship-director--13005-london---30-gresham-street/13023/description/'),
 3:('Investec careers','Corporate Deposit Dealer (13961)','live Oct 2026','https://careers.investec.co.uk/jobs/vacancy/corporate-deposit-dealer-13961-london---30-gresham-street/13979/description/'),
 4:('Investec careers','Treasury Origination (12390), Reading','live Oct 2026','https://careers.investec.co.uk/jobs/vacancy/x/12408/description/'),
 5:('Investec careers','U.S. Sales Trader (13711)','live Oct 2026','https://careers.investec.co.uk/jobs/vacancy/x/13729/description/'),
 6:('Investec careers','New Business & Risk Officer (14064), Guernsey','live Oct 2026','https://careers.investec.co.uk/jobs/vacancy/x/14082/description/'),
 7:('Investec careers','Proposition Lead, Digital Channels (13807)','live Oct 2026','https://careers.investec.co.uk/jobs/vacancy/x/13825/description/'),
 8:('Investec careers','Head of Wealth UK & CI (13965)','live Oct 2026','https://careers.investec.co.uk/jobs/vacancy/x/13983/description/'),
 9:('Job aggregator copy','Private Client FX Dealer (13791)','2026','https://huntukvisasponsors.com/job/private-client-fx-dealer-at-investec-obvpsursbi3l'),
 10:('Mortgage Solutions','Investec hires Oades as relationship manager (city professionals team)','7 Apr 2026','https://www.mortgagesolutions.co.uk/news/2026/04/07/exclusive-investec-hires-oades-as-relationship-manager/'),
 11:('MPA','Investec strengthens London-based mortgage intermediary line-up','Jun 2022','https://mpamag.com/uk/news/general/investec-strengthens-london-based-mortgage-intermediary-line-up/411141'),
 12:('BYP Network','A day in the life of Channon Alley-Gulley, a private banker at Investec','undated','https://www.byp.network/pages/107758-inside-the-world-of-banking-a-day-in-the-life-of-channon-alley-gulley-a-private-banker-at-investec'),
 13:('Spear\'s','Investec Private Bank (Ryan Tholet interview)','16 Aug 2019','https://www.spearswms.com/investec-private-bank-spears/'),
 14:('Glassdoor UK (search summary)','Investec Private Banker reviews','2026','https://www.glassdoor.co.uk/Reviews/Investec-Private-Banker-Reviews-EI_IE7373.0,8_KO9,23.htm'),
 15:('Glassdoor UK (search summary)','Investec London reviews','2026','https://www.glassdoor.co.uk/Reviews/Investec-London-Reviews-EI_IE7373.0,8_IL.9,15_IM1035.htm'),
 16:('Mergers & Inquisitions','Commercial Banking vs Investment Banking','23 Jul 2025','https://mergersandinquisitions.com/commercial-banking-vs-investment-banking/'),
 17:('eFinancialCareers','Wealth management jobs: graduate guide','2015','https://www.efinancialcareers.com/news/graduate-guide/wealth-management-jobs'),
 18:('eFinancialCareers','Day in the life: equities research and sales','n.d.','https://www.efinancialcareers.co.uk/news/day-in-the-life-research-equities'),
 19:('City AM','Investec eyes City hiring spree in major move into UK private banking','21 May 2026','https://www.cityam.com/investec-eyes-city-hiring-spree-in-major-move-into-uk-private-banking/'),
 20:('Investec case study (search extract)','A £7.65m mortgage in 12 business days','undated','https://www.investec.com/en_gb/focus/intermediary-mortgages/case-study-a-7-65m-mortgage-in-12-business-days.html'),
 21:('Investec','Pillar 3 disclosure report, March 2024','2024','https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2024/Investec-plc-group-and-Investec-Bank-plc-Pillar-3-disclosure-report-March-2024.pdf'),
 22:('Investec careers','Summer Internship 2027 (14049)','live Oct 2026','https://careers.investec.co.uk/jobs/vacancy/summer-internship-2027-14049-london---30-gresham-street/14067/description/'),
 23:('Bdaily','Investec strengthens corporate banking team','12 Jul 2026','https://bdaily.co.uk/articles/2026/07/12/investec-strengthens-corporate-banking-team'),
 24:('Investec Bank plc (Companies House)','Annual financial statements 2026','2026','https://find-and-update.company-information.service.gov.uk/company/00489604/filing-history/MzUzMDk3ODM1OWFkaXF6a2N4/document?format=pdf&download=0'),
}
def S(*n): return '[' + ', '.join(f'S{i}' for i in n) + ']'

def fig_map():
    b = text(360, 18, 'Client-facing seats in Investec UK, and who sits behind them', 12.5, NAVY, 'middle', 'bold')
    cols = [('PRIVATE CLIENT (the person)', 8, TEAL, TEALS, [('Private Client RMs','Own a book of HNW clients; teams by segment, e.g. "city professionals", hedge fund and PE clients [S1, S10, S12]'),
             ('Private Client FX Dealer','Prices currency for private clients; measured on margin, retention, volumes [S9]'),
             ('Wealth (with Rathbones)','Wealth managers and planners, "one client, one Investec" [S8]'),
             ('Intermediary BDMs','Win mortgage business through brokers; has associate and apprentice levels [S11]')]),
            ('CORPORATE (the business)', 245, ACC, ACCS, [('Relationship Director + Associate RM','RD owns ~£10m-£250m turnover clients; Associate supports 1-2 RDs [S2]'),
             ('Corporate Deposit Dealers','~800 corporate clients; "relationship-led" cash management [S3]'),
             ('Treasury Origination (Reading)','Most junior seat: calls, qualifies leads, books meetings for specialists [S4]'),
             ('Digital channels / proposition','Makes digital tools a "key differentiator" alongside RMs [S7]')]),
            ('MARKETS (the investor)', 482, SIG, SIGS, [('Equity sales and sales trading','Fund managers as clients; roadshows and investor events [S5]'),
             ('Corporate broking','Listed-company relationships (#1 UK SMID broker)'),
             ('Treasury Risk Solutions','Hedging sales; current sales roles posted in Dublin [I]'),
             ('','')])]
    for t,x,c,f,items in cols:
        b += rect(x, 32, 230, 26, c, c, 5) + text(x+115, 50, t, 10.5, '#fff', 'middle', 'bold')
        for i,(h,d) in enumerate(items):
            if not h: continue
            y = 66 + i*66
            b += node(x, y, 230, 58, h, d, fill=f, stroke=c, size=10, subsize=8.4)
    b += rect(8, 336, 704, 54, SOFT, NAVY2, 6) + text(360, 354, 'BEHIND THEM: credit committees (unanimous) · onboarding / New Business & Risk · client service centre (Sandton, extended hours) · KYC hub (Mumbai)', 9.4, NAVY, 'middle', 'bold')
    b += text(360, 374, 'London client-facing seats are mainly bankers, dealers and sales; much service and KYC work sits in offshore hubs [Inferred from posting locations]', 8.8, MUT, 'middle')
    return svg(720, 396, b)

def fig_flow():
    st = [('Client need','e.g. founder wants a £5m mortgage before bonus lands'),('RM owns it','Gathers the story, the documents and source of wealth'),
          ('Specialists','Credit, FX, wealth, lending desks pulled in by the RM'),('Credit committee','Independent voters; decision needs unanimous consent [S21]'),
          ('Onboarding / KYC','New Business & Risk checks; RM still owns high-risk take-on [S6]'),('Drawdown + service','Money out fast; service centre and RM keep it running')]
    b = ''
    for i,(t,d) in enumerate(st):
        col = i % 3; row = i // 3
        x = 8 + col*238; y = 10 + row*112
        b += node(x, y, 220, 92, t, d, fill=[TEALS,ACCS][row], stroke=[TEAL,ACC][row], size=11.5, subw=40)
        if col < 2: b += arrow(x+221, y+46, x+237, y+46)
    b += path('M705,56 L714,56 L714,108 L118,108 L118,120', MUT)
    b += text(360, 242, 'Real benchmark: £7.65m mortgage drawn 12 working days after first enquiry [S20]. The junior\'s job is to make this chain move without errors.', 9.6, NAVY2, 'middle', 'bold', width=120)
    return svg(720, 256, b)

def fig_day():
    rows = [('08:00','In the office (4 days a week is policy [S1, S3]). Inbox, desk inbox, overnight client emails'),('08:45','Team huddle: pipeline, who needs what today'),
            ('09:30','Chase documents for a new client\'s onboarding: proof of wealth, ID, company structure'),('11:00','Draft the summary for a credit paper: income, assets, why lend, what could go wrong'),
            ('12:30','Prepare a client meeting pack for the RM: holdings, recent activity, three ideas to raise'),('14:00','Sit in on the client meeting; take the action list'),
            ('15:30','Update the CRM; log what the client said and next steps (Consumer Duty record)'),('16:30','Answer client requests fast: "three rings" standard [S19]'),
            ('18:00','Leave most days; some evenings for client events [Inferred]')]
    b = ''
    for i,(t,d) in enumerate(rows):
        y = 6 + i*27
        b += rect(8, y, 64, 22, NAVY, NAVY, 4) + text(40, y+15, t, 10, '#fff', 'middle', 'bold')
        b += rect(78, y, 634, 22, SOFT if i%2 else '#fff', LINE, 4) + text(88, y+15, d, 9.6, NAVY)
    return svg(720, 252, b)

def fig_pillars():
    p = [('1','A small book I know deeply','Few clients, complex lives; one named banker [S1, S2]',TEAL,TEALS),
         ('2','Close to the people who decide','Flat: specialists and credit next door, seniors visible [S2, S22]',ACC,ACCS),
         ('3','Measured on the client, not the call count','Wallet share, retention, portfolio quality, Consumer Duty [S1, S2, S3]',GRN,GRNS),
         ('4','A speed standard','Three rings; 12-day £7.65m mortgage [S19, S20]',SIG,SIGS)]
    b = rect(8, 6, 704, 34, NAVY, NAVY, 6) + text(360, 28, 'MY IDEAL ENVIRONMENT = HOW INVESTEC\'S CLIENT TEAMS ACTUALLY WORK', 11.5, '#fff', 'middle', 'bold')
    for i,(n,t,d,c,f) in enumerate(p):
        x = 8 + i*178
        b += rect(x, 52, 170, 150, f, c, 6, 1.6) + f'<circle cx="{x+24}" cy="{76}" r="14" fill="{c}"/>' + text(x+24, 81, n, 13, '#fff', 'middle', 'bold')
        b += text(x+44, 74, t, 10.6, NAVY, 'start', 'bold', width=19, lh=12) + text(x+12, 132, d, 9.2, NAVY2, width=29, lh=11)
    return svg(720, 210, b)

def build():
    lib.FIGS.clear()
    o = part('p0', 'Start here', 'Your answer, first', 'The recordable script, then the evidence behind every line.')
    o += box('note', 'This pack is for the prompt "What is your ideal work environment?" (and its cousins: "What kind of team do you want to work in?", "Why this division?"). It targets client-facing work in Investec UK: relationship management, sales, onboarding and client servicing. The same material answers "why Investec" too.', 'Use')
    o += box('say', '"Thanks for watching. My ideal environment has four features, and they are the reason I am applying to Investec\'s client side: a small book of complex clients I can really know; being close to the people who decide, so credit and specialists sit next to the banker; being measured on what happens to the client, not on call counts; and a hard speed standard. To start with the first..."', 'The 15-second content section')
    o += fig('Four pillars, each tied to how Investec works', fig_pillars(), 'Sources as marked; pillar framing is the author\'s [I].')
    o += h2('p0a', 'The full script (about 110 seconds)')
    o += box('say', '"Thanks for taking the time to watch. My ideal environment has four features, and they are exactly why I am applying to Investec\'s client side.<br><br>'
             '<b>First, a small book of complex clients I can really know.</b> Investec\'s private bankers serve people like hedge fund and private equity partners, whose pay comes as bonuses, carried interest and shares. That is a different job from processing applications: you have to understand someone\'s whole financial life before you can help. [YOUR EXAMPLE: one sentence on a time you dealt with one person or customer in depth, e.g. a part-time job, a society role, tutoring.]<br><br>'
             '<b>Second, being close to the people who decide.</b> I want to sit where the banker, credit and the specialist desks talk every day. At Investec the relationship manager pulls in lending, FX and wealth teams, and a loan needs every independent voter on the credit committee to agree. I learn faster when I can see how a decision is argued, not just the result.<br><br>'
             '<b>Third, being measured on the client.</b> Investec\'s own job adverts judge bankers on wallet share, retention and portfolio quality, and corporate bankers even on "the stories clients tell". I would rather be judged on whether a client stays and brings more business than on how many calls I made.<br><br>'
             '<b>And fourth, a speed standard.</b> Investec talks about answering within three rings, and published a case of a £7.65 million mortgage drawn in twelve working days. I like environments where the bar is that concrete.<br><br>'
             'So the short version: small book, close to the decision, judged on the client, and fast. That is the client side of Investec."', 'Record this')
    o += P('<span class="small">About 290 words at normal pace: roughly 110 seconds. Fill the bracket with something true; if you have no example, cut the bracket and the script still runs at about 95 seconds.</span>')
    o += END

    o += part('p1', 'Part 1', 'The hidden test, translated for the client side', 'Your four rules were written for investment-banking deal teams. Here is what each means for relationship and client roles.')
    o += table(['What reviewers test','Deal-team version (what you pasted)','Client-facing version (use this)'],[
      ['Cultural realism','Long hours, deal pressure','Targets, responsiveness, compliance and accuracy. Typical relationship hours are ~40-55/week, not 80+ [R] ' + S(16) + '. Pressure is a client who wants an answer today, and KYC that must be right'],
      ['Divisional alignment','Lean deal team, direct MD access','A named banker per client, an Associate RM supporting 1-2 Relationship Directors [R] ' + S(2) + ', specialists and credit next door, a flat structure [C] ' + S(2)],
      ['15-second attention','Lead with technical confidence','Lead with the four pillars and one hard fact (three rings, 12 days, wallet share)'],
      ['Implicit skill','Models, balance sheets to the penny','Onboarding packs right first time, a clean credit summary, a CRM note that a regulator could read, a client email answered the same day']])
    o += box('dont', '"I thrive in fast-paced, 100-hour-week environments." It is false for these seats and tells the reviewer you have not looked. Also cut: "friendly culture", "work-life balance", "great values", "I\'m a people person".', 'Kill these lines')
    o += END

    o += part('p2', 'Part 2', 'The client-facing teams, mapped', 'Built mostly from Investec\'s own live job adverts, read on 5 to 7 October 2026.')
    o += fig('Where the client-facing seats are', fig_map(), 'Sources: live Investec postings S1-S8 (Confirmed); S9-S12 (Reported). Offshore service and KYC: titles and locations of postings (Inferred role content).', full=False)
    o += h2('p2a', 'Private Client: the relationship manager seat')
    o += UL('Manages "a portfolio of high-net-worth clients" with "client engagement plans" and a CRM pipeline [C] ' + S(1) + '.',
            'Must "increase wallet share and work with specialist teams across lending, foreign exchange, investments and wealth management" [C] ' + S(1) + '.',
            'Measured on "growth, engagement and commercial performance objectives", within the Consumer Duty (the FCA rule that firms must deliver good outcomes for retail clients) [C] ' + S(1) + '.',
            'Teams are organised by client type. In April 2026 a new hire joined the "city professionals team" [R] ' + S(10) + '; an Investec private banker describes a book of clients "who work in the hedge fund and private equity industry" [R] ' + S(12) + '.',
            'Mortgages also come through brokers: a separate intermediary business development team has business development managers at associate and apprentice level, one promoted from lending operations [R] ' + S(11) + '.')
    o += h2('p2b', 'Corporate Banking: the Relationship Director and Associate RM')
    o += UL('Relationship Directors are judged on "new-to-bank growth, revenue, product penetration and portfolio quality", and on "the stories clients tell" [C] ' + S(2) + '.',
            'They mentor Associate RMs, need "credibility with specialist desks and credit partners", and coordinate "service, risk, operations and technology" [C] ' + S(2) + '.',
            'They partner "with Private Client teams when personal and business needs intersect" [C] ' + S(2) + '. The posting still says "We combine a flat structure with a focus on internal mobility" [C] ' + S(2) + '.',
            'Associate RMs support 1-2 Relationship Directors on clients with roughly £10m-£250m turnover [R] ' + S(2) + '. Head of Corporate Banking Andy Hart: "corporate banking that feels like private banking" [R] ' + S(23) + '.')
    o += h2('p2c', 'Sales and dealing seats')
    o += UL('**Corporate Deposit Dealer:** a team serving "approximately 800 corporate and institutional clients" with "a personal, relationship-led approach". KPIs: "cost of funds, book granularity, client referrals and increased share of clients\' cash balances". Day to day: "Respond quickly and professionally to calls and emails", "Manage the desk inbox", "Originate and support the onboarding of new-to-bank business". FCA-certified role [C] ' + S(3) + '.',
            '**Treasury Origination (Reading):** the most sales-floor seat. "Outbound direct calling", qualifying leads and booking appointments for specialists; KPIs on "daily calls, leads qualified and appointments generated". Its brief: "Sell the reason for someone to deal with Investec" [C] ' + S(4) + '.',
            '**Equity sales trading:** measured on "Growth in commission revenues and wallet share", "client retention", and "exceptional client service and execution outcomes"; supports roadshows and investor events [C] ' + S(5) + '. Equity sales generally starts around 6:00-6:30am [R] ' + S(18) + '.')
    o += h2('p2d', 'Onboarding and service: who does what')
    o += P('Onboarding is a partnership with tension built in. In Investec\'s Guernsey bank: "The initial business take on of high risk and PEP business remains the responsibility of the RM", while the New Business & Risk team checks the file and must be "Challenging yet non-confrontational" [C] ' + S(6) + '. (A PEP is a politically exposed person, who needs extra checks.) Many UK service and KYC roles sit in Investec\'s Sandton and Mumbai hubs, so in London the client-facing seats are mostly bankers, dealers and sales [I, from posting locations].')
    o += fig('The life of a client request', fig_flow(), 'Process synthesised [I] from S1, S2, S6, S21; benchmark S20 (search extract).')
    o += END

    o += part('p3', 'Part 3', 'What it will actually be like', 'The honest version, from reviews, career guides and the postings.')
    o += h2('p3a', 'A realistic day for a junior on a private client team')
    o += fig('A day supporting a relationship manager', fig_day(), 'Illustrative [I], built from S1, S3, S12, S17, S19. Hours are an estimate; no Investec source states them.')
    o += h2('p3b', 'The real trade-offs')
    o += table(['Good','Hard'],[
      ['People and culture rated well: London culture and values 4.3/5 [R] ' + S(15),'"High targets and low pay" is a common private-banker complaint; private bankers rate the firm ~4.1/5 [R] ' + S(14)],
      ['Hours far below investment banking: ~40-55/week in relationship roles [R] ' + S(16),'Four days a week in the office, "very minimal flexibility" [R] ' + S(15) + '; "being together enables us to live our values and support our clients" [C] ' + S(3)],
      ['Early client exposure on smaller relationships [R] ' + S(16),'Pay well below investment banking; slower promotion [R] ' + S(16) + '; careers sub-rating 3.7/5 [R] ' + S(15)],
      ['Real routes from operations into client roles: one Investec RM started in operations [R] ' + S(12) + '; an associate BDM came from lending operations [R] ' + S(11),'Compliance pressure: KYC, Consumer Duty records, FCA certification for some seats [C] ' + S(1, 3)],
      ['Pay system rewards long-term, risk-aware client work over volume [C] ' + S(21),'Commercial targets are real: wallet share, new-to-bank, revenue [C] ' + S(1, 2)]])
    o += box('unc', 'One Glassdoor snippet mentions "80+ hour weeks"; the role and country could not be checked, so treat it as an outlier. No source gives actual Investec hours or client numbers per banker. No first-hand UK intern write-up exists.')
    o += END

    o += part('p4', 'Part 4', 'Building your answer', 'How each pillar is grounded, plus alternate versions and delivery.')
    o += table(['Pillar','What you say','The evidence underneath','Reason type'],[
      ['1. A small book I know deeply','I want to understand a client\'s whole financial life','RM manages "a portfolio of high-net-worth clients" with engagement plans; segments like hedge fund and PE clients [S1, S12]','Task-specific + your anecdote'],
      ['2. Close to the people who decide','I learn fastest where banker, credit and specialists talk daily','RD needs "credibility with specialist desks and credit partners"; flat structure; unanimous credit committees [S2, S21]','Job-nature'],
      ['3. Measured on the client','Judge me on whether the client stays and grows','Wallet share, retention, portfolio quality, "the stories clients tell" [S1, S2, S3, S5]','Job-nature'],
      ['4. A speed standard','I like a concrete bar','"three rings" [S19]; 12-day £7.65m mortgage [S20]; dealers "respond quickly" [S3]','Anecdotal / firm-specific']])
    o += h2('p4a', 'Alternate version for corporate banking or sales')
    o += box('say', '"Thanks for watching. My ideal environment is a relationship-led desk with three features, and Investec\'s corporate bank is building exactly that: a defined book of mid-sized companies, a direct line between the banker and the specialist desks, and targets tied to the client rather than activity.<br><br>'
             'First, a defined book. Investec\'s deposit desk looks after about 800 corporate clients, and an Associate RM supports one or two Relationship Directors on companies of roughly ten to two hundred and fifty million of turnover. That is small enough to know the client\'s business properly.<br><br>'
             'Second, the line to specialists. The Relationship Director has to connect lending, treasury, cash management and advisory, and even partner with private bankers when the owner\'s personal and business needs meet. I want to be the person who makes those connections happen.<br><br>'
             'Third, client-based targets: share of the client\'s cash, referrals, retention. [YOUR EXAMPLE: a time you kept a customer or member coming back.] That is the scoreboard I would choose."', 'Corporate / sales version (about 95 seconds)')
    o += h2('p4b', 'Delivery')
    o += UL('Note cards under the webcam, three words per line: "small book / close to decision / judged on client / three rings".',
            'Smile on the "three rings" line; it is a light moment and shows you know a real detail.',
            'Suit, camera at eye level, light in front of you. Record 15 times before the real one.',
            'If asked the follow-up "what would you find hard?", answer honestly: targets and the compliance load, and how you would handle them (structure, checklists, asking early).')
    o += h2('p4c', 'Originality check')
    o += table(['Generic line (cut)','Investec-specific line (keep)'],[
      ['"A collaborative, supportive culture"','"Banker, credit and specialists talking every day, with unanimous credit committees"'],
      ['"Client-focused"','"Judged on wallet share, retention and the stories clients tell"'],
      ['"Fast-paced"','"Three rings; a £7.65m mortgage in twelve working days"'],
      ['"Room to grow"','"Routes from operations and onboarding into relationship roles"']])
    o += END

    o += part('p5', 'Back matter', 'Sources', 'Accessed 5 to 7 October 2026. [C] read in a primary document; [R] reported or search summary; [I] the author\'s reasoning.')
    o += '<table class="src"><thead><tr><th style="width:28px">ID</th><th>Outlet</th><th>Title</th><th>Date</th><th>URL</th></tr></thead><tbody>' + ''.join(
        f'<tr><td>S{n}</td><td>{esc(a)}</td><td>{esc(t)}</td><td>{esc(d)}</td><td style="word-break:break-all">{esc(u)}</td></tr>' for n,(a,t,d,u) in SRC.items()) + '</tbody></table>'
    o += END
    return o

def main():
    body = build().replace('—', ', ')
    spec = importlib.util.spec_from_file_location('b', '/home/user/Applications2027/investec/build/build.py'); B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
    cover = ('<div class="cover"><div class="k">HireVue prep</div><h1>Client-facing at Investec:<br>your ideal work environment</h1>'
             '<div class="sub">What the relationship, sales, onboarding and service teams actually do, how they are structured and measured, what the work is really like, and a recordable answer built from that evidence.</div>'
             '<div class="meta">Prepared 7 October 2026 for the Investec UK Summer Internship 2027.<br>Built mainly from Investec\'s own live job adverts, plus reviews and career guides labelled as such.</div></div>')
    css = open('/home/user/Applications2027/investec/build/style.css').read()
    page = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Client-Facing at Investec</title><style>{css}</style></head><body>'
            f'{cover}{B.toc(body)}{B.markers(body)}</body></html>')
    open('/home/user/Applications2027/investec/Investec_Client_Facing_Ideal_Environment.html','w',encoding='utf8').write(page)
    print('figs', len(lib.FIGS))
main()
