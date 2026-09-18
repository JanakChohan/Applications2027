# The two application questions — research pack

Research for the written answers on the Fidelity International Investment Directing
Summer Internship 2027 application form. Compiled 18 September 2026.

**There is no drafted answer in here, deliberately.** Fidelity publishes a Candidates AI Code of
Conduct which permits AI for grammar and structure, requires disclosure for "written responses for
non-timed tasks where originality, reasoning or reflection is assessed", and prohibits "submitting
AI-generated content as your own where authenticity, judgement or personal capability is being
assessed". These two questions fall squarely in the middle category. See Part 1.4.

## The questions

1. *(200 words)* A theme, article or news story learned recently; why it is relevant to an investor
   in the investment management industry; and how you would explain it to a client without a
   financial background.
2. *(150 words)* £1m windfall — how to invest it short term and long term, with the asset allocation
   appropriate to each horizon.

## Files

| File | What it is |
|---|---|
| `Fidelity_Application_Questions_Research_Pack.pdf` | 33 pages, 8 diagrams, 72 sourced references. |
| `…_Research_Pack.html` | HTML source. |
| `research/` | Six raw workstream files with their own source tables and gaps. |
| `src/` | HTML chunks, the two-pass renderer, and the source-table generator. |

## What the research established

- **The Blue Owl story, to primary sources.** Q1 2026 redemption requests of 21.9% of NAV at the
  flagship credit fund and 40.7% at the technology fund, both capped at 5%. Verified against SEC
  8-K filings, including which fund actually used the "AI-related disruption to software companies"
  wording — press coverage routinely attributes it to the wrong one.
- **The analytical finding worth building an answer on:** the redemption wave ran far ahead of the
  credit data. Software multiples collapsed, but private credit default indices moved only from
  1.84% to 2.51% across four quarters. Investors ran from the fear, not the losses.
- **The Fidelity link, with its counter-case.** Fidelity's LTAF sits in a workplace pension default,
  but it has a 90-day regulatory notice floor, a programmatic investor base, and it largely selects
  third-party managers rather than originating loans. Structurally more robust than the US vehicles.
- **Question 2's best angles**, including the FSCS deposit limit of £120,000 (so £1m in one bank
  leaves ~£880,000 uninsured) and the CGT exemption on directly held gilts.

## Rebuilding

```
python3 src/mksources.py && python3 src/render.py
```
