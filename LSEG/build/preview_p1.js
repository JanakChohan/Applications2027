// Preview Part 1 alone: node build/preview_p1.js  -> /tmp/claude-0/p1.pdf and PNGs
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const ROOT = __dirname;
const fonts = fs.readFileSync(path.join(ROOT, 'fonts/fonts_embed.css'), 'utf8');
const css = fs.readFileSync(path.join(ROOT, 'style.css'), 'utf8');
const frag = fs.readFileSync(path.join(ROOT, 'parts/01_role.html'), 'utf8');
const OUT = '/tmp/claude-0/p1.pdf';
(async () => {
  fs.mkdirSync('/tmp/claude-0', { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent(`<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><style>${fonts}\n${css}</style></head><body>${frag}</body></html>`, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: OUT, format: 'A4', printBackground: true, margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' } });
  await browser.close();
  execSync(`rm -f /tmp/claude-0/p1-*.png; pdftoppm -r 60 -png ${OUT} /tmp/claude-0/p1`);
  console.log(execSync(`pdfinfo ${OUT} | grep Pages; ls /tmp/claude-0/p1-*.png`).toString());
})();
