# Pilar: Segurança

## Intenção

Proteger as fronteiras entre canal, identidade, modelo, dados, tools, tenants, operadores e telemetria; reduzir agência excessiva sem depender apenas do prompt.

Esta adaptação preserva as invariantes de [Constituição](../../specs/constitution.md), [runtime](../architecture/runtime.md), [dados e estado](../architecture/data-and-state.md) e [segurança existente](../security/threat-model.md). Os IDs abaixo mantêm rastreabilidade com o AWS Well-Architected Generative AI Lens; o texto e os controles foram reescritos para o cenário deste repositório.

## Práticas adaptadas

| ID | Adaptação para chats/assistentes | Evidência mínima | Fase principal | Gate |
|---|---|---|---|---|
| **GENSEC01-BP01**<br>Menor privilégio nos endpoints de modelos | Separar identidades de API, worker, avaliação e administração. Cada papel acessa somente modelos, regiões, ações e guardrails necessários; o tenant nunca escolhe um ARN ou endpoint arbitrário. | Policies IAM testadas, deny explícito para rotas não permitidas, Access Analyzer e testes de autorização. | Implantação | MVP |
| **GENSEC01-BP02**<br>Comunicação privada entre aplicação e modelos | Executar workloads em sub-redes privadas, limitar egress e usar endpoints privados quando suportados. Quando uma API pública for necessária, exigir TLS, allowlist de destino, proxy/egress controlado e rotação de credenciais. | Diagrama de rede, security groups, VPC endpoints quando aplicáveis, regras de egress e teste de conectividade. | Implantação | MVP |
| **GENSEC01-BP03**<br>Menor privilégio do modelo ao acessar dados | O modelo não recebe credenciais nem acesso amplo. RAG, SQL e tools passam por adapters que aplicam tenant, row/column/document ACL, metadata filters e finalidade antes de recuperar dados. | Testes cross-tenant, políticas por fonte, consultas parametrizadas, trilha de autorização e fixtures negativas. | Desenvolvimento e implantação | MVP |
| **GENSEC01-BP04**<br>Monitorar acesso a serviços e modelos | Auditar invocação, alteração de configuração, mudança de policy, acesso administrativo e uso anômalo. Diferenciar plano de controle de conteúdo de inferência; não registrar prompts completos por padrão. | CloudTrail e logs de aplicação, alertas de abuso/quota, painel por principal e processo de investigação. | Implantação e operação | MVP |
| **GENSEC02-BP01**<br>Aplicar guardrails a respostas nocivas ou incorretas | Combinar filtros de conteúdo, políticas de tópico, detecção de PII, grounding/citações, schemas, validação de pós-condição e regras determinísticas. Guardrail de modelo não substitui autorização nem confirmação. | Política de entrada/saída, testes adversariais, thresholds, casos de bypass, fallback e handoff. | Desenvolvimento e implantação | MVP |
| **GENSEC03-BP01**<br>Monitorar plano de controle e acesso a dados | Registrar alterações de modelo, prompt, guardrail, tool, knowledge base, índices, roles e secrets; registrar acessos privilegiados e exportações. Alertas devem cobrir mudança fora do pipeline. | Audit events imutáveis, CloudTrail, Config ou equivalente, alertas de drift e segregação de funções. | Implantação e operação | MVP |
| **GENSEC04-BP01**<br>Manter catálogo de prompts seguro | Proteger prompts como código e política: acesso restrito, revisão, versão, hash, assinatura ou provenance, scan de secrets, variáveis allowlisted e separação entre conteúdo confiável e não confiável. | CODEOWNERS, revisão, secret scanning, artefato imutável, testes de integridade e rollback. | Customização e melhoria contínua | MVP |
| **GENSEC04-BP02**<br>Sanitizar e validar entradas | Autenticar origem; limitar tamanho, tipo e frequência; validar texto, mídia, URLs e arquivos; bloquear SSRF, zip bombs e codecs perigosos; marcar conteúdo externo como dado não confiável e preservar instruções de sistema fora dele. | Schemas, limites, sandbox de mídia, allowlists, casos de prompt injection e testes de abuso. | Desenvolvimento e implantação | MVP |
| **GENSEC05-BP01**<br>Limitar agência e permissões de agentes | Filtrar o catálogo de tools por identidade, tenant, estado e risco; usar credenciais de curto prazo; impor max steps, tempo, tokens e custo; exigir confirmação/aprovação para mutações sensíveis; fornecer kill switch e reconciliação. | Tool policy, capability matrix, approvals, testes de tool abuse, trilha de decisão e cancelamento. | Customização e desenvolvimento | MVP |
| **GENSEC06-BP01**<br>Purificar dados de treinamento ou customização | Validar provenance, licenças, PII, secrets, malware, conteúdo adversarial, duplicatas e qualidade antes de fine-tuning, avaliação ou memória organizacional. Manter lineage e conjunto holdout independente. | Data card, scanners, quarentena, lineage, aprovação, versionamento e testes de poisoning. | Customização e desenvolvimento | Condicional |

## Aplicação no perfil AWS

- AWS IAM, IAM Identity Center e roles de workload implementam identidades separadas por papel; policies devem restringir modelos, ações e recursos.
- AWS KMS protege dados e artefatos; AWS Secrets Manager ou Parameter Store fornecem referências de secrets, nunca valores no repositório.
- AWS WAF, Application Load Balancer ou API Gateway protegem entrada conforme o perfil; a autenticação do webhook continua no adapter.
- Amazon Bedrock Guardrails é uma camada possível de segurança de entrada/saída, não substitui regras determinísticas, ToolPolicy ou ApprovalPolicy.
- AWS CloudTrail, CloudWatch, Config, GuardDuty e Security Hub podem compor detecção e auditoria conforme risco e conta.
- VPC endpoints e sub-redes privadas devem ser usados quando o serviço e a região oferecerem suporte; egress restante deve ser explícito.

## Métricas e sinais recomendados

- webhooks inválidos, replay, rate limit e payload rejeitado;
- tentativas cross-tenant e negações por policy;
- mudanças de IAM, prompt, guardrail, tool, knowledge e secret;
- prompt injection detectada, tool call bloqueada e aprovação exigida;
- PII/secrets removidos, arquivos rejeitados e URLs bloqueadas;
- acessos administrativos, exportações, replays e reconciliações;
- anomalias de uso de modelo, tokens, regiões e principais.

## Anti-padrões

- Usar uma role ampla compartilhada por API, worker, sender e administração.
- Entregar ao modelo todas as tools e confiar no system prompt para limitar ações.
- Tratar Bedrock Guardrails ou outro filtro como autorização transacional.
- Copiar ACLs de fontes para um índice sem sincronização, testes negativos e fail-closed.
- Registrar conteúdo integral, secrets ou tokens em logs, traces ou datasets de avaliação.

## Gate de revisão

A prática só recebe status **atendida** quando existe implementação, teste e evidência operacional vinculada à versão. Documento sem execução vale no máximo **parcial**. Use a [matriz de lifecycle e review](lifecycle-mapping-and-review.md) para registrar owner, status, risco e plano de melhoria.
