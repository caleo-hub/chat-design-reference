# PRD — Chat Design Reference

## Objetivo

Fornecer uma referência reutilizável para chats com IA multi-canal, Supervisor/Subagentes, ferramentas MCP e operação em VPS.

## Capacidades obrigatórias da arquitetura

1. Receber mensagens de qualquer canal por adapter.
2. Normalizar eventos em envelope canônico versionado.
3. Autenticar, deduplicar e persistir antes do processamento.
4. Processar turns em workers com ordenação por conversa.
5. Executar Supervisor/Subagentes por porta neutra de framework.
6. Carregar tools por escopo e executar MCP com segurança.
7. Persistir estado conversacional e operacional separadamente.
8. Enviar respostas somente por outbox e sender.
9. Suportar retry, DLQ, lease, heartbeat, watchdog e reconciliação.
10. Informar progresso por typing/nudge sem prometer efeito não confirmado.
11. Permitir cancelamento, timeout e retomada.
12. Criar handoff/revisão humana estruturada.
13. Emitir logs, métricas, traces e eventos de auditoria correlacionados.
14. Executar em Docker Compose numa VPS sem serviço cloud gerenciado obrigatório.
15. Expor health, readiness e superfícies operacionais protegidas.

## Requisitos de customização

Cada projeto derivado deve poder escolher, por configuração e adapters:

- canais e providers;
- identidade e tenancy;
- agent runtime;
- LLM e parâmetros;
- agentes, subagentes e prompts;
- MCPs e tools;
- memória e conhecimento;
- políticas de aprovação;
- observabilidade e retenção.

## Restrições

- Python 3.12+ como baseline;
- PostgreSQL como fonte operacional padrão do MVP;
- monólito modular como estilo padrão;
- nenhuma dependência de Kubernetes ou serviço cloud gerenciado;
- rede externa somente para canais, LLMs e integrações configuradas;
- ações críticas não dependem apenas de decisão textual do LLM.

## Não objetivos

- criar um agente universal;
- impor LangChain ou CrewAI;
- esconder decisões de segurança atrás de defaults;
- oferecer alta disponibilidade automática numa única VPS;
- transformar todos os módulos em serviços de rede;
- implementar todos os providers no core.

## Critérios de sucesso da v1

- documentação e contratos cobrem todos os módulos;
- scaffold executa e passa em checks;
- import rules impedem dependências proibidas;
- uma fatia vertical de exemplo demonstra inbox → worker → outbox;
- runbook permite derivar um novo projeto sem conhecimento oral;
- threat model e decisões pendentes ficam explícitos.
