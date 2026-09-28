# Gemini (Porta 8317) — Windows & Pool de Múltiplas Contas (Quantas Quiser)

Usa assinaturas Gemini através do Antigravity (Google AI Pro/Ultra...).
O `cli-proxy-api.exe` autentica contas Google via OAuth e expõe uma API compatível com OpenAI no localhost do Windows.

---

## 🌟 O Segredo do Carrossel (Pool de Múltiplas Contas Google)

No `cli-proxy-api`, quando você realiza o comando de login (`-antigravity-login`), o proxy armazena as credenciais OAuth em arquivos JSON dentro da pasta `auth-dir`.
Para usar **múltiplas contas Google em rodízio automático (2, 4, 10, 20+ contas)**:
1. Você executa o login quantas vezes desejar no navegador (uma com cada conta Google diferente).
2. O proxy salva cada token autenticado na pasta `C:\Users\55119\.cli-proxy-api\`.
3. Com a diretiva `routing.strategy: "round-robin"` (ou `"least-used"`), o proxy distribui as requisições igualmente entre todas as contas.
4. Quando uma conta bate o limite de requisições ou créditos, o bloco `quota-exceeded` faz o chaveamento automático para a próxima conta da fila, sem que a sua IDE trave ou dê erro!

---

## 1. Localização do Executável no Windows

O binário `cli-proxy-api.exe` deve ficar acessível no terminal ou em pasta padrão do usuário:
- Caminho recomendado: `C:\Users\55119\.local\bin\cli-proxy-api.exe` (ou `C:\Users\55119\.config\beta-llm\bin\`).

---

## 2. Configurar o YAML do Gemini (Porta 8317)

Crie o arquivo `C:\Users\55119\.config\beta-llm\cliproxyapi.config.yaml` com o modelo Windows (veja `templates.md`):

```yaml
host: "127.0.0.1"
port: 8317

auth-dir: "C:\\Users\\55119\\.cli-proxy-api"

api-keys:
  - "sk-cpa-gemini-local-key"

remote-management:
  allow-remote: false
  secret-key: "segredo-admin-local"
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

## 3. Realizar o Login das Contas Desejadas (OAuth Google)

Execute o comando de login no PowerShell para cada uma das suas contas (faça com 2, 4, 10, 20 ou quantas contas desejar):

```powershell
# Execução para a Conta 1 (e repita para as demais contas)
C:\Users\55119\.local\bin\cli-proxy-api.exe -config "C:\Users\55119\.config\beta-llm\cliproxyapi.config.yaml" -antigravity-login
```

*O navegador abrirá automaticamente. Faça login na conta Google e autorize.*
*Repita o comando para cada conta que você possuir (2, 4, 10, 20 ou mais contas em pool). Os arquivos de sessão `antigravity-*.json` ficarão armazenados em `C:\Users\55119\.cli-proxy-api\`.*

---

## 4. Iniciar o Serviço no Windows

Você pode rodar diretamente via terminal ou pelo script consolidado `start_proxies.bat`:

```powershell
Start-Process -FilePath "C:\Users\55119\.local\bin\cli-proxy-api.exe" -ArgumentList "-config C:\Users\55119\.config\beta-llm\cliproxyapi.config.yaml" -WindowStyle Hidden
```

Verificar se a porta 8317 está ouvindo no Windows:
```powershell
netstat -ano | findstr :8317
```

---

## 5. Testar e Validar o Endpoint

```powershell
curl.exe -s -H "Authorization: Bearer sk-cpa-gemini-local-key" http://127.0.0.1:8317/v1/models
```

Deverá listar os modelos ativos (ex: `gemini-2.5-pro`, `gemini-2.5-flash`).

Teste de completions com PowerShell:
```powershell
curl.exe -s -H "Authorization: Bearer sk-cpa-gemini-local-key" -H "Content-Type: application/json" http://127.0.0.1:8317/v1/chat/completions -d '{\"model\":\"gemini-2.5-pro\",\"messages\":[{\"role\":\"user\",\"content\":\"responda teste ok\"}]}'
```

---

## 6. Conectar na sua IDE / Cliente

### Dados Universais (Padrão OpenAI):
- **Base URL:** `http://127.0.0.1:8317/v1`
- **API Key:** `sk-cpa-gemini-local-key`
- **Modelos:** `gemini-2.5-pro`, `gemini-2.5-flash`

### Exemplo no ZCode (Windows):
No arquivo `C:\Users\55119\.zcode\v2\provider_config.json`, adicione o provider do Gemini:

```json
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
}
```

### Exemplo no Cursor / Windsurf:
Em **Settings ➔ Models ➔ OpenAI Compatible**:
- **Base URL:** `http://127.0.0.1:8317/v1`
- **API Key:** `sk-cpa-gemini-local-key`
- **Model:** `gemini-2.5-pro`

