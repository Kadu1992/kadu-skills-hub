# Codex / ChatGPT no ZCode (Porta 8319) — Windows

Usa a assinatura OpenAI / ChatGPT (Plus, Team ou Pro) diretamente via OAuth com o `cli-proxy-api.exe`.

---

## 1. Configurar o YAML do Codex no Windows

Crie o arquivo `C:\Users\55119\.config\beta-llm\cliproxyapi-codex.config.yaml`:

```yaml
host: "127.0.0.1"
port: 8319

auth-dir: "C:\\Users\\55119\\.cli-proxy-api-codex"

api-keys:
  - "sk-cpa-codex-local-key"

remote-management:
  allow-remote: false
  secret-key: "segredo-admin-codex"
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

## 2. Login OAuth (Conta OpenAI / ChatGPT)

Execute o comando de autenticação no PowerShell:

```powershell
C:\Users\55119\.local\bin\cli-proxy-api.exe -config "C:\Users\55119\.config\beta-llm\cliproxyapi-codex.config.yaml" -codex-login
```

O navegador abrirá a tela de autorização da OpenAI. Ao autenticar, o arquivo `codex-*.json` será salvo em `C:\Users\55119\.cli-proxy-api-codex\`.

---

## 3. Iniciar o Serviço no Windows

```powershell
Start-Process -FilePath "C:\Users\55119\.local\bin\cli-proxy-api.exe" -ArgumentList "-config C:\Users\55119\.config\beta-llm\cliproxyapi-codex.config.yaml" -WindowStyle Hidden
```

Verificar a porta 8319:
```powershell
netstat -ano | findstr :8319
```

---

## 4. Validar Modelos Disponíveis

```powershell
curl.exe -s -H "Authorization: Bearer sk-cpa-codex-local-key" http://127.0.0.1:8319/v1/models
```

Deverá listar os modelos da assinatura (ex: `gpt-4o`, `o3-mini`, `o1`).

---

## 5. Registrar no ZCode (Windows)

No arquivo `C:\Users\55119\.zcode\v2\provider_config.json`:

```json
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
```
