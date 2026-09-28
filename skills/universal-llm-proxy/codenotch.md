# CodeNotch no Windows — Monitor Lateral de Consumo de Assinaturas

O **CodeNotch** é uma ferramenta de monitoramento visual que fixa um "notch" (arco/barra flutuante) na borda da tela, mostrando em tempo real o quanto de limite de cada assinatura (Claude, Codex, Antigravity, OpenCode/Flatt) você já consumiu e quanto resta.

![Dashboard do CodeNotch no ZCode](../../../raw/assets/codenotch_zcode_dashboard.png)

---

## 🌟 Informações do Projeto

- **Repositório Oficial**: [https://github.com/vinzdg/codenotch](https://github.com/vinzdg/codenotch)
- **Tecnologia do Port Windows**: Rust + Tauri 2 (leve, sem consumo pesado de RAM).
- **Download Windows**: `Codenotch-Setup.exe` (disponível na página de Releases do repositório).

---

## ⚡ Como Funciona no Windows

1. **Leitura Direta de Sessões Locais**:
   - O CodeNotch não pede suas senhas nem envia tokens para a nuvem.
   - Ele lê as respostas de cota oficiais diretamente das sessões e proxies já logados na máquina:
     - **Claude Code**: lê o `/usage` da sessão OAuth local.
     - **Codex / ChatGPT**: lê as janelas de limite de 5 horas e limite semanal.
     - **Antigravity**: monitora o language server local e o endpoint de cotas do Google.
2. **Tooltip Rico ao Passar o Mouse**:
   - Ao pousar o cursor sobre o anel de qualquer modelo:
     - Mostra percentual usado vs. restante (ex: `31% usado • 69% restante`).
     - Data exata de renovação da cota (ex: `Renova 30 de set.`).
     - Status ao vivo (se o modelo está trabalhando, ocioso ou aguardando).

---

## 🚀 Instalação no Windows

1. Baixe o instalador mais recente: `Codenotch-Setup.exe`.
2. Execute o instalador (instala para o usuário atual sem exigir privilégios de Administrador).
   *Caso o SmartScreen do Windows mostre "Windows protegeu o seu computador", clique em "Mais informações" e "Executar assim mesmo".*
3. Ao abrir, o notch se fixará na lateral da tela. Em **Configurações (Settings)**, você pode ativar e reordenar as contas desejadas (Claude, Codex, Antigravity, OpenCode).
