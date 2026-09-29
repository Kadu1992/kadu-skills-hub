# Guia: DESIGN.md (Padrão Google Stitch)

> **Objetivo:** Estabelecer a especificação visual e o design system do projeto em Markdown/YAML nativo, diretamente legível por agentes de IA, **sem qualquer dependência de servidores MCP externos**.

---

## 1. O que é o `DESIGN.md` no `k-sdd`?

O `DESIGN.md` é a contraparte visual do `AGENTS.md`:
* Enquanto o `AGENTS.md` ensina como a IA deve **codificar** e rodar testes;
* O `DESIGN.md` ensina como a interface deve **parecer, reagir e se comportar**.

Ele reside na raiz do repositório (`/DESIGN.md`) e é versionado no Git junto com o código.

---

## 2. Template Oficial: `DESIGN.md` na Raiz do Projeto

```markdown
# Design System Specification (DESIGN.md)

> Este arquivo define os design tokens e regras de interface do projeto.  
> Qualquer agente de IA que desenvolva ou altere componentes de UI DEVE seguir estritamente estas definições.

```yaml
design_system:
  name: "Default Theme"
  version: "1.0.0"
  mode: "dark" # dark | light | adaptive

  colors:
    background: "#0F1117"        # Fundo principal profundo (nunca use preto puro #000)
    surface: "#161822"           # Superfície elevada de cards e modais
    surface_hover: "#1D202F"     # Estado hover de cards
    border: "rgba(255, 255, 255, 0.08)" # Bordas sutis com transparência
    border_focus: "#10B981"      # Anel de foco acessível (esmeralda suave)
    text_primary: "#F8FAFC"      # Texto principal de alto contraste
    text_secondary: "#94A3B8"    # Texto de apoio e descrições
    accent_primary: "#10B981"    # Cor de ação principal (ex: Verde Esmeralda)
    accent_hover: "#059669"      # Hover da ação principal
    destructive: "#EF4444"       # Mensagens de erro e ações destrutivas

  typography:
    font_family_sans: "'Inter', system-ui, -apple-system, sans-serif"
    font_family_mono: "'JetBrains Mono', monospace"
    scale:
      h1: "2.25rem" # 36px - Peso: 700
      h2: "1.75rem" # 28px - Peso: 600
      h3: "1.25rem" # 20px - Peso: 600
      body: "0.95rem" # 15px - Peso: 400
      caption: "0.8rem" # 13px - Peso: 500

  geometry:
    radius_sm: "6px"   # Badges e inputs pequenos
    radius_md: "10px"  # Botões e selects
    radius_lg: "16px"  # Cards e painéis
    radius_full: "9999px" # Pílulas e avatares

  motion:
    transition_fast: "150ms ease"
    transition_normal: "250ms cubic-bezier(0.16, 1, 0.3, 1)"
    tactile_scale: "scale(0.97)" # Feedback tátil ao clique (:active)
```

---

## 3. Diretrizes de Interface (UI Rules & Anti-Slop)

1. **Evite Cores Genéricas:** Nunca use azul ou vermelho padrão de navegador. Utilize paletas curadas HSL ou Hex sofisticadas.
2. **Superfícies Táteis (Física Emil Kowalski):**
   - Todo botão clicável deve conter feedback tátil:
     ```css
     button:active { transform: scale(0.97); }
     ```
3. **Sem Bordas Agressivas em Dark Mode:** Use bordas translúcidas (`rgba(255, 255, 255, 0.08)` ou `0.10`) para criar profundidade elegante com desfoque de vidro (*glassmorphism*).
4. **Alinhamento e Responsividade Mobile:** Elementos como pílulas de seleção, botões de ação e campos devem manter espaçamento fluido e legibilidade sem quebra de texto feia no celular.

---

## 4. Ciclo de Vida do `DESIGN.md`
* **Nascimento:** Gerado na raiz ao rodar `/k-sdd new-project`.
* **Consumo:** A IA consulta o `DESIGN.md` durante a criação de componentes e telas em `tasks.md`.
* **Atualização Contínua:** Se durante o desenvolvimento o usuário pedir para alterar a paleta de cores ou estilo visual, a IA **atualiza o `DESIGN.md` ao mesmo tempo**, garantindo que o design system nunca fique desatualizado.
