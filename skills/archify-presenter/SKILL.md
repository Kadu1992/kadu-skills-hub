---
name: archify-presenter
description: Create interactive, animated Archify architecture and workflow presentation diagrams in HTML/SVG with live laser pointer, right-click laser drawing trail, hover card jump, click-focus speaking mode, trace motion animation, zero layout shift, user-select protection, origin-card color-matched connections, and preset cycling (Signal Flow, Blueprint, Editorial, Obsidian Gold, Nordic Frost, Midnight Tokyo). Use when the user types /archify-presenter, asks for an interactive presentation diagram, laser drawing diagram, or requests a visual Archify diagram with animated signal flows and card focus based on a document or text prompt.
---

# Archify Presenter Skill

Crie diagramas e infográficos visuais interativos de alta fidelidade para apresentações executivas (Pitch C-Level / Reuniões de Liderança), integrando a especificação do **Archify** com recursos de apresentação em tempo real.

## 🚀 Recursos Nativos do Archify Presenter

1. **🔴 Ponteiro Laser Executivo (Pointer, Trail & Double-Click Off):**
   * Cursor laser vermelho ativável por botão ou clique com o botão direito do mouse.
   * **1 Clique com Botão Direito:** Liga o laser pointer para apontar elementos na apresentação.
   * **Segurar Botão Direito e Arrastar:** Desenha linhas em rastro neon vermelho que desvanecem suavemente em ~1 segundo. Soltar o botão interrompe o rastro, mantendo o laser ativo.
   * **Duplo Clique com Botão Direito:** Desliga o laser totalmente e restaura o cursor normal da seta.
   * **Zero Layout Shift:** Cabeçalho fixo no topo com rótulo do botão de largura constante (`min-width: 72px`), garantindo 0px de deslocamento de interface ao alternar o laser.

2. **🦘 Efeito Salto no Hover (Hover Jump):**
   * Ao passar o mouse sobre qualquer card/nó da arquitetura, ele salta suavemente para cima (`transform: translateY(-8px) scale(1.03)`) com sombra luminosa.

3. **🎯 Modo Foco de Apresentador (Click Focus / Speaking Mode):**
   * Ao clicar em um card com o botão esquerdo, ele salta em grande destaque (`transform: translateY(-16px) scale(1.07)`), ganha uma borda neon verde e **esmaece suavemente todos os outros cards da tela (opacidade 35%)**, concentrando a atenção da diretoria no tópico em discussão.
   * **Proteção contra Seleção de Texto:** Regra CSS `user-select: none` para impedir destaques azuis acidentais de texto nos cliques.
   * Clicar no mesmo card ou no fundo da tela desativa o modo foco.

4. **▶️ Animação de Sinais em Tempo Real & Cores de Origem:**
   * Partículas luminosas percorrem as conexões (`<animateMotion>`) com linhas pontilhadas energizadas.
   * **Harmonização em Uníssono:** Todas as partículas `<animateMotion>` usam a mesma duração uniforme (`dur="2.2s"`) para fluírem juntas em cadência e ritmo perfeitos por todo o fluxo.
   * **Setas e Conexões Combinadas:** A cor da linha, da partícula e da ponta da seta (`<marker>`) corresponde exatamente à cor da borda do card de origem.
   * Botão de **Pausar / Rodar** que congela e retoma as animações SMIL nativamente (`svgEl.pauseAnimations()` e `unpauseAnimations()`).

5. **🎨 Ciclo de 6 Presets Visuais Corporativos Archify:**
   * **Signal Flow:** Fundo escuro cybertech (`#030711`), bordas neon ciano/verde/púrpura e tipografia limpa.
   * **Blueprint:** Fundo de engenharia com grade técnica de 32px (`#06131f`), bordas azuis e acabamento de projeto técnico.
   * **Editorial:** Fundo sutil de papel publicado (`#181611` / `#f2eee5`), tipografia serifada (Georgia) e destaques em tom vermelhão.
   * **Obsidian Gold:** Luxo C-Level em tom obsidian profundo (`#0b0d13`) com destaques em Dourado Champagne & Âmbar (`#f59e0b`).
   * **Nordic Frost:** Visual Glassmorphism Enterprise (`#0f172a`), painéis foscos e destaques em Ciano Aurora & Violeta Boreal.
   * **Midnight Tokyo:** Fundo OLED Pitch Black (`#000000`) com alto contraste neon vibrante para grandes telas de projeção.

6. **🌓 Alternador de Tema (Dark / Light Mode):**
   * Alternância entre Modo Escuro e Modo Claro para todos os 6 presets (12 combinações visuais).

7. **📐 Regra Anti-Sobreposição, Coordenadas Diretas e Layout Espaçado:**
   * **Coordenadas Diretas sem `transform="translate(x, y)"`**: NUNCA utilize `transform="translate(x, y)"` na tag `<g class="node">`. Posicione cada elemento informando as coordenadas absolutas diretamente nos atributos `<rect x="..." y="...">` e `<text x="..." y="...">`. Isso evita conflitos com o CSS `:hover` e impede que o card pulando ao passar o mouse.
   * Todo card DEVE pertencer estritamente à sua raia (`Lane`).
   * O valor de `x` do card NUNCA pode invadir a raia vizinha (deve estar contido em `lane.x + 15` até `lane.x + lane.width - 15`).
   * Cards da mesma raia DEVEM ter espaçamento vertical mínimo de 30px entre si (`node[n+1].y >= node[n].y + node[n].height + 30`).
   * Dois cards NUNCA podem se sobrepor visualmente em X nem em Y.

8. **🔄 Protocolo de Manutenção Contínua de Arquitetura (Continuous Sync & Pasta Padrão):**
   * **Pasta Padrão Fixa (`Architecture_Presentation/`):** Todos os diagramas HTML gerados pelo Archify Presenter DEVEM ser salvos obrigatoriamente dentro da pasta `Architecture_Presentation/` na raiz do projeto (ex: `Architecture_Presentation/<nome_do_diagrama>.html`). Se a pasta não existir, crie-a automaticamente.
   * **Garantia de Fidelidade:** Diagramas de arquitetura Archify (`.html`) são documentos vivos do ecossistema.
   * **Verificação Proativa Determinística:** Sempre que houver mudanças no sistema (alteração de escopo, novos endpoints, novos modelos de IA, reestruturações de tabelas de banco de dados ou novos serviços), o agente DEVE consultar a pasta fixa `Architecture_Presentation/` do projeto ativo.
   * **Atualização Cirúrgica:** Ao identificar alterações no ecossistema, consulte os arquivos `.html` dentro de `Architecture_Presentation/` (ou na raiz, em caso de legados) e atualize pontualmente os textos dos nós afetados (`.node-title`, `.node-sub`, `.node-meta`), novos fluxos de conexão e métricas, mantendo 100% de paridade entre o código-fonte em execução e a representação visual da arquitetura.

---

## 🛠️ Como Executar a Skill

Quando o usuário solicitar o uso da skill `/archify-presenter` (ou pedir um diagrama interativo de um documento `.md`, texto descritivo, ou durante alterações de escopo/arquitetura):

1. **Leia a Fonte de Conhecimento:**
   * Se o usuário referenciar um documento (ex: `@[documento.md]`), analise o conteúdo para extrair:
     * Componentes/Nós do sistema.
     * Camadas/Lanes semânticas (ex: Usuários, Orquestração, IA/RAG, Legados).
     * Relações e fluxos de dados entre os componentes.
     * Métricas de KPI, custos e ROI (se aplicável).
   * Se for solicitado por texto digitado, modele os componentes e fluxos correspondentes.

2. **Gere o Arquivo HTML Standalone na Pasta Padrão:**
   * Garanta que a pasta `Architecture_Presentation/` exista na raiz do projeto ativo.
   * Crie o arquivo `Architecture_Presentation/<nome_do_diagrama>.html` utilizando a estrutura do motor Archify Presenter abaixo.

3. **Manutenção e Atualização Contínua de Diagramas Existentes:**
   * Sempre que o escopo ou componentes do projeto forem modificados em código, consulte os arquivos dentro de `Architecture_Presentation/`.
   * Atualize cirurgicamente os textos dos nós, métricas e conexões para refletir as mudanças do código, banco de dados e APIs.

---

## 📄 Estrutura do Código do Motor Archify Presenter

```html
<!DOCTYPE html>
<html lang="pt-BR" data-theme="dark" data-preset="signal-flow" data-motion="running">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="generator" content="archify-presenter 2.13.0">
  <title>[TITULO DO DIAGRAMA]</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    /* PRESETS ARCHIFY */
    :root, [data-preset="signal-flow"][data-theme="dark"] {
      --bg: #030711; --panel: rgba(7, 16, 30, 0.86); --panel-border: #1d3350;
      --text: #f5fbff; --text-muted: #9eb0c7; --text-dim: #52667f;
      --lane-bg: rgba(9, 22, 40, 0.5); --lane-stroke: #2c4564;
      --node-usr-border: #67e8f9; --node-core-border: #5eead4; --node-ai-border: #c4b5fd; --node-sys-border: #a5b4c7;
      --primary: #6366f1; --accent-emerald: #10b981;
      --font-heading: 'Outfit', sans-serif; --font-body: 'Inter', sans-serif; --font-mono: 'JetBrains Mono', monospace;
    }
    [data-preset="signal-flow"][data-theme="light"] {
      --bg: #f4f9fc; --panel: rgba(255, 255, 255, 0.92); --panel-border: #bfd5e2;
      --text: #102638; --text-muted: #587287; --text-dim: #8aa2b4;
      --lane-bg: rgba(232, 243, 248, 0.6); --lane-stroke: #a9c5d5;
      --node-usr-border: #0789a1; --node-core-border: #087f69; --node-ai-border: #7254c7; --node-sys-border: #607a8c;
      --primary: #0284c7; --accent-emerald: #059669;
    }
    [data-preset="blueprint"][data-theme="dark"] {
      --bg: #06131f; --panel: rgba(7, 27, 43, 0.92); --panel-border: #27627f;
      --text: #e3f6ff; --text-muted: #91b8ca; --text-dim: #557e92;
      --lane-bg: rgba(10, 43, 66, 0.4); --lane-stroke: #34799a;
      --node-usr-border: #66d9ef; --node-core-border: #69dfbd; --node-ai-border: #b4a8ff; --node-sys-border: #a7cad9;
      --primary: #38bdf8; --accent-emerald: #34d399;
    }
    [data-preset="blueprint"][data-theme="light"] {
      --bg: #edf7fa; --panel: rgba(249, 253, 255, 0.96); --panel-border: #78aabd;
      --text: #123344; --text-muted: #4e7486; --text-dim: #86a6b4;
      --lane-bg: rgba(210, 232, 240, 0.45); --lane-stroke: #83b2c4;
      --node-usr-border: #087f9c; --node-core-border: #08755f; --node-ai-border: #6757a8; --node-sys-border: #506f7e;
      --primary: #0284c7; --accent-emerald: #059669;
    }
    [data-preset="editorial"][data-theme="dark"] {
      --bg: #181611; --panel: rgba(35, 31, 24, 0.96); --panel-border: #625a4a;
      --text: #f4eddf; --text-muted: #b9ae9b; --text-dim: #776e60;
      --lane-bg: rgba(52, 46, 35, 0.46); --lane-stroke: #726957;
      --node-usr-border: #7fc6c7; --node-core-border: #8fc29e; --node-ai-border: #c0a4d0; --node-sys-border: #b8ad99;
      --primary: #dd6b3d; --accent-emerald: #8fc29e; --font-heading: Georgia, serif;
    }
    [data-preset="editorial"][data-theme="light"] {
      --bg: #f2eee5; --panel: rgba(251, 248, 241, 0.97); --panel-border: #c4b9a6;
      --text: #242018; --text-muted: #6f6658; --text-dim: #a09788;
      --lane-bg: rgba(229, 221, 207, 0.42); --lane-stroke: #b8aa94;
      --node-usr-border: #287e84; --node-core-border: #397b53; --node-ai-border: #765d86; --node-sys-border: #746b5e;
      --primary: #bb4c23; --accent-emerald: #397b53; --font-heading: Georgia, serif;
    }
    /* PRESET 4: OBSIDIAN GOLD (Luxo C-Level Dourado & Âmbar) */
    [data-preset="obsidian-gold"][data-theme="dark"] {
      --bg: #0b0d13; --panel: rgba(22, 24, 34, 0.92); --panel-border: #3b3323;
      --text: #fef3c7; --text-muted: #d4a373; --text-dim: #785d3f;
      --lane-bg: rgba(32, 27, 18, 0.5); --lane-stroke: #524227;
      --node-usr-border: #f59e0b; --node-core-border: #10b981; --node-ai-border: #ec4899; --node-sys-border: #eab308;
      --primary: #f59e0b; --accent-emerald: #10b981;
    }
    [data-preset="obsidian-gold"][data-theme="light"] {
      --bg: #fffbeb; --panel: rgba(255, 255, 255, 0.96); --panel-border: #fde68a;
      --text: #78350f; --text-muted: #92400e; --text-dim: #b45309;
      --lane-bg: rgba(254, 243, 199, 0.6); --lane-stroke: #fcd34d;
      --node-usr-border: #d97706; --node-core-border: #059669; --node-ai-border: #db2777; --node-sys-border: #ca8a04;
      --primary: #d97706; --accent-emerald: #059669;
    }
    /* PRESET 5: NORDIC FROST (Glassmorphism Enterprise Slate/Aurora) */
    [data-preset="nordic-frost"][data-theme="dark"] {
      --bg: #0f172a; --panel: rgba(30, 41, 59, 0.85); --panel-border: #334155;
      --text: #f1f5f9; --text-muted: #94a3b8; --text-dim: #64748b;
      --lane-bg: rgba(30, 41, 59, 0.45); --lane-stroke: #475569;
      --node-usr-border: #38bdf8; --node-core-border: #818cf8; --node-ai-border: #f472b6; --node-sys-border: #cbd5e1;
      --primary: #38bdf8; --accent-emerald: #34d399;
    }
    [data-preset="nordic-frost"][data-theme="light"] {
      --bg: #f0f9ff; --panel: rgba(255, 255, 255, 0.95); --panel-border: #bae6fd;
      --text: #0c4a6e; --text-muted: #0369a1; --text-dim: #38bdf8;
      --lane-bg: rgba(224, 242, 254, 0.6); --lane-stroke: #7dd3fc;
      --node-usr-border: #0284c7; --node-core-border: #4f46e5; --node-ai-border: #c026d3; --node-sys-border: #475569;
      --primary: #0284c7; --accent-emerald: #059669;
    }
    /* PRESET 6: MIDNIGHT TOKYO (OLED Pitch Black Contrast) */
    [data-preset="midnight-tokyo"][data-theme="dark"] {
      --bg: #000000; --panel: rgba(15, 15, 22, 0.95); --panel-border: #262636;
      --text: #ffffff; --text-muted: #a1a1aa; --text-dim: #52525b;
      --lane-bg: rgba(20, 20, 30, 0.6); --lane-stroke: #3f3f56;
      --node-usr-border: #00ff9d; --node-core-border: #00e5ff; --node-ai-border: #ff007f; --node-sys-border: #ffb703;
      --primary: #00ff9d; --accent-emerald: #00ff9d;
    }

    /* IMPEDE SELEÇÃO DE TEXTO AZUL NO CLIQUE DO RATO */
    * { 
      box-sizing: border-box; 
      margin: 0; 
      padding: 0; 
      user-select: none;
      -webkit-user-select: none;
      -moz-user-select: none;
      -ms-user-select: none;
    }
    body { background-color: var(--bg); color: var(--text); font-family: var(--font-body); min-height: 100vh; display: flex; flex-direction: column; padding: 0.75rem 1.25rem 1.25rem 1.25rem; transition: background 0.3s, color 0.3s; }
    
    body.has-laser, body.has-laser * { cursor: none !important; }
    #laser-pointer { position: fixed; width: 16px; height: 16px; border-radius: 50%; background: #ff0055; box-shadow: 0 0 12px #ff0055, 0 0 24px #ff0055, 0 0 36px #ff0055; pointer-events: none; z-index: 9999; transform: translate(-50%, -50%); display: none; }
    body.has-laser #laser-pointer { display: block; }
    #laser-canvas { position: fixed; inset: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 9998; }

    html[data-preset="blueprint"] body,
    html[data-preset="blueprint"] .archify-canvas { background-image: linear-gradient(color-mix(in srgb, var(--panel-border) 40%, transparent) 1px, transparent 1px), linear-gradient(90deg, color-mix(in srgb, var(--panel-border) 40%, transparent) 1px, transparent 1px); background-size: 32px 32px; background-position: -1px -1px; }
    html[data-preset="editorial"] body { background-image: linear-gradient(90deg, transparent 0, transparent 4rem, color-mix(in srgb, var(--primary) 20%, transparent) 4rem, color-mix(in srgb, var(--primary) 20%, transparent) calc(4rem + 1px), transparent calc(4rem + 1px)); }

    .archify-app { max-width: 1400px; margin: 0 auto; width: 100%; display: flex; flex-direction: column; gap: 1rem; flex: 1; }
    .archify-header { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; padding: 1rem 1.5rem; background: var(--panel); border: 1px solid var(--panel-border); border-radius: 16px; backdrop-filter: blur(12px); }
    .archify-tag { font-family: var(--font-mono); font-size: 0.7rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; padding: 0.25rem 0.6rem; border-radius: 6px; background: color-mix(in srgb, var(--primary) 20%, transparent); border: 1px solid var(--primary); color: var(--primary); }
    .archify-title { font-family: var(--font-heading); font-size: 1.35rem; font-weight: 700; color: var(--text); }
    .archify-controls { display: flex; align-items: center; gap: 0.5rem; }
    .archify-btn { background: color-mix(in srgb, var(--text) 5%, transparent); border: 1px solid var(--panel-border); color: var(--text); padding: 0.45rem 0.85rem; border-radius: 8px; font-family: var(--font-mono); font-size: 0.8rem; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 0.4rem; transition: background 0.2s, border-color 0.2s, color 0.2s; }
    .archify-btn:hover { background: color-mix(in srgb, var(--primary) 20%, transparent); border-color: var(--primary); }
    .archify-btn.active { background: color-mix(in srgb, var(--accent-emerald) 25%, transparent); border-color: var(--accent-emerald); color: var(--accent-emerald); }
    .archify-btn.laser-active { background: rgba(244, 63, 94, 0.25); border-color: #f43f5e; color: #fda4af; box-shadow: 0 0 12px rgba(244, 63, 94, 0.4); }
    #laser-label { display: inline-block; min-width: 72px; text-align: center; }
    .archify-canvas { flex: 1; background: var(--panel); border: 1px solid var(--panel-border); border-radius: 20px; padding: 1.5rem; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3); overflow: auto; display: flex; align-items: center; justify-content: center; }

    @keyframes dash-flow { from { stroke-dashoffset: 32; } to { stroke-dashoffset: 0; } }
    .edge-animated { fill: none; stroke-width: 2.5; stroke-dasharray: 8 8; animation: dash-flow 1.2s linear infinite; will-change: stroke-dashoffset; vector-effect: non-scaling-stroke; }
    html[data-motion="paused"] .edge-animated { animation-play-state: paused !important; }
    svg.archify-svg-render { width: 100%; min-width: 1150px; height: auto; }

    .bg-rect { fill: var(--bg); }
    .lane-box { fill: var(--lane-bg); stroke: var(--lane-stroke); stroke-width: 1.5px; stroke-dasharray: 6 6; rx: 16px; }
    .lane-title { font-family: var(--font-heading); font-size: 12px; font-weight: 800; letter-spacing: 1.5px; fill: var(--text-dim); }

    .node-usr { stroke: var(--node-usr-border); }
    .node-core { stroke: var(--node-core-border); }
    .node-ai { stroke: var(--node-ai-border); }
    .node-sys { stroke: var(--node-sys-border); }
    .node-title { font-family: var(--font-heading); font-weight: 700; font-size: 14px; fill: var(--text); }
    .node-sub { font-family: var(--font-body); font-size: 11px; fill: var(--text-muted); }
    .node-meta { font-family: var(--font-mono); font-size: 10px; fill: var(--text); }

    .node { cursor: pointer; transform-box: fill-box; transform-origin: center center; transition: transform 0.2s ease, opacity 0.3s, filter 0.3s; }
    .node:hover { transform: scale(1.02); filter: drop-shadow(0 10px 24px rgba(99, 102, 241, 0.45)); }
    .node.active-speaking { transform: translateY(-12px) scale(1.05) !important; filter: drop-shadow(0 20px 40px rgba(16, 185, 129, 0.8)) !important; }
    .node.active-speaking rect { stroke: #10b981 !important; stroke-width: 3px !important; }
    svg.has-active-focus .node:not(.active-speaking) { opacity: 0.35; filter: grayscale(0.5); }

    .archify-footer { display: flex; align-items: center; justify-content: space-between; padding: 0.75rem 1.25rem; background: var(--panel); border: 1px solid var(--panel-border); border-radius: 12px; font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); }
  </style>
</head>
<body>
  <div id="laser-pointer"></div>
  <canvas id="laser-canvas"></canvas>

  <div class="archify-app">
    <header class="archify-header">
      <div style="display: flex; align-items: center; gap: 0.75rem;">
        <span class="archify-tag">ARCHIFY INTERACTIVE PRESENTATION</span>
        <h1 class="archify-title">[TITULO DO DIAGRAMA]</h1>
      </div>
      <div class="archify-controls">
        <button class="archify-btn" id="btn-laser" onclick="toggleLaser()">🔴 Laser Pointer: <span id="laser-label">DESLIGADO</span></button>
        <button class="archify-btn active" id="btn-motion" onclick="toggleMotion()">▶️ Animação: <span id="motion-label">Rodando</span></button>
        <button class="archify-btn" onclick="cyclePreset()">🎨 Preset: <span id="preset-label">SIGNAL FLOW</span></button>
        <button class="archify-btn" onclick="toggleTheme()">🌓 Tema: <span id="theme-label">ESCURO</span></button>
      </div>
    </header>

    <main class="archify-canvas">
      <svg id="arch-svg" class="archify-svg-render" viewBox="0 0 1200 620" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- LAYOUT VISUAL SEMÂNTICO (LANES, PARTICULAS ANIMADAS & NODES) -->
      </svg>
    </main>

    <footer class="archify-footer">
      <div><span>🖍️ Segure o BOTÃO DIREITO do mouse para riscar com laser que desvanece • Clique no card para destacar durante a fala</span></div>
      <div><span>Archify Presenter</span></div>
    </footer>
  </div>

  <script>
    let laserActive = false, isDrawingLaser = false;
    let lastRightClickTime = 0;
    const laserPointer = document.getElementById('laser-pointer');
    const laserBtn = document.getElementById('btn-laser');
    const laserLabel = document.getElementById('laser-label');
    const canvas = document.getElementById('laser-canvas');
    const ctx = canvas.getContext('2d');
    let laserTrails = [];

    function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
    window.addEventListener('resize', resizeCanvas); resizeCanvas();

    let currentMouseX = window.innerWidth / 2, currentMouseY = window.innerHeight / 2;

    function updatePointerPosition(x, y) {
      if (typeof x === 'number' && typeof y === 'number') {
        currentMouseX = x; currentMouseY = y;
      }
      laserPointer.style.left = currentMouseX + 'px'; 
      laserPointer.style.top = currentMouseY + 'px'; 
    }

    function toggleLaser(state, evt) {
      if (evt && typeof evt.clientX === 'number') {
        updatePointerPosition(evt.clientX, evt.clientY);
      } else {
        updatePointerPosition();
      }

      if (typeof state === 'boolean') laserActive = state;
      else laserActive = !laserActive;

      if (laserActive) { 
        document.body.classList.add('has-laser'); 
        laserBtn.classList.add('laser-active'); 
        laserLabel.textContent = 'LIGADO'; 
      } else { 
        document.body.classList.remove('has-laser'); 
        laserBtn.classList.remove('laser-active'); 
        laserLabel.textContent = 'DESLIGADO'; 
        isDrawingLaser = false;
      }
    }

    document.addEventListener('contextmenu', (e) => e.preventDefault());
    
    // EXCLUSIVO BOTÃO DIREITO DO MOUSE (BOTÃO ESQUERDO É 100% NORMAL/LIVRE)
    document.addEventListener('mousedown', (e) => {
      updatePointerPosition(e.clientX, e.clientY);
      if (e.button === 2) {
        const now = Date.now();
        // Duplo clique com botão direito desliga o laser totalmente
        if (now - lastRightClickTime < 350) {
          toggleLaser(false, e);
          isDrawingLaser = false;
          lastRightClickTime = 0;
          return;
        }
        lastRightClickTime = now;

        // Se estiver desligado, 1 clique liga o laser ponteiro
        if (!laserActive) toggleLaser(true, e);
        
        // Segurar EXCLUSIVAMENTE o botão direito ativa o rastro de desenho neon
        isDrawingLaser = true;
        addLaserPoint(e.clientX, e.clientY, true);
      }
    });

    document.addEventListener('mouseup', (e) => { 
      if (e.button === 2) {
        isDrawingLaser = false; // Soltou o botão direito: interrompe rastro neon, mantém a bolinha do laser para apontar
      }
    });

    document.addEventListener('mousemove', (e) => {
      updatePointerPosition(e.clientX, e.clientY);
      if (laserActive) { 
        if (isDrawingLaser && e.buttons === 2) {
          addLaserPoint(e.clientX, e.clientY, false);
        }
      }
    });

    function addLaserPoint(x, y, isNewStroke) { laserTrails.push({ x: x, y: y, opacity: 1.0, isNewStroke: isNewStroke }); }
    function renderLaserTrail() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      if (laserTrails.length > 1) {
        for (let i = 1; i < laserTrails.length; i++) {
          const pt1 = laserTrails[i - 1], pt2 = laserTrails[i];
          if (pt2.isNewStroke) continue;
          ctx.beginPath(); ctx.moveTo(pt1.x, pt1.y); ctx.lineTo(pt2.x, pt2.y);
          ctx.lineWidth = 6 * pt2.opacity; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
          ctx.strokeStyle = `rgba(255, 0, 85, ${pt2.opacity})`; ctx.shadowColor = '#ff0055'; ctx.shadowBlur = 15 * pt2.opacity; ctx.stroke();
        }
      }
      for (let i = 0; i < laserTrails.length; i++) laserTrails[i].opacity -= 0.025;
      laserTrails = laserTrails.filter(p => p.opacity > 0);
      requestAnimationFrame(renderLaserTrail);
    }
    renderLaserTrail();

    // CARD CLICK FOCUS / SPEAKING MODE
    const svgElement = document.getElementById('arch-svg');
    const nodes = document.querySelectorAll('.node');
    nodes.forEach(node => {
      node.addEventListener('click', (e) => {
        if (e.button === 2) return; e.stopPropagation();
        const isAlreadyActive = node.classList.contains('active-speaking');
        nodes.forEach(n => n.classList.remove('active-speaking'));
        if (!isAlreadyActive) { node.classList.add('active-speaking'); svgElement.classList.add('has-active-focus'); }
        else { svgElement.classList.remove('has-active-focus'); }
      });
    });
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.node') && e.button !== 2) { nodes.forEach(n => n.classList.remove('active-speaking')); svgElement.classList.remove('has-active-focus'); }
    });

    // SMIL ANIMATION CONTROL
    let isRunning = true;
    const svgEl = document.getElementById('arch-svg');
    function toggleMotion() {
      const html = document.documentElement;
      const btn = document.getElementById('btn-motion');
      const label = document.getElementById('motion-label');
      if (isRunning) { 
        html.setAttribute('data-motion', 'paused'); 
        if (svgEl.pauseAnimations) svgEl.pauseAnimations(); 
        btn.classList.remove('active'); 
        label.textContent = 'Pausada'; 
      } else { 
        html.setAttribute('data-motion', 'running'); 
        if (svgEl.unpauseAnimations) svgEl.unpauseAnimations(); 
        btn.classList.add('active'); 
        label.textContent = 'Rodando'; 
      }
      isRunning = !isRunning;
    }

    // THEME & PRESETS CONTROL
    function toggleTheme() {
      const html = document.documentElement;
      const current = html.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      document.getElementById('theme-label').textContent = next.toUpperCase();
    }
    const presets = ['signal-flow', 'blueprint', 'editorial', 'obsidian-gold', 'nordic-frost', 'midnight-tokyo'];
    let currentPresetIdx = 0;
    function cyclePreset() {
      currentPresetIdx = (currentPresetIdx + 1) % presets.length;
      const nextPreset = presets[currentPresetIdx];
      document.documentElement.setAttribute('data-preset', nextPreset);
      document.getElementById('preset-label').textContent = nextPreset.replace('-', ' ').toUpperCase();
    }
  </script>
</body>
</html>
```
