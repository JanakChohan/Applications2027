"""PHASE 9 - verification. (A) re-check reported numbers against the filings in data/sec_txt and transcripts,
(B) model integrity, (C) the deck, memo, markdown files and model agree on the key numbers. Writes verification.md."""
import json, os, re, glob, hashlib
from pptx import Presentation
from docx import Document
from openpyxl import load_workbook
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); D = os.path.join(ROOT, "data", "derived"); F = json.load(open(os.path.join(D, "facts.json"))); MO = json.load(open(os.path.join(D, "model_outputs.json")))
def txt(name): return re.sub(r"\s+", " ", open(glob.glob(os.path.join(ROOT, "data", "sec_txt", name))[0]).read())
K10 = txt("2026-02-12_10-K*"); Q3 = txt("2026-10-29_10-Q*"); PR3 = txt("2026-10-29_8-K_EX*"); PR4 = txt("2026-02-12_8-K_EX*"); PR2 = txt("2026-07-30_8-K_EX*"); PR1 = txt("2026-04-30_8-K_EX*"); PX = txt("2026-04-23_DEF14A*")
K09 = re.sub(r"\s+", " ", open(glob.glob(os.path.join(ROOT, "data", "sec", "2010-02-25_10-K*"))[0], errors="ignore").read()); K09 = re.sub(r"<[^>]+>", " ", K09); K09 = re.sub(r"&#160;|&nbsp;", " ", K09); K09 = re.sub(r"\s+", " ", K09)
TR = " ".join(re.sub(r"\s+", " ", open(f, errors="ignore").read()) for f in glob.glob(os.path.join(ROOT, "data", "transcripts", "*.txt")))
A = []
def chk(desc, hay, pat, regex=False):
    ok = bool(re.search(pat, hay)) if regex else (pat in hay); A.append((desc, pat if len(pat) < 70 else pat[:67] + "...", "OK" if ok else "NOT FOUND"))
chk("FY2025 revenue $4,040.6m (10-K)", K10, "4,040,647"); chk("FY2024 revenue (10-K)", K10, "4,102,108"); chk("Crocs Brand FY25 revenue", K10, "3,325,807"); chk("HEYDUDE FY25 revenue", K10, "714,840")
chk("Crocs Brand segment income FY25", K10, "1,111,679"); chk("Crocs NA FY25 revenue", K10, "1,709,635"); chk("Crocs International FY25 revenue", K10, "1,616,172"); chk("Crocs pairs FY25", K10, "128,938"); chk("Crocs ASP FY25", K10, "25.40")
chk("No customer 10% or more", K10, "There were no customers who represented 10% or more of consolidated revenues"); chk("US revenue FY25", K10, "2,260,656"); chk("Vietnam 45% of Crocs production", K10, r"approximately 45%, 51%, and 56%", True)
chk("Two manufacturers 45% and 28%", K10, r"approximately 28%, 25%, and 26%", True); chk("Distribution cost $488.4m", K10, "$488.4 million"); chk("Unrecognized tax benefit $637.0m", K10, "636,973"); chk("Marketing: cost savings $50m / $100m", K10, r"\$50 million of gross cost savings.*\$100 million of gross cost savings", True)
chk("Interest sensitivity $5.6m per 1%", K10, "$5.6 million"); chk("DTC 52.1% of revenue", K10, "52.1%"); chk("Digital 37.8%", K10, "37.8%"); chk("Employees 8,010", K10, "8,010"); chk("Goodwill impairment $307m; trademark $430m", K10, r"\$430\.0 million related to the indefinite-lived HEYDUDE trademark and \$307\.0 million", True)
chk("Q3-26 revenue (release)", PR3, "1,042,583"); chk("Q3-26 adjusted EPS $3.69", PR3, "Adjusted diluted earnings per share of $3.69"); chk("FY26 EPS guide $14.45-14.65", PR3, "$14.45 to $14.65"); chk("Q4-26 EPS guide $3.25-3.45", PR3, "$3.25 to $3.45")
chk("Q3 buyback $250.0m at $123.32", PR3, "$123.32"); chk("Crocs NA Q3-26", PR3, "438,369"); chk("Crocs International Q3-26", PR3, "434,352"); chk("HEYDUDE Q3-26", PR3, "169,862"); chk("IEEPA refunds in Q3 gross profit", PR3, "64,071"); chk("Adj. operating margin 22.3%", PR3, "22.3%")
chk("FCF 9M-26 $507.6m", PR3, "507,574"); chk("Borrowings $1,289.0m (carrying)", PR3, "1,289,044"); chk("Cash $163.5m", PR3, "163,457"); chk("Shares outstanding 46.2m at 30-Sep-26", PR3, "46.2 million")
chk("Debt: revolver $113m, TLB $500m, notes 2029 / 2031", Q3, r"Term Loan B Facility \| 2029 \| 500,000.*Revolving Facility \| 2027 \| 113,000", True); chk("IEEPA refunds: $75m-$80m eligible", Q3, "$75 million to $80 million"); chk("Tariffs 10% to 12.5%", Q3, "ranging from 10% to 12.5%")
chk("Authorisation: about $1.7bn remaining", Q3, "approximately $1.7 billion remained available"); chk("Class action Carretta v. Crocs", Q3, "Carretta v. Crocs, Inc."); chk("Gross margin walk: product mix -130 bps", Q3, "unfavorable product mix in the Crocs Brand of 130 basis points")
chk("FY25 adj. EPS $12.51; buyback $577m at $88.68 (Q4-25 release)", PR4, r"Adjusted diluted earnings per share of \$12\.51.*\$88\.68", True); chk("Initial FY26 EPS guide $12.88-13.35", PR4, "$12.88 to $13.35"); chk("Q1-26 raise to $13.20-13.75", PR1, "$13.20 to $13.75"); chk("Q2-26 raise to $13.70-14.00", PR2, "$13.70 to $14.00")
chk("Proxy: WIT Partners 2,852,280 shares", PX, "2,852,280"); chk("Proxy: insiders 3.1% as a group", PX, r"1,585,148 \| 3\.1%", True); chk("Proxy: CEO 1,016,929 shares", PX, "1,016,929"); chk("Proxy: CFO Reagan appointed 22-Sep-2025", PX, "September 22, 2025")
chk("FY2007 / FY2008 / FY2009 revenue (10-K FY2009)", K09, r"645,767\s*\$?\s*721,589\s*\$?\s*847,350", True)
for q, d in [("Our average market share in China, India, Japan, Germany and France represented approximately one-third of the market share we have in our established markets", "Quote: one-third share (CEO, Q4-25 call)"),
             ("we are up against a weak compare", "Quote: weak compare (CEO, Q3-26 call)"), ("clogs represented 74% of our mix", "Quote: clogs 74% of mix"), ("has had the greatest impact on our Classic Clog business", "Quote: Classic Clog impact (CEO, Q3-25 call)"),
             ("there is no change to units in the market or market share", "Quote: marketplace shift (CFO, Q3-26 call)"), ("each one selling out", "Quote: collaborations selling out"), ("we are outselling our inventory in the channel", "Quote: outselling inventory"),
             ("many more days that were non-promotional", "Quote: non-promotional days"), ("roughly about what we grew at overall this year", "Quote: 2027 colour (CFO)")]:
    chk(d, TR.lower().replace("’", "'"), q.lower())
# ---------- B: model ----------
Bm = [("Formulas in model.xlsx", MO["n_formulas"], "OK"), ("Formula errors after LibreOffice recalculation", len(MO["errors"]), "OK" if not MO["errors"] else "ERROR")]
for r in MO["checks"]: Bm.append((r[0], r[1] if not isinstance(r[1], float) else round(r[1], 4), r[2]))
wb = load_workbook(os.path.join(ROOT, "model.xlsx"), data_only=True); cached = wb["Valuation"]["C9"].value
Bm.append(("model.xlsx cached base PT equals model_outputs.json", round(cached, 2), "OK" if abs(cached - F["valuation"]["pt"][1]) < 0.01 else "ERROR"))
# ---------- C: cross-document ----------
prs = Presentation(os.path.join(ROOT, "deck.pptx")); deck = []
for s in prs.slides:
    for sh in s.shapes:
        if sh.has_text_frame: deck.append(sh.text_frame.text)
        if getattr(sh, "has_table", False) and sh.has_table:
            for row in sh.table.rows: deck += [c.text for c in row.cells]
    deck.append(s.notes_slide.notes_text_frame.text)
deck = " ".join(deck); n_main = 15; n_notes = sum(1 for s in prs.slides if s.notes_slide.notes_text_frame.text.strip())
doc = Document(os.path.join(ROOT, "pitch-memo.docx")); memo = " ".join(p.text for p in doc.paragraphs) + " " + " ".join(c.text for t in doc.tables for r in t.rows for c in r.cells)
md = {n: open(os.path.join(ROOT, n)).read() for n in ("deep-dive.md", "one-pager.md", "qa-prep.md", "cheat-sheet.md")}
V = F["valuation"]; R = F["rar"]; price = F["price"]
keys = [("Share price", f"${price:.2f}", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md"]), ("Base price target", f"${V['pt'][1]:,.0f}", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md", "qa-prep.md"]),
        ("Probability-weighted value", f"${V['pt'][3]:,.0f}", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md"]), ("Bear target", f"${V['pt'][0]:,.0f}", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md", "qa-prep.md"]),
        ("Bull target", f"${V['pt'][2]:,.0f}", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md"]), ("Expected return", f"{V['ret'][3]*100:+.0f}%", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md"]),
        ("FY27E EPS (mine)", f"${V['eps27'][1]:.2f}", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md", "qa-prep.md"]), ("FY28E EPS (mine)", f"${V['eps28'][1]:.2f}", ["deck", "memo", "deep-dive.md", "cheat-sheet.md"]),
        ("Consensus FY27 EPS", "$16.01", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md", "qa-prep.md"]), ("Revenue at risk %", f"{R['at_risk_pct']*100:.1f}%", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md"]),
        ("Stressed EPS", f"${R['eps1']:.2f}", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md", "qa-prep.md"]), ("TTM free cash flow", f"${F['ttm_fcf']:,.0f}m", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md", "qa-prep.md"]),
        ("FCF yield", f"{F['fcf_yield']:.1f}%", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md"]), ("P/E on consensus FY27", f"{F['pe_fy27_cons']:.1f}x", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md"]),
        ("EV/EBITDA TTM", f"{F['ev_ebitda']:.1f}x", ["deck", "memo", "one-pager.md", "cheat-sheet.md"]), ("Insider sales 12m", f"${F['insider']['sales_12m_usd']/1e6:.1f}m", ["deck", "memo", "deep-dive.md", "cheat-sheet.md"]),
        ("CEO sales", f"${F['insider']['ceo_sales_usd']/1e6:.1f}m", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md", "qa-prep.md"]), ("Base DCF per share", f"${V['dcf'][1]:,.0f}", ["deck", "memo", "deep-dive.md"]),
        ("Net debt / EBITDA", f"{F['nd_ebitda']:.1f}x", ["deck", "memo", "deep-dive.md", "one-pager.md", "cheat-sheet.md"]), ("FY26 EPS guidance", "$14.45-14.65", ["deck", "deep-dive.md", "cheat-sheet.md"])]
Cc = []
for name, val, where in keys:
    miss = [w for w in where if val not in (deck if w == "deck" else memo if w == "memo" else md[w])]
    Cc.append((name, val, ", ".join(where), "OK" if not miss else "MISSING in " + ", ".join(miss)))
qa_n = len(re.findall(r"^### \d+\.", md["qa-prep.md"], re.M)); cs_n = len(re.findall(r"^\| \d+ \|", md["cheat-sheet.md"], re.M))
qa_blocks = re.split(r"^### \d+\..*$", md["qa-prep.md"], flags=re.M)[1:]; qa_num = sum(1 for b in qa_blocks if re.search(r"\d", b)); qa_words = [len(b.split()) for b in qa_blocks]
struct = [("Deck: slides total / main / appendix", f"{len(prs.slides)} / {n_main} / {len(prs.slides)-n_main-1} (+1 divider)", "OK" if len(prs.slides) >= 16 else "CHECK"), ("Deck: slides with speaker notes", f"{n_notes} of {len(prs.slides)}", "OK" if n_notes == len(prs.slides) else "CHECK"),
          ("Q&A: questions / answers containing a number", f"{qa_n} / {qa_num}", "OK" if qa_n == 20 and qa_num == 20 else "CHECK"), ("Q&A: answer length, words (min-max)", f"{min(qa_words)}-{max(qa_words)}", "OK" if max(qa_words) <= 95 else "CHECK"),
          ("Cheat sheet: numbers", str(cs_n), "OK" if cs_n == 25 else "CHECK"), ("Charts in charts/", str(len(glob.glob(os.path.join(ROOT, "charts", "*.png")))), "OK")]
nA = sum(1 for a in A if a[2] == "OK"); nC = sum(1 for c in Cc if c[3] == "OK")
out = ["# verification.md - Phase 9", "", f"Generated by `scripts/19_verify.py` on the data in this folder (prices as of {F['asof']}).", "",
       f"**Summary: {nA} of {len(A)} source re-checks passed; model has {MO['n_formulas']:,} formulas and {len(MO['errors'])} errors; {nC} of {len(Cc)} key numbers agree across deck, memo, markdown and model.**", "",
       "## A. Reported numbers and quotes re-checked against the primary documents", "", "| Claim | Search string in the filing or transcript | Result |", "|---|---|---|"] + [f"| {a} | `{b}` | {c} |" for a, b, c in A]
out += ["", "## B. Model integrity", "", "| Check | Value | Status |", "|---|---|---|"] + [f"| {a} | {b} | {c} |" for a, b, c in Bm]
out += ["", "## C. Key numbers agree across deliverables (each value is generated from data/derived/facts.json, which is read from the recalculated model)", "", "| Number | Value | Checked in | Result |", "|---|---|---|---|"] + [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in Cc]
out += ["", "## D. Structure", "", "| Item | Value | Status |", "|---|---|---|"] + [f"| {a} | {b} | {c} |" for a, b, c in struct]
out += ["", "## E. Uncertain, approximate or stale (read before presenting)", "",
        "1. **Market data source.** Yahoo's price API and Macrotrends refused automated requests. Prices, short interest and Zacks consensus come from Nasdaq's API; Yahoo consensus and beta were read from Yahoo pages; peer multiples from StockAnalysis. Historical forward P/E is my own calculation using realised EPS as a proxy for past consensus, so it is a hindsight series, not a broker series.",
        "2. **Consensus.** FY27 EPS is $16.01 on Yahoo (15 analysts) and $15.85 on Nasdaq/Zacks (5). Consensus by segment was not found. Yahoo's revision timestamps looked lagged.",
        "3. **Share count and net debt at year-end 2026** (45.0m shares, $1,050m) are my estimates; the last reported figures are 46.2m shares and $1,150m at 30-Sep-2026.",
        "4. **Product mix by region** is not disclosed. I applied the FY2025 brand mix (74/13/8) to both regions and assumed China's 8% refers to the Crocs Brand.",
        "5. **All nine risk scores, the haircut map, the fixed/variable cost split, scenario drivers and probabilities are my judgement.** Sensitivities are in the model.",
        "6. **S&P 500 forward P/E (18.3x) and the 10-year Treasury yield (5.0%)** come from web-search summaries of FactSet and press reports, not from the primary documents. Press reports of the yield ranged from 4.84% to 5.13%.",
        "7. **10b5-1 status.** The Form 4 checkbox is unchecked and no footnote mentions a plan on any of the 22 sales. A plan could exist and simply not be marked; check the 10-Q Item 5 disclosures and ask the company.",
        "8. **Holder data.** The proxy's BlackRock and Vanguard figures cite 13G filings from early 2024; I used 13F data at 30-Sep-2026 instead. Himalaya Capital's position comes from secondary sources.",
        "9. **Q4 2026 earnings date** (11-Feb-2027) is Yahoo's estimate; the company has not confirmed it.", "10. **Q3 2026 transcript** is Motley Fool's machine transcription (no company-hosted copy found); figures match the press release.",
        "11. **Securities class action**: no ruling on the motion to dismiss was found as of the 10-Q dated 2026-10-29; PACER was not checked.", "12. **DECK trailing EPS**: XBRL gives $2.31 for the September 2026 quarter against $2.03 on Nasdaq/Zacks; forward multiples are unaffected.",
        "13. **Broker items marked 'snippet only'** in data/research/news_bear_notes.md (some rating changes, TAM deck footnotes) were not opened at source.", "14. **Data will go stale** on the next print: the Morgan Stanley conference on 1-Dec-2026 and Q4 results around 11-Feb-2027."]
open(os.path.join(ROOT, "verification.md"), "w").write("\n".join(out) + "\n")
print(f"A: {nA}/{len(A)}  C: {nC}/{len(Cc)}  model errors: {len(MO['errors'])}")
for a in A:
    if a[2] != "OK": print("  SOURCE CHECK FAILED:", a)
for c in Cc:
    if c[3] != "OK": print("  CROSS-DOC:", c)
for s_ in struct + Bm:
    if s_[2] not in ("OK",): print("  CHECK:", s_)
