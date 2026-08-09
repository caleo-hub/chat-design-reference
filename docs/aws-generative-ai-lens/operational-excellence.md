# Pilar: Excelência operacional

## Intenção

Operar chats e assistentes como sistemas sociotécnicos: qualidade probabilística, estado durável, feedback humano, mudanças versionadas e recuperação verificável.

Esta adaptação preserva as invariantes de [Constituição](../../specs/constitution.md), [runtime](../architecture/runtime.md), [dados e estado](../architecture/data-and-state.md) e [excelência operacional existente](../architecture/observability.md). Os IDs abaixo mantêm rastreabilidade com o AWS Well-Architected Generative AI Lens; o texto e os controles foram reescritos para o cenário deste repositório.

## Práticas adaptadas

| ID | Adaptação para chats/assistentes | Evidência mínima | Fase principal | Gate |
|---|---|---|---|---|
| **GENOPS01-BP01**<br>Avaliar periodicamente o desempenho funcional | Manter conjuntos de avaliação versionados por intenção, canal, idioma, risco e perfil de usuário; comparar prompt, modelo, grafo e RAG antes e depois de cada mudança; bloquear promoção quando uma invariante crítica regredir. | Dataset dourado, relatório de avaliação, limiares aprovados, gate de release e vínculo com a versão implantada. | Melhoria contínua | MVP |
| **GENOPS01-BP02**<br>Coletar e monitorar feedback de usuários | Coletar feedback explícito e sinais operacionais sem confundir satisfação com correção. Separar opinião, falha funcional, conteúdo inseguro, ausência de fonte e erro de ferramenta; encaminhar sinais para triagem humana e backlog. | Eventos de feedback, política de privacidade, taxonomia, painel de tendência e processo de fechamento do loop. | Melhoria contínua | MVP |
| **GENOPS02-BP01**<br>Monitorar todas as camadas da aplicação | Observar edge, webhook, inbox, fila, worker, orquestração, LLM, RAG, tools, outbox, sender, canal, handoff e banco. A mesma correlação deve atravessar o turn inteiro. | Métricas, logs e traces com correlation ID; dashboards por camada; alertas com ação e runbook. | Implantação e operação | MVP |
| **GENOPS02-BP02**<br>Monitorar métricas do foundation model | Acompanhar latência, tokens, custo estimado, erros, throttling, recusas, guardrails, qualidade amostral, fallback e distribuição por versão do modelo. Não usar PII como label. | Painel por modelo/versão, alarmes de quota e degradação, amostragem de qualidade e política de retenção. | Implantação e operação | MVP |
| **GENOPS02-BP03**<br>Mitigar risco de sobrecarga | Aplicar admissão, rate limit por tenant/canal, budgets, backpressure, limites de concorrência, filas duráveis e degradação segura. Escalar workers e capacidade de inferência apenas com base em backlog, idade e utilização medidos. | Limites configurados, teste de carga, alarmes de fila/quotas, plano de fallback e evidência de recuperação. | Escopo e implantação | MVP |
| **GENOPS03-BP01**<br>Gerenciar templates de prompt | Usar catálogo com owner, finalidade, variáveis tipadas, classificação de dados, testes, versão imutável e rollback. O prompt implantado deve ser identificável em cada turn. | Registro de prompt, hash/versão, revisão, testes, histórico e relação com deployment SHA. | Customização e desenvolvimento | MVP |
| **GENOPS03-BP02**<br>Habilitar tracing para agentes e RAG | Registrar trajetória sanitizada: decisão do supervisor, subfluxo, chamadas de modelo, documentos recuperados, filtros, reranking, tools e pós-condições. O trace explica a execução, mas não é fonte do estado operacional. | Spans padronizados, redaction tests, amostra reproduzível e consulta ponta a ponta por correlation ID. | Desenvolvimento e operação | MVP |
| **GENOPS04-BP01**<br>Automatizar o ciclo de vida com IaC | Versionar rede, compute, banco, permissões, alarmes, secrets references, políticas e recursos de IA. Ambientes devem ser reproduzíveis e mudanças destrutivas devem ter plano de migração e rollback. | CDK, CloudFormation ou Terraform versionado; plano revisado; detecção de drift; rollback testado. | Implantação e melhoria contínua | MVP |
| **GENOPS04-BP02**<br>Implementar GenAIOps | Tratar aplicação, prompt, modelo, knowledge base, catálogo de tools e datasets de avaliação como artefatos promovíveis. Separar pipeline de build, avaliação, aprovação, deploy, observação e reversão. | Pipelines, gates de qualidade/segurança/custo, registry de artefatos, promoção por ambiente e comparação de release. | Implantação e melhoria contínua | Profissional |
| **GENOPS05-BP01**<br>Saber quando customizar modelos | Usar uma escada de complexidade: prompt e parâmetros; RAG; fluxo determinístico com tools; fine-tuning; continuous pre-training somente quando evidência justificar. Medir ganho contra custo, risco, manutenção e portabilidade. | ADR/experimento com baseline, hipótese, dataset, ganho, custo total, riscos e critério de saída. | Seleção e customização | MVP |

## Aplicação no perfil AWS

- Amazon CloudWatch, AWS X-Ray e uma distribuição OpenTelemetry podem receber métricas, logs e traces; a instrumentação do núcleo permanece vendor-neutral.
- AWS CloudTrail cobre mudanças de plano de controle, mas não substitui audit events de negócio.
- AWS CDK, AWS CloudFormation ou Terraform podem materializar IaC; o repositório não prescreve uma única ferramenta.
- Avaliações podem usar jobs efêmeros, Amazon Bedrock evaluation capabilities, Amazon SageMaker AI Processing/Experiments ou ferramentas independentes, desde que dataset, versão e resultado sejam reproduzíveis.
- Quotas de Amazon Bedrock ou endpoints Amazon SageMaker AI entram no capacity model, junto com filas, conexões de banco e limites dos canais.

## Métricas e sinais recomendados


- resolução, handoff, abandono, feedback e reabertura por intenção;
- fila: profundidade, idade mais antiga, claim latency, leases expirados e retries;
- turn: tempo total, tempo até primeiro feedback, timeout, cancelamento e stop reason;
- LLM: latência, tokens, custo estimado, erro, throttling, recusa, guardrail e fallback;
- RAG: freshness, recall amostral, groundedness, fontes ausentes e documentos sem permissão;
- tools: chamadas, latência, sucesso, rejected, outcome_unknown, breaker e aprovação;
- outbox/delivery: backlog, tentativas, accepted, delivered, failed e reconciliação;
- release: versões de prompt/modelo/grafo/tool/knowledge e regressões de eval.

## Anti-padrões

- Promover prompt ou modelo por avaliação manual informal e sem baseline.
- Monitorar somente CPU/HTTP e ignorar fila, tokens, RAG, tools, outbox e feedback.
- Registrar prompts e documentos completos em traces para facilitar debug.
- Aumentar quotas ou workers sem backpressure e budgets por tenant.
- Fazer fine-tuning antes de comprovar que prompt, RAG e fluxo determinístico são insuficientes.

## Gate de revisão

A prática só recebe status **atendida** quando existe implementação, teste e evidência operacional vinculada à versão. Documento sem execução vale no máximo **parcial**. Use a [matriz de lifecycle e review](lifecycle-mapping-and-review.md) para registrar owner, status, risco e plano de melhoria.
