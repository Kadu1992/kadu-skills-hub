---
name: questions-and-learning
description: Converte o arquivo de perguntas brutas (questions.md) em documento estruturado por temas (duvidas-vN.md) e respostas técnicas com plano de ação (resposta-vN.md) na pasta chat_questions/. Ativada automaticamente por /questions-and-learning, /chat-questions, /questions, invocação direta, ou ao enviar/mencionar questions.md.
---

# Skill: questions-and-learning (Local & Global Mode)

Converte o arquivo `questions.md` de dúvidas brutas em dois arquivos versionados dentro da pasta `chat_questions`:
1. `duvidas-vN.md` — o conteúdo organizado em Markdown por temas
2. `resposta-vN.md` — as respostas técnicas da IA para cada dúvida + tabela de plano de ação imediato

---

## Trigger

Esta skill é ativada quando:
- O usuário digita o comando slash `/questions-and-learning`, `/chat-questions` ou `/questions` no chat
- O usuário **invoca a skill diretamente no chat** (ex: digita o nome dela e dá enter), sem anexar nenhum arquivo
- O usuário envia **apenas o arquivo `questions.md`** sem nenhuma mensagem (arrastar e soltar)
- O usuário envia o arquivo `questions.md` com qualquer variação de `"converte"`, `"converter"`, `"organiza"`, `"responder"`

Não aguarde nenhuma instrução adicional. Execute o fluxo completo imediatamente.

---

## Passo 0 — Primeira execução (setup automático)

Antes de qualquer conversão, verifique se a estrutura já existe:

1. Verifique se a pasta `chat_questions/` existe e se contém o arquivo `questions.md`
2. **Se NÃO existir:**
   - Crie a pasta `chat_questions/`
   - Crie dentro dela um arquivo `questions.md` **vazio**
   - Responda no chat apenas confirmando a criação e pedindo para o usuário preencher o `questions.md` com as dúvidas e rodar a skill novamente
   - **Pare aqui** — não prossiga para os passos seguintes nesta execução
3. **Se JÁ existir:**
   - Não recrie nada
   - Siga normalmente para o Passo 1, usando o conteúdo já presente em `chat_questions/questions.md`

---

## Passo 1 — Detectar a versão correta

1. Verifique os arquivos existentes dentro da pasta `chat_questions/`
2. Encontre o maior N já existente em arquivos com padrão `duvidas-vN.md`
3. O novo arquivo será `duvidas-v(N+1).md` — se não existir nenhum, começa em `v1`
4. O arquivo de resposta seguirá a mesma versão: `resposta-v(N+1).md`

Exemplo:
- Pasta tem: `duvidas-v1.md`, `duvidas-v2.md` → novo será `duvidas-v3.md` + `resposta-v3.md`
- Pasta vazia → gera `duvidas-v1.md` + `resposta-v1.md`

---

## Passo 2 — Gerar `duvidas-vN.md`

Leia todo o conteúdo do `questions.md` e converta seguindo as regras abaixo.

### Regras de conversão

- **Não remova nada.** Todo conteúdo original deve estar presente, mesmo informal ou redundante.
- **Identifique temas** e agrupe em seções numeradas com emojis.
- **Preserve perguntas como perguntas** — use `**Dúvida:**`, `**Pergunta:**`, `✅ Confirmado?` para questões em aberto.
- Detecte automaticamente o contexto/projeto pelo conteúdo do arquivo.

### Formatação

- Título: `# 📋 Título — Contexto Detectado`
- Blockquote de contexto logo abaixo do título
- Separador `---` entre seções
- Seções: `## 1. 🎯 Nome da Seção`
- Subseções: `### 1.1 Nome`
- Listas com `-`, termos-chave em **negrito**
- Nomes de arquivos, campos e valores em `` `backticks` ``
- Falas/citações importantes em blockquote `>`
- Rodapé: `*Documento gerado em: [contexto] — vN*`

### Temas comuns (use bom senso para detectar)

| Tema | Título sugerido |
|---|---|
| UI/UX, cards, layout | `🃏 Interface / Cards / Layout` |
| Cálculos ou valores errados | `📊 Cálculos e Valores` |
| Bugs visuais | `🐛 Bugs` |
| Lógica / fluxo | `❓ Dúvidas de Lógica` |
| Regras de negócio | `📋 Regras de Negócio` |
| Arquivos, pastas, versões | `🗂️ Arquivos e Versionamento` |
| Automações / integrações | `🤖 Automações` |
| Próximas etapas | `🔜 Próximos Steps` |
| Testes | `📱 Testes` |

Salve o resultado em: `chat_questions/duvidas-vN.md`

---

## Passo 3 — Gerar `resposta-vN.md`

Após salvar o `duvidas-vN.md`, **leia o `duvidas-vN.md` recém-criado** para entender as dúvidas — não o `questions.md` original. O `questions.md` serviu apenas para a conversão. O `.md` gerado é a fonte de verdade para as respostas, pois está organizado e estruturado.

### Estrutura do arquivo de resposta

```
# ✅ Respostas — vN

> Respostas ponto a ponto referentes ao documento `duvidas-vN.md`.
> Status de cada item indicado como ✅ (confirmado), 🔧 (será implementado) ou 💬 (discussão).

---

## 1. [Título da Seção — mesmo título do duvidas-vN.md]

### 1.1 [Título da subseção] — [✅ / 🔧 / 💬] [label do status]
- Resposta direta e técnica.
- Se houver implementação: detalhar como será feito.
- Se houver código/exemplo: incluir bloco de código.
- Se for confirmação: confirmar ou corrigir com justificativa.

### 1.2 ...

---

## 📋 Resumo de Ações Imediatas (Ordem de Execução)

| # | Ação | Prioridade | Status |
|:--|:-----|:-----------|:-------|
| 1 | [ação derivada das respostas] | Alta | ⬜ |
| 2 | ... | Média | ⬜ |
| 3 | ... | Baixa | ⬜ |

---

*Respostas geradas em: [data] — [contexto do projeto]*
```

### Regras para as respostas

- Responda **cada dúvida individualmente**, na mesma ordem e numeração do `duvidas-vN.md`
- Marque o status de cada subseção no próprio título: `— ✅ Confirmado`, `— 🔧 Será implementado`, `— 💬 Discussão`
- Para questões que precisam de decisão, apresente as opções claramente
- Para bugs, indique a causa provável e a correção sugerida
- Para confirmações, confirme ou corrija com justificativa
- **Sempre inclua a tabela de Resumo de Ações no final** — liste todas as ações concretas derivadas das respostas, com prioridade (Alta / Média / Baixa) e status `⬜`
- Seja direto e técnico — sem enrolação

Salve o resultado em: `chat_questions/resposta-vN.md`

---

## Passo 4 — Confirmar no chat

Após salvar os dois arquivos, responda no chat com esta mensagem:

```
Criei os arquivos na pasta `chat_questions`! Abra aqui:

📄 duvidas-vN.md
Está em: `chat_questions/duvidas-vN.md` — dúvidas organizadas em [X] seções.

💬 resposta-vN.md
Está em: `chat_questions/resposta-vN.md` — respostas ponto a ponto dos [X] itens, com resumo de ações no final.
```

Nada mais além disso. O usuário vai abrir os arquivos na IDE.
