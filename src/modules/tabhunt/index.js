// tabhunt/index.js — the "Tab Finder" drill.
//
// Trains the single most mechanical skill in scales numerical: reading a
// statement and knowing WHICH tab(s) hold the figures it needs — before doing
// any maths at all. Several vendors report that submitting with the wrong tab
// displayed costs points on the real test, and slow tab-hunting is where most
// of the ~20s/item budget silently disappears.
//
// It reuses the verified numerical generator wholesale: a real 6-tab dataset is
// shown (browse the tabs exactly like the real test), but instead of judging
// True/False/Cannot Say you select the tab(s) the statement requires — or "No
// tab shows this" when the quantity isn't displayed anywhere (the Cannot-Say
// data-type trap, seen from the tab-hunting side). Multi-tab items (profit,
// per-head, share-of-total) require selecting BOTH tabs, which teaches the
// multi-tab workflow directly.
//
// Ground truth: the required tabs are derived from the item's verified claim
// references (requiredCells), so the answer key inherits the numerical module's
// independent-verifier guarantee. The company-wide total caption renders on the
// share tab, so revenueTotal references map there.

import numerical from '../numerical/index.js';
import { REASONS } from '../../coaching/diagnosis.js';

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

/** The tab ids an item's figures actually live on (caption → share tab). */
function requiredTabIds(item) {
  const ids = new Set();
  for (const c of item.requiredCells || []) {
    const tab = c.tab || (c.m === 'revenueTotal' ? 'share' : null);
    if (tab) ids.add(tab);
  }
  return [...ids].sort();
}
const sigOf = (ids) => (ids.length ? ids.join('+') : 'NONE');

export default {
  id: 'tabhunt',
  label: 'tab finder',
  blurb: 'A statement appears — click the tab(s) it needs, not the answer. Trains tab-hunting speed and the wrong-tab discipline.',
  tiers: ['beginner', 'intermediate', 'advanced'],
  usesTabs: true,
  answerKind: 'custom',
  flavors: numerical.flavors,
  modes: [
    { key: 'timed', label: 'Timed set', count: 20, time: 180, timed: true, allowBack: true, desc: '20 statements · 3:00 (~9s each) — tab-spotting at speed' },
    { key: 'untimed', label: 'Untimed drill', count: 15, time: 0, timed: false, allowBack: true, desc: 'No clock · learn where each quantity lives' },
  ],

  generate({ seed, tier = 'intermediate', count = 15, flavor = null }) {
    const base = numerical.generate({ seed: `th-${seed}`, tier, count, flavor });
    const titleOf = Object.fromEntries(base.context.tabs.map((t) => [t.id, t.title]));
    const items = base.items.map((it, i) => {
      const req = requiredTabIds(it);
      const sig = sigOf(req);
      return {
        module: 'tabhunt', type: 'tabhunt', tier,
        id: `${seed}-t${i}`, index: i,
        skill: req.length === 0 ? 'not-shown' : req.length === 1 ? 'single-tab' : 'multi-tab',
        prompt: `Which tab(s) would you open to judge: “${it.text}”`,
        statement: it.text,
        answer: sig, requiredIds: req, tabTitles: titleOf,
        sourceItem: it, traps: it.traps || [],
      };
    });
    return { module: 'tabhunt', seed, tier, context: base.context, dataset: base.dataset, items };
  },

  answerOf: (item) => item.answer,
  tokenLabel: (token, item) => token === 'NONE'
    ? 'No tab shows this'
    : token.split('+').map((id) => (item && item.tabTitles[id]) || id).join(' + '),
  requiredTabsOf: () => [],   // the tab-choice IS the answer; no wrong-tab double-penalty

  renderControls(item, session, state) {
    const sel = item.__sel || [];
    const submitted = state && state.given != null;
    const chosen = submitted ? (state.given === 'NONE' ? [] : state.given.split('+')) : sel;
    const noneOn = submitted ? state.given === 'NONE' : sel.includes('NONE');
    const btn = (id, title) =>
      `<button class="tabbtn${chosen.includes(id) ? ' on' : ''}" data-tsel="${id}" ${submitted ? 'disabled' : ''}>${esc(title)}</button>`;
    const tabBtns = session.context.tabs.map((t) => btn(t.id, t.title)).join('');
    return `<div class="tabhunt-controls">
      <div class="tabhunt-row">${tabBtns}
        <button class="tabbtn none${noneOn ? ' on' : ''}" data-tsel="NONE" ${submitted ? 'disabled' : ''}>No tab shows this</button>
      </div>
      <div class="tabhunt-actions">
        ${submitted
          ? `<span class="small muted">Submitted: <strong>${esc(this.tokenLabel(state.given, item))}</strong> — you can change it until you move on.</span>
             <button class="btn ghost" data-tsubmit-reset>Change</button>`
          : `<button class="btn" data-tsubmit ${sel.length ? '' : 'disabled'}>Submit selection</button>
             <span class="small muted">Select every tab the statement needs (some need two), or “No tab”.</span>`}
      </div>
    </div>`;
  },

  wireQuestion(root, item, session, api) {
    root.querySelectorAll('[data-tsel]').forEach((el) => {
      el.onclick = () => {
        const id = el.dataset.tsel;
        let sel = item.__sel || [];
        if (id === 'NONE') sel = sel.includes('NONE') ? [] : ['NONE'];       // exclusive
        else {
          sel = sel.filter((x) => x !== 'NONE');
          sel = sel.includes(id) ? sel.filter((x) => x !== id) : [...sel, id];
        }
        item.__sel = sel;
        api.rerender();
      };
    });
    const submit = root.querySelector('[data-tsubmit]');
    if (submit) submit.onclick = () => {
      const sel = item.__sel || [];
      api.select(sel.includes('NONE') ? 'NONE' : sigOf([...sel].sort()));
    };
    const reset = root.querySelector('[data-tsubmit-reset]');
    if (reset) reset.onclick = () => { item.__sel = []; api.select(null); };
  },

  renderReview(item, res) {
    const src = item.sourceItem;
    const need = item.requiredIds.map((id) => `<strong>${esc(item.tabTitles[id] || id)}</strong>`).join(' + ');
    const cells = (src.requiredCells || []).filter((c) => c.visible).map((c) =>
      `<li>${esc(c.title)}${c.e && c.e !== '__ALL__' ? ` — ${esc(c.e)}` : ''}, ${esc(c.p)}: found on the ` +
      `<strong>${esc(item.tabTitles[c.tab || (c.m === 'revenueTotal' ? 'share' : '')] || 'shown')}</strong> tab</li>`).join('');
    const missing = (src.requiredCells || []).filter((c) => !c.visible).map((c) =>
      `<li>${esc(c.title)}${c.e && c.e !== '__ALL__' ? ` — ${esc(c.e)}` : ''}, ${esc(c.p)}: <strong>not shown on any tab</strong></li>`).join('');
    const head = item.answer === 'NONE'
      ? '<p>No tab holds what this statement needs — the quantity type is not displayed anywhere. On the real test this is a strong Cannot-Say signal.</p>'
      : `<p>The statement needs ${need}${item.requiredIds.length > 1
          ? ' — a multi-tab item: read the first figure, note it on paper, switch, and answer while one of the required tabs is showing.'
          : '.'}</p>`;
    const diag = res.diagnosis && res.diagnosis.category !== 'correct_fast'
      ? `<div class="diag"><strong>${esc(res.diagnosis.label)}.</strong> ${esc(res.diagnosis.advice)}</div>` : '';
    return `${head}<div class="solution"><ul>${cells}${missing}</ul></div>${diag}`;
  },

  diagnose(item, ans) {
    const R = (c) => ({ category: c, ...REASONS[c] });
    if (ans.given == null) return R(ans.ranOutOfTime ? 'ran_out_of_time' : 'skipped_blank');
    if (ans.given === item.answer) return ans.timeMs > 15000 ? R('slow_but_correct') : R('correct_fast');
    if (ans.timeMs != null && ans.timeMs < 3000) return R('panic_guess');
    return R('wrong_tab');
  },
};
