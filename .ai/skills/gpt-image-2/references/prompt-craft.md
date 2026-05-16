# Prompt Craft para GPT Image 2

Use este arquivo para melhorar prompts antes de gerar imagens caras ou com requisitos visuais delicados.

## Estrutura base

Ordem recomendada:

```text
Canvas e uso final -> composicao -> sujeito -> contexto -> materiais/luz/paleta -> restricoes -> formato esperado
```

Exemplo:

```text
Asset vertical 2:3 para carrossel, com area limpa no terco superior para texto. Cena editorial de uma mesa de trabalho com notebook aberto, blocos de automacao e post-its organizados. Luz natural lateral, paleta mint, ink e off-white, fotografia realista com leve profundidade de campo. Sem texto, sem marcas, sem logos falsos, sem UI legivel.
```

## Fotografia

- Defina contexto de captura: foto de estúdio, foto documental, iPhone casual, editorial, macro, produto.
- Escolha uma lente/perspectiva dominante; nao empilhe muitas especificacoes.
- Inclua 5 a 12 objetos concretos da cena e 2 a 4 detalhes de material/luz.
- Para realismo, prefira imperfeicoes plausiveis: reflexos, sombras naturais, textura, poeira leve, marcas de uso.

## Produto e mockup

Use prompt em blocos quando houver muitos controles:

```text
PRODUCT_RENDER_CONFIG:
GLOBAL: asset vertical 2:3, editorial, sharp foreground, generous negative space.
SUBJECT: ...
MATERIALS: ...
LIGHTING: ...
BACKGROUND: ...
AVOID: fake brand logos, cheap CGI, unreadable labels, clutter.
```

Separe materiais, iluminacao e paleta. "Premium" sozinho e fraco.

## Poster, capa e imagem promocional

- Defina hierarquia visual mesmo quando o texto sera aplicado depois.
- Se houver texto obrigatorio dentro da imagem, coloque cada string entre aspas e use `quality: high`.
- Para carrossel, prefira sem texto e reserve area limpa para o HTML.
- Aplique o teste de tres olhares: silhueta clara, narrativa compreensivel, detalhes interessantes de perto.

## UI e telas

- Trate como especificacao de produto: dispositivo, layout, componentes, dados e estados.
- Use nomes ficticios quando nao houver referencia real.
- Se a UI for apenas decorativa, diga que textos podem ser abstratos. Se for legivel, forneca todos os labels.
- Para carrossel, normalmente evite UI legivel gerada; prefira mockup abstrato e texto real no HTML.

## Diagramas e infograficos

- Nomeie o tipo: fluxograma, mapa mental, diagrama em camadas, matriz, timeline, small multiples, arquitetura.
- Defina zonas fixas: topo, esquerda, direita, rodape, callouts.
- Forneca labels exatos se precisarem ser lidos.
- Use `quality: high` para diagrama final com texto denso. Para asset de fundo, gere sem texto.

## Edicao com referencia

Se usar `--image`, o prompt deve dizer:

- O papel de cada referencia.
- O que mudar.
- O que preservar.
- Qual detalhe nao pode driftar: identidade, pose, composicao, texto, produto, logo, proporcao, cor.

Modelo:

```text
Imagem 1 e o produto principal. Imagem 2 e referencia de estilo. Aplique a luz e paleta da imagem 2 ao produto da imagem 1. Preserve formato, proporcao, cor principal e todos os detalhes do produto. Nao altere logotipo, texto ou geometria.
```

## Negativos

Use poucos negativos e bem direcionados:

- `sem texto`
- `sem logos falsos`
- `sem marca d'agua`
- `sem UI legivel`
- `evitar visual de banco de imagem`
- `evitar CGI plastico`

Listas longas de proibicoes podem atrapalhar a composicao.
