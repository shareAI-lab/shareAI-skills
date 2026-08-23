# Evidence Protocol

Use this protocol after the user confirms the research map.

## Source order

1. Current source, tests, schemas, tags, and release artifacts.
2. Official documentation, API/SDK references, migration guides, and release notes.
3. GitHub issues, discussions, PRs, commit history, and maintainer explanations.
4. Maintainer talks and high-quality technical blogs with direct evidence.
5. Hacker News, Reddit, X/Twitter, and third-party posts as discovery and pain signals.

Community material may identify failures or disputed scenarios. It does not prove implementation behavior until traced to source, official docs, a reproducer, or a maintainer-confirmed issue.

## Source-code practice

When source is available, prefer a local clone over browsing individual source files online.

- Reuse the repository's canonical reference clone when one exists; otherwise clone into a task-scoped location.
- Record remote URL, branch, commit, tag/version, and research date before drawing conclusions.
- Inspect the current execution path first with `rg`, tests, schemas, and entrypoints.
- Then inspect history: the last six months in detail and up to two years for architectural or breaking changes.
- Compare relevant tags/branches and read migrations, changelogs, removed modules, and changed default examples.
- Use `git log`, `git show`, `git diff`, blame, PRs, issues, and discussions to explain why a seam moved, not merely that files changed.

Do not treat stars, README claims, generated docs, or an unmerged PR as runtime truth.

## Closed-source and hosted products

Use official API/SDK documentation, real official examples, changelogs, status labels, limits, pricing/availability pages, and published engineering reports. State what cannot be verified from public material.

Distinguish developer-account organization/workspace tenancy from the end user's business organization model.

## Evidence ledger

Tag decisive findings during research:

| Tag | Meaning |
|---|---|
| `[CODE]` | Verified current source or test behavior |
| `[DOC]` | Current official contract or documentation |
| `[HIST]` | Commit, release, migration, or version history |
| `[ISSUE]` | Reproduced or maintainer-confirmed problem/boundary |
| `[COMM]` | Community signal awaiting or accompanied by stronger evidence |
| `[PLAN]` | Roadmap, RFC, open PR, or announced future work |
| `[INF]` | Explicit architectural inference from cited evidence |

Resolve conflicts in favor of current executable source for implementation facts, while noting when public docs describe a different supported contract.

## Boundary and failure-path review

For each central mechanism, trace at least one happy path and the production failure paths that matter to the user's design:

- identity, authorization, tenant isolation, and credential ownership;
- concurrency, ordering, retries, idempotency, and delivery;
- session, memory, workspace, checkpoint, snapshot, and migration ownership;
- upgrade compatibility, deprecation, rollback, and data retention;
- long tasks, pause/resume, cancellation, approval, and crash recovery;
- embedded, self-hosted, serverless, and managed deployment limits.

## Code and diagram truth

- Exact code examples come from official docs, examples, or inspected source. Cite the URL/path and version/commit.
- A shortened official example must preserve the actual API relationship and be labeled `minimal adaptation of official usage`.
- Synthesized code must be labeled `pseudocode` or `recommended interface`; never present it as shipped API.
- A diagram may synthesize relationships, but label inference and keep every factual edge traceable to evidence.

## Stop condition

Stop expanding when additional sources repeat the same mechanism or pain without changing the decision. Put secondary evidence in the artifact, not the executive report.
