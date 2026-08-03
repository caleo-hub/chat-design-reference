# Feature — Receber mensagem de canal

## Objetivo

Aceitar eventos autenticados de qualquer canal, convertê-los para envelope canônico e persistir trabalho sem executar IA no request.

## Pré-condições

- channel account configurada;
- adapter conhecido;
- política de autenticação e limite definida;
- PostgreSQL disponível para escrita.

## Invariantes

- evento duplicado não cria segundo turn;
- payload não autenticado não é persistido como mensagem válida;
- LLM/tool/provider de saída não é chamado;
- receipt e inbox são atômicos;
- tenant/channel account vêm da configuração/autenticação, não apenas do payload.

## Happy path

1. provider chama webhook;
2. adapter verifica autenticidade e replay;
3. payload é validado e normalizado;
4. receipt é criado;
5. inbox/job é criado;
6. transação é commitada;
7. API responde 2xx/202 com correlation ID.

## Falhas

- JSON inválido → 400;
- assinatura inválida → 401/403;
- payload grande → 413;
- rate limit → 429;
- banco indisponível → 503, sem afirmar aceitação;
- tipo de evento irrelevante → 2xx skipped auditado, conforme provider;
- duplicado → 2xx/202 `duplicate`.

## Critérios de aceitação

- duas requisições concorrentes com mesmo provider event ID geram um receipt/job;
- o teste falha se agent runtime for instanciado pela rota;
- resposta ocorre sem depender de LLM/MCP;
- correlation ID aparece no receipt e no job;
- conteúdo sensível não aparece no log de acesso.

## Não objetivos

- interpretar intenção;
- baixar/transcrever mídia;
- entregar resposta;
- resolver identidade de negócio completa.
