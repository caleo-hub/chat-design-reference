# Arquitetura multi-canal

## Envelope canônico

Todo evento externo é convertido para um `ChannelEnvelope` antes de entrar na aplicação. O envelope possui, no mínimo:

- `schema_version`;
- `event_id` e `provider_message_id`;
- `tenant_id`, `channel` e `channel_account_id`;
- `conversation_id` e `participant_id` externos;
- direção, timestamp e correlation ID;
- conteúdo tipado e anexos;
- `reply_to` e metadados sanitizados;
- capacidades do canal relevantes ao turno.

O payload bruto pode ser armazenado criptografado e com retenção curta para diagnóstico, mas nunca é o contrato interno.

## ChannelAdapter

```python
class ChannelAdapter(Protocol):
    async def verify_webhook(self, request: WebhookRequest) -> VerifiedWebhook: ...
    async def normalize(self, webhook: VerifiedWebhook) -> list[ChannelEnvelope]: ...
    async def render(self, message: OutboundMessage, capabilities: ChannelCapabilities) -> ProviderRequest: ...
    async def send(self, request: ProviderRequest) -> ProviderSendResult: ...
```

## Capacidades

Canais não oferecem a mesma UX. O domínio declara intenção; o adapter escolhe representação.

| Capacidade | Web | WhatsApp | Teams |
|---|---:|---:|---:|
| streaming token a token | sim | não usual | limitado |
| typing/presence | sim | provider-specific | sim |
| botões | sim | templates/interativos | adaptive cards |
| edição de mensagem | sim | provider-specific | sim |
| anexos grandes | configurável | limitado | configurável |
| delivery/read status | próprio | provider-specific | provider-specific |

Nunca codificar um fluxo essencial que só funciona porque um canal possui botão. Sempre existir alternativa textual.

## Identidade

`participant_id` identifica o participante no canal; não necessariamente uma pessoa ou cliente do domínio.

O módulo `identity` mantém vínculos com:

- tenant;
- subject interno;
- nível de confiança;
- método de verificação;
- validade e revogação.

Telefone, e-mail ou Teams user ID não devem ser usados como autorização sem política explícita.

## Entrada

1. verificar assinatura/token e timestamp;
2. rejeitar replay quando suportado;
3. limitar tamanho e tipo;
4. normalizar um ou mais eventos;
5. deduplicar por provider/event ID;
6. persistir receipt + inbox;
7. responder ao provider;
8. processar assíncronamente.

## Saída

1. aplicação cria `OutboundMessage` canônica;
2. outbox persiste canal/recipient/capabilities;
3. sender carrega adapter;
4. adapter renderiza e envia;
5. provider ID e aceite são persistidos;
6. webhooks de delivery atualizam estado idempotentemente.

## Canal web

O frontend próprio pode usar:

- POST para mensagem de entrada;
- SSE como default de streaming unidirecional;
- WebSocket quando houver colaboração/presença bidirecional real;
- cursor/event ID para reconexão;
- mesma inbox/outbox dos demais canais.

Streaming é uma projeção de eventos do turn, não um caminho transacional alternativo.
