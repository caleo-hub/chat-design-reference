# Referências técnicas

A arquitetura não deriva de um único fornecedor. Estas referências sustentam contratos e padrões específicos:

- Runbook a priori do repositório `engenharia-de-software-com-agentes-de-codigo`;
- C4 Model para contexto e containers;
- PostgreSQL `FOR UPDATE SKIP LOCKED` para consumidores concorrentes de filas relacionais;
- Transactional Outbox e idempotent consumer como padrões de consistência;
- CloudEvents 1.0.x como inspiração para envelope de eventos internos;
- OpenTelemetry para traces, metrics, logs e baggage;
- Model Context Protocol, versão 2025-11-25, para tools/resources/auth e tasks experimentais;
- OWASP ASVS/API Security/LLM Top 10 para controles proporcionais;
- Twelve-Factor apenas onde compatível com estado, containers e operação em VPS/AWS;
- AWS Well-Architected Framework e Generative AI Lens para o perfil AWS e a revisão dos seis pilares.

## Links

- https://c4model.com/
- https://www.postgresql.org/docs/current/sql-select.html
- https://cloudevents.io/
- https://opentelemetry.io/docs/
- https://modelcontextprotocol.io/specification/2025-11-25/
- https://owasp.org/
- https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
- https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html
- https://github.com/aws-samples/sample-well-architected-custom-lens/tree/main/generative-ai-lens

A síntese e a rastreabilidade da fonte AWS estão em [Glossário, fontes, revisões e notices](../aws-generative-ai-lens/glossary-sources-and-notices.md).

## Política de versões

Protocolos, modelos, serviços e bibliotecas mudam. Projetos derivados devem fixar a versão realmente suportada, registrar compatibilidade e não tratar `latest` como contrato. A adaptação do AWS Generative AI Lens deve ser revista no mínimo semestralmente e quando a fonte oficial tiver mudança material.
