# Guia: Painel QA-UATs em Markdown (Observabilidade Universal Multi-Agente)

> **Objetivo:** Estabelecer o protocolo determinístico para o Painel de QA-UATs em Markdown puro (`.specs/qa-uats.md`), provendo observabilidade, gestão de ciclo de vida e orquestração de testes de aceitação e homologação humana independente de IDE, harness ou plugins externos.

---

## 1. Filosofia: Harness-Free & Observabilidade Pura

O painel de QA-UATs do `k-sdd` foi desenhado sob o princípio de **independência de infraestrutura**:
- Qualquer modelo de linguagem (Gemini, Claude, GPT, Codex, DeepSeek) operando em qualquer interface (Orca, Cursor, Windsurf, VS Code, Claude Code, Aider, terminal ou GitHub Web) consegue ler, interpretar e atualizar o painel usando apenas comandos padrão de leitura e edição de arquivos Markdown.
- Interfaces gráficas (como a Sidebar do Orca ou cockpits web na porta `8765`) são **leitores secundários de conveniência** baseados em parsing passivo; a **única fonte da verdade (Single Source of Truth)** é o arquivo físico `.specs/qa-uats.md`.

---

## 2. Localização Canônica

Todo projeto que adota a metodologia `k-sdd` mantém o painel na raiz de especificações:
```
meu-projeto/
└── .specs/
    ├── PRD.md
    ├── STATE.md
    ├── qa-uats.md          <-- MAPA MACRO DE UATs DO PROJETO
    └── features/
        └── [feature]/
            ├── frd.md
            ├── spec.md
            ├── tasks.md
            ├── validation.md
            └── feedback.md
```

---

## 3. Estrutura Canônica do Arquivo (`.specs/qa-uats.md`)

```markdown
# Painel QA-UATs

| UAT | Domínio (arquivos) | Status | Responsável | Observação |
|---|---|---|---|---|
| UAT-01 | src/components/Sidebar.tsx | 🟢 corrigida | @operario-ui | Botão de janela separada ajustado para abrir popout |
| UAT-02 | src/api/auth.ts | 🟡 corrigindo | @operario-backend | Ajustando expiração do token JWT para 24h |
| UAT-03 | src/styles/theme.css | 🔴 reprovada | @orquestrador | Contraste de texto insuficiente no dark mode |
| UAT-04 | src/routes/checkout.tsx | ⚪ aguardando teste | @triagem | Novo fluxo de pagamento via Pix aguardando teste |

---

### Legenda
- ⚪ aguardando teste
- 🔴 reprovada
- 🟡 corrigindo
- 🟢 corrigida
- ✅ validada

---

### Regras do Painel
1. A **Triagem** (ou o Humano) insere novas UATs no topo da tabela ativa com status `🔴 reprovada` (em caso de falha de teste) ou `⚪ aguardando teste` (novo cenário).
2. O **Orquestrador de UATs** altera para `🟡 corrigindo` ao despachar a tarefa e atribui o agente responsável (`@agente`).
3. Ao término do reparo pelo operário, o status muda para `🟢 corrigida` para reteste do usuário no navegador/aplicação.
4. Ao receber o OK do usuário, o status muda para `✅ validada`.
5. Linhas validadas (`✅`) não são apagadas; ao final do ciclo, são movidas para a seção de Arquivo abaixo.

---

### Arquivo (UATs Concluídas)
| UAT | Domínio (arquivos) | Status | Responsável | Observação |
|---|---|---|---|---|
| UAT-00 | package.json | ✅ validada | @antigravity | Configuração inicial do script de inicialização |
```

---

## 4. O Ciclo de Vida dos 5 Estados com Emojis

O estado de cada UAT é representado de forma determinística por emojis, permitindo leitura visual humana imediata e parse inequívoco por regex/código:

```
[ ⚪ aguardando teste ]  ──(Falha no teste)──► [ 🔴 reprovada ]
                                                       │
                                            (Despacho do Orquestrador)
                                                       ▼
[ ✅ validada ] ◄──(Aprovação Humana)─── [ 🟢 corrigida ] ◄──(Reparo Concluído)─── [ 🟡 corrigindo ]
      │
(Fim do Ciclo)
      ▼
[ Movida para Arquivo ]
```

| Emoji / Status | Significado Operacional | Quem Atualiza | Ação Próxima |
| :--- | :--- | :--- | :--- |
| `⚪ aguardando teste` | UAT cadastrada, código pronto, aguardando validação do usuário. | Triagem / Operário | Usuário realiza o teste. |
| `🔴 reprovada` | O usuário testou e o resultado foi insatisfatório ou quebrou. | Usuário / Triagem | Orquestrador assume para planejar correção. |
| `🟡 corrigindo` | Orquestrador alocou um Operário (`@agente`) e a correção está em andamento. | Orquestrador | Operário implementa o reparo em sua branch/worktree. |
| `🟢 corrigida` | Operário concluiu a correção, passou nos gates locais e commita. | Operário | Usuário realiza o reteste prático. |
| `✅ validada` | Usuário humano testou e aprovou formalmente a entrega. | Usuário / Triagem | Concluída. Pronta para ir para o Arquivo. |

---

## 5. Protocolo de Ação para Agentes de IA

### 5.1. Agente de Triagem (ou IA de Entrada)
- **Gatilho:** Usuário relata falha, comportamento inesperado ou necessidade de ajuste ("botão X não funciona", "layout desalinhou", etc.).
- **Ação:**
  1. Abre `.specs/qa-uats.md`;
  2. Adiciona uma nova linha imediatamente abaixo do cabeçalho da tabela ativa;
  3. Preenche:
     - `UAT`: Próximo identificador sequencial (ex: `UAT-05`);
     - `Domínio`: Arquivos ou componentes suspeitos (ex: `src/views/Kanban.tsx`);
     - `Status`: `🔴 reprovada`;
     - `Responsável`: `@orquestrador` (ou `@triagem`);
     - `Observação`: Descrição resumida da falha reportada pelo usuário.

### 5.2. Agente Orquestrador
- **Gatilho:** Presença de UATs com status `🔴 reprovada` no painel.
- **Ação:**
  1. Abre `.specs/qa-uats.md`;
  2. Altera o status da UAT para `🟡 corrigindo`;
  3. Atualiza o campo `Responsável` para o agente operário que executará a tarefa (ex: `@operario-ui`);
  4. Adiciona ou atualiza a fase correspondente no arquivo `tasks.md` da feature;
  5. Despacha o operário com o contexto cirúrgico do problema.

### 5.3. Agente Operário (Executor)
- **Gatilho:** Tarefa de correção delegada pelo Orquestrador.
- **Ação:**
  1. Executa a correção no código;
  2. Valida o Gate local (`npm run build`, testes unitários);
  3. Gera o commit semântico coeso;
  4. Abre `.specs/qa-uats.md` e altera o status da UAT para `🟢 corrigida`;
  5. Atualiza a coluna `Observação` explicando brevemente o que foi feito e os arquivos tocados;
  6. Notifica o Orquestrador / Usuário que a entrega está pronta para reteste.

---

## 6. Higiene do Painel e Regra de Arquivamento

- **Imutabilidade e Rastreabilidade:** Nenhuma UAT validada é excluída.
- **Tabela Ativa Enxuta:** Para evitar poluição visual e manter a tabela ativa focada apenas no trabalho em andamento, todas as linhas com status `✅ validada` são movidas para a seção `### Arquivo (UATs Concluídas)` ao encerramento do ciclo ou da feature.
- **Parsing Automático:** Sistemas e scripts que consom o arquivo identificam itens arquivados pela presença do cabeçalho `### Arquivo (UATs Concluídas)`, tratando-os automaticamente como categoria `done`.

---

## 7. Relação com `feedback.md` e `validation.md`

| Artefato | Escopo | Nível de Detalhe | Destinatário Principal |
| :--- | :--- | :--- | :--- |
| **`.specs/qa-uats.md`** | **Macro / Projeto** | Tabela Kanban de UATs do sistema todo | Visão geral para Humanos e Orquestração Multi-Agente |
| **`feedback.md`** | **Micro / Feature** | Checklists `- [ ] FB-XX` com CSS de risco reativo | Ajustes finos de homologação da feature específica |
| **`validation.md`** | **Técnico / Feature** | Relatório do Verifier com testes automáticos e mutação | Auditoria técnica do Verifier independente |
