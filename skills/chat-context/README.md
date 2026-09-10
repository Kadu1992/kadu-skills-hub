# 🧠 Skill: `chat-context`

Persistência, gerenciamento em tempo real e consulta histórica de contextos de conversa para o Antigravity IDE e ecossistema de agentes.

---

## 📌 Visão Geral

A skill `chat-context` permite salvar, atualizar, retomar e consultar o contexto completo de trabalho em qualquer projeto. Com ela, a IA mantém o "fio da meada" entre sessões, garantindo que refatorações, decisões arquiteturais, pendências e histórico de comandos fiquem gravados no próprio repositório.

---

## ⚡ Ativação e Comandos

A skill é ativada por comandos explícitos no chat ou por gatilhos de intenção em linguagem natural:

| Comando / Gatilho | Ação Executada |
|---|---|
| `/chat-context` | Inicializa a estrutura ou resume a sessão ativa em `chat_context/current_context.md` |
| `iniciar contexto`, `retomar contexto`, `continuar contexto` | Lê o `current_context.md` e sintetiza onde o trabalho parou |
| `salvar contexto` | Força a atualização imediata do `current_context.md` (resumo de código + aprendizados) |
| `/chat-context historico <termo>` | Realiza busca direcionada via `grep_search` nos snapshots em `chat_context/history/` |
| `/chat-context history <termo>` | Variação em inglês do comando de busca histórica |

---

## 🗂️ Estrutura de Armazenamento

Ao ser ativada em um projeto, a skill cria e gerencia a seguinte estrutura na raiz do repositório:

```text
raiz_do_projeto/
└── chat_context/
    ├── current_context.md               # 📌 Contexto VIVO e ativo da sessão atual (mutável)
    ├── README.md                        # 📄 Guia e estrutura da pasta chat_context
    └── history/                          # 📂 Snapshots históricos imutáveis (padrão ISO 8601)
        └── YYYYMMDD_HHMMSS_Topico.md
```

---

## 🔄 Fluxos de Execução

```
                    ┌─────────────────────────┐
                    │  Comando / Gatilho      │
                    │ (/chat-context / texto) │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ É consulta ao histórico?│
                    └──────┬────────────┬─────┘
                           │            │
                  SIM      │            │  NÃO
       ┌───────────────────┘            └────────────────────┐
       ▼                                                     ▼
┌────────────────────────────────┐         ┌───────────────────────────────────┐
│ Executa grep_search em         │         │ `chat_context/` já existe?        │
│ `chat_context/history/`        │         └────────┬────────────────────┬─────┘
└──────────────┬─────────────────┘                  │                    │
               │                           NÃO      │                    │  SIM
               ▼                          ┌─────────┘                    └──────────┐
┌────────────────────────────────┐        ▼                                         ▼
│ Retorna síntese com links      │ ┌─────────────────────────────┐   ┌─────────────────────────────┐
│ clicáveis [Arquivo](file://...)│ │ 1. Cria chat_context/,      │   │ 1. Garante README.md e      │
└────────────────────────────────┘ │    README.md e history/     │   │    pasta history/           │
                                   │ 2. Mapeia projeto e gera    │   │ 2. Lê current_context.md    │
                                   │    current_context.md       │   │ 3. Sintetiza estado atual   │
                                   └─────────────────────────────┘   │ 4. Retoma a sessão          │
                                                                     └─────────────────────────────┘
```

---

## 📄 Formato do `current_context.md`

O arquivo `chat_context/current_context.md` é a **fonte de verdade** do contexto ativo da sessão:

```markdown
---
type: log
category: contexto
tags: [chat-context, resumo-sessao]
updated_at: YYYY-MM-DD HH:mm:ss
---

# 📌 Contexto Ativo da Sessão — [Nome do Projeto]

## 🎯 Objetivo Atual
[Resumo claro e objetivo da meta atual]

## 🛠️ Últimas Alterações Realizadas
- [x] Ajuste efetuado em [Arquivo](file:///caminho/do/arquivo)

## 💬 Estado da Última Troca de Mensagens
- **Último pedido do usuário**: "[Solicitação mais recente]"
- **Status da IA**: "[Resumo da resposta / status da entrega]"

## 🧠 Decisões Arquiteturais & Regras Estabelecidas
- Regras ou escolhas de design acordadas durante a sessão

## ⏳ Próximos Passos & Pendências
- [ ] Tarefa pendente 1
- [ ] Tarefa pendente 2

## 📂 Arquivos Afetados Recentes
- [Nome do Arquivo](file:///caminho/do/arquivo)
```

---

## 📜 Snapshots Históricos (`history/`)

A IA gera **obrigatoriamente** um arquivo snapshot em `chat_context/history/YYYYMMDD_HHMMSS_Topico.md` sempre que:
- Concluir um tópico importante, bloco de tarefas ou refatoração significativa
- Houver uma decisão arquitetural relevante
- O usuário solicitar explicitamente ("salvar contexto", "snapshot", "guardar histórico")

- **Nomenclatura Padrão**: `YYYYMMDD_HHMMSS_Topico.md` (Ex: `20260723_113858_Decisao_IsHidden_BD.md`).
- **ISO 8601**: Garante ordenação cronológica exata no Explorer, IDE e gerenciadores de arquivos.
- **Eficiência de Tokens**: Na busca histórica (`/chat-context historico <termo>`), os arquivos não são lidos todos de uma vez; apenas o termo buscado via `grep_search` é consultado.

### 🔍 Como Funciona a Busca Otimizada por Ripgrep (grep_search)
A busca no histórico antigo (`/chat-context historico <termo>`) utiliza a ferramenta `grep_search` (baseada no utilitário nativo *ripgrep*) para garantir máxima velocidade e economia de tokens:

- **Mecanismo Físico ("Ctrl + F" Local)**: A busca NÃO carrega o conteúdo integral dos arquivos para a memória de contexto da IA. A consulta é executada via CPU/disco diretamente no computador local.
- **Varredura Integral em Disco**: O *ripgrep* pesquisa no texto completo de todos os arquivos `.md` em `chat_context/history/` (títulos, cabeçalhos, corpo de texto, trechos de código, decisões arquiteturais e variáveis).
- **Consumo Mínimo de Tokens**: O sistema devolve à IA apenas as poucas linhas exatas onde o termo foi encontrado. A IA lê unicamente esses recortes, reduzindo o uso de tokens de dezenas de milhares para praticamente zero (~100 a 500 tokens).

#### 📊 Comparativo: Leitura Integral vs Busca Otimizada (Ripgrep)

| Característica | Leitura Integral (Sem Ripgrep) | Busca Otimizada via `grep_search` |
|---|---|---|
| **Processamento** | Lê todos os arquivos para o prompt da IA | Varredura nativa no disco local via CPU |
| **Consumo de Tokens** | 50.000 a 200.000+ tokens por busca | ~100 a 500 tokens (apenas recortes) |
| **Velocidade** | Lenta (depende do envio pesado de API) | Instantânea (milissegundos no processador) |
| **Escalabilidade** | Estoura o limite de contexto | Suporta milhares de arquivos sem impacto |

#### 📚 Analogia do Bibliotecário
Em vez de ler centenas de livros inteiros de uma biblioteca para achar uma frase, a IA pede ao bibliotecário (*ripgrep*): *"Folheie a estante e me traga apenas um papelzinho com a página e a linha marcada"*. A IA lê unicamente o papel anotado entregue pelo bibliotecário.

---

## 📌 Regras de Integridade

1. **Eficiência de Tokens**: Nunca carregar todos os snapshots do histórico simultaneamente na janela de contexto.
2. **Links Universais**: Todos os links para arquivos gerados devem usar o formato de link Markdown universal clicável `[Nome](file:///caminho/completo)`.
3. **Idempotência**: A inicialização verifica previamente a existência da pasta e do arquivo para nunca sobrescrever dados sem necessidade.
4. **Conversas Conceituais e Aprendizados**: O salvamento de contexto NÃO depende de alteração em arquivos ou código. Discussões sobre dúvidas, aprendizados e decisões conceituais são sintetizadas automaticamente nas seções `💬 Estado da Última Troca`, `🧠 Decisões Arquiteturais` e `⏳ Próximos Passos` do `current_context.md`.
