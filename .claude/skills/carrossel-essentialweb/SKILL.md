---
name: carrossel-essentialweb
description: Cria carrosseis editoriais da EssentialWeb para Instagram em HTML e PNG usando a metodologia BrandsDecoded extraida de projetos/carrosseis claude. Use quando o usuario pedir carrossel, carousel, slides de Instagram, narrativa visual, hooks, HTML editavel ou exportacao PNG para a EssentialWeb.
---

# Carrossel EssentialWeb

Use esta skill para criar carrosseis da EssentialWeb. A fonte de conhecimento desta skill e apenas o material legado em `projetos/carrosseis claude`, reorganizado em `references/`.

## Contexto fixo

- Marca: EssentialWeb.
- Handle: `@essentialweb_br`.
- Logo: `assets/logo-essentialweb.png`.
- Saida padrao: `marketing/carrosseis/[slug]/`.
- Formato: 1080x1350 por slide.
- Entrega padrao: texto aprovado, HTML editavel, PNGs exportados e legenda final.

Antes de produzir, leia quando existirem:

- `_contexto/empresa.md`
- `_contexto/preferencias.md`
- `marca/design-guide.md`
- `references/essentialweb-notes.md`

## Referencias

Carregue apenas os arquivos necessarios para a etapa atual:

- `references/workflow.md`: fluxo da Maquina de Carrosseis v4.
- `references/editorial-quality.md`: manual de qualidade, anti-AI slop e criterios editoriais.
- `references/editorial-filter.md`: filtro editorial antes de aprovar texto final.
- `references/headlines.md`: banco de headlines e engine de hooks.
- `references/visual-system.md`: design system e template 1080x1350.
- `references/visual-principles.md`: principios visuais BrandsDecoded.
- `references/examples.md`: exemplos bons para calibragem.

## Fluxo obrigatorio

1. Briefing criativo: use a etapa "7 coisas rapidas" quando o briefing ainda estiver aberto: tema, tese, publico, tensao/problema, prova/contexto, CTA e slides/imagens. Como a marca ja e conhecida, nao pergunte marca/cor/handle salvo se houver excecao.
2. Triagem editorial: aplique `editorial-quality.md` e `editorial-filter.md` para eliminar tese fraca, obviedade, exagero e voz generica.
3. Quando a autoridade do carrossel depender de mercado, noticia, comportamento ou dado, busque fontes confiaveis antes de escrever o texto final. Prefira fontes primarias, oficiais ou imprensa confiavel. Inclua fonte e periodo no `carousel-text.md` e nota discreta no slide quando o dado aparecer visualmente.
4. Gere 10 headlines usando `headlines.md`. Mostre as opcoes e recomende uma.
5. Monte a espinha dorsal do carrossel: abertura, conflito, desenvolvimento, virada, fechamento e CTA.
6. Escreva o texto completo slide a slide e peca aprovacao antes do HTML.
7. Sugira imagens/assets necessarios. Quando houver imagem, pergunte: "Voce quer que eu gere os assets com a skill `gpt-image-2` ou prefere fornecer os arquivos?".
8. Crie o HTML editavel em `marketing/carrosseis/[slug]/carousel.html`, usando o sistema visual e a marca EssentialWeb.
9. Exporte PNGs com Playwright para `marketing/carrosseis/[slug]/slides-png/` somente depois de aprovacao explicita do HTML pelo usuario.
10. Entregue legenda final e checklist de arquivos gerados.

## Assets com imagem

Quando o usuario escolher gerar assets:

- Use a skill `gpt-image-2`.
- Para carrossel vertical, recomende `size: 1024x1536`.
- Quando o usuario escolher preview, gere previews para cada asset relevante antes do final. As variacoes devem testar abordagens visuais diferentes, nao apenas mudancas de angulo.
- Antes do asset final, pergunte se a imagem final deve ser `quality: high`.
- Se o usuario nao quiser `high`, recomende `quality: medium`.
- Salve assets finais em `marketing/carrosseis/[slug]/assets/`.
- Evite texto dentro da imagem; deixe tipografia, logo, CTA e hierarquia para o HTML/CSS.
- Use imagens geradas como materia-prima visual, nao como slide final fechado.

Quando o usuario preferir fornecer assets, peca os arquivos ou caminhos locais e incorpore no HTML mantendo o export por Playwright.

## Estrutura de saida

Crie novos carrosseis assim:

```text
marketing/carrosseis/[slug]/
  carousel-text.md
  carousel.html
  assets/
  slides-png/
```

## Exportacao

Nunca rode exportacao, nem exportacao "temporaria" para validar visual, antes do usuario aprovar o HTML e pedir explicitamente `exportar`, `gera os PNGs` ou equivalente. Antes disso, revise apenas o HTML editavel, CSS, assets e estrutura do arquivo.

Use o script local:

```bash
node .claude/skills/carrossel-essentialweb/scripts/export-carousel-playwright.js marketing/carrosseis/[slug]/carousel.html
```

O export deve capturar cada elemento `.slide`, esperar `document.fonts.ready`, inlinear assets locais em base64 quando necessario, validar PNGs em `1080x1350` e salvar em `slides-png/`.

## Regras

- Nao use material de `templates/skills`.
- Nao copie `node_modules`, `.git`, ZIPs, PDFs, PNGs renderizados ou carrosseis antigos como assets da skill.
- Trate `projetos/carrosseis claude` como legado preservado; novos outputs vao em `marketing/carrosseis/`.
- Nao invente fatos, numeros, estudos, datas ou claims atuais. Pesquise quando a informacao puder ter mudado.
- Preserve a voz da EssentialWeb: direta, estrategica, sem promessa milagrosa e sem texto com cara de IA.
- Mantenha acentos corretamente em HTML e Markdown. Nao remova acentos para evitar problema de encoding; salve em UTF-8.
- O ultimo slide deve fechar a tese com assinatura discreta. Evite CTA exagerado, repetitivo ou com texto quase igual a headline.
