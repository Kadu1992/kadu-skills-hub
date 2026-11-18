# Guia: Os 3 Agentes Especialistas da Esteira k-sdd (Multi-Harness)

> **Objetivo:** Documentar a tríade oficial de agentes de QA/UAT do framework `k-sdd` e demonstrar como instanciá-los e utilizá-los em qualquer harness de IA (Orca ADE, Gemini CLI / Antigravity, Claude Code, Cursor, Windsurf ou Aider).

---

## 1. Visão Geral da Tríade de Agentes

Para garantir máxima separação de responsabilidades e evitar conflitos em arquivos durante a homologação humana, o `k-sdd` divide a esteira em 3 papéis especializados:

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
| **Operário** | [`agents/operario.md`](../agents/operario.md) | Foco cirúrgico no arquivo dominante da sua UAT, rodar gates de build, validar visualmente no navegador e reportar `🟢 corrigida`. | Nunca edita arquivos de `.specs/**` (exceto o status no painel). |

---

## 2. Como Utilizar em Diferentes Harnesses

### 2.1. No Orca ADE
No Orca, os agentes podem ser disparados através do CLI nativo de orquestração:
- **Triagem:** Aba persistente ou comando rápido apontando para `agents/triagem.md` (ou `C:/Users/55119/.orca/roles/Triagem.md`).
- **Orquestrador:** Coordenador do Run de homologação (`orca orchestration run-create --objective "Homologação Feature X"`).
- **Operários:** Spawns dinâmicos sob demanda em abas ordenadas (`agent 1`, `agent 2`...):
  ```bash
  orca orchestration worker-start --task <task_id> --worktree current --agent antigravity --model gemini-3.8-flash --effort high --json
  orca terminal rename --terminal <worker_terminal_handle> --title "agent N - UAT-NN" --json
  ```

### 2.2. No Antigravity CLI / Gemini API
Você pode registrar os agentes usando `define_subagent` ou acioná-los diretamente:
```python
# Exemplo de invocação do Orquestrador:
invoke_subagent(
    TypeName="qa-orchestrator",
    Role="Orquestrador k-sdd",
    Prompt="Leia .specs/qa-uats.md e assuma a coordenação das UATs pendentes seguindo as diretrizes de agents/orquestrador.md."
)
```

### 2.3. No Claude Code / Codex CLI
Inicie sessões ou sub-agentes passando o prompt do arquivo correspondente:
```bash
# Operário focado na UAT-01:
claude --prompt "$(cat agents/operario.md) - Assuma a correção da UAT-01 descrita em .specs/qa-uats.md"
```

### 2.4. No Cursor / Windsurf / VS Code
Adicione os prompts como regras de customização ou Custom Agents na pasta `.cursor/rules/` ou `.windsurfrules`:
- Copie o conteúdo de `agents/triagem.md` para uma regra `@triagem`;
- Copie o conteúdo de `agents/orquestrador.md` para uma regra `@orquestrador`;
- Copie o conteúdo de `agents/operario.md` para uma regra `@operario`.
