// Preview Parts 8 and 12 only: node build/preview_p812.js
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const ROOT = __dirname;
const fonts = fs.readFileSync(path.join(ROOT, 'fonts/fonts_embed.css'), 'utf8');
const css = fs.readFileSync(path.join(ROOT, 'style.css'), 'utf8');
const files = ['08_your_view.html', '12_why_lseg.html'];
const body = files.map(f => fs.readFileSync(path.join(ROOT, 'parts', f), 'utf8')).join('\n');
const html = `<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><style>${fonts}\n${css}</style></head><body>${body}</body></html>`;
const OUT = '/tmp/claude-0/p812.pdf';
(async () => {
  fs.mkdirSync('/tmp/claude-0', { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  // report SVG text overflowing its viewBox
  const issues = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('figure svg').forEach(svg => {
      const vb = svg.viewBox.baseVal; const fig = svg.closest('figure').id;
      svg.querySelectorAll('text').forEach(t => {
        const b = t.getBBox();
        if (b.x < vb.x + 2 || b.y < vb.y + 2 || b.x + b.width > vb.x + vb.width - 2 || b.y + b.height > vb.y + vb.height - 2)
          out.push(`${fig}: "${t.textContent}" bbox ${b.x.toFixed(0)},${b.y.toFixed(0)},${b.width.toFixed(0)}`);
      });
      // text inside rects: check text right edge vs containing rect
      const rects = [...svg.querySelectorAll('rect')].map(r => r.getBBox());
      svg.querySelectorAll('text').forEach(t => {
        const b = t.getBBox();
        const host = rects.filter(r => b.x >= r.x && b.x <= r.x + r.width && b.y >= r.y - 1 && b.y <= r.y + r.height)
          .sort((a, c) => a.width * a.height - c.width * c.height)[0];
        if (host && b.x + b.width > host.x + host.width - 4) out.push(`${fig}: "${t.textContent}" overflows box by ${(b.x + b.width - host.x - host.width).toFixed(1)}`);
      });
    });
    return out;
  });
  console.log(issues.length ? issues.join('\n') : 'No SVG text overflow detected');
  await page.pdf({ path: OUT, format: 'A4', printBackground: true, margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' } });
  await browser.close();
  console.log(execSync(`pdfinfo ${OUT} | grep Pages`).toString().trim());
  execSync(`rm -f /tmp/claude-0/p812-*.png; pdftoppm -r 60 -png ${OUT} /tmp/claude-0/p812`);
  console.log('PNGs in /tmp/claude-0/');
})();
