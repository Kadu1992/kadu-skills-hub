# OpenCode GO & Modelos Gratuitos no ZCode

O **OpenCode** (com planos OpenCode GO e OpenCode.Zen) fornece acesso a modelos de alta performance (como DeepSeek-V4, Qwen 3.8, GLM-5.3 e Muse-Spark) tanto em modalidades gratuitas quanto por créditos.

---

## 1. Como o OpenCode Funciona no ZCode

Diferente do Claude e do Gemini que exigem emulação de navegador OAuth complexa:
1. **Chave Direta (API Key OpenCode-GO)**: Se você possui uma conta no OpenCode, ele fornece uma chave de API que pode ser configurada diretamente no ZCode sem necessidade de passar por um proxy local intermediário.
2. **Via Proxy / Flatt**: Caso você queira unificar o gerenciamento de rate-limits e cotas no mesmo ecossistema local do `cli-proxy-api`, você pode apontar um endpoint local para agregar o OpenCode.

---

## 2. Configuração Direta no ZCode (`provider_config.json`)

Para adicionar o OpenCode GO / OpenCode.Zen diretamente no `C:\Users\55119\.zcode\v2\provider_config.json`:

```json
{
  "providerId": "custom:opencode-go",
  "providerName": "OpenCode GO / Zen",
  "enabled": true,
  "config": {
    "group": "standard-personal",
    "access": {
      "type": "api-key",
      "apiKey": "SUA-CHAVE-OPENCODE-GO-AQUI"
    },
    "api": {
      "type": "openai-chat-completions",
      "baseUrl": "https://api.opencode.ai/v1"
    },
    "personalModelIds": [
      "deepseek-v4",
      "qwen3.8-27b",
      "glm-5.3-flash"
    ],
    "modelOrder": [
      "deepseek-v4",
      "qwen3.8-27b",
      "glm-5.3-flash"
    ]
  }
}
```

---

## 3. Monitoramento no CodeNotch

O **CodeNotch** no Windows detecta automaticamente a sessão do OpenCode lendo a chave local armazenada em `~/.opencode/` ou nas configurações do ZCode, exibindo o anel correspondente de créditos/uso na lateral da tela.
