# Runtime, filas e experiência temporal

## Fluxo de entrada e resposta

```mermaid
sequenceDiagram
    participant U as Usuário
    participant C as Canal
    participant API as Webhook/API
    participant DB as PostgreSQL
    participant W as Worker
    participant O as Orchestrator
    participant T as Tool Gateway
    participant S as Sender

    U->>C: mensagem
    C->>API: webhook
    API->>API: autentica + normaliza
    API->>DB: receipt + inbox idempotentes
    API-->>C: 2xx/202
    W->>DB: claim com lease
    W->>O: TurnRequest
    O->>T: tool call opcional
    T-->>O: ToolResult estruturado
    O-->>W: TurnResult
    W->>DB: estado + OutboxEvent (uma transação)
    S->>DB: claim outbox
    S->>C: entrega
    S->>DB: accepted/provider_id
    C-->>U: resposta
```

## Estados do job

```mermaid
stateDiagram-v2
    [*] --> queued
    queued --> processing: claim
    processing --> waiting_tool: tarefa longa
    processing --> waiting_human: aprovação/handoff
    processing --> completed: estado + outbox
    processing --> retry_scheduled: falha conhecida
    retry_scheduled --> queued
    processing --> reconciliation_required: resultado externo desconhecido
    processing --> cancelled: cancelamento seguro
    processing --> dead_letter: tentativas excedidas
    waiting_tool --> queued: resultado disponível
    waiting_human --> queued: decisão humana
    reconciliation_required --> queued: reconciliado sem efeito
    reconciliation_required --> completed: efeito confirmado
```

## Claim, lease e ordenação

- `FOR UPDATE SKIP LOCKED` permite múltiplos workers;
- somente um turn por `(tenant_id, conversation_id)` fica em processamento;
- claim define `locked_by` e `lease_until`;
- job longo renova lease em intervalo menor que metade do lease;
- atualização exige ownership do worker;
- lease expirado é avaliado pelo watchdog;
- job com possível efeito externo não é simplesmente reenfileirado.

## Heartbeat

Cada papel grava:

- service/role;
- instance ID único;
- started/last_seen;
- build SHA;
- current job opcional;
- readiness resumida.

Containers possuem healthcheck, mas heartbeat permite detectar processo vivo e loop travado.

## Watchdog

Procura:

- heartbeat vencido;
- lease expirado;
- backlog/idade da fila;
- outbox antiga;
- nudge pendente;
- handoff sem claim;
- cache/knowledge stale;
- DLQ e reconciliação abertas;
- jobs excedendo deadline.

Ações são idempotentes e auditadas.

## Nudge

Nudge é um job associado ao turn:

1. agendado ao iniciar processamento;
2. cancelado quando resposta fica durável;
3. enviado no máximo uma vez por estágio;
4. adaptado ao canal;
5. nunca afirma sucesso transacional;
6. pode dizer “consultando dados” ou “demorando mais que o normal”.

## Timeout e cancelamento

- deadline global do turn;
- timeout por LLM/tool/mídia/provider;
- `cancel_requested_at` consultado entre etapas;
- chamada cancelável recebe cancel token;
- mutação já iniciada pode exigir reconciliação, não cancelamento fictício;
- resposta final distingue cancelado, não iniciado e resultado desconhecido.

## Long-running tasks

Processamento longo sai do worker principal:

- cria `background_task` durável;
- tool adapter inicia operação;
- scheduler/worker especializado acompanha progresso;
- progresso gera eventos/nudges;
- conclusão reenfileira o turn ou cria outbox;
- polling usa backoff e deadline;
- callback/webhook é deduplicado.

## Debounce e agrupamento

Mensagens textuais consecutivas podem ser agrupadas por janela curta. Mídia ou comando de cancelamento força flush. O receipt original é preservado para auditoria.
