# 🧠 Kadu Skills Hub

> **Hub central de Agent Skills abertas, projetado para qualquer agente de IA, editor ou LLM compatível com a especificação de skills (`SKILL.md`).**

Bem-vindo ao catálogo central de skills de inteligência artificial mantido por [Kadu Amstetter](https://github.com/Kadu1992). Aqui você encontra ferramentas, metodologias e fluxos práticos prontos para turbinar agentes autônomos.

---

## 📦 Catálogo de Skills Disponíveis

| Skill | Descrição | Status | Instalação Rápida |
| :--- | :--- | :---: | :--- |
| **[`archify-presenter`](./skills/archify-presenter)** | Diagramas executivos interativos em HTML/SVG com ponteiro laser, modo foco de fala e 6 presets corporativos. | 🟢 Ativo | `npx skills add Kadu1992/archify-presenter` |
| **[`questions-and-learning`](./skills/questions-and-learning)** | Conversão de dúvidas brutas (`questions.md`) em Markdown estruturado por temas e respostas com plano de ação. | 🟢 Ativo | `npx skills add Kadu1992/questions-and-learning` |
| **[`chat-context`](./skills/chat-context)** | Persistência global de contexto entre sessões com `current_context.md` e histórico imutável ISO 8601. | 🟢 Ativo | `npx skills add Kadu1992/chat-context` |
| **[`ai-tutor-video`](./skills/ai-tutor-video)** | Tutor de estudos com IA sincronizado com vídeo-aulas do YouTube, transcrições e prática real orientada a evidências. | 🟢 Ativo | `npx skills add Kadu1992/ai-tutor-video` |

---

## 🚀 Como Instalar e Usar

Você pode instalar qualquer skill deste repositório diretamente pelo terminal usando o gerenciador universal de skills em qualquer ambiente (Codex, Claude Code, Cursor, OpenCode ou Antigravity IDE):

### 1. Instalar o Catálogo Completo:
```bash
npx skills add Kadu1992/kadu-skills-hub
```

### 2. Instalar uma Skill Específica a partir do Hub:
```bash
npx skills add Kadu1992/kadu-skills-hub --skill archify-presenter
npx skills add Kadu1992/kadu-skills-hub --skill questions-and-learning
npx skills add Kadu1992/kadu-skills-hub --skill chat-context
npx skills add Kadu1992/kadu-skills-hub --skill ai-tutor-video
```

### 3. Ou Instalar Diretamente pelo Repositório da Skill:
```bash
npx skills add Kadu1992/archify-presenter
npx skills add Kadu1992/questions-and-learning
npx skills add Kadu1992/chat-context
npx skills add Kadu1992/ai-tutor-video
```
