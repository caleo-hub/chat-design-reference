# Níveis de maturidade: POC, MVP e Profissional

## POC

Objetivo: validar valor e fluxo, sem mascarar riscos.

Obrigatório:

- um canal/adaptador;
- envelope canônico;
- uma spec de agente/fluxo;
- ambiente local reproduzível;
- mock de tools;
- logs básicos com correlation ID;
- nenhum efeito irreversível real sem aprovação;
- decisão explícita sobre descarte ou evolução.

Pode simplificar:

- fila em memória apenas se a POC for descartável e sem webhook real;
- um processo;
- sem RAG ou memória durável;
- sem console.

Gate para evoluir: hipótese validada e riscos do uso real mapeados.

## MVP

Objetivo: uso real controlado numa VPS.

Obrigatório:

- webhook autenticado e rápido;
- PostgreSQL inbox/queue com dedupe, lease e ordenação;
- worker separado;
- transactional outbox e sender;
- retries, DLQ e reconciliação;
- heartbeat, watchdog, timeout e cancelamento cooperativo;
- typing/nudge;
- sessões e estado duráveis;
- Supervisor/Subagentes com guardas determinísticas;
- MCP/tool gateway autenticado e allowlisted;
- human handoff estruturado;
- logs/métricas/traces sanitizados;
- live/ready/dependency health;
- CI, imagens imutáveis, secrets, backup/restore e rollback;
- contract, concurrency e fault tests;
- SLO/capacidade inicial medidos.

## Profissional

Objetivo: operação contínua, expansão e governança.

Adicionar conforme necessidade:

- múltiplos canais e capability negotiation;
- multitenancy com isolamento testado;
- console operacional completo;
- approvals/resume persistentes;
- circuit breakers e bulkheads por dependência;
- tasks longas com progresso;
- eval datasets, prompt registry e release comparison;
- feature flags e progressive delivery;
- OTel collector e observabilidade integrada;
- retenção/exclusão automatizadas;
- SBOM, scanning e assinatura de imagens;
- capacity tests e autoscaling por papel;
- replica/HA ou segunda VPS quando SLO exigir;
- disaster recovery com RPO/RTO;
- testes de caos recorrentes;
- compliance e segregação de funções.

## Matriz de componentes

| Componente | POC | MVP | Profissional |
|---|---:|---:|---:|
| envelope/adapters | mínimo | obrigatório | múltiplos + capabilities |
| fila | opcional descartável | PostgreSQL durável | broker se medição justificar |
| outbox | mock | obrigatório | multi-provider/reconciliação |
| heartbeat/watchdog | não | obrigatório | automação e alertas avançados |
| nudge/cancelamento | simples | obrigatório | progresso rico/tasks |
| MCP | mock | auth + allowlist | OAuth/scopes/compatibilidade |
| memória | sessão | sessão + durável curada | políticas/consentimento avançados |
| handoff | manual | estruturado | console/SLA/claim/resume |
| observabilidade | logs | métricas/traces/dashboards | evals/SLO/error budget |
| deploy | local | Compose/VPS | HA/progressive/DR |
