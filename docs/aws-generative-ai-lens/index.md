# AWS Generative AI Lens para chats e assistentes

## Objetivo

Este conjunto adapta o **AWS Well-Architected Generative AI Lens** ao sistema de referência deste repositório: chats e assistentes de IA multi-canal, com processamento durável, Supervisor/Subagentes, RAG, tools/MCP, memória, handoff humano e entrega por outbox.

A adaptação tem três objetivos:

1. transformar os tópicos do Lens em decisões e evidências verificáveis para chats;
2. oferecer arquiteturas-base de implantação na AWS sem acoplar o núcleo à nuvem;
3. fornecer uma revisão rastreável das 51 best practices dos seis pilares.

## Relação com a arquitetura existente

O Lens é um **overlay de avaliação e deploy**, não uma arquitetura paralela. Continuam obrigatórias as decisões já existentes:

- núcleo independente de canal, framework, provedor de LLM e nuvem;
- webhook rápido, persistência antes de processar e execução assíncrona;
- inbox/lease/heartbeat/watchdog/DLQ e transactional outbox;
- `AgentRuntime` e `ToolGateway` como portas neutras;
- autorização, confirmação e pós-condições em regras determinísticas;
- estado operacional separado de checkpoints e telemetria;
- handoff, aprovação, reconciliação e auditoria como comportamento do produto.

Serviços AWS aparecem apenas em adapters, infraestrutura e perfis de implantação. Uma implementação derivada pode continuar em VPS, outra nuvem ou ambiente híbrido preservando os mesmos contratos.

## Escopo adaptado

Inclui:

- Amazon Bedrock, Amazon Q e Amazon SageMaker AI como opções de modelo, knowledge, agents ou customização;
- arquiteturas de chat em ECS/Fargate, serverless/event-driven, multi-tenant, RAG, contact center e modelo customizado;
- Responsible AI, lifecycle, data architecture e níveis de agência;
- oito cenários do Lens reinterpretados para chats/assistentes;
- excelência operacional, segurança, confiabilidade, desempenho, custo e sustentabilidade;
- matriz de lifecycle, checklist de review, glossary, fontes, revisões e notices.

Não inclui:

- IaC pronto para produção, dimensionamento universal ou estimativa de preço;
- substituição do AWS Well-Architected Framework ou do documento oficial;
- garantia de compliance, aprovação jurídica ou certificação AWS;
- pre-training de foundation model como caminho padrão deste template.

## Disponibilidade do Lens oficial

A AWS disponibiliza o Lens como documentação e como custom lens importável no AWS Well-Architected Tool. O fluxo oficial é:

1. baixar o JSON do diretório público `generative-ai-lens`;
2. abrir **Custom lenses** no AWS Well-Architected Tool;
3. criar/importar o lens e usar a experiência de preview;
4. associar o lens a um workload quando for executar uma revisão formal;
5. manter as respostas e improvement plans no processo de governança da organização.

Este diretório não substitui o JSON importável. Ele acrescenta a tradução arquitetural para os contratos, módulos, riscos e evidências deste repositório.

## Ordem de leitura

1. [Fundamentos e princípios](foundations.md)
2. [Responsible AI, lifecycle, dados e agentic AI](responsible-ai-lifecycle-data.md)
3. [Arquiteturas-base na AWS](reference-architectures.md)
4. [Deploy AWS do monólito modular](../architecture/deployment-aws.md)
5. [Cenários adaptados](scenarios.md)
6. [Excelência operacional](operational-excellence.md)
7. [Segurança](security.md)
8. [Confiabilidade](reliability.md)
9. [Eficiência de desempenho](performance-efficiency.md)
10. [Otimização de custos](cost-optimization.md)
11. [Sustentabilidade](sustainability.md)
12. [Lifecycle mapping e review](lifecycle-mapping-and-review.md)
13. [Glossário, fontes, revisões e notices](glossary-sources-and-notices.md)

## Como usar

### Antes de construir

- selecione o cenário e a arquitetura-base mais próximos;
- preencha scoping, riscos, Responsible AI, dados, SLOs e budget;
- escolha o menor nível de agência que resolve o problema;
- defina evidências e critérios de rollback antes do deploy.

### Antes de promover uma release

- execute evals funcionais, adversariais, de policy e de retrieval;
- valide contratos, autorização, idempotência, timeout e outbox;
- execute capacity/load tests proporcionais ao risco;
- compare qualidade, latência e custo com a release anterior;
- registre versões de app, prompt, modelo, grafo, tools e knowledge.

### Em operação

- revise sinais técnicos e de negócio por correlation ID;
- trate feedback, falhas e incidentes como entradas do ciclo de melhoria;
- reavalie arquitetura e best practices quando modelo, região, canal, tenant ou risco mudar;
- mantenha o Lens local versionado e vinculado a evidências reais.

## Resultado esperado

Uma revisão concluída deve produzir:

- diagrama e perfil de implantação aprovados;
- inventário de dados, modelos, prompts, tools, knowledge e owners;
- threat model e matriz de Responsible AI atualizados;
- SLOs, quotas, budgets e capacidade conhecida;
- checklist das 51 práticas com status e evidência;
- riscos aceitos, backlog priorizado e data da próxima revisão.

## Conclusão adaptada

Chats e assistentes bem arquitetados não são apenas chamadas a um LLM. São sistemas distribuídos, probabilísticos e orientados por políticas. O valor vem da combinação de arquitetura de software confiável, dados governados, autonomia controlada, avaliação contínua e operação observável. A nuvem fornece capacidades; os contratos, limites e evidências continuam sendo responsabilidade do produto.
