# Runbook — Adicionar MCP server

1. Nomear owner e finalidade.
2. Fixar versão da spec/SDK suportada.
3. Definir transport e autenticação; HTTP nunca fica anônimo em produção.
4. Listar tools/resources/prompts necessários.
5. Aplicar allowlist por agent/subagent scope.
6. Escrever schemas e exemplos de resultado.
7. Classificar cada tool: read/mutate/destructive.
8. Definir idempotency key, pós-condição e reconciliação.
9. Configurar timeout, rate limit, bulkhead e breaker.
10. Redigir campos sensíveis em logs/traces.
11. Criar mock e contract tests produtor/consumidor.
12. Testar timeout antes/depois do efeito e server comprometido.
13. Fazer rollout mock → ambiente controlado → real.

Gate: nenhuma mutação real pode ser exposta diretamente ao LLM sem policy e guardas correspondentes.
