# EssentialWeb - AI OS

## O que e esse workspace

Workspace central da EssentialWeb para marketing, comercial, automacoes, projetos internos, contexto de negocio e criacao futura de skills reutilizaveis.

**Estrutura de pastas:**
- `_contexto/` - memoria do sistema: empresa, preferencias e foco atual.
- `marca/` - identidade visual, logos e guia de design.
- `marketing/` - carrosseis, posts, campanhas e referencias de conteudo.
- `comercial/` - propostas, follow-ups, scripts comerciais e materiais de venda.
- `clientes/` - um subdiretorio por cliente externo.
- `automacoes/` - referencias e documentacao de fluxos n8n, WhatsApp e CRM.
- `projetos/` - projetos internos/proprios da EssentialWeb, como site institucional e n8nCRM.
- `dados/` - arquivos para analise, imports temporarios, PDFs, CSVs e imagens de apoio.
- `templates/` - modelos reutilizaveis de skills, marca, ferramentas e perfis.
- `.claude/commands/` - slash commands de processo do AI OS (versionados no git, invocaveis por /comando).
- `.claude/skills/` - skills locais especificas deste workspace (versionadas no git, carregadas automaticamente).
- `.env` - segredos e tokens compartilhados pelas skills (raiz do projeto, fora do git).
- `tarefas.md` - lista de pendencias corrente.

## Sobre o negocio

A EssentialWeb e uma empresa brasileira de tecnologia fundada por Patrick, em Campo Grande, MS. Atua com chatbots com IA, sites, automacoes, sistemas e aplicacoes, atendendo clientes externos e organizando a propria operacao de marketing/comercial.

## O que mais fazemos aqui

- Planejamento e producao de conteudo de marketing.
- Carrosseis, posts, campanhas e materiais comerciais.
- Propostas, follow-ups e scripts de venda.
- Organizacao de automacoes com n8n, WhatsApp e CRM.
- Apoio a projetos tecnicos em Node.js/TypeScript, NestJS, React, Kotlin/Spring Boot, PostgreSQL, Redis, Docker e Cloudflare.

## Clientes e contexto

A operacao e solo, com atendimento a clientes externos por consultoria/projetos e projetos internos em `projetos/`. Projetos de clientes devem ficar em `clientes/[nome-cliente]/`; ativos proprios ficam em `projetos/`.

## Tom de voz

Portugues brasileiro, direto, tecnico quando necessario e pragmatico. Para marketing, escrever com angulo concreto, tensao real, clareza comercial e sem frases genericas de IA. Evitar padding, solucoes complexas sem necessidade e convencoes que nao ajudem o resultado.

## Ferramentas conectadas

- Codex / Claude Code
- n8n self-hosted via MCP
- Docker / Docker Compose
- Git / GitHub Actions
- Node.js, TypeScript, NestJS, React
- PostgreSQL, Redis, RabbitMQ, BullMQ
- Cloudflare, Traefik, Nginx
- Playwright

---

## Contexto do negocio

No inicio de toda conversa, ler os seguintes arquivos, se existirem e estiverem configurados:

1. `_contexto/empresa.md` - quem e o usuario, o que faz e como funciona o negocio.
2. `_contexto/preferencias.md` - tom de voz, estilo de escrita e o que evitar.
3. `_contexto/estrategia.md` - foco atual, prioridades e o que pode esperar.

Use essas informacoes como base para qualquer resposta ou decisao. Ao sugerir prioridades, formatos ou abordagens, considere o foco atual descrito em `_contexto/estrategia.md`.

Para qualquer tarefa visual, como carrossel, proposta, slide ou landing page, consulte `marca/design-guide.md`.

Nao e necessario listar o que foi lido nem confirmar a leitura. Use o contexto naturalmente.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verifique se existe um command ou skill relevante em:

1. `.claude/commands/` - slash commands de processo (/iniciar, /setup, /mapear, /atualizar, /novo-projeto, /syncar)
2. `.claude/skills/`

Se encontrar um command ou skill relevante, siga as instrucoes dele. Se nao encontrar, execute a tarefa normalmente.

Ao concluir uma tarefa que nao tinha skill mas parece repetivel, pergunte:

> "Isso pode virar uma skill pra proxima vez. Quer que eu crie?"

Nao pergunte para tarefas pontuais ou perguntas simples. So quando o padrao de repeticao for claro.

---

## Aprender com correcoes

Quando Patrick corrigir algo, melhorar uma resposta ou der uma instrucao que parece permanente, pergunte:

> "Quer que eu salve isso pra nao precisar repetir?"

Se sim, identifique onde faz mais sentido salvar:

- Sobre o negocio: adicionar em `_contexto/empresa.md`
- Sobre preferencias e estilo: adicionar em `_contexto/preferencias.md`
- Sobre prioridades e foco atual: adicionar em `_contexto/estrategia.md`
- Regra de comportamento nesta pasta: adicionar em `AI-OS.md`

Salvar com uma linha nova clara, sem reformatar o arquivo inteiro. Confirmar o que foi salvo mostrando a linha adicionada.

Nao pergunte se a correcao for obvia de contexto imediato. So pergunte quando a informacao tiver valor duradouro.

---

## Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante no projeto, como novo cliente, nova skill, mudanca de foco, novo processo, ferramenta instalada ou estrutura de pastas alterada, pergunte:

> "Isso mudou algo no teu contexto. Quer que eu atualize os arquivos de memoria?"

Se sim, identifique o que precisa atualizar:

- Novo cliente, servico, ferramenta ou equipe: `_contexto/empresa.md`
- Mudanca de prioridade ou foco: `_contexto/estrategia.md`
- Correcao de tom ou estilo: `_contexto/preferencias.md`
- Nova pasta, regra de organizacao, workflow ou skill criada: `AI-OS.md`
- Mudanca visual, cores, fontes ou logo: `marca/design-guide.md`

Mostrar o que vai mudar antes de salvar. Nao reformatar o arquivo inteiro; adicione ou edite apenas a linha relevante.

---

## Criacao de skills

Quando Patrick pedir para criar uma nova skill:

1. Verificar se existe um template relevante em `templates/skills/`. Se existir, usar como base e adaptar.
2. Salvar a skill em `.claude/skills/nome-da-skill/SKILL.md`. Esse e o diretorio de skills do workspace, versionado no git e carregado automaticamente (invocavel por `/nome-da-skill`).
3. Ler `_contexto/empresa.md` e `_contexto/preferencias.md` para calibrar o conteudo.
4. Se a skill precisar de arquivos de apoio, criar dentro da pasta da skill.
5. Segredos e tokens vao no `.env` na raiz do projeto, nunca dentro da pasta da skill.

---

## Regras especificas deste workspace

- Projetos internos/proprios ficam em `projetos/`.
- Projetos de clientes ficam em `clientes/[nome-cliente]/`.
- Conteudo social finalizado fica em `marketing/`.
- Estrategia e copy de follow-up ficam em `comercial/follow-ups/`; implementacoes automatizadas ficam em `automacoes/`.
- `projetos/carrosseis claude/` e referencia temporaria para uma futura skill de carrosseis; outputs finais devem migrar para `marketing/carrosseis/`.
