// -----------------------------------------------------------------------------
// scoring.js — score a completed session the way the real test does, for ANY
// module. Negative marking (correct +1, wrong −1, blank 0), an optional wrong-tab
// penalty for tab modules, and a synthetic norm (Stanine + illustrative
// percentile). The module supplies answerOf / requiredTabsOf / diagnose so this
// stays module-agnostic (research/FINDINGS.md §2, FINDINGS_verbal_logical §C).
// -----------------------------------------------------------------------------

import { rateToPercentile, percentileToStanine, STANINE_LABEL } from './norms.js';

const WRONG_TAB_PENALTY = 1;

/** Which tabs a numerical item requires, from its requiredCells (used by the numerical adapter). */
export function requiredTabs(item) {
  const tabs = new Set();
  for (const c of item.requiredCells || []) if (c.tab) tabs.add(c.tab);
  return tabs;
}

/**
 * @param {object} session  { items, ... }
 * @param {Array}  answers  aligned: { given, timeMs, submittedTab, ranOutOfTime }
 * @param {object} opts     { wrongTabPenalty:boolean }
 * @param {object} module   the active module (answerOf / requiredTabsOf / diagnose / usesTabs)
 */
export function scoreSession(session, answers, opts = {}, module) {
  const items = session.items;
  const wrongTabOn = opts.wrongTabPenalty !== false && module.usesTabs;

  let correct = 0, wrong = 0, blank = 0, wrongTabEvents = 0, timeTotal = 0;
  const perItem = [];

  items.forEach((item, i) => {
    const ans = answers[i] || { given: null };
    const given = ans.given ?? null;
    const isBlank = given == null;
    const correctToken = module.answerOf(item);
    const isCorrect = given === correctToken;

    // wrong-tab: answered with a non-required tab showing (tab modules, decidable items)
    let wrongTab = false;
    if (module.usesTabs && !isBlank) {
      const req = module.requiredTabsOf(item) || [];
      if (req.length && ans.submittedTab && !req.includes(ans.submittedTab)) wrongTab = true;
    }

    if (isBlank) blank++;
    else if (isCorrect) correct++;
    else wrong++;
    if (wrongTab) wrongTabEvents++;
    if (ans.timeMs) timeTotal += ans.timeMs;

    const diagnosis = module.diagnose(item, { ...ans, wrongTab });
    perItem.push({ index: i, item, given, correctToken, isBlank, isCorrect, wrongTab, timeMs: ans.timeMs ?? null, diagnosis });
  });

  const raw = correct - wrong;
  const tabPenalty = wrongTabOn ? wrongTabEvents * WRONG_TAB_PENALTY : 0;
  const adjusted = raw - tabPenalty;
  const attempted = correct + wrong;
  const rate = adjusted / (items.length || 1);
  const percentile = rateToPercentile(rate);
  const stanine = percentileToStanine(percentile);

  return {
    module: session.module,
    count: items.length,
    correct, wrong, blank, attempted,
    naiveScore: correct,
    rawScore: raw,
    wrongTabEvents, tabPenalty,
    adjustedScore: adjusted,
    accuracyAttempted: attempted ? correct / attempted : 0,
    coverage: items.length ? attempted / items.length : 0,
    avgTimeMs: attempted ? timeTotal / attempted : 0,
    percentile, stanine, stanineLabel: STANINE_LABEL[stanine],
    perItem,
    reasonTally: perItem.reduce((acc, p) => { acc[p.diagnosis.category] = (acc[p.diagnosis.category] || 0) + 1; return acc; }, {}),
  };
}
