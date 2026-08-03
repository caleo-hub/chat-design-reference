# Estado da adoção

## Fase atual

Fase 4/5 — arquitetura, contratos e preparação do repositório.

## Resultado esperado desta fase

Tornar os limites da referência revisáveis, localizar as variabilidades e preparar um harness que possa rejeitar violações arquiteturais.

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
- runbook a priori consultado e rastreado.

## Decisões pendentes da referência

- licença;
- baseline de SLOs obrigatória versus apenas sugerida;
- backend opcional de streaming para alto volume;
- formato final de plugins de adapters;
- quanto código executável deve fazer parte do template v1.

## Decisões obrigatórias em cada projeto derivado

- classificação e retenção de dados;
- identidade, autorização e tenancy;
- canais e respectivos providers;
- agent runtime e modelos;
- MCPs/tools, permissões e aprovações;
- SLOs, capacidade e backup;
- política de memória e conhecimento.

## Riscos e bloqueios

- documentação pode divergir do scaffold se fitness functions não forem automatizadas;
- um projeto derivado pode remover invariantes por conveniência;
- funcionalidades profissionais ainda são arquitetura-alvo, não implementação completa.

## Gate

**Parcialmente atendido.** A arquitetura de referência pode ser revisada; uso produtivo de um projeto derivado continua bloqueado até as decisões específicas acima e os gates de verificação/operação.

## Próxima ação recomendada

Revisar este PR, aprovar os ADRs estruturais e então implementar a primeira fatia vertical: webhook canônico → inbox PostgreSQL → worker stub → outbox → canal web de teste.
