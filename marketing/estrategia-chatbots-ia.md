# Estrategia de Marketing - Atendimento Comercial com IA

## Objetivo

Atrair clientes para a oferta de atendimento e qualificacao comercial com IA no WhatsApp usando a landing `/chatbots` como hub de conversao e testando nichos por criativos, campanhas e UTMs antes de criar landings nichadas.

A oferta de entrada e o agente de IA para WhatsApp, mas a promessa comercial nao deve ficar limitada a "chatbot". O foco e resolver perda de leads, demora no atendimento, falta de qualificacao, follow-up ruim e ausencia de registro no CRM.

## Decisao principal

Usar uma estrategia hibrida:

- Conteudo e criativos de topo/meio de funil para educar e criar demanda.
- Campanhas diretas para diagnostico/reuniao para capturar quem ja sente a dor.
- Remarketing para quem interagiu com conteudo ou visitou `/chatbots`.

Nao comecar com campanha ampla apenas para ganhar seguidores. Tambem nao depender apenas de anuncio direto de venda, porque "agente de IA" ainda pode soar abstrato para parte do mercado.

Usar o agente de IA como produto de entrada, nao como limite da empresa. A EssentialWeb continua podendo vender automacoes, sites, sistemas, integracoes e CRM quando esses elementos forem necessarios para resolver o problema completo.

## Posicionamento

Vender resultado comercial, nao "IA" de forma generica.

Mensagem base:

> Atendimento comercial com IA no WhatsApp para responder rapido, qualificar leads, registrar no CRM e acionar o humano na hora certa.

Mensagem curta para criativos:

> Pare de perder lead no WhatsApp por demora, desorganizacao e falta de follow-up.

Como explicar a EssentialWeb:

> A EssentialWeb melhora atendimento, vendas e processos usando IA, automacao e sistemas. O agente de IA para WhatsApp e a porta de entrada porque a dor e visivel e facil de medir.

Dores centrais:

- Demora no atendimento.
- Lead sem qualificacao.
- Perguntas repetidas travando equipe.
- Falta de follow-up.
- Trafego pago gerando lead que o WhatsApp nao converte.
- Falta de registro e visibilidade no CRM.

Diretriz de copy:

- Evitar vender "chatbot", "robo" ou "IA generica" como fim em si.
- Preferir vender atendimento rapido, qualificacao, CRM, follow-up, agenda, vendedor com contexto e gestor com visibilidade.
- Frase central: a promessa nao e "ter IA"; e parar de perder vendas por demora, esquecimento e desorganizacao no WhatsApp.

## Arquitetura comercial da oferta

Organizar a venda em camadas:

1. Oferta de entrada: atendimento comercial com IA no WhatsApp.
2. Promessa: parar de perder leads por demora, desorganizacao e falta de follow-up.
3. Implementacao: agente de IA, automacoes, CRM, integracoes, landing page e dashboards quando fizer sentido.
4. Expansao: depois do primeiro fluxo validado, vender melhorias no funil comercial, sistemas internos e automacoes de operacao.

Essa arquitetura evita parecer que a EssentialWeb "faz de tudo" e, ao mesmo tempo, nao limita a empresa a vender apenas chatbot.

## Oferta de entrada

Usar o diagnostico como porta de entrada:

> Diagnostico gratuito: quantos leads seu WhatsApp esta perdendo?

Forma mais clara da oferta:

> Diagnostico gratuito do WhatsApp: analise de tempo de resposta, follow-up, origem dos leads, registro no CRM e pontos onde oportunidades estao sendo perdidas.

Fluxo esperado:

1. Lead chega por anuncio, conteudo, outbound ou remarketing.
2. Vai para `/chatbots` com UTM.
3. Preenche formulario curto com nome, telefone e email para match posterior.
4. O endpoint do n8nCRM registra origem, campanha, criativo, dados do lead e identificadores de tracking.
5. Lead continua no WhatsApp.
6. O CRM da operacao no WhatsApp faz o match do lead e concentra a conversa.
7. Agente de IA qualifica o lead no WhatsApp, preenche resumo da qualificacao, nivel de ICP, temperatura e proxima acao.
8. Lead quente recebe convite para diagnostico/agendamento.
9. Lead morno entra em follow-up consultivo.
10. Eventos de formulario, conversa, qualificacao e agendamento alimentam o Server Side CAPI quando houver match suficiente.
11. Diagnostico vira proposta de implantacao + mensalidade.

O diagnostico deve avaliar:

- Tempo medio de resposta.
- Volume de perguntas repetidas.
- Como o lead e qualificado hoje.
- Se existe registro em CRM ou planilha.
- Como o follow-up e feito.
- Onde o atendimento manual perde oportunidade.
- Quanto do trafego pago pode estar sendo desperdicado no WhatsApp.

## Operacao de captura, qualificacao e tracking

A captura atual ja acontece por formulario na landing `/chatbots` e por WhatsApp. Por isso, o formulario nao deve tentar fazer toda a qualificacao. Ele deve reduzir friccao e garantir match para tracking, enquanto a qualificacao principal acontece no WhatsApp.

### Papel do formulario

Manter o formulario curto e orientado a identificacao:

- Nome.
- Telefone.
- Email.
- Campo opcional de contexto, apenas se nao reduzir conversao: principal desafio no atendimento/comercial.

Estado atual em `projetos/essential-web/src/pages/Chatbots.tsx`:

- O formulario da landing `/chatbots` ja captura nome, email e telefone.
- O envio gera `eventId`, `anonymousId`, `submittedAt`, UTMs, `fbclid`, `gclid`, `fbp`, `fbc`, URL da pagina, referrer e user agent.
- O envio usa Turnstile quando `VITE_TURNSTILE_SITE_KEY` esta configurado.
- O lead e enviado para o endpoint definido em `VITE_CHATBOTS_LEAD_FORM_ENDPOINT`.
- Depois do envio, o lead e direcionado para WhatsApp com nome, email, telefone e plano de interesse.

Recomendacao atual: nao aumentar o formulario agora. O unico campo extra que pode ser testado, se houver muito lead sem contexto, e uma pergunta simples de desafio principal. Se a taxa de envio cair, remover esse campo e manter toda qualificacao no WhatsApp.

Dados tecnicos que devem ser registrados junto com o lead:

- `lead_id` interno, quando possivel.
- Telefone normalizado em E.164.
- Email normalizado.
- `utm_source`.
- `utm_medium`.
- `utm_campaign`.
- `utm_content`.
- `utm_term`.
- `fbclid` e/ou `gclid`, quando disponiveis.
- `fbp` e `fbc`, quando disponiveis.
- `event_source_url`.
- `landing_page`.
- `client_ip_address`, se a politica de privacidade permitir.
- `client_user_agent`, se a politica de privacidade permitir.
- Timestamp do formulario.

O formulario serve para identificar e rastrear. A conversa no WhatsApp serve para entender dor, urgencia e potencial comercial.

### Papel do CRM no WhatsApp

O CRM deve ser a fonte operacional da qualificacao. Ele precisa guardar campos estruturados e um resumo humano da conversa.

Estado atual em `projetos/n8nCRM`:

- O lead ja possui `nome`, `email`, `phone`, `origem`, `atendimentoVirtual` e `qualificacaoResumo`.
- O kanban usa `LeadCrmState.stage` com as colunas `novo`, `aguardando`, `qualificado`, `proposta` e `fechado`.
- O CRM ja mostra `qualificacaoResumo` no card/listagem do lead.
- O tracking ja possui `LeadTouchpoint`, com UTM, email, telefone, `fbclid`, `fbp`, `fbc`, `gclid`, URL, referrer, IP e user agent.
- O tracking nativo do n8nCRM permite regras por `lead_stage_changed`, ou seja, mudanca de coluna pode disparar evento CAPI.
- O endpoint publico `/public/tracking/web-form` cria ou localiza lead pelo formulario e cria touchpoint `web_form`.
- O endpoint interno `/internal/tracking/signals` permite enviar sinais de mudanca de estagio para o tracking.
- A operacao em n8n pode enviar eventos CAPI de forma mais flexivel do que o gatilho nativo do CRM, usando regras proprias de conversa, qualificacao, agendamento, template, follow-up ou comportamento.

Campos que ja podem ser usados sem mudar schema:

- `stage`: usar como status principal do funil.
- `qualificacaoResumo`: guardar ICP, temperatura, dor, objecao e proxima acao em texto estruturado.
- `origem`: manter fonte principal percebida.
- `LeadTouchpoint`: guardar dados de campanha, UTM e match form -> WhatsApp.

Formato recomendado para `qualificacaoResumo`:

```txt
ICP: alto | Temperatura: quente | Dor: falta de follow-up | Objecao: medo da IA responder errado | Proxima acao: agendar diagnostico.
Resumo: dono de clinica estetica, recebe cerca de 120 leads/mes pelo WhatsApp, tem 3 pessoas no atendimento e ja investe em trafego pago. Usa etiquetas e planilha. Quer reduzir perda por demora e retorno esquecido.
```

Campos recomendados para evolucao futura, se o volume justificar:

- `status_funil`: novo, em_qualificacao, qualificado, agendamento_oferecido, agendado, compareceu, proposta, ganho, perdido ou nutricao.
- `nivel_icp`: icp_alto, icp_medio, icp_baixo ou fora_icp.
- `temperatura`: quente, morno ou frio.
- `dor_principal`: demora_resposta, falta_followup, perda_leads, crm_whatsapp, agenda ou outro.
- `objecao_principal`: preco, medo_ia, tempo, equipe_nao_usa, ja_tentou_crm, sem_prioridade ou sem_objecao.
- `proxima_acao`: agendar, followup, humano, nutrir, proposta ou encerrar.
- `icp_score`: 0 a 100, quando o CRM permitir campo numerico.
- `resumo_qualificacao`: resumo da conversa em linguagem humana.

Recomendacao atual: nao criar campos novos antes de validar a primeira rodada. Usar `stage` + `qualificacaoResumo` + touchpoints para operar. Criar campos separados para ICP, temperatura e proxima acao apenas se o volume crescer ou se relatorios/filtros ficarem ruins.

Usar tags apenas para automacao, filtro e relatorio, se o CRM estiver com gestao de tags ativa na operacao. O resumo da qualificacao deve guardar a nuance da conversa.

Tags minimas recomendadas:

- `icp_alto`, `icp_medio`, `icp_baixo`, `fora_icp`.
- `quente`, `morno`, `frio`.
- `dor_followup`, `dor_demora_resposta`, `dor_perda_leads`, `dor_crm_whatsapp`, `dor_agenda`.
- `usa_trafego`, `tem_equipe`, `quer_agendar`.
- `objecao_preco`, `objecao_ia`, `objecao_tempo`.
- `proxima_acao_agendar`, `proxima_acao_followup`, `proxima_acao_humano`, `proxima_acao_nutrir`.

### Criterios de qualificacao no WhatsApp

Na fase atual, sem base grande de clientes, o ICP nao deve ser usado como portao para recusar conversa. Ele deve priorizar atendimento, adaptar copy, registrar aprendizado e decidir proxima acao.

Perguntas que o agente deve fazer, uma por vez:

1. Hoje voces recebem leads pelo WhatsApp todos os dias?
2. Quantas pessoas atendem ou vendem pelo WhatsApp hoje?
3. O maior problema hoje e demora para responder, falta de follow-up, agenda baguncada ou falta de controle das vendas?
4. Voces ja investem em trafego pago ou recebem leads por Instagram/site?
5. Hoje voces usam CRM, planilha, etiquetas do WhatsApp ou nada estruturado?
6. Se isso fosse resolvido, o maior impacto seria vender mais, reduzir retrabalho ou ter mais controle da equipe?

Regras praticas:

- Lead com dor clara, WhatsApp relevante e urgencia nos proximos 30 dias: oferecer diagnostico/agendamento.
- Lead com dor clara, mas sem urgencia: follow-up consultivo com prova, demo e pergunta de timing.
- Lead sem dor clara: nutricao ou conversa exploratoria curta.
- Lead fora do ICP: registrar aprendizado, responder com utilidade e nao gastar energia comercial longa.

### Eventos para Server Side CAPI

Enviar eventos por etapa para medir qualidade real, nao apenas volume de formulario.

O n8nCRM possui gatilho nativo por mudanca de estagio, mas a operacao em n8n pode disparar eventos de forma mais flexivel. Portanto, nao limitar o desenho de tracking profundo a `lead_stage_changed`. Usar o CRM para estado operacional e usar o n8n para orquestrar eventos quando houver sinais mais precisos.

Eventos conceituais da jornada:

- `Lead` ou `FormSubmit`: formulario enviado.
- `ContactWhatsApp`: lead chegou ou foi identificado no WhatsApp.
- `QualifiedLead`: conversa indicou dor, contexto e potencial minimo.
- `ScheduleOffered`: agenda foi oferecida.
- `ScheduleBooked`: reuniao/diagnostico marcado.
- `ShowedUp`: compareceu.
- `ProposalSent`: proposta enviada.
- `Purchase` ou `ClosedWon`: venda fechada.

Para envio na Meta CAPI, usar preferencialmente eventos padrao da Meta quando eles representarem bem a etapa. A regua definida abaixo traduz a jornada para os eventos que serao enviados.

Regua definida para Meta CAPI na campanha `/chatbots`:

| Evento Meta | Quando enviar | Origem do disparo | Uso na campanha |
|---|---|---|---|
| `Lead` | Formulario enviado em `/chatbots` | Site/n8nCRM via `/public/tracking/web-form` | Evento principal de volume no inicio; mede conversao da landing |
| `Contact` | Lead chegou ou foi identificado no WhatsApp | n8n, logo que a conversa entra e o lead e resolvido/matcheado | Mede quem realmente entrou no canal de venda; ajuda a detectar perda entre form e WhatsApp |
| `CompleteRegistration` | Agente de IA terminou a qualificacao e gerou `qualificacaoResumo` | n8n, imediatamente apos concluir a qualificacao | Mede lead com contexto suficiente; principal indicador de qualidade antes de agendamento |
| `Schedule` | Tool de agendamento criou/confirmou diagnostico ou reuniao | n8n, quando a tool de agenda for chamada com sucesso | Mede oportunidade comercial real; nao enviar apenas por agenda oferecida |
| `Purchase` | Venda fechada | n8n/CRM, apos fechamento comercial | Mede retorno final; usar para analise, nao como otimizacao inicial |

Nao enviar `Schedule` quando a agenda for apenas oferecida. Para agenda oferecida, usar evento interno no n8n/CRM ou anotacao no `qualificacaoResumo`. O evento `Schedule` deve representar agendamento criado ou confirmado.

Uso por fase:

- Fase 1: otimizar campanha para `Lead`; analisar `Contact`, `CompleteRegistration` e `Schedule` como qualidade.
- Fase 2: se `CompleteRegistration` tiver volume consistente, testar otimizacao nele.
- Fase 3: se `Schedule` tiver volume suficiente, testar campanha ou remarketing orientado a agendamento.
- Fase 4: usar `Purchase` para retorno, qualidade comercial e decisao de escala.

Fontes possiveis de disparo:

- Mudanca de coluna no CRM, quando o evento representar uma etapa clara do funil.
- Resposta do agente de IA indicando lead qualificado.
- Campo `qualificacaoResumo` preenchido com ICP e proxima acao.
- Lead receber convite de agenda.
- Agendamento criado ou confirmado.
- Template de follow-up enviado.
- Lead responder depois de follow-up.
- Lead ser marcado manualmente como oportunidade real.
- Proposta enviada.
- Venda fechada.

Na fase inicial, otimizar campanha para evento com volume suficiente e usar eventos profundos para leitura qualitativa. Nao migrar otimizacao para `CompleteRegistration` ou `Schedule` antes de haver volume minimo consistente.

Para CAPI, priorizar qualidade de match:

- Email com hash.
- Telefone com hash.
- Nome e sobrenome, quando disponiveis.
- `fbp`.
- `fbc`.
- IP e user agent, quando permitidos.
- `external_id` ou `lead_id`.
- `event_id` para deduplicacao quando houver evento browser + server.

### Teste dos eventos na Meta

Antes de rodar campanha real, validar os eventos em tres camadas.

1. Test Events sem campanha:
   - Abrir Events Manager da Meta.
   - Entrar no pixel/dataset usado em `/chatbots`.
   - Abrir a aba Test Events.
   - Copiar o `test_event_code`.
   - Configurar temporariamente esse codigo no destino CAPI do n8nCRM ou no envio do n8n.
   - Disparar eventos controlados: `Lead`, `Contact`, `CompleteRegistration` e `Schedule`.
   - Confirmar se chegam como eventos server-side, com `event_id`, telefone/email hasheados, `fbp`, `fbc`, IP, user agent e `external_id` quando disponiveis.

2. Teste real sem campanha:
   - Remover ou desativar o `test_event_code`.
   - Abrir `/chatbots` manualmente.
   - Preencher o formulario.
   - Entrar no WhatsApp.
   - Deixar o agente concluir a qualificacao e gerar o `qualificacaoResumo`.
   - Chamar a tool de agendamento em um teste controlado.
   - Conferir no Events Manager se `Lead`, `Contact`, `CompleteRegistration` e `Schedule` aparecem no historico real.

3. Teste com campanha pequena:
   - Subir campanha com verba baixa apenas depois dos eventos tecnicos estarem chegando.
   - Validar atribuicao, qualidade de match, deduplicacao e progressao do funil por UTM/criativo.
   - So considerar otimizacao para evento profundo depois de volume consistente.

## Papel da landing `/chatbots`

A pagina `/chatbots` e o hub de conversao da oferta.

Ela deve receber:

- Trafego de anuncios.
- Retargeting.
- Link na bio.
- Conteudos que ja aqueceram a dor.
- Outbound personalizado.

Nao criar landings nichadas antes de validar resposta por nicho. Primeiro testar campanhas nichadas levando para a mesma landing geral. Depois, criar `/chatbots/clinicas`, `/chatbots/imobiliarias` ou outra variacao apenas para o nicho vencedor.

## ICP da campanha

Persona de comunicacao reutilizavel: `marketing/persona-comunicacao-mariana-almeida.md`.

O ICP principal sao donos, gestores comerciais ou responsaveis por atendimento em pequenas e medias empresas de servico, com ticket medio ou alto, que recebem leads pelo WhatsApp e perdem oportunidades por demora, falta de qualificacao, ausencia de follow-up e falta de visibilidade do funil.

Eles nao querem apenas um chatbot. Querem vender mais com a mesma equipe, organizar atendimento e parar de desperdicar leads vindos de anuncio, indicacao, Instagram ou site.

Perfil operacional:

- Ja recebe leads pelo WhatsApp, Instagram, site, indicacao ou trafego pago.
- Tem alguem responsavel por atendimento, vendas ou agenda.
- Sente que leads somem entre a primeira mensagem, proposta, agendamento e follow-up.
- Precisa de resposta rapida, qualificacao, registro e acompanhamento.
- Tem margem suficiente para justificar implantacao e mensalidade.

Nao-ICP:

- Empresa sem volume minimo de leads.
- Negocio que quer apenas "chatbot barato".
- Operacao sem responsavel claro por atendimento ou vendas.
- Empresa que nao aceita ajustar processo comercial.
- Ticket baixo demais para justificar implantacao e mensalidade.
- Cliente que quer automacao 100% sem supervisao humana.

## Nichos iniciais para teste

1. Clinicas e estetica
   - Dores: recepcao sobrecarregada, perguntas repetidas, agendamento, no-show, reagendamento.

2. Imobiliarias e corretores
   - Dores: lead frio, demora no atendimento, falta de qualificacao, corretor sem contexto.

3. Servicos locais com orcamento
   - Exemplos: energia solar, assistencia tecnica, reformas, seguros.
   - Dores: orcamento sem follow-up, lead que chama e some, trafego desperdicado.

Manter educacao, agencias, consultorias B2B e outros servicos como banco de segunda rodada. No inicio, nao abrir muitos submercados ao mesmo tempo para nao diluir verba, criativos e leitura.

## Linguagem da persona

Usar a persona Mariana Almeida como filtro de comunicacao.

Priorizar linguagem de:

- Controle comercial.
- Lead perdido.
- Equipe que esquece retorno.
- WhatsApp baguncado.
- Dinheiro de anuncio vazando.
- Follow-up manual.
- CRM que ninguem preenche.
- Venda perdida por demora.

Evitar linguagem de:

- IA revolucionaria.
- Chatbot inteligente como promessa principal.
- Automacao generica.
- Transformacao digital abstrata.
- Futuro da tecnologia.
- Promessa milagrosa de venda automatica.

## Canais

- Meta Ads: canal inicial principal para testar criativos, dores e nichos.
- Organico: Instagram/LinkedIn com carrosseis, videos curtos e bastidores.
- Outbound: abordagem personalizada com diagnostico simples.
- Google Search: testar depois para termos com intencao, como "chatbot whatsapp", "automacao whatsapp" e "atendimento whatsapp ia".
- LinkedIn Ads: deixar para etapa posterior, caso o ticket e o nicho justifiquem custo maior.

## Estrategia de social media

Social media deve rodar junto com trafego pago, mas com funcao diferente.

No inicio, nao medir social principalmente por seguidores. Como a base atual e pequena, a funcao principal do organico e:

- Dar lastro para quem pesquisar a EssentialWeb depois de ver anuncio.
- Gerar confianca antes da reuniao.
- Criar criativos que depois podem virar anuncio.
- Treinar mensagem comercial e descobrir quais dores geram resposta.
- Mostrar dominio sobre o problema, nao so sobre a ferramenta.
- Alimentar remarketing com conteudo.

Seguidores qualificados podem virar objetivo tatico, mas nao como meta principal. A campanha de crescimento de audiencia so entra depois que o perfil estiver pronto para converter visita em confianca, direct, WhatsApp ou clique para `/chatbots`.

### Perfil pronto para receber trafego

Antes de impulsionar conteudo ou rodar campanha para seguidores qualificados, revisar:

- Foto e nome do perfil comunicando pessoa/marca com clareza.
- Titulo buscavel conectado a IA, automacao, WhatsApp, CRM ou atendimento comercial.
- Bio dizendo quem e a EssentialWeb, qual problema resolve e qual proxima acao.
- Link levando para acao objetiva: `/chatbots`, WhatsApp ou diagnostico.
- Destaques minimos: `Agente IA`, `Como funciona`, `Diagnostico`, `Provas`.
- 3 posts fixados: oferta, demo do fluxo e dor principal do WhatsApp.
- Primeiros posts reforcando dor, demonstracao, autoridade, prova e bastidor.

### Papel por canal

- **Instagram:** principal canal social para nichos locais, clinicas, estetica, imobiliarias e servicos.
- **LinkedIn:** canal de autoridade B2B e decisores; menor volume, mas bom para demonstrar pensamento tecnico/comercial.
- **YouTube Shorts:** reaproveitamento de videos curtos, sem prioridade operacional inicial.
- **TikTok:** nao priorizar agora, a menos que exista disposicao para testar volume maior de video e linguagem mais aberta.

### Pilares de conteudo

Usar RETINA como grade de equilibrio editorial para nao publicar apenas conteudo educativo ou apenas oferta:

| Pilar RETINA | Aplicacao na EssentialWeb |
|---|---|
| Relacionamento | Bastidores de projeto, decisao tecnica traduzida, rotina solo e aprendizados reais. |
| Engajamento | Perguntas sobre WhatsApp baguncado, follow-up esquecido, lead sem resposta e CRM abandonado. |
| Transformacao | Passos praticos para organizar atendimento, qualificar lead e criar follow-up. |
| Interacao 1:1 | Enquetes, caixas de pergunta e posts que puxam diagnostico pelo direct/WhatsApp. |
| Niveis de consciencia | Sintomas da perda de lead, comparativos, demos e produto em uso. |
| Autoridade | Casos, provas tecnicas, arquitetura do fluxo, opinioes sobre IA, CRM e automacao. |

Os pilares abaixo continuam sendo a traducao pratica da oferta para a persona Mariana Almeida.

1. Dor comercial
   - Lead perdido por demora.
   - WhatsApp sem processo.
   - Follow-up ruim.
   - Trafego pago desperdicado por atendimento lento.

2. Demonstracao
   - Video de tela com conversa simulada.
   - Antes/depois do atendimento manual vs IA.
   - Fluxo visual: anuncio -> WhatsApp -> qualificacao -> CRM -> humano -> follow-up.
   - Prints com dados sensiveis ocultos.

3. Autoridade tecnica traduzida
   - Quando o bot deve transferir para humano.
   - Por que chatbot ruim irrita cliente.
   - O que precisa estar pronto antes de colocar IA no WhatsApp.
   - Como conectar WhatsApp, CRM e follow-up sem virar gambiarra.

4. Oferta / diagnostico
   - Chamada para diagnostico gratuito.
   - Convite para analisar onde o WhatsApp esta perdendo lead.
   - CTA para comentar, chamar no direct ou acessar `/chatbots`.

### Frequencia realista

Para operacao solo:

- 3 posts por semana.
- 2 videos curtos por semana.
- 1 carrossel por semana.
- Stories quase diarios quando houver bastidor real.
- 1 post fixado explicando a oferta de agente de IA.
- Destaques no Instagram: `Agente IA`, `Como funciona`, `Diagnostico`.

Nao postar todo dia se isso reduzir qualidade. Melhor consistencia util do que volume generico.

### Roteiro semanal

- Segunda: dor comercial.
- Terca: bastidor ou demonstracao.
- Quarta: autoridade tecnica traduzida.
- Quinta: nicho especifico.
- Sexta: oferta leve para diagnostico.

### O que evitar

- Conteudo generico sobre "o futuro da IA".
- Tentar parecer influencer de tecnologia.
- Trend sem relacao com o publico.
- Medir sucesso por seguidores no primeiro mes.
- Produzir apenas carrossel. Demo em video tende a vender melhor esse tipo de servico.
- Vender "chatbot" como ferramenta isolada, sem conectar com lead, CRM, humano e follow-up.

### Metricas de social no inicio

- Cliques para `/chatbots`.
- DMs recebidas.
- Respostas em stories.
- Pessoas que chegam na reuniao dizendo que viram um post.
- Criativos organicos que merecem virar anuncio.
- Temas que geram comentario, pergunta ou pedido de diagnostico.

Seguidores sao metrica secundaria nesta fase.

## Calendario organico Instagram/Facebook - 14 dias

Este calendario roda em paralelo com o trafego pago. A funcao do organico nao e depender de alcance, mas dar lastro para quem pesquisar a EssentialWeb, aquecer audiencia de remarketing, testar mensagens e criar prova de dominio sobre a dor.

Pode repetir tema do trafego pago quando fizer sentido. A diferenca e o tratamento: no pago, o criativo precisa capturar atencao rapido; no organico, o post pode explicar melhor o problema, mostrar bastidor e criar confianca.

| Dia | Canal | Formato | Tema | Angulo | CTA |
|---|---|---|---|---|---|
| 1 | Instagram + Facebook | Carrossel | O lead nao esfria por falta de interesse | Demora no WhatsApp mata intencao de compra | "Chame no direct para avaliar seu atendimento" |
| 2 | Instagram Reels + Facebook Reels | Video curto | Demo do fluxo com IA | Lead chama, IA qualifica, humano assume com contexto | "Veja a landing em `/chatbots`" |
| 3 | Stories | Bastidor | Como mapear um atendimento antes de automatizar | Antes de IA, precisa entender perguntas, etapas e gargalos | Enquete: "Seu WhatsApp tem follow-up?" |
| 4 | Instagram + Facebook | Post estatico | Seu anuncio gera lead. Seu WhatsApp perde a venda. | Trafego pago sem atendimento rapido vira desperdicio | "Peca um diagnostico" |
| 5 | Instagram + Facebook | Carrossel | 5 perguntas que a IA poderia filtrar em clinicas | Convenio, horario, preco, endereco e agendamento | "Salve para revisar seu atendimento" |
| 6 | Stories | Bastidor/prova | Print ou mockup do fluxo WhatsApp -> CRM | Mostrar registro, origem e resumo do lead | Caixa de pergunta: "Quer ver esse fluxo no seu nicho?" |
| 7 | Instagram + Facebook | Post de autoridade | Por que chatbot ruim irrita cliente | IA precisa saber quando responder e quando transferir | "Comente 'fluxo' para receber um exemplo" |
| 8 | Instagram Reels + Facebook Reels | Video curto | Antes/depois do atendimento manual vs IA | Comparar lead perdido com lead qualificado e registrado | "Chame para diagnostico gratuito" |
| 9 | Instagram + Facebook | Post estatico | Quem responde primeiro parece mais preparado | Velocidade vira percepcao de profissionalismo | "Envie para quem cuida do atendimento" |
| 10 | Instagram + Facebook | Carrossel | Orcamento sem follow-up vira lead morto | A IA retoma contato sem depender da memoria do vendedor | "Peca uma analise do seu follow-up" |
| 11 | Stories | Bastidor comercial | Como seria o diagnostico gratuito | Tempo de resposta, perguntas repetidas, CRM e follow-up | Enquete: "Voce mede tempo de resposta?" |
| 12 | Instagram + Facebook | Post nichado | Agenda cheia nao significa atendimento organizado | No-show, reagendamento e duvidas travam recepcao | "Clinicas: chamem para avaliar o fluxo" |
| 13 | Instagram + Facebook | Carrossel | Lead imobiliario chega sem contexto | IA coleta regiao, faixa de preco, tipo de imovel e urgencia | "Corretores: pecam um exemplo" |
| 14 | Instagram + Facebook | Oferta direta | Diagnostico gratuito do WhatsApp | Encontrar onde o atendimento perde oportunidade | "Chame no WhatsApp ou acesse `/chatbots`" |

### Reaproveitamento recomendado

- Publicar no Facebook os mesmos posts do Instagram, ajustando apenas legenda quando necessario.
- Repostar nos stories os criativos pagos que tiverem melhor resposta.
- Fixar 3 posts no Instagram: oferta, demo do fluxo e dor principal do WhatsApp.
- Transformar comentarios, perguntas e respostas de direct em novos posts.
- Repetir a oferta de diagnostico a cada 7 a 10 dias, mudando o angulo.

### Stories recorrentes

Usar stories quase diarios, mesmo quando nao houver post no feed:

- Bastidor de fluxo, tela, automacao ou CRM.
- Pergunta simples sobre atendimento no WhatsApp.
- Antes/depois de um processo manual.
- Enquete sobre follow-up, tempo de resposta ou organizacao de leads.
- Repost de post novo com comentario curto.

## Estrutura de campanhas

Nao tentar subir todas as campanhas completas no primeiro dia. Como a operacao ainda esta comecando, o plano deve ser faseado:

1. Primeiro validar ativos, rastreamento, diagnostico e primeira leva de criativos.
2. Depois subir conversao/diagnostico e conteudo/aquecimento leve.
3. So ativar remarketing quando houver publico suficiente de visitantes, engajamento, visualizadores de video ou cliques no WhatsApp.

O mapa de campanha fica assim:

- Meta Ads: atencao, relacionamento, seguidores qualificados e conversas 1:1.
- Google Ads: intencao de busca, demanda ativa e captura de quem ja procura solucao.
- Organico: lastro, autoridade, repertorio de criativos e aquecimento.

### Campanha 1 - Conversao / diagnostico

Objetivo: gerar leads qualificados para a landing `/chatbots`.

Criativos:

- Dor direta.
- Oferta de diagnostico.
- Demo curta.
- Nichos especificos.
- Antes/depois do atendimento atual vs atendimento com IA.

### Campanha 2 - Vendas 1:1 / WhatsApp

Objetivo: gerar conversas qualificadas diretamente no WhatsApp quando a oferta for diagnostico, exemplo de fluxo ou analise do atendimento.

Configuracao recomendada:

- Objetivo de campanha: Engajamento.
- Conversao: aplicativo de mensagens, usando WhatsApp como fonte unica no conjunto.
- Estrutura manual para controlar publico, criativo, posicionamento e mensagem inicial.
- Nomeacao: campanha por objetivo/orcamento, conjunto por publico e anuncio por criativo.
- Mensagem inicial com pergunta de qualificacao simples, por exemplo: "Oi, quero entender onde meu WhatsApp esta perdendo leads."

Leitura:

- Medir custo por conversa iniciada, mas decidir por conversa qualificada, dor clara, potencial de ticket e agendamento.
- Nao confundir volume de mensagem com venda. O atendimento precisa conduzir diagnostico, contexto e proxima acao.
- Testar posicionamentos Advantage+ como base. Se a qualidade cair, testar recorte Instagram + WhatsApp como hipotese, sabendo que pode reduzir alcance.

### Campanha 3 - Conteudo / seguidores qualificados

Objetivo: criar familiaridade, crescer audiencia certa e alimentar remarketing.

Usar quando o perfil estiver pronto para receber visita. Selecionar posts com potencial de transformacao, relacionamento, engajamento, consciencia, interacao ou autoridade, seguindo RETINA.

Criativos:

- Carrosseis educativos.
- Videos curtos.
- Bastidores de fluxo.
- Teardowns de atendimento.
- Posts com pergunta clara para direct, comentario ou diagnostico.

Seguidores continuam sendo metrica secundaria. A leitura principal e se o publico certo interage, responde stories, chama no direct, visita `/chatbots` ou entra em remarketing.

### Campanha 4 - Remarketing

Objetivo: converter quem ja viu conteudo, visitou a pagina ou interagiu.

Nao precisa nascer junto com a Rodada 1 se ainda nao houver publico quente. Ativar depois que houver volume minimo de visitantes, engajamento ou visualizadores.

Criativos:

- Demo do agente.
- Processo de implantacao.
- Prova tecnica.
- Diagnostico gratuito.
- Comparativo mostrando onde o lead se perde hoje e como o fluxo resolve.

### Publicos por temperatura

Organizar publicos por proximidade da acao:

- Frio: pessoas sem contato previo com a EssentialWeb. Usar dor, educacao, historia, comparacao e descoberta. Evitar oferta direta demais quando o publico ainda nao entende a solucao.
- Consciente do problema: pessoas que ja sentem demora, follow-up ruim ou WhatsApp baguncado. Usar demonstracao, antes/depois e diagnostico.
- Consciente da solucao: pessoas que ja pesquisaram CRM, automacao, chatbot ou IA. Usar prova, processo, seguranca, integracoes e tratamento de objecoes.
- Quente: engajamento Instagram/Facebook, visitantes da landing e visualizadores de video. Usar conteudo curto, prova e convite claro para diagnostico.
- Superquente: clique no WhatsApp, formulario iniciado, visita recente de 1 a 7 dias ou conversa aberta. Usar oferta direta, prova, urgencia e objecoes.

Se a verba for curta, priorizar menos conjuntos e mais clareza de criativo/oferta. Nao depender apenas da segmentacao automatica sem uma hipotese clara.

### Matriz de ganchos

Criar os anuncios por tipo de gancho para evitar testar seis variacoes da mesma ideia:

| Tipo | Exemplo | Melhor uso |
|---|---|---|
| Pergunta | Sua empresa esta perdendo vendas no WhatsApp e voce nem sabe quantas? | Identificacao rapida em publico frio ou consciente do problema |
| Historia | Um lead pediu orcamento, recebeu resposta tarde e fechou com outro. | Mostrar uma cena reconhecivel do problema |
| Contraintuitivo | O problema nao e falta de lead. E falta de follow-up. | Quebrar a crenca de que mais trafego resolve tudo |
| Segmentado | Clinicas: quantos agendamentos morrem no WhatsApp antes da recepcao responder? | Nichos com dor clara e linguagem especifica |
| Direto | Diagnostico gratuito: descubra onde seu WhatsApp esta perdendo vendas. | Remarketing e fundo de funil |
| Dualidade | WhatsApp como caixa de mensagem vs WhatsApp como funil comercial. | Educacao e comparacao de maturidade |
| Prova/processo | Veja como o lead entra, e qualificado, registrado e retomado automaticamente. | Demonstracao, consideracao e reducao de objecao |

## Demo principal

Criar uma demonstracao curta, reaproveitavel em landing, anuncio, post e reuniao comercial.

Roteiro recomendado:

1. Lead chega pelo anuncio ou site e chama no WhatsApp.
2. IA responde rapidamente sem parecer menu travado.
3. IA identifica necessidade, urgencia, perfil e contexto.
4. Dados entram no CRM ou planilha com origem, campanha e resumo.
5. Humano recebe contexto para assumir a conversa.
6. Follow-up e criado para o lead nao morrer depois do primeiro contato.

Comparativo que precisa aparecer:

- Antes: lead chama, espera, recebe resposta generica, nao entra no CRM e morre sem follow-up.
- Depois: lead recebe resposta rapida, e qualificado, registrado, encaminhado e acompanhado.

## Plano de testes para criativos pagos

Nao trocar criativo todo dia.

O calendario de criativos pagos nao deve ser usado como agenda diaria de troca de anuncios. Em Meta Ads, a melhor leitura inicial vem de baterias pequenas de teste rodando por alguns dias, com UTMs separadas e poucas mudancas durante a rodada.

Trocar ou editar anuncio diariamente cria tres problemas:

- O algoritmo nao tem tempo suficiente para distribuir e aprender.
- Fica dificil saber se o problema era criativo, publico, oferta, landing ou tempo de exposicao.
- A campanha vira uma sequencia de tentativas isoladas, sem criterio de comparacao.

Usar o plano abaixo como fila de producao e rodada de teste, nao como troca diaria.

### Fase 0 - Antes de comecar

Antes de subir trafego pago, deixar prontos os ativos minimos para aprender com a campanha:

- Validar se a landing `/chatbots` esta publicada, rapida e com CTA claro.
- Validar formulario curto, WhatsApp e destino do lead.
- Revisar Instagram antes de trafego: bio, link, destaques, 3 posts fixados e primeiros posts por RETINA.
- Confirmar se o n8nCRM salva UTM, nicho, criativo, campanha, origem, telefone, email, `lead_id` e identificadores de tracking.
- Confirmar se o CRM no WhatsApp consegue fazer match entre formulario e conversa.
- Definir convencao de uso do `stage` atual do CRM: `novo`, `aguardando`, `qualificado`, `proposta` e `fechado`.
- Definir template do `qualificacaoResumo` para registrar ICP, temperatura, dor principal, objecao e proxima acao em texto estruturado.
- Criar tags operacionais minimas apenas se elas forem usadas para automacao, filtro ou relatorio.
- Conferir Pixel/CAPI e a regua de eventos `Lead`, `Contact`, `CompleteRegistration`, `Schedule` e `Purchase`.
- Testar `Lead`, `Contact`, `CompleteRegistration` e `Schedule` no Test Events da Meta antes de campanha real.
- Criar roteiro do diagnostico gratuito com perguntas, criterios de qualificacao, resumo da qualificacao e proximo passo.
- Criar demo simples do fluxo WhatsApp -> qualificacao -> CRM -> humano -> follow-up.
- Preparar 3 posts fixados no Instagram: oferta, demo do fluxo e dor principal do WhatsApp.
- Preparar mensagem inicial para campanhas de WhatsApp com pergunta simples de qualificacao e promessa do diagnostico.
- Fazer swipe file com 10 a 20 referencias antes da producao.
- Produzir os 6 criativos base da Rodada 1.
- Fazer outbound para pelo menos 30 empresas usando os mesmos ganchos dos criativos.

Se algum item critico de tracking, destino do lead ou diagnostico estiver ausente, nao subir campanha ainda.

### Swipe file e referencias

Antes de produzir os criativos da rodada, buscar referencias e registrar ideias de gancho, formato, prova, CTA e estrutura visual.

Fontes recomendadas:

- Meta Ad Library.
- Google Ads Transparency.
- TikTok Creator Center, quando houver formato de video curto.
- Swipefile, Marketing Examples, Ads of the World, SwipeWell e SwipeKit.
- Landingfolio e referencias de paginas/ofertas quando o criativo depender da promessa da landing.

Nao copiar concorrente direto. Usar referencias para entender angulo, ritmo, formato e estrutura de oferta.

### Rodada 0 - Preparacao

Antes de subir campanha:

- Conferir se Pixel/CAPI, evento de lead e UTMs estao funcionando.
- Conferir se o match formulario -> WhatsApp esta funcionando por telefone/email.
- Conferir se o CRM registra `qualificacaoResumo` e se a equipe consegue ler ICP, temperatura e proxima acao dentro do resumo.
- Conferir se os eventos `Lead`, `Contact`, `CompleteRegistration` e `Schedule` estao mapeados no n8n/CAPI, mesmo que nem todos sejam usados para otimizacao no inicio.
- Validar no Events Manager da Meta, primeiro com `test_event_code` e depois sem campanha, se os eventos chegam com boa qualidade de match.
- Garantir que `/chatbots` carrega rapido e tem CTA claro.
- Garantir que o Instagram esta pronto para receber visita antes de testar seguidores qualificados.
- Definir ICP, nao-ICP e nivel de consciencia predominante de cada publico.
- Buscar 10 a 20 referencias de anuncios e paginas antes de produzir a rodada.
- Criar pelo menos 6 criativos iniciais.
- Separar criativos por hipotese: gancho, publico, dor, demo, nicho, oferta e nivel de consciencia.
- Separar quais criativos levam para landing, quais puxam WhatsApp direto e quais servem para aquecimento/seguidores qualificados.
- Definir criterio minimo de decisao: lead, conversa iniciada, reuniao marcada e qualidade do lead.
- Manter fila com 6 a 10 criativos em rascunho para reposicao.

### Rodada 1 - Teste inicial de 5 a 7 dias

Subir uma primeira bateria enxuta:

Se a verba inicial for baixa, priorizar os criativos gerais para validar mensagem antes de abrir muitos conjuntos por nicho. Se a verba permitir leitura minima, testar os 3 nichos por criativo/UTM sem fragmentar demais a campanha.

| Prioridade | Formato | Publico | Gancho | Tema | Hipotese | Destino |
|---|---|---|---|---|---|---|
| 1 | Video curto | Frio/amplo | Prova/processo | Demo do fluxo com IA | Demonstracao pratica gera mais confianca que promessa abstrata | `/chatbots?utm_campaign=chatbots_rodada1_geral&utm_content=video_demo_fluxo` |
| 2 | Estatico | Geral | Contraintuitivo | Seu anuncio gera lead. Seu WhatsApp perde a venda. | Dor ligada a trafego pago desperdicado atrai decisor com urgencia | `/chatbots?utm_campaign=chatbots_rodada1_geral&utm_content=estatico_whatsapp_perde` |
| 3 | Carrossel | Geral | Dualidade | WhatsApp como caixa de mensagem vs funil comercial | Explicar o gargalo educa quem ainda nao busca IA | `/chatbots?utm_campaign=chatbots_rodada1_geral&utm_content=carrossel_whatsapp_funil` |
| 4 | Estatico | Clinicas/estetica | Segmentado | Recepcao sobrecarregada | Dor de perguntas repetidas e agenda cria identificacao rapida | `/chatbots?utm_campaign=chatbots_rodada1_clinicas&utm_content=estatico_recepcao` |
| 5 | Carrossel | Imobiliarias | Segmentado | O corretor chega tarde no lead | Velocidade de resposta e contexto do comprador geram urgencia | `/chatbots?utm_campaign=chatbots_rodada1_imobiliarias&utm_content=carrossel_corretor_tarde` |
| 6 | Estatico | Servicos locais | Historia/follow-up | Orcamento sem follow-up vira lead morto | Propostas esquecidas geram conversa comercial qualificada | `/chatbots?utm_campaign=chatbots_rodada1_servicos&utm_content=estatico_followup` |

Se a landing estiver validada mas houver friccao no formulario, testar uma variacao de Vendas 1:1 levando direto para WhatsApp com mensagem inicial padronizada. Comparar qualidade da conversa e agendamento contra o fluxo landing -> formulario -> WhatsApp.

Leitura da rodada:

- Nao pausar criativo nas primeiras horas, salvo erro claro de copy, link, reprovacao ou comentario negativo grave.
- Avaliar diariamente, mas decidir depois de acumular sinais minimos.
- Pausar criativos com gasto relevante e nenhum sinal de clique qualificado, conversa, lead ou engajamento util.
- Manter vencedores rodando sem edicoes desnecessarias.
- Ao pausar um anuncio, subir outro no lugar quando houver verba para manter volume.
- Criar novas variacoes a partir dos melhores, em vez de inventar temas totalmente novos.
- Nao declarar nicho vencedor apenas por clique barato. Priorizar conversa qualificada, reuniao marcada, clareza da dor e potencial de ticket.

Log de aprendizado por rodada:

| Rodada | Criativo | Publico | Hipotese | Metrica observada | Decisao | Proximo teste |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |

### Rodada 2 - Iteracao de 5 a 7 dias

Depois da primeira leitura, produzir variacoes apenas dos angulos que deram sinal.

Exemplos:

| Origem | Variacao recomendada | Quando usar |
|---|---|---|
| Demo performou melhor | Criar versao mais curta e versao com legenda mais direta | Quando video gerou clique ou conversa qualificada |
| Dor de trafego desperdicado performou melhor | Criar criativo com foco em "lead pago perdido no WhatsApp" | Quando decisores mencionarem anuncio/trafego na conversa |
| Clinicas performaram melhor | Criar criativo de agendamento, no-show e perguntas repetidas | Quando lead de clinica tiver dor clara |
| Imobiliarias performaram melhor | Criar criativo de velocidade de resposta e contexto do comprador | Quando corretores responderem bem ao tema |
| Servicos locais performaram melhor | Criar criativo de follow-up e orcamento esquecido | Quando houver leads com venda consultiva/orcamento |

### Rodada 3 - Consolidacao

Quando houver sinal claro de nicho e mensagem:

- Concentrar verba nos 1 ou 2 melhores angulos.
- Criar landing nichada apenas se o nicho provar tracao.
- Separar remarketing com demo, prova de processo e diagnostico.
- Transformar criativos vencedores em posts organicos, stories e argumento de outbound.

### Banco de ideias para proximas rodadas

Estes temas ficam como reserva. Nao subir todos ao mesmo tempo no inicio:

| Formato | Nicho | Tema | Angulo |
|---|---|---|---|
| Carrossel | Clinicas/estetica | 5 perguntas que a IA poderia filtrar | Convenio, horario, preco, endereco, agendamento |
| Video curto | Imobiliarias | Qualificacao automatica de imovel | Tipo de imovel, regiao, faixa de preco, urgencia |
| Estatico | Geral | Quem responde primeiro parece mais preparado | Velocidade de resposta vira percepcao de profissionalismo |
| Post prova/processo | Geral | O que acontece depois que o lead chama | Atendimento, qualificacao, registro, encaminhamento |
| Estatico | Clinicas/estetica | Agenda cheia nao significa atendimento organizado | No-show, reagendamento e duvidas travam recepcao |
| Carrossel | Imobiliarias | Lead imobiliario chega sem contexto | IA coleta contexto antes do corretor gastar tempo |
| Oferta direta | Geral | Diagnostico gratuito do WhatsApp | Encontrar onde o atendimento esta perdendo oportunidade |

## Criativos prioritarios

Produzir primeiro:

1. Video demo geral: WhatsApp -> qualificacao -> CRM -> humano -> follow-up.
2. Carrossel geral: "O lead nao esfria por falta de interesse".
3. Estatico geral: "Seu anuncio gera lead. Seu WhatsApp perde a venda."
4. Carrossel clinicas: "5 perguntas que a IA poderia filtrar".
5. Carrossel imobiliarias: "O corretor chega tarde no lead".
6. Oferta direta: "Diagnostico gratuito do WhatsApp".

## Metricas de decisao

Escolher o nicho vencedor por:

- Custo por lead.
- Tempo ate primeira resposta.
- Taxa de match entre formulario e conversa no WhatsApp.
- Taxa de resposta no WhatsApp.
- Leads sem resposta.
- Leads qualificados.
- Conversas qualificadas iniciadas por campanha de WhatsApp.
- Interacoes qualificadas no perfil: direct, respostas de stories, comentarios com dor real e cliques no link.
- Percentual de `icp_alto` e `icp_medio`.
- Distribuicao de temperatura: quente, morno e frio.
- Dor principal declarada na qualificacao.
- Objecao principal declarada na qualificacao.
- Cliques no WhatsApp.
- Conversas iniciadas.
- Agendamentos.
- Taxa de agendamento oferecido vs agendamento marcado.
- Comparecimento.
- Reunioes marcadas.
- Clareza da dor na conversa.
- Menor necessidade de explicar o servico.
- Potencial de ticket.
- Taxa de proposta enviada.
- Taxa de fechamento.
- Follow-ups realizados.
- Vendas atribuidas ao WhatsApp.
- Motivo de perda: demora, preco, sumiu, sem perfil, concorrente ou atendimento.
- Capacidade de expandir para CRM, automacao, landing page, sistema interno ou dashboard.

## Decisao sobre nichar

Nao nichar a landing logo de inicio.

Primeiro:

1. Testar 3 nichos por criativos e UTMs.
2. Usar `/chatbots` como landing unica.
3. Medir resposta e qualidade dos leads.
4. Criar landing nichada apenas para o nicho que provar tracao.

## Proximos passos

1. Confirmar ICP, nao-ICP, persona Mariana Almeida e 3 nichos prioritarios.
2. Validar landing `/chatbots`, formulario curto, WhatsApp e destino do lead.
3. Revisar Instagram antes de trafego: bio, link, destaques, posts fixados e grade inicial por RETINA.
4. Conferir se o n8nCRM salva UTM, nicho, criativo, campanha, telefone, email, `lead_id` e identificadores de tracking.
5. Validar match formulario -> WhatsApp no CRM usando telefone/email normalizados.
6. Definir como usar as colunas atuais do CRM: `novo`, `aguardando`, `qualificado`, `proposta` e `fechado`.
7. Definir o template de `qualificacaoResumo` com ICP, temperatura, dor principal, objecao principal e proxima acao.
8. Configurar tags operacionais minimas apenas se elas forem usadas para automacao, filtro ou relatorio.
9. Conferir Pixel/CAPI e mapear `Lead`, `Contact`, `CompleteRegistration`, `Schedule` e `Purchase`.
10. Testar eventos no Events Manager com `test_event_code`.
11. Testar fluxo real sem campanha: formulario -> WhatsApp -> qualificacao -> agendamento.
12. Criar roteiro do agente de IA para qualificacao no WhatsApp, com perguntas curtas e uma por vez.
13. Criar roteiro do diagnostico gratuito com criterios de qualificacao, resumo e proximo passo.
14. Preparar mensagem inicial para campanhas de WhatsApp direto.
15. Criar a demo principal do fluxo formulario -> WhatsApp -> qualificacao -> CRM -> humano -> follow-up -> evento CAPI.
16. Preparar 3 posts fixados: oferta, demo do fluxo e dor principal do WhatsApp.
17. Fazer swipe file com 10 a 20 referencias antes da producao da Rodada 1.
18. Mapear os criativos por nivel de consciencia, tipo de gancho e funcao: landing, WhatsApp direto ou seguidores qualificados.
19. Criar a primeira leva de 6 criativos prioritarios a partir da demo e das dores por nicho.
20. Fazer outbound personalizado para pelo menos 30 empresas dos 3 nichos usando os mesmos ganchos dos anuncios.
21. Subir a Rodada 1 no Meta Ads com UTMs separadas e 5 a 7 dias de leitura.
22. Avaliar sinais diariamente, registrar aprendizados e evitar troca ou edicao diaria de criativos.
23. Ativar remarketing apenas quando houver publico suficiente.
24. Criar a Rodada 2 apenas com variacoes dos criativos que gerarem sinal real.
25. Decidir o primeiro nicho a aprofundar usando leads qualificados, reunioes marcadas, propostas enviadas e qualidade das conversas, nao seguidores ou curtidas.
