#!/usr/bin/env python3
"""Flag SVG text that spills outside its viewBox or collides with other text,
and HTML blocks wider than the printable column."""
import glob, os, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))
HTML = glob.glob(os.path.join(os.path.dirname(ROOT), "*Complete_Interview_Pack.html"))[0]
CHROME = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome")[0]

JS = r"""
() => {
  const out = [];
  document.querySelectorAll('figure svg, svg.chk').forEach((svg, si) => {
    const vb = svg.viewBox.baseVal;
    const fig = svg.closest('figure');
    const id = (fig && fig.id) || ('svg#' + si);
    const boxes = [];
    svg.querySelectorAll('rect,circle').forEach(r => {
      let b; try { b = r.getBBox(); } catch(e) { return; }
      const m = r.getCTM(); const sm = svg.getCTM().inverse(); const pt = svg.createSVGPoint();
      pt.x = b.x; pt.y = b.y; const p0 = pt.matrixTransform(m).matrixTransform(sm);
      pt.x = b.x + b.width; pt.y = b.y + b.height; const p1 = pt.matrixTransform(m).matrixTransform(sm);
      if (p0.x < vb.x - 2 || p0.y < vb.y - 2 || p1.x > vb.x + vb.width + 2 || p1.y > vb.y + vb.height + 2)
        out.push(`${id}: SHAPE OUT OF BOUNDS [${p0.x.toFixed(0)},${p0.y.toFixed(0)},${p1.x.toFixed(0)},${p1.y.toFixed(0)}]`);
    });
    svg.querySelectorAll('text').forEach(t => {
      let b; try { b = t.getBBox(); } catch(e) { return; }
      if (!b.width) return;
      // account for transforms by mapping bbox corners through CTM relative to svg
      const m = t.getCTM(); const sm = svg.getCTM().inverse();
      const pt = svg.createSVGPoint();
      const pts = [[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y]) => {
        pt.x = x; pt.y = y; const p = pt.matrixTransform(m).matrixTransform(sm); return [p.x,p.y];});
      const xs = pts.map(p=>p[0]), ys = pts.map(p=>p[1]);
      const bb = {x0:Math.min(...xs), x1:Math.max(...xs), y0:Math.min(...ys), y1:Math.max(...ys), s:t.textContent.slice(0,40)};
      const tsp = t.querySelectorAll('tspan'); const nl = Math.max(1, tsp.length);
      if (bb.x0 < vb.x - 1 || bb.y0 < vb.y - 1 || bb.x1 > vb.x + vb.width + 1 || bb.y1 > vb.y + vb.height + 1)
        out.push(`${id}: OUT OF BOUNDS "${bb.s}" [${bb.x0.toFixed(0)},${bb.y0.toFixed(0)},${bb.x1.toFixed(0)},${bb.y1.toFixed(0)}] vb ${vb.width}x${vb.height}`);
      boxes.push(bb);
    });
    for (let i=0;i<boxes.length;i++) for (let j=i+1;j<boxes.length;j++) {
      const a=boxes[i], b=boxes[j];
      const ox = Math.min(a.x1,b.x1)-Math.max(a.x0,b.x0), oy = Math.min(a.y1,b.y1)-Math.max(a.y0,b.y0);
      const ha=(a.y1-a.y0), hb=(b.y1-b.y0); if (ox > 2 && oy > 0.3*Math.min(ha,hb) && oy > 3) out.push(`${id}: OVERLAP "${a.s}" / "${b.s}"`);
    }
  });
  const W = document.body.clientWidth;
  document.querySelectorAll('table, figure, .card, .box, pre').forEach(el => {
    if (el.scrollWidth > el.clientWidth + 2) out.push(`HTML overflow in ${el.tagName}.${el.className} "${el.textContent.trim().slice(0,50)}"`);
  });
  return out;
}
"""

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME)
    pg = br.new_page(viewport={"width": 794, "height": 1123})
    pg.goto("file://" + HTML)
    pg.emulate_media(media="print")
    # emulate printable width: A4 210mm - 30mm margins = 180mm ~ 680px
    pg.add_style_tag(content="body{width:180mm;}")
    res = pg.evaluate(JS)
    n_svg = pg.evaluate("() => document.querySelectorAll('figure svg').length")
    br.close()
print(f"{n_svg} figure SVGs checked; {len(res)} issues")
for r in res:
    print(" ", r)
