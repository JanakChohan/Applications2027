"""Parse source registries from research notes 11-12, plus the registry of note 10 as it stood when cited (pinned here because the file was renumbered later) and a few earlier IDs."""
FILE10 = """S700 | Bright Network | Inside Private Banking (J.P. Morgan event listing) | 2026 | https://www.brightnetwork.co.uk/graduate-events/jp-morgan/inside-private-banking | READ | High
S701 | J.P. Morgan Private Bank | London, United Kingdom office page | live Oct 2026 | https://privatebank.jpmorgan.com/eur/en/locations/emea/united-kingdom/london | READ | High
S702 | WealthBriefing | JP Morgan Private Bank Appoints Global Chief Executive | Jul 2025 | https://www.wealthbriefing.com/html/article.php/jp-morgan-private-bank-appoints-global-chief-executive- | Snippet only | Med
S703 | FinTech Futures | Jennifer Piepszak named new JP Morgan Chase COO | 2025-01-15 | https://www.fintechfutures.com/job-cuts-new-hires/jennifer-piepszak-named-new-jp-morgan-chase-coo-with-daniel-pinto-set-to-retire | Snippet only | Med
S704 | St. Gallen Business Review | AI Won't Replace Relationships: interview with Adam Tejpaul | 2026-07-16 | https://stgallenbusinessreview.com/ai-wont-replace-relationships-rethinking-the-future-of-private-banking-an-interview-with-adam-tejpaul/ | READ | High
S705 | Euromoney | Europe's best international private bank 2026: JPMorgan Private Bank | 2026-03-20 | https://www.euromoney.com/article/900478nvez8cck4wcgkok4gs0/private-banking/europes-best-international-private-bank-2026-jpmorgan-private-bank/ | READ | High
S706 | J.P. Morgan Private Bank | Maricé Brown profile | n.d. | https://privatebank.jpmorgan.com/eur/en/people/marice-brown | Snippet only | High
S707 | Spear's 500 | Maricé Brown | 2025 | https://spears500.com/adviser/25784/marice-brown | READ | Med
S708 | J.P. Morgan Private Bank | Sarah Catania profile | n.d. | https://privatebank.jpmorgan.com/eur/en/people/sarah-catania | READ | High
S709 | J.P. Morgan Private Bank | Karim Rekik profile | n.d. | https://privatebank.jpmorgan.com/eur/en/people/karim-rekik | READ | High
S710 | Spear's 500 | Diana Robinson | 2026 | https://spears500.com/adviser/24434/diana-robinson | READ | Med
S711 | Caproasia | JP Morgan Private Bank appoints UK team lead Maya Prabhu as Head of Wealth Advisory and Family Governance for Asia | 2026-10-06 | https://www.caproasia.com/2026/10/06/jp-morgan-private-bank-appoints-uk-team-lead-maya-prabhu-as-head-of-wealth-advisory-and-family-governance-for-asia-25-years-private-banking-wealth-management-wealth-advisory-philanthropy-trust/ | READ | Med
S712 | Global Private Banker | J.P. Morgan reshuffles senior private bankers in APAC and EMEA | 2026 | https://globalprivatebanker.net/j-p-morgan-reshuffles-senior-private-bankers-in-apac-and-emea/ | PAYWALLED-NOT-READ | Low
S713 | TheWealthNet (PAM Insight) | Former Coutts head of wealth advisory joins JP Morgan Private Bank | 2018-12-10 | https://www.paminsight.com/twn/article/former-coutts-head-wealth-advisory-joins-jp-morgan-private-bank | READ | High
S714 | Caproasia | JP Morgan Private Bank people-moves roundup (incl. Paul Ferry, Nov 2025) | 2026-06-11 | https://www.caproasia.com/2026/06/11/jp-morgan-private-bank-has-50-private-bankers-in-singapore-for-southeast-asia-australia-new-senior-private-bankers-in-last-12-months-include-hsbc-private-bank-peter-c-y-lee-as-team-leader-standar/ | READ | Med
S715 | Scottish News | JP Morgan appoints Gillian Murray to lead Scottish private banking advisory team | 2024-08-06 | https://www.scottishnews.com/articles/jp-morgan-appoints-gillian-murray-to-lead-scottish-private-banking-advisory-team | READ | High
S716 | Financial News (mirror) | Coutts hires ex-JPMorgan banker James Todd as next private client boss | 2025 | https://fnlondon-spa-stg.sc.onservo.com/articles/coutts-hires-ex-jpmorgan-banker-james-todd-as-next-private-client-boss-103ae703 | Snippet only | Med
S717 | J.P. Morgan Private Bank | Folarin Oyeleye profile | n.d. | https://privatebank.jpmorgan.com/eur/en/people/folarin-oyeleye | READ | High
S718 | GARP Careers (JPM postings) | Head of UK Lending; Team Lead Investment Specialist UK Team | 2025-26 | https://jobs.garp.org/job/international-private-bank-head-of-uk-lending/80505266 | Snippet only | Med
S719 | J.P. Morgan Private Bank | Chris Ottenritter profile | n.d. | https://privatebank.jpmorgan.com/eur/en/people/chris-ottenritter | Snippet only | High
S720 | J.P. Morgan Private Bank | James Chilvers profile | n.d. | https://privatebank.jpmorgan.com/eur/en/people/james-chilvers | Snippet only | High
S721 | J.P. Morgan Private Bank | Mark Hempstead profile | n.d. | https://privatebank.jpmorgan.com/eur/en/people/mark-hempstead | Snippet only | High
S722 | J.P. Morgan Private Bank | Kristin Kallergis Rowland profile | n.d. | https://privatebank.jpmorgan.com/gl/en/people/kristin-kallergis-rowland | Snippet only | High
S723 | J.P. Morgan Private Bank | Stewart Edginton profile | n.d. | https://privatebank.jpmorgan.com/eur/en/people/stewart-edginton | Snippet only | High
S724 | GAIN Health | Sheryl Fofaria bio | n.d. | https://gainhealth.org/sheryl-fofaria | Snippet only | Low
S725 | WORK180 (JPM posting) | Senior Philanthropy Advisor, Greater London (The Philanthropy Centre / Advice Lab) | c. 2022 | https://work180.com/en-gb/for-women/employer/jpmorgan/job/450728/philanthropy-advisor | READ | Med
S726 | J.P. Morgan Private Bank | Grace Peters profile | n.d. | https://privatebank.jpmorgan.com/eur/en/people/grace-peters | READ | High
S727 | J.P. Morgan Private Bank | Michael Cembalest profile | n.d. | https://privatebank.jpmorgan.com/eur/en/people/michael-cembalest | Snippet only | High
S728 | J.P. Morgan Private Bank | Ian Balfour profile | n.d. | https://privatebank.jpmorgan.com/eur/en/people/ian-balfour | Snippet only | Low
S729 | LinkedIn | Steven Rees | n.d. | https://ch.linkedin.com/in/strees | Snippet only | Low
S730 | J.P. Morgan Private Bank | Selim Elgen profile | n.d. | https://privatebank.jpmorgan.com/eur/en/people/selim-elgen | READ | High
S731 | Hubbis | JP Morgan expands private banking team in Middle East with senior hire from Barclays | 2026-03-27 | https://www.hubbis.com/news/jp-morgan-expands-private-banking-team-in-middle-east-with-senior-hire-from-barclays | READ | Med
S732 | Banking Exchange | JP Morgan Sharpens Swiss Private Banking Ambitions | 2025-12-03 | https://www.bankingexchange.com/news-feed/item/10486-jp-morgan-sharpens-swiss-private-banking-ambitions | READ | Med
S733 | TheWealthNet (PAM Insight) | JP Morgan PB makes further addition to London team (Lepschy; Andrews, Jellicoe) | 2026-08-18 | https://www.paminsight.com/twn/article/jp-morgan-pb-makes-further-addition-to-london-team | READ | Med
S734 | TheWealthNet (PAM Insight) | JP Morgan PB hires former Coutts banker (Jellicoe) | 2026-08-04 | https://www.paminsight.com/twn/article/jp-morgan-pb-hires-former-coutts-banker | READ | Med
S735 | JPMorganChase | 2025 Annual Report, AWM CEO letter (Mary Callahan Erdoes) | 2026-04-06 | https://www.jpmorganchase.com/ir/annual-report/2025/ar-ceo-letter-mary-callahan-erdoes | READ | High
S736 | Family Wealth Report | JP Morgan Reports Higher Q3 2026 Net Income, AuM Rises In Assets, Wealth Arm | 2026-10-13 | https://www.familywealthreport.com/article.php/JP-Morgan-Reports-Higher-Q3-2026-Net-Income%2C-AuM-Rises-In-Assets%2C-Wealth-Arm | READ | High
S737 | SEC / JPMorgan Chase | 3Q26 Earnings Release Financial Supplement (8-K Ex. 99.2) | 2026-10 | https://www.sec.gov/Archives/edgar/data/0000019617/000162828026065582/a3q26erfex992supplement.htm | READ | High
S738 | J.P. Morgan Private Bank | Private Bank Careers (EMEA) | n.d. | https://privatebank.jpmorgan.com/eur/en/about-us/private-bank-careers | READ | High
S739 | Gulf News / Bloomberg | JPMorgan to add more than 100 staffers in Mideast hiring spree | 2025-05-20 | https://gulfnews.com/business/banking/jpmorgan-to-add-more-than-100-staffers-in-mideast-hiring-spree-1.500133763 | READ | High
S740 | Bisnow | JPMorgan Plans London's Biggest Office With New Canary Wharf HQ | 2025-11-27 | https://www.bisnow.com/london/news/office/jpmorgan-plans-londons-biggest-office-with-new-canary-wharf-hq-132089 | READ | High
S741 | Irish Times (FT syndication) | JPMorgan to build Canary Wharf's tallest tower after City airport approval | 2026-04-07 | https://www.irishtimes.com/business/2026/04/07/jpmorgan-to-build-canary-wharfs-tallest-tower-after-city-airport-approval/ | READ | High
S742 | Victorian Web | City of London School, Victoria Embankment (Davis & Emanuel) | n.d. | https://victorianweb.org/art/architecture/schools/3.html | Snippet only | Med
S743 | J.P. Morgan Private Bank | Analyst Program / campus recruiting (summer timeline, roadmap, Morning@Morgan) | 2027 cycle | https://privatebank.jpmorgan.com/nam/en/about-us/campus-recruiting | READ | High
S744 | CityU Hong Kong College of Business | J.P. Morgan Private Bank Challenge 2026 | 2026-07-06 | https://www.cb.cityu.edu.hk/careerdevelopment/news/events/eventDetails/?id=40120 | READ | Med
S745 | CleverPrep | The Complete Private Banker Interview Guide for JPMorgan Chase | n.d. | https://www.cleverprep.com/companies/jpmorgan/private-banker | Snippet only | Low
S746 | targetjobs | 2027 Global Private Bank – Advisor Summer Internship Program (London) | 2026 | https://targetjobs.co.uk/jobs/2027-global-private-bank-advisor-summer-internship-program-247457 | READ | Med
S747 | targetjobs | 2027 Global Private Bank – Investment Solutions Summer Internship Program (London) | 2026 | https://targetjobs.co.uk/jobs/2027-global-private-bank-investment-solutions-summer-internship-program-247471 | READ | Med
S748 | Bright Network | 2027 Global Private Bank Advisor Analyst Training Program – London, Manchester, Edinburgh | 2026 | https://www.brightnetwork.co.uk/graduate-jobs/jp-morgan/2027-global-private-bank-advisor-analyst-training-program-london-manchester-edinburgh | Snippet only | Med
S749 | Bright Network | 2027 Global Private Bank Investment Solutions Analyst Training Program – London | 2026 | https://www.brightnetwork.co.uk/graduate-jobs/jp-morgan/2027-global-private-bank-investment-solutions-analyst-training-program-london | Snippet only | Med
S960 | Kean University career page | JPMorganChase 2027 Global Private Bank Advisor Program Summer Analyst (process notice) | 2026 | https://career.kean.edu/jobs/jpmorganchase-2027-global-private-bank-advisor-program-summer-analyst-us-private-bank/ | Snippet only | Med
S961 | The Muse (JPM posting) | International Private Banker, Vice President, UK Financial Institutions Group | 2026-10-06 | https://www.themuse.com/jobs/jpmorganchase/international-private-banker-vice-president-private-banker-uk-financial-institutions-group | READ | High
S962 | The Muse (JPM posting) | International Private Bank, Senior Associate, Private Banker, UK Entrepreneurs & Executives Team | 2026-07-04 | https://www.themuse.com/jobs/jpmorganchase/international-private-bank-senior-associate-private-banker-uk-entrepreneurs-executives-team | READ | High
S963 | Built In (JPM posting) | International Private Bank – Client Service – Associate (Hong Kong) | removed 2026-01-26 | https://builtin.com/job/international-private-bank-client-service-associate/7721290 | READ | Med"""
import re, glob
def load():
    S={}
    for line in FILE10.splitlines():
        p=[x.strip() for x in line.split("|")]
        S[p[0]]=(p[1],p[2],p[3],p[4],p[5],p[6])
    for f in ["../research/11_latest_news_numbers_oct2026.md","../research/12_how_pb_works_scenario_strategy.md"]:
        for line in open(f, encoding="utf-8"):
            m=re.match(r"^(S\d{3})\s*\|\s*(.*)$", line.strip())
            if not m: continue
            parts=[p.strip() for p in m.group(2).split("|")]
            if len(parts)<7: continue
            outlet,title,date,url,acc,status,conf=parts[:7]
            sid=m.group(1)
            if "10_ipb" in f and sid in ("S750","S751","S752","S753"): sid="S96"+sid[-1]
            S[sid]=(outlet,title,date,url,status,conf)
    extra={
    "S572":("JPMorgan Chase","J.P. Morgan increases direct lending commitment to $50 billion","2025-02-24","https://www.jpmorgan.com/about-us/corporate-news/2025/jpmorgan-increases-direct-lending-commitment-to-50-billion","READ","High"),
    "S575":("JPMorgan Chase","2025 Investor Day, Asset & Wealth Management transcript (Erdoes)","2025-05-19","https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/events/2025/jpmc-2025-investor-day/awm.pdf","READ","High"),
    "S576":("J.P. Morgan Private Bank","Private credit under the microscope","2026-03-12","https://privatebank.jpmorgan.com/nam/en/insights/markets-and-investing/private-credit-under-the-microscope-separating-headlines-from-fundamentals","READ","High"),
    "S577":("J.P. Morgan Private Bank","Private credit still earns its place in portfolios, with the right approach","2026-04-16","https://privatebank.jpmorgan.com/eur/en/insights/markets-and-investing/ideas-and-insights/private-credit-still-earns-its-place-in-portfolios-with-the-right-approach","READ","High"),
    "S613":("J.P. Morgan Private Bank","The new frontier: 3 themes driving alternatives in 2026","2026-01-15","https://privatebank.jpmorgan.com/nam/en/insights/markets-and-investing/ideas-and-insights/the-new-frontier-3-themes-driving-alternatives-in-2026","READ","High"),
    "S900":("JPMorgan Chase","2025 Form 10-K and 4Q25 earnings materials (segment revenue, headcount, AWM lines)","2026-02","https://jpmorganchaseco.gcs-web.com/financial-information/sec-filings","READ","High"),
    "S901":("JPMorgan Chase","2024 and 2025 Investor Day AWM transcripts and 2021-2025 AWM CEO letters (advisor economics, 'seed books', targets)","2022-2026","https://www.jpmorganchase.com/ir/annual-report","READ","High"),
    "S902":("Euromoney","The world's best for alternative investments 2025/2026 and Europe's best international private bank 2026 (Tejpaul interview)","2026-03-20","https://www.euromoney.com/","READ","High"),
    "S903":("JPMorgan Chase","Q3 2025 earnings call (Dimon 'cockroach' remark)","2025-10-14","https://fortune.com/2025/10/15/jamie-dimon-issues-private-credit-warning-when-you-see-one-cockroach-there-are-probably-more","READ","High"),
    "S904":("J.P. Morgan Private Bank","Alternatives guide for private clients (allocation ranges, drawdown vs evergreen)","2025","https://privatebank.jpmorgan.com/","READ","Med"),
    "S905":("JPMorgan Chase","Jamie Dimon 2025 shareholder letter ('neural network'; fortress balance sheet)","2026-04-06","https://www.jpmorganchase.com/ir/annual-report/2025/ar-ceo-letter-jamie-dimon","READ","High"),
    }
    for k,v in extra.items(): S.setdefault(k,v)
    return S
if __name__=="__main__":
    S=load(); print(len(S), sorted(S)[:5], sorted(S)[-5:])
