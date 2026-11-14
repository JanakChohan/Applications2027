// Screenshots of the main views for visual review. Usage: node build/shots.js
const { chromium, devices } = require('playwright');
const path = require('path');
const fs = require('fs');
const FILE = 'file://' + path.resolve(__dirname, '..', 'gsam_csg_command_center.html');
const OUT = path.resolve(__dirname, 'out', 'shots');
fs.mkdirSync(OUT, { recursive: true });
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1360, height: 900 } });
  const errs = [];
  page.on('pageerror', (e) => errs.push(String(e)));
  for (const v of ['home', 'intel', 'numbers', 'teams', 'arcade', 'practice', 'read/ch07']) {
    await page.goto(FILE + '#/' + v);
    await page.waitForTimeout(250);
    await page.screenshot({ path: path.join(OUT, 'v-' + v.replace('/', '-') + '.png') });
  }
  await page.goto(FILE + '#/numbers');
  await page.evaluate(() => document.querySelector('.chart').scrollIntoView());
  await page.screenshot({ path: path.join(OUT, 'v-chart.png') });
  await page.goto(FILE + '#/arcade');
  await page.click('#zStart'); await page.click('#zOpts button');
  await page.screenshot({ path: path.join(OUT, 'v-quiz.png') });
  await page.click('#themeBtn'); await page.goto(FILE + '#/home'); await page.waitForTimeout(200);
  await page.screenshot({ path: path.join(OUT, 'v-home-light.png') });
  const m = await (await browser.newContext({ ...devices['iPhone 13'] })).newPage();
  await m.goto(FILE + '#/home'); await m.waitForTimeout(200);
  await m.screenshot({ path: path.join(OUT, 'v-mobile-home.png') });
  await browser.close();
  console.log('page errors:', errs.length ? errs : 'none');
})();
