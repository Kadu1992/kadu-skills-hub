# Playbook: Como Adicionar, Filtrar ou Substituir Modelos e Provedores

Este guia explica exatamente como você (ou o assistente de IA) pode:
1. **Deixar apenas os modelos específicos que você usa** (ex: manter apenas o `gemini-2.5-flash` ou `gemini-1.5-flash` e esconder os outros).
2. **Atualizar modelos quando novas versões forem lançadas** pelo Google, Anthropic ou OpenAI.
3. **Adicionar uma nova empresa ou provedor de LLM** do zero.

---

## 🎯 Onde os Modelos São Filtrados? (Na IDE / Cliente)

O `cli-proxy-api` descobre todos os modelos aos quais a sua assinatura dá direito. Porém, **é a sua IDE quem decide quais deles aparecem no seu menu dropdown**:

- **No ZCode:** No arquivo `C:\Users\55119\.zcode\v2\provider_config.json` através dos campos `"personalModelIds"` e `"modelOrder"`.
- **No Cursor / Windsurf:** Na tela de **Settings ➔ Models**, onde você adiciona ou remove os nomes dos modelos manualmente.
- **No VS Code (Continue.dev):** Na lista `"models"` do arquivo `config.json`.
- **No Cline / Roo Code:** No campo **Model ID** do painel da extensão.

### Exemplo Prático: Quero apenas o Flash no Gemini!
Se você quer que o Gemini mostre **apenas** o modelo Flash (ex: `gemini-2.5-flash`), basta deixar a lista assim:

```json
{
  "providerId": "custom:cliproxy",
  "providerName": "Gemini (Antigravity)",
  "enabled": true,
  "config": {
    "group": "standard-personal",
    "access": { "type": "api-key", "apiKey": "sk-cpa-gemini-local-key" },
    "api": { "type": "openai-chat-completions", "baseUrl": "http://127.0.0.1:8317/v1" },
    "personalModelIds": ["gemini-2.5-flash"],
    "modelOrder": ["gemini-2.5-flash"]
  }
}
```
*Pronto! Ao salvar e reiniciar o ZCode, todos os outros modelos (Pro, Ultra, etc.) somem do seletor e só fica o Flash que você gosta de usar.*

---

## 🚀 Como Descobrir os Nomes Exatos dos Modelos Ativos?

Quando o Google, a Anthropic ou a OpenAI lançarem um novo modelo (ex: Gemini 3, Claude 4, etc.), como saber o nome exato dele no proxy?
Basta rodar no PowerShell:

```powershell
# Para ver todos os modelos que o Gemini liberou na sua conta:
curl.exe -s -H "Authorization: Bearer sk-cpa-gemini-local-key" http://127.0.0.1:8317/v1/models

# Para ver todos os modelos do Claude:
curl.exe -s -H "Authorization: Bearer sk-cpa-claude-local-key" http://127.0.0.1:8318/v1/models

# Para ver todos os modelos do Codex/ChatGPT:
curl.exe -s -H "Authorization: Bearer sk-cpa-codex-local-key" http://127.0.0.1:8319/v1/models
```

Você copia o ID exato retornado (ex: `gemini-3.0-flash` ou `claude-3-7-sonnet`) e coloca no `personalModelIds` do seu ZCode!

---

## 🧩 Adicionando Uma Nova Empresa / Provedor Futuro

Quando você quiser adicionar uma nova empresa (ex: DeepSeek direto, Groq, Mistral, OpenRouter, OpenCode GO, etc.):

### Caso A: A empresa já fornece API compatível com OpenAI (Ex: OpenCode GO, OpenRouter, Groq, DeepSeek)
**Você NÃO precisa de proxy local!**  
Basta adicionar um novo bloco diretamente no `provider_config.json` do ZCode com a URL da empresa e a sua chave. Veja o exemplo em `opencode-proxy.md`.

### Caso B: A empresa exige login OAuth por assinatura de navegador (sem chave de API aberta)
1. **Criamos um novo arquivo na skill**: ex: `empresa-proxy.md` para documentar a porta e os comandos.
2. **Definimos uma nova porta livre**: ex: `8320`.
3. **Criamos o YAML correspondente**: `C:\Users\55119\.config\beta-llm\cliproxyapi-empresa.config.yaml`.
4. **Adicionamos o comando no `start_proxies.bat`**: para subir o novo proxy junto com os outros.
5. **Cadastramos o novo bloco no `provider_config.json`**.
