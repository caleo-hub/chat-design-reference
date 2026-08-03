# Modelo de falhas e resiliência

## Princípio

Falhas externas são normais. O sistema classifica o que sabe, o que pode repetir e o que precisa reconciliar.

## Taxonomia

| Classe | Exemplo | Tratamento |
|---|---|---|
| validação | payload/schema inválido | rejeição conhecida, sem retry |
| autenticação/autorização | assinatura/token inválido | rejeição + auditoria/rate limit |
| transitória conhecida | 429, 503 antes do efeito | retry com backoff/jitter |
| permanente | recurso inexistente, regra inválida | resposta estruturada/handoff |
| timeout antes do efeito comprovado | conexão não estabelecida | retry conforme operação |
| resultado desconhecido | timeout após mutação possível | reconciliação, nunca replay cego |
| bug/invariante | estado impossível | falha, DLQ, alerta e bloqueio |
| capacidade | fila, CPU, memória, disco | backpressure e degradação |

## Retry

Todo retry define:

- operações elegíveis;
- máximo e deadline;
- backoff exponencial com jitter;
- `Retry-After` quando disponível;
- idempotency key;
- condição de saída;
- destino após esgotar.

Não aplicar retry genérico em POST/mutação.

## Circuit breaker

Breakers separados para:

- LLM provider;
- cada MCP server;
- cada provider de canal;
- storage/mídia externa;
- fonte de conhecimento.

Estados: closed → open → half-open. Enquanto aberto, o sistema falha rápido, preserva workers e escolhe fallback permitido.

## Bulkheads

Semáforos independentes limitam:

- turns simultâneos;
- transcrições/visão;
- tool calls por server;
- envios por canal;
- jobs longos;
- chamadas por tenant.

## Backpressure

Quando capacidade se aproxima do limite:

- continuar recebendo apenas se houver espaço durável;
- rejeitar/retardar novos requests conforme política;
- reduzir concorrência de tarefas caras;
- priorizar cancelamento, handoff e mensagens operacionais;
- alertar por idade da fila, não apenas tamanho.

## Degradação segura

- observabilidade indisponível não derruba atendimento;
- knowledge indisponível pode gerar resposta sem RAG apenas se policy permitir;
- MCP de mutação indisponível não vira sucesso simulado;
- canal com falha mantém outbox e informa operação;
- LLM indisponível pode usar resposta determinística/handoff, não inventar.

## DLQ

DLQ contém:

- source kind/ID;
- correlation ID;
- failure code/fingerprint;
- attempts e timestamps;
- retryable;
- outcome unknown;
- resumo sanitizado;
- status e resolução.

Replay exige motivo e é bloqueado para `outcome_unknown` até reconciliação.

## Testes de caos mínimos do MVP

- matar worker antes/depois do commit;
- expirar lease durante LLM;
- duplicar webhook e delivery event;
- timeout depois de tool mutation;
- provider aceitar envio e resposta se perder;
- MCP ficar indisponível;
- PostgreSQL reiniciar;
- disco/backup atingir limiar;
- restore em ambiente vazio.
