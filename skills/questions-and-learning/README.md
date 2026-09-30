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

## 🚀 Como Funciona a Inicialização (Setup na Árvore da IDE)

> **💡 Dúvida Frequente**: *Preciso rodar o terminal toda vez que for usar a skill?*  
> **NÃO!** Você **nunca** é obrigado a rodar nada no terminal se não quiser.  
> Uma vez criada a pasta no projeto, ela permanece na sua árvore para sempre.

Você tem **duas formas** de gerar os arquivos na sua árvore:

### Opção 1: 100% Automática pelo Chat da IA (Recomendada — Sem Terminal)
Basta digitar `/questions-and-learning` (ou `/questions`, `/questions init`) no chat.  
A IA verifica se a pasta `chat_questions/` existe:
- Se ainda **não existir**, a própria IA cria instantaneamente a pasta, o `README.md` e o `questions.md` com template estruturado na árvore da sua IDE.
- Ela te devolve o link clicável direto para você começar a escrever.

### Opção 2: Pelo Terminal (Opcional — Atalho Imediato)
Se você acabou de rodar `npx skills add` no terminal e já quer ver a pasta brotar na árvore da IDE antes mesmo de abrir o chat com a IA, pode rodar:

```bash
python .agents/skills/questions-and-learning/scripts/init.py
```

*Esse comando é 100% opcional e idempotente: se a pasta já existir com anotações, ele preserva tudo sem sobrescrever nada.*

---

## 🔄 Fluxo do Dia a Dia (Depois que a pasta já existe)

Depois que a pasta `chat_questions/` já está na sua árvore, a sua rotina é ultra simples:

```text
1. Abra o arquivo chat_questions/questions.md na IDE e anote suas dúvidas livremente.
2. No chat da IA, digite /questions-and-learning (ou arraste o arquivo questions.md).
3. A IA lê suas anotações, organiza em duvidas-vN.md e responde tudo em resposta-vN.md!
```

---

## ⚡ Formas de Ativação no Chat

A skill é acionada de forma transparente em qualquer um destes cenários:

| Cenário / Gatilho | Exemplo |
|---|---|
| Comando slash principal | `/questions-and-learning` ou `/chat-questions` |
| Atalho curto | `/questions` |
| Setup inicial explícito | `/questions init` ou `/questions setup` |
| Chamada direta no chat | Digitar `questions-and-learning` e enviar |
| Arrastar e soltar o arquivo | Soltar `questions.md` no chat (sem digitar nada) |
| Menção textual | `"organiza as dúvidas desse questions.md"` ou `"responde as perguntas"` |

---

## 📂 Saída Gerada

Dois arquivos versionados são criados incrementalmente na pasta `chat_questions/`:

```text
chat_questions/
├── questions.md     ← suas anotações brutas (sempre preservadas)
├── README.md        ← guia explicativo da pasta
├── duvidas-v1.md    ← dúvidas organizadas em seções com emojis
└── resposta-v1.md   ← respostas técnicas ponto a ponto + tabela de ações
```

O número de versão `vN` é automático. Se já houver `v1` e `v2`, o próximo lote gerará `v3` automaticamente.

---

## 🔄 Fluxo Visual de Decisão da Skill

```text
Skill acionada no chat (ou python scripts/init.py)
    │
    ▼
[Passo 0] chat_questions/ existe com questions.md e README.md?
          • NÃO → Cria pasta + README.md + questions.md com template na árvore → Para aqui
          • SIM  → Se questions.md estiver preenchido com dúvidas, segue para o Passo 1
    │
    ▼
[Passo 1] Detecta versão N incremental (analisa chat_questions/)
    │
    ▼
[Passo 2] Converte questions.md → duvidas-vN.md
          • Agrupa por temas com seções numeradas e emojis
          • Preserva 100% do conteúdo original (não apaga nada)
    │
    ▼
[Passo 3] Lê duvidas-vN.md → gera resposta-vN.md
          • Responde cada dúvida na mesma ordem
          • Status: ✅ Confirmado / 🔧 Será implementado / 💬 Discussão
          • Inclui tabela de Resumo de Ações por prioridade
    │
    ▼
[Passo 4] Confirma no chat com links clicáveis dos arquivos gerados
```

---

## 📄 Formato do `duvidas-vN.md`

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

---

## 💬 Formato do `resposta-vN.md`

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

## 📌 Diretrizes Mandatórias da Skill

- **Preservação Total**: Nunca deleta nem resume conteúdo em `duvidas-vN.md`; todo o conteúdo bruto é preservado.
- **Fonte da Verdade**: O `questions.md` é a entrada; o `duvidas-vN.md` gerado é a base técnica das respostas.
- **Ações Imediatas**: Sempre inclui a tabela com prioridade (Alta / Média / Baixa) ao final de cada rodada.
- **Links Universais**: As confirmações no chat sempre trazem links clicáveis no formato universal `file:///`.

---

## 🗂️ Localização
- **Repositório Oficial**: [Kadu1992/questions-and-learning](https://github.com/Kadu1992/questions-and-learning)
- **Kadu Skills Hub**: [Kadu1992/kadu-skills-hub](https://github.com/Kadu1992/kadu-skills-hub)
- **Local (Workspace)**: `.agents/skills/questions-and-learning/`
- **Global (IDE / Máquina)**: `C:\Users\55119\.gemini\config\skills\questions-and-learning\`