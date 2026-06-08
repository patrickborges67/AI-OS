---
name: carrossel
description: Cria carrosseis editoriais para Instagram em HTML e PNG usando a metodologia BrandsDecoded extraida de projetos/carrosseis claude. Use quando o usuario pedir carrossel, carousel, slides de Instagram, narrativa visual, hooks, HTML editavel ou exportacao PNG sem uma marca local ja configurada.
---

# Carrossel

Use esta skill para criar carrosseis editoriais em HTML e PNG. A fonte de conhecimento desta skill e apenas o material legado em `projetos/carrosseis claude`, reorganizado em `references/`.

## Setup obrigatorio

Antes do primeiro uso em um projeto, colete e registre:

- Marca.
- Handle.
- Nicho e publico.
- Cor principal e cores de apoio.
- Estilo visual desejado.
- CTA padrao.
- Pasta de saida.
- Logo ou caminho para o logo.

Se qualquer item acima estiver ausente, pergunte antes de produzir. Nao use EssentialWeb como padrao nesta skill.

## Referencias

Carregue apenas os arquivos necessarios para a etapa atual:

- `references/workflow.md`: fluxo da Maquina de Carrosseis v4.
- `references/editorial-quality.md`: manual de qualidade, anti-AI slop e criterios editoriais.
- `references/editorial-filter.md`: filtro editorial antes de aprovar texto final.
- `references/headlines.md`: banco de headlines e engine de hooks.
- `references/visual-system.md`: design system e template 1080x1350.
- `references/visual-principles.md`: principios visuais BrandsDecoded.
- `references/examples.md`: exemplos bons para calibragem.

## Aprendizados (memoria persistente)

Ler `aprendizados.md` (raiz da skill) ANTES de produzir ou exportar carrossel. Contem regras
acumuladas sobre export (deviceScaleFactor, sharp), reset de modo preview, frames de imagem
e armadilhas de Windows.

## Fluxo obrigatorio

1. Briefing criativo: confirme tema, objetivo, publico, promessa, CTA, marca, handle, direcao visual, pasta de saida e quantidade aproximada de slides.
2. Triagem editorial: aplique `editorial-quality.md` e `editorial-filter.md` para eliminar tese fraca, obviedade, exagero e voz generica.
3. Gere 10 headlines usando `headlines.md`. Mostre as opcoes e recomende uma.
4. Monte a espinha dorsal do carrossel: abertura, conflito, desenvolvimento, virada, fechamento e CTA.
5. Escreva o texto completo slide a slide e peca aprovacao antes do HTML.
6. Sugira imagens/assets necessarios ou use imagens fornecidas pelo usuario.
7. Crie o HTML editavel na pasta de saida configurada.
8. Exporte PNGs com Playwright para `slides-png/`.
9. Entregue legenda final e checklist de arquivos gerados.

## Estrutura de saida recomendada

```text
[pasta-de-saida]/[slug]/
  carousel-text.md
  carousel.html
  assets/
  slides-png/
```

## Exportacao

Use o script da skill local:

```bash
node .claude/skills/carrossel/scripts/export-carousel-playwright.js [pasta-ou-html-do-carrossel]
```

O export deve capturar cada elemento `.slide`, esperar `document.fonts.ready`, inlinear assets locais em base64 quando necessario, validar PNGs em `1080x1350` e salvar em `slides-png/`.

## Regras

- Nao use material de `templates/skills`.
- Nao copie `node_modules`, `.git`, ZIPs, PDFs, PNGs renderizados ou carrosseis antigos como assets da skill.
- Nao assuma marca, handle, paleta, CTA ou pasta de saida sem setup completo.
- Nao invente fatos, numeros, estudos, datas ou claims atuais. Pesquise quando a informacao puder ter mudado.
- Preserve uma voz direta, editorial e especifica ao nicho configurado, sem promessa milagrosa e sem texto com cara de IA.
