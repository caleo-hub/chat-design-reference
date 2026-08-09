# Lifecycle mapping e review do workload

## Finalidade

Esta matriz transforma as best practices do AWS Generative AI Lens em uma revisão executável para chats e assistentes. O Appendix A oficial oferece uma sugestão de fase para parte das práticas; aqui todas as 51 práticas recebem uma fase primária adaptada e podem ser aplicadas em outras fases conforme risco.

## Escala de status

| Status | Critério |
|---|---|
| `atendida` | controle implantado, testado e com evidência operacional atual |
| `parcial` | desenho ou implementação incompleta; risco e plano registrados |
| `não atendida` | prática aplicável sem controle efetivo |
| `não aplicável` | justificativa aprovada, escopo e condição de reavaliação definidos |
| `não avaliado` | ainda sem owner ou evidência |

Uma documentação declaratória sem teste vale no máximo `parcial`.

## Processo de review

1. Defina workload, ambiente, tenants, canais, região, modelos, dados, tools e owners.
2. Selecione arquitetura-base e nível de maturidade.
3. Avalie cada linha com evidência linkável: código, teste, dashboard, relatório, policy, runbook ou ticket.
4. Registre risco, impacto, probabilidade, owner, prazo e compensating control.
5. Priorize high risk: perda/duplicidade, cross-tenant, mutação, outcome unknown, dados sensíveis, indisponibilidade e falsa afirmação de sucesso.
6. Gere backlog e aceite de risco proporcional.
7. Repita após mudança estrutural, incidente material, novo modelo/tool/fonte/tenant/região ou no ciclo periódico aprovado.

## Matriz completa

| Pilar | ID | Prática adaptada | Fase primária | Aplicação | Evidência esperada | Status | Owner / prazo |
|---|---|---|---|---|---|---|---|
| Excelência operacional | **GENOPS01-BP01** | Avaliar periodicamente o desempenho funcional | Melhoria contínua | MVP | Dataset dourado, relatório de avaliação, limiares aprovados, gate de release e vínculo com a versão implantada. | `não avaliado` |  |
| Excelência operacional | **GENOPS01-BP02** | Coletar e monitorar feedback de usuários | Melhoria contínua | MVP | Eventos de feedback, política de privacidade, taxonomia, painel de tendência e processo de fechamento do loop. | `não avaliado` |  |
| Excelência operacional | **GENOPS02-BP01** | Monitorar todas as camadas da aplicação | Implantação e operação | MVP | Métricas, logs e traces com correlation ID; dashboards por camada; alertas com ação e runbook. | `não avaliado` |  |
| Excelência operacional | **GENOPS02-BP02** | Monitorar métricas do foundation model | Implantação e operação | MVP | Painel por modelo/versão, alarmes de quota e degradação, amostragem de qualidade e política de retenção. | `não avaliado` |  |
| Excelência operacional | **GENOPS02-BP03** | Mitigar risco de sobrecarga | Escopo e implantação | MVP | Limites configurados, teste de carga, alarmes de fila/quotas, plano de fallback e evidência de recuperação. | `não avaliado` |  |
| Excelência operacional | **GENOPS03-BP01** | Gerenciar templates de prompt | Customização e desenvolvimento | MVP | Registro de prompt, hash/versão, revisão, testes, histórico e relação com deployment SHA. | `não avaliado` |  |
| Excelência operacional | **GENOPS03-BP02** | Habilitar tracing para agentes e RAG | Desenvolvimento e operação | MVP | Spans padronizados, redaction tests, amostra reproduzível e consulta ponta a ponta por correlation ID. | `não avaliado` |  |
| Excelência operacional | **GENOPS04-BP01** | Automatizar o ciclo de vida com IaC | Implantação e melhoria contínua | MVP | CDK, CloudFormation ou Terraform versionado; plano revisado; detecção de drift; rollback testado. | `não avaliado` |  |
| Excelência operacional | **GENOPS04-BP02** | Implementar GenAIOps | Implantação e melhoria contínua | Profissional | Pipelines, gates de qualidade/segurança/custo, registry de artefatos, promoção por ambiente e comparação de release. | `não avaliado` |  |
| Excelência operacional | **GENOPS05-BP01** | Saber quando customizar modelos | Seleção e customização | MVP | ADR/experimento com baseline, hipótese, dataset, ganho, custo total, riscos e critério de saída. | `não avaliado` |  |
| Segurança | **GENSEC01-BP01** | Menor privilégio nos endpoints de modelos | Implantação | MVP | Policies IAM testadas, deny explícito para rotas não permitidas, Access Analyzer e testes de autorização. | `não avaliado` |  |
| Segurança | **GENSEC01-BP02** | Comunicação privada entre aplicação e modelos | Implantação | MVP | Diagrama de rede, security groups, VPC endpoints quando aplicáveis, regras de egress e teste de conectividade. | `não avaliado` |  |
| Segurança | **GENSEC01-BP03** | Menor privilégio do modelo ao acessar dados | Desenvolvimento e implantação | MVP | Testes cross-tenant, políticas por fonte, consultas parametrizadas, trilha de autorização e fixtures negativas. | `não avaliado` |  |
| Segurança | **GENSEC01-BP04** | Monitorar acesso a serviços e modelos | Implantação e operação | MVP | CloudTrail e logs de aplicação, alertas de abuso/quota, painel por principal e processo de investigação. | `não avaliado` |  |
| Segurança | **GENSEC02-BP01** | Aplicar guardrails a respostas nocivas ou incorretas | Desenvolvimento e implantação | MVP | Política de entrada/saída, testes adversariais, thresholds, casos de bypass, fallback e handoff. | `não avaliado` |  |
| Segurança | **GENSEC03-BP01** | Monitorar plano de controle e acesso a dados | Implantação e operação | MVP | Audit events imutáveis, CloudTrail, Config ou equivalente, alertas de drift e segregação de funções. | `não avaliado` |  |
| Segurança | **GENSEC04-BP01** | Manter catálogo de prompts seguro | Customização e melhoria contínua | MVP | CODEOWNERS, revisão, secret scanning, artefato imutável, testes de integridade e rollback. | `não avaliado` |  |
| Segurança | **GENSEC04-BP02** | Sanitizar e validar entradas | Desenvolvimento e implantação | MVP | Schemas, limites, sandbox de mídia, allowlists, casos de prompt injection e testes de abuso. | `não avaliado` |  |
| Segurança | **GENSEC05-BP01** | Limitar agência e permissões de agentes | Customização e desenvolvimento | MVP | Tool policy, capability matrix, approvals, testes de tool abuse, trilha de decisão e cancelamento. | `não avaliado` |  |
| Segurança | **GENSEC06-BP01** | Purificar dados de treinamento ou customização | Customização e desenvolvimento | Condicional | Data card, scanners, quarentena, lineage, aprovação, versionamento e testes de poisoning. | `não avaliado` |  |
| Confiabilidade | **GENREL01-BP01** | Escalar throughput conforme utilização | Seleção e operação | MVP | Capacity test, quotas, autoscaling/concorrência, alarmes e limite operacional conhecido. | `não avaliado` |  |
| Confiabilidade | **GENREL02-BP01** | Redundância de rede entre endpoints e suporte | Desenvolvimento e implantação | MVP | Diagrama de falhas, teste de AZ, health checks, connection pooling e runbook de dependência. | `não avaliado` |  |
| Confiabilidade | **GENREL03-BP01** | Gerenciar fluxos de prompt e recuperar de falhas | Desenvolvimento e implantação | MVP | State diagram, testes de crash/retry, DLQ, reconciliação e invariantes da outbox. | `não avaliado` |  |
| Confiabilidade | **GENREL03-BP02** | Aplicar timeouts em workflows agentic | Desenvolvimento e implantação | MVP | Configuração de deadlines, testes de timeout/cancelamento, heartbeat e execução resumível. | `não avaliado` |  |
| Confiabilidade | **GENREL04-BP01** | Implementar catálogo de prompts | Desenvolvimento e melhoria contínua | MVP | Catálogo, matriz de compatibilidade, release context, teste de rollback e retenção de versões. | `não avaliado` |  |
| Confiabilidade | **GENREL04-BP02** | Implementar catálogo de modelos | Seleção e melhoria contínua | MVP | Model registry/catalog, health, policy de routing, contrato de fallback e testes de compatibilidade. | `não avaliado` |  |
| Confiabilidade | **GENREL05-BP01** | Distribuir inferência entre regiões | Seleção e implantação | Profissional | ADR multi-Region, health/routing, teste de failover, quotas e evidência de equivalência. | `não avaliado` |  |
| Confiabilidade | **GENREL05-BP02** | Replicar dados de embeddings entre regiões | Implantação | Profissional | Manifesto do índice, pipeline de rebuild/replicação, RPO/RTO, teste de restore e métricas de freshness. | `não avaliado` |  |
| Confiabilidade | **GENREL05-BP03** | Verificar capacidades do agente em todas as regiões | Implantação | Profissional | Capability matrix regional, teste sintético ponta a ponta, runbook e comportamento de degradação. | `não avaliado` |  |
| Confiabilidade | **GENREL06-BP01** | Tolerância a falhas em computação distribuída | Customização e implantação | Condicional | Job graph, checkpoints, manifestos, testes de worker loss, partial results e reconciliação. | `não avaliado` |  |
| Eficiência de desempenho | **GENPERF01-BP01** | Definir dataset de ground truth de prompts e respostas | Customização e desenvolvimento | MVP | Dataset versionado, rubric, coverage report, provenance e baseline de release. | `não avaliado` |  |
| Eficiência de desempenho | **GENPERF01-BP02** | Coletar métricas de desempenho | Escopo e operação | MVP | SLOs, histogramas, traces, painel por etapa e análise de percentis. | `não avaliado` |  |
| Eficiência de desempenho | **GENPERF02-BP01** | Testar carga nos endpoints de modelo | Desenvolvimento | MVP | Plano de carga, dados sintéticos seguros, resultados p50/p95/p99 e capacidade aprovada. | `não avaliado` |  |
| Eficiência de desempenho | **GENPERF02-BP02** | Otimizar parâmetros de inferência | Desenvolvimento | MVP | Experimentos, matriz por intenção, parâmetros versionados e guardrails de configuração. | `não avaliado` |  |
| Eficiência de desempenho | **GENPERF02-BP03** | Selecionar e customizar o modelo adequado | Seleção | MVP | Scorecard, benchmark por intenção, decisão de routing e critérios de fallback. | `não avaliado` |  |
| Eficiência de desempenho | **GENPERF03-BP01** | Usar soluções gerenciadas quando apropriado | Customização e desenvolvimento | MVP | ADR buy/build, benchmark, SLO, custos e plano de saída ou abstração por adapter. | `não avaliado` |  |
| Eficiência de desempenho | **GENPERF04-BP01** | Testar embeddings por latência e relevância | Desenvolvimento e melhoria contínua | MVP | Benchmark de retrieval, dataset de queries, métricas, análise de erro e versão do índice. | `não avaliado` |  |
| Eficiência de desempenho | **GENPERF04-BP02** | Otimizar dimensão dos vetores | Desenvolvimento | Profissional | Teste de dimensão, plano de migração/reindexação, métricas de qualidade e custo. | `não avaliado` |  |
| Otimização de custos | **GENCOST01-BP01** | Dimensionar a seleção do modelo | Seleção | MVP | Benchmark de qualidade-custo-latência, policy de routing, custo por turn resolvido e revisão periódica. | `não avaliado` |  |
| Otimização de custos | **GENCOST02-BP01** | Equilibrar custo e desempenho dos paradigmas de inferência | Escopo e seleção | MVP | Modelo de demanda, análise de break-even, SLO, decisão aprovada e gatilho de revisão. | `não avaliado` |  |
| Otimização de custos | **GENCOST02-BP02** | Otimizar recursos e hosting | Desenvolvimento e operação | MVP | Relatório de utilização, autoscaling, budgets, tagging e custo por papel/tenant. | `não avaliado` |  |
| Otimização de custos | **GENCOST03-BP01** | Otimizar tamanho do prompt | Desenvolvimento e melhoria contínua | MVP | Métrica de input tokens, testes de qualidade após compressão e limite por fluxo. | `não avaliado` |  |
| Otimização de custos | **GENCOST03-BP02** | Controlar tamanho da resposta | Desenvolvimento | MVP | Métrica de output tokens, templates de resposta, testes de truncamento e UX. | `não avaliado` |  |
| Otimização de custos | **GENCOST03-BP03** | Usar prompt caching | Implantação | Condicional | Design de cache, chaves/versionamento, métricas de hit, testes de isolamento e invalidação. | `não avaliado` |  |
| Otimização de custos | **GENCOST03-BP04** | Anotar entrada para filtragem consciente de custo | Desenvolvimento e melhoria contínua | MVP | Classificador/rules, quotas, explainability de routing, métricas de economia e false routing. | `não avaliado` |  |
| Otimização de custos | **GENCOST04-BP01** | Reduzir comprimento/dimensão de vetores | Implantação | Profissional | Benchmark de dimensão, custo do índice, política de retenção e plano de reindexação. | `não avaliado` |  |
| Otimização de custos | **GENCOST05-BP01** | Criar condições de parada para workflows longos | Desenvolvimento e implantação | MVP | Budgets no TurnRequest, stop reasons, testes de loop, alertas e relatório de custo por trajetória. | `não avaliado` |  |
| Sustentabilidade | **GENSUS01-BP01** | Usar autoscaling e serverless para otimizar recursos | Escopo e implantação | MVP | Utilização, política de escala, teste de cold start, capacidade mínima e custo/energia como proxy. | `não avaliado` |  |
| Sustentabilidade | **GENSUS01-BP02** | Usar serviços eficientes de customização | Escopo e customização | Condicional | ADR de customização, duração/recursos do job, checkpoint, limpeza automática e ganho medido. | `não avaliado` |  |
| Sustentabilidade | **GENSUS02-BP01** | Otimizar processamento e armazenamento de dados | Customização e operação | MVP | Data lifecycle, métricas de bytes/processamento, lineage, políticas de retenção e teste de delete. | `não avaliado` |  |
| Sustentabilidade | **GENSUS03-BP01** | Usar modelos menores e inferência otimizada | Desenvolvimento e melhoria contínua | MVP | Benchmark Pareto, policy de routing, utilização, tokens por resultado útil e revisão de modelo. | `não avaliado` |  |

## Gates por fase

### Scoping

- hipótese e métrica de valor;
- alternativa sem GenAI considerada;
- risco e Responsible AI;
- data map e classificação;
- nível de agência;
- SLO e budget inicial;
- exit criteria da POC.

### Model selection

- benchmark representativo;
- model catalog e data policy;
- routing/fallback;
- região, quota e disponibilidade;
- qualidade, latência, custo e segurança aprovados.

### Model customization

- baseline e necessidade comprovada;
- prompt/RAG avaliados antes de treino;
- dataset/data card e lineage;
- eval e bias/safety tests;
- versão, rollback e custo de manutenção.

### Development and integration

- contratos, schemas e ports;
- state machine, tools, approvals e handoff;
- idempotência, timeout, cancelamento e reconciliação;
- RAG autorizado e citations;
- contract, concurrency, security e fault tests.

### Deployment

- IaC, CI/CD e artifact digest;
- secrets, rede e IAM;
- migrations, backup/restore e rollback;
- readiness, dashboards, alarms e runbooks;
- load/capacity test e rollout gradual.

### Continuous improvement

- feedback e eval recorrentes;
- release comparison;
- incident/postmortem loop;
- freshness/drift e depreciação;
- custo por resultado e sustainability review;
- revisão do Lens e aceite de risco.

## Evidências canônicas neste repositório

| Tema | Fonte principal |
|---|---|
| princípios e invariantes | `specs/constitution.md` |
| contexto, containers e módulos | `docs/architecture/` |
| runtime e jobs | `docs/architecture/runtime.md` |
| dados e estado | `docs/architecture/data-and-state.md` |
| falhas | `docs/architecture/failure-model.md` |
| observabilidade e evals | `docs/architecture/observability.md` |
| segurança | `docs/security/threat-model.md` |
| perfil AWS | `docs/architecture/deployment-aws.md` |
| contratos | `contracts/` |
| operação | `docs/runbooks/` |
| perfil derivado | `config/<projeto>.yaml` |

## Resultado do review

Use este resumo no PR ou documento de arquitetura:

```text
Workload / ambiente:
Data da revisão:
Reviewers:
Arquitetura-base:
Nível de agência:
Modelos e regiões:
Dados e classificação:
Tools/mutações:

Atendidas: __ / 51
Parciais: __ / 51
Não atendidas: __ / 51
Não aplicáveis: __ / 51

Riscos críticos:
1.
2.
3.

Ações, owners e prazos:
1.
2.
3.

Próxima revisão:
```
