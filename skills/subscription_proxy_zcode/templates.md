# Templates para Windows (Copiar e Configurar)

Todos os arquivos estão pré-adaptados para o sistema operacional Windows (`C:\Users\55119\...`).

---

## 1. YAML Gemini (Porta 8317 — Pool 4 Contas)
**Caminho:** `C:\Users\55119\.config\beta-llm\cliproxyapi.config.yaml`

```yaml
host: "127.0.0.1"
port: 8317

auth-dir: "C:\\Users\\55119\\.cli-proxy-api"

api-keys:
  - "sk-cpa-gemini-local-key"

remote-management:
  allow-remote: false
  secret-key: "adm-sec-gemini"
  disable-control-panel: true

debug: false
logging-to-file: true

request-retry: 3

quota-exceeded:
  switch-project: true
  switch-preview-model: true
  antigravity-credits: true

routing:
  strategy: "round-robin"
```

---

## 2. YAML Claude (Porta 8318 — Claude Pro/Max)
**Caminho:** `C:\Users\55119\.config\beta-llm\cliproxyapi-claude.config.yaml`

```yaml
host: "127.0.0.1"
port: 8318

auth-dir: "C:\\Users\\55119\\.cli-proxy-api-claude"

api-keys:
  - "sk-cpa-claude-local-key"

remote-management:
  allow-remote: false
  secret-key: "adm-sec-claude"
  disable-control-panel: true

debug: false
logging-to-file: true

request-retry: 3

quota-exceeded:
  switch-project: true
  switch-preview-model: true

routing:
  strategy: "round-robin"
```

---

## 3. YAML Codex (Porta 8319 — ChatGPT / OpenAI)
**Caminho:** `C:\Users\55119\.config\beta-llm\cliproxyapi-codex.config.yaml`

```yaml
host: "127.0.0.1"
port: 8319

auth-dir: "C:\\Users\\55119\\.cli-proxy-api-codex"

api-keys:
  - "sk-cpa-codex-local-key"

remote-management:
  allow-remote: false
  secret-key: "adm-sec-codex"
  disable-control-panel: true

debug: false
logging-to-file: true

request-retry: 3

quota-exceeded:
  switch-project: true
  switch-preview-model: true

routing:
  strategy: "round-robin"
```

---

## 4. Script Windows para Iniciar os 3 Proxies
**Caminho:** `C:\Users\55119\.config\beta-llm\start_proxies.bat`

```bat
@echo off
title Proxies de Assinaturas ZCode
echo ==============================================
echo Iniciando Proxies de Assinaturas no Windows...
echo ==============================================

set BIN="C:\Users\55119\.local\bin\cli-proxy-api.exe"
set CFG_DIR="C:\Users\55119\.config\beta-llm"

echo [1/3] Iniciando Gemini (Antigravity 4 Contas) na porta 8317...
start /b "" %BIN% -config "%CFG_DIR%\cliproxyapi.config.yaml"

echo [2/3] Iniciando Claude Pro/Max na porta 8318...
start /b "" %BIN% -config "%CFG_DIR%\cliproxyapi-claude.config.yaml"

echo [3/3] Iniciando Codex (ChatGPT) na porta 8319...
start /b "" %BIN% -config "%CFG_DIR%\cliproxyapi-codex.config.yaml"

echo.
echo Todos os proxies foram disparados em segundo plano!
echo 8317 = Gemini (4 contas pool)
echo 8318 = Claude
echo 8319 = Codex
```

*(Opcional: Coloque um atalho para este `.bat` na pasta `shell:startup` para iniciar automaticamente com o Windows).*

---

## 5. Script Windows para Encerrar os Proxies
**Caminho:** `C:\Users\55119\.config\beta-llm\stop_proxies.bat`

```bat
@echo off
echo Encerrando instâncias do cli-proxy-api...
taskkill /f /im cli-proxy-api.exe
echo Concluído.
```

---

## 6. Configuração no ZCode com Contexto de 1M Tokens
**Caminho:** `C:\Users\55119\.zcode\v2\provider_config.json`

Insira dentro de `config.providerConfigRules.providerRules`:

```json
[
  {
    "providerId": "custom:cliproxy",
    "providerName": "Gemini (Antigravity)",
    "enabled": true,
    "config": {
      "group": "standard-personal",
      "access": { "type": "api-key", "apiKey": "sk-cpa-gemini-local-key" },
      "api": { "type": "openai-chat-completions", "baseUrl": "http://127.0.0.1:8317/v1" },
      "personalModelIds": ["gemini-2.5-pro", "gemini-2.5-flash"],
      "modelOrder": ["gemini-2.5-pro", "gemini-2.5-flash"]
    }
  },
  {
    "providerId": "custom:claude-proxy",
    "providerName": "Claude (Assinatura)",
    "enabled": true,
    "config": {
      "group": "standard-personal",
      "access": { "type": "api-key", "apiKey": "sk-cpa-claude-local-key" },
      "api": { "type": "openai-chat-completions", "baseUrl": "http://127.0.0.1:8318/v1" },
      "personalModelIds": ["claude-3-7-sonnet", "claude-3-5-sonnet"],
      "modelOrder": ["claude-3-7-sonnet", "claude-3-5-sonnet"]
    }
  },
  {
    "providerId": "custom:codex-proxy",
    "providerName": "Codex (ChatGPT)",
    "enabled": true,
    "config": {
      "group": "standard-personal",
      "access": { "type": "api-key", "apiKey": "sk-cpa-codex-local-key" },
      "api": { "type": "openai-chat-completions", "baseUrl": "http://127.0.0.1:8319/v1" },
      "personalModelIds": ["gpt-4o", "o3-mini"],
      "modelOrder": ["gpt-4o", "o3-mini"]
    }
  }
]
```

### Regras de Aumento de Contexto para 1 Milhão de Tokens (1M)
Em `config.modelConfigRules`, defina os limites máximos de tokens para que o ZCode permita conversas ultra-longas sem truncamento:

```json
{
  "gemini-2.5-pro": {
    "maxContextTokens": 1048576,
    "maxOutputTokens": 65536
  },
  "gemini-2.5-flash": {
    "maxContextTokens": 1048576,
    "maxOutputTokens": 65536
  },
  "claude-3-7-sonnet": {
    "maxContextTokens": 1048576,
    "maxOutputTokens": 65536
  },
  "gpt-4o": {
    "maxContextTokens": 1048576,
    "maxOutputTokens": 16384
  }
}
```
