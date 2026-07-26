// -----------------------------------------------------------------------------
// shapes.js — plain, legible SVG shape primitives shared by the visual modules
// (lst shape-sudoku, ix odd-one-out, cls grid categorisation).
//
// Deliberately boring and geometric, like the real cut-e "shapes" tests: solid
// or outlined regular polygons, a few glyphs, optional rotation and an optional
// inner (nested) shape. Everything is a pure string builder — no dependencies.
// -----------------------------------------------------------------------------

// A muted, colour-blind-friendly-ish set. Index 0 is the default "ink".
export const SHAPE_COLORS = ['#3a3f47', '#4a6785', '#8a6d3b', '#5f8a5f', '#8a5f7a', '#5f7f8a'];

// Regular-polygon vertex count by name; 'circle' and 'star'/'cross' are special.
const POLY = { triangle: 3, square: 4, pentagon: 5, hexagon: 6, heptagon: 7, octagon: 8 };
export const SHAPE_NAMES = ['circle', 'triangle', 'square', 'pentagon', 'hexagon', 'star', 'cross', 'diamond'];

function polyPoints(sides, r, cx, cy, rotDeg = 0) {
  const pts = [];
  const off = (rotDeg * Math.PI) / 180 - Math.PI / 2; // start at top
  for (let i = 0; i < sides; i++) {
    const a = off + (i * 2 * Math.PI) / sides;
    pts.push(`${(cx + r * Math.cos(a)).toFixed(1)},${(cy + r * Math.sin(a)).toFixed(1)}`);
  }
  return pts.join(' ');
}

function starPoints(cx, cy, rOuter, rInner, rotDeg = 0) {
  const pts = [];
  const off = (rotDeg * Math.PI) / 180 - Math.PI / 2;
  for (let i = 0; i < 10; i++) {
    const r = i % 2 === 0 ? rOuter : rInner;
    const a = off + (i * Math.PI) / 5;
    pts.push(`${(cx + r * Math.cos(a)).toFixed(1)},${(cy + r * Math.sin(a)).toFixed(1)}`);
  }
  return pts.join(' ');
}

/**
 * Draw one shape as inner SVG markup (no <svg> wrapper).
 * @param {object} o { shape, color, filled, rotation, size, cx, cy, scale }
 */
export function shapeMarkup(o = {}) {
  const {
    shape = 'circle', color = SHAPE_COLORS[0], filled = true,
    rotation = 0, cx = 30, cy = 30, size = 22,
  } = o;
  const stroke = color;
  const fill = filled ? color : 'none';
  const sw = filled ? 1 : 2.4;
  const common = `fill="${fill}" stroke="${stroke}" stroke-width="${sw}" stroke-linejoin="round"`;

  if (shape === 'circle') return `<circle cx="${cx}" cy="${cy}" r="${size}" ${common}/>`;
  if (shape === 'star') return `<polygon points="${starPoints(cx, cy, size, size * 0.45, rotation)}" ${common}/>`;
  if (shape === 'cross') {
    const t = size * 0.36; // arm half-thickness
    const s = size;
    const p = [
      [-t, -s], [t, -s], [t, -t], [s, -t], [s, t], [t, t], [t, s], [-t, s],
      [-t, t], [-s, t], [-s, -t], [-t, -t],
    ].map(([x, y]) => rot(x, y, rotation, cx, cy)).join(' ');
    return `<polygon points="${p}" ${common}/>`;
  }
  if (shape === 'diamond') return `<polygon points="${polyPoints(4, size, cx, cy, rotation + 0)}" ${common}/>`;
  const sides = POLY[shape] || 4;
  return `<polygon points="${polyPoints(sides, size, cx, cy, rotation)}" ${common}/>`;
}

function rot(x, y, deg, cx, cy) {
  const a = (deg * Math.PI) / 180;
  const rx = x * Math.cos(a) - y * Math.sin(a);
  const ry = x * Math.sin(a) + y * Math.cos(a);
  return `${(cx + rx).toFixed(1)},${(cy + ry).toFixed(1)}`;
}

/**
 * A composite "object" for ix: an outer shape optionally containing an inner one,
 * with fill/rotation/count attributes. Returns a full <svg> cell.
 * @param {object} obj { shape, color, filled, rotation, inner?, box }
 */
export function objectSvg(obj, box = 76) {
  const c = box / 2;
  let body = shapeMarkup({ ...obj, cx: c, cy: c, size: box * 0.34 });
  if (obj.inner) {
    body += shapeMarkup({ shape: obj.inner, color: obj.innerColor || obj.color, filled: obj.innerFilled ?? false, rotation: obj.rotation || 0, cx: c, cy: c, size: box * 0.16 });
  }
  return `<svg viewBox="0 0 ${box} ${box}" width="${box}" height="${box}" class="obj-svg">${body}</svg>`;
}

/** A single small shape as a full <svg> (used in grids and option buttons). */
export function shapeSvg(o, box = 44) {
  const c = box / 2;
  return `<svg viewBox="0 0 ${box} ${box}" width="${box}" height="${box}" class="shape-svg">${shapeMarkup({ ...o, cx: c, cy: c, size: box * 0.34 })}</svg>`;
}
