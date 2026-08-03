# Rastreabilidade do runbook e do livro

| Recomendação | Aplicação | Decisão | Owner | Evidência | Estado |
|---|---|---|---|---|---|
| Problema antes da solução | Initiative brief e visão separam problema de tecnologias | adotar | owner do template | `INITIATIVE-BRIEF.md` | em uso |
| Perfil proporcional ao risco | perfil padrão, módulos críticos por ação | adaptar | tech lead | initiative brief | decidido |
| Constituição verificável | invariantes em `specs/constitution.md` | adotar | arquitetura | constitution + fitness functions | em uso |
| Menor estilo que sustenta atributos | monólito modular, múltiplos papéis do mesmo artefato | adotar | arquitetura | ADR-0001 | proposto |
| C4 contexto e containers | diagramas Mermaid e limites externos | adotar | arquitetura | `docs/architecture/context.md`, `containers.md` | proposto |
| Contratos concretos | OpenAPI e JSON Schemas versionados | adotar | mantenedores | `contracts/` | proposto |
| Idempotência antes de retry | inbox, outbox, chaves e reconciliação | adotar | módulos jobs/tools | ADR-0002/0005 | proposto |
| Repositório como ambiente operacional | README, AGENTS, comandos e fontes de verdade | adotar | mantenedores | raiz do repositório | em uso |
| Test gauntlet e pipeline com veto | lint, tipos, testes e import-linter | adotar | mantenedores | Makefile e CI | inicial |
| Evidência independente | contracts/fitness functions não dependem do agente implementador | adaptar | revisores | testes arquiteturais | planejado |
| Operação e rollback | deploy VPS, health, backup, DLQ e rollback | adotar | operação | runbooks | proposto |
| Autonomia proporcional ao risco | operações sensíveis exigem aprovação | adotar | owner humano | AGENTS + threat model | em uso |
