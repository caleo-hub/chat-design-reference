# Estado da adoção

## Fase atual

Fases 4–6 — arquitetura, preparação do repositório e sistema inicial de verificação.

## Resultado esperado desta fase

Tornar os limites da referência revisáveis, localizar as variabilidades e preparar um harness que rejeite violações arquiteturais e alegações falsas de prontidão.

## Artefatos canônicos

- `docs/product/vision.md`
- `docs/product/prd.md`
- `specs/constitution.md`
- `docs/architecture/index.md`
- `contracts/`
- `docs/security/threat-model.md`
- `docs/adr/`

## Evidências disponíveis

- pedido explícito de template multi-canal em Python/VPS;
- decisão explícita por monólito modular;
- requisito de Supervisor/Subagentes e MCP configurável;
- pesquisa arquitetural anterior aplicada aos módulos e runtime;
- runbook a priori consultado e rastreado;
- PR #1 criado com os artefatos de fundação;
- CI run #2 concluído com sucesso em 2026-08-03;
- Ruff sem violações;
- mypy strict sem problemas em 8 arquivos-fonte;
- 6 testes aprovados;
- contrato de dependência do import-linter preservado;
- OpenAPI carregado com sucesso;
- readiness permanece fail-closed sem runtime durável conectado.

## Decisões pendentes da referência

- licença;
- baseline de SLOs obrigatória versus apenas sugerida;
- backend opcional de streaming para alto volume;
- formato final de plugins de adapters;
- escopo exato do código executável do template v1;
- geração e política de atualização do `uv.lock`.

## Decisões obrigatórias em cada projeto derivado

- classificação e retenção de dados;
- identidade, autorização e tenancy;
- canais e respectivos providers;
- agent runtime e modelos;
- MCPs/tools, permissões e aprovações;
- SLOs, capacidade e backup;
- política de memória e conhecimento.

## Riscos e bloqueios

- a primeira fatia vertical durável ainda não foi implementada;
- documentação pode divergir do runtime se novos fitness functions não acompanharem o código;
- um projeto derivado pode remover invariantes por conveniência;
- funcionalidades profissionais ainda são arquitetura-alvo, não implementação completa;
- uso produtivo continua bloqueado até inbox/outbox PostgreSQL, probes reais, fault tests, backup/restore e decisões específicas do produto.

## Gate

**Parcialmente atendido.** A fundação arquitetural e o harness inicial foram verificados pelo CI. O repositório pode ser revisado e evoluído, mas não deve ser tratado como runtime produtivo.

## Próxima ação recomendada

Revisar e aprovar os ADRs estruturais; depois implementar uma única fatia vertical: webhook canônico → receipt/inbox PostgreSQL → worker stub com lease/heartbeat → estado + outbox → sender web de teste → testes de duplicidade, crash e recuperação.
