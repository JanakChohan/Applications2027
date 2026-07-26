// numerical/index.js — adapts the existing scales-numerical engine (generators/,
// verify/, ui/charts) to the shared module interface. The numerical logic is
// unchanged; this only wires it into the multi-module shell.
import { generateSession } from '../../generators/session.js';
import { adaptiveWeights } from '../../coaching/adaptive.js';
import { renderChart } from '../../ui/charts.js';
import { requiredTabs } from '../../coaching/scoring.js';
import { diagnose as numDiagnose } from '../../coaching/diagnosis.js';

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const TFC = { TRUE: 'True', FALSE: 'False', CANNOT_SAY: 'Cannot Say' };

export default {
  id: 'numerical',
  label: 'scales numerical',
  blurb: 'Interpret charts and tables across six tabs; judge each statement True / False / Cannot Say.',
  tiers: ['medium', 'intermediate', 'hard'],
  usesTabs: true,
  answerKind: 'tfc',
  modes: [
    { key: 'full', label: 'Full mock', count: 37, time: 720, timed: true, allowBack: true, desc: '37 tasks · 12:00 · the real long form (~20s/item)' },
    { key: 'short', label: 'Short mock', count: 18, time: 360, timed: true, allowBack: true, desc: '18 tasks · 6:00 · the real short form' },
    { key: 'remembered', label: 'As remembered', count: 18, time: 720, timed: true, allowBack: true, nonstandard: true, desc: '18 tasks · 12:00 · gentler (your recollection)' },
    { key: 'untimed', label: 'Untimed drill', count: 15, time: 0, timed: false, allowBack: true, desc: 'No clock · learn the reasoning' },
    { key: 'adaptive', label: 'Adaptive drill', count: 15, time: 0, timed: false, allowBack: true, adaptive: true, desc: 'No clock · more of your weakest categories' },
  ],

  generate({ seed, tier = 'intermediate', count = 18, typeWeights }) {
    const opts = { seed, tier, count };
    if (typeWeights) opts.typeWeights = typeWeights;
    const session = generateSession(opts);
    for (const it of session.items) {
      it.module = 'numerical';
      it.prompt = it.text;               // the statement to judge
      it.skill = it.type;                // fine-grained bucket for progress/adaptive
      it.requiredTabs = [...requiredTabs(it)];
    }
    const context = { tabs: session.dataset.tabs.map((t) => ({ id: t.id, title: t.title, html: renderChart(t, session.dataset) })) };
    return { module: 'numerical', seed, tier, dataset: session.dataset, context, items: session.items };
  },

  adaptive: (data) => ({ typeWeights: adaptiveWeights(data, 2.2) }),
  answerOf: (item) => item.label,
  tokenLabel: (t) => TFC[t] || t,
  requiredTabsOf: (item) => item.requiredTabs || [],

  renderReview(item, res, session) {
    const steps = item.solution.steps.map((s) => `<li>${esc(s)}</li>`).join('');
    const reqTabs = (item.requiredTabs || []).map((id) => {
      const t = session.dataset.tabs.find((x) => x.id === id);
      return t ? t.title : id;
    });
    const tabNote = item.label === 'CANNOT_SAY'
      ? 'No single tab holds the answer — a required figure is missing.'
      : `Needed tab(s): <strong>${reqTabs.map(esc).join(', ') || '—'}</strong>`;
    const diag = res.diagnosis && res.diagnosis.category !== 'correct_fast'
      ? `<div class="diag"><strong>${esc(res.diagnosis.label)}.</strong> ${esc(res.diagnosis.advice)}</div>` : '';
    return `<div class="small muted">${tabNote} · type: ${esc(item.type)}${(item.traps || []).length ? ' · traps: ' + item.traps.map(esc).join(', ') : ''}</div>
      <div class="solution"><ol>${steps}</ol></div>
      <div class="rationale">${esc(item.solution.rationale)}</div>${diag}`;
  },

  diagnose: numDiagnose,
};
