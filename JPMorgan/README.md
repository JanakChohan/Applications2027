# J.P. Morgan Global Private Bank, 2027 London Summer Internship

- `JPMorgan_Private_Bank_2027_London_Internship_Guide.pdf` - volume 1: the firm, the roles, and the Oracle/pymetrics/HireVue screening pipeline (26 pages).
- `JPMorgan_Deep_Dive_Strategy_Competitors_Roles.pdf` - volume 2: five years of 10-Ks, Investor Days and shareholder letters; competitor benchmarking; the Private Bank organisation and the two seats in depth (32 pages).
- `JPMorgan_How_The_Firm_Thinks_Culture_and_Structure.pdf` - volume 3: the beliefs at the top, the episodes that show them (crisis weekends, the London Whale, the 2015 conflicts order, return-to-office), and how those beliefs explain the Private Bank's structure (22 pages).
- `deepdive_source.html`, `culture_source.html` and `parts/` - editable sources for volumes 2 and 3 (parts are concatenated into the source files).
- `guide_source.html` - editable source with inline SVG diagrams.
- `build_pdf.js` - renders the HTML to PDF with headless Chromium via Playwright.

Rebuild volume 1: `node build_pdf.js`. Rebuild volume 3: `node build_pdf.js culture_source.html JPMorgan_How_The_Firm_Thinks_Culture_and_Structure.pdf "How J.P. Morgan Thinks: Culture, Stories and Why It Is Built the Way It Is"`. Rebuild volume 2: `node build_pdf.js deepdive_source.html JPMorgan_Deep_Dive_Strategy_Competitors_Roles.pdf "J.P. Morgan Deep Dive: Strategy, Competitors and the Private Bank Seats"` (set `PLAYWRIGHT_MODULE` to a global playwright install path if it is not in `node_modules`).

Roles covered: Advisor track (req. 210773470) and Investment Solutions track (req. 210774281). Both postings state a 1 November 2026 deadline and rolling review.
