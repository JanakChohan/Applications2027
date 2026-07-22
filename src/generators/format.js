// -----------------------------------------------------------------------------
// format.js — value formatting shared by charts, item text, and the coaching
// worked-solutions. Kept tiny and dependency-free.
//
// Every metric carries a `unit` descriptor:
//   { kind:'currency'|'count'|'percent'|'index', symbol, scale, decimals, label, word }
// where `scale` converts a BASE-unit value into the DISPLAYED number:
//   displayed = base / scale     (e.g. base 7,256,000 / 1e6 = 7.26 shown as "$ million")
// -----------------------------------------------------------------------------

/** Group digits with thousands separators. */
export function group(n, decimals = 0) {
  const fixed = Number(n).toFixed(decimals);
  const [int, frac] = fixed.split('.');
  const withSep = int.replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  return frac ? `${withSep}.${frac}` : withSep;
}

/** The number as it appears ON the chart/table (display units, no unit word). */
export function displayNumber(unit, base) {
  const d = base / unit.scale;
  return group(d, unit.decimals);
}

/** Full standalone label of a value, e.g. "$7.3m", "12.4%", "1,550,000". */
export function formatValue(unit, base) {
  switch (unit.kind) {
    case 'currency': {
      const d = base / unit.scale;
      return `${unit.symbol}${group(d, unit.decimals)}${shortMoneySuffix(unit.scale)}`;
    }
    case 'percent':
      return `${group(base, unit.decimals)}%`;
    case 'index':
      return `${group(base, unit.decimals)}`;
    case 'count':
    default:
      return group(base, unit.decimals);
  }
}

function shortMoneySuffix(scale) {
  if (scale === 1e9) return 'bn';
  if (scale === 1e6) return 'm';
  if (scale === 1e3) return 'k';
  return '';
}

/**
 * Express a currency BASE value in a NAMED unit, for statement text and traps.
 * e.g. money(base=7256000, 'million', '$') -> "$7.26 million"
 *      money(base=7256000, 'thousand','$') -> "$7,256 thousand"
 */
export function money(base, word, symbol = '$', decimals) {
  const scale = word === 'billion' ? 1e9 : word === 'million' ? 1e6 : word === 'thousand' ? 1e3 : 1;
  const d = base / scale;
  const dec = decimals != null ? decimals : scale >= 1e6 ? 2 : 0;
  const w = word ? ` ${word}` : '';
  return `${symbol}${group(d, dec)}${w}`;
}

/** Plain count text, e.g. "1,550,000 employees". */
export function count(base, noun = '') {
  return `${group(base, 0)}${noun ? ' ' + noun : ''}`;
}

/** Percent text with fixed decimals. */
export function percent(base, decimals = 1) {
  return `${group(base, decimals)}%`;
}
