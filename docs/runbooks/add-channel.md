# Runbook — Adicionar canal

1. Documentar provider, conta e fluxo de autenticação.
2. Criar fixtures reais sanitizadas.
3. Implementar `verify_webhook` com replay protection.
4. Implementar normalização para `ChannelEnvelope`.
5. Implementar capability profile.
6. Implementar renderer/sender e parser de delivery events.
7. Definir identity mapping e confiança.
8. Aplicar limites de payload/mídia/SSRF.
9. Criar contract tests e testes de duplicidade.
10. Validar texto alternativo para recursos não suportados.
11. Atualizar perfil, threat model e operação.

Gate: nenhum tipo/payload do provider aparece em orchestration/domain.
