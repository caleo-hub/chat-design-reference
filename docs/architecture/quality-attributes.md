# Atributos de qualidade

Valores abaixo são defaults de referência; cada projeto deve aprovar seus SLOs.

## Confiabilidade

- nenhuma mensagem aceita é perdida silenciosamente;
- duplicidade de webhook não duplica efeito;
- crash entre resposta e envio é recuperável;
- resultado desconhecido é explícito;
- restore do banco é exercitado.

Indicadores: taxa de perda/duplicidade, idade da fila, DLQ, recovery success.

## Desempenho e UX

- webhook p95 sugerido < 500 ms sem depender de LLM;
- primeiro feedback (typing/ack) em poucos segundos;
- nudge configurável para turns longos;
- ordenação por conversa;
- streaming no web sem criar caminho transacional paralelo.

## Segurança e privacidade

- autenticação de webhooks/MCP/admin;
- menor privilégio por tool e tenant;
- PII fora de telemetria padrão;
- secrets fora de imagem/repo;
- retenção e exclusão definidas;
- actions críticas determinísticas/aprovadas.

## Operabilidade

- live/ready/dependency health;
- logs, métricas, traces e audit events;
- dashboard de fila/outbox/DLQ;
- deploy e rollback documentados;
- backup/restore e rotação de secrets;
- diagnóstico por correlation ID.

## Evolutividade

- segundo canal entra por adapter;
- framework de agentes é substituível;
- tools e events são versionados;
- módulos possuem APIs e import rules;
- configurações específicas ficam fora do core.

## Portabilidade

- Python + containers + PostgreSQL;
- sem dependência cloud obrigatória;
- APIs de LLM acessadas por adapters;
- observabilidade vendor-neutral como baseline.

## Custo

- budgets por turn/tenant;
- modelos por tarefa;
- cache/context management;
- concorrência limitada;
- métricas de tokens e custo;
- tarefas longas fora do worker principal.

## Limites do MVP em uma VPS

Uma VPS é ponto único de falha e não oferece alta disponibilidade. O MVP aceita esse risco somente com:

- backups externos;
- restore testado;
- imagens imutáveis e rollback;
- limites de recursos;
- monitoramento externo;
- capacidade conhecida.
