// -----------------------------------------------------------------------------
// charts.js — hand-rolled SVG charts that MATCH the real Aon scales numerical
// displays. Chart types and styling are taken from Aon's official practice PDF
// (5 worked examples) plus vendor descriptions — see the chart-types research:
//
//   • Plain data table — dark header row, bold "Total" row, units in a footnote.
//   • Doughnut (ring) chart — % labels by each arc, legend below, and an absolute
//     TOTAL caption underneath (the "$86 million" line the question logic needs).
//   • Stacked vertical bar — values printed INSIDE each segment, unit in the axis
//     title ("… in thousands").
//   • Grouped HORIZONTAL bar — category axis vertical, value axis horizontal with
//     its unit ("… in million"), value printed at the end of each bar.
//   • Line chart — a metric over time (vendor-attested).
//
// Styling signature replicated: flat 2D (no 3D/shadow), UPPERCASE chart titles,
// light horizontal gridlines only, small square legend below the plot, data values
// printed on the marks, and the unit carried in the axis title / table footnote —
// because reading the unit correctly is deliberately part of the test.
// -----------------------------------------------------------------------------

// Aon-like recurring palette: red, teal, green, orange, magenta/purple, blue.
const PALETTE = ['#c0392b', '#16a085', '#27ae60', '#e67e22', '#8e44ad', '#2980b9', '#c99700'];
const GRID = '#e2e2e2';
const AXIS_INK = '#555';

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

/** Build a {entities, periods, val(e,p)} view of a tab in DISPLAY units. */
function matrix(tab, dataset) {
  const scale = (dataset.units[tab.metric] || { scale: 1 }).scale;
  const map = new Map();
  for (const c of tab.cells) map.set(`${c.e}|${c.p}`, c.base / scale);
  return { entities: tab.entities, periods: tab.periods, val: (e, p) => map.get(`${e}|${p}`) };
}

function niceMax(v) {
  if (v <= 0) return 1;
  const mag = Math.pow(10, Math.floor(Math.log10(v)));
  const n = v / mag;
  const step = n <= 1 ? 1 : n <= 2 ? 2 : n <= 5 ? 5 : 10;
  return step * mag;
}

function fmt(n, decimals) {
  if (n == null) return '';
  const d = decimals != null ? decimals : Math.abs(n) >= 100 ? 0 : 1;
  return Number(n).toLocaleString('en-US', { maximumFractionDigits: d, minimumFractionDigits: 0 });
}

/** The unit phrase for an axis title, e.g. "in $ thousand", "in millions", "%". */
function unitAxisLabel(unit) {
  if (unit.kind === 'currency') return `in ${unit.symbol} ${unit.word}`;
  if (unit.kind === 'percent') return unit.label.includes('%') ? unit.label : '%';
  if (unit.kind === 'index') return 'index (base 100)';
  return unit.label ? `number of ${unit.label}` : 'count';
}

function footnote(tab) {
  const u = tab.unit;
  const label = u.kind === 'currency' ? `All data in ${u.symbol === '$' ? '' : u.symbol + ' '}${u.word} ${u.symbol === '$' ? 'dollars' : ''}`.replace(/\s+/g, ' ').trim()
    : u.kind === 'percent' ? `Figures in ${u.label}`
    : u.kind === 'index' ? 'Index, base 100 in first period'
    : `Figures: number of ${u.label}`;
  return `<div class="chart-foot">${esc(label)}</div>`;
}

// ---- dispatch ---------------------------------------------------------------
export function renderChart(tab, dataset) {
  const inner = (() => {
    switch (tab.chart) {
      case 'table': return renderTable(tab, dataset);
      case 'line': return renderLine(tab, dataset);
      case 'doughnut': return renderPie(tab, dataset, true);
      case 'pie': return renderPie(tab, dataset, false);
      case 'stackedBar': return renderStacked(tab, dataset);
      case 'groupedBarH': return renderGroupedH(tab, dataset);
      case 'bar': return renderBar(tab, dataset);
      case 'groupedBar':
      default: return renderGrouped(tab, dataset);
    }
  })();
  const cap = tab.caption
    ? `<div class="chart-caption">${esc(tab.caption.text)}: <strong>${esc(captionValue(tab))}</strong></div>`
    : '';
  const foot = tab.chart === 'table' || tab.chart === 'doughnut' || tab.chart === 'pie' ? footnote(tab) : '';
  return `<div class="chart-wrap"><div class="chart-title">${esc(tab.title)}</div>${inner}${cap}${foot}</div>`;
}

function captionValue(tab) {
  const u = tab.caption.unit;
  return `${u.symbol}${fmt(tab.caption.base / u.scale, u.decimals)}${u.scale >= 1e6 ? ' million' : u.scale >= 1e3 ? ' thousand' : ''}`;
}

// ---- table ------------------------------------------------------------------
function renderTable(tab, dataset) {
  const m = matrix(tab, dataset);
  const head = `<tr><th>${esc(dataset.meta.entityLabel)}</th>${m.periods.map((p) => `<th>${esc(p)}</th>`).join('')}</tr>`;
  const rows = m.entities.map((e) =>
    `<tr><td class="rowlab">${esc(e)}</td>${m.periods.map((p) => `<td>${fmt(m.val(e, p), tab.unit.decimals)}</td>`).join('')}</tr>`
  ).join('');
  let total = '';
  if (tab.hasTotal) {
    const cells = m.periods.map((p) => {
      let s = 0; for (const e of m.entities) s += m.val(e, p) || 0;
      return `<td>${fmt(s, tab.unit.decimals)}</td>`;
    }).join('');
    total = `<tr class="totalrow"><td class="rowlab">Total</td>${cells}</tr>`;
  }
  return `<div class="table-scroll"><table class="data-table aon">${head}${rows}${total}</table></div>`;
}

// ---- shared plot frame ------------------------------------------------------
function frame(w, h, pad) { return { w, h, pad, x0: pad.l, x1: w - pad.r, y0: h - pad.b, y1: pad.t }; }
function yAxis(f, max, decimals) {
  let g = '';
  for (let i = 0; i <= 4; i++) {
    const v = (max / 4) * i;
    const y = f.y0 - (f.y0 - f.y1) * (i / 4);
    g += `<line x1="${f.x0}" y1="${y}" x2="${f.x1}" y2="${y}" stroke="${GRID}"/>`;
    g += `<text x="${f.x0 - 6}" y="${y + 3}" text-anchor="end" class="axlab">${fmt(v, decimals)}</text>`;
  }
  return g;
}
/** Rotated value-axis title carrying the unit (the unit trap lives here). */
function vAxisTitle(f, text) {
  const cx = 12, cy = (f.y0 + f.y1) / 2;
  return `<text x="${cx}" y="${cy}" transform="rotate(-90 ${cx} ${cy})" text-anchor="middle" class="axtitle">${esc(text)}</text>`;
}

// ---- grouped vertical bar (deprioritised — kept as low-frequency filler) -----
function renderGrouped(tab, dataset) {
  const m = matrix(tab, dataset);
  const w = 470, h = 270, f = frame(w, h, { l: 58, r: 12, t: 18, b: 36 });
  let max = 0;
  for (const e of m.entities) for (const p of m.periods) max = Math.max(max, m.val(e, p) || 0);
  max = niceMax(max);
  const groups = m.periods.length, gw = (f.x1 - f.x0) / groups;
  const bw = Math.min(28, (gw - 8) / m.entities.length);
  let bars = '';
  m.periods.forEach((p, gi) => {
    const gx = f.x0 + gi * gw;
    m.entities.forEach((e, ei) => {
      const v = m.val(e, p) || 0;
      const bh = (f.y0 - f.y1) * (v / max);
      const x = gx + (gw - bw * m.entities.length) / 2 + ei * bw;
      bars += `<rect x="${x}" y="${f.y0 - bh}" width="${bw - 2}" height="${bh}" fill="${PALETTE[ei % PALETTE.length]}"><title>${esc(e)} ${esc(p)}: ${fmt(v)}</title></rect>`;
      if (m.entities.length <= 4) bars += `<text x="${x + (bw - 2) / 2}" y="${f.y0 - bh - 3}" text-anchor="middle" class="barval">${fmt(v)}</text>`;
    });
    bars += `<text x="${gx + gw / 2}" y="${f.y0 + 16}" text-anchor="middle" class="axlab">${esc(p)}</text>`;
  });
  return svg(w, h, yAxis(f, max, tab.unit.decimals) + vAxisTitle(f, unitAxisLabel(tab.unit)) + bars) + legend(m.entities);
}

// ---- grouped HORIZONTAL bar (Aon's FORECAST form) ---------------------------
function renderGroupedH(tab, dataset) {
  const m = matrix(tab, dataset);
  const w = 470, h = 280, f = frame(w, h, { l: 52, r: 40, t: 16, b: 34 });
  let max = 0;
  for (const e of m.entities) for (const p of m.periods) max = Math.max(max, m.val(e, p) || 0);
  max = niceMax(max);
  const groups = m.periods.length, gh = (f.y0 - f.y1) / groups;
  const bh = Math.min(16, (gh - 8) / m.entities.length);
  const X = (v) => f.x0 + (f.x1 - f.x0) * (v / max);
  let g = '';
  // vertical value gridlines + ticks along the bottom
  for (let i = 0; i <= 4; i++) {
    const v = (max / 4) * i, x = X(v);
    g += `<line x1="${x}" y1="${f.y1}" x2="${x}" y2="${f.y0}" stroke="${GRID}"/>`;
    g += `<text x="${x}" y="${f.y0 + 14}" text-anchor="middle" class="axlab">${fmt(v)}</text>`;
  }
  m.periods.forEach((p, gi) => {
    const gy = f.y1 + gi * gh;
    m.entities.forEach((e, ei) => {
      const v = m.val(e, p) || 0;
      const bw = (f.x1 - f.x0) * (v / max);
      const y = gy + (gh - bh * m.entities.length) / 2 + ei * bh;
      g += `<rect x="${f.x0}" y="${y}" width="${bw}" height="${bh - 2}" fill="${PALETTE[ei % PALETTE.length]}"><title>${esc(e)} ${esc(p)}: ${fmt(v)}</title></rect>`;
      g += `<text x="${f.x0 + bw + 3}" y="${y + bh - 4}" class="barval">${fmt(v)}</text>`;
    });
    g += `<text x="${f.x0 - 6}" y="${gy + gh / 2 + 3}" text-anchor="end" class="axlab">${esc(p)}</text>`;
  });
  // value-axis title centred under the plot
  g += `<text x="${(f.x0 + f.x1) / 2}" y="${h - 4}" text-anchor="middle" class="axtitle">${esc(cap1(unitAxisLabel(tab.unit)))}</text>`;
  return svg(w, h, g) + legend(m.entities);
}

// ---- single-series vertical bar (low-frequency) -----------------------------
function renderBar(tab, dataset) {
  const m = matrix(tab, dataset);
  const p = m.periods[m.periods.length - 1];
  const w = 470, h = 260, f = frame(w, h, { l: 58, r: 12, t: 18, b: 42 });
  let max = 0; for (const e of m.entities) max = Math.max(max, m.val(e, p) || 0);
  max = niceMax(max);
  const bw = (f.x1 - f.x0) / m.entities.length;
  let bars = '';
  m.entities.forEach((e, i) => {
    const v = m.val(e, p) || 0;
    const bh = (f.y0 - f.y1) * (v / max);
    const x = f.x0 + i * bw + bw * 0.2;
    bars += `<rect x="${x}" y="${f.y0 - bh}" width="${bw * 0.6}" height="${bh}" fill="${PALETTE[i % PALETTE.length]}"><title>${esc(e)}: ${fmt(v)}</title></rect>`;
    bars += `<text x="${x + bw * 0.3}" y="${f.y0 - bh - 3}" text-anchor="middle" class="barval">${fmt(v)}</text>`;
    bars += `<text x="${x + bw * 0.3}" y="${f.y0 + 16}" text-anchor="middle" class="axlab">${esc(e)}</text>`;
  });
  bars += `<text x="${(f.x0 + f.x1) / 2}" y="${h - 5}" text-anchor="middle" class="axtitle">${esc(p + ' · ' + unitAxisLabel(tab.unit))}</text>`;
  return svg(w, h, yAxis(f, max, tab.unit.decimals) + vAxisTitle(f, unitAxisLabel(tab.unit)) + bars);
}

// ---- line (periods on x, one line per entity) -------------------------------
function renderLine(tab, dataset) {
  const m = matrix(tab, dataset);
  const w = 470, h = 270, f = frame(w, h, { l: 58, r: 14, t: 18, b: 34 });
  let max = 0, min = Infinity;
  for (const e of m.entities) for (const p of m.periods) { const v = m.val(e, p); if (v != null) { max = Math.max(max, v); min = Math.min(min, v); } }
  const base0 = tab.unit.kind === 'index' ? Math.max(0, min * 0.9) : 0;
  const span = niceMax(max - base0) || 1;
  const X = (i) => f.x0 + (f.x1 - f.x0) * (m.periods.length === 1 ? 0.5 : i / (m.periods.length - 1));
  const Y = (v) => f.y0 - (f.y0 - f.y1) * ((v - base0) / span);
  let g = '';
  for (let i = 0; i <= 4; i++) {
    const y = f.y0 - (f.y0 - f.y1) * (i / 4);
    g += `<line x1="${f.x0}" y1="${y}" x2="${f.x1}" y2="${y}" stroke="${GRID}"/>`;
    g += `<text x="${f.x0 - 6}" y="${y + 3}" text-anchor="end" class="axlab">${fmt(base0 + span * (i / 4), tab.unit.decimals)}</text>`;
  }
  m.entities.forEach((e, ei) => {
    const pts = m.periods.map((p, i) => `${X(i)},${Y(m.val(e, p))}`).join(' ');
    g += `<polyline points="${pts}" fill="none" stroke="${PALETTE[ei % PALETTE.length]}" stroke-width="2"/>`;
    m.periods.forEach((p, i) => { g += `<circle cx="${X(i)}" cy="${Y(m.val(e, p))}" r="2.6" fill="${PALETTE[ei % PALETTE.length]}"><title>${esc(e)} ${esc(p)}: ${fmt(m.val(e, p))}</title></circle>`; });
  });
  m.periods.forEach((p, i) => { g += `<text x="${X(i)}" y="${f.y0 + 16}" text-anchor="middle" class="axlab">${esc(p)}</text>`; });
  g += vAxisTitle(f, unitAxisLabel(tab.unit));
  const leg = m.entities.length > 1 || m.entities[0] !== '__ALL__' ? legend(m.entities.map((e) => e === '__ALL__' ? tab.title : e)) : '';
  return svg(w, h, g) + leg;
}

// ---- stacked vertical bar (Aon's EMPLOYEES form, values inside segments) -----
function renderStacked(tab, dataset) {
  const m = matrix(tab, dataset);
  const w = 470, h = 270, f = frame(w, h, { l: 58, r: 12, t: 18, b: 34 });
  let max = 0;
  for (const p of m.periods) { let s = 0; for (const e of m.entities) s += m.val(e, p) || 0; max = Math.max(max, s); }
  max = niceMax(max);
  const bw = Math.min(48, (f.x1 - f.x0) / m.periods.length * 0.6);
  let g = yAxis(f, max, tab.unit.decimals) + vAxisTitle(f, unitAxisLabel(tab.unit));
  m.periods.forEach((p, gi) => {
    const cx = f.x0 + (f.x1 - f.x0) * ((gi + 0.5) / m.periods.length);
    let acc = 0;
    m.entities.forEach((e, ei) => {
      const v = m.val(e, p) || 0;
      const bh = (f.y0 - f.y1) * (v / max);
      const y = f.y0 - (f.y0 - f.y1) * (acc / max) - bh;
      g += `<rect x="${cx - bw / 2}" y="${y}" width="${bw}" height="${bh}" fill="${PALETTE[ei % PALETTE.length]}"><title>${esc(e)} ${esc(p)}: ${fmt(v)}</title></rect>`;
      if (bh > 14) g += `<text x="${cx}" y="${y + bh / 2 + 4}" text-anchor="middle" class="barval inseg">${fmt(v)}</text>`;
      acc += v;
    });
    g += `<text x="${cx}" y="${f.y0 + 16}" text-anchor="middle" class="axlab">${esc(p)}</text>`;
  });
  return svg(w, h, g) + legend(m.entities);
}

// ---- doughnut / pie (Aon's PRODUCT REVENUE form) ----------------------------
function renderPie(tab, dataset, doughnut) {
  const m = matrix(tab, dataset);
  const p = m.periods[m.periods.length - 1];
  const vals = m.entities.map((e) => Math.max(0, m.val(e, p) || 0));
  const total = vals.reduce((s, v) => s + v, 0) || 1;
  const cx = 140, cy = 132, r = 100, rInner = doughnut ? 52 : 0;
  let a0 = -Math.PI / 2, g = '';
  m.entities.forEach((e, i) => {
    const frac = vals[i] / total;
    const a1 = a0 + frac * Math.PI * 2;
    const large = a1 - a0 > Math.PI ? 1 : 0;
    const x0 = cx + r * Math.cos(a0), y0 = cy + r * Math.sin(a0);
    const x1 = cx + r * Math.cos(a1), y1 = cy + r * Math.sin(a1);
    const col = PALETTE[i % PALETTE.length];
    if (doughnut) {
      const ix0 = cx + rInner * Math.cos(a1), iy0 = cy + rInner * Math.sin(a1);
      const ix1 = cx + rInner * Math.cos(a0), iy1 = cy + rInner * Math.sin(a0);
      g += `<path d="M${x0},${y0} A${r},${r} 0 ${large} 1 ${x1},${y1} L${ix0},${iy0} A${rInner},${rInner} 0 ${large} 0 ${ix1},${iy1} Z" fill="${col}" stroke="#fff" stroke-width="1.5"><title>${esc(e)}: ${fmt(vals[i])}%</title></path>`;
    } else {
      g += `<path d="M${cx},${cy} L${x0},${y0} A${r},${r} 0 ${large} 1 ${x1},${y1} Z" fill="${col}" stroke="#fff" stroke-width="1.5"><title>${esc(e)}: ${fmt(vals[i])}%</title></path>`;
    }
    // % label just outside the arc
    const am = (a0 + a1) / 2, lr = r + 16;
    if (frac > 0.03) g += `<text x="${cx + lr * Math.cos(am)}" y="${cy + lr * Math.sin(am) + 3}" text-anchor="middle" class="pielab">${fmt(vals[i])}%</text>`;
    a0 = a1;
  });
  return svg(280, 264, g) + legend(m.entities);
}

// ---- helpers ----------------------------------------------------------------
function svg(w, h, body) {
  return `<svg viewBox="0 0 ${w} ${h}" class="chart-svg" role="img" preserveAspectRatio="xMidYMid meet">${body}</svg>`;
}
function legend(labels) {
  return `<div class="legend">${labels.map((l, i) =>
    `<span class="leg"><span class="swatch" style="background:${PALETTE[i % PALETTE.length]}"></span>${esc(l)}</span>`
  ).join('')}</div>`;
}
function cap1(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
