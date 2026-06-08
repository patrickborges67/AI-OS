const path = require("path");
const fs = require("fs");
const { chromium } = require("playwright");
(async () => {
  const HTML = path.resolve(__dirname, "carousel.html");
  const OUT = path.resolve(__dirname, "review-screens");
  if (!fs.existsSync(OUT)) fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  await page.goto("file://" + HTML.split(path.sep).join("/"));
  await page.evaluate(() => { document.body.classList.remove("preview"); });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(800);
  const slides = process.argv.slice(2).map(Number);
  const list = slides.length ? slides : [2, 4, 6];
  for (const n of list) {
    const el = await page.$("#slide-" + n);
    await el.screenshot({ path: path.join(OUT, "slide_0" + n + ".png") });
    console.log("ok slide", n);
  }
  await browser.close();
})();
