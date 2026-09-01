# -*- coding: utf-8 -*-
from pdfbuild import *
LINK='https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/'

def build():
    F=[]; A=F.append
    A(PageBreak())
    A(heading('Part 5 — The London summer analyst programmes', 0))
    A(Paragraph('Live requisition data, read on 31 August 2026. This is the section that determines what you apply to.', S['h1sub']))

    A(callout('Read this box first — the timing news is unusually good',
        'The <b>2027 London programmes opened on 31 August 2026</b> — the day this research was carried out. Nearly every UK '
        'requisition carries a posting start date of 31 August 2026 and a stated close of <b>1 November 2026, 23:55</b>.<br/><br/>'
        'JPMorgan states in the postings themselves: <i>"We will be filling our classes on a rolling basis. We strongly encourage you '
        'to submit your application as early as possible before job postings close."</i> That language appears in <b>35 of the 43</b> '
        'UK requisitions found.<br/><br/>'
        '<b>The practical consequence: 1 November is a backstop, not a target.</b> Places are filled continuously from September. '
        'An application submitted in mid-October competes for whatever is left. Treat the real deadline as late September.', 'warn'))

    A(heading('5.1  How this list was obtained, and what that means for you', 1))
    A(P('JPMorgan\'s public careers pages — careers.jpmorgan.com, which now redirects to jpmorganchase.com/careers — are content '
        'shells. They show programme <i>categories</i> ("Early Insight", "Internship", "Full-Time") and invite you to join a mailing '
        'list. They do not render live vacancies, and no amount of clicking will make them do so.'))
    A(P('The live data sits in JPMorgan\'s Oracle Recruiting Cloud instance. I queried it directly and harvested 2,751 unique '
        'requisitions across roughly 35 keyword searches, then filtered to the United Kingdom. Everything in the table below is '
        'primary, live data — not a recruitment blog\'s summary of it.'))
    A(callout('The URLs you should use yourself, and re-check monthly',
        '<b>Browse all vacancies:</b><br/>https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions'
        '<br/><br/><b>Go straight to one job</b> (append the Job ID from the table below):<br/>'
        'https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/<b>210775710</b>'
        '<br/><br/>Filter by location "United Kingdom" and search "2027" or "Summer Internship". This is the authoritative source; '
        'everything else, including this report, is a snapshot of it.', 'info'))

    A(heading('5.2  Every UK programme currently open', 1))
    A(Paragraph('Summer internships — London', S['h3']))
    A(make_table(['Programme','Location','Job ID','Closes'],
        [['2027 Global Investment Banking Analyst Program — Summer Internship','London','210775710','1 Nov 2026'],
         ['2027 Commercial &amp; Investment Banking — Global Markets — Summer Internship','London','210780517','1 Nov 2026'],
         ['2027 Commercial &amp; Investment Banking — Sales — Summer Internship','London','210780555','1 Nov 2026'],
         ['2027 Commercial &amp; Investment Banking — Markets — Research — Summer Internship','London','210780476','1 Nov 2026'],
         ['2027 Commercial &amp; Investment Bank — Global Payments Analyst Program — Summer Internship','London','210774762','1 Nov 2026'],
         ['2027 Commercial &amp; Investment Bank — Securities Services Leadership Programme — Summer Internship','London','210774766','1 Nov 2026'],
         ['2027 Commercial &amp; Investment Banking — Risk Management Program — Summer Internship','London','210775727','1 Nov 2026'],
         ['2027 Global Corporate Banking Analyst Program — International ABL — Summer Internship','London','210775320','1 Nov 2026'],
         ['2027 Global Corporate Banking Analyst Program — Public Sector — Summer Internship','London','210775312','1 Nov 2026'],
         ['2027 Asset Management Investments — Summer Internship Program','London','210775295','1 Nov 2026'],
         ['2027 Asset Management — Risk Summer Internship Program','London','210774894','1 Nov 2026'],
         ['2027 Global Private Bank — Advisor Summer Internship Program','London','210773470','1 Nov 2026'],
         ['2027 Global Private Bank — Investment Solutions Summer Internship Program','London','210774281','1 Nov 2026'],
         ['2027 Chase Digital Development Programme — Summer Internship','London','210775305','1 Nov 2026'],
         ['2027 Software Engineer Program — Summer Internship','Glasgow &amp; London','210774716','1 Nov 2026'],
         ['2027 Data &amp; AI — Summer Internship','Glasgow &amp; London','210774745','1 Nov 2026'],
         ['2027 Corporate Analyst Development Program — Summer Internship','London','210775238','1 Nov 2026'],
         ['2027 Global Finance &amp; Business Management — Summer Internship','London','210774857','1 Nov 2026'],
         ['2027 Human Resources Analyst Development Program — Summer Internship','London','210774369','1 Nov 2026'],
        ], widths=[3.2,0.85,0.7,0.65], small=True))
    A(Paragraph('Summer internships and placements — outside London', S['h3']))
    A(make_table(['Programme','Location','Job ID','Closes'],
        [['2027 Corporate Analyst Development Program — Summer Internship','Bournemouth','210775228','1 Nov 2026'],
         ['2027 Corporate Analyst Development Program — Summer Internship','Edinburgh','210774353','1 Nov 2026'],
         ['2027 Global Finance &amp; Business Management — Summer Internship','Bournemouth','210774799','1 Nov 2026'],
         ['2027 Software Engineer Immersion Program — Summer Internship','Glasgow','210774813','1 Nov 2026'],
         ['2027 Software Engineer Program — 12 Month Industrial Placement','Glasgow &amp; London','210774738','1 Nov 2026'],
        ], widths=[3.2,0.85,0.7,0.65], small=True))
    A(Paragraph('Off-cycle internships — note that in London, Quantitative Research recruits this way, not via a summer programme', S['h3']))
    A(make_table(['Programme','Location','Job ID','Closes'],
        [['2027 Quantitative Research Markets Analyst Program — Off-Cycle Internship','London','210775342','1 Nov 2026'],
         ['2027 Quantitative Research Markets Associate Program — Off-Cycle Internship','London','210775780','1 Nov 2026'],
         ['2027 Quantitative Research — Risk and Treasury — Off-Cycle — Analyst','London','210776860','1 Nov 2026'],
         ['2027 Quantitative Research — Risk and Treasury — Off-Cycle — Associate','London','210776873','1 Nov 2026'],
         ['2027 Quantitative Research — Asset Management — Off-Cycle','London','210776770','1 Nov 2026'],
         ['2026 Commercial &amp; Investment Banking — Markets — Off-Cycle Internship','London','210757890','30 Sep 2026'],
         ['2026 Machine Learning Center of Excellence (NLP) — Internship','London','210765492','not stated'],
        ], widths=[3.2,0.85,0.7,0.65], small=True))
    A(Paragraph('Insight and skills programmes, and full-time analyst roles open now', S['h3']))
    A(make_table(['Programme','Location','Job ID','Closes'],
        [['2026 Code for Good','Glasgow','210778599','9 Oct 2026'],
         ['2026 Data for Good','Glasgow','210778609','9 Oct 2026'],
         ['2027 Chase Digital Development Programme — Full-time Analyst','London','210774321','1 Nov 2026'],
         ['2027 Commercial &amp; Investment Banking — Innovation Development Program — Full-Time Analyst','London','210785427','1 Nov 2026'],
         ['2027 Global Payments Analyst Program — Full time','London','210775299','1 Nov 2026'],
         ['2027 Asset Management Investments — Analyst Training Program','London','210775256','1 Nov 2026'],
         ['2027 Asset Management — Risk Analyst Training Program','London','210774880','1 Nov 2026'],
         ['2027 Global Private Bank — Advisor Analyst Training Program','London, Manchester, Edinburgh','210773771','1 Nov 2026'],
         ['2027 Software Engineer Program — Full-time','Glasgow &amp; London','210774781','1 Nov 2026'],
         ['2027 Data &amp; AI — Full Time Analyst','London &amp; Glasgow','210774755','1 Nov 2026'],
         ['2027 Global Finance &amp; Business Management — Full-Time','London','210775272','1 Nov 2026'],
         ['2027 Global Finance &amp; Business Management — Full-Time','Bournemouth','210775263','1 Nov 2026'],
        ], widths=[3.0,1.0,0.7,0.65], small=True))
    A(Paragraph('All 43 UK requisitions found are listed across these four tables. Source: JPMorgan Oracle Recruiting Cloud '
        'requisition records, read 31 August 2026. Job IDs are stable identifiers; append one to the job URL given above. '
        'Closing dates are from the requisition metadata and, for 17 of the postings, are also stated in the description text.', S['cap']))

    A(callout('What is NOT there — and this matters as much as what is',
        '<b>No UK Spring Week or first-year insight programme is currently posted.</b> A search for "spring week" returned zero '
        'requisitions globally; "early insight" and "insight week" returned matches, none in the UK. The only first-year-accessible UK '
        'offerings open now are <b>Code for Good</b> and <b>Data for Good</b> in Glasgow, both closing 9 October 2026.<br/><br/>'
        '<b>No UK-posted "Winning Women" or "Advancing Black Pathways" requisition</b> was found. Both exist as JPMorgan programmes; '
        'in EMEA they appear to be run as events rather than ATS vacancies — that is an inference, not a sourced statement.<br/><br/>'
        '<b>Where to look instead:</b> re-check the Oracle listing filtered to the United Kingdom monthly from October, and watch the '
        '"Early Insight (pre-internship)" category on jpmorganchase.com/careers/explore-opportunities/programs. JPMorgan\'s EMEA spring '
        'programmes have historically opened later in the autumn than summer internships. If you are a first-year student, this is the '
        'thing to diarise.', 'warn'))
    A(callout('Two gaps in the data I could not close',
        '<b>Intake sizes:</b> the field exists in the requisition record and is <b>null on every single posting</b>. JPMorgan does not '
        'publish how many people it takes. Any number you read elsewhere is an estimate.<br/><br/>'
        '<b>Visa sponsorship:</b> most UK postings are <b>silent</b> on it. Two — the Data &amp; AI Summer Internship and the Data &amp; '
        'AI Full Time Analyst role — state explicitly: <i>"We do not offer any type of employment-based immigration sponsorship for this '
        'program."</i> Whether that is UK-specific policy or template language carried over from US postings, I cannot tell from the '
        'text. <b>If you need sponsorship, verify it on the application form or with the recruiter before investing time.</b>', 'warn'))
    A(figure('f11_timeline','Figure 13. The 2027 London cycle. Open and close dates are primary; internal stage timings are inferred.'))

    A(heading('5.3  Standardised role profiles', 1))
    A(P('The nine-week structure is common to most of these programmes: five days of induction and training, then placement on a desk '
        'or team, then a return-offer decision. The postings say so explicitly. What differs is the work and who it suits.'))

    def role(title, where, what, day, screen, tech, good, path, hours, comp):
        A(Paragraph(title, S['h3']))
        A(kv_table([
            ['<b>Where it sits in the business</b>', where],
            ['<b>What the team does</b>', what],
            ['<b>What an intern actually does</b>', day],
            ['<b>Screened for</b>', screen],
            ['<b>Know before day one</b>', tech],
            ['<b>What "good" looks like</b>', good],
            ['<b>Path at 2 / 5 / 10 years</b>', path],
            ['<b>Hours, honestly</b>', hours],
            ['<b>Competitiveness</b>', comp]]))

    role('Global Investment Banking Analyst Program — Summer Internship',
      'CIB → Investment Banking. Touches the <b>$10.2bn</b> Investment Banking revenue line (of which $9.7bn is fees).',
      'Advises companies on acquisitions, disposals and raising money. You join a Coverage, Advisory or Capital Markets team spanning '
      'Consumer &amp; Retail, Healthcare, Technology, Financial Institutions and Real Estate, or products including M&amp;A, Corporate '
      'Finance Advisory, Infrastructure, Ratings Advisory, Sustainable Solutions, ECM and DCM.',
      'Building and checking financial models in Excel; comparable-company and precedent-transaction analysis ("comps"); assembling '
      'pitch books in PowerPoint; company and industry research; profiles of potential targets or buyers; maintaining data rooms. '
      'The posting says it plainly: "analyzing market data, building detailed financial models".',
      'Precision under pressure, commercial curiosity, resilience, evidence you finish things. Attention to detail is screened harder '
      'here than anywhere else — a formatting error in a client document is treated as a serious failure.',
      'The three financial statements and how they link; enterprise vs equity value; DCF and comparable-company valuation; what EBITDA '
      'is and why it is used; one live deal you can discuss intelligently. Genuine Excel fluency.',
      'Zero errors, work returned early, asking one good question rather than five poor ones, and being visibly reliable at 11pm.',
      '<b>2:</b> analyst, execution and modelling. <b>5:</b> associate/VP, running processes and client contact. <b>10:</b> Executive '
      'Director or MD originating business — or, far more commonly, exited to private equity, a corporate development role, or a fund.',
      'The hardest in the firm. Long weekdays and frequent weekend work when live. Do not apply because it sounds prestigious.',
      'Most competitive London programme. Strongest exit optionality in finance, which is why.')

    role('Global Markets — Summer Internship (Sales &amp; Trading)',
      'CIB → Markets. Touches <b>Fixed Income ($22.5bn)</b> and <b>Equity Markets ($13.3bn)</b>.',
      'Market-making and risk management across rates, credit, currencies, emerging markets, securitised products, commodities, cash '
      'equities, equity derivatives and prime brokerage. Note this is the <b>Global Markets</b> posting; <b>Sales</b> is advertised '
      'as a separate requisition in London — read both before choosing.',
      'JPMorgan\'s own words: "monitor markets, develop trade ideas, conduct portfolio reviews, and learn about the solutions and '
      'products we offer". In practice: morning market summaries, tracking positions, small pricing and data tasks, building sheets '
      'that automate something tedious, and absorbing an enormous amount by listening.',
      'Fast mental arithmetic, decisiveness under uncertainty, comfort being wrong in public, genuine market interest. Being able to '
      'say what you think a market will do and why, then defend it.',
      'What bid-ask spread and market making mean; the difference between cash and derivatives; how a bond price relates to its yield; '
      'why central bank policy moves markets. Have a live view on rates or an equity index and the reasoning behind it.',
      'Knowing your desk\'s products cold by week three, having an opinion, and never being the reason a trade is mis-booked.',
      '<b>2:</b> junior trader or salesperson with limited risk. <b>5:</b> running a book or a client list. <b>10:</b> senior '
      'trader, desk head, or a move to a hedge fund or asset manager.',
      'Brutal start (on the desk before 7am) but far more predictable than banking. Rarely weekends. The intensity is the market\'s, not the calendar\'s.',
      'Very competitive, and screens for a different personality than banking — quicker, blunter, more numerate.')

    role('Markets — Research — Summer Internship',
      'CIB → Global Research, supporting the Markets franchise.',
      'Publishing investment views on companies, sectors, economies and asset classes for institutional clients.',
      'Updating earnings models, gathering and cleaning data, drafting sections of notes, building sector screens, summarising results '
      'and industry news for the senior analyst.',
      'Genuine writing ability — rarer than numeracy and more valued here. Analytical independence and the confidence to hold a '
      'contrarian view with evidence.',
      'How to read a company\'s accounts; what drives a sector you care about; and the MiFID II research-payment story in section 3.4. '
      'That last point is the "why now" question for this seat.',
      'A note section that needs almost no editing, and a data point nobody else found.',
      '<b>2:</b> associate supporting an analyst. <b>5:</b> publishing analyst with your own coverage. <b>10:</b> ranked senior '
      'analyst — or, very commonly, a move to the buy side.',
      'Long around earnings season, calmer between. Better than banking.',
      'Competitive, and a smaller intake than Markets. Suits deep, writerly analysts over generalists.')

    role('Quantitative Research — Off-Cycle Internship (Markets / Risk &amp; Treasury / Asset Management)',
      'CIB Markets, Risk, and AWM. Underpins derivative pricing and electronic trading firmwide.',
      'Building the mathematical models that price derivatives, measure risk and drive algorithmic trading. Three separate London '
      'streams are advertised, plus associate-level versions for postgraduates.',
      'Implementing and testing pricing models in Python or C++; calibrating models to market data; back-testing; writing model '
      'documentation; building tooling for traders.',
      'Serious mathematics — stochastic calculus, probability, numerical methods — plus real programming. Typically a strong '
      'quantitative Master\'s or PhD, though the analyst stream accepts Bachelor\'s.',
      'Python to a genuinely fluent standard; linear algebra and probability; ideally exposure to stochastic processes and '
      'option-pricing theory.',
      'Code that works, is tested, and that a trader trusts. Explaining a model to someone who will never read the mathematics.',
      '<b>2:</b> quant analyst on a desk. <b>5:</b> owning a model family. <b>10:</b> head of quant for an asset class, or a '
      'systematic hedge fund.',
      'Reasonable, project-driven. Closer to research than to trading hours.',
      '<b>Note the structural point: in London these are OFF-CYCLE, not summer, internships.</b> If you want quant research in London '
      'you must apply to a different programme type than your peers targeting Markets.')

    role('Global Payments Analyst Program — Summer Internship',
      'CIB → Payments. The <b>$19.3bn</b> revenue line — larger than the entire investment banking fee pool.',
      'In JPMorgan\'s own words, learning "what it takes to make money move". Brings together Payments, Merchant Services and '
      'Commercial Card across the full "Pay In and Pay Out lifecycle".',
      'Client cash-management analysis, product and implementation work, competitor and market research, working with coverage teams, '
      'and — per the posting — identifying "opportunities to leverage emerging technologies".',
      'Commercial and product instinct rather than pure valuation skill. Structured problem-solving, comfort with technology, '
      'client-facing communication.',
      'How money actually moves between banks and countries; what a treasurer worries about; who Stripe and Adyen are and why they '
      'matter. Section 3.4 of this report is most of the preparation you need.',
      'Understanding a client\'s operational problem rather than just the product sheet.',
      '<b>2:</b> product or coverage analyst. <b>5:</b> product manager or treasury sales. <b>10:</b> senior product or sales '
      'leadership; strong moves into fintech.',
      'Genuinely reasonable — closer to corporate hours than banking.',
      'Materially less competitive than IB or Markets for a business of enormous strategic value. <b>This is arguably the best '
      'value-for-effort application on the list.</b>')

    role('Securities Services Leadership Programme — Summer Internship',
      'CIB → Securities Services. The <b>$5.6bn</b> custody, fund administration and collateral business.',
      'Holding and servicing institutional clients\' assets. The posting frames it as a leadership and project-management programme '
      'with exposure "across the full end-to-end business".',
      'Per the posting: "develop solutions and drive change in finance using project management, emerging technologies, data '
      'governance and analytics" and "drive innovation with the use of digital tools". Process and data work more than markets work.',
      'The posting asks for "exceptional writing, verbal communication and client facing skills" and "the aptitude to synthesize large '
      'amounts of information".',
      'What custody and fund administration are, and why switching custodian is so hard. The stickiness argument in section 3.4.',
      'Owning a project end to end and communicating it clearly to people more senior than you.',
      '<b>2:</b> product or client-service analyst. <b>5:</b> product manager or relationship manager. <b>10:</b> senior leadership '
      'in securities services or operations.',
      'Among the most civilised in the CIB.',
      'Less competitive than the front office. Capital-light, sticky, high-quality revenue — a much better business than its '
      'reputation among students suggests.')

    role('Asset Management Investments &amp; Global Private Bank — Summer Internships',
      'AWM. The <b>40% ROE</b> segment: Asset Management $11.7bn, Global Private Bank $12.4bn.',
      '<b>Asset Management Investments</b> runs money — equities, fixed income, multi-asset, alternatives, liquidity funds. '
      '<b>Global Private Bank Advisor</b> serves wealthy families; <b>GPB Investment Solutions</b> builds the portfolios and products '
      'behind that advice. A separate <b>Asset Management Risk</b> internship also exists.',
      'Investments: company and fund research, portfolio analytics, performance attribution, investment committee materials. '
      'Private Bank: client portfolio reviews, market updates, proposals, and a great deal of relationship support.',
      'Investments screens for genuine investment interest — a portfolio you run, an investment society, a view you can defend. '
      'The Private Bank screens far more for maturity and interpersonal polish; you will sit with very wealthy clients.',
      'How funds charge fees; active versus passive; the difference between AUM and client assets (section 3.5); and for the '
      'Private Bank, why an entrepreneur who has just sold a company needs a bank at all.',
      'An investment view with the work behind it; or, in the Private Bank, being someone a client is comfortable with.',
      '<b>2:</b> research or client associate. <b>5:</b> portfolio manager track or banker with own clients. <b>10:</b> senior PM or '
      'senior banker. Note the GPB advisor count grew 9% in 2025 — they are hiring.',
      'The best lifestyle of any front-office route in the firm.',
      'Competitive but less ferocious than IB. The economics of the segment are the best in the firm, which few students realise.')

    role('Software Engineer, Data &amp; AI, and Chase Digital Development Programme',
      'Corporate technology, and Chase UK within International Consumer Banking.',
      '<b>Software Engineer</b>: platform, front-office and infrastructure engineering, in Glasgow and London, with a 12-month '
      'industrial placement variant. <b>Data &amp; AI</b>: per the posting, "end-to-end data, analytics, and artificial intelligence '
      'and machine learning solutions", using AWS, Snowflake, Databricks and LLMs. <b>Chase Digital</b>: product management for the '
      'UK digital bank — the posting describes it as starting "your journey in becoming a Product Manager".',
      'Real code in real repositories, code review, testing, data pipelines, dashboards. Chase Digital is product rather than '
      'engineering: user research, requirements, working with designers and engineers.',
      'Engineering: demonstrable code — projects, contributions, internships. Data &amp; AI: Python plus statistics. Chase Digital: '
      'product instinct, "an entrepreneurial mindset", and interest in fintech.',
      'Engineering: a language you know well, data structures, version control, some cloud. Chase Digital: use Chase UK, Monzo and '
      'Revolut and be able to critique all three.',
      'Shipping something that survives review and is still running after you leave.',
      '<b>2:</b> software engineer II / associate PM. <b>5:</b> senior engineer or product manager. <b>10:</b> lead engineer, '
      'engineering manager, or senior product — with the strongest external optionality of any route here, into tech and startups.',
      'The most reasonable hours in the firm, by a distance.',
      'Least competitive relative to intake, because most finance-focused applicants ignore these. Note that Glasgow is a genuine '
      'engineering centre, not an overflow office. <b>Caution: the Data &amp; AI postings state no immigration sponsorship is offered.</b>')

    role('Risk Management, Global Finance &amp; Business Management, CADP and HR',
      'CIB Risk; and the Corporate segment, which employs 50,031 people firmwide.',
      '<b>CIB Risk Management</b> is a nine-week programme with a five-day induction, placing you in a risk team — the posting names '
      'Credit Risk, which "reviews client credit strength and approves and manages retained credit risk... including investment and '
      'non-investment grade syndicated loans, acquisition finance". <b>Global Finance &amp; Business Management</b> is the firm\'s '
      'internal finance function. <b>CADP</b> is a rotational analytics, project management and process improvement programme. '
      '<b>HR</b> is the people function.',
      'Risk: credit analysis of real borrowers, limit monitoring, portfolio reviews, model outputs. GF&amp;BM: management reporting, '
      'business analysis, controls. CADP: data analysis, process mapping, project delivery.',
      'Risk screens for judgement and the willingness to say no to a revenue-generating colleague. CADP and GF&amp;BM screen for '
      'structured thinking and analytical care.',
      'Risk: what a credit rating means, how default risk is assessed, and section 1.3 of this report. CADP: be comfortable with data.',
      'Risk: an analysis whose conclusion holds when challenged. CADP: making a process measurably better.',
      '<b>2:</b> risk or finance analyst. <b>5:</b> VP owning a portfolio or reporting area. <b>10:</b> senior risk or finance '
      'leadership. Note CADP\'s full-time programme is a two-year rotation across all three disciplines.',
      'Civilised and predictable across all four.',
      'Least competitive of the London programmes. <b>Read this honestly:</b> the CADP posting itself states it "is not aligned to '
      'front-office, client-facing, or software engineering roles". It is an excellent programme for the right person and a poor '
      'consolation prize for someone who wanted IB. Apply to it because you want it.')

    A(heading('5.4  Comparing the programmes', 1))
    A(figure('f12_roles','Figure 14. Scored 1 to 5. These are the author\'s judgements based on the role descriptions and the '
        'business analysis in Part 3 — they are not JPMorgan data and you should argue with them.'))
    A(make_table(['Programme','Best exits','Worst reason to pick it'],
        [['Investment Banking','Private equity, hedge funds, corporate development, growth-stage startups. The broadest exit set in finance.','Because it is the most prestigious. The hours will find you out.'],
         ['Global Markets / Sales','Hedge funds, asset managers, and market-making firms. Narrower than IB but deeper.','Because you like the idea of trading. Watch a desk first.'],
         ['Research','Buy-side analyst roles. A genuinely strong path if you can write.','Because you could not decide between IB and Markets.'],
         ['Quantitative Research','Systematic hedge funds, quant trading firms, technology. Excellent and well paid.','Because you are "good at maths". The bar is a research-level bar.'],
         ['Payments','Fintech product and strategy, corporate treasury, payments companies. Underrated.','Because it sounded like an easier route into the CIB.'],
         ['Securities Services','Asset servicing, operations leadership, fund platforms.','Because it was the only CIB programme you thought you could get.'],
         ['Asset Management / Private Bank','Asset managers, wealth firms, family offices, multi-manager platforms.','Because the hours are better. They are — but the work is different, not lighter.'],
         ['Software Engineering / Data &amp; AI','Technology firms, startups, quant firms, any industry at all.','Because you want to move into a front-office finance seat later. That transfer is possible but not the default.'],
         ['Risk / Finance / CADP','Risk and finance leadership, consulting, corporate strategy.','As a fallback for a front-office ambition — see the CADP posting\'s own warning above.'],
        ], widths=[1.0,2.3,2.0], small=True))

    A(heading('5.5  The recruitment process', 1))
    A(P('The stages below are what the postings and widely-reported candidate accounts describe. <b>Only the application step and the '
        'dates are primary</b>; the internal stage detail is drawn from recruitment aggregators and candidate reports and should be '
        'treated as unverified colour.'))
    A(make_table(['Stage','What happens','What it is really screening for'],
        [['<b>1. Application</b>','Online form, CV, and a location preference. JPMorgan\'s own guidance in the postings: "Help us learn about you by submitting a complete and thoughtful application... it\'s important to complete all relevant application questions."','Eligibility, academic threshold, and whether your story is coherent for the programme you chose. Several UK postings specify a <b>2:1 Bachelor\'s degree (or equivalent)</b>.'],
         ['<b>2. Online assessment</b>','Numerical and situational-judgement style testing, and for some programmes a timed maths test.','Basic numeracy and consistency. It is a filter, not a differentiator — practise so it is a non-event.'],
         ['<b>3. HireVue video interview</b>','Asynchronous, recorded. You are given a prompt and record an answer with no interviewer present. Predominantly behavioural, plus a CV walk-through.','Communication under mild artificial stress, motivation for the specific programme, and whether you have done any homework on the firm. Most rejections happen here.'],
         ['<b>4. Assessment centre / superday</b>','Back-to-back interviews, in the UK usually branded an assessment centre. For IB and Markets expect technical questions on accounting, valuation and markets alongside behavioural ones. May include a case study or group exercise.','Technical competence, and whether the desk wants to sit next to you for nine weeks.'],
         ['<b>5. Offer</b>','Released on a rolling basis as classes fill.','—'],
        ], widths=[0.85,2.6,2.4], small=True))
    A(callout('Three specific things to do this week',
        '<b>1.</b> Decide on <i>at most</i> two programmes and apply in September, not October. The rolling-basis language is in the '
        'postings and it is not decorative.<br/>'
        '<b>2.</b> Record a two-minute answer to "walk me through your CV" and watch it back. The HireVue is the highest-attrition '
        'stage and the easiest to prepare for.<br/>'
        '<b>3.</b> If you are a first-year, diarise a monthly check of the Oracle listing for a UK Spring programme, and apply to Code '
        'for Good or Data for Good in Glasgow before 9 October 2026.', 'key'))

    A(heading('5.6  Which one should you actually apply to?', 1))
    A(make_table(['If this is you','Target','Why'],
        [['You want maximum optionality and will genuinely tolerate the hours','<b>Investment Banking</b>','Broadest exits in finance. Only worth it if the hours are a price you have actually considered, not one you have imagined.'],
         ['You think fast, like being wrong quickly, and follow markets','<b>Global Markets</b> or <b>Sales</b>','Screens for decisiveness and numeracy over polish. Read both postings — they are separate applications.'],
         ['You are strongly mathematical with real programming ability','<b>Quantitative Research</b>','Remember it is off-cycle in London, so the timeline differs from your peers.'],
         ['You write well and think independently','<b>Research</b>','Rare skill, smaller intake, and a live regulatory story to discuss.'],
         ['You are commercially minded but not a modelling obsessive','<b>Payments</b>','Enormous business, far less competition, real product careers. The best value-for-effort application here.'],
         ['You care about investing itself','<b>Asset Management Investments</b>','Highest-return segment in the firm and a better lifestyle.'],
         ['You are personable and interested in people\'s wealth','<b>Global Private Bank</b>','They are expanding advisors 9% a year.'],
         ['You can code','<b>Software Engineering</b> or <b>Data &amp; AI</b>','Least competitive relative to intake, best external optionality. Check the sponsorship clause.'],
         ['You are interested in fintech and product','<b>Chase Digital Development Programme</b>','The only true product-management graduate route, and Chase UK is the most interesting strategic story in JPMorgan\'s UK business.'],
         ['You like structure, analysis and process','<b>CADP</b> or <b>GF&amp;BM</b>','Genuinely good programmes — but only if you want them, not as a fallback.'],
        ], widths=[1.5,0.85,2.6], small=True))
    A(callout('On applying to several: what is coherent and what is not',
        '<b>Coherent pairs.</b> Investment Banking + Global Corporate Banking. Global Markets + Sales. Markets + Quantitative Research '
        '(if genuinely mathematical). Asset Management + Global Private Bank. Software Engineering + Data &amp; AI. Payments + '
        'Securities Services. In each case one story explains both.<br/><br/>'
        '<b>Incoherent.</b> Investment Banking + Software Engineering. Private Bank + Quantitative Research. Anything + everything.<br/><br/>'
        '<b>The blunt version:</b> recruiters can see your applications. Applying to six unrelated programmes does not multiply your '
        'chances; it tells them you have no idea what you want, and the interviewer\'s first question — "why this team?" — becomes '
        'unanswerable. Two well-argued applications beat six scattered ones. If you cannot write a paragraph explaining why a programme '
        'follows from what you have already done, do not apply to it.', 'warn'))
    return F
