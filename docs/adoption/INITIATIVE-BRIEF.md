# Initiative brief

## Problema

Equipes que criam chats com IA repetem decisões de infraestrutura e frequentemente começam pelo framework, canal ou prompt. Isso produz sistemas acoplados, frágeis e difíceis de operar.

## Resultado esperado

Disponibilizar uma arquitetura de referência e um template que permita iniciar vários chats com:

- infraestrutura profissional já especificada;
- módulos e contratos estáveis;
- variabilidades explícitas;
- evolução por POC, MVP e Profissional;
- operação em Python e VPS sem serviços gerenciados obrigatórios;
- capacidade de trocar canal, LLM, framework e MCP sem reescrever o núcleo.

## Usuários

- arquitetos e tech leads;
- programadores e agentes de código;
- equipes que constroem atendimento, suporte, vendas ou assistentes internos;
- operadores responsáveis por VPS e integrações.

## Owner e responsabilidade

- Sponsor/owner proposto: Caléo Santos — confirmar formalmente.
- Responsável técnico: pendente por projeto derivado.
- Segurança/operação: deve ser nomeado antes de uso produtivo.

## Perfil de adoção

**Padrão**, com tratamento **crítico** para módulos que executam ações irreversíveis, processam dados regulados ou cruzam tenants.

## Escopo desta referência

- arquitetura e limites do monólito modular;
- múltiplos canais por adapters;
- Supervisor/Subagentes por porta neutra;
- filas, workers, outbox, heartbeat, watchdog e DLQ;
- MCP/tools, memória, conhecimento, handoff e observabilidade;
- contracts, threat model, fitness functions e runbooks;
- harness Python mínimo e caminho de implantação em VPS.

## Fora do escopo

- um produto de negócio pronto;
- prompts e agentes universais;
- fornecedor de WhatsApp ou Teams obrigatório;
- framework único de agentes;
- UI administrativa final;
- alta disponibilidade multi-VPS como default;
- compliance automático sem decisões do projeto derivado.

## Permissões do agente neste repositório

Permitido:

- ler e editar documentação, contratos, testes e scaffold em branch;
- propor ADRs e critérios de verificação;
- executar checks locais/CI sem secrets.

Exige aprovação:

- merge na `main`;
- alteração de licença;
- publicação de pacote/imagem;
- secrets, deploy, migração destrutiva ou acesso a produção;
- mudança de invariantes da constituição.
