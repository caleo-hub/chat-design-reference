# Pilar: Eficiência de desempenho

## Intenção

Otimizar a experiência completa do turn com qualidade, latência, throughput e retrieval medidos em conjunto, evitando a escolha de modelo ou vetor por intuição.

Esta adaptação preserva as invariantes de [Constituição](../../specs/constitution.md), [runtime](../architecture/runtime.md), [dados e estado](../architecture/data-and-state.md) e [eficiência de desempenho existente](../architecture/quality-attributes.md). Os IDs abaixo mantêm rastreabilidade com o AWS Well-Architected Generative AI Lens; o texto e os controles foram reescritos para o cenário deste repositório.

## Práticas adaptadas

| ID | Adaptação para chats/assistentes | Evidência mínima | Fase principal | Gate |
|---|---|---|---|---|
| **GENPERF01-BP01**<br>Definir dataset de ground truth de prompts e respostas | Criar casos representativos com resposta esperada, critérios, fontes, trajetória de tools e invariantes. Separar treino, desenvolvimento, regressão e red team; versionar por domínio e idioma. | Dataset versionado, rubric, coverage report, provenance e baseline de release. | Customização e desenvolvimento | MVP |
| **GENPERF01-BP02**<br>Coletar métricas de desempenho | Medir webhook, espera em fila, tempo até primeiro feedback, time to first token, geração, retrieval, tool, outbox e entrega; correlacionar com qualidade e custo, não otimizar latência isoladamente. | SLOs, histogramas, traces, painel por etapa e análise de percentis. | Escopo e operação | MVP |
| **GENPERF02-BP01**<br>Testar carga nos endpoints de modelo | Usar distribuições realistas de tamanho de contexto, output, streaming, concorrência, tool loops e retries. Testar quotas, throttling, fallback e recuperação após pico. | Plano de carga, dados sintéticos seguros, resultados p50/p95/p99 e capacidade aprovada. | Desenvolvimento | MVP |
| **GENPERF02-BP02**<br>Otimizar parâmetros de inferência | Ajustar temperatura, top-p, max tokens, stop conditions, structured output e reasoning budget por tarefa. Registrar parâmetros na versão e avaliar qualidade, latência, segurança e custo juntos. | Experimentos, matriz por intenção, parâmetros versionados e guardrails de configuração. | Desenvolvimento | MVP |
| **GENPERF02-BP03**<br>Selecionar e customizar o modelo adequado | Comparar modelos na fronteira de Pareto entre qualidade, latência, custo, contexto, modalidade, região e política de dados. Evitar usar o maior modelo como default; roteamento por tarefa deve ser testado. | Scorecard, benchmark por intenção, decisão de routing e critérios de fallback. | Seleção | MVP |
| **GENPERF03-BP01**<br>Usar soluções gerenciadas quando apropriado | Preferir serviços gerenciados quando reduzem toil e atendem controle, latência, portabilidade e custo; medir cold start, quotas, limites, observabilidade e lock-in antes da decisão. | ADR buy/build, benchmark, SLO, custos e plano de saída ou abstração por adapter. | Customização e desenvolvimento | MVP |
| **GENPERF04-BP01**<br>Testar embeddings por latência e relevância | Avaliar modelo de embedding, chunking, metadata filters, top-k, hybrid search e reranking com queries reais. Medir recall, precision/nDCG, groundedness e latência ponta a ponta. | Benchmark de retrieval, dataset de queries, métricas, análise de erro e versão do índice. | Desenvolvimento e melhoria contínua | MVP |
| **GENPERF04-BP02**<br>Otimizar dimensão dos vetores | Escolher dimensão pelo ganho de relevância versus armazenamento, memória e latência. Validar redução, quantização ou novo embedding antes de reindexar; nunca misturar vetores incompatíveis. | Teste de dimensão, plano de migração/reindexação, métricas de qualidade e custo. | Desenvolvimento | Profissional |

## Aplicação no perfil AWS

- Amazon Bedrock e Amazon SageMaker AI expõem perfis diferentes de modelos e hosting; a escolha deve vir de benchmark do caso de chat.
- Amazon Bedrock Knowledge Bases, Amazon OpenSearch Service, Amazon Kendra ou um store PostgreSQL/pgvector são alternativas, não defaults universais.
- CloudWatch e OpenTelemetry devem separar latência de fila, inferência, retrieval, tools e delivery.
- Provisioned throughput, cross-Region inference, batch e endpoints self-hosted são decisões de capacidade; medir com tráfego representativo antes de adotar.

## Métricas e sinais recomendados

- webhook p50/p95/p99 e tempo de persistência;
- queue wait, time to first feedback, TTFT e time to final answer;
- latência de retrieval, reranking, tool, outbox e delivery;
- qualidade por intenção: task success, groundedness, citation precision e policy adherence;
- throughput em requests e tokens, throttling e utilização;
- recall/nDCG do retrieval, dimensão de vetor e tamanho do índice.

## Anti-padrões

- Escolher o maior modelo e a maior dimensão de embedding como padrão.
- Otimizar TTFT ignorando fila, tool latency, qualidade e entrega ao canal.
- Executar load test com prompts curtos quando a produção usa contexto longo e tools.
- Mudar chunking, embedding ou top-k sem dataset de retrieval e reindexação controlada.
- Confundir resposta longa com resposta melhor.

## Gate de revisão

A prática só recebe status **atendida** quando existe implementação, teste e evidência operacional vinculada à versão. Documento sem execução vale no máximo **parcial**. Use a [matriz de lifecycle e review](lifecycle-mapping-and-review.md) para registrar owner, status, risco e plano de melhoria.
