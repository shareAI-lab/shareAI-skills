# Conversation Lineage and Intent Preservation

Read this file when selected records contain forks, subagents, copied prefixes,
compaction summaries, context rollover, or signs that later work drifted from the
user's original request.

## Reconstruct the conversation family

A stored session is not necessarily one human conversation, and one human conversation
is not necessarily one context window.

```text
root human conversation
  ├─ fork: shared ancestors + branch-specific human continuation
  ├─ subagent: derived task and evidence attached to its parent
  └─ epoch 1 -> compaction -> epoch 2 -> compaction -> epoch 3
                         one logical conversation
```

- **Root conversation**: human-authored messages are the primary record of intent.
- **Fork**: count shared ancestors once. Preserve new human turns on each meaningful
  branch; do not silently merge divergent answers.
- **Subagent**: its delegated prompt is a derived agent task, not a new human request,
  unless the Store proves human authorship. Attach useful results and artifacts to the
  parent conversation.
- **Compaction or rollover**: each segment is another context epoch of the same logical
  conversation. A summary helps navigation but does not replace retained raw messages.
- **Missing ancestors**: when only a summary survives, label recovered intent as
  summary-derived rather than presenting it as verbatim.

Deduplicate by lineage and stable message identity when available. Text equality alone
is insufficient: a user may intentionally repeat a question, while a fork may copy an
ancestor under a new session ID.

## Preserve and audit the original question set

Retain every accepted human request verbatim, or retain a stable address to the exact
text when it is too large for working context. Build a normalized question set beside
the original, never instead of it. Preserve constraints, exclusions, examples,
uncertainties, and small details that could change the intended answer.

```text
Q0: original user request set
        │ compare coverage and meaning
        ├─ AI interpretation
        ├─ delegated subagent tasks
        ├─ compaction summaries
        ├─ intermediate plans and artifacts
        └─ final answers and conclusions

coverage(q) = preserved | narrowed | expanded | distorted | dropped | unresolved
```

Treat drift as a review finding. A polished later summary may be less trustworthy than
an earlier raw message. When meaning changed, identify the original requirement, where
the change appeared, and whether later work recovered it. Repeated summaries may copy
the same misunderstanding rather than independently confirm it.
