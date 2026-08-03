# Segurança

## Relato de vulnerabilidade

Não publique vulnerabilidades exploráveis em issue aberta. Use o canal privado de segurança configurado pelo mantenedor do repositório. Enquanto esse canal não estiver definido, contate diretamente o owner do repositório.

## Regras da referência

- secrets nunca entram no Git;
- webhooks precisam de autenticação, replay protection e limite de payload;
- mídia remota exige allowlist/proxy, timeout, limite de bytes e validação de tipo;
- identidade de canal não equivale automaticamente a identidade de negócio;
- tool calls usam allowlist, escopo, timeout, auditoria e resultado estruturado;
- operações destrutivas ou financeiras exigem autorização determinística e, quando aplicável, aprovação humana;
- logs e traces usam identificadores opacos e sanitização;
- MCP HTTP deve ser autenticado; token passthrough é proibido;
- dados de tenants não podem compartilhar namespace sem controles explícitos;
- dependências e imagens devem ser fixadas e verificadas.

Veja `docs/security/threat-model.md` antes de derivar um produto.