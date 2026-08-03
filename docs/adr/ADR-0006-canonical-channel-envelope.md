# ADR-0006 — Envelope canônico de canal

- Status: proposto
- Data: 2026-08-03

## Contexto

WhatsApp, Teams e web possuem payloads, identidades e capacidades diferentes. Permitir que essas formas atravessem o sistema espalha condicionais e impede reutilização.

## Decisão

Normalizar entrada para `ChannelEnvelope` versionado e saída para `OutboundMessage`. Payload/provider metadata ficam isolados no adapter.

## Consequências

- orquestração independente do canal;
- segundo canal não duplica negócio;
- capability negotiation explícita;
- alguns recursos específicos exigem extensions namespaced;
- contract fixtures obrigatórios por adapter.

## Alternativas rejeitadas

- schema separado por canal dentro do domínio;
- usar telefone como identidade universal;
- fazer frontend web chamar diretamente o agent runtime.
