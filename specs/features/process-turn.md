# Feature — Processar turn

## Objetivo

Converter uma mensagem persistida em resultado conversacional e efeitos controlados, preservando ordem, lease, estado e verdade transacional.

## Pré-condições

- job `queued` e disponível;
- nenhum turn anterior da mesma conversa está ativo;
- worker ready e configurado.

## Invariantes

- somente owner do lease conclui/reagenda;
- lease é renovado durante processamento longo;
- no máximo um turn por conversa é processado;
- tool mutation usa idempotency key;
- resposta final não declara efeito sem pós-condição confirmada;
- estado + outbox são atômicos;
- telemetria pode falhar sem mudar resultado.

## Etapas

1. claim;
2. preprocessamento e política de mídia;
3. resolução de identity/session;
4. carregamento de estado e memória permitida;
5. catálogo de tools filtrado;
6. Supervisor/Subagente via `AgentRuntime`;
7. validação de `TurnResult` e pós-condições;
8. estado + audit + outbox numa transação;
9. job `completed`.

## Falhas e transições

- erro transitório conhecido → `retry_scheduled`;
- limite excedido → fallback/handoff;
- cancelamento antes de mutação → `cancelled`;
- timeout após possível mutação → `reconciliation_required`;
- bug/invariante → `dead_letter` e alerta;
- human approval → `waiting_human`.

## Critérios de aceitação

- crash antes do commit permite retry sem resposta duplicada;
- crash depois do commit mantém uma outbox recuperável;
- confirmação crítica não pode alcançar mutação por rota alternativa;
- worker sem lease não altera job;
- histórico de outra conversa/tenant não entra no contexto;
- budgets interrompem loop de agente.
