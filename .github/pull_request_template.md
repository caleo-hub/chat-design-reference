## Problema e objetivo

<!-- Qual problema esta mudança resolve? Qual resultado observável esperamos? -->

## Escopo e não objetivos

- Inclui:
- Não inclui:

## Fontes canônicas e decisões

- Spec relacionada:
- ADR relacionada:
- Contratos alterados:
- Threat model afetado: sim / não

## Mudanças

<!-- Resuma comportamento e módulos afetados; não liste apenas arquivos. -->

## Risco e compatibilidade

- Classe de risco: baixo / moderado / alto / crítico
- Compatibilidade: backward compatible / exige migração
- Dados pessoais ou secrets afetados: sim / não
- Efeito externo ou mutação: sim / não
- Estratégia de idempotência/reconciliação:

## Evidências

```text
make verify
<cole o resumo real do resultado>
```

- Testes adicionados:
- Contratos/fitness functions executados:
- Validação independente:

## Operação

- Métricas/logs/traces afetados:
- Rollout ou feature flag:
- Smoke test:
- Rollback/restauração:

## Checklist

- [ ] Li `AGENTS.md` e as fontes canônicas aplicáveis.
- [ ] A mudança preserva `specs/constitution.md` ou inclui ADR de exceção.
- [ ] Atualizei spec, contrato, ADR, ameaça e runbook quando necessário.
- [ ] Não introduzi acesso direto de framework/provider no núcleo.
- [ ] Toda mutação sujeita a retry possui idempotência e reconciliação.
- [ ] Toda mensagem durável de negócio passa pela outbox.
- [ ] Logs e traces não expõem dados sensíveis por padrão.
- [ ] Executei as verificações e registrei resultados reais.
- [ ] Existe caminho de rollback ou reconciliação.
