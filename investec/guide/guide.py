import sys, os, re
sys.path.insert(0, '/home/user/Applications2027/investec/build')
from lib import *
import lib

SRC = {
 1:('Investec plc RNS via Investegate','Final Results 31/03/2026','21 May 2026','https://www.investegate.co.uk/announcement/rns/investec--invp/final-results-31-03-2026/9578809'),
 2:('BusinessTech','The South African brothers who built a R100 billion banking empire','5 Feb 2025','https://businesstech.co.za/news/business/810414/the-south-african-brothers-who-built-a-r100-billion-banking-empire/'),
 3:('Investec','DLC Annual Report 2019, Vol 1','2019','https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2019/investec-dlc-vol-1-annual-report-2019.pdf'),
 4:('Investec','Corporate Profile 2021','2021','https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2021/Investec-Corporate-Profile-2021-Online.pdf'),
 5:('Investec Limited (via Botswana Stock Exchange)','Investec Limited Annual Report 2026','2026','https://apis.bse.co.bw/storage/disclosures/06/2026/6950.pdf'),
 6:('Investec','Investec plc group and Investec Bank plc Pillar 3 disclosure report, March 2024','2024','https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2024/Investec-plc-group-and-Investec-Bank-plc-Pillar-3-disclosure-report-March-2024.pdf'),
 7:('Investec (FCA National Storage Mechanism)','Group remuneration report 2024','2024','https://data.fca.org.uk/artefacts/NSM/Portal/NI-000099890/NI-000099890.pdf'),
 8:('Court of Appeal (National Archives)','Brogden & Reid v Investec Bank plc [2016] EWCA Civ 1031','2016','https://caselaw.nationalarchives.gov.uk/ewca/civ/2016/1031'),
 9:('Investec careers','Senior Reward Manager (13645)','live Oct 2026','https://careers.investec.co.uk/jobs/vacancy/senior-reward-manager-13645-london---30-gresham-street/13663/description/'),
 10:('Investec careers','Private Client Relationship Manager (13796)','live 2026','https://careers.investec.co.uk/jobs/vacancy/private-client-relationship-manager-13796/13814/description/'),
 11:('Investec careers','Corporate Banking Relationship Director (13005)','2026','https://careers.investec.co.uk/jobs/vacancy/corporate-banking-relationship-director-13005/13023/description/'),
 12:('Companies House','Investec Bank plc annual financial statements 2026','filed Jul 2026','https://find-and-update.company-information.service.gov.uk/company/00489604/filing-history/MzUzMDk3ODM1OWFkaXF6a2N4/document?format=pdf&download=0'),
 13:('Jersey Evening Post','The firm that places worth above wealth','8 Mar 2023','https://jerseyeveningpost.com/business/2023/03/08/the-firm-that-places-worth-above-wealth/'),
 14:('City AM','Investec eyes City hiring spree in major move into UK private banking','21 May 2026','https://www.cityam.com/investec-eyes-city-hiring-spree-in-major-move-into-uk-private-banking/'),
 15:('City AM','Investec looks to mid-market businesses in growth push','Nov 2025','https://www.cityam.com/investec-looks-to-mid-market-businesses-in-growth-push/'),
 16:('WealthBriefing','Investec updates private client growth strategy','26 May 2026','https://www.wealthbriefing.com/html/printarticle.php?id=207821'),
 17:('WealthBriefing','Targeting Restless Entrepreneurs: Investec\'s UK Private Bank','16 Oct 2018','https://www.wealthbriefing.com/html/article.php/Targeting-Restless-Entrepreneurs:-Investec\'s-UK-Private-Bank'),
 18:('Money Helpdesk (broker guide)','Investec mortgages','Dec 2025','https://www.moneyhelpdesk.com/mortgages/mortgage-lenders/investec/'),
 19:('Investec press release (search snippet)','Investec accelerates mid-market strategy','Nov 2025','https://www.investec.com/en_gb/welcome-to-investec/press/investec-accelerates-mid-market-strategy.html'),
 20:('Investec press release (search snippet)','Investec updates its private client growth strategy','May 2026','https://www.investec.com/en_gb/welcome-to-investec/press/investec-updates-its-private-client-growth-strategy.html'),
 21:('Extel','Investec retains the UK SMID crown','Jun 2026','https://www.extelinsights.com/results/uk-small-mid-cap-brokers/uk-small-mid-cap/2026/investec-retains-the-uk-smid-crown'),
 22:('Investec Save','Help','n.d.','https://savings.investec.com/help'),
 23:('Trustpilot UK','Investec reviews','fetched Oct 2026','https://uk.trustpilot.com/review/investec.com'),
 24:('Investec plc RNS via Investegate','Half-year Financial Report 30 Sep 2025','20 Nov 2025','https://www.investegate.co.uk/announcement/rns/investec--invp/half-year-financial-report-30-sep-2025/9245448'),
 25:('Investec plc RNS via Investegate','Pre-Close Trading Statement','18 Sep 2026','https://www.investegate.co.uk/announcement/rns/investec--invp/pre-close-trading-statement/9778512'),
 26:('Arbuthnot Latham','About Arbuthnot Latham','n.d.','https://www.arbuthnotlatham.co.uk/about-arbuthnot-latham'),
 27:('Arbuthnot Latham','Awards','2026','https://www.arbuthnotlatham.co.uk/about/awards'),
 28:('Close Brothers','Our business model','2025','https://www.closebrothers.com/sites/default/files/Digital%20download%20centre%202025/Our%20business%20model.pdf'),
 29:('C. Hoare & Co','Advisers','n.d.','https://www.hoaresbank.co.uk/advisers'),
 30:('HSBC UK Bank plc','Annual Report and Accounts 2025','25 Feb 2026','https://www.hsbc.com/-/files/hsbc/investors/hsbc-results/2025/annual/pdfs/hsbc-uk-bank-plc/260225-annual-report-and-accounts-2025.pdf'),
 31:('OakNorth','OakNorth 2025 annual results','17 Mar 2026','https://oaknorth.co.uk/press/oaknorth-2025-annual-results/'),
 32:('Shawbrook RNS via Investegate','Interim Report, period ended 30 June 2026','5 Aug 2026','https://www.investegate.co.uk/announcement/rns/shawbrook-group-plc--shaw/interim-report-for-the-period-ended-30-june-2026/9704867'),
 33:('Shawbrook RNS via Investegate','Full Year 2025 Results','12 Mar 2026','https://www.investegate.co.uk/announcement/rns/shawbrook-group-plc--shaw/shawbrook-full-year-2025-results/9470256'),
 34:('WealthBriefing','Wealth, group profits rise strongly at NatWest in 2025','13 Feb 2026','https://www.wealthbriefing.com/html/article.php/wealth,-group-profits-rise-strongly-at-natwest-in-2025'),
 35:('Barclays plc','FY2025 Results Announcement','Feb 2026','https://home.barclays/content/dam/home-barclays/documents/investor-relations/ResultAnnouncements/FullYear2025Results/FY25-BPLC-Results-RA.pdf'),
 36:('Close Brothers RNS via Investegate','Preliminary Results','29 Sep 2026','https://www.investegate.co.uk/announcement/rns/close-brothers-group--cbg/preliminary-results/9795269'),
 37:('Euromoney','Private banking awards national winners 2025: UK','2025','https://www.euromoney.com/article/2egwtz8oxplnnrfbl9wxt/awards/private-banking-awards/private-banking-awards-national-winners-2025-uk/'),
 38:('SA Jewish Report','Stephen Koseff conquers Investec\'s sub-prime woes','18 Feb 2014','https://www.sajr.co.za/stephen-koseff-conquers-investec-s-sub-prime-woes/'),
 39:('MarketScreener','Investec: Sale of Kensington Group','Sep 2014','https://www.marketscreener.com/quote/stock/INVESTEC-PLC-4006220/news/Investec-Sale-of-Kensington-Group-19014449/'),
 40:('Daily Maverick','Split decision: Investec\'s Ninety One unbundling defies the sceptics','10 Aug 2021','https://www.dailymaverick.co.za/article/2021-08-10-split-decision-investecs-ninety-one-unbundling-defies-the-sceptics/'),
 41:('European Business Magazine','Rathbones shares sink after FCA finds compliance failings','16 Jun 2026','https://europeanbusinessmagazine.com/rathbones-fca-review-shares-collapse/'),
 42:('Glassdoor UK (search summaries)','Investec reviews','n.d.','https://www.glassdoor.co.uk/Reviews/Investec-Reviews-E7373.htm'),
 43:('Financial Mail','Investec\'s five-year plan: smart humans on tap, not chatbots','20 Nov 2025','https://fm.co.za/2025-11-20-investec-s-five-year-plan-smart-humans-on-tap-not-chatbots/'),
 44:('Jewish News','The unique bank with a dazzling Jewish history','30 Mar 2017','https://www.jewishnews.co.uk/the-unique-bank-with-a-dazzling-jewish-history/'),
 45:('AJ Bell / Alliance News','Rathbones ends share buybacks as Investec stake hits 29.9%','13 Jul 2026','https://www.ajbell.co.uk/news/articles/brief-rathbones-ends-share-buybacks-investec-stake-hits-299'),
 46:('Rathbones RNS via Investegate','Completion of the Combination','21 Sep 2023','https://www.investegate.co.uk/announcement/rns/rathbones-group--rat/completion-of-the-combination/7769142'),
 47:('Private Banker International','Investec agrees to sell its Australian business to Bank of Queensland','Apr 2014','https://www.privatebankerinternational.com/news/investec-agrees-to-sell-its-australian-business-to-the-bank-of-queensland-4213793/'),
 48:('Bdaily','Investec strengthens corporate banking team','12 Jul 2026','https://bdaily.co.uk/articles/2026/07/12/investec-strengthens-corporate-banking-team'),
 49:('Investec (search snippet)','Fund Solutions','n.d.','https://www.investec.com/en_gb/corporate-finance/specialist-lending/fund-solutions.html'),
 50:('Investec (search snippet)','Corporate broking','n.d.','https://www.investec.com/en_gb/business/public-companies/investment-banking-and-equities/corporate-broking.html'),
}
def S(*n): return '[' + ', '.join(f'S{i}' for i in n) + ']'

# ---------------- figures ----------------
def fig_bank():
    b = rect(130, 15, 460, 210, '#fff', NAVY, 6, 2)
    b += node(150, 40, 130, 70, 'Savers', 'leave money with the bank', fill=TEALS, stroke=TEAL)
    b += node(440, 40, 130, 70, 'Borrowers', 'pay interest on loans', fill=ACCS, stroke=ACC)
    b += node(295, 40, 130, 70, 'THE BANK', fill=NAVY, stroke=NAVY, tc='#fff', size=13)
    b += arrow(282, 65, 293, 65) + arrow(427, 65, 438, 65)
    b += arrow(438, 90, 427, 90, accent=True) + arrow(293, 90, 282, 90, accent=True)
    b += text(360, 132, 'Pays savers 3%  ·  charges borrowers 6%', 11, NAVY, 'middle', 'bold')
    b += text(360, 150, 'The 3% gap is "net interest income"', 10.5, MUT, 'middle')
    b += node(150, 165, 200, 48, 'Plus fees', 'for advice, broking, hedging, payments', fill=GRNS, stroke=GRN, size=10.5)
    b += node(370, 165, 200, 48, 'Minus costs and bad loans', 'staff, systems, loans not repaid', fill=REDS, stroke=RED, size=10.5)
    b += text(360, 248, 'Illustrative rates only. What is left after costs and bad loans is profit.', 9, MUT, 'middle')
    return svg(720, 258, b)

def fig_dlc():
    b = node(220, 8, 280, 46, 'Investec Group: "a single unified economic enterprise"', fill=NAVY, stroke=NAVY, tc='#fff', size=10.5)
    b += node(40, 90, 260, 70, 'Investec plc', 'Listed in London. Owns the UK bank (Investec Bank plc) and the Rathbones stake', fill=ACCS, stroke=ACC)
    b += node(420, 90, 260, 70, 'Investec Limited', 'Listed in Johannesburg. Owns the South African bank and wealth business', fill=TEALS, stroke=TEAL)
    b += path('M300,54 L300,72 L170,72 L170,88', MUT) + path('M420,54 L420,72 L550,72 L550,88', MUT)
    b += f'<rect x="352" y="80" width="16" height="96" fill="{RED}"/>' + text(360, 196, 'No cross-guarantees; capital and liquidity cannot flow across', 9.5, RED, 'middle', 'bold')
    b += node(40, 214, 260, 50, 'UK must stand on its own feet', 'Own board, own capital, own risk committees', fill=SOFT, stroke=MUT, size=10)
    b += node(420, 214, 260, 50, 'One board, one strategy, one brand', 'Shareholders treated as one group', fill=SOFT, stroke=MUT, size=10)
    return svg(720, 272, b)

def fig_businesses():
    items = [('Private Bank','Mortgages, lending, savings; from 2026 current accounts and a card','~8,200 high-earning households',TEAL,TEALS),
             ('Mid-market corporate bank','Lending, hedging, payments, advice for companies','Firms with ~£10m to £250m turnover',ACC,ACCS),
             ('Specialist lending','Fund finance, aviation, real estate, energy and infrastructure','Funds and specialist borrowers',NAVY2,SOFT),
             ('Corporate broking and research','Stock-market adviser to listed companies','100+ listed companies; Extel #1 SMID',SIG,SIGS),
             ('Investec Save','Online savings accounts','Ordinary savers; no personal banker',MUT,'#fff'),
             ('Rathbones stake','41.25% of a separate wealth manager','Runs the money behind Investec advice',GRN,GRNS)]
    b = ''
    for i,(t,d,c,s,f) in enumerate(items):
        col = i % 3; row = i // 3
        x = 6 + col*238; y = 8 + row*128
        b += rect(x, y, 228, 118, f, s, 6, 1.6) + rect(x, y, 228, 26, s, s, 6)
        b += text(x+114, y+18, t, 11, '#fff', 'middle', 'bold')
        b += text(x+12, y+46, d, 9.6, NAVY, width=40, lh=12) + text(x+12, y+92, c, 9.2, MUT, width=42, lh=11, italic=True)
    return svg(720, 266, b)

def fig_values():
    eras = [('2019','Four values',['Client focus: "We break china for the client"','Cast-iron integrity','Distinctive performance','Dedicated partnership'],TEAL,TEALS),
            ('2021','Five values + purpose',['Adds Entrepreneurial spirit: "We are pioneers at heart"','Purpose: "create enduring worth, living in, not off, society"'],ACC,ACCS),
            ('2026','Ten "we" statements',['"Deep client partnerships... are the bedrock of our business"','"We trust our people to exercise their judgement..."','"living in society, not off it" now a value','Purpose: "create enduring worth"'],SIG,SIGS)]
    b = ''
    for i,(y,t,items,c,f) in enumerate(eras):
        x = 6 + i*238
        b += rect(x, 8, 228, 230, f, c, 6, 1.6)
        b += text(x+114, 34, y, 18, c, 'middle', 'bold') + text(x+114, 54, t, 10.5, NAVY, 'middle', 'bold')
        yy = 78
        for it in items:
            lines = wrap(it, 40)
            for k,l in enumerate(lines): b += text(x+12, yy+k*12, l, 9.3, NAVY)
            yy += len(lines)*12 + 10
        if i < 2: b += arrow(x+229, 120, x+237, 120)
    b += text(360, 258, 'Same ideas, new wording. Safe line: "four long-standing values, now written as ten statements."', 9.6, NAVY2, 'middle', 'bold')
    return svg(720, 266, b)

def fig_veto():
    b = node(10, 30, 210, 90, '1974: every founder has a veto', '"you can do anything you like as long as there is consensus" (Ian Kantor)', fill=ACCS, stroke=ACC, size=11)
    b += node(255, 30, 210, 90, 'Value today', '"open and honest dialogue to test decisions, seek consensus and accept responsibility"', fill=SIGS, stroke=SIG, size=11)
    b += node(500, 30, 210, 90, 'Credit committees today', '"All decisions to enter into a transaction are based on unanimous consent"', fill=TEALS, stroke=TEAL, size=11)
    b += arrow(222, 75, 253, 75, accent=True) + arrow(467, 75, 498, 75, accent=True)
    b += text(360, 150, 'One "no" can stop a decision: the founding habit survives in how loans are approved.', 10.5, NAVY, 'middle', 'bold')
    b += text(360, 168, 'Sources: S2 (Reported), S5 (Confirmed), S6 (Confirmed). Link between the three is the author\'s inference.', 8.6, MUT, 'middle')
    return svg(720, 178, b)

def fig_order():
    st = [('1. Choose','Pick a narrow client type: people building wealth; mid-sized firms','Not "all things to all people"'),
          ('2. One banker','A named relationship manager is the single door into the bank','Few clients per banker'),
          ('3. Earn trust','Fast, human lending decisions on complex incomes','No credit scorecard'),
          ('4. Grow','Add accounts, FX, hedging, advice, business banking','"Increase wallet share"')]
    b = ''
    for i,(t,d,k) in enumerate(st):
        x = 6 + i*180
        b += f'<path d="M{x},20 L{x+160},20 L{x+174},80 L{x+160},140 L{x},140 L{x+14},80 Z" fill="{[TEALS,ACCS,GRNS,SIGS][i]}" stroke="{[TEAL,ACC,GRN,SIG][i]}" stroke-width="1.5"/>'
        b += text(x+87, 46, t, 12.5, NAVY, 'middle', 'bold') + text(x+87, 66, d, 9.2, NAVY, 'middle', width=27, lh=11)
        b += text(x+87, 168, k, 9.6, [TEAL,ACC,GRN,SIG][i], 'middle', 'bold')
    b += text(360, 196, 'Relationship first, revenue second. Investec does sell, but in this order.', 11, NAVY, 'middle', 'bold')
    return svg(720, 206, b)

def fig_founder():
    b = ''
    for x,y in [(220,50),(500,50),(220,220),(500,220)]:
        b += f'<line x1="{x}" y1="{y}" x2="360" y2="132" stroke="{ACC}" stroke-width="1.8"/>'
    b += node(270, 100, 180, 64, 'Relationship managers', 'corporate + private, partnering', fill=NAVY, stroke=NAVY, tc='#fff', size=11)
    b += node(20, 20, 200, 60, 'The company', '£10m-£250m turnover; needs loans, payments, hedging', fill=ACCS, stroke=ACC, size=11)
    b += node(500, 20, 200, 60, 'The founder', 'High earner; needs mortgage, accounts, investments', fill=TEALS, stroke=TEAL, size=11)
    b += node(20, 190, 200, 60, 'Broking and ECM', 'If the company lists or raises equity', fill=SIGS, stroke=SIG, size=11)
    b += node(500, 190, 200, 60, 'Rathbones (behind Investec)', 'Runs the founder\'s investments', fill=GRNS, stroke=GRN, size=11)
    b += text(360, 280, '"partnering with Private Client teams when personal and business needs intersect" (job advert, S11)', 9.6, NAVY2, 'middle', 'bold')
    return svg(720, 290, b)

def fig_intensity():
    pts = [('Investec Save',0.05,'Rate-led, online, no banker'),('Specialist lending',0.45,'Sector experts; repeat borrowers (not measured)'),
           ('Mid-market corporate bank',0.7,'~25 clients per RM (inferred)'),('Private Bank',0.82,'Named banker; human credit decisions'),('Corporate broking',0.95,'Years-long adviser to listed firms')]
    b = f'<defs><linearGradient id="gr" x1="0" x2="1"><stop offset="0" stop-color="{SOFT}"/><stop offset="1" stop-color="{ACC}"/></linearGradient></defs>'
    b += f'<rect x="40" y="110" width="640" height="14" rx="7" fill="url(#gr)"/>'
    b += text(40, 145, 'Transactional (sold on price)', 9.5, MUT) + text(680, 145, 'Deep relationship (sold on trust)', 9.5, MUT, 'end')
    for i,(n,v,d) in enumerate(pts):
        x = 40 + v*640; up = i % 2 == 0
        b += f'<circle cx="{x:.0f}" cy="117" r="8" fill="{NAVY}"/>'
        y = 30 if up else 168
        b += f'<line x1="{x:.0f}" y1="{109 if up else 125}" x2="{x:.0f}" y2="{y+40 if up else y-8}" stroke="{LINE}"/>'
        b += text(x, y, n, 10.5, NAVY, 'middle', 'bold') + text(x, y+14, d, 8.8, MUT, 'middle', width=30, lh=10)
    return svg(720, 210, b)

def fig_eva():
    b = text(360, 20, 'Two teams, same revenue. Which one earns a bonus?', 12, NAVY, 'middle', 'bold')
    for i,(t,rev,cost,cap,c) in enumerate([('Team A: careful, repeat clients',10,5,3,GRN),('Team B: big risky deals',10,5,6,RED)]):
        x = 30 + i*350; base = 230; sc = 15
        b += text(x+150, 48, t, 11, c, 'middle', 'bold')
        bars = [('Revenue',rev,NAVY2),('Costs',-cost,MUT),('Capital charge',-cap,ACC)]
        run = 0
        for j,(l,v,col) in enumerate(bars):
            bx = x + j*75
            top = run + max(v,0); bot = run + min(v,0)
            y1 = base - top*sc; h = (top-bot)*sc
            b += f'<rect x="{bx}" y="{y1}" width="56" height="{h}" fill="{col}" rx="2"/>'
            b += text(bx+28, base+42, l, 8.6, MUT, 'middle') + text(bx+28, y1-5 if v>0 else y1+h+12, f'{"+" if v>0 else "−"}£{abs(v)}m', 9.5, NAVY, 'middle', 'bold')
            run += v
        eva = rev-cost-cap; bx = x + 225
        y1 = base - max(eva,0)*sc; h = abs(eva)*sc
        b += f'<rect x="{bx}" y="{y1 if eva>0 else base}" width="56" height="{max(h,2)}" fill="{c}" rx="2"/>'
        b += text(bx+28, base+42, 'EVA', 8.6, MUT, 'middle', 'bold') + text(bx+28, (y1-5) if eva>0 else base+h+12, f'£{eva}m' if eva>=0 else f'−£{abs(eva)}m', 10, c, 'middle', 'bold')
        b += f'<line x1="{x-5}" y1="{base}" x2="{x+290}" y2="{base}" stroke="{MUT}"/>'
        b += text(x+150, 298, 'Bonus pool grows' if eva>0 else 'Bonus pool: zero', 11.5, c, 'middle', 'bold')
    b += text(360, 320, 'Illustrative numbers. Real case: in Brogden v Investec (2016) a desk with negative EVA received no bonus [S8].', 9, MUT, 'middle')
    return svg(720, 326, b)

def fig_deferral():
    b = text(20, 22, 'A senior banker\'s bonus awarded in year 0', 11.5, NAVY, 'start', 'bold')
    x0, w = 60, 620; yr = lambda y: x0 + y*w/10
    b += f'<line x1="{x0}" y1="150" x2="{x0+w}" y2="150" stroke="{NAVY}" stroke-width="2"/>'
    for y in range(11): b += f'<line x1="{yr(y):.0f}" y1="145" x2="{yr(y):.0f}" y2="155" stroke="{NAVY}"/>' + text(yr(y), 172, f'Yr {y}', 9, MUT, 'middle')
    b += rect(yr(0), 50, yr(1)-yr(0), 30, GRN, GRN, 3) + text((yr(0)+yr(1))/2, 70, 'Part paid', 9, '#fff', 'middle', 'bold')
    b += rect(yr(1), 50, yr(7)-yr(1), 30, ACC, ACC, 3) + text((yr(1)+yr(7))/2, 70, 'Deferred: paid in instalments, much of it in shares (4-7 years for risk-takers)', 9.2, '#fff', 'middle', 'bold')
    b += rect(yr(0), 95, yr(7)-yr(0), 24, SIGS, SIG, 3) + text((yr(0)+yr(7))/2, 111, 'MALUS: unpaid bonus can be cancelled', 9.2, SIG, 'middle', 'bold')
    b += rect(yr(0), 190, yr(10)-yr(0), 24, REDS, RED, 3) + text((yr(0)+yr(10))/2, 206, 'CLAWBACK: paid bonus can be recovered (up to 10 years for executive directors)', 9.2, RED, 'middle', 'bold')
    b += text(360, 240, 'A loan that goes bad in year 3 can still cost the banker who wrote it.', 10.5, NAVY, 'middle', 'bold')
    return svg(720, 250, b)

def fig_levers():
    lev = [('EVA bonus pools','Profit after a capital charge'),('Bonus factors','Client outcomes, risk attitude'),('Deferral + clawback','Results that last years'),
           ('Staff share ownership','Long-run value of the firm'),('Unanimous credit committees','Loans sceptics accept'),('Hold loans to maturity','Live with every loan')]
    b = node(260, 105, 200, 80, 'Behaviour: long-term, risk-aware client relationships', fill=NAVY, stroke=NAVY, tc='#fff', size=11)
    import math
    for i,(t,d) in enumerate(lev):
        a = i/6*2*math.pi - math.pi/2
        x = 360 + 270*math.cos(a) - 95; y = 145 + 115*math.sin(a) - 24
        b += f'<line x1="360" y1="145" x2="{x+95:.0f}" y2="{y+24:.0f}" stroke="{ACC}" stroke-width="1.6"/>'
        b += node(x, y, 190, 48, t, d, fill=ACCS, stroke=ACC, size=10)
    b = b.replace(node(260, 105, 200, 80, 'Behaviour: long-term, risk-aware client relationships', fill=NAVY, stroke=NAVY, tc='#fff', size=11), '', 1)
    b += node(265, 115, 190, 60, 'Behaviour: long-term, risk-aware client work', fill=NAVY, stroke=NAVY, tc='#fff', size=10.5)
    return svg(720, 295, b)

def fig_bundle():
    firms = ['Investec','Close Brothers','Shawbrook','OakNorth','Arbuthnot','Coutts','C. Hoare','Peel Hunt','HSBC UK']
    caps = ['Private bank','Mid-market lending','Stock-market broking','Wealth via stake/partner','Mid-sized firm']
    grid = {'Investec':[1,1,1,1,1],'Close Brothers':[0,1,0,0,1],'Shawbrook':[0,1,0,0,1],'OakNorth':[0,1,0,0,1],'Arbuthnot':[1,1,0,0,1],
            'Coutts':[1,0,0,0,0],'C. Hoare':[1,0,0,0,1],'Peel Hunt':[0,0,1,0,1],'HSBC UK':[1,1,0,0,0]}
    b = ''
    for j,c in enumerate(caps): b += text(220+j*100, 30, c, 9.4, NAVY, 'middle', 'bold', width=16, lh=10)
    for i,f in enumerate(firms):
        y = 52 + i*28; inv = f=='Investec'
        if inv: b += rect(10, y-4, 700, 26, ACCS, ACC, 4)
        b += text(20, y+13, f, 10.5, ACC if inv else NAVY, 'start', 'bold' if inv else 'normal')
        for j,v in enumerate(grid[f]):
            cx = 220+j*100
            b += f'<circle cx="{cx}" cy="{y+9}" r="8" fill="{(ACC if inv else NAVY2) if v else "#fff"}" stroke="{LINE if not v else "none"}"/>'
    b += text(360, 318, 'Author\'s classification [I] from peer results and websites [S26-S36]. HSBC UK and Coutts are part of very large groups. "Mid-sized" = not a big-five ring-fenced bank group.', 8.8, MUT, 'middle', width=130)
    return svg(720, 340, b)

def fig_returns():
    items = [('Barclays private bank (RoTE, 2025)',26.3),('OakNorth (adj. ROE, 2025)',22.0),('Coutts / NatWest PB&WM (ROE, 2025)',21.7),('Shawbrook (underlying RoTE, 2025)',17.2),('Investec plc (RoTE, FY26)',13.7),('Investec plc (ROE, FY26)',10.8),('Close Brothers (RoTE, FY26)',5.5)]
    return hbar(items, label_w=250, unit='%', valfmt='{:.1f}', colors=[MUT,MUT,MUT,MUT,ACC,ACC,MUT])

def fig_cost():
    items = [('Investec UK specialist bank (FY26)',54.0),('Shawbrook (H1 2026)',36.4),('HSBC UK commercial (2025)',30.5),('OakNorth efficiency ratio (2025)',26.0)]
    return hbar(items, label_w=250, unit='%', valfmt='{:.1f}', colors=[ACC,MUT,MUT,MUT])

# ---------------- content ----------------
def build():
    lib.FIGS.clear()
    o = part('p0', 'Start here', 'The answer in one page', 'If you read nothing else, read this.')
    o += box('say', '"Investec chooses a narrow set of ambitious clients, serves the person and their business through one banker, and backs that with pay and credit rules that reward long-term, risk-aware client work. The open question is whether that model can lift UK returns to its targets by 2030."', 'The one-sentence answer')
    o += P('**Does Investec sell, or build relationships?** Both, in a set order. It picks its clients carefully, gives each one a named banker and fast, human lending decisions, and then grows its share of that client\'s business. Its own job adverts set revenue and "wallet share" targets for bankers [C] ' + S(10, 11) + '.',
           '**Is "relationship banking" what makes it different?** No. At least four UK rivals say almost the same thing [C/R] ' + S(26, 28, 29, 30) + '. What is rare is the **bundle**: a private bank, a mid-market corporate lender, the top-ranked small and mid-cap stockbroker and a large stake in wealth manager Rathbones, all inside one mid-sized firm [I].',
           '**Where does the ethos actually live?** In the plumbing. Bonuses come from profit after a charge for the capital used, not from sales volume. Big bonuses are paid years later in shares and can be taken back. Most staff own shares. One independent "no" stops a loan [C] ' + S(6, 7, 8) + '. Many banks say they build relationships. Investec pays for them [I].',
           '**What is the catch?** The model is expensive. The UK bank\'s costs are 54% of its income, against 26% to 36% at leaner rivals, and its UK returns trail Shawbrook, Coutts and Barclays\' private bank [C] ' + S(1, 31, 32, 33, 34, 35) + '.')
    o += table(['Five things that really stand out','Two things not to claim'],[
      ['1. The bundle: lend to a founder\'s company, broke its shares and bank the founder, in one firm','"Investec is unique because it does relationship banking"'],
      ['2. Private clients chosen for building wealth, not holding it','"Investec never sells" or "has no sales targets"'],
      ['3. Bonus pools from risk-adjusted profit (EVA), deferred and clawable',''],
      ['4. Unanimous credit committees, a habit dating back to the founders\' veto',''],
      ['5. A deliberate bet on "smart humans on tap, not chatbots"','']])
    o += P('<span class="small">How to read the tags: <span class="c cC">Confirmed</span> read in a primary document such as Investec\'s results, annual report or job advert. <span class="c cR">Reported</span> from the press, a third party or a search snippet. <span class="c cI">Inferred</span> the author\'s reasoning from the evidence. [S1] etc. resolve in the source list at the back.</span>')
    o += END

    o += part('p1', 'Part 1', 'Banking from zero', 'Five minutes of background so the rest makes sense.')
    o += h2('g1a', 'What a bank does')
    o += P('A bank takes in **deposits**, money that people and companies leave with it, and lends that money out at a higher interest rate. The gap between the interest it earns on loans and the interest it pays on deposits is **net interest income**. Banks also earn **fees** for advice, for helping companies raise money, for hedging and for payments. From that income they pay their staff and systems and cover loans that are never repaid. What is left is profit.')
    o += fig('How a bank makes money', fig_bank(), 'Illustrative rates [I]. Investec\'s real numbers are on the next pages.')
    o += h2('g1b', 'Four words you will meet')
    o += box('term', '<b>Private bank</b>: a bank for wealthy or high-earning individuals, offering tailored loans and a named banker rather than standard products.')
    o += box('term', '<b>Mid-market company</b>: an established business too big for small-business banking but too small for global investment banks. Investec\'s UK corporate bank targets roughly £10m to £250m of annual turnover [R] ' + S(11) + '.')
    o += box('term', '<b>Relationship manager (RM)</b>: the single named banker responsible for a client. The client calls one person, and the RM brings in specialists.')
    o += box('term', '<b>Corporate broker</b>: a listed company\'s ongoing stock-market adviser, which helps it raise money from investors and keeps it connected to fund managers.')
    o += END

    o += part('p2', 'Part 2', 'What Investec is, and how it is built', 'A South African start-up that became a two-part specialist bank.')
    o += h2('g2a', 'Where it came from')
    o += P('Investec started in Johannesburg in 1974 as a small leasing and finance company called "Investors, Technical and Executors" [R] ' + S(2) + '. Leasing means renting out equipment in return for regular payments. It got a banking licence around 1980 and came to the UK in 1992 [R] ' + S(2) + '. Sources list the founders differently, so the safe line is "a small group led by Ian Kantor, later joined by Bernard Kantor and Stephen Koseff".',
           'The logo is a zebra. Investec links it to its South African roots and to "restless spirits", people "dissatisfied with the status quo" [R] ' + S(44) + '.')
    o += h2('g2b', 'Two companies run as one, with a wall in the middle')
    o += P('Since July 2002 Investec has been a **dual-listed company (DLC)**: two separate companies, each listed on its own stock exchange, that agree by contract to act as one business [C] ' + S(1) + '. Investec plc (London) owns the UK bank. Investec Limited (Johannesburg) owns the South African bank. The group "operates as if it is a single unified economic enterprise", but there are "no cross-guarantees between the companies" [C] ' + S(3) + ', and "capital and liquidity are prohibited from flowing between the two entities" [C] ' + S(4) + '.')
    o += fig('The dual-listed structure', fig_dlc(), 'Sources: S1, S3, S4 (Confirmed). The UK bank is Investec Bank plc, 30 Gresham Street, London.')
    o += P('In plain English: the UK bank must stand on its own feet. It has its own board and its own risk and pay committees [C] ' + S(6) + '. It also measures risk with a simpler, more cautious method than the South African bank, so it holds more capital for every pound it lends. That is one reason UK returns trail South Africa [I].')
    o += h2('g2c', 'How the money is made')
    o += P('In the year to 31 March 2026 the group earned £2,281.4m of revenue. About 59% was net interest income and 41% was fees and other income; fees and commissions grew 14.7% to £506.0m. Adjusted operating profit was £951.0m and return on equity (profit per pound of shareholders\' money) was 13.6% [C] ' + S(1) + '. The UK specialist bank made £401.6m, down 2.1%, with £17.8bn of loans, £22.5bn of deposits and costs equal to 54.0% of income [C] ' + S(1) + '.')
    o += h2('g2d', 'The UK businesses')
    o += fig('Investec\'s UK businesses at a glance', fig_businesses(), 'Sources: S16 (private clients, Reported), S11 and S19 (corporate bank), S1 (specialist lending, Rathbones), S21 and S50 (broking), S22 (Save), S45 and S46 (Rathbones).')
    o += P('**Rathbones** needs a word. In September 2023 Investec swapped its UK wealth management business for shares in Rathbones, a listed wealth manager [C] ' + S(46) + '. Investec now owns 41.25% of the economic value, with votes capped at 29.9% [R] ' + S(45) + '. Rathbones contributed £76.6m to Investec\'s profit in FY26 [C] ' + S(1) + '.')
    o += END

    o += part('p3', 'Part 3', 'The ethos: what Investec says it stands for', 'Purpose, values, and the founders\' veto that still shapes how decisions are made.')
    o += h2('g3a', 'Purpose and values, in its own words')
    o += P('The purpose today is short: "Our purpose is to create enduring worth" [C] ' + S(5) + '. "Enduring worth" means value that lasts, rather than a quick profit. In 2021 the line was longer: "to create enduring worth, living in, not off, society" [C] ' + S(4) + '. That phrase now sits among the values. It means a bank should give something back to the communities its profits come from [C] ' + S(5) + '.',
           'The brand line is **"Out of the Ordinary"** [C] ' + S(4) + '.')
    o += fig('How the values have been worded over time', fig_values(), 'Sources: S3 (2019), S4 (2021), S5 (2026). All Confirmed from Investec\'s own reports.')
    o += P('The 2019 wording of Client focus is the most vivid: "We break china for the client, having the tenacity and confidence to challenge convention" [C] ' + S(3) + '. "Breaking china" means being willing to upset normal procedures to get the client the right result.')
    o += h2('g3b', 'Choosing not to be everything to everyone')
    o += box('say', '"We do not seek to be all things to all people. Our aim is to build well-defined, value-adding businesses focused on serving the needs of select market niches." Investec Limited Annual Report 2026 [S5], with almost identical words in 2019 [S3].', 'The key sentence')
    o += P('This is the bridge between the ethos and the business model. A **niche** is a small, specialised corner of a market. Investec deliberately serves a few client types deeply, rather than everyone a little [C] ' + S(5) + '.')
    o += h2('g3c', 'Where the culture came from: every founder had a veto')
    o += P('Ian Kantor: "Every one of the founders at the time had veto power and could use it on anything." And: "This thing of \'you can do anything you like as long as there is consensus\' became the basis of Investec\'s culture" [R] ' + S(2) + '. A **veto** is the right to block a decision on your own.')
    o += fig('From the founders\' veto to today\'s loan approvals', fig_veto(), 'Sources: S2, S5, S6.')
    o += h2('g3d', 'How the culture is meant to work day to day')
    o += P('Investec has called its culture its "strategic differentiator": "We have a flat structure and meritocratic approach and uphold an environment that encourages self-starters to drive their careers" [C] ' + S(3) + '. A **flat structure** has few layers of management. **Meritocratic** means people progress on results rather than seniority.',
           'The UK bank\'s 2026 accounts say the culture is "defined by material ownership, freedom to operate with accountability and open and honest dialogue" [C] ' + S(12) + '. Chief executive Fani Titi on the owner mindset: "as an owner, if you act like an owner and you walk into your home and there is something amiss you act immediately" [R] ' + S(13) + '.')
    o += h2('g3e', 'The social side follows the same logic')
    o += P('Investec says sustainability should be "an integral part of our business rather than a peripheral consideration", and reports seven years of carbon-neutral own operations and coal at 0.09% of loans [C] ' + S(5) + '. In London it has run **Beyond Business**, an incubator for social enterprises, with the Bromley by Bow Centre since 2011 [R]. In South Africa, Promaths supports maths and science pupils [C] ' + S(4) + '. Both back education and founders rather than simple charity, which mirrors the business itself [I].')
    o += box('dont', 'Do not quote "we do not do business at any cost", or Koseff lines such as "anyone can talk to anyone" or "cowboys on the hill". None could be verified in an original source.')
    o += END

    o += part('p4', 'Part 4', 'Do they sell, or build relationships?', 'Both, in a set order. Here is how the order shows up in each business.')
    o += P('Investec\'s job adverts are frank. A UK Private Client Relationship Manager must find "opportunities to increase wallet share across lending, FX, investments, wealth management" and is measured on "growth, engagement and commercial performance objectives" [C] ' + S(10) + '. **Wallet share** is the portion of a client\'s total banking that one bank captures. So yes, Investec sells. But Titi frames returns as "the consequence or perhaps the reward" of doing "right by our clients and do that long term" [R] ' + S(13) + '.')
    o += fig('Relationship first, revenue second', fig_order(), 'Author\'s synthesis [I] of S5, S10, S11, S17, S18.')
    o += h2('g4a', 'Private Bank: a human decides, and the banker becomes the hub')
    o += P('The UK Private Bank serves about **8,200 clients** and plans to add about 5,000 [R] ' + S(16) + ' (City AM reported a bigger target of 16,000 households [R] ' + S(14) + '; the sources conflict). Typical clients earn £300,000 or more or have net worth of £3m or more [R] ' + S(18) + '.',
           'The client choice is deliberate. Ryan Tholet, then head of the UK private bank, in 2018: "We are not always especially useful to high net worth individuals who are simply looking to preserve their wealth" [R] ' + S(17) + '. Investec targets people **building** wealth: executives, entrepreneurs, finance professionals.',
           'Decisions are made by people. A broker guide says Investec does "not use standard credit scorecards" and that "every application is assessed by a dedicated Private Banker who looks at your global wealth and future earning potential", counting bonuses, profit shares and trust income [R] ' + S(18) + '. A **credit scorecard** is the automated points system most high-street banks use to approve loans.',
           'In May 2026 Investec announced a move "from a specialist lender to a full-service primary bank", adding current accounts, its first UK credit card and rewards [R] ' + S(20) + '. Tholet: "Our shift from mortgage banker to relationship manager enables a greater offering at the source of any lending, increasing our relevance" [R] ' + S(14) + '. Titi set a standard: "if a client calls in, the phone should not ring for more than three rings" [R] ' + S(14) + '.')
    o += h2('g4b', 'Rathbones: from passing on referrals to owning the advice')
    o += P('Investec is "evolving our strategic partnership from a referral-based model to an integrated assets-under-advice model. Investec will now lead the client relationship and advice, with Rathbones providing underlying investment capabilities" [C] ' + S(1) + '. The client talks to Investec; Rathbones runs the money in the background. Investec keeps the relationship rather than handing it away [I].')
    o += h2('g4c', 'Mid-market corporate bank: "corporate banking that feels like private banking"')
    o += P('In November 2025 Investec said it would build "transactional banking, a dedicated team of relationship managers and intuitive digital platforms", aiming for **1,000 mid-market relationships by FY2030** with more than 40 relationship managers [R] ' + S(19, 48) + '. That is roughly 25 companies per banker, very few by high-street standards [I]. Head of corporate banking Andy Hart: the aim is to "bring a private client banking experience to UK mid-market corporates" [R] ' + S(15) + '.',
           'The Relationship Director advert asks for a "proactive, trusted advisor" who connects clients "to the full breadth of Investec\'s expertise" and partners "with Private Client teams when personal and business needs intersect". The same advert measures "new-to-bank growth, revenue, product penetration and portfolio quality" [C] ' + S(11) + '. Selling and loan quality sit side by side.')
    o += fig('The founder and the company: one bank on both sides', fig_founder(), 'Author\'s illustration [I] of S1, S11, S15. Investec publishes no figure for how many UK clients use more than one of its businesses.')
    o += h2('g4d', 'Specialist lending, broking and savings')
    o += UL('**Specialist lending.** Niche teams in fund finance, aviation, real estate, energy and infrastructure. Fund Solutions says "one size does not fit all" and stresses "long-term relationships built on trust" [R] ' + S(49) + '. No repeat-client figures are published, so this rests on Investec\'s own language [I].',
            '**Corporate broking.** Investec acts for "over 100 public companies" [R] ' + S(50) + ' and in June 2026 was ranked #1 UK small and mid-cap broker for the fourth year running, voted by 248 fund managers and analysts [C] ' + S(21) + '. Because investors cast the votes, the ranking measures Investec\'s relationships with the buyers of shares [I].',
            '**Investec Save: the exception.** Online savings sold on rate, directly and through platforms like Raisin, with no personal banker [R] ' + S(22) + '. Trustpilot: 4.7 out of 5 on 6,302 reviews, with praise for "no faff" and complaints of "no way to talk to anyone in person" [C, anecdote] ' + S(23) + '.')
    o += fig('How relationship-heavy each UK business is', fig_intensity(), 'Positions are the author\'s judgement [I] from the evidence above. Not a measured scale.')
    o += END

    o += part('p5', 'Part 5', 'The plumbing: how pay and rules make it stick', 'Values on a wall do not change behaviour. Pay and approval rules do.')
    o += h2('g5a', 'Bonuses come from risk-adjusted profit, not sales volume')
    o += P('Investec Bank plc funds bonus pools from **Economic Value Added (EVA)**: "the Bank-wide risk adjusted Economic Value Added (EVA) model which is, at a high level, based on revenue less risk adjusted costs, and overall affordability" [C] ' + S(6) + '. EVA is profit minus a charge for the capital tied up in earning it. A **bonus pool** is the total pot a team shares.',
           'It is literal. In Brogden & Reid v Investec Bank plc (2016), two bankers\' bonuses were set as a share of their desk\'s EVA. The desk made an EVA loss, so no bonus was paid, and the Court of Appeal backed the bank [C] ' + S(8) + '. The system is still live: a 2026 advert asks the reward manager to "co-ordinate the EVA bonus pool and Long-Term Share Awards" [C] ' + S(9) + '.')
    o += fig('Why EVA rewards careful, repeat business', fig_eva(), 'Illustrative numbers [I]. EVA method: S6 (Confirmed); court case: S8 (Confirmed).')
    o += P('Individual shares of the pot weigh "client outcomes", "attitude displayed towards risk consciousness", "treating customers fairly", "the ability to grow and develop markets and client relationships", "multi-year contribution" and "specific input from the risk and compliance functions" [C] ' + S(6) + '. No source says Investec "does not pay on sales". The evidence is the design, not a stated ban.')
    o += h2('g5b', 'Bonuses are paid late, in shares, and can be taken back')
    o += P('For most staff, 60% of a bonus above a set level is deferred, paid over about three years. For senior staff whose jobs can change the bank\'s risk, deferral runs four to seven years. "All variable remuneration is subject to clawback" [C] ' + S(6) + '. For executive directors, clawback can apply for up to 10 years [C] ' + S(7) + '.')
    o += box('term', '<b>Malus</b>: cancelling a bonus that has been awarded but not yet paid. <b>Clawback</b>: recovering a bonus already paid.')
    o += fig('Deferral, malus and clawback on one timeline', fig_deferral(), 'Sources: S6, S7 (Confirmed). Durations vary by role; shown for a senior risk-taker.')
    o += h2('g5c', 'Staff are owners, by design')
    o += P('"All employees are eligible for, and the majority receive, long-term share incentives", "designed to give our people a sense of ownership" [C] ' + S(7) + '. At 31 March 2026, staff share trusts held 8.0% and 5.8% of Investec Limited [C] ' + S(5) + '. The schemes exist "to promote an esprit de corps... by allowing all staff to share in the risks and rewards of the Group" [C] ' + S(5) + '. Some trust shares fund future awards, so they overstate what staff own today [I].')
    o += h2('g5d', 'Credit decisions need everyone to agree')
    o += P('"All credit committees include voting members who are independent of the originating business unit. All decisions to enter into a transaction are based on unanimous consent" [C] ' + S(6) + '. Investec lends to "clients we know and understand", assessing "character, integrity" and track record, and originates loans "mainly with the intent of holding these assets to maturity, thereby developing a \'hands-on\' and long-standing relationship" [C] ' + S(6) + '. **Holding to maturity** means keeping a loan until it is repaid rather than selling it on, so the banker lives with it for its whole life.')
    o += h2('g5e', 'Growth is chosen by return on capital')
    o += P('Investec manages to a return target, not a size target: "the upper end of our target range by FY2030" through "dynamic capital management" [C] ' + S(1) + '. History fits: it sold its Australian bank in 2014 [R] ' + S(47) + ', demerged its asset manager as Ninety One in 2020 [R] ' + S(40) + ', and swapped UK wealth for the Rathbones stake in 2023 [C] ' + S(46) + '. When a business cannot earn its capital, Investec exits or partners [I].')
    o += fig('Six levers, one behaviour', fig_levers(), 'Levers: S6, S7, S8, S5 (Confirmed). Effect on behaviour is the author\'s inference [I].')
    o += box('op', 'One tension: EVA is measured team by team, which can breed silos that work against "One Investec" cross-referral. Investec does list "the level of cooperation and collaboration fostered" as a pay factor [C] ' + S(6) + '. Ask in interview how collaboration is rewarded in practice.', 'Worth asking about')
    o += END

    o += part('p6', 'Part 6', 'What is genuinely different, and what is not', 'Rivals say "relationship" too, so the bundle is what differs.')
    o += h2('g6a', 'Many UK banks make the same promise')
    o += table(['Rival','What it says','Source'],[
      ['Arbuthnot Latham','"Relationships are at the heart of our approach"','S26 [C]'],
      ['Close Brothers','"deep expertise, consistent service, and long-term relationships" and "fast lending decisions"','S28 [R]'],
      ['C. Hoare & Co','Being small means "decisions can be made quickly"','S29 [R]'],
      ['HSBC UK','Referrals from its commercial bank to its private bank rose 8% in 2025','S30 [C]']])
    o += h2('g6b', 'What is genuinely rare')
    o += P('Investec calls itself "the only integrated and diversified mid-market focused specialist bank, providing the capabilities of global investment banks to the corporate mid-market" [C, its own claim] ' + S(24) + '. The fair version is narrower. Lenders like Close Brothers, Shawbrook and OakNorth do not offer stock-market advice. Brokers like Peel Hunt have no lending balance sheet. Private banks like Coutts and Hoare\'s have no investment bank. Investec can **lend to a founder\'s company, act as its stock-market broker and bank the founder personally**, in one mid-sized firm [I].')
    o += fig('The bundle: who offers what', fig_bundle(), 'Classification [I]; see caption note.')
    o += P('Three further differences hold up. It targets wealth **creators** [R] ' + S(17) + '. It has made an open bet on people over automation: Financial Mail summed up Titi\'s five-year plan as "smart humans on tap, not chatbots" [C, headline] ' + S(43) + '. And it came through 2008 without a state rescue, in Koseff\'s words: "Seven of the 10 big UK banks had to get a government bailout. We survived that crises without any help from anyone" [C that he said it; his own figure] ' + S(38) + '.')
    o += h2('g6c', 'Where Investec is ordinary or weaker')
    o += fig('Returns: Investec against rivals', fig_returns(), 'Sources: S1, S31, S33, S34, S35, S36 (Confirmed). Measures differ (ROE vs RoTE; adjusted vs underlying). Not like-for-like.')
    o += fig('Cost to income: the price of the high-touch model', fig_cost(), 'Sources: S1, S32, S30, S31 (Confirmed). OakNorth reports an "efficiency ratio"; definitions differ slightly. Lower is leaner.')
    o += UL('**UK momentum is soft.** FY27 is the "peak investment year", UK return on tangible equity is guided at 12.5% to 13.5% [C] ' + S(1) + ', and UK half-year profit is expected 2% to 6% lower [C] ' + S(25) + '.',
            '**Not the leader in private-banking service awards.** Arbuthnot Latham won WealthBriefing\'s Best UK Private Bank Overall and Client Service in 2025 and 2026 [C, self-reported] ' + S(27) + '; Euromoney\'s 2025 UK best private bank was Standard Chartered [C] ' + S(37) + '.',
            '**Entrepreneurial culture can overreach.** Investec bought UK subprime lender Kensington in 2007 for about £283m just before the crisis; the share price fell from about R104 to R27 by 2009 [C] ' + S(38) + '. Kensington was sold in 2014 for about £180m [R] ' + S(39) + '.',
            '**Some strengths are really about business mix.** Investec\'s UK motor finance provision is £30m against about £320m at Close Brothers [C] ' + S(1, 36) + '. That mostly reflects a much smaller motor book, not better ethics [I].',
            '**Rathbones carries live risk.** In June 2026 Rathbones disclosed a regulator-prompted review and about £60m of remediation [R] ' + S(41) + '. It now runs the money behind Investec\'s new advice offer [I].',
            '**Staff reviews are good but typical.** Glassdoor about 4.1 to 4.2 out of 5; praise for a "flat hierarchy", complaints about slow change and progression [R, anecdote] ' + S(42) + '.')
    o += table(['Genuinely distinctive','Ordinary, shared or weaker'],[
      ['The bundle in one mid-sized firm [I]','"Relationship banking" claimed by Arbuthnot, Close, Hoare\'s, Coutts [C/R]'],
      ['Clients chosen for building wealth [R]','Not the award leader in UK private banking [C]'],
      ['EVA bonus pools, deferred and clawable [C]','UK cost-to-income 54% vs 26-36% at lean rivals [C]'],
      ['Unanimous credit committees with independent voters [C]','UK returns below Shawbrook, Coutts, Barclays PB [C]'],
      ['No state rescue in 2008 (Koseff\'s claim) [C]','Kensington showed overreach [C]'],
      ['"Smart humans, not chatbots" [C headline]','Savings arm draws "no way to talk to anyone" complaints [anecdote]']])
    o += END

    o += part('p7', 'Part 7', 'How to say it in an interview', 'Lines you can use, and traps to avoid.')
    o += h2('g7a', 'Three lengths')
    o += box('say', '"Investec picks ambitious clients and serves the person and their business through one banker, and its pay and credit rules reward long-term, risk-aware work rather than volume."', '10 seconds')
    o += box('say', '"What struck me is that Investec\'s relationship model is built into its plumbing. Bonus pools come from economic value added, so a team that wins business with capital-heavy, risky deals doesn\'t grow its pot. Big bonuses are deferred into shares and can be clawed back, most staff own shares, and every credit committee needs unanimous consent, which goes back to the founders\' veto. Lots of banks say relationship. Investec pays for it."', '45 seconds')
    o += box('say', '"Many UK banks say they build relationships, so that alone isn\'t it. What is rare is the bundle: Investec can lend to a founder\'s company, act as its broker, where it has been the top-ranked small and mid-cap broker four years running, and bank the founder personally, now with Rathbones running the money behind Investec\'s advice. The 2026 plan pushes that further with current accounts for private clients and a corporate bank that is meant to feel like private banking. The honest test is cost: UK costs are 54% of income and returns are below Shawbrook and Coutts, so the next three years show whether relationships turn into returns at scale."', '2 minutes')
    o += h2('g7b', 'Traps')
    o += table(['Do not say','Say instead'],[
      ['"Investec is unique because it does relationship banking"','"The combination of businesses is rare; the relationship claim is shared"'],
      ['"Investec doesn\'t sell"','"It sells through a relationship, and pays on risk-adjusted profit, not volume"'],
      ['"Investec has the best private bank"','"It targets wealth creators; Arbuthnot leads the service awards"'],
      ['"They never make mistakes"','"Kensington in 2007 is the lesson; selling it and Australia in 2014 showed discipline"']])
    o += h2('g7c', 'Questions that show you understood')
    o += OL('How is collaboration between private and corporate bankers rewarded, given bonus pools are measured by team EVA?',
            'With Investec now leading the advice relationship and Rathbones running the money, how does a private banker\'s day change?',
            'What would tell you by FY28 that the high-touch model is lifting UK returns towards the target range?',
            'How does a unanimous credit committee work in practice when a relationship manager is keen on a deal?')
    o += END

    gl = [('Basis point','One hundredth of one percent.'),('Bonus pool','The total pot of bonus money a team shares.'),('Capital','The bank\'s own money that absorbs losses.'),
          ('Clawback','Recovering a bonus already paid.'),('Corporate broker','A listed company\'s ongoing stock-market adviser.'),('Cost-to-income ratio','Costs as a share of income; lower is leaner.'),
          ('Credit committee','The group that approves loans.'),('Credit scorecard','An automated points system for approving loans.'),('Deferral','Paying part of a bonus years later.'),
          ('Demerger','Splitting off a business as a separately listed company.'),('Deposit','Money a customer leaves with a bank.'),('DLC','Dual-listed company: two listed companies acting as one.'),
          ('EVA','Economic value added: profit minus a charge for the capital used.'),('Flat structure','An organisation with few layers of management.'),('Fund finance','Lending to investment funds.'),
          ('Holding to maturity','Keeping a loan until it is repaid.'),('Malus','Cancelling a bonus awarded but not yet paid.'),('Meritocratic','Progress based on results, not seniority.'),
          ('Mid-market','Companies too big for small-business banking, too small for global banks.'),('Net interest income','Interest earned on loans minus interest paid on deposits.'),
          ('Niche','A small, specialised corner of a market.'),('Primary bank','The bank where a client keeps their main current account.'),('Private bank','A bank for wealthy or high-earning individuals.'),
          ('Relationship manager','The single named banker responsible for a client.'),('ROE / RoTE','Return on (tangible) equity: profit per pound of shareholders\' money.'),
          ('Transactional banking','Day-to-day services such as payments and cash management.'),('Veto','The right to block a decision on your own.'),('Wallet share','The share of a client\'s total banking one bank captures.'),
          ('Wealth management','Investing clients\' money for a fee.')]
    o += part('p8', 'Back matter', 'Glossary and sources', 'Every [Sxx] marker resolves below. All accessed 5 to 7 October 2026.')
    o += h2('g8a', 'Glossary')
    o += '<dl class="gl">' + ''.join(f'<dt>{esc(t)}</dt><dd>{esc(d)}</dd>' for t,d in gl) + '</dl>'
    o += h2('g8b', 'Sources')
    o += '<table class="src"><thead><tr><th style="width:28px">ID</th><th>Outlet</th><th>Title</th><th>Date</th><th>URL</th></tr></thead><tbody>' + ''.join(
        f'<tr><td>S{n}</td><td>{esc(a)}</td><td>{esc(t)}</td><td>{esc(d)}</td><td style="word-break:break-all">{esc(u)}</td></tr>' for n,(a,t,d,u) in SRC.items()) + '</tbody></table>'
    o += h2('g8c', 'What could not be found')
    o += UL('No published UK figures for cross-selling, client retention, client satisfaction (NPS) or repeat borrowers. "Integration" remains Investec\'s claim, not a measured fact.',
            'No current figure for staff ownership of Investec plc (only Investec Limited).', 'The 2025 and 2026 group remuneration reports could not be retrieved; pay design is from the 2024 reports and a 2026 share-award notice.',
            'investec.com web pages block automated reading; some Investec wording comes from search snippets and is tagged Reported.',
            'UK private-client targets conflict between sources (about +5,000 clients vs 16,000 households).')
    o += END
    return o

def main():
    body = build().replace('—', ', ')
    import importlib.util
    spec = importlib.util.spec_from_file_location('b', '/home/user/Applications2027/investec/build/build.py'); B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
    cover = ('<div class="cover"><div class="k">A guide from zero</div><h1>What makes<br>Investec stand out</h1>'
             '<div class="sub">The business model, the structure, the values and the relationship ethos: what Investec actually does differently, how it is wired into pay and risk, and where it is ordinary. No prior knowledge assumed.</div>'
             '<div class="meta">Prepared 7 October 2026 for the Investec UK Summer Internship 2027 application.<br>Built only from public sources: Investec\'s own reports, results and job adverts, regulators, courts and quality press.<br>Every claim carries a confidence tag and a source number listed at the back.</div></div>')
    css = open('/home/user/Applications2027/investec/build/style.css').read()
    page = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>What Makes Investec Stand Out</title><style>{css}</style></head><body>'
            f'{cover}{B.toc(body)}{B.markers(body)}</body></html>')
    open('/home/user/Applications2027/investec/What_Makes_Investec_Stand_Out.html','w',encoding='utf8').write(page)
    print('figs', len(lib.FIGS))
main()
