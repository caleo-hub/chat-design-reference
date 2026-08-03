# Constituição da arquitetura

Estas regras governam a referência e os projetos derivados. Exceções exigem ADR, risco explícito, evidência e aprovação humana proporcional.

## 1. O núcleo é independente de canal, framework e provider

**Regra:** domínio e aplicação não importam FastAPI, SDKs de WhatsApp/Teams, ORM, LangChain, CrewAI, SDK de LLM ou cliente MCP.

**Motivo:** essas tecnologias são variabilidades, não regras do produto.

**Verificação:** import-linter e testes de arquitetura.

## 2. Todo canal entra por um envelope canônico versionado

**Regra:** adapters convertem payloads externos para `ChannelEnvelope`; módulos internos não leem payload bruto de provider.

**Motivo:** preservar portabilidade e reduzir lógica duplicada.

**Verificação:** JSON Schema, contract tests e ausência de tipos de provider fora de adapters.

## 3. Webhooks são rápidos e não executam IA

**Regra:** a entrada autentica, valida, deduplica, persiste e responde. LLM, MCP, mídia pesada e efeitos externos rodam em workers.

**Motivo:** proteger disponibilidade e permitir retry/replay.

**Verificação:** teste de dependências e teste de tempo sem adapters externos.

## 4. Processamento é at-least-once e efeitos são idempotentes

**Regra:** cada mensagem, turn, tool mutation e entrega possui chave de idempotência, escopo e política de retenção.

**Motivo:** duplicidade é esperada em webhooks, filas e falhas de rede.

**Verificação:** testes de repetição e concorrência.

## 5. Respostas duráveis passam pela transactional outbox

**Regra:** nenhuma mensagem de negócio é enviada diretamente pelo worker de conversa. A resposta e a outbox são gravadas na mesma transação; um sender possui a entrega.

**Motivo:** eliminar a janela entre commit e chamada ao provider.

**Verificação:** fitness function de imports/chamadas e testes de crash.

## 6. Estado operacional, conversacional e telemetria são separados

**Regra:** fila/leases/outbox/DLQ não dependem do checkpointer do framework nem do backend de observabilidade.

**Motivo:** cada estado tem ciclo de vida, disponibilidade e finalidade diferentes.

**Verificação:** schema e dependências dos módulos.

## 7. LLM propõe; regras críticas decidem

**Regra:** autorização, confirmação, limites, transações, roteamento crítico e pós-condições são validados em código. O LLM não pode converter falha em sucesso.

**Motivo:** linguagem probabilística não é controle transacional.

**Verificação:** state machines, testes de inalcancabilidade e schemas de resultado.

## 8. Tools usam porta própria e menor privilégio

**Regra:** tools são carregadas por escopo, com allowlist, timeout, auditoria, schema e política de mutação. MCP é o protocolo preferido para fronteiras externas, não um atalho para expor tudo ao modelo.

**Motivo:** reduzir blast radius e acoplamento.

**Verificação:** testes de catálogo e autorização.

## 9. Retry nunca oculta resultado desconhecido

**Regra:** timeout após possível efeito externo produz `outcome_unknown` e reconciliação; não há replay automático cego.

**Motivo:** evitar duplicação de efeitos irreversíveis.

**Verificação:** fault injection entre request, resposta e persistência.

## 10. Operação é parte do comportamento

**Regra:** jobs possuem lease renovável, heartbeat, watchdog, timeout, cancelamento, DLQ, métricas e runbook. Health distingue liveness, readiness e dependências.

**Motivo:** processo vivo não significa serviço utilizável.

**Verificação:** testes de recuperação e dashboards.

## 11. Usuário recebe progresso sem promessas falsas

**Regra:** typing e nudges são idempotentes, canceláveis e nunca afirmam conclusão antes da pós-condição persistida.

**Motivo:** melhorar UX sem comprometer verdade transacional.

**Verificação:** testes temporais e de cancelamento.

## 12. Dados sensíveis não entram em telemetria por padrão

**Regra:** logs, métricas e traces usam IDs opacos e campos allowlisted. Conteúdo integral exige decisão de retenção e controle de acesso.

**Motivo:** reduzir exposição e custo de governança.

**Verificação:** redaction tests e scanning.

## 13. Contratos evoluem explicitamente

**Regra:** APIs, eventos, tools, prompts e grafos carregam versão. Mudança incompatível requer nova versão, contract tests e rollout coordenado.

**Motivo:** impedir quebra silenciosa entre adapters e projetos derivados.

**Verificação:** schemas e checks de compatibilidade.

## 14. O monólito permanece modular

**Regra:** módulos possuem API pública, ownership e direção de dependências. Compartilhar deploy e banco não autoriza acesso arbitrário a tabelas ou detalhes internos.

**Motivo:** conservar simplicidade operacional sem criar acoplamento estrutural.

**Verificação:** import rules, revisão de migrations e testes de arquitetura.

## 15. Toda automação tem interrupção, auditoria e rollback

**Regra:** deploy, migrations, tool mutations, replays e aprovações produzem evidência e possuem mecanismo de interrupção ou reconciliação.

**Motivo:** autonomia é proporcional à reversibilidade.

**Verificação:** runbooks, audit events e exercícios.
