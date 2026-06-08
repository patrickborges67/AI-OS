// Export dos anuncios 1080x1080 via Playwright (reaproveita o chromium ja instalado).
// Captura cada .slide e salva em slides-png/slide_NN.png.
const path = require("path");
const fs = require("fs");
const { chromium } = require("playwright");

const DIR = __dirname;
const HTML = path.join(DIR, "carousel.html");
const OUT = path.join(DIR, "slides-png");
const SIZE = 1080;

(async () => {
  if (!fs.existsSync(OUT)) fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: SIZE, height: SIZE }, deviceScaleFactor: 1 });
  await page.goto("file://" + HTML.replace(/\\/g, "/"));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(600); // garante fontes/gradientes
  const slides = await page.$$(".slide");
  console.log("slides encontrados:", slides.length);
  for (let i = 0; i < slides.length; i++) {
    const file = path.join(OUT, `slide_${String(i + 1).padStart(2, "0")}.png`);
    await slides[i].screenshot({ path: file });
    console.log("ok:", path.basename(file));
  }
  await browser.close();
  console.log("concluido:", slides.length, "PNGs em slides-png/");
})();
