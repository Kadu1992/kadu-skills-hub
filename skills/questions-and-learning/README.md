# 📝 Skill: `questions-and-learning`

Converte o arquivo `questions.md` de notas brutas em dois arquivos Markdown versionados — um com as dúvidas organizadas e outro com as respostas — salvos automaticamente na pasta `chat_questions/`.

---

## 📦 Instalação

Instale diretamente no seu projeto com um único comando:

```bash
npx skills add Kadu1992/questions-and-learning
```

Ou instale globalmente na sua máquina/IDE:

```bash
npx skills add Kadu1992/questions-and-learning -g
```

> **Dica**: Esta skill também pode ser instalada via catálogo central [Kadu Skills Hub](https://github.com/Kadu1992/kadu-skills-hub) (`npx skills add Kadu1992/kadu-skills-hub`).

---

## ⚡ Ativação

A skill pode ser acionada em múltiplos cenários:

| Cenário / Gatilho | Exemplo |
|---|---|
| Slash command na IDE | `/questions-and-learning`, `/chat-questions` ou `/questions` |
| Skill invocada diretamente no chat, sem anexo (primeira execução) | *(digitar o nome da skill e dar enter)* |
| Arquivo `questions.md` enviado **sem mensagem** (arrastar e soltar) | *(sem texto)* |
| Arquivo `questions.md` com menção de conversão | `"converte esse questions.md"` ou `"organiza as perguntas"` |

Nenhuma instrução adicional é necessária. O fluxo completo executa imediatamente.

### 🆕 Primeira execução (setup automático)

Se `chat_questions/questions.md` **ainda não existe**, a skill:
1. Cria a pasta `chat_questions/`
2. Cria dentro dela um `questions.md` **vazio**
3. Pede para o usuário preencher o arquivo e rodar a skill novamente
4. **Não** executa a conversão nessa primeira chamada

Se `chat_questions/questions.md` **já existe**, a skill ignora a criação e segue direto para o fluxo normal de conversão descrito abaixo.

---

## 📂 Saída

Dois arquivos versionados são criados na pasta `chat_questions/`:

```
chat_questions/
├── duvidas-v1.md   ← dúvidas organizadas em seções com emojis
└── resposta-v1.md  ← respostas técnicas ponto a ponto + tabela de ações
```

O `N` da versão é detectado automaticamente — se já existem `v1` e `v2`, o próximo será `v3`.

---

## 🔄 Fluxo de execução

```
Skill acionada
    │
    ▼
[Passo 0] chat_questions/questions.md existe?
          • NÃO → cria pasta + questions.md vazio → para aqui
          • SIM → segue para o Passo 1
    │
    ▼
[Passo 1] Detecta versão N (analisa chat_questions/)
    │
    ▼
[Passo 2] Converte questions.md → duvidas-vN.md
          • Agrupa por temas com seções numeradas
          • Preserva todo o conteúdo original
          • Usa emojis, negrito, backticks, blockquotes
    │
    ▼
[Passo 3] Lê duvidas-vN.md → gera resposta-vN.md
          • Responde cada dúvida na mesma ordem
          • Marca status: ✅ Confirmado / 🔧 Será implementado / 💬 Discussão
          • Inclui tabela de Ações com prioridade
    │
    ▼
[Passo 4] Confirma no chat com paths dos dois arquivos
```

---

## 📄 Estrutura do `duvidas-vN.md`

```markdown
# 📋 Título — Contexto Detectado

> Contexto do projeto/arquivo

---

## 1. 🎯 Nome da Seção

### 1.1 Subseção
- Item com **termo-chave** em negrito
- Arquivo em `backtick`
- **Dúvida:** pergunta em aberto

*Documento gerado em: [contexto] — vN*
```

**Temas detectados automaticamente:**

| Conteúdo | Seção gerada |
|---|---|
| UI, cards, layout | `🃏 Interface / Cards / Layout` |
| Cálculos, valores | `📊 Cálculos e Valores` |
| Erros visuais | `🐛 Bugs` |
| Fluxo, lógica | `❓ Dúvidas de Lógica` |
| Regras de negócio | `📋 Regras de Negócio` |
| Arquivos, versões | `🗂️ Arquivos e Versionamento` |
| Automações | `🤖 Automações` |
| Próximos passos | `🔜 Próximos Steps` |

---

## 💬 Estrutura do `resposta-vN.md`

```markdown
# ✅ Respostas — vN

---

## 1. [Mesma seção do duvidas-vN.md]

### 1.1 Subseção — ✅ Confirmado
- Resposta direta e técnica.

---

## 📋 Resumo de Ações Imediatas

| # | Ação | Prioridade | Status |
|:--|:-----|:-----------|:-------|
| 1 | ...  | Alta       | ⬜     |
```

---

## 📌 Regras importantes

- **Nunca remove conteúdo** — todo o `questions.md` original é preservado no `duvidas-vN.md`
- O `questions.md` é apenas fonte para conversão; o `.md` gerado é a fonte de verdade para as respostas
- A tabela de Ações no final do `resposta-vN.md` é obrigatória
- A resposta no chat é minimalista — apenas os paths dos arquivos gerados

---

## 🗂️ Localização
- **Local (Workspace Kadu_OS)**: `c:\Users\55119\iCloudDrive\iCloud~md~obsidian\Kadu_OS\.agents\skills\questions-and-learning\SKILL.md`
- **Global (IDE / Todos os Projetos)**: `C:\Users\55119\.gemini\config\skills\questions-and-learning\SKILL.md`