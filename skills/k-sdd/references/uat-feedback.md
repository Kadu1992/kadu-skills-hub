# Guia: UAT Feedback Loop & Homologação Humana

> **Objetivo:** Estabelecer o protocolo determinístico para captura de observações de homologação humana (UAT), conversão em novas fases de tarefas com rastreabilidade formal na `spec.md`, execução com commits coesos e fechamento auditável.

---

## 1. O Problema da Homologação Solta

Após o término da execução técnica e aprovação pelo Verifier automatizado, entra em cena o **Humano (PO / Lead / Usuário)** para testar no mundo real (celular, navegador, múltiplos cliques, cenários de borda).

Inevitavelmente, o teste humano revela refinamentos:
* Botões espremidos no mobile;
* Regras de status ou transição de dados para calibrar;
* Ajustes de contraste e cores.

Se o feedback for feito por mensagens soltas, a IA entra em modo "remendo": altera arquivos sem tasks formais, acumula dezenas de mudanças no Git e esquece de commitar.

O **UAT Feedback Loop do `k-sdd`** fecha essa lacuna.

---

## 2. O Ciclo de 6 Etapas do UAT & Reconciliação de Documentos Vivos

```mermaid
graph TD
    A[1. Entrada Fluida: Áudio, Print com Setas, Texto] --> B[2. IA gera feedback.md com Checklist FB-01]
    B --> C[3. IA mapeia na spec.md pending e atualiza frd.md]
    C --> D[4. IA cria Nova Fase em tasks.md com Gates]
    D --> E[5. Execução -> Gates -> Commit Coeso da Fase]
    E --> F[6. Reconciliação Total: feedback, spec, frd, design, PRD, STATE]
```

### Etapa 1: Entrada Fluida do Usuário
O usuário não precisa formatar nada. Ele pode:
* Gravar um áudio no microfone do chat;
* Enviar um print com setas ou anotações visuais apontando o erro/ajuste;
* Digitar tópicos soltos no chat;
* Escrever livremente suas percepções de teste.

### Etapa 2: Estruturação do `feedback.md`
A IA cria (ou atualiza) o arquivo `.specs/features/[feature]/feedback.md` com caixas de seleção numeradas:

```markdown
# UAT Feedback: [Nome da Feature]

## Rodada 1 - [Data]
- **Entrada do Usuário:** [Texto, transcrição de áudio ou resumo de print]

### Checklist de Ajustes Solicitados
- [ ] **FB-01**: Alinhar botões de prazo lado a lado no mobile sem espremer -> *Task: T8*
- [ ] **FB-02**: Alterar status inicial de captura para 'novo' (não agendado) -> *Task: T9*
- [ ] **FB-03**: Documentar regra de transição de status no CRM -> *Task: T10*
```

### Etapa 3: Rastreabilidade na `spec.md` e Alinhamento no `frd.md`
1. A IA abre a `spec.md` da feature e adiciona os novos critérios de aceite derivados do feedback na tabela de **Requirement Traceability** com status inicial **`pending`**:
```markdown
| Requirement ID | User Story | Acceptance Criteria | Status |
| KANBAN-12 | US-02 | AC-KANBAN-12 | pending |
```
2. Se o feedback alterar uma regra de negócio, comportamento ou fluxo de usuário, a IA atualiza imediatamente o **`frd.md`** correspondente (seção de User Stories ou Critérios de Aceite), garantindo que os 4 pilares reflitam a nova intenção.

### Etapa 4: Nova Fase em `tasks.md`
A IA adiciona uma nova fase ao final do `tasks.md` com numeração contínua:
```markdown
### Phase 6: UAT Refinements & Fixes (Round 1)

#### T8: [Descrição da Correção]
**What**: [Ajuste específico]
**Where**: [Arquivo afetado]
**Depends on**: none
**Requirement**: KANBAN-12
**Done when**:
- [ ] [Condição de aceite observável]
- [ ] [npm run build com código 0]
**Gate**: Quick
```

### Etapa 5: Execução, Gates e Commit Coeso
1. A IA executa cada task da fase e valida seu Gate individual;
2. Ao concluir **todas as tasks da fase**, ela gera um **commit semântico coeso e robusto da Fase inteira**:
   ```bash
   git commit -m "fix(kanban): alinha layout mobile, ajusta status inicial e documenta ciclo"
   ```

### Etapa 6: Reconciliação Total de Documentos Vivos (Living Specs)
**A documentação nunca mente sobre o código.** Ao concluir a rodada e validar as alterações com o usuário, a IA atualiza obrigatoriamente toda a suíte de documentos vivos da feature e do produto:
1. **`feedback.md`**: Marca **`[x]`** nos itens resolvidos citando o hash do commit:
   ```markdown
   - [x] **FB-01**: Alinhar botões de prazo... -> *Resolvido em T8 (commit 8a9b0c)*
   ```
2. **`spec.md`**: Atualiza a tabela de rastreabilidade para **`complete`** e adiciona/ajusta os requisitos técnicos EARS (`SHALL`).
3. **`frd.md`**: Garante que os 4 pilares (User Stories e Critérios de Aceite) reflitam a funcionalidade real após a correção.
4. **`tasks.md`**: Marca os checkboxes das tasks de UAT executadas com seus gates comprovados.
5. **`design.md`** *(se aplicável)*: Se houve alteração de layout, cores, espaçamento, tipografia ou comportamento de componentes, atualiza os tokens ou especificações visuais.
6. **`PRD.md`** *(se aplicável)*: Se a mudança alterou o escopo geral do módulo, fluxos macro ou capacidades do sistema, atualiza o mapa de módulos e descrições no `.specs/PRD.md`.
7. **`STATE.md`**: Registra uma decisão arquitetural formal (AD-NNN) com o contexto do ajuste, arquivos tocados e status do handoff.
8. **`validation.md`**: Inclui os cenários de UAT na tabela de aceitação humana com as devidas evidências.
9. O script `validate_state.py` confirma que **nenhum item de feedback ficou pendente**.

---

## 3. Diretriz de Higiene de Contexto (Gerenciamento de Chats)

* **Durante a mesma Feature + UAT Feedback:** Mantenha o **MESMO CHAT**. A IA retém na memória recente o raciocínio dos arquivos recém-criados, permitindo ajustes cirúrgicos e instantâneos.
* **Ao Iniciar uma Nova Feature:** Abra um **NOVO CHAT**. Como o histórico da feature concluída já está persistido no Git, no `validation.md` e no `.specs/STATE.md`, o novo chat inicia com foco máximo, sem poluição de memória e com velocidade total.
* **Retomada de Sessão:** Caso uma sessão seja interrompida no meio do UAT, a IA lê o `feedback.md` e o `STATE.md` para continuar exatamente de onde parou.
