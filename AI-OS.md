# AI OS — Kit Ratos de IA

Este workspace organiza contexto, workflows e skills de forma agnóstica para agentes de IA. A fonte de verdade é este arquivo. Arquivos específicos de ferramentas, como `CLAUDE.md` e `AGENTS.md`, devem apenas apontar para ele.

## Compatibilidade

Alguns arquivos vieram do Claude Code OS. Ao executar este workspace em qualquer agente, aplique estes aliases:

- `CLAUDE.md` significa `AI-OS.md`
- `/setup`, `/mapear`, `/atualizar`, `/iniciar`, `/novo-projeto` e `/syncar` sao slash commands em `.claude/commands/` (invocaveis diretamente por /comando)
- "skill-creator nativa do Claude Code" significa usar a melhor capacidade disponível do agente para criar uma skill estruturada em `SKILL.md`
- "WebFetch" significa usar a capacidade disponível para buscar conteúdo web, quando o ambiente permitir
- "MCP" significa conector, ferramenta externa ou servidor MCP disponível no ambiente atual

Use `.claude/commands/` (rotinas de processo) e `.claude/skills/` (capacidades) como fontes locais deste workspace.

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos, se existirem e estiverem configurados:

1. `_contexto/empresa.md` — quem é o usuário, o que faz e como funciona o negócio
2. `_contexto/preferencias.md` — tom de voz, estilo de escrita e o que evitar
3. `_contexto/estrategia.md` — foco atual, prioridades e o que pode esperar

Use essas informações como base para qualquer resposta ou decisão. Ao sugerir prioridades, formatos ou abordagens, considere o foco atual descrito em `_contexto/estrategia.md`.

Para qualquer tarefa visual, como carrossel, proposta, slide ou landing page, consulte `marca/design-guide.md` como referência de estilo.

Não é necessário listar o que foi lido nem confirmar a leitura. Use o contexto naturalmente.

## Fluxo de trabalho

Antes de executar qualquer tarefa, verifique se existe um workflow ou skill relevante em:

1. `.claude/commands/`
2. `.claude/skills/`
Se encontrar um workflow ou skill relevante, siga as instruções dele. Se não encontrar, execute a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível, pergunte:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não pergunte para tarefas pontuais ou perguntas simples. Só quando o padrão de repetição for claro.

## Commands disponiveis

Os slash commands de processo ficam em `.claude/commands/`:

- `iniciar.md` — inicia a sessão lendo contexto e pendências
- `setup.md` — configura o sistema para o negócio do usuário
- `mapear.md` — identifica processos repetitivos e cria skills personalizadas
- `atualizar.md` — compara o estado real do projeto com os arquivos de contexto
- `novo-projeto.md` — cria uma pasta de projeto com contexto dedicado
- `syncar.md` — sincroniza o workspace com Git/GitHub

## Skills locais disponíveis

- `google-ads-ratos` — skill local em `.claude/skills/google-ads-ratos/` para configurar, ler e operar campanhas Google Ads via SDK oficial.
- `ga4-ratos` — skill local em `.claude/skills/ga4-ratos/` para consultar propriedades, relatórios, tráfego, UTMs, conversões e dados em tempo real do GA4.
- `ads-ratos` — skill local em `.claude/skills/ads-ratos/` para diagnóstico, histórico, auditoria e relatórios de tráfego pago integrando Meta Ads, Google Ads e GA4.
- `ads-ratos` carrega `references/pedro-sobral-campanhas.md` como instrucao operacional para estrategia, criacao, segmentacao, testes, otimizacao e auditoria de campanhas de trafego pago.
- `carrossel` — skill local em `.claude/skills/carrossel/` para criar carrosseis editoriais em HTML/PNG.
- `gpt-image-2` — skill local em `.claude/skills/gpt-image-2/` para planejar e gerar imagens com GPT Image 2, incluindo previews baratos, escolha de tamanho/formato/background e confirmação antes de `quality: high`.
- `carrossel-essentialweb` — skill local em `.claude/skills/carrossel-essentialweb/` para criar carrosséis editoriais da EssentialWeb em HTML e PNG, usando a metodologia legado de `projetos/carrosseis claude` e salvando novos outputs em `marketing/carrosseis/`.
- O carrossel `chatbot-whatsapp-gambiarra` fica em `marketing/carrosseis/chatbot-whatsapp-gambiarra/`; novos carrosséis devem seguir a mesma estrutura `carousel-text.md`, `carousel.html`, `assets/` e `slides-png/`.
- `google-ads-ratos` está configurada em modo teste com MCC `3202454490` e conta Ads `7574792015`; IDs de produção ficam preservados em `.claude/skills/google-ads-ratos/contas.yaml`.
- `ga4-ratos` está configurada para a propriedade GA4 `533408886` (`Essential Web site`) com OAuth próprio no `.env` compartilhado de `.claude/skills/`.
- O site institucional da EssentialWeb fica em `projetos/essential-web/` e usa GA4 `533408886` (`Essential Web site`).

## Aprender com correções

Quando o usuário corrigir algo, melhorar uma resposta ou der uma instrução que parece permanente, como "na verdade é assim", "não faça mais isso", "prefiro assim", "sempre que...", "evita..." ou "da próxima vez...", pergunte:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identifique onde faz mais sentido salvar:

- Sobre o negócio: adicionar em `_contexto/empresa.md`
- Sobre preferências e estilo: adicionar em `_contexto/preferencias.md`
- Sobre prioridades e foco atual: adicionar em `_contexto/estrategia.md`
- Regra de comportamento nesta pasta: adicionar em `AI-OS.md`

Salvar com uma linha nova clara, sem reformatar o arquivo inteiro. Confirmar o que foi salvo mostrando a linha adicionada.

Não pergunte se a correção for óbvia de contexto imediato, como "na verdade o arquivo se chama X". Só pergunte quando a informação tiver valor duradouro.

## Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante no projeto, como novo cliente, nova skill, mudança de foco, novo processo, ferramenta instalada ou estrutura de pastas alterada, pergunte:

> "Isso mudou algo no teu contexto. Quer que eu atualize os arquivos de memoria?"

Se sim, identifique o que precisa atualizar:

- Novo cliente, serviço, ferramenta ou equipe: `_contexto/empresa.md`
- Mudança de prioridade ou foco: `_contexto/estrategia.md`
- Correção de tom ou estilo: `_contexto/preferencias.md`
- Nova pasta, regra de organização, workflow ou skill criada: `AI-OS.md`
- Mudança visual, cores, fontes ou logo: `marca/design-guide.md`

Mostrar o que vai mudar antes de salvar. Não reformatar o arquivo inteiro; adicione ou edite apenas a linha relevante.

Não perguntar em tarefas pontuais que não mudam o contexto, perguntas simples, conversas sem ação ou mudanças que já foram salvas pelo bloco "Aprender com correções".

## Criação de skills

Quando o usuário pedir para criar uma nova skill:

1. Verificar se existe um template relevante em `templates/skills/`. Se existir, usar como base e adaptar ao contexto do usuário.
2. Perguntar: "Essa skill é específica pra esse projeto ou vai ser útil em qualquer projeto?"
3. Salvar a skill em `.claude/skills/nome-da-skill/SKILL.md`. Esse é o diretório de skills do workspace, versionado no git e carregado automaticamente (invocável por `/nome-da-skill`).
4. Segredos e tokens vão no `.env` na raiz do projeto (não dentro da pasta da skill).
5. Ler `_contexto/empresa.md` e `_contexto/preferencias.md` para calibrar o conteúdo da skill.
6. Se a skill precisar de arquivos de apoio, como templates, referências ou exemplos, criar dentro da pasta da skill.

## Regras gerais

- Tom direto e humano, sem excesso de entusiasmo.
- Prefira mudanças mínimas e consistentes com a estrutura existente.
- Antes de mudanças estruturais, explique rapidamente a arquitetura atual e o plano.
- Nunca mova ou apague pastas existentes sem confirmacao.
- Não introduza dependências novas sem avisar.
- Manter Playwright instalado no workspace quando for usado para revisar páginas web, carrosséis ou exports visuais; não remover `node_modules`, `package.json` ou `package-lock.json` nesses casos.
- Não invente informação de contexto; se não conseguir inferir, pergunte.
- Ao finalizar uma tarefa, informe resumo das mudanças, arquivos alterados, impacto na arquitetura, riscos ou itens não verificados e próximos passos recomendados.
