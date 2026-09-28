---
name: universal-llm-proxy
description: >
  Usar contas oficiais e assinaturas de IA (Gemini, Claude, Codex, GPT, OpenCode, DeepSeek, Qwen...)
  com pool flexível de qualquer provedor e quantidade de contas que desejar (2, 4, 10, 20+ contas em rodízio...)
  e modelos comunitários/gratuitos no Windows em QUALQUER IDE ou cliente:
  Cursor, ZCode, Windsurf, VS Code (Cline / Roo Code / Continue.dev), Aider, Claude Code, LibreChat...
  cli-proxy-api como ponte OAuth local expondo endpoints padrão OpenAI no localhost (:8317, :8318, :8319...)
  com contexto expandido de até 1M de tokens e monitoramento visual via CodeNotch.
  Permite setup do zero, filtragem de modelos favoritos (ex: só o Flash), inclusão de novas LLMs e manutenção.
  Triggers: universal-llm-proxy, subscription-proxy, subscription_proxy_zcode, assinatura claude, claude pro, claude max, cli-proxy-api, claude-login,
  antigravity, assinatura gemini, custom:claude-proxy, custom:cliproxy, custom:codex-proxy,
  porta 8318, porta 8317, porta 8319, oauth local, proxy universal, cursor proxy, zcode proxy, windsurf proxy,
  codenotch, opencode, opencode go, adicionar modelo proxy, filtrar modelos proxy, configurar proxy assinaturas.
version: 3.1-windows-universal
manifest:
  - {file: gemini-proxy.md, when: "conectar assinatura Gemini/Antigravity ao proxy com pool de múltiplas contas (quantas quiser), porta 8317"}
  - {file: claude-proxy.md, when: "conectar assinatura Claude Pro/Max ao proxy, porta 8318"}
  - {file: codex-proxy.md, when: "conectar assinatura Codex/ChatGPT ao proxy, porta 8319"}
  - {file: opencode-proxy.md, when: "conectar OpenCode GO, OpenCode.Zen e modelos gratuitos como DeepSeek, Qwen..."}
  - {file: adicionar-novo-modelo.md, when: "como filtrar modelos para deixar só o que você usa (ex: Flash), substituir ou adicionar novas LLMs..."}
  - {file: codenotch.md, when: "configurar e monitorar limites de uso em tempo real via CodeNotch no Windows"}
  - {file: templates.md, when: "yamls para Windows, scripts de inicialização (.bat), guia de conexão universal e receitas por IDE"}
---

# Universal LLM Proxy — Hub Universal de Assinaturas de IA (Windows)

> Use suas assinaturas pagas (Gemini, Claude, ChatGPT/Codex...), pool de contas sem limite (quantas contas desejar em rodízio: 2, 4, 10, 20+...) e modelos comunitários (OpenCode GO, DeepSeek, Qwen...) em **qualquer IDE ou ferramenta** (Cursor, ZCode, Windsurf, VS Code, Aider...) sem pagar por API key adicional:
> O `cli-proxy-api.exe` realiza autenticação OAuth diretamente nas suas contas oficiais no navegador e expõe uma API compatível com OpenAI no localhost do Windows. Qualquer ferramenta se conecta a elas como se fosse a API da OpenAI.

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│               QUALQUER IDE OU FERRAMENTA DE IA NO WINDOWS                               │
│  (Cursor, ZCode, Windsurf, VS Code / Cline, Continue.dev, Aider, Claude Code...)        │
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

## 🌐 A Regra de Ouro Universal (Compatibilidade 100% OpenAI)

Como o proxy transforma suas contas em um **servidor local compatível com a API da OpenAI**, para conectar **qualquer** software basta fornecer 3 parâmetros:

| Provedor / Assinatura | Porta Local | Base URL (Endpoint) | API Key Padrão | Exemplos de Modelos Suportados |
| :--- | :---: | :--- | :--- | :--- |
| **Gemini (Pool de Contas: quantas quiser)** | `8317` | `http://localhost:8317/v1` | `sk-cpa-gemini-local-key` | `gemini-2.5-pro`, `gemini-2.5-flash`... |
| **Claude (Pro / Max...)** | `8318` | `http://localhost:8318/v1` | `sk-cpa-claude-local-key` | `claude-3-7-sonnet`, `claude-3-5-sonnet`... |
| **Codex (ChatGPT Plus / Pro...)** | `8319` | `http://localhost:8319/v1` | `sk-cpa-codex-local-key` | `gpt-4o`, `o3-mini`, `gpt-4.5-preview`... |
| **OpenCode GO / Comunitários** | `8317` | `http://localhost:8317/v1` | `sk-cpa-gemini-local-key` | `deepseek-chat`, `qwen-2.5-72b`... |
| **Qualquer Novo Provedor...** | Porta livre | `http://localhost:<porta>/v1` | chave-definida | qualquer modelo compatível... |

---

## 🚀 Receitas Rápidas de Conexão por IDE

### 1. No Cursor / Windsurf
1. Abra **Settings** (`Ctrl + ,`) ➔ **Models** (ou **AI Providers**).
2. Adicione um provedor **OpenAI Compatible**:
   - **Base URL:** `http://localhost:8317/v1` (ou `:8318` para Claude / `:8319` para ChatGPT).
   - **API Key:** `sk-cpa-gemini-local-key` (ou qualquer texto).
   - **Model Name:** Digite `gemini-2.5-pro`, `claude-3-7-sonnet`...
3. Desative os modelos padrão do Cursor e ative seu modelo customizado.

### 2. No ZCode
Configurado via arquivo `C:\Users\55119\.zcode\v2\provider_config.json` adicionando as regras de provider e regras de 1M de tokens em `templates.md`.

### 3. No VS Code (Cline, Roo Code ou Continue.dev)
- **No Cline / Roo Code:** No painel da extensão, selecione **API Provider: OpenAI Compatible**, preencha `Base URL: http://localhost:8318/v1`, `API Key: sk-cpa-claude-local-key` e `Model ID: claude-3-7-sonnet`.
- **No Continue.dev:** No `config.json`, adicione:
  ```json
  {
    "title": "Claude Local",
    "provider": "openai",
    "model": "claude-3-7-sonnet",
    "apiBase": "http://localhost:8318/v1",
    "apiKey": "sk-cpa-claude-local-key"
  }
  ```

### 4. No Terminal / Aider / Scripts
Basta definir as variáveis de ambiente:
```cmd
set OPENAI_BASE_URL=http://localhost:8317/v1
set OPENAI_API_KEY=sk-cpa-gemini-local-key
aider --model openai/gemini-2.5-pro
```

---

## 🤖 Modos de Operação do Agente de IA

Quando esta skill for invocada no chat de qualquer IDE ou projeto, o agente deve identificar a intenção do usuário e agir de acordo:

### Modo 1: Setup / Instalação do Zero (Primeira vez)
*Gatilho: "Configure o proxy com minhas assinaturas", "Instale os proxies no Windows", "Configurar universal proxy do zero".*
1. **Baixar o binário:** Verificar se `cli-proxy-api.exe` existe em `C:\Users\55119\.local\bin\cli-proxy-api.exe`. Se não existir, orientar o download da release oficial de Windows (`https://github.com/router-for-me/CLIProxyAPI/releases`).
2. **Criar diretórios e YAMLs:** Gerar a pasta `C:\Users\55119\.config\beta-llm\` e os YAMLs (`cliproxyapi.config.yaml`, `cliproxyapi-claude.config.yaml`, `cliproxyapi-codex.config.yaml`...) conforme `templates.md`.
3. **Disparar logins OAuth:** Guiar o usuário a executar no terminal os comandos de login (`-antigravity-login` quantas vezes quiser para o pool de contas no navegador, `-claude-login` e `-codex-login`).
4. **Criar script de inicialização:** Gerar `start_proxies.bat` para rodar os serviços em segundo plano no Windows.
5. **Configurar o cliente desejado:** Injetar as configurações na IDE desejada (Cursor, ZCode, Windsurf, Cline ou terminal) com o contexto expandido de **1 Milhão de Tokens (1M)**.
6. **CodeNotch:** Orientar a instalação do `Codenotch-Setup.exe` para acompanhamento visual do consumo.

### Modo 2: Customização / Gerenciamento de Modelos
*Gatilho: "Adicionar modelo ao proxy", "Deixar só o Flash", "Configurar OpenCode GO", "Trocar modelo no Cursor/ZCode".*
1. Ler `adicionar-novo-modelo.md` ou `opencode-proxy.md`.
2. Para adicionar modelo comunitário (OpenCode GO, DeepSeek, Qwen...): editar o YAML da porta 8317 ou configurar direto no cliente.
3. Para filtrar a lista (ex: remover Pro e deixar apenas Flash): editar os IDs no cliente configurado.

### Modo 3: Manutenção e Resolução de Problemas
*Gatilho: "Proxy parou de responder", "Erro 401 no proxy", "Trocar conta do Claude/Gemini".*
1. Verificar se o processo está rodando: `tasklist | findstr cli-proxy-api`.
2. Se estiver travado: executar `stop_proxies.bat` e depois `start_proxies.bat`.
3. Se o token expirou: reexecutar o comando de login específico (ex: `cli-proxy-api.exe -claude-login`).

---

## 🧭 Arquitetura de Portas e Serviços Locais

```
[Porta 8317] -> Gemini / Antigravity (Pool de quantas contas quiser) + OpenCode GO...
[Porta 8318] -> Claude Pro / Max... (Anthropic OAuth)
[Porta 8319] -> Codex / ChatGPT Plus... (OpenAI OAuth)
```

Todos rodam silenciosamente em segundo plano no Windows através do script `start_proxies.bat` e podem ser inicializados automaticamente com o Windows colocando um atalho em `shell:startup`.
