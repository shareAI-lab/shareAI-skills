# Visual and Evidence Patterns

Load this file for technical, architectural, or research reporting.

## Choose the smallest useful visual

| Need | Use |
|---|---|
| Ownership or layer boundary | Box hierarchy with named owners |
| Request, event, or data movement | Left-to-right or top-to-bottom flow |
| Pause, retry, resume, migration | State/lifecycle diagram |
| Exact mappings across several systems | Compact table |
| One definition serving several modes | One-to-many relationship tree |

One visual should answer one question. Keep labels short, arrows directional, and the main path obvious. Prefer a width that fits an ordinary code block without horizontal scrolling.

## Boundary pattern

```text
┌──────────────────┐
│ Business meaning │
└────────┬─────────┘
         │ resolved policy
         ▼
┌──────────────────┐
│ Runtime contract │
└────────┬─────────┘
         │ enforced effect
         ▼
┌──────────────────┐
│ External system  │
└──────────────────┘
```

Use this when the main question is “which layer owns what?” Replace labels with verified project objects; do not force every system into this template.

## Mechanism flow pattern

```text
input -> verify -> persist -> execute -> record -> deliver
```

Expand only the stages that affect the decision. Show retry, approval, or failure branches when they are the main risk.

## Fact versus inference

A diagram edge is a claim. Keep factual edges traceable to citations near the visual. Mark synthesized edges as `recommended`, `inferred`, or `application-owned` when the project does not ship them.

## Code provenance

Use one of these labels immediately above a code block:

- `官方原始用法（version/tag）`
- `官方用法的最小化改写（source link/path）`
- `源码关系摘录（commit + path）`
- `伪代码：推荐设计，不是现有 API`

For exact official code, preserve names and call relationships. Elide unrelated setup with comments rather than silently changing semantics. Keep excerpts short enough that the architectural point is visible.

## Attention sequence

Reveal complexity in this order:

```text
answer -> one mental model -> decisive proof -> boundary -> action
```

Do not lead with methodology, a glossary, or a vendor catalog. If the reader must learn a new term, define it beside the first diagram edge that depends on it.

## Visual failure checks

- A decorative box around prose adds weight without understanding.
- A diagram with several unrelated flows should be split or reduced.
- A dense ontology is not a senior brief; show only objects that change the choice.
- A code block without provenance risks turning plausible synthesis into false API evidence.
- A table with many nearly identical rows belongs in the artifact unless the differences decide the architecture.
