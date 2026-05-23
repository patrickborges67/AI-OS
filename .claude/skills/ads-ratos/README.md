# Ads Ratos

Inteligencia de trafego pago para agentes de IA. Diagnostico, relatorio, auditoria e estrategia para Meta Ads, Google Ads e GA4 com benchmarks do mercado brasileiro.

## Instalacao

Esta copia local fica em `.claude/skills/ads-ratos/`.


## Pre-requisitos

Precisa de pelo menos uma skill de execucao instalada. Neste workspace, as skills internas ja estao em:

- **Meta Ads**: `.claude/skills/meta-ads-ratos`
- **Google Ads**: `.claude/skills/google-ads-ratos`
- **GA4**: `.claude/skills/ga4-ratos`

## Setup

```
/ads-ratos setup
```

Guia o cadastro de contas e testa conexoes.

## Comandos

| Comando | O que faz | Quando usar |
|---|---|---|
| `/ads-ratos setup` | Configura contas e testa conexoes | Primeira vez |
| `/ads-ratos diagnostico` | Health Score + KPIs + alertas automaticos | Check diario (5 min) |
| `/ads-ratos relatorio` | Dashboard HTML com benchmarks BR | Entrega pro cliente |
| `/ads-ratos auditoria` | Analise profunda com Quality Gates | Revisao mensal |

## O que esta incluso

- **Benchmarks BR**: metricas de referencia do mercado brasileiro por nicho
- **Quality Gates**: regras de decisao (3x Kill Rule, limites de escala, bidding)
- **Health Score**: nota 0-100 da conta com classificacao A-F
- **Alertas automaticos**: deteccao de problemas com numeros e acoes
- **Referencia Pedro Sobral**: instrucoes de criativos, segmentacao e testes para campanhas

## Arquitetura

```
ads-ratos (cerebro - estrategia + inteligencia)
  |-- referencia -> .claude/skills/meta-ads-ratos (execucao Meta)
  |-- referencia -> .claude/skills/google-ads-ratos (execucao Google)
  `-- referencia -> .claude/skills/ga4-ratos (execucao Analytics)
```

## Licenca

MIT - [Ratos de IA](https://ratosdeia.com.br)
