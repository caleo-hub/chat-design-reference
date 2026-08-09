# Pilar: Otimização de custos

## Intenção

Gerenciar custo por resultado útil, tenant e trajetória, controlando modelos, tokens, vetores, compute e loops agentic sem comprometer segurança ou durabilidade.

Esta adaptação preserva as invariantes de [Constituição](../../specs/constitution.md), [runtime](../architecture/runtime.md), [dados e estado](../architecture/data-and-state.md) e [otimização de custos existente](../architecture/quality-attributes.md). Os IDs abaixo mantêm rastreabilidade com o AWS Well-Architected Generative AI Lens; o texto e os controles foram reescritos para o cenário deste repositório.

## Práticas adaptadas

| ID | Adaptação para chats/assistentes | Evidência mínima | Fase principal | Gate |
|---|---|---|---|---|
| **GENCOST01-BP01**<br>Dimensionar a seleção do modelo | Roteamento por intenção, risco e complexidade: modelos menores para classificação/extração, modelos maiores somente quando o ganho medido justificar. Incluir fallback e erro de routing no custo total. | Benchmark de qualidade-custo-latência, policy de routing, custo por turn resolvido e revisão periódica. | Seleção | MVP |
| **GENCOST02-BP01**<br>Equilibrar custo e desempenho dos paradigmas de inferência | Comparar on-demand, provisionado, batch, serverless e self-hosted com volume, sazonalidade, latência, disponibilidade, compromisso e operação. Usar break-even real, não preço unitário isolado. | Modelo de demanda, análise de break-even, SLO, decisão aprovada e gatilho de revisão. | Escopo e seleção | MVP |
| **GENCOST02-BP02**<br>Otimizar recursos e hosting | Escalar papéis separadamente, limitar concorrência cara, reutilizar conexões, descarregar tarefas longas, right-size compute e desligar ambientes efêmeros. Não sacrificar durabilidade para reduzir custo. | Relatório de utilização, autoscaling, budgets, tagging e custo por papel/tenant. | Desenvolvimento e operação | MVP |
| **GENCOST03-BP01**<br>Otimizar tamanho do prompt | Recuperar apenas contexto relevante, remover duplicatas, resumir histórico com provenance, usar schemas compactos e budgets de contexto. O corte deve preservar instruções, segurança e evidências. | Métrica de input tokens, testes de qualidade após compressão e limite por fluxo. | Desenvolvimento e melhoria contínua | MVP |
| **GENCOST03-BP02**<br>Controlar tamanho da resposta | Definir max tokens por intenção, respostas estruturadas, resumo primeiro e detalhamento sob demanda. Evitar verbosidade automática, mas não truncar avisos, fontes ou confirmação crítica. | Métrica de output tokens, templates de resposta, testes de truncamento e UX. | Desenvolvimento | MVP |
| **GENCOST03-BP03**<br>Usar prompt caching | Separar prefixos estáveis de dados variáveis, medir hit ratio e invalidar por versão. Garantir isolamento entre tenants e não colocar segredo ou dado pessoal em cache compartilhado. | Design de cache, chaves/versionamento, métricas de hit, testes de isolamento e invalidação. | Implantação | Condicional |
| **GENCOST03-BP04**<br>Anotar entrada para filtragem consciente de custo | Classificar modalidade, tamanho, complexidade, intenção, risco e urgência antes de escolher modelo, RAG ou tool. Rejeitar abuso e pedir esclarecimento quando reduz custo sem degradar o objetivo. | Classificador/rules, quotas, explainability de routing, métricas de economia e false routing. | Desenvolvimento e melhoria contínua | MVP |
| **GENCOST04-BP01**<br>Reduzir comprimento/dimensão de vetores | Selecionar embeddings e dimensões adequados, deduplicar chunks, aplicar lifecycle e reindexar somente quando necessário. Medir custo de storage, ingestão e query contra recall. | Benchmark de dimensão, custo do índice, política de retenção e plano de reindexação. | Implantação | Profissional |
| **GENCOST05-BP01**<br>Criar condições de parada para workflows longos | Impor max steps, chamadas de tool, tokens, tempo e custo; detectar repetição e falta de progresso; solicitar confirmação ou handoff antes de continuar; cancelar jobs abandonados. | Budgets no TurnRequest, stop reasons, testes de loop, alertas e relatório de custo por trajetória. | Desenvolvimento e implantação | MVP |

## Aplicação no perfil AWS

- AWS Budgets, Cost Explorer e Cost and Usage Reports podem apoiar governança financeira; tags e dimensões de aplicação devem permitir atribuição por ambiente, produto e tenant sem expor PII.
- On-demand, provisioned throughput, batch e hosting em SageMaker AI/EKS/EC2 devem ser comparados pelo custo total, incluindo operação e ociosidade.
- S3 lifecycle, índices dimensionados, autoscaling de ECS/Lambda e ambientes efêmeros reduzem desperdício quando acompanhados de SLOs.
- Prompt caching ou caching de aplicação só é habilitado com isolamento, versionamento e invalidação testados.

## Métricas e sinais recomendados

- custo estimado por turn, usuário ativo, tenant, intenção e resolução bem-sucedida;
- input/output tokens, cache hit, RAG tokens, tool calls e passos agentic;
- custo de storage/indexação, ingestão e reindexação;
- utilização e ociosidade por papel/endpoint;
- custo de handoff e retrabalho causado por baixa qualidade;
- budget consumido e turns interrompidos por limite.

## Anti-padrões

- Otimizar preço por token enquanto a taxa de resolução cai e o handoff aumenta.
- Compartilhar cache entre tenants ou versões sem chave de isolamento.
- Permitir loops agentic sem stop reason, budget e máximo de tool calls.
- Reindexar corpus completo em toda atualização.
- Comprar capacidade fixa sem perfil de demanda e break-even.

## Gate de revisão

A prática só recebe status **atendida** quando existe implementação, teste e evidência operacional vinculada à versão. Documento sem execução vale no máximo **parcial**. Use a [matriz de lifecycle e review](lifecycle-mapping-and-review.md) para registrar owner, status, risco e plano de melhoria.
