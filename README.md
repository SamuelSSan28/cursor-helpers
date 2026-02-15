# Cursor Workspace Setup (FastAPI + Pydantic + pytest)

This repository provides a lean, practical Cursor setup focused on Python backend quality.

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
   │  ├─ python-fastapi.mdc
   │  ├─ python-pydantic.mdc
   │  ├─ python-pytest.mdc
   │  ├─ python-review-format.mdc
   │  ├─ 10-backend-nest.mdc
   │  ├─ 20-frontend-next.mdc
   │  └─ 90-reviewer.mdc
   ├─ commands/
   │  ├─ agent-backend-nest.md
   │  ├─ agent-frontend-next.md
   │  ├─ agent-reviewer.md
   │  └─ agent-refactor.md
   └─ skills/
      ├─ skill-clean-code.md
      └─ skill-react-next-patterns.md
```

> If you are working only with FastAPI, prioritize the Python rule files listed above.

---

## What each layer means (practical)

### 1) Rules — when to use
Rules are persistent constraints that should be applied automatically.

Use rules for things that are:
- structural,
- non-negotiable,
- always expected.

For FastAPI projects, rules should enforce:
- thin routers,
- business logic in service/use-case layers,
- Pydantic validation at boundaries,
- pytest coverage for new behavior,
- naming and Clean Code conventions.

**Mindset:** if you never want to debate it again, make it a rule.

### 2) Commands — when to use
Commands are reusable prompt templates for specific task execution.

Use commands when you want consistent output for tasks like:
- implementing a feature,
- reviewing code,
- refactoring safely,
- writing tests.

**Mindset:** I want repeatable behavior for this task type.

### 3) Skills — when to use
Skills are compact reference modules with technical patterns.

Use skills when the model needs guidance on how your team builds things (style, architecture, standards).

**Mindset:** this is how our engineering standards work.

### 4) Hooks — when to use
Hooks are event-based automation (reminders/checks on file changes).

They are optional. Start without hooks unless you need automated guardrails.

### 5) MCP — when to use
MCP is for external tool integration (scripts, services, databases, generators).

This workspace currently avoids MCP to keep things simple.

---

## How layers work together (real FastAPI flow)

Example: you need a new endpoint.

1. Start with a command template for implementation.
2. Cursor applies project and Python rules (`.cursorrules` + `python-*.mdc`).
3. Use skill references for naming and architecture consistency.
4. Run review command and enforce the review format.
5. Add/update pytest coverage.

---

## Responsibility hierarchy

| Layer | Purpose | Usage frequency |
|---|---|---|
| Rules | Fixed project constraints | Always |
| Commands | Task execution format | Very frequent |
| Skills | Technical reference patterns | Medium |
| Hooks | Automation | Optional |
| MCP | External integrations | Advanced |

---

## What matters most for your current stack

For **FastAPI + Pydantic + pytest**, you mainly need:

- ✅ Rules
- ✅ Command templates
- ✅ Skills

You do **not** need initially:

- ❌ Hooks
- ❌ MCP

Keep the workflow simple: **implement -> test -> refactor -> review**.
