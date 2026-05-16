# Guia de Design - EssentialWeb

> Voce pode editar esse arquivo a qualquer momento.
> As skills de carrossel, proposta e slide leem este arquivo antes de criar qualquer visual.

---

## Cores

- **Fundo principal:** azul-marinho quase preto / ink (`#081311`, `#0d1715`, HSL aproximado `210 43% 9%`).
- **Cor de destaque / CTA:** verde mint/teal (`#17b7a6`, HSL aproximado `160 63% 46%`).
- **Destaque claro:** mint claro (`#71e4d8`) para palavras-chave em fundo escuro.
- **Acento secundario:** amarelo/saffron (`hsl(45 90% 57%)`) com uso pontual.
- **Texto principal:** branco em fundos escuros; ink em fundos claros.
- **Texto de apoio:** cinzas frios e brancos com opacidade entre 45% e 70%.
- **Fundo alternativo / cards:** fundos claros esverdeados (`#edf6f4`) e cards brancos; em dark, glass panels em navy/ink.
- **Cor proibida:** evitar paleta roxa/purple-blue generica e visual SaaS default sem relacao com a marca.

---

## Tipografia

- **Titulos e destaques do site:** `Space Grotesk`.
- **Corpo, subtitulos e botoes do site:** `Outfit`.
- **Carrosseis:** usar headline condensada e forte quando o formato pedir impacto; referencia atual usa `Barlow Condensed`/fallback condensado e corpo em `Plus Jakarta Sans`/Segoe UI.
- **Peso do titulo:** forte, geralmente 800-900 em pecas sociais e 700-800 no site.

---

## Estilo geral

Tecnologia B2B moderna, escura, objetiva e orientada a conversao. O visual deve passar clareza operacional, velocidade e confianca tecnica, sem parecer template generico de SaaS.

O site usa fundo escuro, grids sutis, glass panels, glow mint, bordas discretas, motion leve e CTAs evidentes. Os carrosseis usam ritmo editorial, alternancia claro/escuro, headlines grandes, safe area generosa, progresso visual e CTA final conectado ao conteudo.

---

## Elementos-chave

- **Bordas:** finas, com opacidade baixa em mint ou cinza frio.
- **Border-radius dos cards:** medio, entre 12px e 20px conforme formato.
- **Botoes:** arredondados, mint com texto ink em CTA principal; estados hover sutis.
- **Sombras:** glow mint controlado e sombras profundas em dark UI; evitar sombras decorativas excessivas.
- **Motion:** reveal suave, sheen discreto e floating leve. Movimento nunca deve atrapalhar leitura.
- **Carrosseis:** 1080x1350, accent bar, brand bar discreta, progress bar e conteudo alinhado pela base.

---

## O que NUNCA fazer

- Nao usar copy generica de IA, frases motivacionais vagas ou hooks desgastados.
- Nao centralizar todo o conteudo dos carrosseis por padrao; o layout editorial aprovado usa alinhamento forte e base visual.
- Nao usar CTA desconectado do insight anterior.
- Nao usar afirmacao factual sem dado/fonte/periodo quando a peca depende de credibilidade.
- Nao deixar texto com baixo contraste sobre imagens; legibilidade vence a imagem.
- Nao usar roxo generico, gradientes aleatorios ou cards decorativos sem funcao.

---

## Logo

- **Site, versao header:** `projetos/essential-web/public/header_logo.png`
- **Site, versao limpa:** `projetos/essential-web/public/clean_logo.png`
- **Carrosseis:** `projetos/carrosseis claude/assets/Logo EssentialWeb.png`
- **Onde usar:** header do site/propostas, badge de marca em carrosseis, slide final do carrossel e materiais comerciais.
- **Tamanho sugerido:** largura entre 120-200px em HTMLs, ajustando conforme contraste e composicao.

---

## Perfil do autor

> Usado no estilo "tweet" do carrossel. Preenchido automaticamente no setup.

- **Nome:** EssentialWeb
- **Handle:** @essentialweb
- **Foto:** usar logo da marca quando nao houver foto pessoal.
- **Badge verificado:** sim, quando fizer sentido visual no template.

---

## Observacoes adicionais

- Para carrosseis da EssentialWeb, usar `projetos/carrosseis claude/` como referencia ate a skill dedicada ser criada.
- Manter HTMLs e MDs de carrosseis em UTF-8 sem BOM; no Windows, evitar regravar com ferramenta que gere mojibake.
- Site institucional de referencia: `projetos/essential-web/`.
