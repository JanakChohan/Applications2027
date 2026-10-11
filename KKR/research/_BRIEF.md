# Shared research brief (read this first)

Today is 2026-10-11. Your training knowledge may stop around mid-2026, so anything about 2026 must be checked live on the web. Use WebSearch and WebFetch (load them with ToolSearch "select:WebSearch,WebFetch" if they are not already loaded). If WebFetch is blocked on a site, try curl through the configured proxy (`curl -sSL --max-time 30 -A "Mozilla/5.0" URL`), then strip HTML with python. Never disable TLS verification.

## The candidate and the target
- Candidate: UK undergraduate applying to the **KKR London 2027 Summer Internship** (6 Jun to 29 Jul 2027) via **SEO London** (Alternative Investments programme). Applications close **18 Oct 2026**. Candidate ranks 6 teams in order of preference: Private Equity (incl. Global Impact, off-cycle), Real Estate, Infrastructure, Capital Markets (KCM), Client Solutions (KCS), Capstone.
- Candidate's first choice: **KKR Global Client Solutions ("KCS")** in London. Knowledge level of the industry: close to zero. Visual learner.
- The official KCS team description from KKR (verbatim): "KKR's Global Client Solutions ("KCS") consists of experienced professionals with diverse backgrounds dedicated to developing and servicing KKR's global network of investors and clients. Relationship managers in direct outreach to clients; Product specialists providing specific support and expertise; Junior resources serving in a generalist capacity; Relationship-focused, solutions-oriented approach, able to deliver customized products. Primary Activities: Facilitate client access to products and services across KKR's platform; Apply integrated approach by leveraging all KKR executives and capabilities globally; Work in partnership with Capital Markets in the syndication/distribution of product."
- KKR's own internship text says interns are "encouraged to leverage KKR's approved AI tools".

## Hard rules
1. Never fabricate. No invented figures, names, quotes, deals. If you cannot find it, say so in Gaps.
2. Every non-obvious claim gets a source ID from YOUR assigned range, and a confidence tag: [Confirmed] (primary source or two credible outlets), [Reported] (single credible source), [Inferred] (your reasoning).
3. Prefer primary sources: kkr.com (incl. investor relations, press releases, Insights, 10-K / 10-Q / 8-K / investor day decks on SEC EDGAR and ir.kkr.com), KKR careers (KKR uses Workday: try https://kkr.wd1.myworkdayjobs.com/ and its JSON endpoint `https://kkr.wd1.myworkdayjobs.com/wday/cxs/kkr/KKR_Careers/jobs` via POST with {"appliedFacets":{},"limit":20,"offset":0,"searchText":"London"} — check the exact site name), FCA Register (KKR's UK entity is believed to be Kohlberg Kravis Roberts & Co. Partners LLP — verify), Companies House, SEC Form ADV, regulators, trade bodies. Then quality press (FT, Bloomberg, Reuters, WSJ, PEI, Private Equity International, Institutional Investor, Pensions & Investments, Citywire, Financial News, eFinancialCareers).
4. Paywalls: never guess unread content. Record headline, outlet, date, URL and mark PAYWALLED-NOT-READ, then look for a non-paywalled summary.
5. People: strictly public professional info (role, employer, tenure, career path, education, public talks/writing). Nothing personal. Flag identity uncertainty.
6. At least 12 distinct search queries and 8 full-page fetches. Snippets alone are not enough for key facts.
7. Plain English. No em dashes. Short sentences.

## Output: write ONE markdown file at the path you are given, with exactly these six sections
1. **Findings** (detailed, organised by sub-topic, each claim with [Sxx] and confidence tag; be generous with detail: this feeds a 100-page report written for a total beginner)
2. **Key numbers table** (metric | value | as-of date | source | confidence)
3. **Verbatim quotes actually read** (quote | speaker/document | date | [Sxx])
4. **Source table**, one row per source: `[Sxx] | Outlet | Title | Pub date | URL | Accessed 2026-10-xx | FETCHED/SNIPPET/PAYWALLED | confidence note`
5. **Gaps** (what you could not establish)
6. **Interview angles** (how a candidate could use these facts; opinions they could form; smart questions)

Your final message back should be a short summary (under 300 words) of the most important findings and the file path. The file is what matters.
