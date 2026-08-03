# Subagente — <nome>

## Owner e versão

- Owner:
- Prompt version:
- Flow version:
- Risk class:

## Objetivo

<resultado específico>

## Não objetivos

- ...

## Estado

| Campo | Tipo | Fonte | Obrigatório | Sensível |
|---|---|---|---:|---:|
| | | | | |

## Estados e transições

```text
start → ... → completed
           ↘ waiting_user
           ↘ waiting_human
           ↘ reconciliation_required
```

## Tools permitidas

| Tool/scope | Classe | Idempotência | Aprovação | Pós-condição |
|---|---|---|---|---|
| | read/mutate/destructive | | | |

## Regras determinísticas

- ...

## Prompt/LLM é usado para

- extração/classificação/formulação...

## Handoff

- motivos;
- resumo necessário;
- continuidade após decisão.

## Budgets

- tempo;
- tools;
- loops;
- tokens/custo.

## Critérios e evals

- happy path;
- dados faltantes;
- ambiguidade;
- duplicidade;
- falha parcial;
- prompt injection;
- cancelamento.
