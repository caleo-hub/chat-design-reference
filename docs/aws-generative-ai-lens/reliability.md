# Pilar: Confiabilidade

## Intenção

Preservar mensagens, estado e efeitos diante de duplicidade, throttling, falhas de rede, timeouts, crashes, indisponibilidade regional e resultados externos desconhecidos.

Esta adaptação preserva as invariantes de [Constituição](../../specs/constitution.md), [runtime](../architecture/runtime.md), [dados e estado](../architecture/data-and-state.md) e [confiabilidade existente](../architecture/failure-model.md). Os IDs abaixo mantêm rastreabilidade com o AWS Well-Architected Generative AI Lens; o texto e os controles foram reescritos para o cenário deste repositório.

## Práticas adaptadas

| ID | Adaptação para chats/assistentes | Evidência mínima | Fase principal | Gate |
|---|---|---|---|---|
| **GENREL01-BP01**<br>Escalar throughput conforme utilização | Dimensionar por requests, tokens, tempo de geração, fila e idade do backlog. Aplicar admissão antes do esgotamento, reservas por tenant e escalabilidade separada para API, worker, sender, mídia e avaliação. | Capacity test, quotas, autoscaling/concorrência, alarmes e limite operacional conhecido. | Seleção e operação | MVP |
| **GENREL02-BP01**<br>Redundância de rede entre endpoints e suporte | Usar Multi-AZ para componentes controlados, múltiplas tasks, balanceamento, pools saudáveis, DNS/egress resilientes e caminhos alternativos aprovados. Evitar dependência de um NAT, AZ ou endpoint único. | Diagrama de falhas, teste de AZ, health checks, connection pooling e runbook de dependência. | Desenvolvimento e implantação | MVP |
| **GENREL03-BP01**<br>Gerenciar fluxos de prompt e recuperar de falhas | Modelar o turn como máquina de estados. Retries só ocorrem com resultado conhecido e idempotência; timeout após possível mutação vira outcome_unknown e reconciliação; respostas e outbox são atômicas. | State diagram, testes de crash/retry, DLQ, reconciliação e invariantes da outbox. | Desenvolvimento e implantação | MVP |
| **GENREL03-BP02**<br>Aplicar timeouts em workflows agentic | Definir deadline global e timeouts por LLM, retrieval, tool, mídia e entrega. Renovar lease, cooperar com cancelamento, limitar loops e mover tarefas longas para jobs duráveis. | Configuração de deadlines, testes de timeout/cancelamento, heartbeat e execução resumível. | Desenvolvimento e implantação | MVP |
| **GENREL04-BP01**<br>Implementar catálogo de prompts | Manter prompts versionados e compatíveis com o estado do fluxo, o modelo e o schema de tool. Rollback deve recuperar o conjunto completo de artefatos, não apenas o texto do prompt. | Catálogo, matriz de compatibilidade, release context, teste de rollback e retenção de versões. | Desenvolvimento e melhoria contínua | MVP |
| **GENREL04-BP02**<br>Implementar catálogo de modelos | Registrar capacidades, modalidades, regiões, quotas, contexto, latência, custo, data policy, versão, depreciação e fallback permitido. A seleção deve ser determinística e auditável. | Model registry/catalog, health, policy de routing, contrato de fallback e testes de compatibilidade. | Seleção e melhoria contínua | MVP |
| **GENREL05-BP01**<br>Distribuir inferência entre regiões | Para SLOs que exigem tolerância regional, usar routing entre regiões apenas quando modelo, versão, guardrails, política de dados e comportamento forem equivalentes. Respeitar residência e latência. | ADR multi-Region, health/routing, teste de failover, quotas e evidência de equivalência. | Seleção e implantação | Profissional |
| **GENREL05-BP02**<br>Replicar dados de embeddings entre regiões | Versionar corpus, chunking, embedding e índice; replicar fontes e reconstruir índices de forma determinística; acompanhar freshness e evitar misturar dimensões/modelos incompatíveis. | Manifesto do índice, pipeline de rebuild/replicação, RPO/RTO, teste de restore e métricas de freshness. | Implantação | Profissional |
| **GENREL05-BP03**<br>Verificar capacidades do agente em todas as regiões | Não considerar failover pronto enquanto tools, secrets, approvals, knowledge, model routing, quotas, callbacks e sender não estiverem disponíveis ou explicitamente degradados na região secundária. | Capability matrix regional, teste sintético ponta a ponta, runbook e comportamento de degradação. | Implantação | Profissional |
| **GENREL06-BP01**<br>Tolerância a falhas em computação distribuída | Dividir avaliação, ingestão, transcrição, indexação e customização em unidades idempotentes com checkpoint, lease, retry seletivo e agregação parcial. O coordenador deve retomar sem reiniciar tudo. | Job graph, checkpoints, manifestos, testes de worker loss, partial results e reconciliação. | Customização e implantação | Condicional |

## Aplicação no perfil AWS

- ECS/Fargate ou EKS podem executar múltiplas réplicas dos papéis; Aurora PostgreSQL-Compatible ou RDS for PostgreSQL Multi-AZ preservam o desenho de inbox/leases/outbox.
- Route 53, ALB e health checks ajudam no failover, mas a aplicação precisa readiness real e comportamento de degradação.
- Cross-Region inference, modelos em várias regiões e replicação do corpus são opções profissionais; somente entram depois de residência de dados, equivalência e quotas serem testadas.
- Amazon S3 versionado pode guardar corpus e manifestos para reconstrução de índices; o índice não deve ser o único backup do conhecimento.
- AWS Step Functions, AWS Batch ou filas dedicadas podem coordenar jobs distribuídos condicionais, preservando os contratos de idempotência e reconciliação do núcleo.

## Métricas e sinais recomendados

- disponibilidade por papel e dependência, não apenas endpoint HTTP;
- idade da fila/outbox, throughput, quotas e saturation;
- leases expirados, heartbeats vencidos, jobs órfãos e DLQ;
- retries por classe, outcome_unknown e tempo de reconciliação;
- failover testado, freshness regional, RPO/RTO e restore success;
- erros de schema/compatibilidade de prompt, modelo, tool e índice.

## Anti-padrões

- Repetir automaticamente qualquer timeout de tool mutante.
- Considerar um modelo alternativo equivalente sem teste de qualidade, guardrail e schema.
- Usar checkpoint do framework de agentes como fila operacional.
- Declarar multi-Region sem replicar tools, secrets, knowledge, callbacks e delivery.
- Manter apenas o índice vetorial, sem corpus e manifesto para reconstrução.

## Gate de revisão

A prática só recebe status **atendida** quando existe implementação, teste e evidência operacional vinculada à versão. Documento sem execução vale no máximo **parcial**. Use a [matriz de lifecycle e review](lifecycle-mapping-and-review.md) para registrar owner, status, risco e plano de melhoria.
