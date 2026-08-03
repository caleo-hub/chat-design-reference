# Rastreabilidade do runbook e do livro

| Recomendação | Aplicação | Decisão | Owner | Evidência | Estado |
|---|---|---|---|---|---|
| Problema antes da solução | Initiative brief e visão separam problema de tecnologias | adotar | owner do template | `INITIATIVE-BRIEF.md` | em uso |
| Perfil proporcional ao risco | perfil padrão, módulos críticos por ação | adaptar | tech lead | initiative brief | decidido |
| Constituição verificável | invariantes em `specs/constitution.md` | adotar | arquitetura | constitution + fitness functions | em uso |
| Menor estilo que sustenta atributos | monólito modular, múltiplos papéis do mesmo artefato | adotar | arquitetura | ADR-0001 + aprovação do owner | aprovado |
| C4 contexto e containers | diagramas Mermaid e limites externos | adotar | arquitetura | `docs/architecture/context.md`, `containers.md` | em uso |
| Contratos concretos | OpenAPI e JSON Schemas versionados | adotar | mantenedores | `contracts/` + contract tests | em uso |
| Idempotência antes de retry | inbox, outbox, chaves e reconciliação | adotar | módulos jobs/tools | ADR-0002/0005 | aprovado |
| Repositório como ambiente operacional | README, AGENTS, comandos, ownership e fontes de verdade | adotar | mantenedores | raiz e `.github/` | em uso |
| Test gauntlet e pipeline com veto | lint, tipos, testes, schemas e import-linter | adotar | mantenedores | Makefile e CI verde | em uso |
| Evidência independente | contratos e fitness functions não dependem do agente implementador | adaptar | revisores | testes arquiteturais e revisão humana do PR | inicial |
| Operação e rollback | deploy VPS, health, backup, DLQ e rollback | adotar | operação | runbooks | especificado |
| Autonomia proporcional ao risco | operações sensíveis exigem aprovação | adotar | owner humano | AGENTS + threat model + PR template | em uso |
| Dependências e supply chain controladas | versões limitadas, CI fixado, Dependabot e licença explícita | adotar | mantenedores | `pyproject.toml`, CI, Dependabot e LICENSE | em uso |
| Aprendizado retorna ao repositório | estado, changelog e próximos gates permanecem versionados | adotar | mantenedores | `STATUS.md` e `CHANGELOG.md` | em uso |
