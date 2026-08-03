# Arquitetura — índice canônico

## Objetivo

Definir uma arquitetura de referência para chats profissionais com IA, executável em Python numa VPS, sem impor canal, framework de agentes ou provider de LLM.

## Ordem de leitura

1. [Contexto](context.md)
2. [Containers e papéis de runtime](containers.md)
3. [Módulos e dependências](modules.md)
4. [Multi-canal](multi-channel.md)
5. [Agentes e tools](agent-and-tools.md)
6. [Runtime e sequências](runtime.md)
7. [Dados e estado](data-and-state.md)
8. [Modelo de falhas](failure-model.md)
9. [Observabilidade](observability.md)
10. [Atributos de qualidade](quality-attributes.md)
11. [Fitness functions](fitness-functions.md)
12. [Customização](customization.md)
13. [Níveis de maturidade](maturity-levels.md)
14. [Deploy em VPS](deployment-vps.md)
15. [Referências](references.md)

## Decisões estruturais

- [ADR-0001 — Monólito modular](../adr/ADR-0001-modular-monolith.md)
- [ADR-0002 — PostgreSQL como fila durável inicial](../adr/ADR-0002-postgresql-durable-queue.md)
- [ADR-0003 — Porta neutra de agent runtime](../adr/ADR-0003-framework-neutral-agent-runtime.md)
- [ADR-0004 — MCP como fronteira de tools](../adr/ADR-0004-mcp-tool-boundary.md)
- [ADR-0005 — Transactional outbox](../adr/ADR-0005-transactional-outbox.md)
- [ADR-0006 — Envelope canônico de canal](../adr/ADR-0006-canonical-channel-envelope.md)

## Fontes de verdade

| Assunto | Fonte |
|---|---|
| Princípios | `specs/constitution.md` |
| Contratos externos | `contracts/` |
| Estados e invariantes | `specs/features/` e `data-and-state.md` |
| Decisões | `docs/adr/` |
| Segurança | `docs/security/threat-model.md` |
| Operação | `docs/runbooks/` |
| Perfil derivado | `config/<projeto>.yaml` |

## Regra de atualização

Atualize arquitetura, spec, contratos e testes no mesmo PR quando uma mudança:

- atravessar módulos;
- alterar persistência, retry, idempotência ou efeito externo;
- mudar envelope de canal, evento, tool ou resultado;
- introduzir dependência operacional;
- alterar autorização, dados ou tenancy;
- mudar a resposta esperada em incidente.
