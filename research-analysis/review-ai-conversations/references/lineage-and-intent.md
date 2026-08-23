# Conversation Lineage and Intent

Read this file only when forks, child Agents, copied prefixes, compaction, rollover, or
original-intent drift affects the requested review.

## Reconstruct only proven relationships

```text
root conversation
  |- fork: shared prefix + distinct continuation
  |- child Agent: delegated task and result attached to a parent
  `- context epoch: continuity proven by Store-specific markers
```

- Count a copied ancestor once and keep every relevant divergent suffix.
- Do not classify repeated wording as a fork without stronger lineage evidence.
- Treat a child Agent's user-role prompt as delegated work unless human authorship is
  independently proven. Attach useful results to the parent.
- Connect context epochs only through explicit lineage, stable identity, or a proven
  copied-prefix relationship. Similar summaries alone do not prove continuity.
- Use summaries to bridge missing history, never to replace retained original messages.

For an ordinary review, select the branch relevant to the request and label ambiguity.
Preserve every branch only when comparing alternatives, recovering abandoned work, or
auditing drift.

## Audit intent only when needed

When the user asks whether work drifted, retain the original human text or stable exact
reference and normalize a question set beside it, never instead of it. Compare later AI
interpretations, delegated tasks, summaries, artifacts, and conclusions as:

```text
preserved | narrowed | expanded | distorted | dropped | unresolved
```

Show where a material change first appeared and whether later work recovered it.
Repeated AI summaries may share one misunderstanding and are not independent evidence.
