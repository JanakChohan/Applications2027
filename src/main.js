// -----------------------------------------------------------------------------
// main.js — the multi-module app shell.
//
// A small screen state-machine that drives ANY module through the same authentic
// flow: pick a test type → tabbed/visual display → answer → countdown → verified
// scoring with negative marking → per-question coaching → progress over time.
// Each module (src/modules/*) supplies its own generation, answer UI, worked
// solutions and diagnosis; this shell owns the timer, scoring, navigation, store,
// results and progress screens.
// -----------------------------------------------------------------------------

import './ui/styles.css';
import guideMd from '../GUIDE.md?raw';

import { MODULES, moduleById } from './modules/index.js';
import { createCalculator } from './ui/calculator.js';
import { scoreSession } from './coaching/scoring.js';
import { recordSession, load, reset } from './coaching/store.js';
import { weakestWithStats } from './coaching/adaptive.js';
import { REASONS } from './coaching/diagnosis.js';

const TFC = [
  { v: 'TRUE', label: 'True', cls: 't' },
  { v: 'FALSE', label: 'False', cls: 'f' },
  { v: 'CANNOT_SAY', label: 'Cannot Say', cls: 'c' },
];

const app = document.getElementById('app');
let state = {
  screen: 'home',
  moduleId: 'numerical',
  tier: null, flavor: '',
  options: { wrongTabPenalty: true, allowBack: true },
  session: null, answers: [], current: 0, activeTab: 0,
  timer: null, deadline: 0, enterTs: 0, expired: false, mode: null,
  lastScore: null, progressModule: 'numerical',
};
let calc = null;

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const fmtTime = (s) => `${Math.floor(s / 60)}:${String(Math.max(0, s % 60)).padStart(2, '0')}`;
const pct = (x) => `${Math.round(x * 100)}%`;
const activeModule = () => moduleById[state.moduleId];

function topbar(right = '') {
  return `<div class="topbar"><div class="brand">Aon scales · <small>trainer</small></div><div class="meta">${right}</div></div>`;
}
function render() {
  if (state.screen !== 'test' && calc) hideCalc();
  app.innerHTML = ({ home: renderHome, test: renderTest, results: renderResults, progress: renderProgress, guide: renderGuide }[state.screen])();
  wire();
}

// =============================================================================
// HOME — a progress dashboard on top, then the session launcher
// =============================================================================
function renderHome() {
  const m = activeModule();
  if (!state.tier || !m.tiers.includes(state.tier)) state.tier = m.tiers[Math.min(1, m.tiers.length - 1)];
  const chips = MODULES.map((mod) =>
    `<button class="modchip${mod.id === state.moduleId ? ' active' : ''}" data-mod="${mod.id}">${esc(mod.label)}</button>`).join('');
  const cards = m.modes.map((mode) => `
    <div class="mode-card">
      <h3>${esc(mode.label)}${mode.nonstandard ? ' <span class="pill">non-standard</span>' : ''}${mode.adaptive ? ' <span class="pill">adaptive</span>' : ''}</h3>
      <div class="spec">${esc(mode.desc)}</div>
      <div style="margin-top:10px"><button class="btn" data-start="${mode.key}">Start</button></div>
    </div>`).join('');

  return `${topbar('')}
  ${renderDashboard()}
  <div class="panel">
    <h2 style="margin-top:0">Start a session</h2>
    <div class="modchips">${chips}</div>
    <div class="module-head"><strong>${esc(m.label)}</strong> — ${esc(m.blurb)}</div>
    <div class="controls" style="margin:12px 0">
      <label class="chk">Difficulty
        <select data-tier>${m.tiers.map((t) => `<option value="${t}"${t === state.tier ? ' selected' : ''}>${t}</option>`).join('')}</select>
      </label>
      ${m.flavors ? `<label class="chk">Sector
        <select data-flavor>${m.flavors.map((f) => `<option value="${f.key}"${f.key === (state.flavor || '') ? ' selected' : ''}>${esc(f.label)}</option>`).join('')}</select>
      </label>` : ''}
      ${m.usesTabs ? `<label class="chk"><input type="checkbox" data-opt="wrongTabPenalty"${state.options.wrongTabPenalty ? ' checked' : ''}/> Wrong-tab penalty</label>` : ''}
      <label class="chk"><input type="checkbox" data-opt="allowBack"${state.options.allowBack ? ' checked' : ''}/> Allow going back</label>
    </div>
    <div class="mode-grid">${cards}</div>
    <div class="banner">Preparation only — a practice simulator, not affiliated with Aon, with no live-test answer lookup. The Stanine/percentile after a session is an illustrative synthetic estimate. See the Guide’s integrity note on why practising the skill (not memorising) is what actually transfers.</div>
  </div>`;
}

// The dashboard: at-a-glance progress across every module, with quick actions.
function renderDashboard() {
  const data = load();
  const active = MODULES.filter((mod) => data.byModule[mod.id] && data.byModule[mod.id].seen);

  if (!active.length) {
    return `<div class="panel dash-empty">
      <h2 style="margin-top:0">Your dashboard</h2>
      <p class="muted">No sessions yet. Pick a test below and start a drill — your accuracy, weakest areas, and trend will appear here so you can track progress at a glance.</p>
      <div class="controls"><span class="btn ghost" data-nav="guide">Read the guide first</span></div>
    </div>`;
  }

  // overall totals
  let seen = 0, correct = 0;
  for (const mod of active) { const b = data.byModule[mod.id]; seen += b.seen; correct += b.correct; }
  const sessions = data.sessions.length;
  const overallAcc = seen ? correct / seen : 0;
  const todayISO = new Date().toISOString().slice(0, 10);
  const today = data.sessions.filter((s) => (s.date || '').slice(0, 10) === todayISO).length;

  const cards = active.map((mod) => {
    const b = data.byModule[mod.id];
    const acc = b.seen ? b.correct / b.seen : 0;
    const modSessions = data.sessions.filter((s) => s.module === mod.id);
    const hist = data.history.filter((h) => h.module === mod.id).slice(-14);
    const maxH = Math.max(...hist.map((h) => h.accuracy), 1);
    const spark = hist.map((h) => `<div class="b" style="height:${Math.max(3, h.accuracy / maxH * 40)}px" title="${pct(h.accuracy)}"></div>`).join('');
    const last = modSessions[modSessions.length - 1];
    const weak = weakestWithStats(mod.id, data, 1)[0];
    const accCls = acc < 0.5 ? 'bad' : acc < 0.75 ? 'warn' : 'good';
    return `<div class="dash-card">
      <div class="dash-top"><span class="dash-name">${esc(mod.label)}</span><span class="dash-acc ${accCls}">${pct(acc)}</span></div>
      <div class="spark mini">${spark || ''}</div>
      <div class="dash-meta">${modSessions.length} session${modSessions.length !== 1 ? 's' : ''} · ${b.seen} items${last ? ` · last Stanine ${last.stanine}` : ''}</div>
      ${weak ? `<div class="dash-weak">Focus: <strong>${esc(weak.skill)}</strong> (${pct(weak.accuracy)})</div>` : '<div class="dash-weak muted">Keep drilling to surface weak spots.</div>'}
      <div class="dash-actions">
        <button class="btn secondary" data-mod="${mod.id}">Practise</button>
        ${mod.adaptive ? `<button class="btn" data-drillmod="${mod.id}">Drill weakest ▶</button>` : ''}
      </div>
    </div>`;
  }).join('');

  return `<div class="panel">
    <div class="dash-head">
      <h2 style="margin:0">Your dashboard</h2>
      <div class="dash-summary">
        <span><strong>${sessions}</strong> sessions</span>
        <span><strong>${seen}</strong> items</span>
        <span><strong>${pct(overallAcc)}</strong> overall</span>
        ${today ? `<span class="muted">${today} today</span>` : ''}
        <span class="btn ghost" data-nav="progress">Full progress</span>
        <span class="btn ghost" data-nav="guide">Guide</span>
      </div>
    </div>
    <div class="dash-grid">${cards}</div>
  </div>`;
}

// =============================================================================
// TEST
// =============================================================================
function startSession(modeKey) {
  const m = activeModule();
  const mode = m.modes.find((x) => x.key === modeKey);
  const seed = `${Date.now()}-${Math.floor(performance.now())}`;
  let opts = { seed, tier: state.tier, count: mode.count };
  if (m.flavors && state.flavor) opts.flavor = state.flavor;
  if (mode.adaptive && m.adaptive) opts = { ...opts, ...m.adaptive(load()) };
  const session = m.generate(opts);
  if (!session.items.length) { alert('Could not generate items — try another difficulty.'); return; }

  state.session = session;
  state.mode = mode;
  state.answers = session.items.map(() => ({ given: null, timeMs: 0, submittedTab: null }));
  state.current = 0; state.activeTab = 0; state.expired = false;
  state.screen = 'test';
  state.enterTs = performance.now();
  clearInterval(state.timer);
  if (mode.timed) startTimer(mode.time);
  render();
}

function startTimer(seconds) {
  clearInterval(state.timer);
  state.deadline = Date.now() + seconds * 1000;
  state.timer = setInterval(() => {
    const remaining = Math.round((state.deadline - Date.now()) / 1000);
    const el = document.querySelector('.timer');
    if (el) {
      el.textContent = fmtTime(remaining);
      el.classList.toggle('warn', remaining <= 60 && remaining > 20);
      el.classList.toggle('crit', remaining <= 20);
    }
    updatePace(remaining);
    if (remaining <= 0) { state.expired = true; finish(); }
  }, 250);
}

// Live pacing pressure: where you SHOULD be by now vs where you are, plus the
// seconds-per-task budget your remaining time actually allows. The real test is
// lost on pace, not knowledge — this keeps the clock in your face the whole way.
function updatePace(remaining) {
  const el = document.querySelector('[data-pace]');
  if (!el || !state.mode || !state.mode.timed || !state.session) return;
  const total = state.mode.time;
  const count = state.session.items.length;
  const elapsed = Math.max(0, total - remaining);
  const target = Math.min(count, Math.floor((elapsed / total) * count) + 1);
  const onQ = state.current + 1;
  const unanswered = state.answers.filter((a) => a.given == null).length;
  const perTask = unanswered > 0 ? Math.max(0, remaining) / unanswered : 0;
  const behind = target - onQ;
  el.textContent = behind >= 2
    ? `⏱ behind pace — target Q${target} · ${perTask.toFixed(0)}s/task left`
    : behind <= -2
      ? `ahead of pace · ${perTask.toFixed(0)}s/task left`
      : `on pace · target Q${target} · ${perTask.toFixed(0)}s/task left`;
  el.classList.toggle('behind', behind >= 2);
  el.classList.toggle('ahead', behind <= -2);
}

function renderTest() {
  const m = activeModule();
  const { session, current } = state;
  const item = session.items[current];
  const given = state.answers[current].given;
  const right = state.mode.timed
    ? `<span class="pacechip" data-pace></span><span class="timer">${fmtTime(Math.round((state.deadline - Date.now()) / 1000))}</span>`
    : '<span class="muted">untimed</span>';

  // display area
  let displayHtml;
  if (m.usesTabs) {
    const tabs = session.context.tabs.map((t, i) => `<div class="tab${i === state.activeTab ? ' active' : ''}" data-tab="${i}">${esc(t.title)}</div>`).join('');
    displayHtml = `<div class="tabs">${tabs}</div><div class="display-area">${session.context.tabs[state.activeTab].html}</div>`;
  } else {
    displayHtml = `<div class="display-area stage">${m.renderDisplay(item, session, { given })}</div>`;
  }

  // answer controls
  const controls = m.answerKind === 'tfc'
    ? `<div class="answers">${TFC.map((a) => `<div class="ans ${a.cls}${given === a.v ? ' sel' : ''}" data-ans="${a.v}">${a.label}</div>`).join('')}</div>`
    : m.renderControls(item, session, { given });

  const dots = session.items.map((_, i) =>
    `<div class="pdot${state.answers[i].given != null ? ' answered' : ''}${i === current ? ' current' : ''}" data-goto="${i}">${i + 1}</div>`).join('');

  const calcBtn = m.id === 'numerical' ? '<button class="btn secondary calc-toggle" data-calc>🖩 Calculator</button>' : '';
  const tip = state.mode.exam
    ? 'Exam simulation: answering moves you straight on and there is no going back. Decide, click, move — Skip anything not cracked in ~30s. Blanks 0, wrong −1.'
    : m.usesTabs
      ? 'Confirm the correct tab is showing before you answer — the wrong tab up can cost points. Blanks score 0; wrong answers −1, so skip rather than guess blindly.'
      : 'Blanks score 0; wrong answers score −1. If you can’t reason it out, skip rather than guess blindly.';

  return `${topbar(`<span class="muted">Question ${current + 1} / ${session.items.length}</span>${right}`)}
  <div class="panel">
    ${displayHtml}
    <div class="statement">${esc(item.prompt)}</div>
    ${controls}
    <div class="navbar">
      <div>
        ${state.options.allowBack && state.mode.allowBack ? '<button class="btn secondary" data-prev>◀ Prev</button>' : ''}
        <button class="btn ghost" data-skip>Skip</button>${calcBtn}
      </div>
      <div class="progress-dots">${dots}</div>
      <div>${current < session.items.length - 1 ? '<button class="btn" data-next>Next ▶</button>' : '<button class="btn" data-finish>Finish ▶</button>'}</div>
    </div>
  </div>
  <div class="panel small muted">${tip}</div>`;
}

function selectAnswer(token) {
  const m = activeModule();
  const a = state.answers[state.current];
  a.given = token;
  a.submittedTab = m.usesTabs ? state.session.context.tabs[state.activeTab].id : null;
  // Exam simulation: answering commits you — auto-advance, no going back. This
  // is the real test's rhythm: decide, click, move on.
  if (state.mode && state.mode.exam && state.current < state.session.items.length - 1) {
    render();
    setTimeout(() => { if (state.screen === 'test') goTo(state.current + 1); }, 160);
    return;
  }
  render();
}
function accrueTime() {
  const now = performance.now();
  state.answers[state.current].timeMs += now - state.enterTs;
  state.enterTs = now;
}
function goTo(i) {
  accrueTime();
  state.current = Math.max(0, Math.min(state.session.items.length - 1, i));
  state.enterTs = performance.now();
  render();
}

// =============================================================================
// FINISH + SCORE
// =============================================================================
function finish() {
  clearInterval(state.timer);
  accrueTime();
  state.answers.forEach((a) => { a.ranOutOfTime = !!(state.mode.timed && state.expired && a.given == null); });
  const m = activeModule();
  const score = scoreSession(state.session, state.answers, { wrongTabPenalty: state.options.wrongTabPenalty }, m);
  recordSession(score, { module: m.id, mode: state.mode.key, tier: state.tier, dateISO: new Date().toISOString() });
  state.lastScore = score;
  state.screen = 'results';
  render();
}

// =============================================================================
// RESULTS
// =============================================================================
function renderResults() {
  const m = activeModule();
  const s = state.lastScore;
  const stat = (n, l, cls = '') => `<div class="stat ${cls}"><div class="n">${n}</div><div class="l">${l}</div></div>`;
  const scorebar = `<div class="scorebar">
    ${stat(s.correct, 'correct', 'good')}${stat(s.wrong, 'wrong (−1)', 'bad')}${stat(s.blank, 'blank (0)')}
    ${stat(s.adjustedScore, 'net score')}${stat(pct(s.accuracyAttempted), 'accuracy')}${stat(pct(s.coverage), 'coverage')}</div>`;

  const gap = s.naiveScore - s.adjustedScore;
  const penaltyNote = `<div class="banner">Naive “count correct” would be <strong>${s.naiveScore}</strong>. With negative marking${s.tabPenalty ? ' and the wrong-tab penalty' : ''}, your net score is <strong>${s.adjustedScore}</strong> — a <strong>${gap}</strong>-point gap.
    ${s.wrong ? `${s.wrong} wrong answer${s.wrong > 1 ? 's' : ''} cost ${s.wrong}; a blank would have cost 0.` : ''}${s.wrongTabEvents ? ` ${s.wrongTabEvents} answered on the wrong tab cost ${s.tabPenalty} more.` : ''}</div>`;

  const norm = `<div class="row" style="align-items:center;margin-top:12px">
    <div class="stat" style="flex:0 0 160px"><div class="stanine-badge">${s.stanine}</div><div class="l">Stanine (1–9) · ${esc(s.stanineLabel)}</div></div>
    <div class="col"><div><strong>≈ ${s.percentile}th percentile</strong> <span class="muted small">(illustrative synthetic norm — not an official Aon result)</span></div>
    <div class="muted small" style="margin-top:6px">Avg time/attempted: ${(s.avgTimeMs / 1000).toFixed(1)}s. On the real test you are not expected to finish — accuracy beats coverage.</div></div></div>`;

  const reasons = Object.entries(s.reasonTally).filter(([k]) => k !== 'correct_fast').sort((a, b) => b[1] - a[1]);
  const reasonList = reasons.length ? `<h3>Where the points went</h3><div>${reasons.map(([k, n]) =>
    `<div class="bar-row"><div class="bar-label">${esc(REASONS[k]?.label || k)}</div><div class="bar-track"><div class="bar-fill" style="width:${Math.min(100, n / s.count * 100)}%"></div></div><div class="bar-num">${n}</div></div>`).join('')}</div>` : '';

  const review = s.perItem.map((p) => renderReviewItem(m, p)).join('');

  return `${topbar(`<span class="btn ghost" data-nav="home">Home</span>`)}
  <div class="panel">
    <h2 style="margin-top:0">${esc(m.label)} — session review · ${esc(state.tier)}</h2>
    ${scorebar}${penaltyNote}${norm}${reasonList}
    <div class="controls" style="margin-top:14px">
      ${m.adaptive ? '<button class="btn" data-drill>Drill my weakest areas ▶</button>' : ''}
      <button class="btn secondary" data-nav="progress">See progress</button>
      <button class="btn ghost" data-nav="home">Back to home</button>
    </div>
  </div>
  <div class="panel"><h3 style="margin-top:0">Per-question worked solutions</h3>
    <p class="muted small">Click any question to expand the explanation and diagnosis.</p>${review}</div>`;
}

function renderReviewItem(m, p) {
  const item = p.item;
  const correct = p.correctToken;
  const cls = p.isBlank ? 'blankh' : p.isCorrect ? 'correct' : 'wrong';
  const your = p.isBlank ? '—' : m.tokenLabel(p.given, item);
  const rightLabel = m.tokenLabel(correct, item);
  const pillCls = m.answerKind === 'tfc' ? { TRUE: 't', FALSE: 'f', CANNOT_SAY: 'c' }[correct] : '';
  const timeStr = p.timeMs != null ? `${(p.timeMs / 1000).toFixed(1)}s` : '';
  return `<div class="review-item">
    <div class="review-head ${cls}" data-toggle>
      <div><span class="pill ${pillCls}">${esc(rightLabel)}</span> &nbsp;${esc(item.prompt)}</div>
      <div class="small muted" style="white-space:nowrap">you: <strong>${esc(your)}</strong> ${p.wrongTab ? '· ⚠ wrong tab' : ''} ${timeStr ? '· ' + timeStr : ''}</div>
    </div>
    <div class="review-body">${m.renderReview(item, p, state.session)}</div>
  </div>`;
}

// =============================================================================
// PROGRESS
// =============================================================================
function renderProgress() {
  const data = load();
  const modsWithData = MODULES.filter((m) => data.byModule[m.id] && data.byModule[m.id].seen);
  if (!modsWithData.length) {
    return `${topbar(`<span class="btn ghost" data-nav="home">Home</span>`)}<div class="panel"><h2>Progress</h2>
      <p class="muted">No sessions yet — complete a drill and your stats appear here.</p><button class="btn" data-nav="home">Start practising</button></div>`;
  }
  if (!data.byModule[state.progressModule]) state.progressModule = modsWithData[0].id;
  const pm = state.progressModule;

  const overall = MODULES.map((m) => {
    const b = data.byModule[m.id];
    if (!b || !b.seen) return '';
    const acc = b.correct / b.seen;
    return `<div class="bar-row"><div class="bar-label">${esc(m.label)}</div>
      <div class="bar-track"><div class="bar-fill" style="width:${acc * 100}%;background:${acc < .5 ? 'var(--bad)' : acc < .75 ? 'var(--warn)' : 'var(--ok)'}"></div></div>
      <div class="bar-num">${pct(acc)} · ${b.seen}</div></div>`;
  }).join('');

  const skills = Object.entries(data.bySkill).filter(([k]) => k.startsWith(`${pm}:`))
    .map(([k, b]) => ({ skill: k.slice(pm.length + 1), acc: b.seen ? b.correct / b.seen : 0, seen: b.seen }))
    .sort((a, b) => a.acc - b.acc);
  const skillBars = skills.map((s) => `<div class="bar-row"><div class="bar-label">${esc(s.skill)}</div>
    <div class="bar-track"><div class="bar-fill" style="width:${s.acc * 100}%;background:${s.acc < .5 ? 'var(--bad)' : s.acc < .75 ? 'var(--warn)' : 'var(--ok)'}"></div></div>
    <div class="bar-num">${pct(s.acc)} · ${s.seen}</div></div>`).join('');

  const hist = data.history.filter((h) => h.module === pm).slice(-24);
  const maxH = Math.max(...hist.map((h) => h.accuracy), 1);
  const spark = hist.map((h) => `<div class="b" style="height:${Math.max(3, h.accuracy / maxH * 60)}px" title="${new Date(h.date).toLocaleDateString()}: ${pct(h.accuracy)} · Stanine ${h.stanine}"></div>`).join('');
  const weak = weakestWithStats(pm, data, 3);
  const modTabs = modsWithData.map((m) => `<button class="modchip${m.id === pm ? ' active' : ''}" data-pmod="${m.id}">${esc(m.label)}</button>`).join('');

  return `${topbar(`<span class="btn ghost" data-nav="home">Home</span>`)}
  <div class="panel"><h2 style="margin-top:0">Progress</h2>
    <h3>Accuracy by test type</h3>${overall}
    <div class="modchips" style="margin-top:16px">${modTabs}</div>
    <div class="row">
      <div class="col"><h3>${esc(moduleById[pm].label)} — accuracy by skill</h3>${skillBars || '<p class="muted small">Not enough data yet.</p>'}</div>
      <div class="col"><h3>Accuracy trend</h3><div class="spark">${spark || '<span class="muted small">—</span>'}</div>
        ${weak.length ? `<p class="muted small" style="margin-top:12px">Weakest: ${weak.map((w) => `${esc(w.skill)} (${pct(w.accuracy)})`).join(', ')}.</p>` : ''}
      </div>
    </div>
    <div class="controls" style="margin-top:14px">
      ${moduleById[pm].adaptive ? `<button class="btn" data-drillmod="${pm}">Adaptive drill on ${esc(moduleById[pm].label)} ▶</button>` : ''}
      <button class="btn ghost" data-reset>Reset all progress</button>
    </div>
  </div>`;
}

// =============================================================================
// GUIDE
// =============================================================================
function renderGuide() {
  return `${topbar(`<span class="btn ghost" data-nav="home">Home</span>`)}
  <div class="panel guide">${mdToHtml(guideMd)}</div>
  <div class="panel"><button class="btn" data-nav="home">Back to home</button></div>`;
}
function mdToHtml(md) {
  const lines = md.replace(/\r/g, '').split('\n');
  let html = '', inList = false, inTable = false;
  const inline = (s) => esc(s).replace(/`([^`]+)`/g, '<code>$1</code>').replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/\*([^*]+)\*/g, '<em>$1</em>').replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  const closeList = () => { if (inList) { html += '</ul>'; inList = false; } };
  const closeTable = () => { if (inTable) { html += '</tbody></table>'; inTable = false; } };
  for (const line of lines) {
    if (/^\|/.test(line)) {
      if (/^[-:\s|]+$/.test(line.replace(/\|/g, ''))) continue;
      if (!inTable) { closeList(); html += '<table><tbody>'; inTable = true; }
      const cells = line.split('|').slice(1, -1).map((c) => c.trim());
      html += `<tr>${cells.map((c) => `<td>${inline(c)}</td>`).join('')}</tr>`;
      continue;
    } else closeTable();
    if (/^### /.test(line)) { closeList(); html += `<h3>${inline(line.slice(4))}</h3>`; }
    else if (/^## /.test(line)) { closeList(); html += `<h2>${inline(line.slice(3))}</h2>`; }
    else if (/^# /.test(line)) { closeList(); html += `<h1>${inline(line.slice(2))}</h1>`; }
    else if (/^> /.test(line)) { closeList(); html += `<blockquote>${inline(line.slice(2))}</blockquote>`; }
    else if (/^(---|___)\s*$/.test(line)) { closeList(); html += '<hr/>'; }
    else if (/^\s*[-*] /.test(line)) { if (!inList) { html += '<ul>'; inList = true; } html += `<li>${inline(line.replace(/^\s*[-*] /, ''))}</li>`; }
    else if (/^\s*\d+\. /.test(line)) { if (!inList) { html += '<ul>'; inList = true; } html += `<li>${inline(line.replace(/^\s*\d+\. /, ''))}</li>`; }
    else if (line.trim() === '') closeList();
    else { closeList(); html += `<p>${inline(line)}</p>`; }
  }
  closeList(); closeTable();
  return html;
}

// =============================================================================
// CALCULATOR
// =============================================================================
function showCalc() { if (!calc) calc = createCalculator(); document.body.appendChild(calc); document.addEventListener('keydown', calc._onKey); }
function hideCalc() { if (calc && calc.parentNode) { calc.parentNode.removeChild(calc); document.removeEventListener('keydown', calc._onKey); } }

// =============================================================================
// EVENT WIRING
// =============================================================================
function wire() {
  app.querySelectorAll('[data-nav]').forEach((el) => (el.onclick = () => { state.screen = el.dataset.nav; render(); }));

  if (state.screen === 'home') {
    app.querySelectorAll('[data-mod]').forEach((el) => (el.onclick = () => { state.moduleId = el.dataset.mod; state.tier = null; render(); }));
    app.querySelectorAll('[data-start]').forEach((el) => (el.onclick = () => startSession(el.dataset.start)));
    app.querySelectorAll('[data-drillmod]').forEach((el) => (el.onclick = () => startAdaptive(el.dataset.drillmod)));
    const tierSel = app.querySelector('[data-tier]');
    if (tierSel) tierSel.onchange = () => { state.tier = tierSel.value; };
    const flavSel = app.querySelector('[data-flavor]');
    if (flavSel) flavSel.onchange = () => { state.flavor = flavSel.value; };
    app.querySelectorAll('[data-opt]').forEach((el) => (el.onchange = () => { state.options[el.dataset.opt] = el.checked; }));
  }

  if (state.screen === 'test') {
    const m = activeModule();
    app.querySelectorAll('[data-tab]').forEach((el) => (el.onclick = () => { state.activeTab = +el.dataset.tab; render(); }));
    app.querySelectorAll('[data-ans]').forEach((el) => (el.onclick = () => selectAnswer(el.dataset.ans)));
    const next = app.querySelector('[data-next]'); if (next) next.onclick = () => goTo(state.current + 1);
    const prev = app.querySelector('[data-prev]'); if (prev) prev.onclick = () => goTo(state.current - 1);
    const skip = app.querySelector('[data-skip]'); if (skip) skip.onclick = () => goTo(state.current + 1);
    const fin = app.querySelector('[data-finish]'); if (fin) fin.onclick = () => finish();
    app.querySelectorAll('[data-goto]').forEach((el) => (el.onclick = () => { if ((state.options.allowBack && state.mode.allowBack) || +el.dataset.goto >= state.current) goTo(+el.dataset.goto); }));
    const calcBtn = app.querySelector('[data-calc]'); if (calcBtn) calcBtn.onclick = () => (calc && calc.parentNode ? hideCalc() : showCalc());
    if (m.wireQuestion) m.wireQuestion(app, state.session.items[state.current], state.session, { select: selectAnswer, rerender: render });
  }

  if (state.screen === 'results' || state.screen === 'progress') {
    app.querySelectorAll('[data-toggle]').forEach((el) => (el.onclick = () => el.nextElementSibling.classList.toggle('open')));
    const drill = app.querySelector('[data-drill]'); if (drill) drill.onclick = () => startAdaptive(state.moduleId);
    app.querySelectorAll('[data-drillmod]').forEach((el) => (el.onclick = () => startAdaptive(el.dataset.drillmod)));
    app.querySelectorAll('[data-pmod]').forEach((el) => (el.onclick = () => { state.progressModule = el.dataset.pmod; render(); }));
    const rst = app.querySelector('[data-reset]'); if (rst) rst.onclick = () => { if (confirm('Erase all saved progress?')) { reset(); render(); } };
  }
}

function startAdaptive(moduleId) {
  state.moduleId = moduleId;
  const m = activeModule();
  if (!state.tier || !m.tiers.includes(state.tier)) state.tier = m.tiers[Math.min(1, m.tiers.length - 1)];
  const adaptiveMode = m.modes.find((x) => x.adaptive);
  startSession(adaptiveMode ? adaptiveMode.key : m.modes[0].key);
}

window.addEventListener('beforeunload', (e) => { if (state.screen === 'test') { e.preventDefault(); e.returnValue = ''; } });

render();
