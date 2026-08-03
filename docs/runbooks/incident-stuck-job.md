# Incidente — Mensagem ou job travado

## Sinais

- usuário sem resposta;
- `queue_oldest_age` acima do SLO;
- job `processing` com lease expirado;
- heartbeat ausente;
- outbox antiga;
- nudge enviado sem conclusão.

## Triagem

1. localizar por correlation ID, conversation ou provider ID;
2. verificar receipt/inbox/job attempts;
3. confirmar `locked_by`, lease e heartbeat;
4. verificar LLM/tool spans e breaker;
5. verificar estado do turn e outbox;
6. determinar se houve possível efeito externo.

## Decisão

### Sem efeito externo iniciado

- liberar/reagendar job de forma auditada;
- corrigir causa;
- acompanhar conclusão.

### Efeito conhecido como falho

- retry conforme policy/idempotência.

### Resultado desconhecido

- marcar/reter `reconciliation_required`;
- consultar sistema externo por idempotency/effect reference;
- nunca reenviar mutação cegamente;
- concluir ou reabrir somente após evidência.

### Resposta durável, entrega pendente

- investigar outbox/sender/provider;
- replay da outbox apenas se policy permitir;
- correlacionar delivery events.

## Comunicação

Enviar mensagem ao usuário somente pela outbox, sem prometer resultado não confirmado.

## Pós-incidente

- registrar timeline e causa;
- adicionar teste/fault injection apropriado;
- atualizar runbook/métrica/alerta, não apenas prompt;
- revisar lease, timeout, breaker e capacidade.
