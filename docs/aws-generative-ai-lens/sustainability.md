# Pilar: Sustentabilidade

## Intenção

Reduzir trabalho computacional e armazenamento desnecessários por meio de dimensionamento, modelos adequados, pipelines incrementais e retenção consciente.

Esta adaptação preserva as invariantes de [Constituição](../../specs/constitution.md), [runtime](../architecture/runtime.md), [dados e estado](../architecture/data-and-state.md) e [sustentabilidade existente](../architecture/quality-attributes.md). Os IDs abaixo mantêm rastreabilidade com o AWS Well-Architected Generative AI Lens; o texto e os controles foram reescritos para o cenário deste repositório.

## Práticas adaptadas

| ID | Adaptação para chats/assistentes | Evidência mínima | Fase principal | Gate |
|---|---|---|---|---|
| **GENSUS01-BP01**<br>Usar autoscaling e serverless para otimizar recursos | Ajustar compute à demanda, escalar cada papel separadamente e usar serviços gerenciados/serverless quando o perfil de carga e a latência permitirem. Evitar capacidade ociosa e overprovisioning permanente. | Utilização, política de escala, teste de cold start, capacidade mínima e custo/energia como proxy. | Escopo e implantação | MVP |
| **GENSUS01-BP02**<br>Usar serviços eficientes de customização | Preferir técnicas e serviços que reutilizem modelos base, jobs efêmeros, checkpoint e hardware adequado. Encerrar recursos após o job e comparar fine-tuning com RAG/prompt antes de treinar. | ADR de customização, duração/recursos do job, checkpoint, limpeza automática e ganho medido. | Escopo e customização | Condicional |
| **GENSUS02-BP01**<br>Otimizar processamento e armazenamento de dados | Ingestão incremental, deduplicação, lifecycle, compressão, tiering, retenção mínima, reuso de chunks e embeddings, exclusão verificável e pipelines que não reprocessam todo o corpus. | Data lifecycle, métricas de bytes/processamento, lineage, políticas de retenção e teste de delete. | Customização e operação | MVP |
| **GENSUS03-BP01**<br>Usar modelos menores e inferência otimizada | Aplicar roteamento para modelos menores, batch quando possível, caching seguro, quantização/distillation em self-hosted quando justificado e limites de contexto/saída. Medir qualidade por unidade de recurso. | Benchmark Pareto, policy de routing, utilização, tokens por resultado útil e revisão de modelo. | Desenvolvimento e melhoria contínua | MVP |

## Aplicação no perfil AWS

- Serviços gerenciados e serverless podem reduzir ociosidade, mas devem ser escolhidos após medir cold start, retenção mínima e perfil de carga.
- Autoscaling de ECS, SageMaker AI ou componentes serverless deve usar demanda real e limites para evitar thrashing.
- S3 lifecycle, ingestão incremental e reconstrução controlada de índices reduzem armazenamento e processamento repetido.
- A seleção de região, modelo e hardware deve considerar requisitos de dados e SLOs; sustentabilidade não autoriza mover dados ou degradar controles.

## Métricas e sinais recomendados

- utilização média e picos por papel e endpoint;
- tokens, passos, chamadas, bytes processados e bytes retidos por resultado útil;
- frequência de reindexação e percentual incremental versus full rebuild;
- proporção de tarefas atendidas por modelos menores;
- recursos de customização ativos, duração e limpeza pós-job;
- retenção efetiva de mídia, traces, corpus, chunks e embeddings.

## Anti-padrões

- Assumir que serverless é sempre mais eficiente, independentemente de cold starts e carga constante.
- Treinar/customizar modelo para problemas resolvíveis com RAG ou prompt.
- Manter mídia, traces, chunks e embeddings sem retenção ou finalidade.
- Usar modelos grandes em classificação e extração simples.
- Reprocessar todo o corpus em vez de usar ingestão incremental e manifestos.

## Gate de revisão

A prática só recebe status **atendida** quando existe implementação, teste e evidência operacional vinculada à versão. Documento sem execução vale no máximo **parcial**. Use a [matriz de lifecycle e review](lifecycle-mapping-and-review.md) para registrar owner, status, risco e plano de melhoria.
