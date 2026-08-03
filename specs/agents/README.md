# Especificações de agentes

Agentes são comportamento versionado, não apenas prompts.

Cada agente/subagente deve declarar:

- objetivo e não objetivos;
- entradas e estado permitido;
- saídas estruturadas;
- tools/scopes disponíveis;
- regras determinísticas externas ao prompt;
- handoff e aprovação;
- budgets de loops, tools, tokens, tempo e custo;
- exemplos, contraexemplos e evals;
- prompt/model/graph version;
- owner e política de rollout.

Use `supervisor.md` como referência e `subagent.template.md` para novos fluxos.
