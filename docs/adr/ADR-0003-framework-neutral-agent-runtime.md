# ADR-0003 — Porta neutra de agent runtime

- Status: proposto
- Data: 2026-08-03

## Contexto

Projetos derivados podem usar LangGraph, CrewAI, SDKs nativos ou código próprio. Acoplar o domínio a um framework reduz reutilização e torna migração arriscada.

## Decisão

Definir `AgentRuntime` com `TurnRequest` e `TurnResult` canônicos. Frameworks existem em adapters.

## Consequências

- troca/benchmark de runtime possível;
- testes determinísticos com stub;
- núcleo preserva políticas e estado operacional;
- features muito específicas de um framework precisam de mapeamento explícito;
- não se busca menor denominador comum para tudo: extensões ficam em metadata versionada e isolada.

## Alternativas rejeitadas

- usar diretamente LangChain/CrewAI em use cases;
- criar framework próprio completo antes de necessidade;
- modelar cada projeto sem contrato comum.
