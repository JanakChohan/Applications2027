// Screenshots of the main pages for visual review. Usage: node build/shots.js
const { chromium, devices } = require('playwright');
const path = require('path');
const fs = require('fs');
const FILE = 'file://' + path.resolve(__dirname, '..', 'gsam_csg_command_center.html');
const OUT = path.resolve(__dirname, 'out', 'shots');
fs.mkdirSync(OUT, { recursive: true });
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1360, height: 900 }, colorScheme: 'light' });
  const errs = [];
  page.on('pageerror', (e) => errs.push(String(e)));
  for (const v of ['', 'role', 'relationships', 'sales', 'teams', 'facts', 'practise', 'library', 'library/people', 'library/calculator']) {
    await page.goto(FILE + '#/' + v);
    await page.waitForTimeout(250);
    await page.screenshot({ path: path.join(OUT, 'p-' + (v || 'home').replace('/', '-') + '.png') });
  }
  await page.goto(FILE + '#/relationships');
  await page.evaluate(() => document.querySelector('#view-relationships .diagram').scrollIntoView({ block: 'center' }));
  await page.screenshot({ path: path.join(OUT, 'p-relationships-diagram.png') });
  const m = await (await browser.newContext({ ...devices['iPhone 13'], colorScheme: 'light' })).newPage();
  await m.goto(FILE + '#/'); await m.waitForTimeout(200);
  await m.screenshot({ path: path.join(OUT, 'p-mobile-home.png') });
  await m.goto(FILE + '#/relationships'); await m.waitForTimeout(200);
  await m.screenshot({ path: path.join(OUT, 'p-mobile-relationships.png') });
  await browser.close();
  console.log('page errors:', errs.length ? errs : 'none');
})();
