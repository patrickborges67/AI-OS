# Aprendizados — Skill Carrossel

Regras aprendidas durante o uso. O Claude DEVE ler este arquivo antes de executar o fluxo
de produção/exportação de carrossel.

---

### 2026-05-27 — Export precisa de supersampling 2x + downscale Lanczos para nitidez
**Regra:** O script `export-carousel-playwright.js` deve rodar com `deviceScaleFactor: 2` no
Playwright e usar `sharp` (Lanczos3) pra reduzir 2160×2700 → 1080×1350 com `compressionLevel: 9`.
Sem essa cadeia, texto serif e detalhes finos (rostos gerados por IA) saem fosco/borrado.
**Fallback obrigatório:** se `sharp` não estiver instalado, cair pra `deviceScaleFactor: 1` direto
no PNG do Playwright, sem quebrar.
**Contexto:** primeira exportação saiu com qualidade abaixo do esperado mesmo em PNG lossless;
1:1 do browser perde nitidez visível especialmente em headlines em Cormorant/Playfair e fotos
do gpt-image-2. Supersampling 2x deu ~26% mais informação visual real no slide 1 (Lumina Namorados).

### 2026-05-27 — Reset defensivo de modo preview cobre múltiplos templates
**Regra:** No `preparePage`, sempre limpar TODAS as variações de "modo preview" que os templates
de carrossel usam: (1) `window.applyMode()` global (template antigo); (2) `document.body.classList.remove("preview")` (template novo); (3) `document.body.removeAttribute("data-mode")`. E injetar CSS que zera `transform`,
margens negativas e força `.slide { width:1080px; height:1350px; flex: 0 0 auto }`.
**Contexto:** o script só conhecia `window.applyMode()` e ignorava o `body.preview` do template
novo da Lumina — exportou os 8 slides do carrossel de Namorados todos sobrepostos/embolados
(cada um capturado escalado a 30% com vazamento dos vizinhos). Validação `1080×1350` passava
porque o `slide.screenshot()` respeita bounding box CSS, mas o conteúdo vinha errado.

### 2026-05-27 — Limpar PNGs com unlink arquivo a arquivo (não rm -rf da pasta)
**Regra:** Antes de exportar, limpar PNGs antigos com loop `unlinkSync` em cada `.png` da pasta,
ignorando erros individuais. NÃO usar `fs.rmSync(outDir, { recursive: true })` — quebra com
EPERM no Windows quando a pasta está aberta no Explorer/IDE.
**Contexto:** segunda tentativa de export do carrossel de Namorados deu EPERM no `rm -rf` porque
o Explorer estava na pasta `slides-png/`. Solução: criar a pasta com `mkdirSync(recursive:true)`
e iterar arquivos. Arquivo bloqueado é sobrescrito depois sem problema.

### 2026-05-27 — Imagens verticais (1024×1536) não cabem em frame compartilhado com texto
**Regra:** Se o slide tem `tag + título + corpo` empilhados na metade inferior, a foto na metade
superior deve estar em frame **horizontal 16:9** (~`height: 540px; width: 100%`), não vertical.
Imagem vertical alta empurra/corta o conteúdo. Se a fonte for vertical (gpt-image-2 1024×1536),
recortar pra 16:9 manualmente ou regerar horizontal.
**Contexto:** carrossel Lumina Namorados tentou usar imagens verticais 2:3 em slides 2 e 4. Frame
ficou cortando topo/base ou criando barras pretas com `contain`. Trocar pra frame 16:9 (com
imagens recortadas manualmente pra 16:9) resolveu — paralelismo visual com carrossel de aniversário.
