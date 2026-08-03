# ADR-0001 — Monólito modular como estilo padrão

- Status: proposto
- Data: 2026-08-03

## Contexto

O template precisa servir a vários chats, ser operável por equipes pequenas e rodar em VPS. Microsserviços adicionariam rede, deploys, observabilidade e consistência antes de existir necessidade comprovada.

## Decisão

Usar monólito modular: um repositório, domínio e artefato, com módulos e dependências verificáveis. O mesmo artefato pode rodar em processos API/worker/sender/scheduler.

## Consequências

Positivas:

- menor custo operacional;
- transações locais para inbox/outbox;
- evolução rápida do domínio;
- deploy/rollback simples;
- possibilidade de escalar papéis separadamente.

Negativas:

- banco e release compartilhados;
- disciplina necessária para evitar acesso interno arbitrário;
- falha da VPS afeta todos os papéis.

## Alternativas rejeitadas

- processo único: reduz isolamento e capacidade operacional;
- microsserviços por módulo: custo prematuro;
- serverless/cloud gerenciado: viola a restrição base e aumenta lock-in.

## Fitness functions

Import rules, APIs de módulo, migrations revisadas e proibição de tabelas privadas cruzadas.
