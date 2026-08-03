# Runbook — Operar na VPS

## Verificação diária

- containers e health;
- idade da inbox/outbox;
- heartbeats e leases expirados;
- DLQ/reconciliação/handoff;
- PostgreSQL connections/size;
- CPU, memória, disco e swap;
- backup age e monitor externo;
- erros/circuit breakers de LLM, MCP e canais.

## Deploy

1. registrar versão atual;
2. confirmar backup/restore point;
3. baixar imagem por digest;
4. validar Compose/config sem revelar secrets;
5. executar migration job;
6. atualizar API/worker/sender/scheduler;
7. verificar live/ready/dependencies;
8. executar fluxo sintético;
9. observar SLOs e fila;
10. registrar conclusão.

## Rollback

- parar rollout;
- voltar digest anterior compatível;
- não reverter migration destrutiva sem plano;
- reconciliar jobs/efeitos desconhecidos;
- executar smoke e registrar incidente.

## Backup

- gerar cópia fora da VPS;
- validar tamanho/checksum;
- restaurar periodicamente em banco vazio;
- registrar RPO/RTO observado;
- testar acesso e descarte.

## Secrets

- rotação por integração;
- overlap quando provider permitir;
- restart controlado;
- validar chamadas;
- revogar antigo;
- auditar sem registrar valor.
