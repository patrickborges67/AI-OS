---
name: novo-projeto
description: >
  Cria uma nova pasta de projeto com contexto personalizado. Entrevista o usuario
  sobre o projeto, gera a estrutura, pode instalar AI OS/skills locais e referencia
  no CLAUDE.md principal.
---

# /novo-projeto - Criar novo projeto com contexto

Cria uma pasta de projeto com contexto dedicado. Pode operar em dois modos:

1. **Pasta simples:** cria uma pasta dentro deste workspace com `CLAUDE.md` curto.
2. **Projeto limpo/standalone:** cria uma pasta que ja nasce com `AI-OS.md`, `AGENTS.md`, workflows e skills locais instaladas.

## Quando usar

- Novo cliente entrando
- Novo site ou app para desenvolver
- Novo produto ou lancamento
- Qualquer trabalho que merece pasta propria e contexto separado
- Novo repositorio limpo que deve carregar as skills deste workspace

## Fluxo

### Passo 1: Entender o projeto

Perguntar em conversa natural, uma pergunta por vez:

**Pergunta 1:** "Qual e o nome do projeto? Pode ser nome do cliente, produto ou site."

**Pergunta 2:** "Que tipo de projeto e?"
- Cliente: entrega de servico para alguem
- Produto proprio: site, app, curso, loja
- Conteudo: canal, serie, newsletter
- Interno: processo, ferramenta, organizacao

**Pergunta 3:** "Me explica em poucas palavras o que e o projeto e o que precisa ser entregue."

**Pergunta 4:** "Tem prazo, orcamento ou ferramenta especifica que eu precise saber?"

**Pergunta 5:** "Esse projeto deve ser uma pasta simples dentro deste workspace ou um projeto limpo/standalone com AI OS e skills instaladas?"

Se o usuario der respostas completas logo na primeira mensagem, pular as perguntas ja respondidas.

### Passo 2: Definir a pasta

Sugerir o local baseado no tipo de projeto e na estrutura atual:

- **Cliente** -> `clientes/nome-do-cliente/`
- **Produto** -> `projetos/nome-do-projeto/`
- **Conteudo** -> `conteudo/nome-do-projeto/`
- **Interno** -> `projetos/nome-do-projeto/`

Verificar a estrutura de pastas que ja existe para manter consistencia.

Apresentar a sugestao:

> "Sugiro criar em `clientes/nome-do-cliente/`. Faz sentido ou prefere outro lugar?"

Aguardar confirmacao.

### Passo 3: Definir modo de criacao

Usar **Projeto limpo/standalone** quando o usuario disser algo como:

- "projeto limpo"
- "standalone"
- "repositorio proprio"
- "com skills instaladas"
- "pra subir separado"
- "quero clonar/subir esse projeto depois"

Caso contrario, usar **Pasta simples**.

### Passo 4: Criar a pasta e o contexto

Criar a pasta e gerar o `CLAUDE.md` do projeto:

```markdown
# [Nome do Projeto]

## O que e
[descricao curta do projeto, 1-2 frases]

## Tipo
[Cliente / Produto / Conteudo / Interno]

## Escopo
[o que precisa ser entregue, baseado nas respostas]

## Contexto
[prazo, orcamento, ferramentas, qualquer detalhe relevante]

## Arquivos importantes
- (sera preenchido conforme o projeto avanca)

## Regras especificas
- (sera preenchido conforme o projeto avanca)
```

Se for **cliente**, adicionar tambem:

```markdown
## Contato
[nome do contato, se mencionou]

## Entregas
- [ ] [entrega 1]
- [ ] [entrega 2]
```

### Passo 5: Instalar AI OS e skills no modo standalone

Se o modo for **Projeto limpo/standalone**, criar/copiar:

```text
[pasta-do-projeto]/
  AI-OS.md
  AGENTS.md
  CLAUDE.md
  .claude/
    commands/
    skills/
  _contexto/
    empresa.md
    preferencias.md
    estrategia.md
  marca/
    design-guide.md
  dados/
    README.md
```

Regras para copiar a base:

- Copiar `.claude/commands/` inteiro.
- Copiar `.claude/skills/` inteiro.
- Excluir segredos e artefatos: `.env`, `.env.*`, `node_modules/`, `dist/`, `build/`, `__pycache__/`, `*.pyc`, `*.log`, caches e outputs gerados.
- Nao copiar `contas.yaml` com IDs reais por padrao. Para skills que precisam de contas, criar `contas.example.yaml` ou deixar instrucao de setup.
- Copiar `AI-OS.md` e `AGENTS.md`.
- Criar `CLAUDE.md` do projeto apontando para `AI-OS.md` e mantendo o contexto curto do projeto.
- Copiar `_contexto/preferencias.md` se fizer sentido manter o tom de voz.
- Criar `_contexto/empresa.md` e `_contexto/estrategia.md` especificos do novo projeto.
- Copiar `marca/design-guide.md` apenas se a marca atual servir para o novo projeto. Se for cliente ou marca nova, criar um template vazio e perguntar depois.
- Copiar `dados/README.md`.
- Nao copiar `projetos/`, `clientes/`, `marketing/carrosseis/` ou outputs atuais do workspace raiz.

### Passo 6: Atualizar referencia no workspace principal

Ler o `CLAUDE.md` da raiz do workspace. Encontrar a secao de estrutura de pastas e adicionar a nova pasta.

Exemplo:

> Adicionei `clientes/fabio-haag/` na estrutura de pastas do CLAUDE.md principal.

Se a secao de estrutura nao existir ou nao fizer sentido editar, pular e informar:

> "Criei a pasta e o CLAUDE.md do projeto. Se quiser, adiciona na estrutura de pastas do CLAUDE.md principal depois."

### Passo 7: Atualizar contexto, se aplicavel

Se o projeto e um **cliente novo**, perguntar:

> "Quer que eu adicione esse cliente em `_contexto/empresa.md` tambem?"

Se sim, adicionar uma linha na secao de clientes do `empresa.md`.

### Passo 8: Confirmar

Mostrar o resumo:

```text
Projeto criado.

Pasta: clientes/fabio-haag/
CLAUDE.md: clientes/fabio-haag/CLAUDE.md
Modo: pasta simples ou projeto limpo/standalone
Skills: instaladas se o modo standalone foi usado
Referencia: adicionada na estrutura de pastas do CLAUDE.md principal, se aplicavel
```

## Regras

- Tom direto, sem cerimonia.
- Nao criar subpastas dentro do projeto a menos que o usuario peca ou o modo standalone exija a base AI OS.
- O `CLAUDE.md` do projeto deve ser curto no inicio. Vai crescer com o uso.
- Nunca mover pastas existentes sem perguntar.
- Se o usuario ja criou a pasta manualmente, gerar ou atualizar o contexto dentro dela.
- Respeitar a estrutura de pastas que o `/setup` criou para aquele perfil.
- No modo standalone, nao copiar segredos, contas reais ou dependencias instaladas.
