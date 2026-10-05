// Preview Parts 11 and 13: render to PDF and PNGs for visual checks.
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const ROOT = __dirname;
const fonts = fs.readFileSync(path.join(ROOT, 'fonts/fonts_embed.css'), 'utf8');
const css = fs.readFileSync(path.join(ROOT, 'style.css'), 'utf8');
const which = process.argv[2] || 'both';
const files = which === 'cheat' ? ['13_cheat_sheet.html'] : which === 'p11' ? ['11_scenarios.html'] : ['11_scenarios.html', '13_cheat_sheet.html'];
const body = files.map(f => fs.readFileSync(path.join(ROOT, 'parts', f), 'utf8')).join('\n');
const html = `<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><style>${fonts}\n${css}</style></head><body>${body}</body></html>`;
const out = which === 'both' ? '/tmp/claude-0/p1113.pdf' : `/tmp/claude-0/p1113_${which}.pdf`;
(async () => {
  fs.mkdirSync('/tmp/claude-0', { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: out, format: 'A4', printBackground: true, margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' } });
  await browser.close();
  const pages = execSync(`pdfinfo ${out} | grep Pages`).toString().trim();
  console.log(out, pages);
  const prefix = out.replace('.pdf', '');
  execSync(`rm -f ${prefix}-*.png; pdftoppm -r 60 -png ${out} ${prefix}`);
})();
