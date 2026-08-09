# Glossário, fontes, revisões e notices

## Glossário adaptado

| Termo | Uso nesta referência |
|---|---|
| Agent | sistema que percebe contexto, decide etapas e usa tools para atingir um objetivo sob limites |
| Agency | grau de liberdade para escolher ações; deve ser proporcional à tarefa e ao risco |
| AgentRuntime | porta do núcleo para executar grafo, workflow, agent ou state machine sem acoplamento ao framework |
| Autonomous agent | loop em que o modelo seleciona próximas ações até uma stop condition |
| Bias and fairness testing | avaliação de diferenças indevidas de qualidade, recusa, recomendação ou ação entre grupos relevantes |
| ChannelEnvelope | contrato canônico versionado que normaliza eventos de WhatsApp, Teams, web, voz e outros canais |
| Chunking | divisão de conteúdo em unidades recuperáveis, preservando contexto, metadata, ACL e provenance |
| Continuous pre-training | atualização do modelo com grande corpus adicional; excepcional e fora do default do template |
| Data card | documentação de finalidade, origem, licença, composição, qualidade, riscos, retenção e lineage de dataset |
| Data management | identificação, coleta, qualidade, armazenamento, busca, acesso, governança, retenção e exclusão de dados |
| Embedding | representação vetorial usada para similaridade; versão e dimensão fazem parte do contrato do índice |
| Eval dataset / ground truth | casos versionados com critérios de resposta, trajetória, fontes, políticas e thresholds |
| Fine-tuning | ajuste de um modelo base com dataset específico; requer baseline, data card, eval e rollback |
| Foundation model | modelo geral pré-treinado usado como base para geração, entendimento ou multimodalidade |
| GenAIOps / LLMOps | práticas de versionar, avaliar, promover, observar e governar app, modelo, prompt, data e knowledge |
| Guardrail | controle de entrada/saída ou tópico; é uma camada e não substitui autorização ou regra de negócio |
| Hallucination | saída sem suporte, incorreta ou desconectada; tratar com grounding, validação e recusa proporcional |
| Handoff | transferência persistente para humano com contexto, motivo, SLA, claim e retorno ao fluxo |
| Human oversight | revisão, aprovação, contestação, interrupção ou decisão humana em pontos proporcionais ao risco |
| Indexing | criação/atualização de índices a partir de corpus, chunks, embeddings, metadata e ACL versionados |
| Knowledge base | corpus recuperável com provenance, autorização e freshness; não é memória nem estado operacional |
| Knowledge graph | entidades e relações estruturadas usadas para retrieval ou reasoning, sob autorização da fonte |
| Memory | contexto persistido de sessão, usuário ou organização; promoção exige policy e curadoria |
| Model card | finalidade, capacidades, dados conhecidos, limites, avaliações, regiões, custo e riscos de um modelo |
| Model catalog | registro de modelos, versões, capacidades, quotas, regiões, data policy, routing e depreciação |
| Model customization | prompt, RAG, agents, fine-tuning, distillation ou outras técnicas para adaptar comportamento |
| Model distillation | treinamento de modelo menor para reproduzir capacidades selecionadas de outro maior |
| Model gateway | camada de acesso padronizado que autentica, autoriza, roteia, mede e aplica políticas a modelos |
| Model hub | catálogo/repositório de modelos aprovados; não concede acesso por si só |
| Model interpretability | mecanismos para entender fatores e limitações de uma saída, além de explicações textuais do próprio modelo |
| Orchestration | coordenação de estados, modelos, retrieval, tools, approvals, budgets e retries |
| Outcome unknown | estado em que uma mutação pode ter ocorrido, mas a confirmação falhou; exige reconciliação antes de replay |
| Prompt catalog | repositório versionado de templates, variáveis, owners, testes, compatibilidade e rollback |
| Prompt engineering | desenho e teste de instruções/contexto para orientar o modelo, sem ser o único controle de segurança |
| Provisioned throughput | capacidade de inferência reservada/contratada; decisão de custo e confiabilidade conforme serviço |
| Quantization | redução de precisão para diminuir memória/compute, sujeita a avaliação de qualidade |
| RAG | retrieval autorizado de fontes externas para grounding antes da geração |
| Retrieval | busca de evidências estruturadas ou não estruturadas, com filtros, ranking, ACL e freshness |
| Self-hosted model | modelo cujo serving, patching, escala e segurança são responsabilidade da organização |
| Serverless | perfil em que o provedor gerencia alocação de compute; não remove limites, idempotência ou observabilidade |
| Tool | capacidade externa read-only ou mutante chamada por contrato, policy, timeout e auditoria |
| Tool Gateway | fronteira única para discovery, autorização, schema, idempotência, approval e resultado canônico de tools |
| Tokenization | divisão do conteúdo em tokens; impacta contexto, latência, custo e truncamento |
| Vector store | armazenamento/indexação de embeddings para busca; deve poder ser reconstruído do corpus e manifesto |
| Zero-shot | execução sem exemplos específicos de treino; ainda requer eval do domínio |

## Fontes primárias

- AWS Well-Architected Framework - Generative AI Lens: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html
- PDF completo do Lens: https://docs.aws.amazon.com/pdfs/wellarchitected/latest/generative-ai-lens/generative-ai-lens.pdf
- Custom lens JSON oficial: https://github.com/aws-samples/sample-well-architected-custom-lens/tree/main/generative-ai-lens
- AWS Well-Architected Framework: https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
- AWS Well-Architected Tool custom lenses: https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses.html

Referências específicas de serviços devem ser verificadas na documentação oficial na data da implementação. Este material evita fixar preços, quotas ou disponibilidade regional porque mudam.

## Cobertura dos tópicos do documento oficial

| Tópico oficial | Adaptação local |
|---|---|
| Abstract and introduction, scope e lens availability | `index.md` |
| Definitions e design principles | `foundations.md` e este glossário |
| Responsible AI | `responsible-ai-lifecycle-data.md` |
| Generative AI lifecycle | `responsible-ai-lifecycle-data.md` e `lifecycle-mapping-and-review.md` |
| Data architecture | `responsible-ai-lifecycle-data.md` |
| Agentic AI | `responsible-ai-lifecycle-data.md` e `reference-architectures.md` |
| Scenarios | `scenarios.md` |
| Operational excellence | `operational-excellence.md` |
| Security | `security.md` |
| Reliability | `reliability.md` |
| Performance efficiency | `performance-efficiency.md` |
| Cost optimization | `cost-optimization.md` |
| Sustainability | `sustainability.md` |
| Conclusion | `index.md` |
| Appendix A lifecycle mapping | `lifecycle-mapping-and-review.md` |
| Contributors, revisions, notices e AWS glossary | este documento, com links para a fonte oficial |

## Versão e revisão

- Fonte oficial consultada: publicação indicada pela AWS em **19 de novembro de 2025**; PDF oficial acessado na versão disponível durante esta adaptação.
- A lista de 51 best practices foi conferida pelos IDs `GENOPS`, `GENSEC`, `GENREL`, `GENPERF`, `GENCOST` e `GENSUS` do custom lens oficial.
- Revisar este overlay no mínimo semestralmente e também quando a AWS publicar revisão material, um serviço mudar de nome/comportamento ou o workload adotar novo modelo, região, dado, tool ou nível de agência.
- Registrar mudanças no `CHANGELOG.md`; alterações de invariantes da referência exigem ADR.

## Contributors

O Lens oficial possui uma lista extensa de contribuidores da AWS e parceiros no documento fonte. Este repositório não replica essa lista. A autoria desta adaptação deve ser atribuída pelo histórico Git e pelo PR correspondente; contribuições futuras seguem `CONTRIBUTING.md` e `CODEOWNERS`.

## Notices e atribuição

- Este é um trabalho independente de síntese e adaptação; **não é documentação oficial da AWS, não é endossado pela AWS e não substitui uma AWS Well-Architected Review**.
- Amazon Web Services, AWS, Amazon Bedrock, Amazon Q, Amazon SageMaker e demais marcas citadas pertencem aos respectivos titulares.
- O texto oficial não foi reproduzido integralmente. Os IDs foram preservados para rastreabilidade; recomendações foram reescritas para o contexto do projeto.
- O repositório continua sob Apache License 2.0 conforme `LICENSE`; documentos e marcas de terceiros permanecem sujeitos aos respectivos termos.
- A disponibilidade de serviços, modelos, regiões, quotas, preços e features deve ser confirmada antes de cada implementação.
- Nenhum template elimina a necessidade de revisão de segurança, privacidade, compliance, acessibilidade, ética e jurídico aplicável ao produto.
