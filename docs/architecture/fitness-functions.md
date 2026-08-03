# Fitness functions

Fitness functions transformam princípios em poder de veto.

## Dependências

1. `core` não importa `adapters`, FastAPI, SQLAlchemy, LangChain, CrewAI ou MCP.
2. `orchestration` depende apenas de ports de agent runtime/tools.
3. SDKs de canal existem somente em adapters de canal/delivery.
4. cliente MCP existe somente no adapter MCP.
5. observability não é importada como fonte de decisão de negócio.

Ferramenta inicial: `import-linter` + testes AST quando necessário.

## Contratos

- JSON Schemas válidos;
- exemplos validam contra schemas;
- OpenAPI lint;
- `schema_version` obrigatório;
- mudanças incompatíveis detectadas;
- producer/consumer contract tests para MCP e canal.

## Invariantes operacionais

- webhook não instancia agent runtime ou tool gateway;
- worker não chama `ChannelAdapter.send` para mensagem de negócio;
- toda saída possui outbox record;
- mutating tool exige idempotency key;
- `outcome_unknown` não pode ser replayado automaticamente;
- claim/complete exige worker ownership;
- apenas um turn ativo por conversa;
- nudge é único por estágio.

## Segurança

- secret scanning;
- nenhum default `change-me`/token vazio permitido em produção;
- logs passam por redaction tests;
- webhook sem assinatura falha;
- cross-tenant access property tests;
- URLs de mídia obedecem política anti-SSRF;
- dependencies/images são verificadas.

## Confiabilidade

- duplicar webhook mantém um receipt/job;
- crash antes/depois do commit não perde nem duplica resposta;
- lease expirado é recuperável;
- timeout após mutação cria reconciliação;
- delivery event duplicado é idempotente;
- migrations sobem do zero em PostgreSQL real;
- backup é restaurável.

## Qualidade de agente

- tool trajectory permitida;
- nenhuma falsa afirmação de sucesso;
- confirmação obrigatória é inalcançável por rota alternativa;
- limite de loops/tools/tokens;
- prompts e grafos têm versão;
- baseline de eval não regride além do limiar aprovado.

## CI alvo

```text
format/lint
→ typecheck
→ unit
→ architecture
→ contracts
→ postgres integration
→ reliability/fault
→ security/dependencies
→ container/compose
→ eval smoke
```

Nem toda etapa existe na fundação v0.1; o STATUS deve registrar lacunas sem declarar prontidão falsa.
