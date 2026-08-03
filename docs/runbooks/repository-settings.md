# Configuração do repositório no GitHub

Este runbook cobre controles que não vivem no Git e precisam ser aplicados uma vez nas configurações do repositório.

## 1. Marcar como template

Em **Settings → General**, habilite **Template repository**. Isso libera o botão **Use this template** sem preservar histórico, branches ou issues do repositório de referência.

## 2. Estratégia de merge

Configuração recomendada para esta referência:

- habilitar **Squash merging**;
- usar título do PR como título do commit;
- apagar automaticamente a branch após merge;
- desabilitar merge commit e rebase merge se a equipe quiser histórico linear e uma mudança arquitetural por commit.

Projetos derivados podem escolher outra política, mas devem registrá-la.

## 3. Proteção da `main`

Crie uma ruleset para a branch padrão:

- exigir pull request antes do merge;
- exigir o check `verify` do workflow `CI`;
- exigir resolução das conversas;
- bloquear force push e exclusão;
- exigir branch atualizada quando houver risco de integração concorrente;
- exigir revisão de `CODEOWNERS` para mudanças em specs, contratos, ADRs, segurança ou workflows quando houver mais de um mantenedor.

Em repositório mantido por uma única pessoa, permita bypass do owner para não bloquear correções emergenciais; registre o motivo no PR.

## 4. Segurança e supply chain

Habilite, conforme disponibilidade do plano:

- Dependabot alerts;
- Dependabot security updates;
- secret scanning;
- push protection para secrets;
- private vulnerability reporting;
- revisão periódica de permissões de GitHub Apps e Actions.

O token padrão de Actions deve permanecer somente leitura. Workflows com escrita precisam declarar `permissions` localmente e justificar o efeito.

## 5. Actions

- permitir apenas Actions confiáveis ou fixadas por versão/digest conforme a política da equipe;
- impedir que workflows de forks recebam secrets;
- manter ambientes de deploy com aprovação humana;
- não usar secrets de produção em testes de PR.

## 6. Metadados

Configure:

- descrição curta do repositório;
- tópicos como `ai-agents`, `chatbot`, `mcp`, `modular-monolith`, `python` e `reference-architecture`;
- website/documentação, quando existir;
- imagem social, quando a referência estiver pública e estável.

## 7. Release inicial

Depois do primeiro merge:

1. confirme CI verde na `main`;
2. crie a tag/release `v0.1.0`;
3. use a seção `0.1.0` do `CHANGELOG.md` como base das notas;
4. deixe explícito que a release é fundação arquitetural, não runtime produtivo.

## Evidência esperada

Registre no PR ou issue de governança:

- screenshot ou link da ruleset;
- checks obrigatórios;
- recursos de segurança habilitados;
- data da release;
- exceções aceitas e owner.
