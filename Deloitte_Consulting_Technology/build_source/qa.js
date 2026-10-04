// Report SVG text that overflows its viewBox or overlaps other text, plus any element wider than the page body.
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch(); const page = await browser.newPage({viewport:{width:794,height:1123}});
  await page.goto('file://' + process.argv[2]); await page.evaluate(() => document.fonts.ready);
  await page.emulateMedia({media:'print'});
  const r = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('figure.fig').forEach((fig, fi) => {
      const svg = fig.querySelector('svg'); if (!svg) { out.push(`${fig.id||fi}: no svg`); return; }
      const vb = svg.viewBox.baseVal; if (!vb || !vb.width) { out.push(`${fig.id||fi}: no viewBox`); return; }
      const texts = [...svg.querySelectorAll('text')]; const boxes = [];
      texts.forEach(t => { let b; try { b = t.getBBox(); } catch(e) { return; }
        // account for transforms roughly via getCTM relative to svg
        const m = t.getCTM(), sm = svg.getCTM().inverse(); const M = sm.multiply(m);
        const p1 = new DOMPoint(b.x,b.y).matrixTransform(M), p2 = new DOMPoint(b.x+b.width,b.y+b.height).matrixTransform(M);
        const x1=Math.min(p1.x,p2.x), x2=Math.max(p1.x,p2.x), y1=Math.min(p1.y,p2.y), y2=Math.max(p1.y,p2.y);
        if (x1 < vb.x-1 || y1 < vb.y-1 || x2 > vb.x+vb.width+1 || y2 > vb.y+vb.height+1) out.push(`${fig.id||fi}: OVERFLOW "${t.textContent.slice(0,40)}" [${x1|0},${y1|0},${x2|0},${y2|0}] vb ${vb.width}x${vb.height}`);
        boxes.push({x1,x2,y1,y2,s:t.textContent.slice(0,30)});
        if (!t.hasAttribute('data-free')) {
        const ax=(x1+x2)/2, ay=(y1+y2)/2; let best=null;
        svg.querySelectorAll('rect').forEach(rc => { const rb=rc.getBBox(); const rm=sm.multiply(rc.getCTM());
          const q1=new DOMPoint(rb.x,rb.y).matrixTransform(rm), q2=new DOMPoint(rb.x+rb.width,rb.y+rb.height).matrixTransform(rm);
          const rx1=Math.min(q1.x,q2.x),rx2=Math.max(q1.x,q2.x),ry1=Math.min(q1.y,q2.y),ry2=Math.max(q1.y,q2.y);
          if (ax>=rx1&&ax<=rx2&&ay>=ry1&&ay<=ry2 && (rx2-rx1)<vb.width*0.97) { const ar=(rx2-rx1)*(ry2-ry1); if(!best||ar<best.ar) best={rx1,rx2,ry1,ry2,ar}; } });
        if (best && (x1<best.rx1-1.5||x2>best.rx2+1.5)) out.push(`${fig.id||fi}: SPILL "${t.textContent.slice(0,40)}" text ${x1|0}-${x2|0} box ${best.rx1|0}-${best.rx2|0}`); }
        });
      for (let i=0;i<boxes.length;i++) for (let j=i+1;j<boxes.length;j++){ const a=boxes[i],b=boxes[j];
        const ox=Math.min(a.x2,b.x2)-Math.max(a.x1,b.x1), oy=Math.min(a.y2,b.y2)-Math.max(a.y1,b.y1);
        if (ox>2 && oy>2 && a.s.trim() && b.s.trim()) out.push(`${fig.id||fi}: OVERLAP "${a.s}" / "${b.s}"`); }
    });
    const bw = document.body.getBoundingClientRect().width;
    document.querySelectorAll('table,figure,.card,.callout,pre').forEach(e => { if (e.scrollWidth > e.clientWidth + 2) out.push(`WIDE ${e.tagName}.${e.className} ${(e.id||'')} ${e.scrollWidth}>${e.clientWidth}`); });
    out.push(`FIGURES ${document.querySelectorAll('figure.fig').length}`);
    return out; });
  console.log(r.join('\n')); await browser.close();
})();
