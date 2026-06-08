# Estúdio Lumina

## O que é
Cliente da EssentialWeb. Gestão de marca, marketing, criativos, campanhas e sistema de galeria fotográfica (Lumina Web).

## Tipo
Cliente

## Escopo
- Criação e manutenção do design system
- Definição e documentação do ICP
- Produção de criativos
- Gestão de campanhas
- Sistema de galeria fotográfica para entrega de fotos a clientes (`projetos/lumina-web/`)

## Contexto
Sem prazo ou orçamento definidos no setup inicial.

## Contato
(preencher)

## Entregas
- [ ] Design system documentado
- [ ] ICP definido
- [x] MVP de galeria fotográfica (lumina-web)
- [ ] Deploy de produção da galeria na VPS
- [ ] (adicionar conforme o projeto avança)

## Arquivos importantes
- `_contexto/empresa.md` — quem é o Estúdio Lumina, nicho, produto
- `_contexto/icp.md` — perfil de cliente ideal
- `_contexto/preferencias.md` — tom de voz e estilo de comunicação
- `marca/design-guide.md` — cores, tipografia, logo, design system
- `projetos/lumina-web/` — sistema de galeria fotográfica

## Regras específicas
- Para qualquer tarefa visual, consultar `marca/design-guide.md`
- Tom de voz e estilo de escrita seguem `_contexto/preferencias.md`

---

## Lumina Web — Sistema de Galeria

### Visão geral
MVP de galeria fotográfica: admin faz upload com marca d'água → cliente acessa link público → seleciona fotos → checkout via WhatsApp Pix → admin libera download.

**Stack:** Rails 7.2 API + Next.js 15 + PostgreSQL + Redis/Sidekiq + Cloudflare R2

### Estrutura do projeto
```
projetos/lumina-web/
├── backend/          — Rails 7.2 API (porta 3001)
├── frontend/         — Next.js 15 (porta 3000)
├── docker-compose.yml          — ambiente de desenvolvimento local
├── docker-compose.prod.yml     — deploy na VPS EssentialWeb
├── .env.example                — variáveis para dev
└── .env.production.example     — variáveis para produção (nunca commitar o .env.production real)
```

### Infraestrutura VPS
A VPS EssentialWeb já possui os seguintes serviços compartilhados na rede `essential_n8n_network`:

| Container  | Imagem           | Função                        | Nota                           |
|------------|------------------|-------------------------------|--------------------------------|
| `postgres` | postgres:16.8    | Banco de dados                | Lumina usa DB `lumina_production` |
| `redis`    | redis:7.4.3      | Fila Sidekiq + cache          | Lumina usa DB 3 (n8n usa DB 2) |
| `traefik`  | traefik:v3.6.1   | Reverse proxy + TLS           | Let's Encrypt automático       |

**O compose de produção NÃO cria postgres nem redis.** Reutiliza os containers existentes.

### Domínios planejados para produção
| Domínio                    | Serviço         |
|----------------------------|-----------------|
| `galeria.lumina.com.br`    | Frontend (galeria pública + admin) |
| `api.lumina.com.br`        | Backend Rails API |

### Checklist de deploy (primeira vez)
```bash
# 1. Criar banco no postgres existente da VPS
docker exec -it postgres psql -U postgres -c "CREATE DATABASE lumina_production;"
docker exec -it postgres psql -U postgres -c "CREATE USER lumina WITH PASSWORD 'SENHA_FORTE';"
docker exec -it postgres psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE lumina_production TO lumina;"

# 2. Configurar variáveis
cp .env.production.example .env.production
# Editar .env.production com valores reais

# 3. Build e subir
docker compose -f docker-compose.prod.yml build
docker compose -f docker-compose.prod.yml up -d

# 4. Apontar DNS para IP da VPS
# galeria.lumina.com.br → IP da VPS
# api.lumina.com.br     → IP da VPS

# 5. Verificar saúde
curl https://api.lumina.com.br/health
```

### Variáveis de produção críticas
- `SECRET_KEY_BASE` — gerar com `rails secret` (nunca usar o valor de dev)
- `ADMIN_PASSWORD` — trocar após primeiro login
- `DATABASE_URL` — apontar para `postgres:5432/lumina_production` (container na rede)
- `REDIS_URL` — `redis://redis:6379/3` (DB 3, não conflita com n8n)
- `R2_*` — credenciais do bucket Cloudflare R2 (obrigatório em produção)

### Fluxo de negócio
1. Admin cria cliente → cria galeria → faz upload de fotos (com marca d'água automática)
2. Sistema processa fotos em background (Sidekiq, fila `images`)
3. Admin compartilha link público com o cliente
4. Cliente acessa galeria, seleciona fotos, informa nome e telefone
5. Se tiver fotos extras: WhatsApp com Pix manual → admin libera no painel
6. Se não tiver extras: download liberado imediatamente
7. Originais ficam retidos 30 dias após expiração da galeria

### Pontos de atenção técnicos
- MiniMagick (ImageMagick) processa fotos em memória — fila `images` limitada a 2 workers simultâneos
- Liberação de pagamento é manual (WhatsApp → admin → clique no painel) — gargalo ao escalar
- Sem paginação nos endpoints de listagem — monitorar volume de galerias/imagens
- Sidekiq Web não está montado — para monitorar jobs em produção, usar `docker exec` no container

### Desenvolvimento local
```bash
cp .env.example .env
docker compose up --build
# Admin: http://localhost:3000/admin (admin@lumina.local / lumina-admin-123)
# API:   http://localhost:3001/health
```
