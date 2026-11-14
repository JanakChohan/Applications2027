# Project conventions (source of truth for every contributor and build step)

Research date and information cutoff: **14 November 2026**. Nothing published after that date may be used.

## Directory layout

| Path | Purpose |
|---|---|
| `research/evidence/<STREAM>.md` | Narrative research notes for one stream: findings, exact supporting passages, open questions, search log |
| `data/sources/<STREAM>.json` | Source register fragment for the stream |
| `data/claims/<STREAM>.json` | Claim register fragment (one row per material claim) |
| `data/fragments/<type>.<STREAM>.json` | Entity fragments: `people`, `mandates`, `teams`, `developments`, `competitors`, `glossary` |
| `data/*.json` | Canonical merged/curated data used by the HTML app and PDF |
| `content/chapters/NN-slug.md` | Dossier chapters (prose) |
| `build/` | Build scripts. `python3 build/build.py` regenerates dossier, HTML and PDF |

## Evidence status vocabulary (use exactly these strings)

`Verified` · `Supported inference` · `Unverified account` · `Illustrative example` · `Conflicting evidence` · `Not publicly established`

- **Verified** only when the supporting passage was actually read on a primary or credible source page (page fetched, or the passage is quoted verbatim in the search result from that source). One AI draft, the former intern's call, or several articles re-reporting one press release do not corroborate each other.
- Search-snippet-only knowledge: record the source with `"fetched": false` and do not go above `Supported inference` unless the snippet is a verbatim passage from the primary source.
- Anything known only from the call with the former intern is `Unverified account`.
- Never fill a gap with an estimate. Write `null` in data and "Not publicly disclosed" in prose.

## JSON schemas

### `data/sources/<STREAM>.json` — array
```json
{"id":"R3-S01","title":"","publisher":"","url":"","published":"YYYY-MM-DD|YYYY-MM|YYYY|null","accessed":"2026-11-14",
 "type":"official_gs|filing|regulator|government|client_official|trade_press|news|profile|jobs_board|industry_body|other",
 "fetched":true,"note":"what this source establishes; period the figures describe if different from publication date"}
```
### `data/claims/<STREAM>.json` — array
```json
{"id":"R3-C01","topic":"short topic key","claim":"one sentence","status":"Verified","sources":["R3-S01"],
 "passage":"short verbatim supporting passage (<=30 words) or precise reference (page/section)","event_date":"","period":"","layer":"A|B","notes":"limits, conflicts, what it does NOT establish"}
```
### `data/fragments/people.<STREAM>.json` — array
```json
{"id":"P-R6-01","name":"","title_public":"exact public title","title_class":"Partner|Managing Director|Executive Director/Vice President|Associate|Analyst|Intern|Unclear",
 "office":"","coverage":"client geography or 'Unclear'","segment":"Institutional|Third Party Wealth|OCIO/Fiduciary|Insurance|Liquidity|Consultant Relations|Multiple|Unclear",
 "function_interpretation":"Sales|Relationship management|Both/blended|Leadership|Product/Investment specialist|Unclear","function_basis":"why you classified it so",
 "career_history":"brief, public only","evidence_date":"date the title was observed as current","current_as_of_cutoff":"Yes|Likely|Unknown|No (left/moved)",
 "sources":["R6-S01"],"confidence":"High|Medium|Low","notes":""}
```
Public professional information only. No contact details, no personal characteristics, no inference of language/nationality from names.
### `data/fragments/mandates.<STREAM>.json` — array
```json
{"id":"M-R7-01","client":"","client_type":"","country":"","date":"event date","kind":"Awarded mandate|OCIO appointment|Expansion|Renewal|Loss/termination|Distribution agreement|Product launch|Fund commitment|Fundraising target|Acquisition/partnership",
 "strategy":"","amount":"as disclosed, with currency, or null","amount_basis":"e.g. scheme assets at announcement; NOT fee-paying AUM unless stated","rationale":"as publicly stated","consultant":"or null","decision_makers":"or null",
 "gs_team_attribution":"what is publicly stated about which GS team/people; 'Not publicly established' otherwise","status":"Verified","sources":["R7-S01"],"notes":""}
```
### `data/fragments/developments.<STREAM>.json` — array (commercial-awareness items)
```json
{"id":"D-R3-01","title":"","teams":["UK Institutional","OCIO","Third Party Wealth","Insurance","Liquidity Solutions","Middle East","Nordics","Switzerland","Benelux","All"],
 "event_date":"","publication_date":"","what_happened":"","client_effect":"","decision_that_changes":"","existing_investments":"","possible_gsam_response":"(Layer B, not a GS statement)",
 "sales_angle":"","rm_angle":"","risks_counterarguments":"","client_question":"a question you could ask a client","watch":"indicators","status":"Verified","sources":[]}
```
### `data/fragments/teams.<STREAM>.json` — array (candidate team facts)
```json
{"id":"T-R5-01","name_public":"name as publicly used, or null","name_reported":"former intern's label if different","kind":"Regional coverage|Client segment|Product line|Function",
 "covers":"","office_evidence":"which offices, with source","clients":"","products":"","languages_evidence":"from job descriptions only","recruitment_evidence":"","relations":[{"type":"Reports to|Covers clients in|Works with|Distributes products for","target":"","status":"Verified","sources":[]}],
 "status":"Verified","sources":[],"notes":""}
```

## Chapter Markdown conventions (`content/chapters/*.md`)

- One `#` title, then `##` sections and `###` subsections. UK English. Plain language first.
- **Citations**: `[@R3-S01]` immediately after the supported statement. IDs must exist in a sources fragment.
- **Evidence badges** inline: `{{V}}` Verified, `{{SI}}` Supported inference, `{{UA}}` Unverified account, `{{IL}}` Illustrative example, `{{CE}}` Conflicting evidence, `{{NPE}}` Not publicly established.
- **Layer labels** at the start of a paragraph or block when it matters: `{{L:A}}` verified business/role fact, `{{L:B}}` commercial interpretation, `{{L:C}}` personal fit.
- **Teaching levels** (fenced containers, closing line is `:::` alone):
  - `:::l1` … `:::` Level 1, first-principles foundation
  - `:::l2` … `:::` Level 2, institutional mechanics
  - Text outside containers shows in both views. Caveats and uncertainty must sit outside `l2` so the beginner view never hides them.
- **Callouts**: `:::note`, `:::warn` (limits and caveats), `:::example` (illustrative, always labelled), `:::workproduct` (sample work product), `:::dialogue` (realistic conversation), `:::check` (self-test questions). Optional title on the opening line, e.g. `:::example A £500m mandate`.
- Tables: GitHub pipe tables. Keep to 5 columns or fewer so they print.
- Define every acronym at first use in the chapter and make sure it has a `glossary` entry.
- Illustrative figures are always tagged `{{IL}}`. Never present an illustrative fee as Goldman Sachs's actual fee.
- Do not name the two companies the former intern called confidential clients unless `data/claims` holds a `Verified` public source for the relationship.
- No candidate identifiers, interview links, phone numbers or email addresses anywhere.

## Glossary fragment (`data/fragments/glossary.<STREAM>.json`) — array
```json
{"id":"G-aus","term":"AUS","expansion":"Assets under supervision","plain":"one-sentence plain-English definition","technical":"mechanics, 1-3 sentences","why_it_matters":"for this role","see":["G-aum"],"sources":[]}
```
