# Guia: PRD (Sistema) & FRD (Feature)

> **Objetivo:** Estabelecer o contrato de negócio e a intenção de produto antes de qualquer linha de código ou especificação técnica, eliminando "vibe coding" e planos temporários soltos na raiz.

---

## 1. A Diferença Fundamental: PRD vs. FRD

| Dimensão | PRD (Product Requirements Document) | FRD (Feature Requirements Document) |
| :--- | :--- | :--- |
| **Escopo** | O **Sistema Inteiro** (Produto macro) | A **Funcionalidade Específica** |
| **Quando é Criado** | No nascimento de um novo projeto do zero | A cada nova feature planejada ou solicitada |
| **Localização** | `.specs/PRD.md` | `.specs/features/[feature]/frd.md` |
| **Foco** | Visão do produto, mercado, personas, roadmap de módulos | Os 4 pilares: Problema, Solução, Constraints e Critérios |
| **Acompanhamento** | Checkboxes gerais de módulos entregues | Checkboxes de critérios de aceite de alto nível |

---

## 2. Template Oficial: PRD do Sistema (`.specs/PRD.md`)

```markdown
# [Nome do Produto / Sistema] - PRD

> **Versão:** 1.0.0  
> **Status:** Aprovado  
> **Data:** YYYY-MM-DD  

---

## 1. Visão Geral do Produto
[Descreva em 2 a 3 parágrafos a proposta de valor do software. Qual problema real de mercado ele resolve? Quem é o público-alvo?]

## 2. Personas & Dores Principais
- **Persona 1 ([Cargo/Perfil]):** [Dor principal e como o produto soluciona].
- **Persona 2 ([Cargo/Perfil]):** [Dor principal e como o produto soluciona].

## 3. Arquitetura Conceitual & Stack Inegociável
- **Frontend:** [Ex: Next.js 15, React 19, Tailwind CSS]
- **Backend / Banco:** [Ex: Supabase, PostgreSQL, Edge Functions]
- **Design System:** Documentado na raiz em `DESIGN.md`

## 4. Mapa de Módulos e Roadmap de Features
- [ ] **Módulo 1 - [Nome]:** [Breve descrição da capacidade].
- [ ] **Módulo 2 - [Nome]:** [Breve descrição da capacidade].
- [ ] **Módulo 3 - [Nome]:** [Breve descrição da capacidade].

---
*A cada módulo implementado e validado, este checklist é atualizado.*
```

---

## 3. Template Oficial: FRD da Feature (`.specs/features/[feature]/frd.md`)

Baseado no Método **P-E-R-A** (Preparação) ensinado por Rafael Quintanilha, o FRD é enxuto, direto e amigável ao humano (*human-friendly*):

```markdown
# FRD: [Nome da Funcionalidade]

> **Feature:** `[feature_slug]`  
> **Status:** Pronto para Especificação Técnica  
> **Data:** YYYY-MM-DD  

---

## 1. Problema & Contexto
[Descreva a dor específica do usuário que esta feature resolve. Por que estamos fazendo isso agora? Exemplo: "Os usuários mobile estão com dificuldade de visualizar os cards no Kanban devido à sobreposição de botões."]

## 2. Solução & Capacidades (User Stories)
Descreva as capacidades que o usuário terá no formato canônico:
- **US-01:** Como [perfil], quero [capacidade] para que [benefício].
- **US-02:** Como [perfil], quero [capacidade] para que [benefício].

## 3. Constraints (Restrições Inegociáveis)
O que é top-down e **não pode ser alterado pela IA** (delimita a liberdade criativa):
- [Ex: Usar exclusivamente a biblioteca @dnd-kit]
- [Ex: Não criar migrations destrutivas no banco]
- [Ex: Seguir rigorosamente a paleta de cores e raios do DESIGN.md]

## 4. Critérios de Aceite de Alto Nível
Checklist das condições que precisam ser verdade para o aceite do produto:
- [ ] [Critério 1: Condição observável de sucesso]
- [ ] [Critério 2: Condição observável de sucesso]
- [ ] [Critério 3: Tratamento de exceção ou erro]

---
*Após a aprovação deste FRD pelo usuário, a IA gera a spec.md técnica e o tasks.md.*
```

---

## 4. Regras de Ouro
1. **Nada de AI Slop:** Nunca gere um PRD ou FRD com 10 páginas de enrolação que ninguém vai ler. Seja direto, visual e objetivo.
2. **Aprovação Obrigatória:** O agente não pode criar tarefas técnicas nem escrever código antes do usuário ler e aprovar o FRD.
3. **Derivação Determinística:** O `spec.md` traduz os critérios do FRD para a sintaxe matemática EARS (`SHALL`).
