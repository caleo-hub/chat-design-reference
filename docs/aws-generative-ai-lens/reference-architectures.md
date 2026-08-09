# Arquiteturas-base de chats e assistentes na AWS

## Princípio de seleção

As arquiteturas abaixo são perfis de implantação. Todas preservam os contratos do monólito modular e as portas de canal, modelo, knowledge, tools e persistência. Escolha a menor topologia que atenda risco, SLO, capacidade e equipe; introduza serviços adicionais somente com evidência e ADR quando a estrutura mudar.

## Arquitetura A: monólito modular gerenciado em ECS/Fargate

É o perfil AWS mais próximo da referência em VPS.

```mermaid
flowchart TB
    U[Usuários e canais] --> R53[Route 53]
    R53 --> CF[CloudFront opcional]
    CF --> WAF[AWS WAF]
    WAF --> ALB[Application Load Balancer]

    subgraph VPC[VPC - sub-redes privadas]
      API[ECS service: api]
      WORKER[ECS service: worker]
      SENDER[ECS service: sender]
      SCHED[ECS service: scheduler]
      ADMIN[ECS service: admin]
      DB[(Aurora PostgreSQL ou RDS PostgreSQL)]
      CACHE[(ElastiCache opcional)]
      API --> DB
      WORKER --> DB
      SENDER --> DB
      SCHED --> DB
      ADMIN --> DB
      WORKER --> CACHE
    end

    ALB --> API
    ALB --> ADMIN
    WORKER --> BR[Amazon Bedrock]
    WORKER --> SM[Amazon SageMaker AI opcional]
    WORKER --> KB[Knowledge / OpenSearch / Kendra / S3]
    WORKER --> TOOLS[APIs e MCPs autorizados]
    SENDER --> CH[APIs dos canais]
    S3[(Amazon S3: mídia, corpus, backups)]
    WORKER --> S3
    SEC[Secrets Manager + KMS] -.-> API
    SEC -.-> WORKER
    OBS[CloudWatch + CloudTrail + OpenTelemetry] -.-> API
    OBS -.-> WORKER
    OBS -.-> SENDER
```

**Quando usar:** MVP e produção com equipe pequena/média, preferência por containers, PostgreSQL como estado operacional e necessidade de escalar papéis separadamente.

**Invariantes:** mesma imagem por digest para os papéis; webhook não chama LLM; PostgreSQL mantém inbox/lease/outbox; sender é o único dono da entrega; admin é privado; observabilidade é best effort.

**Trade-offs:** mais simples que microsserviços, mas ainda exige operação de banco, containers, rede, migrations e capacity planning. Multi-AZ reduz falhas de infraestrutura, não elimina bugs ou falhas regionais.

## Arquitetura B: assistente RAG corporativo

```mermaid
flowchart LR
    C[Canal / Web] --> API[API + Identity]
    API --> ORCH[Orquestração]
    ORCH --> RET[KnowledgeRetriever]
    RET --> ACL[Autorização e metadata filters]
    ACL --> V[(Vector / hybrid search)]
    ACL --> SQL[Dados estruturados via tool]
    V --> DOC[(S3 / fontes sincronizadas)]
    ORCH --> LLM[Bedrock ou SageMaker AI]
    ORCH --> CIT[Validação de evidência e citações]
    CIT --> OUT[Outbox]
```

**Opções AWS:** Amazon Bedrock Knowledge Bases, Amazon OpenSearch Service, Amazon Kendra, Amazon S3, AWS Glue Data Catalog, Amazon Redshift e adapters SQL. Amazon Q Business ou Amazon Q in QuickSight podem ser produtos gerenciados quando o caso se encaixa.

**Controles essenciais:** ACL atual por documento/linha, tenant em toda consulta, provenance, freshness, proteção contra indirect prompt injection, dataset de retrieval, reconstrução de índice e resposta sem RAG apenas quando policy permitir.

## Arquitetura C: assistente transacional com tools e aprovação

```mermaid
flowchart TB
    MSG[Mensagem] --> IN[(Inbox)]
    IN --> SUP[Supervisor]
    SUP --> FLOW[State machine]
    FLOW --> LLM[LLM para linguagem/extração]
    FLOW --> TG[Tool Gateway]
    TG --> POL[ToolPolicy]
    POL -->|read-only| TOOL[API / MCP]
    POL -->|mutação sensível| APR[Approval]
    APR --> TOOL
    TOOL --> REC[Idempotência e reconciliação]
    REC --> RES[Turn result]
    RES --> OUT[(Transactional outbox)]
```

**Quando usar:** agendamento, suporte com atualização, tickets, pedidos, operações internas e qualquer fluxo que produz efeito externo.

**Controles essenciais:** tools não são chamadas diretamente pelo modelo; scopes e credenciais são resolvidos fora do prompt; mutações possuem idempotency key; outcome unknown bloqueia replay; confirmação e aprovação são persistentes; resposta só afirma sucesso após pós-condição.

## Arquitetura D: plataforma multi-tenant de GenAI/chat

```mermaid
flowchart TB
    APPS[Apps e canais dos tenants] --> GW[API / Model Gateway]
    GW --> AUTH[Identity, tenant, quotas e policy]
    AUTH --> ROUTE[Model / Agent Router]
    ROUTE --> MODELS[Bedrock, SageMaker AI, providers autorizados]
    ROUTE --> AGENTS[Agent Runtime]
    AGENTS --> CATALOG[Tool, prompt e model catalogs]
    AGENTS --> DATA[Knowledge e dados por tenant]
    CTRL[Control plane] --> AUTH
    CTRL --> CATALOG
    CTRL --> EVAL[Evaluation service]
    CTRL --> FIN[Metering e chargeback]
    OBS[Auditoria e observabilidade] -.-> GW
    OBS -.-> ROUTE
    OBS -.-> AGENTS
```

**Quando usar:** várias unidades de negócio, produtos ou tenants compartilham acesso governado a modelos, RAG, agents e ferramentas.

**Separação recomendada:**

- **control plane:** onboarding, modelos, prompts, policies, quotas, budgets, evals e releases;
- **data plane:** inferência e execução de turns;
- **tenant plane:** identidade, dados, tools, limites, chaves e custo;
- **operations plane:** auditoria, incidentes, DLQ, reconciliação e capacity.

**Controles essenciais:** isolamento em chaves e policies, quota por tenant, metering, data residency, catálogo aprovado, guardrails consistentes, model gateway sem acesso irrestrito e testes cross-tenant.

## Arquitetura E: contact center omnichannel

```mermaid
flowchart LR
    USER[Telefone / chat] --> CONNECT[Amazon Connect]
    CONNECT --> LEX[Amazon Lex V2 - intents estruturadas]
    CONNECT --> Q[Amazon Q in Connect / knowledge]
    CONNECT --> BEDROCK[Bedrock agent ou workflow]
    BEDROCK --> TG[Tool Gateway]
    CONNECT --> HUMAN[Agente humano]
    Q --> HUMAN
    BEDROCK --> HUMAN
    HUMAN --> CRM[CRM / sistemas]
```

**Estratégia de adoção:** começar por fluxos frequentes e simples; escalar para RAG e ações complexas; sempre preservar contexto no handoff. Voz, gravações e transcrições têm classificação e retenção próprias.

## Arquitetura F: event-driven/serverless

```mermaid
flowchart TB
    CH[Canal] --> APIGW[API Gateway]
    APIGW --> ING[Lambda ingress]
    ING --> Q[SQS FIFO ou fila durável]
    Q --> ORCH[Step Functions / workers]
    ORCH --> BR[Amazon Bedrock]
    ORCH --> TOOLS[Tools]
    ORCH --> STATE[(DynamoDB ou Aurora)]
    ORCH --> OQ[Outbox / delivery queue]
    OQ --> SEND[Lambda ou Fargate sender]
    EVT[EventBridge Scheduler] --> ORCH
```

**Quando usar:** carga muito variável, tarefas naturalmente event-driven e equipe preparada para limites de execução, duplicidade e observabilidade distribuída.

**Importante:** este perfil altera a decisão de PostgreSQL como fila operacional e a topologia de processos. Exige ADR, preservação de ordering/idempotência/outbox/reconciliação e testes equivalentes. Step Functions não elimina a necessidade de estado de negócio e audit events.

## Arquitetura G: modelo customizado ou self-hosted

```mermaid
flowchart LR
    ORCH[AgentRuntime / LLM port] --> ROUTER[Model adapter/router]
    ROUTER --> BR[Amazon Bedrock]
    ROUTER --> SMEP[SageMaker AI endpoint]
    ROUTER --> EKS[EKS / EC2 self-hosted]
    REG[Model catalog + evaluation] --> ROUTER
    DATA[Datasets e artifacts em S3] --> TRAIN[SageMaker AI training/customization]
    TRAIN --> REG
```

**Quando usar:** requisito de modelo próprio, modalidade, performance, isolamento ou economics que managed inference não atende.

**Controles essenciais:** model card, dataset/data card, lineage, artifact integrity, endpoint autoscaling, patching, vulnerability scan, capacity, drift, rollback, licença e plano de depreciação. O adapter mantém o núcleo independente.

## Mapeamento de módulos para serviços AWS

| Módulo da referência | Baseline AWS | Alternativas/observações |
|---|---|---|
| edge e channels | Route 53, CloudFront, WAF, ALB/API Gateway | adapter continua validando assinatura do provider |
| identity | IAM Identity Center, Cognito ou IdP externo | identidade de usuário não é a role de workload |
| jobs/inbox/outbox | Aurora/RDS PostgreSQL | SQS/Step Functions somente por ADR e contratos equivalentes |
| compute | ECS/Fargate com a mesma imagem por papel | EKS, Lambda ou EC2 conforme perfil |
| model access | Amazon Bedrock | SageMaker AI ou provider externo por adapter |
| agent runtime | runtime próprio em worker; Bedrock Agents opcional | framework permanece atrás de `AgentRuntime` |
| tools | Tool Gateway próprio; APIs privadas; MCP | Bedrock Agent action groups são adapter, não bypass de policy |
| knowledge | Bedrock Knowledge Bases, OpenSearch, Kendra, S3 | Redshift/Glue/SQL para dados estruturados |
| memory | PostgreSQL e stores governados | ElastiCache somente para cache, não verdade operacional |
| media/corpus | S3 com KMS e lifecycle | malware scan, metadata, retenção e URL curta |
| secrets | Secrets Manager/Parameter Store + KMS | nunca em imagem, prompt ou log |
| observability | CloudWatch, CloudTrail, ADOT/X-Ray | OpenTelemetry como contrato neutro |
| delivery | ECS/Lambda sender para APIs dos canais | status do provider volta como evento deduplicado |
| CI/CD | GitHub Actions ou AWS CodePipeline/CodeBuild | imagens no ECR por digest, IaC e gates |

## Matriz de escolha

| Necessidade dominante | Arquitetura inicial | Evolução provável |
|---|---|---|
| chat profissional em produção | A | B ou C conforme knowledge/tools |
| consulta corporativa com fontes | A + B | D quando várias unidades compartilham plataforma |
| ações transacionais | A + C | approvals avançados e multi-Region quando SLO exigir |
| contact center | E | C para ações e B para knowledge |
| muitos produtos/tenants | D | células por região/tenant e control plane separado |
| carga altamente variável | F | Fargate para tarefas longas e Aurora para transações |
| modelo próprio | A + G | EKS/EC2 apenas com capacidade operacional comprovada |

## Critérios antes de escolher um serviço

- contrato e portabilidade necessária;
- regiões, residência e classificação de dados;
- modelo de responsabilidade e acesso;
- quota, throughput, latência e falhas;
- custo total e compromisso;
- observabilidade e auditabilidade;
- backup, restore, versionamento e depreciação;
- compatibilidade com idempotência, outbox e reconciliação;
- competência da equipe e runbook.
