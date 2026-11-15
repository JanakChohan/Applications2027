// Render build/out/print.html to PDF with page numbers, then fill the contents page
// with real page numbers (pass 1 finds the page of each destination; pass 2 prints them).
// Usage: node build/make_pdf.js <print.html> <out.pdf>
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

(async () => {
  const [src, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(src), { waitUntil: 'load' });
  await page.emulateMedia({ media: 'print' });
  const opts = {
    path: out, format: 'A4', printBackground: true, displayHeaderFooter: true,
    margin: { top: '18mm', bottom: '18mm', left: '15mm', right: '15mm' },
    headerTemplate: '<div style="font:7pt sans-serif;color:#666;width:100%;padding:0 15mm;display:flex;justify-content:space-between"><span>GSAM Client Solutions Group 2027 · Study Dossier</span><span>Research to 14 November 2026 · independent preparation material</span></div>',
    footerTemplate: '<div style="font:8pt sans-serif;color:#444;width:100%;text-align:center">Page <span class="pageNumber"></span> of <span class="totalPages"></span></div>',
  };
  await page.pdf(opts);
  // pass 1 -> page numbers of named destinations
  let map = {};
  try {
    const py = `
import json,sys
from pypdf import PdfReader
r=PdfReader(sys.argv[1]); out={}
for name,d in r.named_destinations.items():
    try: out[name.lstrip('/')]=r.get_destination_page_number(d)+1
    except Exception: pass
print(json.dumps(out))`;
    map = JSON.parse(execFileSync('python3', ['-c', py, out], { maxBuffer: 1 << 26 }).toString());
  } catch (e) { console.error('page-number pass failed:', e.message); }
  const filled = await page.evaluate((m) => {
    let n = 0;
    document.querySelectorAll('.toc-p[data-dest]').forEach((el) => { const p = m[el.dataset.dest]; if (p) { el.textContent = String(p); n++; } });
    return n;
  }, map);
  await page.pdf(opts);
  await browser.close();
  try { console.log(execFileSync('python3', [path.join(__dirname, 'page_background.py'), out]).toString().trim()); } catch (e) { console.error('background step failed:', e.message); }
  console.log(`PDF written: ${out} (${(fs.statSync(out).size / 1e6).toFixed(1)} MB), contents entries numbered: ${filled}`);
})();
