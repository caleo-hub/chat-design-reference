# ADR-0004 — MCP como fronteira preferida de tools externas

- Status: proposto
- Data: 2026-08-03

## Contexto

Agentes precisam consultar e alterar sistemas externos. Implementar clientes dentro dos agentes mistura conversa, autenticação, integração e regras de retry.

## Decisão

Usar `ToolGateway` como porta interna e MCP como adapter preferido para integrações externas/reutilizáveis. Tools internas simples podem implementar a mesma porta sem MCP.

## Regras

- auth e allowlist por server/scope;
- schemas versionados;
- mutações com idempotência;
- contexto mínimo e sanitizado;
- timeout, breaker, rate limit e auditoria;
- resultado canônico;
- ações críticas podem ser invocadas apenas por código determinístico.

## Consequências

- integração desacoplada do framework;
- mock/contract testing melhor;
- processo/protocolo adicional quando MCP é externo;
- necessidade de coordenar versões produtor/consumidor.

## Alternativas rejeitadas

- expor clientes REST diretamente como tools do modelo;
- permitir discovery irrestrito;
- transformar cada função local em MCP sem valor de fronteira.
