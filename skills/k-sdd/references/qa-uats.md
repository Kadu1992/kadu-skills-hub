# Guia: Painel QA-UATs em Markdown & Live Viewer em Tempo Real

> **Objetivo:** Estabelecer o protocolo determinístico para o Painel de QA-UATs em Markdown puro (`.specs/qa-uats.md`), a regra de ouro do pool de operários com afinidade de contexto (*Sticky Threading*), e a especificação de renderização visual local em tempo real (HTML/CSS/JS vanilla).

---

## 1. Filosofia: Harness-Free & Observabilidade Pura

O painel de QA-UATs do `k-sdd` foi desenhado sob o princípio de **independência de infraestrutura**:
- Qualquer modelo de linguagem (Gemini, Claude, GPT, Codex, DeepSeek) operando em qualquer interface (Orca, Herdr, T3 Code, Cursor, Windsurf, VS Code, Claude Code, Aider, terminal ou GitHub Web) consegue ler, interpretar e atualizar o painel usando apenas comandos padrão de leitura e edição de arquivos Markdown.
- Interfaces gráficas (painéis laterais de IDEs ou cockpits locais em HTML) são **leitores secundários de conveniência** baseados em parsing passivo; a **única fonte da verdade (Single Source of Truth)** é o arquivo físico `.specs/qa-uats.md`.

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
| UAT-01 | src/components/Sidebar.tsx | 🟢 corrigida | agent1 | Botão de popout configurado para tela cheia |
| UAT-02 | src/api/sync.ts | 🟡 corrigindo | agent2 | Ajustando timeout do handshake SSE |
| UAT-03 | src/styles/theme.css | 🔴 reprovada | agent3 | Contraste de texto insuficiente no dark mode |
| UAT-04 | src/routes/checkout.tsx | ⚪ aguardando teste | Triagem | Novo fluxo de pagamento via Pix aguardando teste |

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
2. O **Orquestrador de UATs** altera para `🟡 corrigindo` ao despachar a tarefa e atribui o operário correspondente (`agent1`, `agent2`...).
3. Ao término do reparo pelo operário, o status muda para `🟢 corrigida` para reteste do usuário no navegador/aplicação.
4. Ao receber o OK do usuário, o status muda para `✅ validada`.
5. Linhas validadas (`✅`) não são apagadas; ao final do ciclo, são movidas para a seção de Arquivo abaixo.

---

### Arquivo (UATs Concluídas)
| UAT | Domínio (arquivos) | Status | Responsável | Observação |
|---|---|---|---|---|
| UAT-00 | package.json | ✅ validada | agent1 | Configuração inicial do script de build |
```

---

## 4. Regra de Ouro do Pool de Operários: Numeração e Afinidade Estrita (Sticky Threading)

### 4.1. Numeração Sequencial Obrigatória:
Todos os operários despachados devem seguir estritamente o padrão de nomenclatura numérica contínua:
`agent1`, `agent2`, `agent3`, `agent4`...

### 4.2. Afinidade Estrita de Contexto (Sticky Threading):
- **O mesmo operário resolve o mesmo elemento até a aprovação final**:
  - Quando o Orquestrador despacha o `agent1` para resolver um problema (ex: *Elemento X* ou *UAT-01*), este operário carrega em sua thread o raciocínio, os arquivos lidos e a lógica da correção.
  - Se o usuário testar e o item **reprovar no reteste**, o Orquestrador deve **OBRIGATORIAMENTE devolver a correção para o MESMO agente (`agent1`)**! Não crie um novo operário para corrigir o trabalho do `agent1` enquanto o `agent1` estiver com aquele contexto ativo. Mantenha a mesma thread/conversa até que o elemento esteja 100% aprovado (`✅ validada`).
- **Paralelismo Seguro:**
  - Se enquanto o `agent1` estiver trabalhando surgir uma nova UAT em arquivo diferente e independente, despache o `agent2`.
  - Se surgir uma terceira, despache o `agent3`, mantendo cada agente focado e isolado em sua respectiva frente.
- **Anti-Conflito:** Dois operários nunca tocam o mesmo arquivo simultaneamente.

---

## 5. O Ciclo de Vida dos 5 Estados com Emojis

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
| `🟡 corrigindo` | Orquestrador alocou um Operário (`agentN`) e a correção está em andamento. | Orquestrador | Operário implementa o reparo em sua frente. |
| `🟢 corrigida` | Operário concluiu a correção, passou nos gates locais e commita. | Operário | Usuário realiza o reteste prático. |
| `✅ validada` | Usuário humano testou e aprovou formalmente a entrega. | Usuário / Triagem | Concluída. Pronta para ir para o Arquivo. |

---

## 6. Protocolo de Ação para Agentes de IA

### 6.1. Agente de Triagem
- **Ação:** Recebe o relato do usuário, lê `.specs/qa-uats.md`, insere no topo como `🔴 reprovada` e notifica o Orquestrador.

### 6.2. Agente Orquestrador
- **Ação:** Lê `.specs/qa-uats.md`. Se a UAT for reincidência de um elemento já tocado, devolve para o mesmo agente (`agent1`); se for nova frente independente, despacha o próximo número (`agent2`). Atualiza o status para `🟡 corrigindo`.

### 6.3. Agente Operário
- **Ação:** Foco estrito no arquivo dominante, executa a correção, valida visualmente no navegador, altera para `🟢 corrigida` e documenta o que fez.

---

## 7. Higiene do Painel e Arquivamento

- Itens validados (`✅`) nunca são apagados; são transferidos para `### Arquivo (UATs Concluídas)`, mantendo a tabela ativa limpa e focada no ciclo atual com histórico preservado.

---

## 8. Painel Web Local em Tempo Real (Live Viewer em HTML/CSS/JS Vanilla)

Para visualizar o painel em tempo real em uma aba de navegador ou em um segundo monitor com cards dinâmicos, animações pulsantes nos agentes ativos e contadores em tempo real:

### 8.1. Como Funciona a Leitura em Tempo Real:
- O frontend faz um polling periódico leve a cada 1.5 segundos no arquivo `.specs/qa-uats.md` com parâmetro de cache-busting (`?t=` + timestamp).
- Faz o parse das linhas da tabela Markdown usando regex simples e monta os cards nas 4 colunas Kanban:
  1. **Backlog** (`🔴 reprovada` / `⚪ aguardando teste`);
  2. **Corrigindo** (`🟡 corrigindo` — com **efeito de pulso animado** no card e no badge do agente ativo);
  3. **Aguardando Reteste** (`🟢 corrigida`);
  4. **Concluídas** (`✅ validada` e itens arquivados).

### 8.2. Código de Referência Autocontido (`qa-uats-viewer.html`):

Qualquer IA ou desenvolvedor pode instanciar este arquivo diretamente na raiz do projeto ou servi-lo localmente (`npx serve`, `python -m http.server 8080` ou direto no browser):

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>QA-UATs Live Board — k-sdd</title>
  <style>
    :root {
      --bg: #0f172a;
      --card-bg: #1e293b;
      --border: #334155;
      --text: #f8fafc;
      --muted: #94a3b8;
      --yellow: #f59e0b;
      --red: #ef4444;
      --green: #10b981;
      --blue: #3b82f6;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: system-ui, sans-serif; }
    body { background: var(--bg); color: var(--text); padding: 20px; }
    header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
    h1 { font-size: 1.4rem; display: flex; align-items: center; gap: 10px; }
    .pulse-dot { width: 10px; height: 10px; background: var(--green); border-radius: 50%; box-shadow: 0 0 8px var(--green); animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { opacity: 0.4; } 50% { opacity: 1; } 100% { opacity: 0.4; } }
    
    .stats { display: flex; gap: 12px; }
    .stat-badge { background: var(--card-bg); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.85rem; }
    
    .board { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; min-height: 80vh; }
    .column { background: rgba(30, 41, 59, 0.5); border: 1px solid var(--border); border-radius: 8px; padding: 12px; }
    .col-header { font-size: 0.9rem; font-weight: 600; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; }
    
    .card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 6px; padding: 12px; margin-bottom: 10px; transition: transform 0.2s; }
    .card:hover { transform: translateY(-2px); }
    .card.working { border-color: var(--yellow); box-shadow: 0 0 10px rgba(245, 158, 11, 0.2); animation: workingPulse 2s infinite ease-in-out; }
    @keyframes workingPulse { 0% { border-color: var(--yellow); } 50% { border-color: #fbbf24; box-shadow: 0 0 14px rgba(245, 158, 11, 0.4); } 100% { border-color: var(--yellow); } }
    
    .card-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
    .uat-id { font-weight: 700; font-size: 0.85rem; color: var(--blue); }
    .agent-tag { background: #334155; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; color: #cbd5e1; }
    .card.working .agent-tag { background: rgba(245, 158, 11, 0.2); color: var(--yellow); border: 1px solid var(--yellow); }
    .domain { font-size: 0.8rem; color: var(--muted); margin-bottom: 6px; word-break: break-all; }
    .obs { font-size: 0.85rem; line-height: 1.4; }
  </style>
</head>
<body>
  <header>
    <h1><span class="pulse-dot"></span> QA-UATs Live Board</h1>
    <div class="stats" id="stats">Carregando...</div>
  </header>
  
  <div class="board">
    <div class="column" id="col-backlog">
      <div class="col-header"><span>🔴 Backlog / Reprovadas</span> <span id="count-backlog">0</span></div>
      <div class="cards" id="cards-backlog"></div>
    </div>
    <div class="column" id="col-progress">
      <div class="col-header"><span>🟡 Em Correção</span> <span id="count-progress">0</span></div>
      <div class="cards" id="cards-progress"></div>
    </div>
    <div class="column" id="col-review">
      <div class="col-header"><span>🟢 Aguardando Reteste</span> <span id="count-review">0</span></div>
      <div class="cards" id="cards-review"></div>
    </div>
    <div class="column" id="col-done">
      <div class="col-header"><span>✅ Validadas</span> <span id="count-done">0</span></div>
      <div class="cards" id="cards-done"></div>
    </div>
  </div>

  <script>
    async function loadUats() {
      try {
        const res = await fetch('.specs/qa-uats.md?t=' + Date.now());
        if (!res.ok) return;
        const text = await res.text();
        parseAndRender(text);
      } catch (err) {
        console.error("Erro ao carregar qa-uats.md:", err);
      }
    }

    function parseAndRender(md) {
      const lines = md.split(/\r?\n/);
      const items = [];
      let inTable = false;
      let inArchive = false;

      for (let line of lines) {
        line = line.trim();
        if (line.toLowerCase().includes('arquivo (uats concluídas)')) { inArchive = true; }
        if (line.startsWith('|') && line.includes('UAT') && line.includes('Status')) { inTable = true; continue; }
        if (inTable && line.startsWith('|') && line.includes('---')) continue;
        if (inTable && line.startsWith('|')) {
          const parts = line.split('|').map(p => p.trim()).filter((_, idx, arr) => idx > 0 && idx < arr.length - 1);
          if (parts.length >= 4) {
            items.push({
              id: parts[0],
              domain: parts[1],
              status: parts[2],
              assignee: parts[3],
              notes: parts[4] || '',
              archived: inArchive
            });
          }
        } else if (inTable && !line.startsWith('|') && line.length > 0 && !line.startsWith('-')) {
          inTable = false;
        }
      }
      render(items);
    }

    function render(items) {
      const cols = { backlog: [], progress: [], review: [], done: [] };
      
      items.forEach(item => {
        const s = item.status.toLowerCase();
        if (item.archived || s.includes('validada') || s.includes('✅')) {
          cols.done.push(item);
        } else if (s.includes('corrigida') || s.includes('🟢')) {
          cols.review.push(item);
        } else if (s.includes('corrigindo') || s.includes('🟡')) {
          cols.progress.push(item);
        } else {
          cols.backlog.push(item);
        }
      });

      function buildCard(item, isWorking) {
        return `
          <div class="card ${isWorking ? 'working' : ''}">
            <div class="card-top">
              <span class="uat-id">${item.id}</span>
              <span class="agent-tag">${item.assignee || '—'}</span>
            </div>
            <div class="domain">${item.domain}</div>
            <div class="obs">${item.notes}</div>
          </div>
        `;
      }

      document.getElementById('cards-backlog').innerHTML = cols.backlog.map(i => buildCard(i, false)).join('');
      document.getElementById('cards-progress').innerHTML = cols.progress.map(i => buildCard(i, true)).join('');
      document.getElementById('cards-review').innerHTML = cols.review.map(i => buildCard(i, false)).join('');
      document.getElementById('cards-done').innerHTML = cols.done.map(i => buildCard(i, false)).join('');

      document.getElementById('count-backlog').textContent = cols.backlog.length;
      document.getElementById('count-progress').textContent = cols.progress.length;
      document.getElementById('count-review').textContent = cols.review.length;
      document.getElementById('count-done').textContent = cols.done.length;

      document.getElementById('stats').innerHTML = `
        <span class="stat-badge">Total: ${items.length}</span>
        <span class="stat-badge" style="color:var(--yellow)">Ativos: ${cols.progress.length}</span>
        <span class="stat-badge" style="color:var(--green)">Concluídos: ${cols.done.length}</span>
      `;
    }

    setInterval(loadUats, 1500);
    loadUats();
  </script>
</body>
</html>
```
