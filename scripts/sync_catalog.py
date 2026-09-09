#!/usr/bin/env python3
"""
Script de sincronização automática do catálogo de skills.
Lê o arquivo skills.json na raiz do repositório e atualiza a pasta
de cada skill a partir do seu respectivo repositório no GitHub.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


# ==============================================================================
# Função para carregar a lista de skills cadastradas
# O que esta parte faz: Lê e interpreta o arquivo skills.json na raiz do projeto.
# Para que serve / Como funciona no fluxo: Identifica quais skills fazem parte
# da vitrine (hub), qual repositório do GitHub elas pertencem e qual branch usar.
# ==============================================================================
def carregar_catalogo(caminho_json: Path) -> list[dict]:
    if not caminho_json.exists():
        print(f"Erro: Arquivo de catalogo nao encontrado em {caminho_json}")
        sys.exit(1)

    with open(caminho_json, "r", encoding="utf-8") as f:
        return json.load(f)


# ==============================================================================
# Função para sincronizar uma skill individual
# O que esta parte faz: Clona o repositório da skill em uma pasta temporária e
# copia os arquivos atualizados para dentro da pasta 'skills/<id>' no Hub.
# Para que serve / Como funciona no fluxo: Garante que a vitrine receba a versão
# mais recente do código da skill sem trazer a pasta interna '.git' de lá.
# ==============================================================================
def sincronizar_skill(skill: dict, pasta_destino_base: Path):
    skill_id = skill["id"]
    repo = skill["repo"]
    branch = skill.get("branch", "main")
    url_repo = f"https://github.com/{repo}.git"

    print(f"\n--- Sincronizando: {skill_id} ({repo} @ {branch}) ---")

    pasta_final_skill = pasta_destino_base / skill_id

    with tempfile.TemporaryDirectory() as temp_dir:
        caminho_temp = Path(temp_dir) / "clone"

        # Clona apenas o commit mais recente (depth 1) para ser ultra rapido e leve
        comando_clone = [
            "git",
            "clone",
            "--depth",
            "1",
            "--branch",
            branch,
            url_repo,
            str(caminho_temp),
        ]

        resultado = subprocess.run(comando_clone, capture_output=True, text=True)
        if resultado.returncode != 0:
            print(f"Aviso: Falha ao clonar {repo}: {resultado.stderr.strip()}")
            return False

        # Cria ou limpa a pasta da skill no catalogo garantindo compatibilidade com Windows
        def _remover_erro(action, name, exc):
            import stat
            os.chmod(name, stat.S_IWRITE)
            action(name)

        if pasta_final_skill.exists():
            shutil.rmtree(pasta_final_skill, onerror=_remover_erro if sys.version_info < (3, 12) else None, onexc=_remover_erro if sys.version_info >= (3, 12) else None)
        pasta_final_skill.mkdir(parents=True, exist_ok=True)

        # Copia todos os arquivos ignorando a pasta .git interna
        for item in caminho_temp.iterdir():
            if item.name == ".git":
                continue
            destino = pasta_final_skill / item.name
            if item.is_dir():
                shutil.copytree(item, destino)
            else:
                shutil.copy2(item, destino)

        print(f"Sucesso: {skill_id} atualizada com sucesso no catalogo!")
        return True


# ==============================================================================
# Fluxo principal de execução
# O que esta parte faz: Percorre todas as skills registradas e executa a sincronização.
# Para que serve / Como funciona no fluxo: Ponto de entrada do script tanto para
# rodar localmente no seu computador quanto para ser chamado pelo GitHub Actions.
# ==============================================================================
def main():
    raiz_projeto = Path(__file__).resolve().parent.parent
    arquivo_catalogo = raiz_projeto / "skills.json"
    pasta_skills = raiz_projeto / "skills"

    pasta_skills.mkdir(parents=True, exist_ok=True)
    skills = carregar_catalogo(arquivo_catalogo)

    total = len(skills)
    sucessos = 0

    print(f"Iniciando sincronizacao do catalogo ({total} skills encontradas)...")

    for skill in skills:
        if sincronizar_skill(skill, pasta_skills):
            sucessos += 1

    print(f"\nConcluido: {sucessos} de {total} skills sincronizadas com sucesso!")


if __name__ == "__main__":
    main()
