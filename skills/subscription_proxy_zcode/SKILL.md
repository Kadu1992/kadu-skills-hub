---
name: subscription_proxy_zcode
description: >
  Usar assinaturas pagas (Claude Pro/Max, Gemini via Antigravity em pool de 4 contas e Codex/ChatGPT)
  e modelos comunitários/gratuitos (OpenCode GO, DeepSeek, Qwen) dentro do ZCode no Windows:
  cli-proxy-api como ponte OAuth local + provider custom no provider_config.json
  com contexto expandido de até 1M de tokens e monitoramento visual via CodeNotch.
  Permite setup do zero, filtragem de modelos favoritos (ex: só o Flash), inclusão de novas LLMs e manutenção.
  Triggers: assinatura claude, claude pro, claude max, cli-proxy-api, claude-login,
  antigravity, assinatura gemini, custom:claude-proxy, custom:cliproxy, custom:codex-proxy,
  porta 8318, porta 8317, porta 8319, oauth local, provider custom zcode, codenotch, opencode, opencode go,
  adicionar modelo zcode, filtrar modelos zcode, configurar zcode assinaturas.
version: 2.2-windows
manifest:
  - {file: gemini-proxy.md, when: "conectar assinatura Gemini/Antigravity ao ZCode com carrossel de 4 contas, porta 8317"}
  - {file: claude-proxy.md, when: "conectar assinatura Claude Pro/Max ao ZCode, porta 8318"}
  - {file: codex-proxy.md, when: "conectar assinatura Codex/ChatGPT ao ZCode, porta 8319"}
  - {file: opencode-proxy.md, when: "conectar OpenCode GO, OpenCode.Zen e modelos gratuitos como DeepSeek e Qwen"}
  - {file: adicionar-novo-modelo.md, when: "como filtrar modelos para deixar só o que você usa (ex: Flash), substituir ou adicionar novas LLMs"}
  - {file: codenotch.md, when: "configurar e monitorar limites de uso em tempo real via CodeNotch no Windows"}
  - {file: templates.md, when: "yamls para Windows, scripts de inicialização (.bat/.ps1) e trecho de provider_config.json com contexto 1M"}
---

# Subscription Proxy & Hub Universal de LLMs no ZCode (Windows)

> Use suas assinaturas pagas (Gemini, Claude, Codex) e modelos comunitários (OpenCode GO, DeepSeek, Qwen) no ZCode sem pagar por API key adicional:
> O `cli-proxy-api.exe` realiza autenticação OAuth diretamente nas suas contas oficiais e expõe uma API compatível com OpenAI no localhost do Windows. O ZCode conecta-se a elas através de providers customizados.

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

---

## 🤖 Modos de Operação do Agente de IA

Quando esta skill for invocada no chat de qualquer IDE ou projeto, o agente deve identificar a intenção do usuário e agir de acordo:

### Modo 1: Setup / Instalação do Zero (Primeira vez)
*Gatilho: "Configure o ZCode com minhas assinaturas", "Instale os proxies do ZCode", "Configurar ZCode do zero".*
1. **Baixar o binário:** Verificar se `cli-proxy-api.exe` existe em `C:\Users\55119\.local\bin\cli-proxy-api.exe`. Se não existir, orientar o download da release oficial de Windows (`https://github.com/router-for-me/CLIProxyAPI/releases`).
2. **Criar diretórios e YAMLs:** Gerar a pasta `C:\Users\55119\.config\beta-llm\` e os 3 YAMLs (`cliproxyapi.config.yaml`, `cliproxyapi-claude.config.yaml`, `cliproxyapi-codex.config.yaml`) conforme `templates.md`.
3. **Disparar logins OAuth:** Guiar o usuário a executar no terminal os comandos de login (`-antigravity-login` 4 vezes no navegador para o carrossel, `-claude-login` e `-codex-login`).
4. **Criar script de inicialização:** Gerar `start_proxies.bat` para rodar os 3 serviços em segundo plano.
5. **Configurar o ZCode:** Injetar os 3 providers no `provider_config.json` do ZCode com o contexto expandido de **1 Milhão de Tokens (1M)**.
6. **CodeNotch:** Orientar a instalação do `Codenotch-Setup.exe` para acompanhamento visual do consumo.

---

### Modo 2: Customização e Filtragem de Modelos Favoritos (Manutenção)
*Gatilho: "Quero deixar apenas o Flash no Gemini", "Tire o modelo X e deixe só o Y", "Mude os modelos do ZCode".*
1. Abrir o arquivo de configuração do ZCode: `C:\Users\55119\.zcode\v2\provider_config.json`.
2. Localizar o provedor desejado (`custom:cliproxy`, `custom:claude-proxy`, etc.).
3. Alterar os campos `"personalModelIds"` e `"modelOrder"` para conter **apenas** os modelos solicitados pelo usuário (ex: `["gemini-2.5-flash"]`).
4. Salvar o arquivo e solicitar ao usuário que reinicie o ZCode.
5. *Resultado:* O seletor de modelos do ZCode fica limpo e exibe exclusivamente os modelos escolhidos.

---

### Modo 3: Adição de Nova Empresa ou Modelo Futuro (Expansão)
*Gatilho: "Quero adicionar uma nova empresa", "Lançaram o modelo novo X, inclua pra mim", "Adicionar OpenCode GO".*
- **Se a empresa tem API direta (Ex: OpenCode GO, Groq, DeepSeek, OpenRouter):**
  - Consultar `opencode-proxy.md`.
  - Injetar o novo bloco de provedor diretamente no `provider_config.json` com a URL base e a chave.
- **Se a empresa exige login OAuth por assinatura de navegador (Ex: nova conta ou serviço):**
  - Consultar `adicionar-novo-modelo.md`.
  - Criar o YAML para a nova empresa com uma porta livre (ex: 8320).
  - Adicionar a linha de inicialização no `start_proxies.bat`.
  - Cadastrar o novo provider no `provider_config.json`.
- **Se for um novo modelo em serviço existente (Ex: Gemini 3.0 ou Claude 4):**
  - Rodar o comando `curl.exe -s http://127.0.0.1:PORTA/v1/models` para capturar o ID exato liberado pela API.
  - Adicionar o ID na lista `personalModelIds` do provedor.

---

## 📑 Mapa de Conteúdo (Windows)

| Arquivo | Finalidade | Porta |
| :--- | :--- | :---: |
| `gemini-proxy.md` | Assinatura Gemini via Antigravity com **pool de 4 contas em carrossel** | `8317` |
| `claude-proxy.md` | Assinatura Claude Pro/Max via OAuth | `8318` |
| `codex-proxy.md` | Assinatura Codex / ChatGPT / OpenAI | `8319` |
| `opencode-proxy.md` | Modelos OpenCode GO, OpenCode.Zen, DeepSeek-V4 e Qwen | Direto / API |
| `adicionar-novo-modelo.md` | **Playbook**: Como filtrar para deixar só os modelos que você usa (ex: só o Flash) ou adicionar novos | - |
| `codenotch.md` | Monitor de uso visual na barra lateral via **CodeNotch** (Tauri/Rust Windows) | - |
| `templates.md` | Yamls para Windows, scripts de inicialização em background (`.bat`) e `provider_config.json` com 1M tokens | - |

---

## ⚡ Comandos Rápidos de Validação

```powershell
# Testar se os proxies estão ouvindo:
netstat -ano | findstr "8317 8318 8319"

# Testar modelos do Gemini:
curl.exe -s -H "Authorization: Bearer sk-cpa-gemini-local-key" http://127.0.0.1:8317/v1/models

# Testar modelos do Claude:
curl.exe -s -H "Authorization: Bearer sk-cpa-claude-local-key" http://127.0.0.1:8318/v1/models

# Testar modelos do Codex/ChatGPT:
curl.exe -s -H "Authorization: Bearer sk-cpa-codex-local-key" http://127.0.0.1:8319/v1/models
```
