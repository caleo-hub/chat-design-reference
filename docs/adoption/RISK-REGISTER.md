# Registro de riscos

| ID | Risco | Prob. | Impacto | Mitigação de referência | Estado |
|---|---|---:|---:|---|---|
| R-01 | Framework de agentes contaminar o domínio | média | alto | porta `AgentRuntime`, adapters e import rules | aberto |
| R-02 | Webhook bloquear em LLM/tool | média | alto | persistir e responder 2xx/202 rapidamente | aberto |
| R-03 | Mensagem duplicada gerar efeito duplicado | alta | crítico | receipt idempotente, external ID e outbox | aberto |
| R-04 | Timeout após mutação deixar resultado desconhecido | média | crítico | estado `outcome_unknown`, reconciliação e sem replay cego | aberto |
| R-05 | Worker travado manter job indefinidamente | média | alto | lease renovável, heartbeat e watchdog | aberto |
| R-06 | Resposta perdida entre commit e provider | média | alto | transactional outbox e sender separado | aberto |
| R-07 | Prompt injection acionar tool indevida | alta | crítico | allowlist, escopo, validação e aprovação determinística | aberto |
| R-08 | Vazamento de PII em logs/traces | média | crítico | sanitização, IDs opacos e retenção explícita | aberto |
| R-09 | Identidade do canal ser confundida com identidade de negócio | média | alto | módulo identity e verificação por nível de confiança | aberto |
| R-10 | Mistura de tenants | baixa/média | crítico | tenant em toda chave, policy tests e autorização | aberto |
| R-11 | Cache/RAG desatualizado produzir decisão incorreta | média | alto | freshness, evidência, watermark e fallback seguro | aberto |
| R-12 | Retry storm degradar VPS e dependências | média | alto | backoff com jitter, circuit breaker e bulkheads | aberto |
| R-13 | Documentação divergir do código | alta | alto | fitness functions, contract tests e atualização no mesmo PR | aberto |
| R-14 | Template virar plataforma excessivamente abstrata | média | médio | portas apenas em fronteiras de variabilidade/efeito | aberto |
| R-15 | Uma VPS ser ponto único de falha | média | alto | backup, restore testado, health e limite explícito do perfil | aceito no MVP |
| R-16 | Dependência comprometida ou imagem mutável | baixa/média | crítico | lockfile, digest, scanning e SBOM | aberto |
| R-17 | Nudge duplicar ou contradizer resposta final | média | médio | nudge como job idempotente e cancelável | aberto |
| R-18 | Handoff existir no banco sem operador responsável | média | alto | estados claimed/SLA, alertas e console/runbook | aberto |
