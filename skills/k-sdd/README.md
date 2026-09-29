# k-sdd (Kadu Spec-Driven Development)

> **Framework de Engenharia Agêntica de Alta Precisão para Desenvolvimento com IA.**  
> Combina o rigor estrutural do **Tech Lead's Club** (Felipe Rodrigues), a metodologia **P-E-R-A / PRD** (Rafael Quintanilha), a especificação visual **DESIGN.md** (Google Stitch) e o protocolo exclusivo **UAT Feedback Loop** com commits coesos por fase e rastreabilidade estrita.

---

## 🎯 Por que o `k-sdd`?

O desenvolvimento orientado por agentes de IA falha quando cai na armadilha do "vibe coding": prompts soltos, falta de especificações claras, testes rasos e correções improvisadas que acumulam dezenas de arquivos no painel de *Changes* sem commits atômicos.

O **`k-sdd`** resolve isso instituindo uma **trilha de ferro sequencial e inegociável**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 O CICLO P-E-R-A DO k-sdd                               │
├───────────────┬───────────────────────────┬───────────────────────┬────────────────────┤
│ P - PREPARAR  │ E - EXECUTAR              │ R - REVISAR (UAT)     │ A - ACELERAR       │
├───────────────┼───────────────────────────┼───────────────────────┼────────────────────┤
│ 1. PRD (Sis)  │ 4. Tasks (Fases e Gates)  │ 6. Verifier (Auto)    │ 8. Sincronia / Git │
│ 2. FRD (Feat) │ 5. Código + Commits Fase  │ 7. UAT Feedback (-[x])│    Deploy / Loop   │
│ 3. Spec (EARS)│                           │    Re-verification    │                    │
└───────────────┴───────────────────────────┴───────────────────────┴────────────────────┘
```

---

## 🏗️ Arquitetura de Artefatos no Projeto

```
meu-projeto/
├── AGENTS.md                   # Diretrizes da IA (gerado/atualizado pelo k-sdd com idempotência tripla)
├── DESIGN.md                   # Design System no padrão Stitch (YAML tokens + regras de UI)
└── .specs/
    ├── PRD.md                  # PRD do Sistema (visão macro do produto + mapa de módulos)
    ├── STATE.md                # Memória viva (decisões AD-NNN e snapshot de handoff)
    ├── LESSONS.md / json       # Lições aprendidas retroalimentadas após testes
    └── features/
        └── [feature]/
            ├── frd.md          # Feature Requirements Document (os 4 pilares essenciais)
            ├── spec.md         # Requisitos técnicos em formato EARS + Requirement Traceability
            ├── design.md       # Arquitetura e componentes técnicos (se complexo)
            ├── tasks.md        # Decomposição em Fases e Tasks atômicas com Gates
            ├── validation.md   # Relatório do Verifier independente (evidências file:line)
            └── feedback.md     # Checklist rastreável de UAT (- [ ] FB-01) com commits
```

---

## 🚀 Instalação Rápida

Para adicionar o `k-sdd` a qualquer projeto (Next.js, React, Node, Python, etc.):

```bash
npx skills add https://github.com/Kadu1992/k-sdd --skill k-sdd
```

---

## 💬 Comandos e Ativação

A skill pode ser utilizada de forma **100% fluida em linguagem natural** (a IA identifica o momento da conversa) ou por meio dos atalhos diretos:

* `/k-sdd new-project <descrição>` ➔ Inicia um projeto do zero, gerando o `PRD.md` do sistema e o `DESIGN.md` inicial.
* `/k-sdd init-feature <nome>` ➔ Inicia uma nova funcionalidade, gerando o `frd.md` (Problema, Solução, Constraints e Critérios de Aceite).
* `/k-sdd` ➔ Gera a especificação técnica formal (`spec.md`) e quebra em fases de tarefas com gates (`tasks.md`).
* `/k-sdd uat` ➔ Abre o checklist no `feedback.md`, processa seu feedback de homologação (áudio ou texto) e cria a fase de correção com commits coesos.

---

## 🛡️ Validações Determinísticas em Python (`scripts/`)

A IA é fiscalizada por código em cada etapa da jornada:

* `validate_spec.py`: Garante que a spec tenha requisitos testáveis no padrão EARS (`SHALL`) e valida a presença do `frd.md`.
* `validate_tasks.py`: Garante tarefas granulares com campos obrigatórios (`What`, `Where`, `Depends on`, `Done when`, `Gate`).
* `validate_state.py`: O guardião do fechamento! Exige veredito PASS com evidências `file:line` e **bloqueia o encerramento se houver qualquer item pendente no `feedback.md`**.
* `check_commit.py`: Valida mensagens de commit semântico (Conventional Commits).
* `lessons.py`: Registra e carrega lições aprendidas para evitar repetição de erros.
* `sync_upstream.py`: Sincroniza novidades do repositório oficial do Tech Lead's Club sem trazer monorepo.
* `migrate_tlc.py`: Migra projetos legados do `tlc-spec-driven` para o `k-sdd` em 1 segundo.

---

## 🔄 Migração de Projetos TLC Existentes

Se você já possui um projeto usando `tlc-spec-driven`, migre instantaneamente:

```bash
python .agents/skills/k-sdd/scripts/migrate_tlc.py
```

O script adapta suas features, gera os FRDs retroativos, atualiza o `AGENTS.md` e remove a dependência legada preservando todo o histórico.

---

## 👏 Créditos e Upstream

- **Base Original:** Criado a partir do `tlc-spec-driven` v3.3.0 de **Felipe Rodrigues** ([Tech Lead's Club](https://github.com/tech-leads-club/agent-skills)).
- **Conceitos de Produto:** Inspirado no método **P-E-R-A** e especificações de PRD de **Rafael Quintanilha** ([QuantBrasil](https://youtube.com/@quantbrasil)).
- **Padrão de Design System:** Especificação `DESIGN.md` concebida pela equipe do **Google Stitch**.
- **Desenvolvido e Mantido por:** **Kadu Amstetter** ([Kadu1992](https://github.com/Kadu1992)).
