# Feature — Tarefa longa, heartbeat, nudge e cancelamento

## Objetivo

Executar operações que ultrapassam o tempo de um turn normal sem prender worker, perder progresso ou deixar o usuário sem retorno.

## Fluxo

1. turn cria `background_task` com deadline;
2. worker especializado inicia/acompanha;
3. heartbeat/progress é persistido;
4. nudge pode ser enfileirado;
5. callback ou polling atualiza estado idempotentemente;
6. conclusão reenfileira continuação ou cria outbox;
7. timeout/cancelamento segue policy.

## Invariantes

- task ID é durável;
- progresso não é conclusão;
- nudge é único por estágio e cancelado após finalização;
- cancelamento é cooperativo e não falsifica reversão;
- callback duplicado não duplica continuação;
- task sem heartbeat entra em watchdog;
- resultado desconhecido exige reconciliação.

## Critérios de aceitação

- worker de turn fica livre após agendamento;
- usuário recebe no máximo os nudges configurados;
- task finalizada não envia nudge tardio;
- cancelamento antes do efeito impede início;
- cancelamento após mutação retorna estado correto;
- restart da VPS preserva task e continuidade.
