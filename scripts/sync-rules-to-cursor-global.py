#!/usr/bin/env python3
"""
Sync this repo into Cursor global config:
1) User Rules (state.vscdb): .cursorrules + rules + skills + commands as text
2) ~/.cursor/skills/: copy each skill folder so skills appear globally
3) ~/.cursor/commands/: copy each command .md so commands appear globally
Run from repo root or pass REPO_ROOT. Cursor should be closed to avoid overwrite.
"""
import re
import shutil
import sqlite3
import sys
from pathlib import Path

CURSOR_STATE_DB = Path.home() / ".config/Cursor/User/globalStorage/state.vscdb"
CONTEXT_KEY = "aicontext.personalContext"
GLOBAL_SKILLS_DIR = Path.home() / ".cursor" / "skills"
GLOBAL_COMMANDS_DIR = Path.home() / ".cursor" / "commands"


def _rule_order(path: Path) -> tuple[int, str]:
    """Sort by leading number in filename (00, 10, 20, ...), then by name."""
    match = re.match(r"^(\d+)", path.stem)
    return (int(match.group(1)), path.name) if match else (999, path.name)


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    if len(sys.argv) > 1:
        repo_root = Path(sys.argv[1]).resolve()

    cursor_dir = repo_root / ".cursor"
    cursorrules_file = repo_root / ".cursorrules"
    rules_dir = cursor_dir / "rules"
    skills_dir = cursor_dir / "skills"
    commands_dir = cursor_dir / "commands"

    parts: list[str] = []

    if cursorrules_file.exists():
        parts.append(cursorrules_file.read_text(encoding="utf-8").strip())
        parts.append("")

    if rules_dir.exists():
        parts.append("## Rules")
        mdc_files = sorted(rules_dir.glob("*.mdc"), key=_rule_order)
        for path in mdc_files:
            parts.append(f"### {path.stem}\n" + path.read_text(encoding="utf-8").strip())
        parts.append("")

    if skills_dir.exists():
        parts.append("## Skills")
        for skill_dir in sorted(skills_dir.iterdir()):
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if skill_md.exists():
                parts.append(f"### {skill_dir.name}\n" + skill_md.read_text(encoding="utf-8").strip())
        parts.append("")

    if commands_dir.exists():
        parts.append("## Commands")
        for path in sorted(commands_dir.glob("*.md")):
            parts.append(f"### {path.stem}\n" + path.read_text(encoding="utf-8").strip())
        parts.append("")

    merged = "\n\n---\n\n".join(p for p in parts if p)

    if not merged:
        print("No .cursorrules or .cursor content found.")
        sys.exit(1)

    if not CURSOR_STATE_DB.exists():
        print(f"Cursor state DB not found: {CURSOR_STATE_DB}")
        sys.exit(1)

    conn = sqlite3.connect(CURSOR_STATE_DB)
    try:
        conn.execute(
            "UPDATE ItemTable SET value = ? WHERE key = ?",
            (merged, CONTEXT_KEY),
        )
        if conn.total_changes == 0:
            conn.execute(
                "INSERT INTO ItemTable (key, value) VALUES (?, ?)",
                (CONTEXT_KEY, merged),
            )
        conn.commit()
        print("Global User Rules updated.")
    finally:
        conn.close()

    _sync_global_skills(repo_root)
    _sync_global_commands(repo_root)


def _sync_global_skills(repo_root: Path) -> None:
    skills_dir = repo_root / ".cursor" / "skills"
    if not skills_dir.exists():
        return
    GLOBAL_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        if (skill_dir / "SKILL.md").exists():
            target = GLOBAL_SKILLS_DIR / skill_dir.name
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(skill_dir, target)
    print("Global skills copied to ~/.cursor/skills/")


def _sync_global_commands(repo_root: Path) -> None:
    commands_dir = repo_root / ".cursor" / "commands"
    if not commands_dir.exists():
        return
    GLOBAL_COMMANDS_DIR.mkdir(parents=True, exist_ok=True)
    for path in sorted(commands_dir.glob("*.md")):
        shutil.copy2(path, GLOBAL_COMMANDS_DIR / path.name)
    print("Global commands copied to ~/.cursor/commands/")


if __name__ == "__main__":
    main()
