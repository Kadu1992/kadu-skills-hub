# Archify Presenter — Interactive Architecture & Workflow Presentation Skill

**Archify Presenter** é uma skill personalizada para criação autônoma de diagramas visuais e infográficos interativos em HTML/SVG voltados para **Apresentações Executivas (Pitch C-Level / Reuniões de Liderança)**.

---

## 📦 Instalação

Instale diretamente no seu projeto com um único comando:

```bash
npx skills add Kadu1992/archify-presenter
```

Ou instale globalmente na sua máquina/IDE:

```bash
npx skills add Kadu1992/archify-presenter -g
```

> **Dica**: Esta skill também pode ser instalada via catálogo central [Kadu Skills Hub](https://github.com/Kadu1992/kadu-skills-hub) (`npx skills add Kadu1992/kadu-skills-hub`).

---

## 🚀 Recursos Principais (Presenter Superpowers)

### 🔴 1. Ponteiro Laser Executivo (Pointer, Trail & Double-Click Off)
* **Cursor Laser Vermelho:** Ativável pelo botão `🔴 Laser Pointer` no topo da tela ou por clique com o botão direito do mouse.
* **Isolamento de Botões do Mouse:**
  - **Botão Esquerdo:** 100% livre/normal para clicar nos botões do topo ou nos cards da arquitetura (Modo Foco / Speaking Mode).
  - **1 Clique com Botão Direito:** Liga a bolinha do laser pointer para apontar elementos na tela.
  - **Segurar Botão Direito e Arrastar:** Desenha EXCLUSIVAMENTE com o botão direito um **rastro de luz neon vermelho** que desvanece em ~1s.
  - **Soltar Botão Direito:** Para de desenhar rastro, mantendo o laser visível para apontar.
  - **Duplo Clique com Botão Direito:** Desliga o laser totalmente e devolve o cursor padrão da seta do mouse.
* **Ponteiro Laser no Ponto Exato do Cursor (Zero Cursor Jump):** O ponto laser é posicionado instantaneamente nas coordenadas exatas do mouse no momento em que é ativado, sem sobressaltos ou pulos de posição.
* **Zero Layout Shift:** O layout inicia alinhado fixo no topo com rótulo do botão de largura constante (`min-width: 72px`), garantindo 0px de deslocamento de interface ao alternar o laser.
* **Bloqueio de ContextMenu:** Previne o menu de contexto do navegador ao usar o botão direito.

### 🦘 2. Brilho Neon Estável no Hover (Zero Jitter / Zero Pulo)
* Ao passar o cursor do mouse sobre qualquer componente/card da arquitetura, o elemento expande suavemente no lugar (`scale(1.02)`) com iluminação de sombra neon (`filter: drop-shadow(...)`), usando coordenadas absolutas diretas no SVG (`x="..." y="..."`) sem `transform="translate"`. Isso garante **estabilidade total e zero trepidação ao passar o mouse**.

### 🎯 3. Modo Foco de Apresentador (Click Focus / Speaking Mode)
* **Primeiro Clique no Card:** O card salta em grande destaque para a frente (`translateY(-16px) scale(1.07)`), ganha um contorno neon verde e **esmaece suavemente todos os outros cards ao redor (opacidade para 35%)**, concentrando 100% da atenção da audiência no tópico em explicação.
* **Sem Seleção de Texto Azul:** Proteção com `user-select: none` para impedir que cliques rápidos ou arrastados selecionem textos com destaque azul indesejado durante a apresentação.
* **Segundo Clique (or clicar no fundo):** Restaura a visualização completa e traz todos os cards de volta à posição original.

### ▶️ 4. Animação de Fluxo em Tempo Real (Trace Motion & Partículas Coloridas)
* **Linhas Energizadas & Partículas Luminosas:** Partículas coloridas acompanhando a cor da conexão percorrem as linhas de fluxo (`<animateMotion>`) junto com traços tracejados animados.
* **Controle de Movimento:** Botão no topo para **Pausar / Rodar** a animação em tempo real utilizando as APIs nativas do SVG (`svgEl.pauseAnimations()` / `unpauseAnimations()`).

### 🎨 5. Ciclo de 6 Presets Visuais Corporativos & Alternador de Tema
* **Signal Flow:** Estilo cybertech escuro (`#030711`), bordas neon vibrantes (ciano, verde, violeta) e fonte moderna `Outfit`.
* **Blueprint:** Fundo de engenharia com grade técnica de 32px (`#06131f`), bordas ortogonais em tons azul/ciano técnico.
* **Editorial:** Fundo sépia/papel publicado (`#181611` / `#f2eee5`), tipografia serifada (`Georgia`) e destaques em laranja vermelhão.
* **Obsidian Gold:** Luxo C-Level em tons obsidian profundo (`#0b0d13`) com detalhes em Dourado Champagne & Âmbar (`#f59e0b`).
* **Nordic Frost:** Estilo Glassmorphism Enterprise (`#0f172a`), painéis foscos e destaques em Ciano Aurora & Violeta Boreal.
* **Midnight Tokyo:** Fundo OLED Pitch Black (`#000000`) com alto contraste neon vibrante (Verde Menta, Ciano e Magenta).
* **Tema Dark / Light:** Alternância instantânea de tema para todos os presets (6 presets × 2 temas = 12 combinações visuais).

### 🔄 6. Protocolo de Manutenção e Sincronização Contínua de Arquitetura
* **Pasta Padrão Fixa (`Architecture_Presentation/`):** Todos os diagramas gerados pelo Archify Presenter são criados obrigatoriamente dentro da pasta `Architecture_Presentation/` na raiz do projeto (ex: `Architecture_Presentation/<nome_do_diagrama>.html`), facilitando a localização e manutenção determinística.
* **Diagramas Vivos:** Todo diagrama HTML gerado pelo Archify Presenter é considerado documentação executiva viva.
* **Sincronização com o Código:** Sempre que o sistema sofrer alterações estruturais (novos endpoints, modelos de IA, tabelas de banco de dados ou escopo), o agente consulta proativamente a pasta `Architecture_Presentation/` e atualiza pontualmente os nós, fluxos e métricas para manter 100% de paridade técnica e visual.

---

## 🛠️ Como Usar a Skill

A skill pode ser acionada diretamente no chat de quatro maneiras:

### 1. Por Comando Direto
```text
/archify-presenter
```

### 2. Referenciando um Documento de Origem
```text
Crie um diagrama de apresentação interativo usando o /archify-presenter com base no arquivo @[plano_e_apresentacao_case_innova.md]
```

### 3. Por Pedido em Linguagem Natural
```text
Crie um infográfico de apresentação animado com ponteiro laser e foco de cards para a arquitetura da nossa plataforma de IA.
```

### 4. Por Atualizações de Sistema e Escopo (Sincronização Contínua)
```text
Sempre que você alterar o backend, banco de dados ou fluxo de um projeto, atualize os diagramas em Architecture_Presentation/.
```

---

## 📂 Estrutura de Arquivos da Skill

```text
.agents/skills/archify-presenter/
├── SKILL.md      # Instruções de execução e código-fonte base do motor Archify Presenter
└── README.md     # Documentação didática de uso e guia rápido dos recursos
```

---

## ⌨️ Guia Rápido de Controles para a Reunião

| Ação na Tela | Comando / Atalho do Mouse | Efeito Visual na Apresentação |
| :--- | :--- | :--- |
| **Ativar Laser** | **1 CLIQUE COM BOTÃO DIREITO** do mouse | Liga a bolinha do laser vermelho para apontar |
| **Riscar Rastro Neon** | **SEGURAR BOTÃO DIREITO** e arrastar | Desenha rastro neon vermelho que desvanece em 1s |
| **Desativar Laser** | **DUPLO CLIQUE COM BOTÃO DIREITO** | Desliga o laser e restaura a seta do mouse padrão |
| **Destacar card em fala** | **CLIQUE ESQUERDO** no card desejado | Card salta para frente + Esmaecimento dos demais |
| **Voltar ao normal** | **CLIQUE ESQUERDO** fora do card ou no mesmo card | Restaura todos os cards e opacidade |
| **Pausar movimento** | Clicar no botão `▶️ Animação` | Congela as partículas em movimento instantaneamente |
| **Trocar estilo** | Clicar no botão `🎨 Preset` | Comuta entre Signal Flow, Blueprint e Editorial |
