# Tool policy — <tool ou MCP>

## Owner e contrato

- Server/tool:
- Schema version:
- Transport/auth:
- Data classification:

## Finalidade

<por que o agente precisa desta capacidade>

## Escopos permitidos

- supervisor:
- subagentes:
- operadores:

## Classe de efeito

- read-only / mutating / destructive;
- reversível?;
- approval required?;
- idempotency key e retenção;
- pós-condição verificável;
- reconciliação.

## Limites

- timeout;
- rate limit;
- payload/response bytes;
- concorrência/bulkhead;
- circuit breaker.

## Dados

- entrada permitida;
- saída pública;
- campos proibidos em log/trace;
- retenção.

## Falhas

Mapear para `ToolResult.status`, sem exceção crua no LLM.

## Testes

- auth/allowlist;
- schema/compatibilidade;
- idempotência;
- timeout antes/depois do efeito;
- rate limit;
- resposta maliciosa/grande;
- cross-tenant.
