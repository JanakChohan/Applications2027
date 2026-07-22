// -----------------------------------------------------------------------------
// scoring.js — score a completed session the way the real test does, and explain
// the gap between naive and penalised scoring so the negative-marking lesson
// lands (research/FINDINGS.md §2).
//
//   raw       = (#correct)          − (#wrong)            [negative marking]
//   adjusted  = raw − (wrong-tab events × penalty)        [wrong-tab quirk]
//   naive     = #correct                                  [what people assume]
//
// The score is then expressed against a synthetic norm (Stanine + illustrative
// percentile). Blanks are 0 — never negative — so skipping beats guessing.
// -----------------------------------------------------------------------------

import { diagnose } from './diagnosis.js';
import { rateToPercentile, percentileToStanine, STANINE_LABEL } from './norms.js';

const WRONG_TAB_PENALTY = 1;

/** Which tabs does an item actually require? (decidable items only.) */
export function requiredTabs(item) {
  const tabs = new Set();
  for (const c of item.requiredCells || []) if (c.tab) tabs.add(c.tab);
  return tabs;
}

/**
 * @param {object} session  { items, dataset }
 * @param {Array}  answers  aligned to items: { given, timeMs, submittedTab, ranOutOfTime }
 * @param {object} opts     { wrongTabPenalty:boolean }
 */
export function scoreSession(session, answers, opts = {}) {
  const items = session.items;
  const wrongTabOn = opts.wrongTabPenalty !== false;

  let correct = 0, wrong = 0, blank = 0, wrongTabEvents = 0;
  let timeTotal = 0;
  const perItem = [];

  items.forEach((item, i) => {
    const ans = answers[i] || { given: null };
    const given = ans.given ?? null;
    const isBlank = given == null;
    const isCorrect = given === item.label;

    // Wrong-tab: submitted an answer while a non-required tab was showing.
    let wrongTab = false;
    if (!isBlank && item.label !== 'CANNOT_SAY') {
      const req = requiredTabs(item);
      if (req.size && ans.submittedTab && !req.has(ans.submittedTab)) wrongTab = true;
    }

    if (isBlank) blank++;
    else if (isCorrect) correct++;
    else wrong++;
    if (wrongTab) wrongTabEvents++;
    if (ans.timeMs) timeTotal += ans.timeMs;

    const dx = diagnose(item, { ...ans, wrongTab });
    perItem.push({
      index: i, item, given, isBlank, isCorrect, wrongTab,
      timeMs: ans.timeMs ?? null, diagnosis: dx,
    });
  });

  const raw = correct - wrong;
  const tabPenalty = wrongTabOn ? wrongTabEvents * WRONG_TAB_PENALTY : 0;
  const adjusted = raw - tabPenalty;
  const attempted = correct + wrong;
  const rate = adjusted / items.length;
  const percentile = rateToPercentile(rate);
  const stanine = percentileToStanine(percentile);

  return {
    count: items.length,
    correct, wrong, blank, attempted,
    naiveScore: correct,
    rawScore: raw,
    wrongTabEvents, tabPenalty,
    adjustedScore: adjusted,
    accuracyAttempted: attempted ? correct / attempted : 0,
    coverage: attempted / items.length,
    avgTimeMs: attempted ? timeTotal / attempted : 0,
    percentile, stanine, stanineLabel: STANINE_LABEL[stanine],
    perItem,
    // reason tally for the coaching summary
    reasonTally: perItem.reduce((acc, p) => {
      acc[p.diagnosis.category] = (acc[p.diagnosis.category] || 0) + 1;
      return acc;
    }, {}),
  };
}
