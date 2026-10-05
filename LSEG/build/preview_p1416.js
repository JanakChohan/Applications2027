// Preview Parts 14 and 16: node build/preview_p1416.js -> /tmp/claude-0/p1416.pdf and PNGs
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const ROOT = __dirname;
const fonts = fs.readFileSync(path.join(ROOT, 'fonts/fonts_embed.css'), 'utf8');
const css = fs.readFileSync(path.join(ROOT, 'style.css'), 'utf8');
const frags = ['parts/14_glossary.html', 'parts/16_gaps.html'].map(f => fs.readFileSync(path.join(ROOT, f), 'utf8')).join('\n');
const OUT = '/tmp/claude-0/p1416.pdf';
(async () => {
  fs.mkdirSync('/tmp/claude-0', { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent(`<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><style>${fonts}\n${css}</style></head><body>${frags}</body></html>`, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  // report the page each part starts on (approximate, by y offset / page height not reliable in print); rely on pdftotext instead
  await page.pdf({ path: OUT, format: 'A4', printBackground: true, margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' } });
  await browser.close();
  execSync(`rm -f /tmp/claude-0/p1416-*.png; pdftoppm -r 60 -png ${OUT} /tmp/claude-0/p1416`);
  console.log(execSync(`pdfinfo ${OUT} | grep Pages; ls /tmp/claude-0/p1416-*.png`).toString());
})();
