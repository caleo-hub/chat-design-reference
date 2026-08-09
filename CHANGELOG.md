# Changelog

Todas as mudanças relevantes deste projeto serão documentadas neste arquivo.

O formato segue uma adaptação de Keep a Changelog e o projeto usa versionamento semântico para releases da referência.

## [Unreleased]

### Adicionado

- adaptação completa do AWS Well-Architected Generative AI Lens para chats e assistentes;
- princípios, Responsible AI, lifecycle, data architecture e padrões de Agentic AI;
- arquiteturas-base AWS para ECS/Fargate, RAG, tools transacionais, multi-tenant, contact center, serverless e modelos customizados;
- perfil de deploy AWS preservando o monólito modular, PostgreSQL inbox/leases/outbox e portas neutras;
- oito cenários do Lens adaptados ao contexto do repositório;
- seis pilares e checklist das 51 best practices com lifecycle, gates e evidências;
- glossário, fontes, política de revisão, atribuição e notices.

### Planejado

- primeira fatia vertical durável com PostgreSQL, inbox, leases, heartbeat e outbox;
- adapter web de teste e sender de referência;
- testes de crash, duplicidade, reconciliação e restauração;
- empacotamento do repositório como GitHub Template.

## [0.1.0] - 2026-08-03

### Adicionado

- arquitetura de referência em monólito modular para chats profissionais com IA;
- envelope canônico multi-canal;
- portas neutras para Agent Runtime e Tool Gateway/MCP;
- especificações de Supervisor, subagentes, handoff e tarefas longas;
- modelo de inbox, leases, heartbeat, watchdog, DLQ e transactional outbox;
- C4, sequências críticas, atributos de qualidade, threat model e ADRs;
- contratos OpenAPI e JSON Schema;
- harness Python/FastAPI com readiness fail-closed;
- fitness functions, Ruff, mypy strict, pytest e import-linter;
- runbooks de criação, extensão, operação e incidentes;
- governança de contribuição, ownership, dependências e licença Apache-2.0.
