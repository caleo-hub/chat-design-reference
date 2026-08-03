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
- Twelve-Factor apenas onde compatível com estado, containers e operação em VPS.

## Links

- https://c4model.com/
- https://www.postgresql.org/docs/current/sql-select.html
- https://cloudevents.io/
- https://opentelemetry.io/docs/
- https://modelcontextprotocol.io/specification/2025-11-25/
- https://owasp.org/

## Política de versões

Protocolos e bibliotecas mudam. Projetos derivados devem fixar a versão realmente suportada, registrar compatibilidade e não tratar `latest` como contrato.
