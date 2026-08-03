# Estado da adoção

## Fase atual

Fases 4–6 — arquitetura aprovada, preparação do repositório e sistema inicial de verificação.

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
- owner aprovou a fundação e autorizou o merge em 2026-08-03;
- PR #1 contém os artefatos de fundação;
- CI mais recente do PR concluído com sucesso;
- Ruff sem violações;
- mypy strict sem problemas nos arquivos-fonte;
- testes de contrato, arquitetura e health aprovados;
- contrato de dependência do import-linter preservado;
- OpenAPI carregado com sucesso;
- readiness permanece fail-closed sem runtime durável conectado;
- licença Apache-2.0, metadata do pacote, CODEOWNERS, template de PR, Dependabot e changelog definidos.

## Decisões da referência concluídas

- estilo: monólito modular;
- execução: mesmo artefato com papéis API, worker, sender e scheduler;
- persistência durável inicial: PostgreSQL;
- entrada: envelope canônico multi-canal;
- processamento: webhook rápido + worker assíncrono;
- entrega: transactional outbox;
- agentes: porta neutra de runtime com Supervisor/Subagentes;
- tools: Tool Gateway com MCP como adapter preferido;
- licença: Apache-2.0;
- governança mínima: CI, ownership, PR orientado a risco e atualizações de dependências.

## Decisões pendentes da referência

- baseline de SLOs obrigatória versus apenas sugerida;
- backend opcional de streaming para alto volume;
- formato final de plugins de adapters;
- escopo exato do runtime executável do template v1.

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

**Fundação aprovada; runtime produtivo ainda bloqueado.** A arquitetura e o harness inicial podem ser usados como base oficial do template. Nenhum projeto derivado deve declarar produção pronta apenas por herdar este repositório.

## Próxima ação recomendada

Implementar uma única fatia vertical: webhook canônico → receipt/inbox PostgreSQL → worker stub com lease/heartbeat → estado + outbox → sender web de teste → testes de duplicidade, crash e recuperação.
