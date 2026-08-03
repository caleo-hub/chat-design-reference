# ADR-0005 — Transactional outbox para toda mensagem de negócio

- Status: proposto
- Data: 2026-08-03

## Contexto

Enviar ao canal antes ou depois do commit cria janelas de perda ou duplicidade. Não existe transação distribuída com providers.

## Decisão

Persistir estado final do turn e `OutboxEvent` na mesma transação. Um sender separado entrega e registra status do provider.

## Consequências

- crash é recuperável;
- retry de entrega centralizado;
- sender pode escalar por canal;
- entrega é ao menos uma vez e exige `delivery_key` idempotente;
- aceite não equivale a entrega/leitura.

## Exceções

Typing/presence efêmeros podem ser enviados diretamente, pois não representam efeito de negócio e não exigem garantia.

## Alternativas rejeitadas

- worker enviar e depois persistir;
- persistir e enviar no mesmo processo sem outbox;
- considerar HTTP 2xx do provider como delivery final.
