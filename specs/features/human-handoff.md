# Feature — Handoff e aprovação humana

## Objetivo

Permitir que incerteza, política ou falha sejam assumidas por uma pessoa sem perder contexto, duplicar atendimento ou burlar a outbox.

## Estados

```text
pending → notified → claimed → in_progress → resolved
                              ↘ dismissed
pending/notified → expired
```

Aprovação pode ter `approved`, `rejected`, `edited` ou `cancelled`.

## Dados mínimos

- tenant/conversation/turn;
- reason code e risk class;
- resumo sanitizado;
- evidências e links internos;
- ação solicitada e parâmetros redigidos;
- SLA e assignee;
- decisão, motivo e auditoria;
- continuation token/state.

## Invariantes

- apenas um operador possui claim ativo;
- resposta humana passa pela outbox;
- aprovação não altera silenciosamente parâmetros;
- expiração não significa aprovação;
- retomada revalida estado e autorização;
- replay de `outcome_unknown` requer reconciliação.

## Critérios de aceitação

- dois operadores não resolvem simultaneamente;
- decisão aparece no audit trail;
- turn retoma do estado persistido;
- usuário recebe mensagem coerente e não detalhes internos;
- handoff sem assignee/SLA gera alerta;
- operador não acessa tenant fora da função.
