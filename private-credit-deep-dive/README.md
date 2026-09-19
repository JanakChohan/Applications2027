# Private credit — a deep dive from zero

A 49-page explainer on private credit as an asset class, written for someone starting from no
knowledge. Compiled 19 September 2026 from public sources. 14 diagrams, 77 sourced references,
78-term glossary.

Built to support saying "I want to be a client portfolio manager for private credit" and then
defending it for an hour.

## Contents

| Part | Covers |
|---|---|
| 0 | The ten things that actually matter |
| 1 | What private credit is — debt vs equity, and the four things that make a loan "private" |
| 2 | Where it came from: the BDC in 1980, Basel III, the 2013 leveraged lending guidance and its 2025 withdrawal, and why market-size estimates differ twofold |
| 3 | The strategy map: direct lending, unitranche, mezzanine, distressed, asset-based finance, NAV lending, SRT |
| 4 | How a deal works: the capital structure, unitranche mechanics, pricing, covenants, EBITDA add-backs, PIK |
| 5 | Follow the money: real BDC fee terms, the return bridge, returns, defaults, recoveries, valuation |
| 6 | Why it works for investors, borrowers and the firms lending |
| 7 | The players, and why Fidelity International is an allocator rather than an originator |
| 8 | Trends: insurance convergence, bank partnerships, retailisation, asset-based finance |
| 9 | The bear case, the regulators, and three real failures |
| 10 | Forming your own view: five contested questions |
| 11 | The job, and 15 questions that test real understanding |
| 12–14 | Glossary, source table, gaps |

## Some things the research established

- **A loan to Lithium Technologies was marked at 50, 53 and 77 cents by three different BDCs in the
  same quarter.** The clearest possible evidence that NAV in private credit is an opinion.
- **US Federal Reserve research put private credit recovery at 33%, below syndicated loans at 52%.**
  This complicates the standard "senior secured" pitch and deserves more attention than it gets.
- **The 2013 leveraged lending guidance that helped create the market was withdrawn in December 2025**
  as "overly restrictive".
- **Partners Group calculates a closed-end fund needs roughly a 20% IRR to match an evergreen fund
  delivering 11%**, once the drag of uncalled capital is counted. The best single number for why
  institutions are moving into evergreen vehicles.
- The industry's defence rests on capital being locked up. Its growth came from vehicles where it
  is not. That tension is the through-line of the whole document.

## Health warnings

Private credit is badly served by data. Market size, default rates and recovery rates all vary by
provider, honestly, because they measure different things. Every figure names its source and carries
a confidence tag. Part 14 lists what could not be established, including that the Financial Times
article behind the institutional-into-evergreen story was unreachable, so the claim that USS
specifically is involved is **unverified**.

## Rebuilding

```
python3 src/mksources.py && python3 src/render.py
```
