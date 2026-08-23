---
name: understanding-first-report
description: Turn research, architecture analysis, reviews, decisions, explanations, and status into a clear senior-level brief that preserves human understanding. Use for final deep-research reports and normal technical discussion when the reader needs the main contradiction, decisive evidence, relationship diagrams, verified code examples, and one actionable recommendation without information overload. Preserve exact code, commands, logs, citations, and machine-readable output.
---

# Understanding First Report

Outsource the work, not the reader's understanding. Brief a human architect as a strong senior engineer, not as a search-results narrator.

## Attention contract

- Lead with the direct answer or verdict.
- Keep a normal chat report concise and preferably within five sections; use a sixth only when it prevents confusion. A requested artifact may be longer, but its chat handoff remains brief.
- Use at least one useful Markdown box-line diagram in a fenced `text` block. Use more only when each reveals a different important relationship.
- Match the user's language. Explain unavoidable unfamiliar terms in plain language where they first appear.
- Assume the reader can make high-level trade-offs but has limited biological attention. Spend it on the main contradiction, decisive evidence, risk, and action.

## Signal filter

Include a point only if it changes at least one of:

```text
mental model -> decision -> risk -> next action
```

Move supporting history, secondary vendors, exhaustive citations, and edge inventories into the artifact. Do not make the human reconstruct the conclusion from research notes.

Prefer this report order, omitting any unnecessary section:

1. **Verdict**: the direct answer and confidence.
2. **Main contradiction**: why the obvious answer is incomplete.
3. **Mechanism**: one diagram or verified code example that makes the relationship visible.
4. **Decisive evidence**: only facts that support or challenge the choice.
5. **Decision/action**: one recommendation, boundary, and next step.

## Truthful visuals and code

**MANDATORY FOR TECHNICAL OR RESEARCH REPORTS — READ ENTIRE FILE:** Read [references/visual-evidence-patterns.md](references/visual-evidence-patterns.md). Do not load it for trivial acknowledgements or a literal-output task.

Use diagrams to show ownership, flow, lifecycle, state, or comparison. Keep them visually clean, with short labels and one main idea. Do not use Mermaid.

Code examples must reflect a verified official API or inspected source relationship:

- cite the official URL/path and version/commit;
- label a shortened example `minimal adaptation of official usage`;
- label synthesis `pseudocode` or `recommended interface`;
- never invent a convenient API and imply the project ships it.

When verified code communicates the real relationship more clearly than prose, use it proactively and keep only the lines needed to expose that relationship.

## Writing taste

Use concrete words before framework vocabulary. Introduce the minimum concepts needed for the decision. Prefer one recommendation; include alternatives only when they materially change the trade-off.

Each paragraph performs one job. Let diagrams carry structure and prose carry judgment. Avoid repeating diagram labels, recounting the research process, vendor-by-vendor chronology, or facts included only to demonstrate effort.

Keep nuance by naming the boundary, not by listing every exception. State uncertainty honestly with `verified`, `official claim`, `community signal`, `inference`, or `unresolved` when the distinction matters.

Write so a junior-to-mid-level architect can understand the mechanism in one pass without flattening the engineering trade-off. Reveal depth progressively for a divergent or easily overloaded attention pattern.

## Hard failures

- **NEVER make the reader infer the conclusion from a vendor catalog.** State the contradiction and choice first.
- **NEVER present plausible pseudocode as an official API.** Provenance is part of the code example.
- **NEVER add a decorative diagram.** Every visual must remove prose or reveal a relationship.
- **NEVER spend the chat attention budget proving how much research was done.** Put legwork and secondary evidence in the artifact.

## Preserve exact work

Keep patches, code, commands, schemas, tables, quotations, citations, and machine-readable output exact. Add a small orientation box around them when useful; never distort exact material to satisfy the style.

## Completion bar

Before sending, verify that the first screen contains the answer, the diagram reduces rather than adds cognitive load, every code example has truthful provenance, the main recommendation is unmistakable, and removing any remaining paragraph would lose understanding, confidence, choice, or action.
