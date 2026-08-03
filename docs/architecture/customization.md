# Customização de projetos derivados

## Regra

Customize adapters, specs e políticas. Não copie e altere invariantes operacionais sem ADR.

## Superfícies de variação

| Área | Escolhas | Onde configurar/implementar |
|---|---|---|
| canal | web, WhatsApp, Teams, outros | `channels.adapters` + perfil YAML |
| identidade | anônimo, login, telefone verificado, diretório | módulo `identity` |
| agent runtime | LangGraph, CrewAI, custom | adapter `AgentRuntime` |
| LLM | OpenAI, Anthropic, Azure, local etc. | adapter/model registry |
| agentes | supervisor, subfluxos, prompts | `specs/agents/` e runtime config |
| tools | MCPs, tools internas | catálogo, scopes e policies |
| memória | sessão, resumo, durável | memory policy/store |
| conhecimento | RAG, busca, banco | knowledge adapter |
| handoff | fila humana, aprovação, SLA | módulo handoff |
| tenancy | single/multi | identidade, chaves e policies |
| observabilidade | OTel/backends | adapters e retention |
| deploy | tamanho VPS, replicas de papel | Compose/profile |

## Invariantes que o perfil não pode desligar no MVP

- autenticação do canal;
- receipt/deduplicação;
- persistência antes de processar;
- lease/retry/DLQ;
- outbox;
- tool schemas e idempotência de mutação;
- sanitização;
- health/backup/rollback;
- correlation e auditoria de ações sensíveis.

## Passos de instanciação

1. definir problema, owner e perfil de risco;
2. copiar `reference.example.yaml`;
3. preencher decisões sem `define-me`;
4. escrever agentes e fluxos em specs;
5. classificar tools por risco;
6. escolher adapters e registrar ADRs quando estruturais;
7. gerar scaffold dos módulos necessários;
8. executar contract/architecture tests;
9. implementar uma fatia vertical;
10. testar falhas, backup e rollback.

## Troca de framework de agentes

O adapter deve mapear `TurnRequest`/`TurnResult`. Estado operacional permanece no chat; checkpoints específicos podem ser migrados ou descartados conforme política.

A troca não deve alterar:

- envelope de canal;
- inbox/outbox;
- tool result taxonomy;
- autorização;
- audit/correlation;
- handoff;
- estados transacionais.

## Adição de canal

Adicionar:

- webhook verification;
- normalizer;
- capability profile;
- renderer/sender;
- delivery event parser;
- identity mapping;
- contract fixtures e fault tests.

Não duplicar orquestração ou memória por canal.

## Adição de MCP

Definir:

- owner e finalidade;
- transport/auth;
- tools/resources permitidos por escopo;
- schemas e compatibilidade;
- timeouts, rate limits e circuit breaker;
- idempotência/reconciliação;
- dados enviados e retenção;
- mock e contract tests.
