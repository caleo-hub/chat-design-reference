# AGENTS.md

## Missão

Evoluir uma arquitetura de referência para chats profissionais com IA sem permitir que canal, framework de agentes, LLM ou integração externa governem o núcleo do sistema.

## Antes de editar

1. Leia a spec ou ADR relacionada à tarefa.
2. Leia `docs/architecture/index.md` e o documento do módulo afetado.
3. Execute `make check` e registre falhas preexistentes.
4. Distinga arquitetura obrigatória, customização e trabalho ainda não implementado.
5. Faça mudanças pequenas e reversíveis.

## Fontes de verdade

- Produto: `docs/product/`
- Princípios: `specs/constitution.md`
- Features: `specs/features/`
- Arquitetura: `docs/architecture/`
- Decisões: `docs/adr/`
- API e eventos: `contracts/`
- Segurança: `docs/security/threat-model.md`
- Operação: `docs/runbooks/`

## Limites arquiteturais

- O núcleo não importa FastAPI, SDK de canal, ORM, LangChain, CrewAI ou cliente MCP.
- Adapters dependem de portas; portas não dependem de adapters.
- Nenhum webhook executa LLM ou efeito externo de negócio.
- Nenhuma mensagem de negócio é enviada antes de existir registro durável na outbox.
- Nenhuma mutação externa sujeita a retry existe sem chave de idempotência e reconciliação.
- Tools sensíveis não ficam disponíveis irrestritamente ao modelo.
- Dados sensíveis, prompts integrais e payloads brutos não são registrados por padrão.
- Alterações de contrato exigem versão, testes de compatibilidade e estratégia de rollout.

## Comandos canônicos

- Preparar: `make bootstrap`
- Verificação rápida: `make check`
- Verificação completa: `make verify`
- Executar harness: `make run`

## Operações que exigem decisão humana

Pare antes de alterar:

- política de dados, retenção ou exclusão;
- autorização, multitenancy ou identidade;
- contrato público incompatível;
- ação destrutiva ou irreversível;
- tecnologia estrutural ou nova dependência central;
- infraestrutura de produção, secrets ou migração destrutiva;
- invariantes definidos em `specs/constitution.md`.

## Evidência de conclusão

Informe arquivos alterados, decisões, comandos executados, resultados, riscos residuais, documentos atualizados e rollback. Não use apenas “os testes passaram” como evidência.