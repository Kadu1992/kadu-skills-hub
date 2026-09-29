---
name: k-sdd
description: Metodologia Spec-Driven Development (P-E-R-A) para engenharia de software agêntica de alta precisão. Cobre desde o nascimento do produto (PRD em .specs/PRD.md) ou da funcionalidade (FRD com os 4 pilares em .specs/features/[feature]/frd.md), DESIGN.md nativo estilo Google Stitch sem MCP, especificação técnica EARS, decomposição em Fases e Tasks atômicas com gates, Verifier independente com Discrimination Sensor (teste de mutação), UAT Feedback Loop com checklist rastreável (- [ ] FB-01) e commits coesos por fase, governança automática com AGENTS.md (idempotência tripla), guardião contra pular etapas (Step Gatekeeper) e sincronização upstream via sync_upstream.py. Triggers on "/k-sdd", "k-sdd", "novo projeto k-sdd", "nova feature k-sdd", "iniciar projeto sdd", "especificar feature", "discuss feature", "tasks", "implement", "validate", "verify work", "UAT", "feedback uat", "homologação", "record decision", "pause work", "resume work".
license: CC-BY-4.0
metadata:
  author: Kadu Amstetter - github.com/Kadu1992
  base_authors: Felipe Rodrigues (Tech Lead's Club) & Rafael Quintanilha (QuantBrasil)
  version: 1.0.0
---

# k-sdd (Kadu Spec-Driven Development)

Planeje, especifique, implemente, valide e homologue com precisão cirúrgica. Menos ceremony, zero vibe coding, máxima confiança.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 O CICLO P-E-R-A DO k-sdd                               │
├───────────────┬───────────────────────────┬───────────────────────┬────────────────────┤
│ P - PREPARAR  │ E - EXECUTAR              │ R - REVISAR (UAT)     │ A - ACELERAR       │
├───────────────┼───────────────────────────┼───────────────────────┼────────────────────┤
│ 1. PRD (Sis)  │ 4. Tasks (Fases e Gates)  │ 6. Verifier (Auto)    │ 8. Sincronia Git   │
│ 2. FRD (Feat) │ 5. Código + Commits Fase  │ 7. UAT Feedback (-[x])│    Deploy / Loop   │
│ 3. Spec (EARS)│                           │    Re-verification    │                    │
└───────────────┴───────────────────────────┴───────────────────────┴────────────────────┘
```

---

## Regras Críticas Inegociáveis (Leia antes de agir)

### 1. Governança Automática via `AGENTS.md` (Idempotência Tripla)
Ao rodar a skill pela primeira vez em qualquer projeto:
1. **Se NÃO existe `AGENTS.md`:** A skill cria o arquivo na raiz estabelecendo o `k-sdd` como padrão de engenharia.
2. **Se JÁ existe `AGENTS.md` mas NÃO contém as regras do `k-sdd`:** A skill preserva 100% das regras originais e **apenas anexa** a diretriz do `k-sdd` ao final.
3. **Se JÁ existe `AGENTS.md` e JÁ contém as regras do `k-sdd`:** **IGNORA COMPLETAMENTE** (mantém o arquivo intacto, sem duplicar nada).

### 2. O Guardião Inegociável contra Pular Etapas (Step Gatekeeper)
A metodologia possui uma trilha de ferro sequencial. **É expressamente proibido pular etapas**:
`PRD (novo projeto) ➔ FRD (feature) ➔ SPEC (técnica) ➔ TASKS (fases) ➔ EXECUTE (gates) ➔ VERIFIER (auto) ➔ UAT FEEDBACK (humano)`
- Se o usuário ou agente tentar gerar código ou tasks sem que o `frd.md` e a `spec.md` estejam criados e com gate aprovado:
  ➔ **A IA BLOQUEIA:** *"⛔ Etapa Bloqueada: Não é permitido pular etapas no k-sdd. Para gerar tarefas e codificar, precisamos primeiro aprovar o FRD (`frd.md`) e a Especificação (`spec.md`)."*
- Se tentar abrir o UAT Humano antes que todas as tasks da fase estejam concluídas e o Verifier automatizado tenha passado com `PASS`:
  ➔ **A IA BLOQUEIA:** *"⛔ Etapa Bloqueada: A homologação de UAT só pode ser aberta após a conclusão das tasks e verificação dos testes automáticos."*
- Se tentar declarar a feature concluída com itens pendentes no `feedback.md`:
  ➔ **O script `validate_state.py` BLOQUEIA no terminal com erro 1!**

### 3. Higiene de Contexto de IA (Diretriz Oficial de Chats)
- **Nova Feature = Novo Chat (Recomendado):** Ao concluir uma feature (com UAT e validação PASS) e for iniciar outra, oriente abrir um novo chat. O histórico do projeto está gravado em `.specs/STATE.md` e no Git, garantindo foco máximo, sem poluição de memória (*attention dilution*) e velocidade total.
- **Durante a Mesma Feature + UAT Feedback = Mesmo Chat:** Durante a implementação das fases e nas rodadas de homologação humana (UAT / Feedback), mantenha o mesmo chat. A IA retém na memória recente o raciocínio dos arquivos recém-tocados, tornando os ajustes instantâneos.

### 4. Execução por Fases e Commits Coesos
- As tarefas são organizadas em **Fases sequenciais** em `tasks.md`.
- Cada task individual tem seu comando de Gate (`npm run build` / testes) testado antes de avançar para a próxima.
- Ao concluir **todas as tasks de uma Fase** (ou rodada de UAT), a IA gera **um commit semântico coeso e robusto da Fase inteira**, eliminando dezenas de micro-commits fragmentados e evitando acúmulo desordenado no painel de *Changes*.

### 5. Carregamento de Arquivos e Scripts da Skill
- Arquivos de referência moram sob `references/` na pasta da própria skill.
- Scripts executáveis moram sob `scripts/` na pasta da própria skill. Execute via:
  `python3 <skill-dir>/scripts/<nome>.py ...` passando `--root` se necessário.
- Dados do projeto moram em `.specs/` e na raiz do projeto alvo (`/DESIGN.md`, `/AGENTS.md`).

---

## Estrutura de Artefatos no Projeto

```
projeto/
├── AGENTS.md                   # Instruções de engenharia para agentes (idempotência tripla)
├── DESIGN.md                   # Design System no padrão Stitch (YAML tokens + UI rules)
└── .specs/
    ├── PRD.md                  # PRD do Sistema inteiro (visão macro + módulos com checks)
    ├── STATE.md                # Decisões arquiteturais (AD-NNN) e snapshot de handoff
    ├── LESSONS.md / json       # Lições aprendidas retroalimentadas pelo Verifier
    └── features/
        └── [feature]/
            ├── frd.md          # Feature Requirements Document (os 4 pilares de Quintanilha)
            ├── spec.md         # Requisitos técnicos EARS + Requirement Traceability
            ├── design.md       # Arquitetura e componentes da feature (se complexo)
            ├── tasks.md        # Fases sequenciais e Tasks com Gates
            ├── validation.md   # Relatório do Verifier (testes automáticos + evidências)
            └── feedback.md     # Checklist rastreável de UAT (- [ ] FB-01) com commits
```

---

## Comandos e Gatilhos (Fluidez Total)

Você pode apenas conversar naturalmente em linguagem natural ou utilizar os atalhos:

| Comando / Gatilho | O que faz | Referência |
| :--- | :--- | :--- |
| `/k-sdd new-project <desc>` | Inicia um sistema do zero gerando o `PRD.md` e o `DESIGN.md`. | [prd-frd.md](references/prd-frd.md) / [stitch-design.md](references/stitch-design.md) |
| `/k-sdd init-feature <nome>` | Inicia uma feature criando o `frd.md` (Problema, Solução, Constraints, Critérios). | [prd-frd.md](references/prd-frd.md) |
| `/k-sdd` | Deriva a especificação técnica (`spec.md`) e quebra em fases de tarefas com gates (`tasks.md`). | [specify.md](references/specify.md) / [tasks.md](references/tasks.md) |
| `/k-sdd uat` | Abre a homologação no `feedback.md`, processa áudio/texto e cria a fase de correção. | [uat-feedback.md](references/uat-feedback.md) |
| `Resume work / Continuar` | Lê `STATE.md` (Handoff) e reconcilia com Git para propor o próximo passo. | [memory.md](references/memory.md) |

---

## Validadores Determinísticos em Python (`scripts/`)

- `python3 <skill-dir>/scripts/validate_spec.py <feature>`: Valida se a `spec.md` tem requisitos EARS (`SHALL`) e valida a presença/estrutura dos 4 pilares do `frd.md`.
- `python3 <skill-dir>/scripts/validate_tasks.py <feature>`: Valida se as tasks possuem `What`, `Where`, `Depends on`, `Done when` e `Gate`.
- `python3 <skill-dir>/scripts/validate_state.py <feature>`: Portão de encerramento! Exige `validation.md` com PASS, citações `file:line` e **garante que todos os checkboxes do `feedback.md` estão marcados como `[x]`**.
- `python3 <skill-dir>/scripts/check_commit.py --message "<msg>"`: Valida se o commit segue Conventional Commits.
- `python3 <skill-dir>/scripts/sync_upstream.py --check`: Sincroniza melhorias do Tech Lead's Club sem trazer monorepo.
- `python3 <skill-dir>/scripts/migrate_tlc.py`: Migra projetos legados do `tlc-spec-driven` para o `k-sdd`.

---

## Verifier e Discrimination Sensor (Alarme de Incêndio)

Após a última task da fase, o **Verifier independente** (`author != verifier`) roda automaticamente:
1. Executa os testes automatizados normais;
2. **Injeta um bug temporário em scratch isolado** (inverte condição lógica ou valor de retorno);
3. Executa os testes novamente e confirma que o mutante foi MORTO (`Killed ✅`). Se o teste continuar passando com código quebrado, flag como falso-positivo e cria task de ajuste;
4. Restaura o código limpo e escreve o relatório `.specs/features/[feature]/validation.md`.
