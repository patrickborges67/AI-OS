# Slash Commands

Esta pasta contém os comandos de processo do workspace, invocáveis por `/comando`
no Claude Code. Cada `.md` vira um slash command nativo (carregado automaticamente).

## Mapa

- `iniciar.md` — início de sessão e leitura de contexto (`/iniciar`)
- `setup.md` — onboarding e configuração inicial (`/setup`)
- `mapear.md` — mapeamento de processos e criação de skills (`/mapear`)
- `atualizar.md` — auditoria e manutenção de contexto (`/atualizar`)
- `novo-projeto.md` — criação de projeto com contexto próprio (`/novo-projeto`)
- `syncar.md` — sincronização com Git/GitHub (`/syncar`)

## Regra de manutenção

Novos comandos de processo devem ser criados aqui, com frontmatter `description`
(e opcionalmente `argument-hint`). Capacidades reutilizáveis que o agente pode
acionar sozinho pelo contexto vão em `.claude/skills/`, não aqui.
