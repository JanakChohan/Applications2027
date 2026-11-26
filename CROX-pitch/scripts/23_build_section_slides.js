// Build risks-catalysts-mitigants-slides.pptx: the "Catalysts, Risks and Mitigants" section for the team deck.
// Two core slides, a one-slide alternative in the layout Oakwood's Consumer team used before, and one backup slide.
// Needs pptxgenjs on NODE_PATH (npm install pptxgenjs).
// Numbers are read from data/derived/facts.json so they match the model, the deck and the study guides.
const path = require("path"); const fs = require("fs"); const pptxgen = require("pptxgenjs");
const SKILL = "/root/.claude/skills/synced/7edf4b5b-8aee-4870-84d8-e8f6244ca22c_814abe95-1ebe-48f6-9d90-b31f121f65db/pptx";
const { applyTheme } = require(path.join(SKILL, "scripts/apply_theme.js"));
const ROOT = path.resolve(__dirname, ".."); const F = JSON.parse(fs.readFileSync(path.join(ROOT, "data/derived/facts.json"), "utf8").replace(/\bNaN\b/g, "null"));
const R = F.rar, K = F.key, B = F.scen.Base, fy23 = F.fy2023, INS = F.insider;
const fcf = Math.round(F.ttm_fcf), intl = Math.round(F.intl_share_ttm), lev = F.nd_ebitda.toFixed(1), buyPct = Math.round(1700 / F.mcap * 100);
const opChg = Math.round((1 - B.ebit.FY2026E / fy23.adj_op_income) * 100), epsChg = Math.round((B.eps.FY2026E / fy23.adj_eps - 1) * 100);
const tariffC = Math.round(Math.abs(F.sens["+1 pt US tariff rate on imports"][0]) * 100), atRisk = Math.round(R.at_risk_pct * 100), atRiskM = Math.round(R.at_risk);
const eps0 = Math.round(R.eps0), eps1 = Math.round(R.eps1), epsFall = Math.round(Math.abs(R.eps1 / R.eps0 - 1) * 100), impl = Math.round(K["Market-implied probability of the bear case (base:bull 2:1)"] * 100);
const THEME = { name: "Crocs pitch section", headFontFace: "Calibri", bodyFontFace: "Calibri",
  colors: { dk1: "1B1F23", lt1: "FFFFFF", dk2: "0F3D2E", lt2: "EDF4EF", accent1: "1F7A4D", accent2: "B5382E", accent3: "B7791F", accent4: "2E6F95", accent5: "5F6B66", accent6: "9CCBB0", hlink: "2E6F95", folHlink: "5F6B66" } };
const pres = new pptxgen(); pres.layout = "LAYOUT_WIDE"; pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "Crocs (CROX): catalysts, risks and mitigants"; pres.subject = "Stock pitch section"; const C = pres.SchemeColor;
pres.defineSlideMaster({ title: "CONTENT", background: { color: C.background1 },
  objects: [{ placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.32, w: 12.13, h: 0.95, fontSize: 36, bold: true, color: C.text2, align: "left", valign: "middle", margin: 0 }, text: "" } },
            { text: { text: "Property of Oakwood Fund Management", options: { x: 0.6, y: 7.08, w: 6, h: 0.3, fontSize: 10, color: C.accent5, margin: 0 } } }],
  slideNumber: { x: 12.33, y: 7.08, w: 0.4, h: 0.3, fontSize: 10, color: C.accent5, align: "right" } });
const SRC = "Sources: Crocs 10-K FY2025, Q3 2026 results (29 Oct 2026), 2025 Comfort Report; Yahoo Finance consensus (26 Nov 2026); Piper Sandler teen survey. Data as of 25 Nov 2026.";
const source = (s, t, y) => s.addText(t || SRC, { x: 0.6, y: y || 6.7, w: 12.13, h: 0.3, fontSize: 10, color: C.accent5, margin: 0, isTextBox: true, objectName: "Source" });
const box = (s, x, y, w, h, color, transparency, name) => s.addShape(pres.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.08, fill: { color, transparency: transparency || 0 }, line: { type: "none" }, objectName: name });
const txt = (s, t, o, name) => s.addText(t, Object.assign({ isTextBox: true, margin: 0, color: C.text1, valign: "top", objectName: name }, o));

// ---------------------------------------------------------------- Slide 1: catalysts
pres.addSection({ title: "Catalysts, risks and mitigants" });
let s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Catalysts, risks and mitigants" });
s.addText("Three catalysts that test our thesis", { placeholder: "title" });
const cats = [
  { imp: "Impact  +++", when: "Around 11 Feb 2027", head: "First guidance for 2027", pts: ["Consensus EPS is $16.01", "Guidance leaves out buybacks, so it is built to be beaten", "Crocs raised 2026 guidance three times"], want: "We want: EPS guidance of $16 or more" },
  { imp: "Impact  ++", when: "Late Oct 2027", head: "First clean North America number", pts: ["An accounting change hides 7 to 8 points of direct sales growth until then", "Underlying direct sales grew about 2% last quarter"], want: "We want: direct sales growing" },
  { imp: "Impact  +", when: "All year", head: "Share buybacks", pts: [`$1.7bn approved: ${buyPct}% of the company`, "Share count fell 11% in a year", "Not in guidance or consensus"], want: "We want: $500m or more a year" }];
const cw = (12.13 - 0.6) / 3;
cats.forEach((c, i) => {
  const x = 0.6 + i * (cw + 0.3), y = 1.45;
  box(s, x, y, cw, 3.95, C.background2, 0, `Catalyst ${i + 1} card`);
  box(s, x + 0.25, y + 0.24, 1.55, 0.42, C.text2, 0, `Catalyst ${i + 1} impact pill`);
  txt(s, c.imp, { x: x + 0.25, y: y + 0.24, w: 1.55, h: 0.42, fontSize: 14, bold: true, color: C.background1, align: "center", valign: "middle" }, `Catalyst ${i + 1} impact`);
  txt(s, c.when, { x: x + 1.9, y: y + 0.24, w: cw - 2.15, h: 0.42, fontSize: 14, bold: true, color: C.text2, align: "right", valign: "middle" }, `Catalyst ${i + 1} date`);
  txt(s, c.head, { x: x + 0.25, y: y + 0.82, w: cw - 0.5, h: 0.72, fontSize: 20, bold: true, valign: "middle" }, `Catalyst ${i + 1} heading`);
  txt(s, c.pts.map((p, j) => ({ text: p, options: { bullet: true, breakLine: j < c.pts.length - 1, paraSpaceAfter: 5 } })), { x: x + 0.25, y: y + 1.62, w: cw - 0.5, h: 1.5, fontSize: 14 }, `Catalyst ${i + 1} points`);
  box(s, x + 0.25, y + 3.2, cw - 0.5, 0.55, C.background1, 0, `Catalyst ${i + 1} test box`);
  txt(s, c.want, { x: x + 0.37, y: y + 3.2, w: cw - 0.74, h: 0.55, fontSize: 14, bold: true, color: C.text2, valign: "middle" }, `Catalyst ${i + 1} test`);
});
// timeline strip: Dec 2026 to Dec 2027
const tx0 = 1.6, tx1 = 11.7, ty = 6.05, mx = m => tx0 + (tx1 - tx0) * m / 13;
s.addShape(pres.ShapeType.roundRect, { x: tx0, y: ty + 0.16, w: tx1 - tx0, h: 0.14, rectRadius: 0.07, fill: { color: C.accent6 }, line: { type: "none" }, objectName: "Buyback band" });
s.addShape(pres.ShapeType.line, { x: tx0, y: ty, w: tx1 - tx0, h: 0, line: { color: C.text2, width: 2 }, objectName: "Timeline" });
[[2.5, "11 Feb: guidance"], [11, "Late Oct: clean number"]].forEach(([m, lab], i) => {
  s.addShape(pres.ShapeType.ellipse, { x: mx(m) - 0.11, y: ty - 0.11, w: 0.22, h: 0.22, fill: { color: C.text2 }, line: { color: C.background1, width: 1.5 }, objectName: `Timeline marker ${i + 1}` });
  txt(s, lab, { x: mx(m) - 1.4, y: ty - 0.46, w: 2.8, h: 0.3, fontSize: 12, bold: true, align: "center" }, `Timeline label ${i + 1}`); });
txt(s, "Dec 2026", { x: 0.6, y: ty - 0.15, w: 0.95, h: 0.3, fontSize: 12, color: C.accent5, valign: "middle" }, "Timeline start");
txt(s, "Dec 2027", { x: 11.8, y: ty - 0.15, w: 0.95, h: 0.3, fontSize: 12, color: C.accent5, align: "right", valign: "middle" }, "Timeline end");
txt(s, "Buybacks run all year", { x: tx0, y: ty + 0.32, w: tx1 - tx0, h: 0.26, fontSize: 12, color: C.accent5, align: "center" }, "Buyback band label");
source(s, null, 6.74);
s.addNotes(`SAY IT (about 60 seconds)
A cheap stock needs a reason to stop being cheap. These are our three catalysts, ranked by impact.
One. Around the 11th of February, Crocs gives its first guidance for 2027. Consensus is 16 dollars of EPS. Guidance leaves out buybacks, and Crocs raised guidance three times this year. We want guidance of 16 dollars or more.
Two. Late October 2027. An accounting change makes North America direct sales look 7 to 8 points worse than they are. In October that drops out and we see the real trend. That number settles the fad debate.
Three. Buybacks, all year. 1.7 billion dollars is approved, about ${buyPct} percent of the company. None of it is in consensus.
One warning: the shares move about 15 percent on a results day, up or down.

CHECK BEFORE PRESENTING
- The 11 February date is an estimate. Say "around".
- "We want" lines are our own tests, not company targets.
- If you present after 1 December (investor conference) check for news.`);

// ---------------------------------------------------------------- Slide 2: risks and mitigants
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Catalysts, risks and mitigants" });
s.addText("Three risks, and what softens each one", { placeholder: "title" });
txt(s, "Severity", { x: 0.6, y: 1.36, w: 1.05, h: 0.34, fontSize: 14, bold: true, color: C.accent5, align: "center" }, "Severity header");
txt(s, "Risk", { x: 1.8, y: 1.36, w: 5.2, h: 0.34, fontSize: 16, bold: true, color: C.accent2 }, "Risk header");
txt(s, "Mitigant", { x: 7.6, y: 1.36, w: 5.13, h: 0.34, fontSize: 16, bold: true, color: C.accent1 }, "Mitigant header");
const risks = [
  { sev: "!!", rh: "The clog is a fad", rb: "North America sales fell 7% in 2025 and are still down 2%. US teens rank Crocs 10th, down from 6th. Clogs are 74% of the brand.",
    mh: "A majority-international brand", mb: `International is ${intl}% of the brand and growing 12%. Crocs' own North America stores and sites still grew about 2%. Discounts were cut by choice.` },
  { sev: "!", rh: "EPS growth is all buybacks", rb: `2026 operating profit is set to be ${opChg}% below 2023, yet EPS is ${epsChg}% higher. Margins fell in three of the last four quarters.`,
    mh: "The cash is real", mb: `Free cash flow was $${fcf}m in 12 months. Margin rose 150 basis points last quarter. Debt is low at ${lev} times EBITDA.` },
  { sev: "!", rh: "Supply chain and tariffs", rb: "45% of Crocs are made in Vietnam, and two manufacturers make 73%. US tariffs are 10% to 12.5%. The clog is an oil-based resin.",
    mh: "Lower tariffs, audited suppliers", mb: `Tariffs were cut in 2026, from about 19%. Each point costs about ${tariffC} cents of EPS (our estimate). MSCI ESG rating AA; all suppliers audited.` }];
risks.forEach((r, i) => {
  const y = 1.8 + i * 1.58, h = 1.42;
  box(s, 0.6, y, 1.05, h, C.accent2, 0, `Risk ${i + 1} severity badge`);
  txt(s, r.sev, { x: 0.6, y, w: 1.05, h, fontSize: 32, bold: true, color: C.background1, align: "center", valign: "middle" }, `Risk ${i + 1} severity`);
  box(s, 1.8, y, 5.2, h, C.accent2, 88, `Risk ${i + 1} card`);
  txt(s, [{ text: r.rh, options: { bold: true, fontSize: 17, breakLine: true, paraSpaceAfter: 3 } }, { text: r.rb, options: { fontSize: 14 } }], { x: 1.98, y: y + 0.1, w: 4.86, h: h - 0.2, valign: "middle" }, `Risk ${i + 1} text`);
  s.addShape(pres.ShapeType.rightArrow, { x: 7.1, y: y + h / 2 - 0.16, w: 0.4, h: 0.32, fill: { color: C.text2 }, line: { type: "none" }, objectName: `Risk ${i + 1} arrow` });
  box(s, 7.6, y, 5.13, h, C.accent1, 86, `Mitigant ${i + 1} card`);
  txt(s, [{ text: r.mh, options: { bold: true, fontSize: 17, breakLine: true, paraSpaceAfter: 3 } }, { text: r.mb, options: { fontSize: 14 } }], { x: 7.78, y: y + 0.1, w: 4.79, h: h - 0.2, valign: "middle" }, `Mitigant ${i + 1} text`);
});
source(s, null, 6.66);
s.addNotes(`SAY IT (about 75 seconds)
Crocs is cheap because of one risk: that the clog is a fad.
There is real evidence. North America revenue fell 7 percent last year and is still down 2 percent. Teens now rank Crocs 10th.
The mitigant is international. It is ${intl} percent of the brand and growing 12 percent. And Crocs' own stores and sites in North America are still growing.
Second risk: earnings quality. Operating profit is ${opChg} percent below 2023, but EPS is ${epsChg} percent higher. The whole difference is buybacks.
The mitigant: the cash is real. ${fcf} million dollars of free cash flow, and debt is low.
Third risk: supply chain and tariffs. 45 percent of Crocs are made in Vietnam.
The mitigant: tariffs were cut this year, each point is only about ${tariffC} cents of EPS, and MSCI rates Crocs double-A on ESG.

IF ASKED
- How bad could the fad risk be? Our stress test: about ${atRisk} percent of revenue at risk, which would cut EPS from about ${eps0} dollars to about ${eps1}. See the backup slide.
- A spare risk: insiders sold ${(INS.sales_12m_usd / 1e6).toFixed(1)} million dollars of shares in 12 months and bought ${(INS.buys_12m_usd / 1e6).toFixed(1)} million. The CEO sold ${(INS.ceo_sales_usd / 1e6).toFixed(1)} million. Say "the forms do not show a pre-arranged plan". Mitigant: he still holds about ${Math.round(INS.ceo_shares_after * F.price / 1e6)} million dollars of shares.
- "All suppliers audited" means 100 percent of main factories and suppliers completed social compliance audits (Comfort Report, page 23). MSCI AA is on page 8.

LABELS
- Facts: sales, margins, free cash flow, tariffs, sourcing, MSCI rating.
- Our estimate: 2026 operating profit and EPS (inside Crocs' guidance), cost per tariff point.`);

// ---------------------------------------------------------------- Slide 3: one-slide alternative
pres.addSection({ title: "One-slide version" });
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "One-slide version" });
s.addText("Catalysts, risks and mitigants to our thesis", { placeholder: "title" });
const hd = (t, color) => ({ text: t, options: { bold: true, color: C.background1, fill: { color }, fontSize: 14, valign: "middle" } });
const cell = (t, o) => ({ text: t, options: Object.assign({ fontSize: 14, color: C.text1, valign: "middle" }, o || {}) });
const mark = (t, color) => ({ text: t, options: { fontSize: 18, bold: true, color, align: "center", valign: "middle" } });
const border = { type: "solid", color: THEME.colors.lt2, pt: 1 };
s.addTable([[hd("Impact", C.text2), hd("Catalyst", C.text2), hd("What we need to see", C.text2)],
  [mark("+++", C.text2), cell("First guidance for 2027, around 11 Feb 2027. Consensus EPS is $16.01"), cell("EPS guidance of $16 or more")],
  [mark("++", C.text2), cell("First clean North America number, late Oct 2027"), cell("Direct sales growing")],
  [mark("+", C.text2), cell(`Buybacks all year: $1.7bn approved, ${buyPct}% of the company`), cell("$500m or more a year")]],
  { x: 0.6, y: 1.4, w: 12.13, colW: [1.2, 7.03, 3.9], rowH: [0.4, 0.58, 0.58, 0.58], border, margin: [0.03, 0.1, 0.03, 0.1], objectName: "Catalysts table" });
s.addTable([[hd("Severity", C.accent2), hd("Risk", C.accent2), hd("Mitigant", C.accent1)],
  [mark("!!", C.accent2), cell("The clog is a fad: North America down 7% in 2025, still down 2%"), cell(`International is ${intl}% of the brand, growing 12%`)],
  [mark("!", C.accent2), cell(`EPS growth is all buybacks: operating profit ${opChg}% below 2023`), cell(`Cash is real: $${fcf}m free cash flow; debt ${lev} times EBITDA`)],
  [mark("!", C.accent2), cell("Supply chain and tariffs: 45% made in Vietnam; tariffs 10% to 12.5%"), cell("Tariffs cut from about 19%; MSCI AA; suppliers audited")]],
  { x: 0.6, y: 3.95, w: 12.13, colW: [1.2, 5.8, 5.13], rowH: [0.4, 0.62, 0.62, 0.62], border, margin: [0.03, 0.1, 0.03, 0.1], objectName: "Risks and mitigants table" });
source(s, null, 6.66);
s.addNotes(`This is the same content as the two slides before it, on one slide.
It follows the layout the Consumer team used for Deckers: catalysts ranked by impact, risks ranked by severity, a mitigant beside each risk.
Use EITHER this slide OR the two before it. Delete the one you do not use.
The speaking script is in the notes of the two slides before this one.`);

// ---------------------------------------------------------------- Slide 4: backup
pres.addSection({ title: "Backup" });
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Backup" });
s.addText("Backup: how big is the fad risk?", { placeholder: "title" });
const stats = [[`${atRisk}%`, `of revenue is at risk if the clog trend reverses ($${atRiskM}m)`], [`$${eps0} to $${eps1}`, `EPS in our stress test. Fixed costs turn a ${atRisk}% sales fall into a ${epsFall}% EPS fall`], [`25% vs ${impl}%`, "our chance of the bear case, against what the share price implies"]];
stats.forEach(([n, l], i) => {
  const x = 0.6 + i * (cw + 0.3);
  box(s, x, 1.45, cw, 2.2, C.background2, 0, `Stat ${i + 1} card`);
  txt(s, n, { x: x + 0.25, y: 1.55, w: cw - 0.5, h: 0.95, fontSize: 44, bold: true, color: C.text2, valign: "middle" }, `Stat ${i + 1} number`);
  txt(s, l, { x: x + 0.25, y: 2.52, w: cw - 0.5, h: 1.0, fontSize: 14 }, `Stat ${i + 1} label`); });
box(s, 0.6, 3.95, 12.13, 2.4, C.accent2, 90, "Kill criteria panel");
txt(s, "What would make us sell", { x: 0.85, y: 4.08, w: 11.6, h: 0.42, fontSize: 20, bold: true, color: C.accent2, valign: "middle" }, "Kill criteria heading");
txt(s, ["North America direct sales negative for two quarters in a row", "International growth below 5% for two quarters in a row", "2027 operating margin guidance below 21.5%"].map((t, j) => ({ text: t, options: { bullet: true, breakLine: j < 2, paraSpaceAfter: 6 } })),
  { x: 0.85, y: 4.62, w: 11.6, h: 1.6, fontSize: 18 }, "Kill criteria list");
source(s, "All figures on this slide are our estimates. Method: revenue split into nine parts, each scored 1 to 5 for exposure; a score of 5 means a 30% fall, close to Crocs in 2007-09 (-24%).", 6.66);
s.addNotes(`Use this only if someone asks "how bad could it get?" or "what would make you sell?".
SAY IT
We split revenue into nine parts and scored each for how exposed it is to clogs going out of fashion. About ${atRisk} percent of revenue is at risk.
Crocs has high fixed costs. So a ${atRisk} percent fall in revenue would roughly halve EPS, from about ${eps0} dollars to about ${eps1}.
We give that kind of outcome a one-in-four chance. The share price implies about ${impl} percent.
And we have written down what would make us sell.

IMPORTANT
- Every number here is our estimate, not a company figure. Say "we estimate".
- If someone says the scores are made up: moving every score one notch gives ${Math.round(R.minus1_pct * 100)} to ${Math.round(R.plus1_pct * 100)} percent of revenue. The conclusion does not change.
- Check these numbers fit the team's DCF before using this slide.`);

(async () => {
  const out = path.join(ROOT, "risks-catalysts-mitigants-slides.pptx");
  await pres.writeFile({ fileName: out }); await applyTheme(out, THEME); console.log("saved", out);
})();
