// verbal/view.js — rendering + coaching for the verbal module.
import { REASONS } from '../../coaching/diagnosis.js';
import { relevantTab } from './verify.js';
import { key } from './generate.js';

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

/** A tab's short passage, rendered for the tabbed display. */
export function passageHtml(tab) {
  return `<div class="passage"><h4>${esc(tab.title)}</h4><p>${esc(tab.passage)}</p></div>`;
}

export function tokenLabel(token) {
  return { TRUE: 'True', FALSE: 'False', CANNOT_SAY: 'Cannot Say' }[token] || token;
}

/** Worked solution: quote the deciding sentence (or name the missing attribute). */
export function renderReview(item, res, session) {
  const world = session.world;
  const c = item.claim;
  const tabId = relevantTab(world, c);
  const tab = world.tabs.find((t) => t.id === tabId);
  const fact = world.facts.get(key(c.subject, c.attribute));

  let body;
  if (item.label === 'CANNOT_SAY') {
    body = `<p>The statement asks about <strong>${esc(prettyAttr(c.attribute))}</strong>. ` +
      `Scan the tabs — <strong>none of them state this</strong>. ` +
      `${item.traps.includes('quantifier')
        ? 'The passages support a general claim but never the absolute (“every / all”) version the statement makes. '
        : 'It may feel plausible, but the passages neither confirm nor deny it. '}` +
      `With nothing in the text to decide it, the answer is <strong>Cannot Say</strong>.</p>`;
  } else {
    const decisive = tab ? tab.passage : '';
    body = `<p>This relates to the <strong>${esc(tab ? tab.title : '?')}</strong> tab, which states: ` +
      `<span class="quote">“${esc(decisive)}”</span></p>` +
      (item.label === 'TRUE'
        ? `<p>The statement ${item.traps.includes('synonym') ? 'restates this in different words that still match' : 'matches this exactly'} ` +
          `(“${esc(c.asserted)}” ↔ “${esc(fact ? fact.value : '')}”), so it is fully supported → <strong>True</strong>.</p>`
        : `<p>The statement says “${esc(c.asserted)}”, but the tab states “${esc(fact ? fact.value : '')}”. ` +
          `That is a direct contradiction, so → <strong>False</strong>.</p>`);
  }
  const dx = res.diagnosis && res.diagnosis.category !== 'correct_fast'
    ? `<div class="diag"><strong>${esc(res.diagnosis.label)}.</strong> ${esc(res.diagnosis.advice)}</div>` : '';
  return `${body}${dx}`;
}

function prettyAttr(a) { return a.replace(/\bthe\b/g, '').trim(); }

/** Verbal-specific why-wrong diagnosis. */
export function diagnose(item, ans) {
  const R = (cat) => ({ category: cat, ...REASONS[cat] });
  const correct = item.label;
  const given = ans.given;
  if (given == null) return R(ans.ranOutOfTime ? 'ran_out_of_time' : 'skipped_blank');
  if (given === correct) return ans.timeMs > 30000 ? R('slow_but_correct') : R('correct_fast');
  if (ans.wrongTab) return R('wrong_tab');

  if (correct === 'CANNOT_SAY' && given !== 'CANNOT_SAY') {
    if (item.traps.includes('quantifier')) return R('quantifier_overreach');
    if (item.traps.includes('outside_knowledge')) return R('used_outside_knowledge');
    return R('missed_cannot_say');
  }
  if (given === 'CANNOT_SAY' && correct !== 'CANNOT_SAY') return R('over_cautious');
  // TRUE/FALSE swapped
  if (item.traps.includes('synonym')) return R('paraphrase_miss');
  if (ans.timeMs != null && ans.timeMs < 5000) return R('panic_guess');
  return R('paraphrase_miss');
}
