import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
import parts_end as E, lib
OUT = '/home/user/Applications2027/investec'
# Question bank
q = ['# Investec Summer Internship 2027: Question Bank', '', 'Prepared 5 October 2026. Scaffolds, not scripts. [Sxx] markers resolve in Part 15 of the complete pack. HireVue and team-round questions marked "Reported" come from Glassdoor/WSO anecdotes [S40, S41].', '']
n = 0
for grp, qs in E.QB.items():
    q += [f'## {grp}', '']
    for item in qs:
        n += 1
        q += [f'### {n}. {item[0]}', f'- **Tests:** {item[1]}', f'- **Structure:** {item[2]}', f'- **Weave in:** {item[3]}', f'- **Trap:** {item[4]}', '']
q += ['## Questions to ask them', ''] + [f'{i+1}. {a}' for i,a in enumerate(E.ASK)]
open(f'{OUT}/Question_Bank.md','w').write('\n'.join(q) + '\n')
# Reading list from WS5 section 7
src = open(f'{OUT}/research/WS5_live_news.md', encoding='utf8').read()
rl = src[src.index('## 7. Reading list'):]
head = ['# Investec Summer Internship 2027: Reading List', '', 'Recurring sources to follow, compiled 5 October 2026 (from workstream WS5). Dates to watch: UK Budget 28 Oct 2026; MPC 5 Nov 2026; Investec interim results 19 Nov 2026; motor finance Upper Tribunal hearing 14-18 Dec 2026 or 16-26 Feb 2027; Basel 3.1 in force 1 Jan 2027.', '',
        '## Primary documents to read first', '',
        '1. Investec Final Results 31/03/2026 (RNS, 21 May 2026): https://www.investegate.co.uk/announcement/rns/investec--invp/final-results-31-03-2026/9578809',
        '2. Investec Pre-Close Trading Statement (18 Sep 2026): https://www.investegate.co.uk/announcement/rns/investec--invp/pre-close-trading-statement/9778512',
        '3. Investec Half-year Report to 30 Sep 2025 (corporate mid-market strategy): https://www.investegate.co.uk/announcement/rns/investec--invp/half-year-financial-report-30-sep-2025/9245448',
        '4. The internship posting (req 14049): https://careers.investec.co.uk/jobs/vacancy/summer-internship-2027-14049-london---30-gresham-street/14067/description/',
        '5. Bank of England, September 2026 Monetary Policy Summary: https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2026/september-2026',
        '6. HM Treasury Ring-Fencing Review (May 2026): https://assets.publishing.service.gov.uk/media/6a0ae2c5279ebb7d24f8f39b/Safeguarding_Stability__Enabling_Growth.pdf', '']
open(f'{OUT}/Reading_List.md','w').write('\n'.join(head) + '\n' + rl.replace('## 7. Reading list – recurring sources', '## Recurring sources').replace('–', '-'))
# Cheat sheet HTML
lib.FIGS.clear()
svgc = E.fig_cheat()
css = open(os.path.join(os.path.dirname(__file__),'style.css')).read()
html = f'<!doctype html><html><head><meta charset="utf-8"><title>Investec Cheat Sheet</title><style>{css} @page{{size:A4;margin:10mm}} body{{margin:0}}</style></head><body>{svgc}<p class="small" style="margin-top:6px">Sources: S70, S120, S278, S282 (figures, Confirmed); S78, S80, S157, S176, S222, S230, S244 (dates). Full source table in Part 15 of the complete pack. Prepared 5 Oct 2026.</p></body></html>'
open(f'{OUT}/build/Cheat_Sheet.html','w').write(html)
print(n, 'questions')
