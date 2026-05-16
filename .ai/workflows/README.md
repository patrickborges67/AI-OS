# Workflows Agnósticos

Esta pasta contém os workflows operacionais do workspace em formato Markdown.

Eles foram migrados de `.claude/commands/` para permitir uso por qualquer agente. Quando um workflow mencionar termos específicos do Claude Code, use os aliases definidos em `AI-OS.md`.

## Mapa

- `iniciar.md` — início de sessão e leitura de contexto
- `setup.md` — onboarding e configuração inicial
- `mapear.md` — mapeamento de processos e criação de skills
- `atualizar.md` — auditoria e manutenção de contexto
- `novo-projeto.md` — criação de projeto com contexto próprio
- `syncar.md` — sincronização com Git/GitHub

## Regra de manutenção

Novos workflows devem ser criados primeiro aqui. Se precisar manter compatibilidade com Claude Code, crie um espelho ou adaptador em `.claude/commands/`.
