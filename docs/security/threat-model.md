# Threat model

## Escopo

Entrada multi-canal, processamento de mensagens/mídia, LLM, Supervisor/Subagentes, memória, conhecimento, MCP/tools, outbox, operação e VPS.

## Ativos

- identidade e vínculo com tenant;
- conteúdo de conversas e anexos;
- memória e conhecimento privado;
- secrets de canais, LLMs e MCPs;
- autorização e catálogo de tools;
- tickets/transações/efeitos externos;
- audit trail e estado de reconciliação;
- disponibilidade da VPS e PostgreSQL.

## Adversários

- usuário malicioso;
- webhook forjado/replay;
- tenant tentando acessar outro tenant;
- prompt/tool injection em mensagem, mídia ou RAG;
- MCP/provider comprometido;
- operador interno além da função;
- dependência/imagem comprometida;
- agente de código com permissão excessiva.

## Ameaças e controles

| Ameaça | Cenário | Controle mínimo |
|---|---|---|
| spoofing de webhook | atacante envia evento falso | assinatura/token, timestamp, replay cache, TLS |
| account linking indevido | telefone/ID mapeado ao cliente errado | verificação, confidence e política identity |
| cross-tenant | ID previsível acessa dados alheios | tenant em chaves/queries, policy tests |
| prompt injection | usuário manda ignorar regras e chamar tool | tools por scope, policy determinística, output validation |
| indirect injection | documento/RAG contém instrução | separar dados/instruções, provenance e sanitização |
| tool abuse | LLM chama mutação destrutiva | classificação, allowlist, confirmação/approval e idempotência |
| MCP impersonation | server falso/coleta token | TLS, auth, audience, allowlist e config protegida |
| token passthrough | credencial de usuário chega ao server errado | tokens específicos, nunca repassar bearer arbitrário |
| SSRF/mídia maliciosa | URL interna, zip bomb, codec | proxy/allowlist, DNS/IP checks, size/time limits, sandbox |
| PII em telemetry | payload vai a traces/logs | redaction allowlist, IDs opacos, retention/access |
| replay de efeito | retry duplica ticket/pagamento | idempotency key e reconciliação |
| outcome unknown | timeout após mutação | estado explícito, bloquear replay, consultar provider |
| DoS/custo | spam gera LLM/tools caros | rate limit, quota, budgets, queue/backpressure |
| worker starvation | tool lenta ocupa todos slots | timeout, circuit breaker e bulkhead |
| admin compromise | token dá acesso total | rede privada, RBAC, MFA/IdP, audit e rotação |
| memory poisoning | fato falso vira memória permanente | memória curada, source e aprovação/revogação |
| supply chain | pacote/imagem comprometido | lock, scanning, SBOM, digest e revisão de dependência |
| backup leak | dump contém conversas/secrets | criptografia, acesso, retenção e teste de descarte |

## Operações de alto risco

Exigem aprovação humana/policy explícita:

- pagamento, exclusão, publicação ou alteração irreversível;
- envio massivo;
- mudança de identidade/tenant;
- reprocessamento com resultado desconhecido;
- exportação de dados;
- alteração de prompt/tool policy em produção;
- migration destrutiva.

## Dados e retenção

Decisões obrigatórias por projeto:

- classificação de texto, áudio, imagem e documentos;
- base legal/consentimento quando aplicável;
- retenção de payload bruto, memória, traces e backups;
- acesso de operadores;
- direito de exclusão e limitações de backup;
- região/localização de APIs externas.

## Segurança de LLM

- conteúdo externo é dado não confiável;
- system/policy não é único controle;
- limitar contexto e tools;
- validar schemas e pós-condições;
- proteger contra exfiltração por tool/URL;
- não revelar prompts, secrets ou topologia sensível;
- evals adversariais antes de rollout.

## Riscos residuais da referência

- uma VPS é ponto único de falha;
- provider de LLM/canal observa dados enviados conforme contrato;
- MCP tasks são experimentais na versão de referência;
- nenhum template substitui revisão jurídica/compliance do produto derivado.
