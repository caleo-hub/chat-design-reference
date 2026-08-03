# Runbook — Criar um novo chat a partir da referência

## 1. Abrir iniciativa

- nomear owner, tech lead, segurança/operação;
- descrever problema sem tecnologia;
- escolher perfil POC/MVP/Profissional;
- classificar dados e ações;
- registrar escopo, não objetivos e riscos.

## 2. Instanciar perfil

```bash
cp config/reference.example.yaml config/<projeto>.yaml
```

Resolver todos os `define-me`. Não usar defaults silenciosos para dados, auth ou secrets.

## 3. Especificar canais

Para cada canal:

- provider e contrato de webhook;
- autenticação/replay;
- identidade;
- capabilities;
- limites de mídia;
- delivery events;
- mock/fixtures.

Use [Adicionar canal](add-channel.md).

## 4. Especificar agentes

- supervisor;
- subagentes/fluxos;
- estados, guardas e critérios;
- tools e scopes;
- handoff/approval;
- budgets e evals.

Não comece apenas pelo system prompt.

## 5. Escolher agent runtime

Implementar `AgentRuntime` adapter. Registre ADR se a escolha afetar operação/estado. Use [Adicionar runtime](add-agent-runtime.md).

## 6. Configurar MCP/tools

- owner e auth;
- allowlist por scope;
- schemas;
- idempotência e reconciliação;
- mocks/contract tests;
- dados e retenção.

Use [Adicionar MCP](add-mcp.md).

## 7. Primeira fatia vertical

Ordem recomendada:

1. canal web/test adapter;
2. envelope + receipt/inbox PostgreSQL;
3. worker + runtime stub;
4. outbox + sender de teste;
5. health/metrics;
6. fault tests;
7. somente depois LLM/MCP real.

## 8. Gates do MVP

- duplicate/retry/crash tests;
- lease/heartbeat/watchdog;
- outbox;
- handoff;
- PII redaction;
- backup/restore;
- deploy/rollback;
- capacidade e SLO;
- security review.

## 9. Deploy controlado

- imagem por SHA/digest;
- secrets fora do repo;
- migration explícita;
- smoke sintético;
- janela de observação;
- rollback preparado.

## 10. Aprender

Atualize specs, ADRs, evals e runbooks a partir do piloto. Não resolva incidente apenas adicionando frase ao prompt.
