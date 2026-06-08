# Planejamento de Tráfego — Estúdio Lumina

**Data:** 23/05/2026 · **Período analisado:** 20–23/05 (4 dias) · **Campanha:** `lumina-aniversario-adulto-01` (CTWA)

---

## 0. Diagnóstico oficial — RECEITA REAL (base de decisão)

> Este é o diagnóstico oficial. Usa as **4 vendas reais** (não a receita que o Meta atribui).
> O Meta enxerga só R$ 34,89 de R$ 119,89 reais — subnotifica 71% da receita por falta de
> `ctwa_clid`. Decisões de escala e otimização seguem os números reais abaixo.

**Vendas reais:** 5 = 2 capturadas pelo Meta + R$ 70,00 (23/05), R$ 15,00 (22/05) e R$ 5,00 (24/05)
não atribuídas. A de 24/05 (R$ 5,00) é um caso à parte: a cliente **não clicou no anúncio** —
veio pelo perfil do Instagram e de lá foi pro WhatsApp, então nunca houve `ctwa_clid` pra perder
(ver seção 5, item "tráfego de marca / orgânico").

| Indicador | Meta reporta | **Real (base oficial)** |
|---|---|---|
| Gasto | R$ 33,52 | R$ 33,52 (R$ 8,38/dia) |
| Vendas | 2 | **5** |
| Receita | R$ 34,89 | **R$ 124,89** |
| **ROAS** | 1,06 | **3,73** (benchmark 2,5–4,0 = bom) |
| Conversa → venda | 10,5% | **21,1%** |
| Custo por venda | R$ 16,45 | **R$ 8,38** |
| Ticket médio | R$ 17,45 | **R$ 29,97** |
| CPM | R$ 22,27 (bom) | — |
| CTR / Frequência | 2,33% / 1,12 (sem fadiga) | — |
| Custo por conversa | R$ 1,76 (excelente) | — |
| Clique → conversa | 54% | — |

**Leitura:** campanha **lucrativa e saudável** (ROAS real 3,58). Aquisição barata e eficiente,
fechamento de 21% mesmo com atendimento manual, ticket médio R$ 29,97 (acima do pacote base
R$ 24,90 → upsell/pacotes maiores funcionando).

**Implicações para o plano:**
- **Pode escalar** verba gradualmente (+20–30% por vez) — a trava "não escalar com ROAS 1,06" cai.
- O agente de IA **já está ativo** (não é mais pendência) — agora é medir o ganho de fechamento.
- A subnotificação do `ctwa_clid` é **limitação aceita** (Coexistence é requisito) — ver seção 5.
  Não é ação no plano; só usamos o ROAS real como bússola.

> A coluna "Meta reporta" (seção 1) mostra a subnotificação. A leitura de decisão é a real.

---

## 1. Métricas detalhadas (real vs. o que o Meta reporta)

> Os números **reais** são a base de decisão (seção 0). A coluna "Meta reporta" fica só pra
> mostrar o tamanho da subnotificação por falta de `ctwa_clid`.

| Métrica | Real (base) | Meta reporta | Benchmark BR |
|---|---|---|---|
| Gasto total | R$ 33,52 (~R$ 8,38/dia) | R$ 33,52 | — |
| Impressões / Alcance | 1.505 / 1.345 | — | — |
| CPM | R$ 22,27 | — | R$ 8–25 = bom |
| CTR | 2,33% | — | saudável |
| Frequência | 1,12 | — | < 2 = ótimo (sem fadiga) |
| Conversas WhatsApp | 19 | 19 | — |
| **Custo por conversa** | **R$ 1,76** | — | excelente |
| Clique → conversa | 54% | — | forte |
| **Conversa → venda** | **21,1%** (4 de 19) | 10,5% | bom (no manual) |
| Custo por venda | **R$ 8,38** | R$ 16,45 | ótimo |
| Ticket médio | **R$ 29,97** | R$ 17,45 | acima do pacote base |
| **ROAS** | **3,58** | 1,06 | 2,5–4,0 = bom |

### Onde está o problema (e onde NÃO está)

- **A mídia funciona e a campanha lucra.** CPM bom, CTR saudável, 54% de clique→conversa,
  R$ 1,76 por conversa e ROAS real **3,58**. Aquisição barata e eficiente.
- **A subnotificação é uma limitação estrutural, não uma tarefa.** O Meta enxerga só
  R$ 34,89 de R$ 119,89 reais (71% invisível) porque parte dos touchpoints chega sem
  `ctwa_clid` (erro 131060, inerente ao Coexistence). Como o número precisa manter o app no
  celular, **não vamos sair do Coexistence** — então essa perda parcial é aceita e permanente.
  Ver seção 5 (limitações conhecidas).
- Implicação prática: o ROAS do painel do Meta vai sempre parecer pior que o real. **Decisões
  usam o ROAS real** (calculado com as vendas confirmadas no WhatsApp/CRM), não o do painel.

---

## 2. Situação dos criativos

| Anúncio | Gasto | Impressões | CTR | Conversas |
|---|---|---|---|---|
| **Anúncio 2 (Resultado)** | R$ 30,31 | 1.408 | 2,13% | **19** |
| Anúncio 3 (Antes/Depois) | R$ 0,70 | 16 | 12,50% | 0 |
| Reframe | R$ 1,88 | 42 | 2,38% | 0 |

- **Anúncio 2 carrega 100% das conversas** — o algoritmo concentrou quase todo o orçamento nele e os outros dois foram praticamente desligados.
- **Risco:** campanha dependente de um único criativo. Quando ele fadigar, a campanha cai sem substituto.
- Anúncio 3 teve CTR de 12,5%, mas com só 16 impressões — amostra insignificante, não dá pra concluir nada.

---

## 3. Plano de ação (ordem por impacto) — só o que está sob nosso controle

### Prioridade 1 — Escalar verba (a campanha já comporta)
ROAS real 3,58 justifica escalar. A trava anterior ("não escalar") era artefato da subnotificação.
- Subir o orçamento **+20–30% por vez**, sem resets bruscos, acompanhando o **ROAS real** (CRM),
  não o do painel do Meta.
- Hoje ~R$ 8/dia; primeiro passo pra ~R$ 10–11/dia e observar 3–4 dias.

### Prioridade 2 — Medir o impacto do agente de IA (já implementado)
O agente de IA **já está implementado e ativo** no WhatsApp (prompt + tool de exemplos + PIX +
handoff + echo/pausa por intervenção humana). O fechamento de 21% foi medido ainda no atendimento
manual — agora é monitorar a nova janela com o agente operando.
- Acompanhar a **nova taxa conversa→venda** com o agente respondendo (resposta imediata < 5 min garantida pela automação).
- **Meta:** conversa→venda de 21% → 30%+.
- Validar qualidade da conversa (não só quantidade): o agente está qualificando, enviando exemplos e fechando com PIX corretamente?

### Prioridade 3 — Proteger e diversificar criativo (paralelo, baixo custo)
- Criar **3 variações do Anúncio 2 (Resultado)** — mesmo formato vencedor, ganchos diferentes
  (pergunta, prova/depoimento, dualidade preço-tradicional vs IA).
- Pausar formalmente Reframe e Anúncio 3 (já zerados) pra concentrar verba.

### Prioridade 4 — Lookalike de compradores (limitado pela atribuição)
- **Atenção:** como parte das compras chega sem `ctwa_clid`, o público de compradores que o
  Meta forma é incompleto — o lookalike vai aprender com dados parciais. Ainda vale testar quando
  houver volume (50+ Purchases/semana no CAPI), mas com expectativa calibrada por causa da seção 5.

---

## 4. Metas para a próxima janela (próximos 7–14 dias)

| Indicador | Hoje (real) | Meta |
|---|---|---|
| ROAS real | 3,58 | manter ≥ 3,0 ao escalar |
| Conversa → venda | 21,1% | 30%+ (com agente) |
| Custo por venda | R$ 8,38 | manter < R$ 12 |
| Orçamento/dia | R$ 8,38 | escalar gradual (+20–30%/vez) |
| Criativos ativos | 1 efetivo | 4+ |

**Regra de ouro:** a campanha lucra (ROAS real 3,58). Escalar com cautela acompanhando o ROAS
**real** (confirmado no WhatsApp/CRM), porque o painel do Meta sempre vai subnotificar.

---

## 5. Limitações conhecidas (aceitas, sem ação prevista)

- **`ctwa_clid` perdido em parte dos leads (erro 131060 / Coexistence).** O número opera em
  Coexistence (Cloud API + app no celular), o que é requisito da operação. Nesse modo, mensagens
  de companion devices chegam degradadas e sem `ctwa_clid` — e **não há como recuperar** o que já
  veio assim, nem evento secundário que o traga. A única correção de raiz seria sair do Coexistence
  (número 100% Cloud API), o que **foi descartado** porque o atendimento pelo celular é necessário.
- **Consequências aceitas:** (a) o ROAS do painel do Meta fica subnotificado — por isso usamos o
  ROAS real; (b) o lookalike de compradores aprende com dados parciais; (c) vendas como as de
  Mônica (R$70/R$15) ficam registradas só no CRM, não na atribuição do Meta.
- **Tráfego de marca / orgânico (caso distinto do 131060).** Quando o cliente **não clica no
  anúncio** — ex.: chega pelo perfil do Instagram, pela bio, por um post orgânico ou indicação e
  de lá vai pro WhatsApp — **nunca existiu `ctwa_clid`**. Não é um clid "perdido"; é um lead que não
  passou pelo anúncio. O Meta corretamente não atribui essa venda à campanha (venda de R$ 5,00 em
  24/05 foi assim). **Esse tráfego é influenciado pelos anúncios** (presença de marca leva gente a
  procurar o perfil), mas não há mecanismo CTWA que ligue a venda à campanha — só análise de canal
  (last-click do CRM) consegue separar "veio do anúncio" de "veio do orgânico".
  - *Como (não) rastrear:* o `ctwa_clid` **só nasce do clique no botão do anúncio CTWA**. Perfil→WhatsApp
    gera no máximo um `referral` genérico de Instagram/página, sem amarração à campanha/anúncio. A única
    forma de tracking é no atendimento/CRM: registrar a **origem declarada** ("como você nos achou?") e
    classificar como orgânico vs. anúncio. Não dá pra recuperar no Meta depois.
- **Mitigação possível (não-prioritária):** manter o registro manual de vendas no CRM/histórico
  pra que a leitura de ROAS real continue fiel, mesmo com o Meta cego a uma fração — incluindo a
  **origem do lead** (anúncio / perfil-orgânico / indicação) pra não misturar ROAS de mídia com venda orgânica.

---

## 6. Campanha Dia dos Namorados (nova) — estrutura e direção criativa

> Ancorada no `_contexto/ICP-namorados.md` (persona Mariana Lopes, 22–34). **Campanha NOVA e
> separada** da de aniversário — ICP, oferta e criativo mudam estruturalmente (critério Sobral).

### A persona em uma frase
Mulher 22–34 que quer **presentear o parceiro** com algo criativo e emocional, fugindo do óbvio
(caneca, chocolate, perfume). Dores centrais: "**a gente quase não tem foto bonita junta**" e "**ele
morre de vergonha de posar**". Ela não compra imagens — compra a sensação de ser criativa e atenciosa.
> Promessa-síntese do nicho: *"Transforme fotos simples do casal em um ensaio romântico criado com
> IA, pronto para emocionar no Dia dos Namorados."*

### Por quê campanha nova (e não adset novo)
- **ICP diferente:** aniversário mira a própria pessoa; Namorados mira a **presenteadora** (foco no casal).
- **Oferta diferente:** pacotes românticos próprios (ver abaixo), não o de aniversário.
- **Criativo diferente:** estética romântica/cinematográfica, ângulos de presente.
- **Leitura limpa:** misturar contamina o aprendizado do algoritmo. Campanha separada = orçamento e
  métricas isolados; quando a data passar, pausa a campanha sem tocar na de aniversário.

### Estrutura recomendada
```
Campanha: lumina-namorados-2026  (CTWA / OUTCOME_ENGAGEMENT / CONVERSATIONS / WHATSAPP)
  └─ 1 conjunto: namorados-br  (feminino, 22–34, BR — espelha o ICP)
       └─ 4–6 criativos românticos
```
- **Um adset só** no início (verba baixa → menos segmentação, mais clareza de criativo/oferta — Sobral).
- **Janela:** subir **02–05/jun** (7–10 dias antes de 12/jun). Em cima da data = CPM caro (pico) + sem
  tempo de otimizar. Produção dos criativos precisa começar ~27–28/05 pra chegar folgada.
- Público feminino 22–34 reflete o submercado primário ("namoradas românticas e criativas"). Os homens
  "last-minute" (submercado 2) podem ser um segundo adset SE houver verba — não no início.

### Oferta para a campanha (preços fechados — fonte: `_contexto/empresa.md`)

| Pacote | Conteúdo | Preço |
|---|---|---|
| Casal Essencial | 10 fotos do casal, 1 cenário + frase romântica | R$ 39,90 |
| **Casal Romântico** ⭐ (carro-chefe) | 10 fotos, 3 cenários + frase + versão story | **R$ 59,90** |
| Casal Inesquecível | 15 fotos, 4–5 cenários + versão story | R$ 89,90 |

- **Upsell:** Entrega Express 4h +R$ 19,99 (disponível pra todos os pacotes; oferecer só se cliente sinalizar pressa).
- **Versão story:** 2 fotos finais (escolhidas pelo cliente após a entrega) reenquadradas em 9:16,
  prontas pra postar (no Romântico e Inesquecível).
- **R$ 59,90 é aposta de mercado a validar:** subir com ele; se conversa→venda cair muito vs.
  aniversário, testar R$ 49,90. Posicionamento de **presente** (compara com chocolate/perfume/jantar
  R$ 80–200), não autoimagem — por isso acima dos pacotes de aniversário.
- **Fluxo de casal:** ✅ confirmado com a operação (ensaio com qualquer nº de pessoas). Input = foto
  do casal (ou 2 fotos separadas). Não é mais bloqueio.

### Direção criativa — ângulos (testar 1 por vez, formato "Resultado" constante)
Ordenados por força no ICP. Ganchos saídos direto das seções W/X/Y/Z do ICP:

1. **Anti-óbvio (mais forte)** — "Chega de caneca, chocolate e perfume: transforme o amor de vocês
   num ensaio romântico criado com IA." Ataca o inimigo nº1 da persona.
2. **Ele não gosta de posar** — "Ele odeia tirar foto? Crie um ensaio de casal sem convencer ninguém
   a posar." Resolve a dor mais específica e diferenciada.
3. **A foto que nunca tiveram** — "Vocês têm mil momentos juntos, mas quase nenhuma foto bonita?"
4. **Desejo/cena de cinema** — "Imagine entregar pra ele uma imagem de vocês dois em Paris, na praia
   ou numa cena de filme."
5. **Última hora** — "Faltam poucos dias e você ainda não comprou nada? Parece caro, mas é digital,
   rápido e personalizado." (urgência real da data).

### Direção visual (estilos que a persona deseja — usar nos criativos e na tool de exemplos)
Paris · praia paradisíaca · capa de revista romântica · cena de filme · casamento dos sonhos ·
pôr do sol no campo · jantar luxuoso · editorial de moda · polaroid/vintage. Mostrar **antes/depois**
(selfie comum → cena cinematográfica) é o que mais reduz a objeção "vai parecer com a gente?".

### Quebra de objeção (embutir no criativo/legenda e no agente)
- "Vai parecer com a gente?" → mostrar antes/depois realista.
- "Ele vai achar brega / foto de IA não é real" → enquadrar como **presente emocional**, não como
  "tecnologia". A IA é o meio, nunca o herói (alinhado ao `preferencias.md`).
- "Vale pagar por algo digital?" → comparar com ensaio de casal tradicional (fração do preço).

### Aviso operacional (atribuição)
Herda a limitação de `ctwa_clid` (seção 5). Medir o ROAS **real** pelo CRM desde o dia 1 — o painel
do Meta vai subnotificar essa campanha também.
