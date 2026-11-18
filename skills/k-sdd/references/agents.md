# Guia: Tríade de Agentes de Homologação k-sdd (Multi-Harness)

> **Objetivo:** Estabelecer a governança de papéis, a regra de ouro do pool de operários com afinidade de contexto (*Sticky Threading*) e a arquitetura agnóstica para instanciação dos 3 agentes em qualquer ambiente ou harness de IA.

---

## 1. Princípio Arquitetural: Separação Estrita de Responsabilidades

Para eliminar conflitos no Git e impedir sobreposição de arquivos durante a homologação humana, o `k-sdd` isola o trabalho em 3 papéis autônomos:

```
[ Usuário / Humano ]
       │
       ▼ (Relatos de Erros)
┌──────────────┐
│   TRIAGEM    │ ──► Registra no [ .specs/qa-uats.md ] ──► Status 🔴 reprovada
└──────────────┘
                               │
                               ▼ (Notificação / Leitura do Painel)
                      ┌──────────────────┐
                      │   ORQUESTRADOR   │ ──► Atualiza para 🟡 corrigindo
                      └──────────────────┘     Gerencia Pool & Reconcilia Specs
                               │
                               ▼ (Despacho Cirúrgico por Arquivo)
                      ┌──────────────────┐
                      │   OPERÁRIO(S)   │ ──► Corrige Código, Valida no Browser
                      └──────────────────┘     Atualiza para 🟢 corrigida
                               │
                               ▼ (Reteste Humano)
                      [ Usuário Aprova ✅ ] ──► Movido para Arquivo (Concluído)
```

| Agente | Arquivo de Prompt | Responsabilidade Principal | O que NUNCA Faz |
| :--- | :--- | :--- | :--- |
| **Triagem** | [`agents/triagem.md`](../agents/triagem.md) | Receber relatos de teste do usuário em menos de 3s e cadastrar como `🔴 reprovada` em `.specs/qa-uats.md`. | Nunca toca no código nem em arquivos `.specs/**`. |
| **Orquestrador** | [`agents/orquestrador.md`](../agents/orquestrador.md) | Coordenar o pool de operários, despachar tasks atômicas e ser o **único escriba oficial** dos documentos vivos k-sdd (`feedback.md`, `spec.md`, `frd.md`, etc.). | Nunca escreve código de implementação diretamente. |
| **Operário** | [`agents/operario.md`](../agents/operario.md) | Foco cirúrgico no arquivo dominante da sua UAT, rodar gates de build, validar visualmente no navegador e reportar `🟢 corrigida`. | Nunca edita arquivos de `.specs/**` (exceto a sua linha no painel). |

---

## 2. Regra de Ouro do Pool de Operários: Numeração e Afinidade Estrita (Sticky Threading)

### Regra 1: Numeração Sequencial Limpa
Os operários recebem identificadores numéricos contínuos:
`agent1`, `agent2`, `agent3`, `agent4`...

### Regra 2: Afinidade Estrita de Contexto (Sticky Threading)
- **Um agente é dono da sua frente até o fim:**
  Quando o Orquestrador despacha o `agent1` para corrigir um problema (ex: *Elemento X* ou *UAT-01*), esse agente carrega em sua memória ativa (thread) os arquivos lidos, as tentativas e a lógica da solução.
- **Se o usuário testar e reprovar no reteste:**
  O Orquestrador **devolve a correção obrigatoriamente para o mesmo agente (`agent1`)**. Jamais crie um novo operário para resolver o que o `agent1` já estava tratando enquanto ele estiver disponível, pois isso descartaria o contexto quente e consumiria tokens desnecessários.
- **Paralelismo Seguro:**
  Demandas em arquivos diferentes e independentes abrem novos operários na ordem numérica (`agent2`, `agent3`...).
- **Anti-Conflito:** Dois operários nunca tocam o mesmo arquivo simultaneamente.

---

## 3. Como os Agentes Operam em Diferentes Harnesses

A skill `k-sdd` define os **contratos, papéis e fluxos**. A IA que estiver executando deve ler essas definições e adaptá-las para os comandos e ferramentas nativas do seu ambiente:

- **No Orca ADE / Herdr / T3 Code:**
  O orquestrador gerencia os operários através de terminais dedicados, abas nomeadas (`agent1 - UAT-01`) ou comandos nativos de orquestração e worktrees.
- **No Gemini CLI / Antigravity (`agy`):**
  A orquestração é feita via subagentes nativos (`invoke_subagent`, `/agents`, `define_subagent`), aproveitando as ferramentas de sistema de arquivos e comandos.
- **No Claude Code / Codex CLI:**
  Subagentes são disparados via linha de comando ou threads dedicadas passando o conteúdo de `agents/operario.md`.
- **No Cursor / Windsurf / VS Code:**
  As roles podem ser adicionadas como regras customizadas (`.cursor/rules/`, `.windsurfrules`) ou como agentes no chat (`@triagem`, `@orquestrador`, `@operario`).
