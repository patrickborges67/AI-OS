# Histórico de Otimizações - EssentialWeb

> Última atualização: 2026-05-14
> Total de registros: 1
> Confirmados: 0 | Refutados: 0 | Pendentes: 0 | Diagnósticos: 1

---

### 2026-05-14 - Diagnóstico inicial Meta Ads + GA4

**Tipo:** Diagnóstico

**Ação:** Rodado diagnóstico da conta `essentialweb` usando Meta Ads (`act_1306638014333858`) e GA4 (`property_id: 533408886`). Google Ads foi ignorado neste diagnóstico porque o usuário informou que ainda não há dados úteis lá.

**Motivo:** Criar uma linha de base para aquisição paga e mensuração antes de retomar campanhas.

**Hipótese:** Antes de escalar tráfego pago, a conta precisa corrigir mensuração de conversão e ativar uma campanha simples; com isso, próximos diagnósticos passam a ter CPL/CPA real para decisão.

**Métricas antes:**
- Período analisado: 2026-04-15 a 2026-05-14
- Health Score operacional: 58/100, nota D
- Meta Ads: 0 campanhas com entrega nos últimos 30 dias
- Meta Ads: 0 campanhas com entrega nos últimos 90 dias
- Meta Ads: todas as campanhas listadas estavam pausadas
- GA4 sessões: 57
- GA4 usuários: 15
- GA4 visualizações: 128
- GA4 taxa de rejeição geral: 50,9%
- GA4 tempo médio de sessão: 238s
- GA4 conversões marcadas: 0
- GA4 evento `generate_lead`: 1 evento, mas 0 conversões
- GA4 `google / cpc`: 4 sessões, 100% de rejeição, 1,35s de duração média
- GA4 `tagassistant.google.com / referral`: 25 sessões, 64% de rejeição
- GA4 `/`: 18 sessões, 38,9% de rejeição, 287,6s de duração média
- GA4 `/chatbots`: 18 sessões, 44,4% de rejeição, 90,7s de duração média

**Alertas registrados:**
- Crítico: não há mídia ativa no Meta Ads para otimizar.
- Crítico: `generate_lead` existe, mas não está marcado como conversão no GA4.
- Crítico: tráfego `google / cpc` chegou com rejeição crítica e sem campanha identificada.
- Atenção: tráfego de `tagassistant.google.com` está poluindo a leitura do GA4.
- Bom: páginas `/` e `/chatbots` mostram engajamento aceitável pelos benchmarks BR.

**Recomendações derivadas:**
- Marcar `generate_lead` como conversão no GA4.
- Filtrar tráfego interno/testes, principalmente `tagassistant.google.com`.
- Ativar campanha Meta simples com objetivo de lead ou WhatsApp quando a captação paga voltar.
- Revisar origem `google / cpc` e UTMs antes de considerar esse tráfego em diagnóstico.
- Rodar novo diagnóstico depois de 7 dias com campanha ativa ou pelo menos 100 cliques.

**Status:** Diagnóstico registrado. Ações ainda não executadas.

---

### 2026-05-14 - Leitura de Pixel/CAPI via API Meta

**Tipo:** Diagnóstico técnico

**Ação:** Adicionado suporte de leitura de Pixel/CAPI na skill `meta-ads-ratos` e consultados os pixels usados pelo site institucional (`957417780098573`) e pela página `/chatbots` (`872873935769143`).

**Motivo:** Validar pela API da Meta se os eventos do Pixel estão chegando e complementar o diagnóstico de mensuração.

**Hipótese:** O site já envia eventos de Pixel, mas a qualidade de leitura pela API depende das permissões do token e nem todos os dados do Events Manager ficam disponíveis.

**Métricas antes:**
- Pixel padrão `957417780098573`, período 2026-04-15 a 2026-05-14: 36 `PageView`, 1 `Lead`, 1 `chatbots_view_plans`
- Pixel `/chatbots` `872873935769143`, período 2026-04-15 a 2026-05-14: 9 `PageView`, 5 `Lead`, 4 `Custom`, 1 `test_event_code`
- Pixel padrão, consulta recente sem intervalo: 1 `PageView` em 2026-05-13 22:00
- Pixel `/chatbots`, consulta recente sem intervalo: sem eventos retornados
- Conversões personalizadas da conta: nenhuma retornada
- Detalhes/listagem de pixels: bloqueados pela Meta com erro `(#200)` pedindo permissão `ads_management` ou `ads_read`

**Alertas registrados:**
- Atenção: a API confirma eventos de Pixel chegando, incluindo `Lead`.
- Atenção: a leitura de detalhes do Pixel/dataset está limitada por permissão do token ou vínculo do owner da conta.
- Atenção: o evento `test_event_code` apareceu como evento no Pixel `/chatbots`, indicando tráfego de teste no período.
- Atenção: não há conversões personalizadas retornadas pela API.

**Recomendações derivadas:**
- Validar no Events Manager se o token/app tem acesso correto aos datasets/pixels.
- Conferir se os pixels `957417780098573` e `872873935769143` são os datasets definitivos para campanhas.
- Remover/ignorar eventos de teste nos relatórios de performance.
- Em diagnóstico futuro, cruzar GA4 `generate_lead` com Pixel `Lead` para detectar divergência de mensuração.

**Status:** Diagnóstico técnico registrado. Ações de permissão/configuração ainda não executadas.

---
