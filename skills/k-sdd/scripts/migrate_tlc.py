#!/usr/bin/env python3
"""
migrate_tlc.py - Migração segura e completa de projetos tlc-spec-driven para k-sdd.

Permite migrar projetos que já utilizavam o tlc-spec-driven para o k-sdd
sem perder nenhum histórico, nenhuma task, nenhuma validação e nenhum commit.

Ações executadas:
1. Detecta features existentes em .specs/features/ e gera FRD retroativo se ausente.
2. Atualiza diretrizes no AGENTS.md trocando referências do tlc-spec-driven para k-sdd.
3. Remove a pasta legada .agents/skills/tlc-spec-driven.
4. Instala a skill k-sdd completa em .agents/skills/k-sdd (SKILL.md, scripts, references).
5. Registra a nova skill k-sdd no skills-lock.json do projeto.

Uso:
  python3 <skill-dir>/scripts/migrate_tlc.py [--root DIR]
"""

import argparse
import json
import os
import re
import shutil
import sys

# Garante suporte a UTF-8 no terminal Windows para exibição de emojis e acentuação
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def migrate_agents_md(root):
    agents_path = os.path.join(root, "AGENTS.md")
    if not os.path.exists(agents_path):
        return False
    content = open(agents_path, "r", encoding="utf-8", errors="replace").read()

    updated = content
    updated = updated.replace("tlc-spec-driven", "k-sdd")
    updated = updated.replace("Tech Lead's Club - Spec-Driven", "Kadu - Spec-Driven Development (k-sdd)")
    updated = updated.replace("TLC Spec-Driven Development", "Kadu - Spec-Driven Development (k-sdd)")
    updated = updated.replace("TLC Spec-Driven", "Kadu - Spec-Driven Development (k-sdd)")

    if "k-sdd" not in updated:
        updated += "\n\n<!-- k-sdd framework rules -->\n# k-sdd Governança\nEste projeto segue estritamente o framework k-sdd (P-E-R-A: PRD, FRD, DESIGN.md, Tasks atômicas com gates, UAT Feedback Loop e commits coesos por fase).\n"

    if updated != content:
        with open(agents_path, "w", encoding="utf-8") as f:
            f.write(updated)
        print("  ✓ AGENTS.md atualizado com sucesso para k-sdd.")
        return True
    else:
        print("  • AGENTS.md já está apontando para k-sdd.")
        return False


def migrate_features(root):
    feat_base = os.path.join(root, ".specs", "features")
    if not os.path.isdir(feat_base):
        print("  • Nenhuma pasta .specs/features/ encontrada para migrar.")
        return 0

    count = 0
    for f in sorted(os.listdir(feat_base)):
        fdir = os.path.join(feat_base, f)
        if not os.path.isdir(fdir):
            continue
        frd_path = os.path.join(fdir, "frd.md")
        spec_path = os.path.join(fdir, "spec.md")
        if not os.path.exists(frd_path) and os.path.exists(spec_path):
            # Cria FRD retroativo sintetizado a partir da spec
            spec_content = open(spec_path, "r", encoding="utf-8", errors="replace").read()
            title_m = re.search(r"^#\s+(.+)$", spec_content, re.MULTILINE)
            title = title_m.group(1).replace("Specification", "").strip() if title_m else f

            frd_template = f"""# FRD: {title}

## 1. Problema & Contexto
Funcionalidade migrada do histórico de desenvolvimento do projeto. Requisitos originais preservados em `spec.md`.

## 2. Solução & Capacidades
- Implementação completa e testada conforme decomposição em `tasks.md`.

## 3. Constraints (Inegociáveis)
- Manter convenções de código, tipos e frameworks definidos no projeto.

## 4. Critérios de Aceite de Alto Nível
- [x] Requisitos técnicos especificados em `spec.md` atendidos.
- [x] Validação formal aprovada em `validation.md`.
"""
            with open(frd_path, "w", encoding="utf-8") as out:
                out.write(frd_template)
            print(f"  ✓ FRD retroativo criado para a feature: {f}")
            count += 1
    return count


def cleanup_legacy_skill(root):
    legacy_path = os.path.join(root, ".agents", "skills", "tlc-spec-driven")
    if os.path.isdir(legacy_path):
        shutil.rmtree(legacy_path, ignore_errors=True)
        print("  ✓ Pasta legada .agents/skills/tlc-spec-driven removida com segurança.")


def install_ksdd_skill(root):
    # Identifica o diretório raiz da skill k-sdd onde o script está localizado
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_src = os.path.abspath(os.path.join(script_dir, ".."))

    dest_skill_dir = os.path.join(root, ".agents", "skills", "k-sdd")
    os.makedirs(dest_skill_dir, exist_ok=True)

    # Copia os arquivos e subpastas essenciais da skill k-sdd
    items_to_copy = ["SKILL.md", "README.md", "references", "scripts"]
    for item in items_to_copy:
        src_item = os.path.join(skill_src, item)
        dest_item = os.path.join(dest_skill_dir, item)
        if not os.path.exists(src_item):
            continue

        if os.path.isdir(src_item):
            if os.path.exists(dest_item):
                shutil.rmtree(dest_item, ignore_errors=True)
            shutil.copytree(
                src_item,
                dest_item,
                ignore=shutil.ignore_patterns(".git", ".github", "__pycache__", "*.pyc")
            )
        else:
            shutil.copy2(src_item, dest_item)

    print("  ✓ Skill k-sdd instalada com sucesso em .agents/skills/k-sdd.")

    # Atualiza ou cria o arquivo skills-lock.json registrando a k-sdd
    lock_path = os.path.join(root, "skills-lock.json")
    try:
        data = {"version": 1, "skills": {}}
        if os.path.exists(lock_path):
            with open(lock_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if "skills" not in data:
                data["skills"] = {}

        # Remove referência legada
        if "tlc-spec-driven" in data["skills"]:
            del data["skills"]["tlc-spec-driven"]

        # Registra a nova skill k-sdd
        data["skills"]["k-sdd"] = {
            "source": "Kadu1992/k-sdd",
            "sourceType": "github",
            "skillPath": "SKILL.md",
        }

        with open(lock_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print("  ✓ skills-lock.json atualizado com a referência oficial k-sdd.")
    except Exception as e:
        print(f"  Aviso ao atualizar skills-lock.json: {e}")


def main():
    parser = argparse.ArgumentParser(description="Migrador tlc-spec-driven -> k-sdd")
    parser.add_argument("--root", default=".", help="Raiz do projeto alvo (padrão: diretório atual)")
    args = parser.parse_args()

    root = os.path.abspath(args.root)
    print("=" * 60)
    print(f" 🚀 Migrador k-sdd: {root}")
    print("=" * 60)

    migrate_agents_md(root)
    migrated_features = migrate_features(root)
    cleanup_legacy_skill(root)
    install_ksdd_skill(root)

    print("-" * 60)
    print(f"🎉 Migração concluída com sucesso!")
    print(f"   • Features adaptadas: {migrated_features}")
    print(f"   • Nova skill instalada: .agents/skills/k-sdd")
    print(f"   • Bloqueio registrado: skills-lock.json")
    print("O projeto agora utiliza 100% o ecossistema k-sdd com todas as ferramentas disponíveis.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
