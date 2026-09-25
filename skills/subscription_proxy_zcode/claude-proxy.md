# Claude no ZCode (Porta 8318) — Windows

Usa a assinatura Claude Pro/Max via OAuth diretamente na Anthropic, sem necessidade de chaves de API pagas.

---

## 1. Configurar o YAML do Claude no Windows

Crie o arquivo `C:\Users\55119\.config\beta-llm\cliproxyapi-claude.config.yaml`:

```yaml
host: "127.0.0.1"
port: 8318

auth-dir: "C:\\Users\\55119\\.cli-proxy-api-claude"

api-keys:
  - "sk-cpa-claude-local-key"

remote-management:
  allow-remote: false
  secret-key: "segredo-admin-claude"
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

## 2. Login OAuth (Conta Anthropic)

Execute o comando de autenticação no PowerShell:

```powershell
C:\Users\55119\.local\bin\cli-proxy-api.exe -config "C:\Users\55119\.config\beta-llm\cliproxyapi-claude.config.yaml" -claude-login
```

O navegador abrirá na tela de autorização do Claude. Faça login com a conta Pro/Max.
Ao finalizar, o arquivo de sessão `claude-*.json` será gerado em `C:\Users\55119\.cli-proxy-api-claude\`.

---

## 3. Iniciar o Serviço no Windows

Para rodar em segundo plano:

```powershell
Start-Process -FilePath "C:\Users\55119\.local\bin\cli-proxy-api.exe" -ArgumentList "-config C:\Users\55119\.config\beta-llm\cliproxyapi-claude.config.yaml" -WindowStyle Hidden
```

Verificar a porta 8318:
```powershell
netstat -ano | findstr :8318
```

---

## 4. Validar Modelos Disponíveis

```powershell
curl.exe -s -H "Authorization: Bearer sk-cpa-claude-local-key" http://127.0.0.1:8318/v1/models
```

Deverá listar os modelos da sua assinatura (ex: `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-opus`).

---

## 5. Registrar no ZCode (Windows)

No arquivo `C:\Users\55119\.zcode\v2\provider_config.json`:

```json
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
}
```
