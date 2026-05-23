# Qualidade, preview e custo

Use este arquivo quando precisar explicar ou decidir a estrategia de custo/qualidade para GPT Image 2.

## Regra pratica

Antes de gerar, pergunte se o usuario quer usar preview:

```text
Voce quer usar o fluxo de preview em quality: low antes da imagem final?
```

Se o usuario pedir explicitamente para gerar direto, sem preview, ou ja escolher preview, nao repita a pergunta.

Preview em `low` faz sentido quando o usuario escolhera entre varias direcoes. Nao faz sentido como etapa obrigatoria quando a imagem ja esta bem definida e seria gerada uma unica vez.

Quando um projeto tiver mais de um asset, o compromisso de preview vale para cada asset relevante. Nao gerar asset secundario direto em final se o usuario escolheu fluxo de preview. As previews devem explorar abordagens diferentes de conceito, metafora ou composicao; mudar apenas angulo, zoom ou crop nao e suficiente.

Exemplo de decisao:

- 1 imagem muito bem definida: gerar direto final, perguntando antes se sera `high`.
- 3 a 6 possibilidades conceituais: gerar primeiro direcoes em texto.
- 2 a 3 direcoes fortes: gerar previews `low`.
- Direcao aprovada: gerar final `medium` ou `high`, conforme decisao do usuario.

## Qualidade

- `low`: rascunho, preview, validacao de composicao, custo/latencia menores.
- `medium`: padrao recomendado para a maioria dos assets finais.
- `high`: usar quando nitidez e acabamento visual compensam custo/latencia maiores.
- `auto`: aceitar quando o usuario preferir delegar ao modelo, mas para controle de custo prefira escolher explicitamente.

Sempre perguntar antes da final:

```text
Voce quer gerar a imagem final em quality: high?
```

Se a resposta for negativa ou indiferente, usar `medium`.

## Upscale

Nao vender preview low como "upscale". O fluxo correto e:

1. Preview low valida direcao.
2. Final e gerado ou editado em qualidade maior.
3. Upscale externo/local so entra se a imagem final aprovada precisar de mais resolucao sem mudar composicao.

Quando consistencia visual exata for importante, preferir edicao com a imagem escolhida como referencia em vez de regeracao solta.

## Tamanhos

- `1024x1024`: quadrado, posts, icones, thumbnails.
- `1536x1024`: paisagem, hero, banners, capas horizontais.
- `1024x1536`: retrato, carrossel vertical, stories, posters.
- `auto`: usar quando o formato ainda nao foi definido.

Para carrossel 1080x1350, `1024x1536` costuma ser o melhor ponto de partida porque preserva composicao vertical e margem de corte.
