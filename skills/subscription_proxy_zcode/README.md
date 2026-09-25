# Subscription Proxy ZCode (Windows)

> **Agent Skill para conectar assinaturas pagas de IA (Gemini em pool de 4 contas, Claude Pro/Max e Codex/ChatGPT) e modelos comunitários (OpenCode GO, DeepSeek, Qwen) diretamente ao ZCode no Windows com contexto de até 1 Milhão de Tokens e monitoramento visual via CodeNotch.**

[![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-blue)](https://github.com/Kadu1992/subscription_proxy_zcode)
[![ZCode](https://img.shields.io/badge/IDE-ZCode-orange)](https://github.com/Kadu1992/subscription_proxy_zcode)
[![Agent Skill](https://img.shields.io/badge/agent--skills-ready-green)](https://github.com/Kadu1992/subscription_proxy_zcode)
[![License](https://img.shields.io/badge/license-MIT-purple)](LICENSE)

---

## 📦 Como Instalar via NPX

Você pode instalar esta skill em qualquer projeto, IDE ou assistente compatível com o ecossistema `agent-skills`:

```bash
# 1. Instalação direta pelo repositório da Skill:
npx skills add Kadu1992/subscription_proxy_zcode

# 2. Ou instalação através do Kadu Skills Hub:
npx skills add Kadu1992/kadu-skills-hub --skill subscription_proxy_zcode
```

---

## 🤖 Como Usar com o seu Agente de IA

Assim que a skill for adicionada ao seu projeto, qualquer LLM (no Claude Code, Antigravity, Cursor, OpenCode ou ZCode) saberá exatamente o que fazer quando você conversar com ela:

### 1. Para Instalar do Zero no seu Computador:
> *"Configure o ZCode com minhas assinaturas usando a skill subscription_proxy_zcode."*  
O agente verificará o `cli-proxy-api.exe`, gerará os YAMLs na porta 8317 (Gemini), 8318 (Claude) e 8319 (Codex), criará o script `start_proxies.bat` e configurará o `provider_config.json` do ZCode com 1M tokens.

### 2. Para Filtrar e Deixar Apenas seus Modelos Favoritos:
> *"Quero deixar apenas o Gemini Flash no ZCode e retirar os outros modelos."*  
O agente ajustará o `personalModelIds` no seu ZCode para exibir exclusivamente os modelos que você deseja.

### 3. Para Adicionar Novas Empresas ou Modelos:
> *"Adicione o OpenCode GO com DeepSeek-V4 no meu ZCode."* ou *"Lançaram o modelo novo X, adicione pra mim."*  
O agente consultará o playbook da skill e injetará a nova empresa/modelo com facilidade.

---

## 🏗️ Arquitetura dos Proxies no Windows

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ZCODE (IDE no Windows)                          │
└───────┬──────────────────────────┬──────────────────────────┬──────────┘
        │ :8317                    │ :8318                    │ :8319
        ▼                          ▼                          ▼
┌──────────────────┐       ┌──────────────────┐       ┌──────────────────┐
│ Gemini Proxy     │       │ Claude Proxy     │       │ Codex Proxy      │
│ (cli-proxy-api)  │       │ (cli-proxy-api)  │       │ (cli-proxy-api)  │
└───────┬──────────┘       └───────┬──────────┘       └───────┬──────────┘
        │ OAuth Pool               │ OAuth                    │ OAuth
        ▼                          ▼                          ▼
 4 Contas Google           Conta Claude               Conta OpenAI /
 (Antigravity Carrossel)   (Pro / Max)                (ChatGPT / Codex)
```

- **Porta 8317 (Gemini / Antigravity)**: Carrossel com 4 contas Google em rodízio (`round-robin`) e fallback em caso de esgotamento de cota.
- **Porta 8318 (Claude)**: Conta Claude Pro/Max oficial via OAuth Anthropic.
- **Porta 8319 (Codex)**: Conta OpenAI via OAuth ChatGPT.
- **OpenCode GO / Zen**: Conexão direta ou via API para DeepSeek, Qwen e GLM.
- **CodeNotch**: Aplicativo desktop em Rust/Tauri 2 para monitorar a queima de cotas e limites na borda da tela.

---

## 📂 Arquivos da Skill

- [`SKILL.md`](SKILL.md) — Roteador principal, modos de agente e regras de automação.
- [`gemini-proxy.md`](gemini-proxy.md) — Configuração do carrossel de 4 contas Google.
- [`claude-proxy.md`](claude-proxy.md) — Configuração do Claude Pro/Max no Windows.
- [`codex-proxy.md`](codex-proxy.md) — Configuração do Codex/ChatGPT no Windows.
- [`opencode-proxy.md`](opencode-proxy.md) — Integração do OpenCode GO e modelos gratuitos.
- [`adicionar-novo-modelo.md`](adicionar-novo-modelo.md) — Playbook de filtragem e adição de novas LLMs.
- [`codenotch.md`](codenotch.md) — Guia do instalador e monitor de limites.
- [`templates.md`](templates.md) — Modelos YAML para Windows, scripts `.bat` e JSON com 1M tokens.

---

## 👤 Autor

Desenvolvido e mantido por **[Kadu Amstetter](https://github.com/Kadu1992)**.
Distribuído sob licença MIT.
