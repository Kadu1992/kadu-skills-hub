#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Inicialização Automática da Skill questions-and-learning.
Cria deterministicamente a estrutura necessária na raiz do projeto:
- pasta chat_questions/
- arquivo chat_questions/README.md
- arquivo chat_questions/questions.md (com template inicial amigável e orientações de uso)
"""

import sys
from pathlib import Path

# ==============================================================================
# Ajuste de codificação UTF-8 para terminais Windows (cp1252)
# O que esta parte faz: Reconfigura a saída padrão para UTF-8 de forma segura.
# Para que serve / Como funciona no fluxo: Evita erros de UnicodeEncodeError ao
# imprimir emojis e caracteres especiais no PowerShell ou Prompt de Comando do Windows.
# ==============================================================================
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# ==============================================================================
# Função para encontrar a raiz do projeto atual
# O que esta parte faz: Percorre os diretórios pai a partir do local de execução
# procurando marcadores comuns de raiz de projeto (.git, package.json, etc.).
# Para que serve / Como funciona no fluxo: Garante que a pasta chat_questions/ seja
# sempre criada na raiz do repositório/projeto ativo, e não dentro de subpastas da skill.
# ==============================================================================
def obter_raiz_projeto() -> Path:
    cwd = Path.cwd().resolve()
    candidato = cwd

    # Percorre os diretórios para cima procurando indicadores de raiz
    for pai in [candidato] + list(candidato.parents):
        if (pai / ".git").exists() or (pai / "package.json").exists() or (pai / ".agents").exists():
            return pai

    return cwd


# ==============================================================================
# Template padrão do arquivo README.md da pasta chat_questions
# O que esta parte faz: Define a documentação didática embutida da pasta.
# Para que serve / Como funciona no fluxo: Orienta qualquer desenvolvedor ou agente
# sobre a finalidade dos arquivos gerados, comandos de terminal e uso no chat.
# ==============================================================================
README_CONTEUDO = """# ❓ Pasta de Dúvidas e Aprendizados (`chat_questions`)

Esta pasta centraliza o fluxo de captura de dúvidas brutas e sua conversão inteligente em documentos estruturados de suporte técnico, decisões e plano de ação imediato.

---

## 🗂️ Estrutura da Pasta

```text
chat_questions/
├── questions.md             # 📝 Arquivo de entrada: escreva aqui suas dúvidas brutas
├── README.md                # 📄 Guia explicativo da pasta
├── duvidas-v1.md            # 📋 Versão 1: dúvidas organizadas por temas com emojis
├── resposta-v1.md           # ✅ Versão 1: respostas técnicas + resumo de ações
└── ...                      # Versões subsequentes (v2, v3, etc.)
```

---

## 🚀 Como Usar no Dia a Dia

1. **Escreva suas dúvidas**: Abra o arquivo `questions.md` e anote tudo o que precisa ser esclarecido ou decidido (dúvidas de tela, regras de negócio, bugs, lógica, etc.).
2. **Execute a skill**: No chat da IDE/assistente, você tem duas opções equivalentes:
   - **Opção A (Comando)**: Digite `/questions-and-learning` (ou `/questions`) e envie.
   - **Opção B (Arrastar e Soltar)**: Simplesmente arraste o arquivo `questions.md` para o chat da IA e dê Enter (sem precisar digitar nada!).
3. **Consulte o resultado**:
   - `duvidas-vN.md`: Suas anotações 100% preservadas e organizadas por temas com emojis.
   - `resposta-vN.md`: Respostas técnicas ponto a ponto com tabela de ações imediatas por prioridade.

---

## 🛠️ Como Inicializar ou Gerar a Estrutura (Setup)

Caso a estrutura ainda não exista ou você esteja iniciando em um novo projeto, use uma destas opções:

### Opção 1: Pelo Chat da IA (Sem Terminal — Recomendada)
Basta digitar `/questions-and-learning` ou `/questions init` no chat. A IA criará instantaneamente a pasta `chat_questions/`, o `README.md` e o `questions.md` pré-formatado na árvore da IDE.

### Opção 2: Pelo Terminal (Script Python Determinístico)
Execute o comando abaixo na raiz do seu projeto:

```bash
python .agents/skills/questions-and-learning/scripts/init.py
```

*(Comando idempotente: gera os arquivos com template estruturado e nunca sobrescreve anotações já existentes).*
"""


# ==============================================================================
# Template padrão do arquivo questions.md
# O que esta parte faz: Define o modelo estruturado inicial de anotações.
# Para que serve / Como funciona no fluxo: Evita arquivos em branco e orienta o usuário
# com categorias sugeridas onde ele pode listar dúvidas e como acionar a IA (comando ou arrastar).
# ==============================================================================
QUESTIONS_TEMPLATE = """# ❓ Dúvidas e Anotações Brutas

> Escreva abaixo suas dúvidas, ideias, comportamentos inesperados ou decisões pendentes.
> 
> Quando terminar de escrever, você tem duas opções equivalentes para acionar a IA:
> 1. **Via comando**: Digite `/questions-and-learning` (ou `/questions`) no chat e dê Enter.
> 2. **Via arrastar e soltar**: Arraste este arquivo `questions.md` para o chat da IA e dê Enter (sem precisar digitar texto nenhum!).
> 
> Ambas as formas acionam a skill e geram o documento estruturado (`duvidas-vN.md`) e as respostas técnicas (`resposta-vN.md`).

---

## 1. Dúvidas Gerais & Funcionalidades
- [ ] 

## 2. Interface, Layout & Telas
- [ ] 

## 3. Lógica, Regras de Negócio & Dados
- [ ] 
"""


# ==============================================================================
# Função principal de inicialização da estrutura
# O que esta parte faz: Cria a pasta chat_questions e os arquivos README.md e questions.md.
# Para que serve / Como funciona no fluxo: Executa o setup de forma idempotente,
# sem sobrescrever o questions.md se o usuário já tiver inserido conteúdo nele.
# ==============================================================================
def inicializar_estrutura(raiz: Path = None) -> bool:
    if raiz is None:
        raiz = obter_raiz_projeto()

    pasta_chat_questions = raiz / "chat_questions"
    pasta_chat_questions.mkdir(parents=True, exist_ok=True)

    arquivo_readme = pasta_chat_questions / "README.md"
    arquivo_questions = pasta_chat_questions / "questions.md"

    # Cria ou atualiza o README.md explicativo com o comando de terminal embutido
    arquivo_readme.write_text(README_CONTEUDO, encoding="utf-8")

    # Cria o questions.md apenas se ele ainda não existir ou se estiver vazio
    criou_questions = False
    if not arquivo_questions.exists() or arquivo_questions.stat().st_size == 0:
        arquivo_questions.write_text(QUESTIONS_TEMPLATE, encoding="utf-8")
        criou_questions = True

    print("==================================================================")
    print("✨ Skill questions-and-learning: Estrutura inicial criada com sucesso!")
    print(f"📁 Pasta: {pasta_chat_questions}")
    print(f"📄 Guia: {arquivo_readme}")
    if criou_questions:
        print(f"📝 Anotações: {arquivo_questions} (template inicial inserido)")
    else:
        print(f"📝 Anotações: {arquivo_questions} (conteúdo existente preservado)")
    print("==================================================================")
    print("💡 Próximo passo: Escreva suas dúvidas no questions.md e chame /questions-and-learning ou arraste o arquivo para o chat!")
    return True


if __name__ == "__main__":
    inicializar_estrutura()
