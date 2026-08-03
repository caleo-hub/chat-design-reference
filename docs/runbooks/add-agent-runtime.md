# Runbook — Adicionar ou trocar agent runtime

1. Fixar versão e revisar licença/manutenção.
2. Mapear `TurnRequest` para o framework.
3. Mapear resultado para `TurnResult` sem exceções cruas.
4. Isolar checkpoints/store específicos.
5. Integrar tool catalog filtrado, não discovery irrestrito.
6. Propagar correlation, deadline e cancelamento.
7. Registrar prompt/model/graph/crew versions.
8. Implementar stub/fakes para testes.
9. Executar eval baseline e fault tests.
10. Fazer rollout por feature flag e manter rollback.

Gate: remover o adapter não exige alterar inbox, outbox, channel envelope, tool taxonomy ou handoff.
