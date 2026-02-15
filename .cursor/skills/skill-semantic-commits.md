Skill: Semantic Commits (Single-line) + Change Grouping

Goal:
Given a set of changed files (git status / diff summary), propose:
1) logical commit groups (if it makes sense to split)
2) one Conventional Commit message per group (single line)
3) the exact file list for each commit group

Rules:
- Conventional Commit format (single line):
  <type>(<scope>): <imperative summary>
- Use types: feat | fix | refactor | test | docs | chore | ci | perf | build
- Summary must be imperative, concise, and specific.
- One commit must represent one cohesive intent.
- Prefer fewer commits unless changes represent distinct intents.
- Avoid mixing unrelated areas (backend vs frontend vs infra) unless they are tightly coupled.

Scopes (suggested):
- api-python (FastAPI)
- api (NestJS)
- web (Next.js)
- shared
- infra
- ci
- docs

Grouping heuristics:
- Group by feature/module path first (e.g., modules/payments/*).
- Then by layer: schema/service/router/tests can be grouped if they belong to the same feature.
- Separate pure formatting/lint changes into chore.
- Separate test-only changes into test.
- Separate refactors from behavior changes unless strictly required.

Output format:
- Commit Plan:
  - Group 1: [intent]
    - Files: [...]
    - Commit: type(scope): summary
  - Group 2: ...
- If everything is cohesive, propose a single commit.
