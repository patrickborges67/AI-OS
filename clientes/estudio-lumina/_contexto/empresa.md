# Contexto do Cliente - Estúdio Lumina

**Nome do cliente:** Estúdio Lumina
**Contato:** (preencher)
**Nicho:** ensaios fotográficos com IA para datas especiais
**Produto/Serviço:** cliente envia uma foto comum e o estúdio gera um ensaio fotográfico profissional usando IA — voltado para aniversários, formaturas, conquistas pessoais e outras datas marcantes
**Público-alvo:** mulheres que querem um registro visual bonito de uma data especial, mas não têm budget ou disposição para ensaio fotográfico tradicional
**Persona:** Mariana Oliveira — ver `_contexto/icp.md` para mapeamento emocional completo
**Canais ativos:** Instagram, WhatsApp, Facebook
**Fase do negócio:** lançamento

## Contas Meta

| Conta | ID |
|-------|----|
| Meta Ads | `act_1399522635268024` |
| Instagram | `17841443954905257` |
| Instagram @ | `@estudiolumina67` |
| Facebook Page | `1075178832353494` |
| Pixel / CAPI | `871404632654375` |
| WhatsApp Business | `+55 67 8104-2715` (WABA ID: `97044169286271`) |

## Produto e oferta

- **Pacote promocional (carro-chefe):** 10 fotos por R$ 24,90 (~R$ 2,49/foto) — **válido apenas para
  cenário único** (as 10 fotos no mesmo tema).
- **Outros pacotes:** 1 foto R$ 5,00 · 3 fotos R$ 9,99 · 5 fotos R$ 14,99.
- **Foto de casal:** adicional de R$ 10 (independente da quantidade).
- **Foto em grupo:** R$ 14,99 por foto · ou 10 fotos por R$ 99,00. (cliente escolhe os cenários livremente, sem taxa extra)
- **Restauração de fotos antigas:** R$ 9,99 por foto · ou 10 fotos por R$ 70,00. (não tem cenário)
- **Pacotes de aniversário por nº de cenários (10 fotos, preço fixo):**
  | Pacote | Cenários | Preço |
  |---|---|---|
  | Promocional | 1 cenário | R$ 24,90 |
  | 2 cenários | 2 cenários | R$ 29,90 |
  | 3 cenários | 3 cenários | R$ 34,90 |
  - Cada cenário é um **ensaio temático diferente** (ex.: 3 fotos preto e branco + 3 com balão + 4 com
    sombra). Distribuição das 10 fotos entre os cenários a critério do cliente.
  - **Comunicar o cenário como valor, não como taxa:** vender cada cenário extra como "mais um ensaio
    temático" (mais variedade, mais looks), nunca como "pedágio" sobre o pacote base.
  - **Cenário avulso (acima de 3):** +R$ 4,99 por cenário adicional, SÓ no ensaio de aniversário.
    Não se aplica a foto em grupo nem a restauração.
- **Prazo de produção:** 24h padrão. **Upsell "Entrega Express":** +R$ 19,99 entrega em até 4h.
- **Pacotes Dia dos Namorados 2026 (campanha sazonal — produto de presente, ensaio do casal):**
  | Pacote | Conteúdo | Preço |
  |---|---|---|
  | Casal Essencial | 10 fotos do casal, 1 cenário + frase romântica | R$ 39,90 |
  | Casal Romântico ⭐ (carro-chefe) | 10 fotos, 3 cenários + frase + versão story | R$ 59,90 |
  | Casal Inesquecível | 15 fotos, 4–5 cenários + versão story | R$ 89,90 |
  - **Upsell:** Entrega Express 4h +R$ 19,99 (disponível pra todos os pacotes; só ofertar se cliente sinalizar pressa).
  - **R$ 59,90 é aposta de mercado a validar:** subir com ele; se a conversa→venda cair muito vs.
    aniversário, testar R$ 49,90.
  - **Versão story:** 2 fotos finais (escolhidas pelo cliente após a entrega do ensaio) reenquadradas
    em formato vertical 9:16, prontas pra postar nos stories.
  - Posicionamento: presente (compara com chocolate/perfume/jantar R$80–200), não autoimagem — por
    isso preço acima dos pacotes de aniversário. Detalhes da campanha na seção 6 do planejamento de tráfego.
- **Como funciona:** cliente manda 1 foto do rosto pelo WhatsApp → equipe gera o ensaio temático.

## Operação e stack

- **Aquisição:** anúncios CTWA (Click-to-WhatsApp) no Meta. Campanha atual: `lumina-aniversario-adulto-01`.
- **Atendimento:** agente de IA no WhatsApp **implementado e ativo** (workflow n8n `Estudio Lumina v2`,
  ID `tu8iSkeGA7m505Yp`) — qualifica, envia exemplos, fecha com PIX, faz handoff e pausa ao detectar
  intervenção humana (echo `smb_message_echoes`).
- **Gateway de webhook Meta→n8n:** workflow `pjD76QbrysJsYKz9`.
- **CAPI de Purchase:** enviado pelo backend do n8nCRM no pixel `871404632654375`.
- **PIX de recebimento:** CNPJ `65487517000100` — titular Patrick Borges Silva (Nubank).
- **Gerador de fotos IA (interno):** app Streamlit em `clientes/estudio-lumina/projetos/gerador-fotos-ia`
  (OpenAI gpt-image-2, modo batch/síncrono).

## Limitação conhecida — atribuição CTWA

- O número opera em **Coexistence** (Cloud API + app no celular, requisito da operação).
- Consequência: parte dos leads chega sem `ctwa_clid` (erro 131060), e essas vendas **não são
  atribuídas pelo Meta** — o painel subnotifica o ROAS. **Decisões usam o ROAS real (CRM/WhatsApp)**,
  não o do painel. Limitação aceita (não vamos sair do Coexistence). Detalhes no planejamento de tráfego.
