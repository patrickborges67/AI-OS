const fs = require("fs");
const path = require("path");
const { pathToFileURL } = require("url");

const ROOT = process.cwd();

function parseArgs(argv) {
  if (argv.includes("--help") || argv.includes("-h")) {
    console.log(`Uso:
  node scripts/export-carousel-playwright.js [arquivo-ou-pasta-html] [--out pasta]

Entrada:
  - arquivo .html com elementos .slide
  - pasta contendo carousel.html ou *-carousel.html

Saida padrao:
  slides-png/ dentro da pasta do HTML`);
    process.exit(0);
  }

  const outIndex = argv.indexOf("--out");
  const outDir = outIndex >= 0 ? argv[outIndex + 1] : null;
  const input = argv.find((arg, index) => arg !== "--out" && index !== outIndex + 1);

  return {
    input: input || ".",
    outDir,
  };
}

function resolveInput(inputArg = ".", outArg = null) {
  const inputPath = path.resolve(ROOT, inputArg);

  if (!fs.existsSync(inputPath)) {
    throw new Error(`Caminho não encontrado: ${inputPath}`);
  }

  const stat = fs.statSync(inputPath);
  if (stat.isFile()) {
    if (path.extname(inputPath).toLowerCase() !== ".html") {
      throw new Error(`Arquivo informado não é HTML: ${inputPath}`);
    }

    const carouselDir = path.dirname(inputPath);
    const parsedPath = path.parse(inputPath);
    const inlinePath = inputPath.endsWith("-inline.html")
      ? inputPath
      : path.join(parsedPath.dir, `${parsedPath.name}-inline${parsedPath.ext}`);

    return {
      carouselDir,
      htmlPath: inputPath,
      inlinePath,
      outDir: outArg ? path.resolve(ROOT, outArg) : path.join(carouselDir, "slides-png"),
      shouldInline: !inputPath.endsWith("-inline.html"),
    };
  }

  if (!stat.isDirectory()) {
    throw new Error(`Caminho informado não é arquivo nem diretório: ${inputPath}`);
  }

  const files = fs.readdirSync(inputPath);
  const htmlFile =
    files.find((file) => file.endsWith("-carousel.html") && !file.endsWith("-inline.html")) ||
    files.find((file) => file === "carousel.html") ||
    files.find((file) => file.endsWith(".html") && !file.endsWith("-inline.html")) ||
    files.find((file) => file.endsWith(".html"));

  if (!htmlFile) {
    throw new Error(`Nenhum HTML encontrado em: ${inputPath}`);
  }

  const htmlPath = path.join(inputPath, htmlFile);
  const inlinePath = htmlFile.endsWith("-carousel.html")
    ? path.join(inputPath, htmlFile.replace("-carousel.html", "-carousel-inline.html"))
    : htmlPath;

  return {
    carouselDir: inputPath,
    htmlPath,
    inlinePath,
    outDir: outArg ? path.resolve(ROOT, outArg) : path.join(inputPath, "slides-png"),
    shouldInline: inlinePath !== htmlPath,
  };
}

function mimeFor(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  if (ext === ".png") return "image/png";
  if (ext === ".jpg" || ext === ".jpeg") return "image/jpeg";
  if (ext === ".webp") return "image/webp";
  if (ext === ".woff2") return "font/woff2";
  if (ext === ".woff") return "font/woff";
  return "application/octet-stream";
}

function dataUrl(relativePath, baseDir) {
  if (/^(?:data:|https?:|file:)/i.test(relativePath)) {
    return relativePath;
  }

  const absolutePath = path.resolve(baseDir, relativePath.replace(/\\/g, "/"));
  const data = fs.readFileSync(absolutePath);
  return `data:${mimeFor(absolutePath)};base64,${data.toString("base64")}`;
}

function buildInlineHtml({ carouselDir, htmlPath, inlinePath, shouldInline }) {
  if (!shouldInline) {
    return;
  }

  const html = fs.readFileSync(htmlPath, "utf8");
  const inlined = html
    .replace(/url\("([^"]+\.(?:png|jpe?g|webp|woff2?|woff))"\)/gi, (_match, assetPath) => `url("${dataUrl(assetPath, carouselDir)}")`)
    .replace(/src="([^"]+\.(?:png|jpe?g|webp))"/gi, (_match, assetPath) => `src="${dataUrl(assetPath, carouselDir)}"`);

  fs.writeFileSync(inlinePath, inlined, { encoding: "utf8" });
}

function readPngSize(filePath) {
  const buffer = fs.readFileSync(filePath);
  return {
    width: buffer.readUInt32BE(16),
    height: buffer.readUInt32BE(20),
  };
}

async function preparePage(page) {
  await page.evaluate(() => {
    // Variação 1: applyMode global (alguns templates)
    if (typeof window.applyMode === "function" && "isPreview" in window) {
      window.isPreview = false;
      window.applyMode();
    }

    // Variação 2: classe "preview" no body (padrão do template novo)
    document.body.classList.remove("preview");

    // Variação 3: atributo data-mode
    document.body.removeAttribute("data-mode");

    document.body.classList.add("full");
  });

  // Reset defensivo: desliga toolbar, anula transform/margens negativas que vêm do modo preview,
  // garante que cada .slide renderize em 1080x1350 isolado.
  await page.addStyleTag({
    content: `
      .toolbar, .controls { display: none !important; }
      body, body.preview { background: #111 !important; }
      .deck, .slides-wrap {
        display: block !important;
        grid-template-columns: none !important;
        margin: 0 auto !important;
        padding: 0 !important;
        max-width: none !important;
        gap: 0 !important;
      }
      .slide-frame { margin: 0 auto 28px !important; box-shadow: none !important; }
      .slide {
        transform: none !important;
        margin: 0 auto 28px !important;
        width: 1080px !important;
        height: 1350px !important;
        flex: 0 0 auto !important;
      }
    `,
  });

  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(2000);
}

async function exportSlides(config) {
  const { chromium } = require("playwright");
  let sharp = null;
  try { sharp = require("sharp"); } catch { /* sharp opcional — fallback pra 1x */ }

  buildInlineHtml(config);
  if (!config.outDir || path.resolve(config.outDir) === path.parse(path.resolve(config.outDir)).root) {
    throw new Error(`Pasta de saida insegura: ${config.outDir}`);
  }

  fs.mkdirSync(config.outDir, { recursive: true });
  // Limpa só os PNGs antigos (não apaga a pasta — evita EPERM no Windows quando ela
  // está aberta no Explorer/IDE). Arquivos individuais bloqueados são ignorados.
  for (const file of fs.readdirSync(config.outDir)) {
    if (file.toLowerCase().endsWith(".png")) {
      try { fs.unlinkSync(path.join(config.outDir, file)); } catch { /* arquivo bloqueado, será sobrescrito */ }
    }
  }

  const browser = await chromium.launch();
  // Quando sharp está disponível, faz supersampling 2x: o navegador renderiza em 2x,
  // captura em 2160x2700 e downscalamos pra 1080x1350 com Lanczos — ganho de nitidez
  // visível em texto serif e detalhes finos (rostos gerados por IA). Sem sharp, 1x.
  const scale = sharp ? 2 : 1;
  const page = await browser.newPage({
    viewport: { width: 1200, height: 1400 },
    deviceScaleFactor: scale,
  });
  await page.goto(pathToFileURL(config.inlinePath).href, { waitUntil: "networkidle" });
  await preparePage(page);

  const slides = page.locator(".slide");
  const count = await slides.count();

  if (count === 0) {
    throw new Error(`Nenhum slide encontrado em: ${config.inlinePath}`);
  }

  for (let i = 0; i < count; i += 1) {
    const slide = slides.nth(i);
    await slide.scrollIntoViewIfNeeded();
    await page.waitForTimeout(300);
    const outputPath = path.join(config.outDir, `slide_${String(i + 1).padStart(2, "0")}.png`);

    if (sharp) {
      // Captura em 2x na memória e faz downscale Lanczos pra 1080x1350.
      const buffer = await slide.screenshot();
      await sharp(buffer)
        .resize(1080, 1350, { kernel: sharp.kernel.lanczos3 })
        .png({ compressionLevel: 9 })
        .toFile(outputPath);
    } else {
      await slide.screenshot({ path: outputPath });
    }

    const { width, height } = readPngSize(outputPath);
    if (width !== 1080 || height !== 1350) {
      throw new Error(`Slide ${i + 1} exportado em ${width}x${height}, esperado 1080x1350.`);
    }
  }

  await browser.close();
  console.log(`Exportados ${count} slides em ${config.outDir}`);
}

const args = parseArgs(process.argv.slice(2));
const config = resolveInput(args.input, args.outDir);

exportSlides(config).catch((error) => {
  console.error(error);
  process.exit(1);
});
