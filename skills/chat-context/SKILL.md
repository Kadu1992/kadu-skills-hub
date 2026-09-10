---
name: chat-context
description: Ativada quando o usuário digita `/chat-context`, `/chat-context history <termo>`, `/chat-context historico <termo>`, ou solicita "salvar contexto", "retomar contexto", "iniciar contexto". Gerencia a persistência de contexto em tempo real no arquivo `chat_context/current_context.md` e histórico imutável em `chat_context/history/YYYYMMDD_HHMMSS_Topico.md` seguindo o padrão ISO 8601 e links Markdown universais `[Nome](file:///...)`.
---

# Skill: chat-context (Persistência Global de Contexto)

Esta skill permite salvar, sincronizar e consultar o contexto de conversas entre sessões do Antigravity IDE (ou qualquer outra IDE compatível) sem perder o fio da meada.

---

## 🗂️ Estrutura de Armazenamento do Projeto

Quando acionada, a skill gerencia a seguinte estrutura na raiz do projeto ativo:

```text
raiz_do_projeto/
└── chat_context/
    ├── current_context.md               # 📌 Contexto VIVO e ativo da sessão atual
    ├── README.md                        # 📄 Guia e estrutura explicativa da pasta chat_context
    └── history/                          # 📂 Snapshots históricos imutáveis (ISO 8601)
        └── YYYYMMDD_HHMMSS_Topico.md
```

---

## 🚀 Fluxo de Operação

### 1. Inicialização de Sessão (`/chat-context` ou `iniciar contexto`)
1. **Idempotência**: Verifica se a pasta `chat_context/` já existe na raiz do projeto.
   - **Se NÃO existir**:
     - Cria a pasta `chat_context/`, o arquivo `chat_context/README.md` e a subpasta `chat_context/history/` (garantindo a criação física e visual no gerenciador de arquivos e IDEs).
     - Mapeia a estrutura inicial do projeto (arquivos principais, README, configs, etc.).
     - Instancia o arquivo `chat_context/current_context.md` com o mapeamento e o resumo da troca atual.
   - **Se JÁ existir**:
     - Garante que o arquivo `chat_context/README.md` e a subpasta `chat_context/history/` existam fisicamente.
     - Lê o arquivo `chat_context/current_context.md` existente.
     - Resume para o usuário o estado onde a conversa parou e retoma a sessão.
2. **Atualização Automática do Contexto Vivo**: Ao concluir tarefas, modificações em arquivos ou conversas conceituais/aprendizados importantes no chat, atualiza as seções do `chat_context/current_context.md`.
3. **Geração Automática de Snapshots no Histórico (`history/`)**: Ao concluir um tópico importante, refatoração significativa, decisão arquitetural, encerramento de bloco de tarefas ou solicitação do usuário ("salvar contexto", "snapshot"):
   - Gere obrigatoriamente um arquivo snapshot em `chat_context/history/YYYYMMDD_HHMMSS_Topico.md` seguindo o formato ISO 8601.
   - Registre a data/hora local atual, o resumo do tópico, as decisões e os arquivos afetados.

---

### 2. Consulta ao Histórico Antigo (`/chat-context historico <termo>` ou `/chat-context history <termo>`)
1. **NUNCA** leia todos os arquivos de `chat_context/history/` simultaneamente (para não gastar tokens).
2. Execute a ferramenta `grep_search` filtrando pelo termo de busca em `chat_context/history/`.
3. Traga no chat a síntese dos resultados encontrados.
4. Inclua sempre o link de arquivo Markdown universal clicável no formato:
   `[Nome do Arquivo](file:///caminho/absoluto/ou/relativo/chat_context/history/YYYYMMDD_HHMMSS_Topico.md)`

---

## 📄 Template Padrão do `current_context.md`

```markdown
---
type: log
category: contexto
tags: [chat-context, resumo-sessao]
updated_at: YYYY-MM-DD HH:mm:ss
---

# 📌 Contexto Ativo da Sessão — [Nome do Projeto]

## 🎯 Objetivo Atual
[Resumo do objetivo principal em andamento]

## 🛠️ Últimas Alterações Realizadas
- [x] Alteração 1 realizada em [Arquivo](file:///caminho)
- [x] Ajuste 2 concluído

## 💬 Estado da Última Troca de Mensagens
- **Último pedido do usuário**: "[Texto resumido do último pedido]"
- **Status da IA**: "[Status e síntese da resposta dada]"

## 🧠 Decisões Arquiteturais & Regras Estabelecidas
- Decisão 1
- Regra 2

## ⏳ Próximos Passos & Pendências
- [ ] Pendência 1
- [ ] Pendência 2

## 📂 Arquivos Afetados Recentes
- [Nome do Arquivo](file:///caminho/do/arquivo)
```

---

## 📜 Regras de Nomeação do Histórico (Snapshots)
- Formato do nome: `YYYYMMDD_HHMMSS_Topico.md` (Ex: `20260722_193500_RAG_Lembretes.md`).
- Formato ISO 8601 garante ordenação cronológica exata no Windows Explorer, Obsidian e IDEs.
- Dentro do arquivo, inclua o cabeçalho formatado em português: `Data de Registro: DD/MM/AAAA HH:mm:ss`.
