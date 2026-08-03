# Observabilidade, auditoria e evals

## Princípio

Telemetria explica execução; não substitui estado operacional. Sua falha não pode alterar o resultado do usuário.

## Correlação

Um correlation ID nasce na entrada e atravessa:

- receipt e message;
- turn e job attempts;
- LLM generations;
- tool calls/MCP;
- outbox e delivery events;
- handoff e audit events.

Trace/baggage não transporta secrets ou PII.

## Logs

JSON estruturado com campos allowlisted:

- timestamp, level, service role e instance;
- deployment SHA e environment;
- correlation/trace ID;
- tenant opaco;
- job/turn/outbox IDs;
- event type, status, duration e error code.

Não registrar por padrão:

- telefone/e-mail/CPF;
- conteúdo integral;
- token, headers ou URLs assinadas;
- prompt completo;
- tool payload sensível.

## Métricas técnicas

- requests/webhooks por resultado;
- fila: depth, oldest age, claim latency, expired leases;
- turns: duração, sucesso, timeout, cancelamento;
- LLM: latency, tokens, custo, erro e fallback;
- MCP/tools: calls, latency, status, breaker;
- outbox: backlog, attempts, delivery latency/status;
- DLQ/reconciliação/handoff abertos;
- heartbeat e readiness;
- CPU, memória, disco, conexões e backup age.

Evitar labels de alta cardinalidade como user ID ou conversation ID.

## Traces

OpenTelemetry é o padrão neutro para HTTP, fila, turn, LLM e tool spans. Um backend específico de LLM pode complementar com prompts/evals quando a política de dados permitir.

Spans recomendados:

```text
webhook.receive
inbox.enqueue
job.claim
turn.process
identity.resolve
agent.supervisor
agent.subflow
llm.generate
tool.call
outbox.enqueue
delivery.send
handoff.create
```

## Auditoria

Audit event é dado operacional versionado, não log comum. Registrar:

- quem/qual serviço;
- ação;
- objeto;
- decisão/policy;
- antes/depois sanitizado quando necessário;
- motivo;
- timestamp e correlation ID.

Ações de replay, aprovação, configuração e acesso privilegiado são auditadas.

## Evals

Cada projeto mantém dataset versionado com:

- happy paths;
- ambiguidades;
- prompt injection;
- falhas de dependência;
- handoff;
- loops e perguntas repetidas;
- invariantes transacionais.

Medidas:

- resolução e handoff;
- falsa afirmação de sucesso;
- tool trajectory;
- latência e custo;
- aderência a política;
- regressão entre prompt/modelo/grafo.

LLM-as-judge é sinal complementar, nunca única evidência para invariantes críticos.

## Dashboards e alertas

Alertar apenas quando existir ação definida. Painéis mínimos:

1. entrada e backlog;
2. turns/LLM/tools;
3. entrega por canal;
4. DLQ/reconciliação/handoff;
5. VPS/PostgreSQL/backup.
