#!/usr/bin/env python3
"""
Percorre os repositórios na pasta informada e cria symlinks de .cursor e .cursorrules
apontando para este repo (cursor-helpers). Ignora o próprio cursor-helpers.
Uso: python3 scripts/link-cursor-in-repos.py [DIR_REPOSITORIOS]
"""
from pathlib import Path
import sys

REPO_NAME = "cursor-helpers"


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    if len(sys.argv) > 1:
        repos_dir = Path(sys.argv[1]).resolve()
    else:
        repos_dir = repo_root.parent

    if not repos_dir.is_dir():
        print(f"Pasta não encontrada: {repos_dir}")
        sys.exit(1)

    source_cursor = repo_root / ".cursor"
    source_cursorrules = repo_root / ".cursorrules"
    if not source_cursor.is_dir() or not source_cursorrules.is_file():
        print("Este repo não tem .cursor/ ou .cursorrules. Rode a partir de cursor-helpers.")
        sys.exit(1)

    linked = 0
    skipped = 0
    for path in sorted(repos_dir.iterdir()):
        if not path.is_dir():
            continue
        if path.name == REPO_NAME:
            print(f"  skip {path.name} (é o repo das configs)")
            skipped += 1
            continue
        if path.name.startswith("."):
            continue

        target_cursor = path / ".cursor"
        target_cursorrules = path / ".cursorrules"

        try:
            if target_cursor.exists():
                target_cursor.unlink()
            if target_cursorrules.exists():
                target_cursorrules.unlink()
            target_cursor.symlink_to(source_cursor)
            target_cursorrules.symlink_to(source_cursorrules)
            print(f"  ok   {path.name}")
            linked += 1
        except OSError as e:
            print(f"  err  {path.name}: {e}")

    print(f"\nResumo: {linked} repos com symlinks, {skipped} ignorados.")


if __name__ == "__main__":
    main()
