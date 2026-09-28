# 🌐 Universal LLM Proxy (Windows)

[![NPX Skill](https://img.shields.io/badge/npx%20skills-universal--llm--proxy-blue.svg)](https://github.com/Kadu1992/universal-llm-proxy)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-blue.svg)](#)
[![Context](https://img.shields.io/badge/context-1M%20Tokens-purple.svg)](#)
[![IDE Support](https://img.shields.io/badge/IDEs-Universal%20(Cursor%2C%20ZCode%2C%20Windsurf%2C%20VSCode...)-success.svg)](#)

> **Use suas assinaturas pagas e contas oficiais de IA (Claude, Gemini, ChatGPT/Codex...), pool de contas sem limite (quantas contas desejar em rodízio: 2, 4, 10, 20+...) e modelos comunitários (OpenCode GO, DeepSeek, Qwen...) em QUALQUER IDE ou cliente no Windows com contexto de até 1 Milhão de Tokens (1M) e monitor visual CodeNotch.**

Sem gastar um único centavo a mais com créditos avulsos de APIs: o `cli-proxy-api.exe` autentica diretamente nas suas contas web via OAuth no navegador e expõe portas locais no padrão **OpenAI API** (`http://localhost:<porta>/v1`).

---

## ⚡ Instalação Rápida como Agent Skill

Instale instantaneamente em qualquer editor ou agente compatível:

```bash
npx skills add Kadu1992/universal-llm-proxy
```

Ou através do [Kadu Skills Hub](https://github.com/Kadu1992/kadu-skills-hub):

```bash
npx skills add Kadu1992/kadu-skills-hub --skill universal-llm-proxy
```

---

## 🏗️ Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│               QUALQUER IDE OU FERRAMENTA DE IA NO WINDOWS                               │
│      (Cursor, ZCode, Windsurf, VS Code / Cline, Continue.dev, Aider, Claude Code...)    │
└──────────────┬───────────────────────────┬───────────────────────────┬──────────────────┘
               │ :8317                     │ :8318                     │ :8319...
               ▼                           ▼                           ▼
       ┌──────────────────┐        ┌──────────────────┐        ┌──────────────────┐
       │ Gemini Proxy     │        │ Claude Proxy     │        │ Codex Proxy      │
       │ (cli-proxy-api)  │        │ (cli-proxy-api)  │        │ (cli-proxy-api)  │
       └───────┬──────────┘        └───────┬──────────┘        └───────┬──────────┘
               │ OAuth Pool (N contas)     │ OAuth                     │ OAuth
               ▼                           ▼                           ▼
        Múltiplas Contas Google    Conta Claude                Conta OpenAI /
        (Quantas contas quiser)    (Pro / Max...)              (ChatGPT / Codex...)
```

---

## 🌐 A Regra Universal de Conexão

Qualquer aplicativo que suporte uma **API OpenAI Customizada (OpenAI-Compatible)** pode ser conectado imediatamente usando os 3 parâmetros abaixo:

| Provedor | Porta | Base URL (Endpoint) | API Key Padrão | Exemplos de Modelos Suportados |
| :--- | :---: | :--- | :--- | :--- |
| **Gemini (Pool: quantas contas quiser)** | `8317` | `http://localhost:8317/v1` | `sk-cpa-gemini-local-key` | `gemini-2.5-pro`, `gemini-2.5-flash`... |
| **Claude (Pro / Max...)** | `8318` | `http://localhost:8318/v1` | `sk-cpa-claude-local-key` | `claude-3-7-sonnet`, `claude-3-5-sonnet`... |
| **Codex (ChatGPT Plus / Pro...)** | `8319` | `http://localhost:8319/v1` | `sk-cpa-codex-local-key` | `gpt-4o`, `o3-mini`, `gpt-4.5-preview`... |
| **OpenCode GO / Comunitários** | `8317` | `http://localhost:8317/v1` | `sk-cpa-gemini-local-key` | `deepseek-chat`, `qwen-2.5-72b`... |
| **Qualquer Novo Modelo...** | Porta livre | `http://localhost:<porta>/v1` | chave-definida | qualquer modelo compatível... |

---

## 🚀 Como Conectar nas Principais Ferramentas

### 1. No Cursor / Windsurf
1. Acesse **Settings** (`Ctrl + ,`) ➔ **Models** (ou **AI Providers**).
2. Adicione um **OpenAI Compatible Provider**:
   - **Base URL:** `http://localhost:8317/v1` (ou `:8318` para Claude / `:8319` para Codex).
   - **API Key:** `sk-cpa-gemini-local-key` (ou qualquer texto).
   - **Model Name:** Digite o nome do modelo (ex: `gemini-2.5-pro`, `claude-3-7-sonnet`...).

### 2. No ZCode
Insira os provedores no arquivo `C:\Users\55119\.zcode\v2\provider_config.json` conforme detalhado no arquivo [templates.md](./templates.md), aproveitando as regras de 1M de tokens.

### 3. No VS Code (Cline / Roo Code / Continue.dev)
- **No Cline / Roo Code:** Escolha **OpenAI Compatible**, preencha `Base URL: http://localhost:8318/v1`, `API Key: sk-cpa-claude-local-key` e `Model ID: claude-3-7-sonnet`.
- **No Continue.dev:** Insira o bloco no seu `config.json` com `provider: "openai"`, `apiBase: "http://localhost:8318/v1"`.

### 4. No Terminal (Aider, Claude Code, Scripts Python)
```cmd
set OPENAI_BASE_URL=http://localhost:8317/v1
set OPENAI_API_KEY=sk-cpa-gemini-local-key
aider --model openai/gemini-2.5-pro
```

---

## 🛠️ Passo a Passo de Instalação no Windows

1. **Baixar o `cli-proxy-api.exe`:**
   Coloque o executável em `C:\Users\55119\.local\bin\cli-proxy-api.exe` (ou diretório no seu PATH).
2. **Criar os arquivos de configuração (.yaml):**
   Crie a pasta `C:\Users\55119\.config\beta-llm\` e copie os arquivos de configuração de [templates.md](./templates.md).
3. **Fazer login nas suas contas oficiais:**
   Execute no terminal para abrir o navegador e autorizar:
   ```cmd
   cli-proxy-api.exe -antigravity-login   # Execute quantas vezes quiser com contas diferentes para o pool
   cli-proxy-api.exe -claude-login        # Autoriza Claude Pro/Max
   cli-proxy-api.exe -codex-login         # Autoriza ChatGPT Plus / Codex
   ```
4. **Iniciar os proxies:**
   Rode `start_proxies.bat` para iniciar todos os serviços em segundo plano.
5. **Monitorar Consumo:**
   Abra o **CodeNotch** para acompanhar cotas e limites das contas em tempo real.

---

## 📂 Estrutura de Módulos da Skill

- [SKILL.md](./SKILL.md) — Roteador principal e checklist para agentes.
- [gemini-proxy.md](./gemini-proxy.md) — Pool de múltiplas contas Antigravity (Porta 8317).
- [claude-proxy.md](./claude-proxy.md) — Conexão Claude Pro/Max... (Porta 8318).
- [codex-proxy.md](./codex-proxy.md) — Conexão ChatGPT Plus / Codex... (Porta 8319).
- [opencode-proxy.md](./opencode-proxy.md) — Integração com OpenCode GO, DeepSeek, Qwen...
- [adicionar-novo-modelo.md](./adicionar-novo-modelo.md) — Como filtrar e customizar modelos.
- [codenotch.md](./codenotch.md) — Configuração do monitor visual CodeNotch.
- [templates.md](./templates.md) — Arquivos YAML, scripts `.bat` e receitas de configuração.
