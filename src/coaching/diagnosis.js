// -----------------------------------------------------------------------------
// diagnosis.js — decide WHY an item was got wrong (or was slow), by category.
//
// This is the heart of the coaching: not just "you missed 6", but "4 of your 6
// misses were you over-inferring to True/False when the honest answer was Cannot
// Say" — the single biggest real-test score-killer (research/FINDINGS.md §4).
// -----------------------------------------------------------------------------

// A "slow" correct answer still costs you on a ~20s/item test.
export const SLOW_MS = 45000;
export const PANIC_MS = 7000;

export const REASONS = {
  correct_fast: { label: 'Correct', advice: '' },
  slow_but_correct: {
    label: 'Slow but correct',
    advice: 'Right answer, but over the ~20s budget — this pace would cost you unfinished items on the real test.',
  },
  missed_cannot_say: {
    label: 'Should have been Cannot Say',
    advice: 'You committed to True/False when a required figure was not shown. Over-inference is the #1 score-killer — if any needed number is missing, the answer is Cannot Say.',
  },
  over_cautious: {
    label: 'Answerable — not Cannot Say',
    advice: 'You chose Cannot Say, but every figure you needed WAS on the tabs. Re-check the exact entity/period before giving up.',
  },
  wrong_tab: {
    label: 'Wrong tab on submit',
    advice: 'You answered with the wrong data display showing. On the real test that reduces your points even when the answer is right — confirm the correct tab before you submit.',
  },
  pct_vs_pp_confusion: {
    label: 'Percent vs percentage points',
    advice: 'You mixed a change in percentage points with a relative % change. “From 10% to 15%” is +5 points but +50% relative — decide which the statement asks for.',
  },
  arithmetic_slip: {
    label: 'Arithmetic slip',
    advice: 'The right figures, wrong calculation. Slow down on the single step; use the on-screen calculator and pen for multi-stage sums.',
  },
  unit_error: {
    label: 'Unit / scale error',
    advice: 'Check the axis/footnote unit first (thousands vs millions, % vs absolute) and convert before comparing.',
  },
  misread_data: {
    label: 'Misread the data',
    advice: 'Wrong row/column/point read from the tab. Match the exact label named in the statement — beware Total rows sitting next to line items.',
  },
  reasoning_error: {
    label: 'Reasoning error',
    advice: 'Re-read the statement literally and check each figure it depends on.',
  },
  ran_out_of_time: {
    label: 'Ran out of time',
    advice: 'Left blank at the buzzer. Blanks score 0 (no penalty) — but attempting more accurate items lifts your score. Work the skip rule: abandon anything not cracked by ~30s.',
  },
  skipped_blank: {
    label: 'Left blank',
    advice: 'You skipped this one. Blanks score 0 (no penalty), which is correct when you truly can’t narrow it — but in untimed practice, work it through to learn the pattern.',
  },
  panicked_guess: {
    label: 'Fast wrong guess',
    advice: 'Answered in under ~7s and missed. Blind guesses are negative-EV here (wrong = −1). If you can’t eliminate an option, leave it blank.',
  },
};

/**
 * @param {object} item     the generated item (has type, traps, label)
 * @param {object} ans      { given, timeMs, wrongTab, ranOutOfTime }
 * @returns {{category, label, advice}}
 */
export function diagnose(item, ans) {
  const correct = item.label;
  const given = ans.given;
  const isBlank = given == null;
  const isCorrect = given === correct;

  if (isBlank) {
    return withMeta(ans.ranOutOfTime ? 'ran_out_of_time' : 'skipped_blank');
  }

  if (isCorrect) {
    if (ans.timeMs != null && ans.timeMs > SLOW_MS) return withMeta('slow_but_correct');
    return withMeta('correct_fast');
  }

  // Wrong answers — classify the failure.
  if (ans.wrongTab) return withMeta('wrong_tab');

  if (correct === 'CANNOT_SAY' && given !== 'CANNOT_SAY') return withMeta('missed_cannot_say');
  if (given === 'CANNOT_SAY' && correct !== 'CANNOT_SAY') return withMeta('over_cautious');

  // True/False swapped → use the item's trap tags to attribute the slip.
  const traps = item.traps || [];
  if (traps.includes('pct_vs_pp')) return withMeta('pct_vs_pp_confusion');
  if (traps.includes('unit')) return withMeta('unit_error');
  if (ans.timeMs != null && ans.timeMs < PANIC_MS) return withMeta('panicked_guess');
  if (traps.includes('pct_change') || item.type === 'arithmetic' || item.type === 'multi_tab') {
    return withMeta('arithmetic_slip');
  }
  if (item.type === 'lookup' || item.type === 'rank' || item.type === 'trend') return withMeta('misread_data');
  return withMeta('reasoning_error');
}

function withMeta(category) {
  return { category, ...REASONS[category] };
}
