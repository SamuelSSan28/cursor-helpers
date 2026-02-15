# Cursor Workspace Setup (NestJS + Next.js + FastAPI)

This repository provides a lean, practical Cursor setup for:

- **Backend:** NestJS + TypeScript, FastAPI + Pydantic
- **Frontend:** Next.js + TypeScript
- **Testing:** pytest for Python services
- **Support scripting:** Python

It is designed to keep behavior consistent through **global rules**, **context rules**, **agent-like commands**, and **reusable skills**.

## Project Structure

```text
.
├─ .cursorrules
└─ .cursor/
   ├─ rules/
   │  ├─ 00-global-clean-code.mdc
   │  ├─ 10-backend-nest.mdc
   │  ├─ 20-frontend-next.mdc
   │  ├─ 90-reviewer.mdc
   │  ├─ python-fastapi.mdc
   │  ├─ python-pydantic.mdc
   │  ├─ python-pytest.mdc
   │  └─ python-review-format.mdc
   ├─ commands/
   │  ├─ agent-backend-nest.md
   │  ├─ agent-frontend-next.md
   │  ├─ agent-reviewer.md
   │  └─ agent-refactor.md
   └─ skills/
      ├─ skill-clean-code.md
      └─ skill-react-next-patterns.md
```

## How to use in Cursor

### 1) Apply persistent behavior with rules
- Keep `.cursorrules` at the repository root for project-wide constraints.
- Use `.cursor/rules/*.mdc` for context-specific behavior:
  - `00-global-clean-code.mdc`: always-on naming and code hygiene
  - `10-backend-nest.mdc`: NestJS backend constraints for controllers/services/tests
  - `20-frontend-next.mdc`: Next.js constraints for render and component design
  - `python-fastapi.mdc`: FastAPI layering and endpoint boundaries
  - `python-pydantic.mdc`: schema and validation discipline
  - `python-pytest.mdc`: test quality expectations
  - `90-reviewer.mdc` and `python-review-format.mdc`: standardized review output formats

### 2) Use commands as practical agents
Cursor custom modes are deprecated, so use command templates as your agent prompts:
- `agent-backend-nest.md`: implement backend features
- `agent-frontend-next.md`: implement frontend features
- `agent-reviewer.md`: perform strict code reviews
- `agent-refactor.md`: refactor without behavior changes

### 3) Use skills as reusable knowledge modules
- `skill-clean-code.md`: naming, control flow, constants, comments
- `skill-react-next-patterns.md`: clean React/Next patterns

## When to use each file

- Use **`.cursorrules`** for organization-wide standards that should always apply.
- Use **`rules/*.mdc`** when behavior must change by language/framework area.
- Use **`commands/*.md`** at task start to force a consistent delivery format.
- Use **`skills/*.md`** as compact reference modules during implementation and review.

## Notes

- This setup intentionally avoids MCP.
- Keep the workflow simple: implement -> test -> refactor -> review.
