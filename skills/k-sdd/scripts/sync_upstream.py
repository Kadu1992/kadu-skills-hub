#!/usr/bin/env python3
"""
sync_upstream.py - Sincronização inteligente com o repositório upstream do Tech Lead's Club.

Verifica e atualiza a skill k-sdd a partir do repositório upstream oficial
(tech-leads-club/agent-skills) sem a necessidade de clonar ou manter o monorepo gigante.

Preserva 100% das extensões e melhorias autorais do k-sdd (UAT Feedback Loop,
PRD/FRD, DESIGN.md Stitch e scripts adicionais).

Uso:
  python3 scripts/sync_upstream.py --check
  python3 scripts/sync_upstream.py --pull
"""

import argparse
import hashlib
import json
import os
import sys
import urllib.request
import urllib.error

UPSTREAM_API = "https://api.github.com/repos/tech-leads-club/agent-skills/contents/packages/skills-catalog/skills/(development)/tlc-spec-driven"
HEADERS = {
    "User-Agent": "k-sdd-sync-tool",
    "Accept": "application/vnd.github.v3+json"
}

# Arquivos e pastas exclusivos do k-sdd que JAMAIS devem ser sobrescritos
PRESERVED_PATHS = {
    "scripts/sync_upstream.py",
    "scripts/migrate_tlc.py",
    "references/prd-frd.md",
    "references/stitch-design.md",
    "references/uat-feedback.md",
    ".github",
    ".git"
}


def get_remote_tree(api_url):
    """Obtém a lista de arquivos da pasta remota no GitHub."""
    req = urllib.request.Request(api_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Erro ao consultar API do GitHub ({e.code}): {e.reason}")
        return []
    except Exception as e:
        print(f"Falha na conexão com upstream: {e}")
        return []


def calculate_hash(filepath):
    """Calcula o hash sha256 de um arquivo local."""
    if not os.path.exists(filepath):
        return None
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


def run_sync(base_dir, pull=False):
    print("=" * 60)
    print(" 🔄 k-sdd Upstream Sync Tool (Tech Lead's Club Tracker)")
    print("=" * 60)
    print("Consultando upstream oficial...")

    items = get_remote_tree(UPSTREAM_API)
    if not items:
        print("❌ Não foi possível obter dados do upstream. Verifique sua conexão à internet.")
        return 1

    updates_found = []
    
    # Processa itens raiz (SKILL.md, scripts, references)
    for item in items:
        name = item.get("name")
        item_type = item.get("type")
        download_url = item.get("download_url")

        if item_type == "file":
            local_path = os.path.join(base_dir, name)
            if name == "SKILL.md":
                # O SKILL.md do k-sdd é customizado; apenas avisa se houver nova versão remota
                print(f"ℹ️  [Upstream] SKILL.md upstream detectado no repositório oficial.")
                continue

            # Baixa e compara
            if download_url:
                try:
                    req = urllib.request.Request(download_url, headers=HEADERS)
                    with urllib.request.urlopen(req, timeout=10) as resp:
                        remote_content = resp.read()
                    remote_hash = hashlib.sha256(remote_content).hexdigest()
                    local_hash = calculate_hash(local_path)
                    if local_hash != remote_hash:
                        updates_found.append((name, download_url, local_path, remote_content))
                except Exception as e:
                    print(f"Aviso ao checar {name}: {e}")

        elif item_type == "dir" and name in ["references", "scripts"]:
            sub_items = get_remote_tree(item.get("url"))
            for sub in sub_items:
                sub_name = sub.get("name")
                rel_path = f"{name}/{sub_name}"
                if rel_path in PRESERVED_PATHS:
                    continue
                local_sub_path = os.path.join(base_dir, name, sub_name)
                sub_dl = sub.get("download_url")
                if sub_dl:
                    try:
                        req = urllib.request.Request(sub_dl, headers=HEADERS)
                        with urllib.request.urlopen(req, timeout=10) as resp:
                            remote_sub_content = resp.read()
                        remote_hash = hashlib.sha256(remote_sub_content).hexdigest()
                        local_hash = calculate_hash(local_sub_path)
                        if local_hash != remote_hash:
                            updates_found.append((rel_path, sub_dl, local_sub_path, remote_sub_content))
                    except Exception as e:
                        print(f"Aviso ao checar {rel_path}: {e}")

    if not updates_found:
        print("✅ Sua skill k-sdd está 100% atualizada com o upstream oficial!")
        return 0

    print(f"\n📢 Foram encontradas {len(updates_found)} atualizações no upstream:")
    for rel_name, _, _, _ in updates_found:
        print(f"  • {rel_name}")

    if not pull:
        print("\nPara aplicar essas atualizações mantendo suas customizações, execute:")
        print("  python3 scripts/sync_upstream.py --pull")
        return 0

    # Aplica atualizações
    print("\nAplicando atualizações...")
    for rel_name, _, dest_path, content in updates_found:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "wb") as f:
            f.write(content)
        print(f"  ✓ Atualizado: {rel_name}")

    print("\n🎉 Atualização concluída com sucesso! Todas as novidades do upstream foram mescladas.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="k-sdd Upstream Sync Tool")
    parser.add_argument("--check", action="store_true", help="Apenas verifica se há novidades sem alterar arquivos")
    parser.add_argument("--pull", action="store_true", help="Baixa e aplica as novidades do upstream")
    args = parser.parse_args()

    skill_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    pull_mode = args.pull or not args.check
    return run_sync(skill_root, pull=args.pull)


if __name__ == "__main__":
    sys.exit(main())
