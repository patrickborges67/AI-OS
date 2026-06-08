# Aprendizados — Meta Ads Ratos

Regras aprendidas durante o uso. O Claude DEVE ler este arquivo antes de criar qualquer objeto.

---

### 2026-04-03 — Sempre incluir CTA no criativo
**Regra:** Ao criar criativos (create.py creative), SEMPRE incluir call_to_action_type. Padrão: LEARN_MORE pra tráfego, SIGN_UP pra leads, SHOP_NOW pra vendas. Nunca criar criativo sem CTA.
**Contexto:** Criou carrossel sem botão de CTA. Usuário teve que corrigir manualmente.

### 2026-04-03 — Carrossel Instagram: multi_share_end_card=false
**Regra:** Em campanhas de visita ao perfil Instagram, SEMPRE usar multi_share_end_card=false e multi_share_optimized=false no criativo.
**Contexto:** Cartão "Ver mais" sem URL quebrou o anúncio em 10 posicionamentos. O end_card exige uma URL de destino que não existe em campanhas de perfil.

### 2026-04-03 — Sempre passar instagram_user_id no criativo
**Regra:** Ao criar criativos pra Instagram, SEMPRE usar --instagram-user-id com o ID da conta Instagram do cliente (do contas.yaml).
**Contexto:** Sem instagram_user_id, o ad não publica no Instagram. Erro: "Seu anúncio deve ser associado a uma conta do Instagram."

### 2026-05-20 — Budget em um nível só (campanha OU adset, nunca os dois)
**Regra:** Nunca passar daily_budget no adset se a campanha já tem daily_budget, e vice-versa. API rejeita com erro 1885621.
**Contexto:** Criação de adset para Lumina falhou repetidamente até isolar que o budget duplo era o bloqueio.

### 2026-05-20 — bid_strategy default da API pode ser LOWEST_COST_WITH_BID_CAP
**Regra:** Sempre incluir bid_strategy explicitamente. O script agora defaulta para LOWEST_COST_WITHOUT_CAP. LOWEST_COST_WITH_BID_CAP exige bid_amount e causa erro 1815857 se não fornecido.
**Contexto:** Todas as tentativas de criar adset falhavam com "bid_amount obrigatório" porque a API assumia bid strategy com teto.

### 2026-05-20 — Click-to-WhatsApp exige WhatsApp vinculado à Página
**Regra:** Antes de criar campanha Click-to-WhatsApp, confirmar que a Página Facebook está vinculada a uma conta WhatsApp Business. Erro 2446886 se não estiver.
**Contexto:** Adset para Lumina com destination_type WHATSAPP falhou porque a página não tinha WhatsApp Business associado.

### 2026-04-03 — Desligar format options em carrosséis
**Regra:** Ao criar ads de carrossel, SEMPRE passar --degrees-of-freedom-spec com OPT_OUT pra carousel_to_video, image_touchups e standard_enhancements.
**Contexto:** "Blocos de coleção" e "mídia única" distorcem o carrossel sequencial. Desligar pra manter ordem dos slides.

### 2026-05-26 — Pixel em CTWA é por anúncio (tracking_specs), não no adset
**Regra:** Em campanhas Click-to-WhatsApp, o pixel/dataset NÃO fica no `promoted_object` do adset (que só carrega page_id). É aplicado **por anúncio** no `tracking_specs`, na entrada `{"action.type":["offsite_conversion"],"fb_pixel":["<PIXEL_ID>"]}`. Ads criados via POST simples nascem SEM essa linha — adicionar via update de tracking_specs.
**Contexto:** c1/c3 da Lumina recriados sem pixel; os outros ads (criados por outro caminho) tinham a linha offsite_conversion/fb_pixel e os recriados não. Corrigido via POST de tracking_specs no ad. Comparar tracking_specs do anúncio vencedor é a forma rápida de detectar ads sem pixel.

### 2026-06-01 — TODA campanha nova deve ser agendada pra 00:01 do timezone DA CONTA (padrão)
**Regra (padrão obrigatório):** SEMPRE que criar uma campanha nova, o `start_time` do adset deve ser **00:01:00 do próximo dia disponível, no timezone configurado da conta de anúncios**. Não perguntar se Patrick quer agendar — agendar é o padrão, garante que o orçamento diário roda 24h cheias desde o primeiro dia (sem desperdício do dia 1 com janela menor).

**Como calcular o start_time correto:**
1. GET `act_<ID>?fields=timezone_name,timezone_offset_hours_utc` pra pegar o offset da conta. **NUNCA assumir** baseado em onde Patrick está.
2. Determinar a próxima data viável: data atual no timezone da conta + 1 dia.
3. Montar string ISO com o offset literal: `YYYY-MM-DDT00:01:00<±HH:MM>`. Ex: conta em America/Sao_Paulo (UTC-3) → `2026-06-02T00:01:00-03:00`.
4. Após criar/atualizar o adset, **VALIDAR com GET** pra confirmar que `start_time` retornado bate. Se a Meta tiver sobrescrito (start_time no passado é sobrescrito silenciosamente, ver regra abaixo), refazer.

**Por que 00:01 e não 00:00:** 00:00 às vezes cai em "transição de dia" e a Meta pode tratar como dia anterior. 00:01 é seguro.

**Conta da Lumina:** `act_1399522635268024` → timezone `America/Sao_Paulo` (UTC-3) → `2026-XX-XXT00:01:00-03:00`.
**Conta EssentialWeb:** `act_1306638014333858` → confirmar antes via GET (não inferir).

### 2026-06-01 — start_time no passado é silenciosamente sobrescrito pelo "agora"
**Regra:** Se enviar `start_time` que JÁ PASSOU (data anterior ao momento da chamada da API), a Meta NÃO retorna erro — ela substitui silenciosamente pelo timestamp da criação. O adset começa a entregar imediatamente, e quem olhar depois acha que "está agendado". SEMPRE validar com `GET /<adset_id>?fields=start_time` logo após criar/atualizar pra confirmar o valor efetivo.
**Contexto:** Patrick disse "subir 00:01 de hoje" mas eu interpretei a data atual errada e enviei start_time já passado. A Meta aceitou silenciosamente e ativou na hora; só descobri ao consultar o adset. Pra evitar: comparar o `start_time` retornado com `datetime.now()` no timezone da conta.

### 2026-06-01 — Campos obrigatórios novos da API (v21) ao criar campanha/adset
**Regra:** A API Marketing v21 (mai/2026) passou a exigir campos que antes eram opcionais. SEMPRE incluir nos POSTs:
- **Campanha (`/{ACC}/campaigns`):** `is_adset_budget_sharing_enabled` (`true`/`false`) — obrigatório quando NÃO se usa budget na campanha (CBO). Sem ele: erro 4834011.
- **Adset (`/{ACC}/adsets`):** dentro de `targeting`, adicionar `targeting_automation: {advantage_audience: 0 ou 1}`. 0 = mantém targeting estrito; 1 = deixa Meta expandir. Sem ele: erro 1870227.
**Contexto:** Ao criar a campanha de Namorados da Lumina, dois erros sequenciais por esses campos novos. Antes eu criava sem eles e funcionava — não funciona mais.

### 2026-06-01 — Placements descontinuados (não passar manualmente)
**Regra:** A API v21 rejeita placements antigos. Evitar passar manualmente:
- `instagram_positions: ["search"]` — não existe (erro 1815508). Search só existe em `facebook_positions`.
- `facebook_positions: ["video_feeds"]` — descontinuado (erro 2490562). Era "feeds de vídeos do Facebook".
**Alternativa preferida (CTWA):** NÃO passar `publisher_platforms` nem `*_positions` no targeting → ativa **Advantage+ Placements automático**, que é o que vinha vencendo o leilão (Status do WhatsApp dominou aniversário com 59% das conversas). Só forçar placement manual se for excluir algum por estratégia clara.

### 2026-06-01 — Receita completa pra subir campanha CTWA (parâmetros validados v21)
**Regra:** Templates abaixo funcionam end-to-end. Reusar sempre.

**Pré-flight obrigatório (antes de qualquer POST):**
1. Ler `contas.yaml` pra pegar: `meta.conta_anuncio`, `meta.pagina_facebook`, `meta.instagram_id`, `meta.pixel_id`.
2. Confirmar `META_ADS_TOKEN` está no `.env` da raiz.
3. GET `act_<ID>?fields=timezone_offset_hours_utc` pra calcular offset (regra do 00:01 acima).

**Campanha:**
```json
{
  "name": "<slug>",
  "objective": "OUTCOME_ENGAGEMENT",
  "status": "ACTIVE",
  "special_ad_categories": "[]",
  "buying_type": "AUCTION",
  "is_adset_budget_sharing_enabled": "false"
}
```

**Adset:**
```json
{
  "name": "<slug>",
  "campaign_id": "<id>",
  "status": "ACTIVE",
  "daily_budget": 1500,
  "billing_event": "IMPRESSIONS",
  "optimization_goal": "CONVERSATIONS",
  "destination_type": "WHATSAPP",
  "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
  "start_time": "<YYYY-MM-DD>T00:01:00<offset_DA_CONTA>",
  "promoted_object": {"page_id": "<page_id>"},
  "targeting": {
    "geo_locations": {"countries": ["BR"]},
    "genders": [2],
    "age_min": 22,
    "age_max": 34,
    "targeting_automation": {"advantage_audience": 0}
  }
}
```

**Creative (CTWA):**
```json
{
  "name": "creative-<slug>",
  "object_story_spec": {
    "page_id": "<page_id>",
    "instagram_user_id": "<ig_id>",
    "link_data": {
      "image_hash": "<hash do adimages>",
      "link": "https://api.whatsapp.com/send",
      "name": "<headline curta>",
      "message": "<body do post>",
      "call_to_action": {"type":"WHATSAPP_MESSAGE","value":{"app_destination":"WHATSAPP"}}
    }
  }
}
```

**Ad (pixel obrigatório):**
```json
{
  "name": "<nome>",
  "adset_id": "<id>",
  "creative": {"creative_id": "<id>"},
  "status": "ACTIVE",
  "tracking_specs": [{"action.type":["offsite_conversion"],"fb_pixel":["<PIXEL_ID>"]}]
}
```

**Ordem de execução:** (1) upload imagens via `/adimages` → guardar hashes; (2) POST campanha; (3) POST adset com 00:01 do timezone da conta; (4) loop por criativo: POST `/adcreatives` → POST `/ads` com tracking_specs do pixel; (5) GET adset confirmando `start_time` efetivo (anti-sobrescrita silenciosa); (6) reportar IDs gerados em arquivo `<campanha>_ids.json` na pasta da campanha.

### 2026-06-05 — Auditoria de purchases via API: SEMPRE puxar os 4 campos juntos
**Regra:** Ao auditar resultado de campanha com purchases (qualquer cliente CTWA com pixel), SEMPRE puxar **os 4 campos abaixo na mesma chamada**, pra evitar leitura parcial induzindo a erro:
1. `actions` → **quantidade** de purchases (ex: `purchase = 2`)
2. `action_values` → **receita atribuída em R$** (ex: `purchase = 30.00`)
3. `cost_per_action_type` → **custo de mídia por purchase** (ex: `purchase = 28.29` = R$ 56,57 ÷ 2)
4. `purchase_roas` → **ROAS atribuído pelo Meta** (ex: `omni_purchase = 0.53`)

**NUNCA confundir:**
- `cost_per_action_type.purchase` (custo de MÍDIA) ≠ `action_values.purchase` (VALOR da venda)
- "R$ 28,29 por purchase" no relatório significa "gastei R$ 28,29 em mídia pra gerar cada conversão", NÃO "o cliente pagou R$ 28,29 por venda".

**Exemplo concreto (Namorados Lumina 02-05/06):**
- spend: R$ 56,57 · purchases: 2 · action_values.purchase: R$ 30,00 · cost_per_action.purchase: R$ 28,29 · ROAS: 0,53
- Leitura correta: "Gastei R$ 56,57, atribuíram 2 vendas totalizando R$ 30 de receita; cada conversão custou R$ 28,29 em mídia; ROAS atribuído 0,53."
- Leitura ERRADA (que cometi): "2 vendas a R$ 28,29 cada" (mistura custo de mídia com valor de venda).

**Comando padrão:**
```bash
insights.py campaign --id <CID> --date-preset maximum \
  --fields "spend,actions,action_values,cost_per_action_type,purchase_roas"
```

**Contexto:** Em 05/06, ao analisar Namorados da Lumina, puxei só `actions` e `cost_per_action_type`. Patrick perguntou pelo valor da venda, eu interpretei `28.29` como valor unitário da venda (errado — era custo de mídia). Só depois puxei `action_values` e vi R$ 30 totais. Custou 2 iterações desnecessárias com o Patrick.

### 2026-06-06 — Aumento de orçamento: teto seguro é +20%, NÃO +30%
**Regra:** Ao subir orçamento de adset em campanha que já saiu do learning, manter aumento **≤20% por vez**. Acima disso, alto risco de resetar o aprendizado da Meta.
**Convenções comuns (errado e certo):**
- ❌ "Pode até +30%" — material brasileiro (incluindo Sobral) cita 30% mas a Meta nunca documentou. Comunidade testou e convergiu pra 20%.
- ✅ **≤20%:** muito seguro, raramente dispara reset.
- ⚠ **20–30%:** zona cinzenta, PODE disparar reset.
- 🔴 **>30%:** alto risco de reset.

**Como aplicar:** sempre calcular `novo_budget = budget_atual * 1.20` (arredonda pra baixo). Esperar **3-4 dias** entre aumentos pra avaliar efeito.

**Contexto:** Em 06/06 sugeri ao Patrick subir Namorados Lumina de R$15 → R$20/dia (+33%) sem checar. Patrick puxou: "mais de X% não reseta o aprendizado?". Corrigi pra +20% (R$18/dia). Erro de descuido — não validei o número antes de propor.

**Frase pra usar:** "Recomendo +20% (R$X → R$Y). 20% é o teto seguro — acima disso há risco de resetar learning."

### 2026-06-05 — Lumina: SEMPRE configurar Quick Replies (Perguntas Frequentes) ao subir campanha
**Regra (Lumina específica):** Toda campanha CTWA nova da Lumina (act_1399522635268024) deve ter, **antes de entrar em veiculação**, "Perguntas frequentes" configurada na mensagem de boas-vindas do anúncio com os 3 botões abaixo. Faz qualificação de tema antes da Bia receber o lead.

**Configuração padrão:**
- **Saudação:** "Olá! Bem-vindo(a) ao Estúdio Lumina. Como posso te ajudar?"
- **Pergunta 1:** "Quero saber sobre o ensaio de aniversário"
- **Pergunta 2:** "Quero saber sobre o ensaio de Dia dos Namorados"
- **Pergunta 3:** "Tenho outra dúvida"
- **Resposta automática:** deixar VAZIA nas 3 (Bia precisa do controle total do fluxo)
- **Nome do modelo:** `Lumina - Qualifica tema (MM/AAAA)`

**Como configurar:** SÓ via UI do Gerenciador de Anúncios da Meta. Editar anúncio → "Mensagem de boas-vindas" → "Editar modelo" → seleciona **"Perguntas frequentes"** (não "Mensagem pronta"). API rejeita atualização de `page_welcome_message` em creative existente (erro 1815573 — só permite atualizar `name`/`status`/`adlabels`).

**Por que importa:** o lead toca no botão e a string vai direto pra Bia como primeira mensagem. Ela recebe `tema=aniversario` ou `tema=namorados` qualificado sem precisar perguntar — pula direto pra cotação. Reduz atrito da primeira interação e canaliza pro fluxo correto.

**Contexto:** Descoberto em 05/06 ao analisar anúncio do Well (concorrente) que usava o mesmo padrão visual. Tentamos via API, falhou (erro 1815573); resolvemos pela UI. Configuração se aplica por anúncio individual — replicar manualmente em todos os ads CTWA da Lumina (atualmente: 5 da Namorados + ads ativos da aniversário). Quando criar ad novo, já subir com esse modelo aplicado.

**Limitação aceita:** botões reais (chips clicáveis dentro do balão da Meta, estilo Well) NÃO estão disponíveis na conta da Lumina via UI nem API atualmente. "Perguntas frequentes" é o substituto funcional disponível — visualmente diferente, mesma mecânica de qualificação.
