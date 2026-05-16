---
name: gpt-image-2
description: Planeja e gera imagens com GPT Image 2, incluindo briefing visual, previews baratos em baixa qualidade, escolha de direcao, pergunta obrigatoria sobre quality high na imagem final, definicao de size/formato/background e salvamento dos assets. Use para qualquer geracao ou edicao de imagem, assets de carrossel, fundos, mockups, cenas, texturas, ilustracoes, variacoes visuais e imagens finais.
---

# GPT Image 2

Use esta skill para gerar ou editar imagens com GPT Image 2. Ela nao e especifica para carrosseis: funciona para assets, imagens finais, fundos, mockups, cenas editoriais, texturas, objetos, composicoes e variacoes visuais.

## Premissas

- Modelo preferido: `gpt-image-2`, quando disponivel no ambiente/API.
- Se o ambiente nao aceitar `gpt-image-2`, pare e informe o modelo realmente disponivel antes de gerar.
- Para imagens com texto critico, prefira gerar sem texto e aplicar texto depois em HTML, Figma, Canva ou editor equivalente.
- Nao prometa reproducao perfeita entre preview e final. Preview valida direcao visual; a imagem final deve ser regerada ou editada a partir da direcao escolhida.
- Use o script `scripts/generate-image.py` para chamadas normais. Nao escreva wrappers ad hoc salvo se o usuario pedir alterar a skill.

## Loop operacional

1. Classifique o pedido: `generate`, `edit`, `inpaint` ou `multi-reference`.
2. Leia `references/prompt-craft.md` quando o pedido envolver fotografia, produto, poster, UI, diagrama, infografico, imagem com referencia ou prompt fraco.
3. Leia `references/quality-and-preview.md` quando houver duvida sobre preview, custo, quality ou size.
4. Pergunte se o usuario quer usar o fluxo de preview antes da imagem final, salvo quando ele ja pediu explicitamente para gerar direto.
5. Confirme no maximo uma pergunta critica antes de chamadas caras ou ambiguas.
6. Rode preflight: modo, prompt, paths, size, quality, format, background, referencia/mask e destino.
7. Execute via `scripts/generate-image.py`.
8. Reporte arquivos, parametros e um ajuste recomendado se fizer sentido.

## Briefing minimo

Antes de gerar, defina:

- Objetivo da imagem.
- Uso final: asset, capa, fundo, mockup, anuncio, post, hero, thumbnail ou outro.
- Assunto principal e elementos proibidos.
- Estilo visual: fotografia, 3D, editorial, ilustracao, colagem, flat, isometrico, surreal, minimalista etc.
- Composicao: enquadramento, perspectiva, quantidade de espaco negativo e area reservada para texto.
- Paleta ou referencias de marca.
- Saida: pasta/caminho, nome base do arquivo e formato.
- `size`: `1024x1024`, `1536x1024`, `1024x1536` ou `auto`.
- `background`: opaco, transparente ou `auto`, quando suportado.
- `output_format`: `png`, `jpeg` ou `webp`.
- `output_compression`: 0-100 somente para `jpeg`/`webp`, quando suportado.

Se a imagem for para carrossel vertical, recomende `1024x1536`. Se for asset recortavel, pergunte se precisa de fundo transparente.

## Modos

- `generate`: texto para imagem. Use quando nao houver `--image`.
- `edit`: uma ou mais imagens de referencia. Use `--image` repetivel e diga no prompt o papel de cada referencia.
- `inpaint`: edicao localizada com `--image` e `--mask`. Confirme que a mascara PNG existe.
- `multi-reference`: edicao com varias referencias. Identifique cada arquivo por funcao: imagem 1 = sujeito, imagem 2 = estilo, imagem 3 = logo etc.

Para edicoes, preserve invariantes explicitamente: identidade, layout, posicao, texto existente, proporcao, cor de marca e elementos que nao devem mudar.

## Estrategia de preview

Antes de gerar imagens, pergunte:

> "Voce quer usar o fluxo de preview em `quality: low` antes da imagem final?"

Se o usuario responder sim, use previews em baixa qualidade para validar conceito, composicao, estilo ou direcao visual. Se responder nao, gere direto a imagem final depois de confirmar os parametros finais.

Nao pergunte de novo quando o usuario ja disser algo como "gere direto", "sem preview", "quero so uma imagem final" ou "usa preview".

Fluxo recomendado:

1. Propor 3 a 6 direcoes visuais em texto, sem gerar imagem.
2. Selecionar ate 3 direcoes candidatas.
3. Gerar previews com `quality: low` e `size` igual ao formato final pretendido.
4. Pedir escolha da direcao vencedora e ajustes objetivos.
5. Gerar a imagem final com prompt refinado.

Quando houver mais de um asset no mesmo projeto, repetir o fluxo de preview para cada asset relevante. Nao pular preview de asset secundario se o usuario escolheu fluxo com preview. As opcoes de preview devem testar ideias visuais diferentes, nao apenas variacoes de angulo, zoom ou posicao.

Nao use preview como final. Nao trate preview low como upscale automatico. Se a continuidade visual for importante, use o preview escolhido como referencia de edicao quando o ambiente aceitar imagem de entrada; caso contrario, regerar com prompt refinado.

## Qualidade final

Antes da imagem final, pergunte explicitamente:

> "Voce quer gerar a imagem final em `quality: high`?"

Recomende:

- `medium` como padrao para assets comuns, fundos, texturas, mockups simples, imagens que ficarao atras de texto ou imagens pequenas no layout.
- `high` para capa, hero, imagem que ocupa grande parte da arte, mockup/produto com alta nitidez, asset reutilizavel fora do projeto ou quando o `medium` ficar visualmente fraco.
- `low` somente para preview, rascunho ou validacao rapida.

Se o usuario responder "nao" para high, use `medium` salvo se ele pedir outro valor.

## Preflight

Antes de executar, confirme:

- `OPENAI_API_KEY` existe no ambiente, `.ai/skills/.env`, `.env` local ou `~/.env`; nunca imprima o valor e nunca crie arquivo de segredo sem pedido explicito.
- Caminho de saida nao sobrescreve algo importante sem confirmacao.
- Imagens de referencia existem quando `--image` for usado.
- Mascara existe quando `--mask` for usada.
- `--format` e compativel com `--compression`; compressao so para `jpeg` e `webp`.
- `quality` foi escolhido; para final, confirme se sera `high`.

Comando base:

```bash
python .ai/skills/gpt-image-2/scripts/generate-image.py --prompt "..." --file caminho/saida.png --size 1024x1536 --quality medium
```

Edicao com referencia:

```bash
python .ai/skills/gpt-image-2/scripts/generate-image.py --prompt "..." --image ref.png --file saida.png --size 1024x1536 --quality medium
```

## Prompt final

Monte prompts com:

- Descricao objetiva da cena.
- Sujeito principal e contexto.
- Estilo, materialidade, luz, lente/perspectiva, nivel de realismo.
- Composicao e espaco negativo.
- Cores permitidas e cores a evitar.
- O que nao deve aparecer.
- Regras de texto: "sem texto, sem letras, sem marcas d'agua, sem UI falsa", quando aplicavel.

Para assets de layout, inclua instrucoes como "deixar area limpa no terco superior", "fundo simples", "objeto isolado", "com margem para recorte" ou "sem elementos importantes nas bordas".

## Parametros do script

- `--prompt`: obrigatorio.
- `--file`: caminho de saida. Se `--n` for maior que 1, o script adiciona sufixos.
- `--image`: repetivel; ativa o endpoint de edits.
- `--mask`: PNG com alpha; requer `--image`.
- `--model`: padrao `gpt-image-2`.
- `--size`: `1024x1024`, `1536x1024`, `1024x1536`, `auto` ou aliases `square`, `landscape`, `portrait`.
- `--quality`: `low`, `medium`, `high` ou `auto`.
- `--n`: quantidade de imagens.
- `--background`: `auto`, `opaque` ou `transparent`, quando suportado.
- `--format`: `png`, `jpeg` ou `webp`.
- `--compression`: 0-100 para `jpeg`/`webp`.
- `--moderation`: `auto` ou `low`, quando suportado.
- `--user`: identificador opcional do usuario final.

## Nomes e salvamento

Salve imagens com nomes descritivos:

```text
[pasta]/[slug]-preview-01.png
[pasta]/[slug]-preview-02.png
[pasta]/[slug]-final.png
```

Ao finalizar, informe:

- prompt final usado;
- parametros usados: model, quality, size, format, background;
- arquivos gerados;
- se a imagem e preview ou final.

## Regras

- Nao gere imagem final sem confirmar se deve ser `quality: high`.
- Nao use `high` como padrao automatico.
- Nao inclua texto pequeno ou informacao critica dentro da imagem quando o layout final puder renderizar texto com mais controle.
- Nao invente marcas, logos, pessoas reais, dados, produtos ou claims factuais. Pesquise ou peca referencia quando necessario.
- Para imagem de pessoa real, marca registrada, produto especifico ou interface real, use referencias fornecidas ou confirme permissao/contexto antes de gerar.
- Se a API rejeitar parametro/modelo, mostre o erro de forma suficiente para debug e ajuste apenas o parametro incompatível.
