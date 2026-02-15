# Cursor Workspace Setup (FastAPI + Pydantic + pytest)

This repository provides a practical Cursor setup focused on Python backend quality.

- **Backend:** FastAPI + Pydantic
- **Testing:** pytest
- **Language policy:** English-only code and identifiers

The setup is intentionally simple: clear rules, reusable task commands, and lightweight skills.

## Project Structure

```text
.
├─ .cursorrules
└─ .cursor/
   ├─ rules/
   │  ├─ 00-global-clean-code.mdc
   │  ├─ 10-backend-nest.mdc
   │  ├─ 20-frontend-next.mdc
   │  ├─ 30-python-fastapi.mdc
   │  ├─ 40-python-pydantic.mdc
   │  ├─ 50-python-pytest.mdc
   │  ├─ 90-reviewer.mdc
   │  └─ 95-python-review-format.mdc
   ├─ commands/
   │  ├─ agent-backend-nest.md
   │  ├─ agent-frontend-next.md
   │  ├─ agent-reviewer.md
   │  └─ agent-refactor.md
   └─ skills/
      ├─ skill-clean-code.md
      └─ skill-react-next-patterns.md
```

## Rule filename order (numeric pattern)

Numeric prefixes keep files organized by responsibility and reading order:

- `00-*`: global base rules
- `10-*` and `20-*`: backend/frontend framework guidance
- `30-*` to `50-*`: Python implementation rules
- `90-*` and above: review/report formatting rules

For this workspace:
- `00-global-clean-code.mdc`: universal naming and code hygiene
- `10-backend-nest.mdc`: NestJS backend boundaries
- `20-frontend-next.mdc`: Next.js/React component and rendering guidance
- `30-python-fastapi.mdc`: FastAPI router/service architecture
- `40-python-pydantic.mdc`: Pydantic validation/model discipline
- `50-python-pytest.mdc`: pytest quality expectations
- `90-reviewer.mdc`: generic review output format
- `95-python-review-format.mdc`: Python-specific review checklist

## How to use each layer

### 1) Rules
Rules are persistent constraints applied automatically.

Use rules for anything that is:
- structural,
- non-negotiable,
- always expected.

For FastAPI projects, rules should enforce:
- thin routers,
- business logic in service/use-case layers,
- Pydantic validation at boundaries,
- pytest coverage for new behavior,
- naming and Clean Code conventions.

### 2) Commands
Commands are reusable prompt templates for specific tasks.

Use commands for consistent output when:
- implementing a feature,
- reviewing code,
- refactoring safely,
- writing tests.

### 3) Skills
Skills are compact reference modules with technical patterns.

Use skills when the model needs guidance on team standards (style, architecture, naming).
