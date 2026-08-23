# Efficient Conversation Retrieval

Read this file only when local Agent Stores must be searched. Product-specific paths
and fields remain in `sources/`; this file defines the shared retrieval strategy.

## Treat Store schemas as observed anchors

Local clients may rename fields, add wrappers, change timestamp representations, or
introduce a newer projection. Product references record the last-known storage root,
time index, lineage markers, and visible message fields. Treat them as strong starting
evidence, not immutable parser contracts.

For small schema drift, inspect a few neighboring records from one or two candidates.
Infer the new mapping from stable conversation identity, record order, plausible
timestamps, parent relationships, human-authored prompts, visible assistant text, and
turn continuity. Adapt the selector once, then apply it to the whole batch.

Do not force a new schema to fit by treating tool output, reasoning, copied context, or
synthetic instructions as visible conversation. Ask the user only when two plausible
mappings would materially change the included human conversations or conclusions.

## Use bounded passes

```text
one index pass per product
  -> select in-window conversation families
one body pass per selected family
  -> visible turns + lineage markers + activity time
  -> one compact conversation capsule
cross-session analysis
  -> cluster capsules
  -> reopen raw text only for decisive evidence or contradictions
```

Freeze one UTC `[start, end]` window. Prefer the maximum accepted human-message or
visible AI-message timestamp as real activity time. File mtime is only a fallback when
the Store exposes no message or session clock.

Use this capsule as a working shape, adapting it when the analysis needs less or more:

```text
{
  agent, conversation_id, activity_time, workstream,
  lineage: {root, parent, relation, context_epochs[]},
  original_user_requests[{message_ref, exact_text}],
  normalized_question_set[], derived_agent_tasks[],
  ai_conclusions[], intent_coverage[], decisions[],
  artifacts[], open_loops[], candidate_insights[]
}
```

Preserve message references so exact text can be reopened without concatenating every
conversation into one giant transcript. When several products are in scope, process
their independent Stores concurrently when practical, but keep one owner for each
canonical conversation family.

## Recover visible conversation, not execution noise

Keep accepted human-authored messages and visible assistant replies in conversational
order. Exclude tool calls, internal reasoning, system injection, copied parent history,
host commands, and synthetic messages. Read child work only when its derived results
materially inform the parent review.

Avoid expensive or misleading retrieval patterns:

- Do not walk every file when an index already identifies candidates.
- Do not probe the same schema repeatedly.
- Do not query once per message, part, or bubble; batch selected conversation IDs.
- Do not reread a conversation separately for metadata, questions, replies, and
  artifacts; collect them together.
- Do not concatenate all raw text before classification; compress per conversation,
  then cluster capsules.
- Do not stop at an inventory or intermediate export unless requested.
