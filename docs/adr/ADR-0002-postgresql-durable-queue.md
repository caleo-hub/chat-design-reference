# ADR-0002 — PostgreSQL como fila durável inicial

- Status: proposto
- Data: 2026-08-03

## Contexto

O MVP precisa de inbox, ordenação, lease, retry, DLQ, outbox e auditoria numa VPS, sem operar broker adicional.

## Decisão

Usar tabelas PostgreSQL e claims transacionais com `FOR UPDATE SKIP LOCKED` como backend padrão de jobs.

## Consequências

- uma fonte operacional e backup;
- sem Redis/RabbitMQ obrigatório;
- idempotência e estado próximos;
- throughput limitado pelo banco e polling;
- exige índices, retenção e medição de contenção.

## Limite de validade

Reavaliar quando métricas demonstrarem que o banco não sustenta throughput, latência, fan-out ou isolamento necessários. Migração para broker requer preservar contracts, idempotência, ordering, DLQ e observabilidade.

## Alternativas rejeitadas

- fila em memória para MVP: perde jobs em restart;
- Celery/Redis como default: nova operação sem necessidade comprovada;
- Kafka: complexidade incompatível com o estágio.
