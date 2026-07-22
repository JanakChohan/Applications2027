# Target List — Summary

**Scoping date:** 2026-07-22 · **Status:** Research complete (single pass)
**Interactive viewer:** https://claude.ai/code/artifact/8f92139d-238f-4046-8f52-0e0456504f8e
**Data file:** `targets.csv` (237 rows) · **Log:** `progress.log`

---

## Headline numbers (honest)

- **173 unique firms**, **237 contact rows** (a firm with 2–3 named seniors = 2–3 rows).
- Against the target of **400 firms (~200 per geography)** this is a **genuine shortfall** — see "Did the geographies run dry?" below. I did **not** pad the list to hit the number, and no firm, name, or email was invented.
- **South Essex: 106 firms / 146 rows.** **Norwich & Norfolk: 67 firms / 91 rows.**
- **0 S-tier firms found anywhere.** Boutique investment banks, PE, VC, hedge funds and prop-trading houses simply do not have a registered-office presence in either region — they cluster in the City, Canary Wharf and Cambridge. This was confirmed independently by all ten research agents. The nearest thing is **Barratt & Cooke** (Norwich), a genuine independent stockbroker/investment manager (est. 1880), classed A.

### By tier (firms)

| Tier | Firms | Rows | What it is |
|------|-------|------|-----------|
| **S** | **0** | 0 | boutique IB / corporate finance / PE / VC / hedge / prop — none exist regionally |
| **A** | 69 | 91 | wealth management, IFAs/financial planning, investment mgmt, corp-finance arms |
| **B** | 100 | 141 | accountancy, audit/tax, insurance brokers/underwriters, commercial-finance brokers, fintech |
| **C** | 4 | 5 | professional services w/ a finance function (Norwich corporate-law firms only) |

### By tier × geography (firms)

| Tier | South Essex | Norwich/Norfolk |
|------|:-----------:|:---------------:|
| S | 0 | 0 |
| A | 40 | 29 |
| B | 66 | 34 |
| C | 0 | 4 |

### By search radius (firms) — recorded in the `geography` column

| Radius | Firms |
|--------|:-----:|
| Norwich (wider Norfolk) — Yarmouth, Dereham, King's Lynn, Attleborough, Diss, Wymondham, N. Walsham | 34 |
| South Essex (Southend core) — SS0–SS3, SS9 | 28 |
| South Essex (Basildon/Brentwood belt) — SS14–16, CM11–15 | 26 |
| South Essex (Rochford/Rayleigh belt) — SS4–8, SS11–13 | 23 |
| Norwich (city centre) — NR1–3 | 23 |
| South Essex (Chelmsford) — CM0–3 | 17 |
| South Essex (Grays/Thurrock) — RM16–20, SS17 | 11 |
| Norwich (wider ring) — NR4–8, NR13–14 | 10 |
| City/Canary Wharf (firm with an explicit Essex office) | 1 |

---

## Contact & email quality

- **208 of 237 rows carry a named senior contact** (Partner / MD / Director / Head of / Founder). The 29 blanks are firms where no senior name was published on the site *and* none was safely attributable from Companies House — left blank rather than guessed.
- **Email confidence (rows):** 37 published · 4 inferred · 84 generic inbox · **112 blank**.
  - Blank dominates because many small practices publish only a shared `info@`/`enquiries@` inbox, or nothing. Where only a generic inbox existed I recorded it as `generic`; where I couldn't verify even that, the cell is blank.
  - Only 4 emails are **inferred** (from a visible published pattern on the same domain) — each records the pattern used in the `personalisation_hook` cell, e.g. `[email pattern: firstname.lastname@ibawm.co.uk]`.
- **234 of 237 rows have a real personalisation hook** (a verifiable sector focus, deal, founding date, or named specialism). The rest are blank, not filler.
- **`careers_portal` = "no" for all 237 rows** — that was the whole selection criterion. Any firm found running Workday/Greenhouse/etc. was excluded (see below).

## Which sources produced the most firms

1. **Companies House advanced search** (by postcode district × SIC code) was the backbone — the highest-yield way to enumerate real firms with a company number and registered address, and the source of record for **60 contact rows** (officer filings) plus most of the initial firm discovery. It's also where the bulk of noise lived: a large majority of hits under the finance SIC codes are one-person contractor/accountant shells at residential addresses, which were skipped.
2. **Firm websites' "Meet the Team" / "Our People" pages** — the source for most named seniors and every published personal email (177 rows sourced to firm sites / directories).
3. **Web search** with varied local queries ("chartered accountants <town>", "wealth management <town>", "insurance brokers <town>", etc.) — best for discovering trading names that don't surface cleanly in Companies House.
4. **FCA-adjacent / directory corroboration** (ICAEW firm finder, financialadvisers.co.uk, St. James's Place partner pages) — used mainly to confirm firms whose own sites returned anti-bot 403/503 errors.

A recurring friction: **many genuine firm sites return 403/503 to automated fetchers** (bot protection). Where that happened, the firm was kept **only** if its existence and directors were corroborated via Companies House/ICAEW, and the caveat is noted in the row's hook. Firms that could be neither rendered nor corroborated were dropped.

## Did the geographies run dry? (why 173, not 400)

**Yes — both did, at this quality bar, well before 200 each.** The 400 target assumes a density of independent finance firms that these two regions don't contain once you strictly exclude (a) the Big 4 and large regional consolidators, (b) anything running a graduate ATS, and (c) one-person shells with no real website or team.

- **South Essex (106 firms):** All the named towns were swept, including a deliberate second-pass sweep for firms the first pass missed. Genuine independent finance firms thin out fast outside accountancy, IFAs and insurance broking. Shoeburyness (SS3) and much of Grays/Thurrock returned almost nothing but sole traders.
- **Norwich/Norfolk (67 firms):** Norwich city centre and the wider ring are covered; wider Norfolk (Yarmouth, King's Lynn, Dereham, Diss, Attleborough) was opened up and added 34 firms, but these are rural market towns where the finance sector is small.
- **The binding constraint is S-tier and A-tier density, not effort.** You could push the totals higher only by (a) adding more micro accountancy practices (diminishing quality), or (b) expanding C-tier into solicitors, commercial property, corporate-services firms — which your brief reserves for a geography that has run dry. I included **4 C-tier corporate-law firms in Norwich** as a marker of that boundary; I did not roll C-tier out across the board.

**To get materially closer to 400 would mean relaxing a rule** — e.g. include large regional firms with grad schemes, include SJP/national-network appointed representatives more liberally, or fold in C-tier professional services (solicitors, corporate-services, commercial property) across both regions. Happy to do any of these on your say-so; I held the line on the strict brief instead of padding.

---

## Firms found but EXCLUDED (with reasons)

### Excluded by rule — Big 4 / large regional / national consolidators
Deloitte, PwC, EY, KPMG, Grant Thornton, BDO, RSM, Mazars — none have qualifying local offices anyway. Plus, found locally and excluded:
- **Azets**, **Xeinadin** (offices in Southend, Billericay, Chelmsford, Norwich) — named exclusions / consolidators.
- **Rickard Luckin** (Southend, Leigh, Basildon, Chelmsford) — ~200+ staff regional firm running a formal student/graduate scheme; its corporate-finance arm is **Attain Corporate Finance**.
- **Affinia / LB Group** (Chelmsford) — Top-40 consolidated firm.
- **THP**, **Haslers** (Loughton), **Perspective**, **Amber River**, **Progeny**, **Fairstone** (Essex) — national/large with formal recruitment.
- **FRP Advisory** (Leigh-on-Sea, Norwich) — national AIM-listed; absorbed Norwich CF house **JDC**.
- **Larking Gowen**, **Lovewell Blake**, **Price Bailey**, **Ensors**, **Scrutton Bland**, **TC Group / TC Farnell Clarke** (Norwich/Norfolk) — large regional firms with grad schemes. Scrutton Bland's 2025 acquisition of **Argents** took Argents out of scope too.
- **Alan Boswell Group** (Norwich, 500+ staff), **Jensten (East)**, **Towergate**, **Adrian Flux** — large brokers with group ATS.

### Excluded — runs a graduate/careers ATS
- **Handelsbanken** (Chelmsford branch) — a genuinely attractive decentralised commercial-banking target, but recruitment runs through a corporate ATS and no senior branch contact is published on a first-party source. Flagged as worth a **direct paper letter to the branch's Corporate Banking Manager** if you want to pursue it off-list.
- **Moneyfacts Group** (Norwich fintech, ~150–200 staff) — likely formal ATS; left out.

### Dropped — not genuinely in-geography (SEO "location pages", real office elsewhere)
Haslers (Loughton IG10), Ascott Blake (Bishop's Stortford CM23), ABM (Canary Wharf E14), Paul Dodd Asset Management (Leeds LS16), Prescient Accounting (Romsey), Berry Wealth (Market Harborough), Quilliam Marr (Birmingham), Brayan & Spencer (Borehamwood), Otium Partners (Somerset), Essex & Suffolk Insurance (Colchester CO4), Turner Pope Investments (Mayfair HQ; only its *registered* office is in Brentwood), Anglia Capital Group (Cromer NR27), plus several holding-company shells at formation-agent addresses.

### Dropped — dissolved, acquired into an excluded group, or a national-network AR treated conservatively
- **Dissolved:** Vector Capital Finance, Coast Underwriting, R&R Insurance Brokers, Essex Commercial Finance, Welcome Wealth Management, Simply Wealth & Protection, ES Insurance Consultants.
- **Acquired into a larger group:** Spencer Fellows (→ Buckley Watson), J M Wakeling (→ Amber River), Waveney Valley IFA (→ Beckett), Priory Insurance (→ Alan Boswell), Face to Face Finance (→ MKC Wealth), Lucas Fettes (→ Brooks Macdonald), Finance Shop / The Private Office (→ Titan Wealth).
- Numerous **St. James's Place / Openwork / national-network appointed representatives** were treated case-by-case: tiny genuinely-local one/two-adviser SJP practices were **kept** (labelled "SJP"/"AR" in the sub-sector) as legitimate small speculative targets; ones that were really a national brand's outpost were dropped.

### Dropped — could not verify a live website OR a named senior (blank > wrong)
Belmore Wood, Baylon Philips, Caledon MGA, Cooper/Oak Tree/GP Financial Planning (NR7), Tubbs Son Giles, Miura Financial (Hadleigh), Orbit Financial, Ratcliff, Wiseman, Sand Financial, Brookfield Donovan, Money Balance, Torus Risk Partners, Draper Webb Chandler, Fenchurch IFP, Olympia Finance, Holloway Davies, Laura Shaw FP, plus many one-person accountancy shells at residential addresses across all districts.

---

## Caveats to act on before you send

1. **Verify the contact is still there.** Regional firms change staff often; a name from a 2024–25 team page or a Companies House filing may have moved. A 30-second check on the firm's current team page before sending is worth it.
2. **`inferred` emails are educated guesses** from a visible pattern — expect the occasional bounce. `generic` inboxes reach the firm but not a named person; open with "FAO <name>".
3. **Anti-bot flagged rows** (noted in the hook, e.g. Edmund Carr, Mayor Cuttle, Shirley Smith, several Norfolk firms): the firm and directors are corroborated via Companies House, but I couldn't render the live site this session — sanity-check the URL loads for you.
4. **Same firm, multiple offices** are listed as separate labelled rows (e.g. *M+A Partners* Norwich vs Attleborough; *Stephenson Smart* Gorleston vs King's Lynn; *Sterling & Law* Brentwood/Billericay/Rayleigh/Chelmsford). Dedupe to one approach per firm if you'd rather not double-contact.
5. **Almary Green ≈ Smith & Pinching** (same Norwich address & MD Carl Lamb) — treat as one approach.
