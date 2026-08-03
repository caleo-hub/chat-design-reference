# Contribuindo

## Princípios

Mudanças devem preservar os limites do monólito modular e manter a referência independente de canal, framework e provedor.

## Fluxo

1. Abra ou associe uma issue quando a mudança alterar comportamento ou arquitetura.
2. Crie uma branch pequena.
3. Atualize spec/ADR antes ou junto do código.
4. Execute `make verify`.
5. Abra PR com problema, decisão, evidências, riscos e rollback.

## Quando criar ADR

Crie ADR para decisões que:

- alteram fronteira ou direção de dependência;
- introduzem tecnologia central;
- mudam persistência, entrega, idempotência ou autorização;
- afetam todos os projetos derivados;
- rejeitam uma alternativa plausível e relevante.

## Compatibilidade

Contratos em `contracts/` são públicos para adapters e projetos derivados. Mudanças incompatíveis exigem nova versão e período de migração.

## Dependências

Toda dependência nova precisa de:

- motivo e alternativa considerada;
- licença compatível;
- estado de manutenção;
- impacto em segurança e operação;
- localização correta no adapter, sem contaminar o núcleo.

## Pull request

Inclua:

- objetivo e não objetivos;
- arquivos e módulos afetados;
- critérios atendidos;
- comandos e resultados;
- risco residual;
- migração e rollback;
- documentos/ADRs atualizados.