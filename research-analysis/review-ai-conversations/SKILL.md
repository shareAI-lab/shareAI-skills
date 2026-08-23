---
name: review-ai-conversations
description: Review and synthesize recent human-AI conversations across Claude Code, Codex, opencode, Grok Build, and Cursor while preserving original user intent across forks, subagents, and repeated context compaction. Use when the user wants to revisit work done with AI workers, cluster recurring questions, map the problem space, detect drift from original requests, review prior replies and artifacts as reference material, compress long-running work across sessions, deepen understanding, brainstorm, or surface new insights and next questions.
---

# Review AI Conversations

Help the user understand long-running work spread across conversations with multiple
AI workers. Reading local chat stores is only the input step; the deliverable is a
clear review of the work, problem space, decisions, and new insights.

## Accept natural-language requests

The user may specify any combination of:

- **Agents or locations**: one client, several clients, a project, or explicit paths.
- **Time range**: recent hours, days, weeks, calendar dates, or named conversations.
- **Focus**: architecture, work progress, decisions, repeated problems, or one topic.
- **Analysis type**: review, summary, comparison, clustering, problem map, or insights.
- **Content to extract**: prompts, visible replies, conclusions, artifacts, open questions.
- **Content to find**: a phrase, proposal, decision, changed belief, or missing answer.

Do not require the user to know store schemas or session IDs. Infer the intended scope
from ordinary language. Ask only when two interpretations would materially change the
conversations included in the review.

## Load only the relevant conversation source

When the user already supplied conversation text, analyze it directly and load no
source reference.

When local stores must be read, load only the matching source file:

- Claude Code: `references/sources/claude-code.md`
- Codex: `references/sources/codex.md`
- opencode: `references/sources/opencode.md`
- Grok Build: `references/sources/grok-build.md`
- Cursor: `references/sources/cursor.md`

Each source reference records four last-known anchors: the storage root, the recent/time
index and its units, root/child or fork identity, and the fields that contain the
user's question and visible AI reply. Treat these as strong starting evidence, not as
an immutable parser contract.

For a request spanning several products, process each source independently, then merge
the clean human/assistant conversations at the analysis stage.

Freeze one UTC `[start, end]` window for the review. Use the product's recorded
recent index to find candidates, then prefer the maximum accepted human-message or
visible AI-message timestamp as the conversation's real activity time. File mtime is
only a fallback when the store has no message or session clock.

## Exercise judgment when stores evolve

Local clients may rename fields, add wrappers, change timestamp representations, or
introduce a newer projection. Small schema drift is expected. Do not abandon the
review merely because one known path no longer matches.

```text
known shape matches
  -> use the source fast path

small local drift
  -> inspect a tiny representative sample
  -> infer the new mapping from semantic invariants
  -> adapt once and apply it to the whole selected batch

competing or contradictory projections
  -> compare continuity and visible human/assistant turns
  -> choose one canonical projection
  -> mention uncertainty only when it could change the review
```

Use semantic invariants to make the judgment: stable conversation identity, ordered
records, plausible timestamps, root/parent relationships, human-authored prompts,
visible assistant text, and continuity between adjacent turns. Field names alone are
weaker evidence than the role and behavior of the records.

Be autonomous but evidence-grounded. Tolerate renamed or nested fields and harmless
extra event types. Do not reinterpret tool output, reasoning, copied context, or
synthetic instructions as visible conversation merely to make a new schema fit. If
the shape changed substantially, derive the narrowest mapping that recovers a coherent
sample conversation, record that assumption internally, and continue. Ask the user
only when two plausible mappings would materially change which human conversations or
conclusions are included.

Keep adaptation cheap: inspect a few neighboring records from one or two candidates,
not the entire store; update the selector once; then return to the normal batched or
streaming path. Do not build and maintain a version-by-version schema matrix during an
ordinary review.

## Use the efficient retrieval path

Do not build one giant transcript. Use three bounded passes:

```text
one index pass per product
        │ select related root, fork, and child records in the frozen time window
        ▼
one body pass per conversation family
        │ recover lineage + original human turns + visible replies
        │ emit one lineage-aware conversation capsule
        ▼
cluster capsules across conversations
        │ reopen raw text only for decisive evidence or contradictions
        ▼
problem map + insights + next questions
```

Each conversation capsule should be compact and structured:

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

Extract visible turns and build the capsule in the same streaming read or database
query. Preserve references to conversation IDs and message positions so exact text can
be reopened without retaining or concatenating every message.

When several products are in scope and the environment permits it, process their
independent stores concurrently. Keep one owner for each canonical conversation so
branches are not summarized twice. Merge capsules, not raw transcripts.

Avoid retrieval work that does not improve the review:

- Do not walk every file when an index already identifies candidate conversations.
- Do not probe schemas repeatedly; inspect once only when observed fields differ from
  the matching source reference.
- Do not run one command or SQL query per message, part, or bubble; batch by selected
  conversation IDs.
- Do not reread a conversation separately for metadata, questions, replies, and
  artifacts; collect them in one pass.
- Do not concatenate all conversation text before classification. Compress each
  conversation first, then cluster the capsules.
- Do not stop after creating an inventory or intermediate export unless the user
  explicitly requested one.

## Reconstruct lineage before interpreting meaning

A stored session is not necessarily one human conversation, and one human
conversation is not necessarily one context window. Build a small lineage graph while
reading instead of flattening every record into one timeline:

```text
root human conversation
  ├─ fork: shared ancestors + branch-specific human continuation
  ├─ subagent: derived task and evidence attached to its parent
  └─ context epoch 1 -> compaction -> epoch 2 -> compaction -> epoch 3
                         one logical conversation, not three sessions
```

Apply these rules:

- **Root conversation**: human-authored messages are the primary record of intent.
- **Fork**: count shared ancestors once. Preserve new human turns on each meaningful
  branch, but do not duplicate the copied prefix or silently merge divergent answers.
- **Subagent session**: treat its delegated prompt as a derived agent task, not a new
  human request, unless the store proves that the user authored it. Attach useful
  results, artifacts, and disagreements to the parent conversation.
- **Compaction or context rollover**: treat each segment as another context epoch of
  the same logical conversation. A compaction summary helps navigation but is never a
  substitute for original human messages that still exist in the store.
- **Missing ancestors**: if only a summary or copied projection survives, label the
  recovered intent as summary-derived rather than silently presenting it as verbatim.

Deduplicate by lineage and stable message identity when available. Text equality alone
is not enough: a user may intentionally repeat a question, while a fork may copy the
same ancestor under a new session ID.

## Preserve the original question set and detect drift

Retain each accepted human-authored request verbatim, or retain a stable address to the
exact text when it is too large for working context. Build a normalized question set
beside the original text, never instead of it. Preserve constraints, exclusions,
examples, uncertainties, and small details that could change the intended result.

```text
Q0: original user request set
        │ compare coverage and meaning at every derived stage
        ├─ AI interpretation
        ├─ delegated subagent tasks
        ├─ compaction summaries
        ├─ intermediate plans and artifacts
        └─ final answers and conclusions

coverage(q) = preserved | narrowed | expanded | distorted | dropped | unresolved
```

Treat semantic drift as a first-class review finding. A polished later summary may be
less trustworthy than an earlier raw user message. When meaning changed, show the
specific original requirement, where the change appeared, and whether later work
recovered it. Do not assume that repeated AI summaries form independent confirmation;
they may be copies of the same earlier misunderstanding.

## Read the conversation body

Recover the user's actual messages and the visible AI replies in conversational order.
Exclude tool calls, internal reasoning, system injection, copied parent history,
subagent chatter, host commands, and synthetic messages that were not typed by the
user or shown as an AI reply.

Prefer complete conversation families. Do not count forks, retries, copied context,
compaction epochs, or subagents as independent lines of human thought. If a store has
changed shape, inspect the current fields and adapt instead of forcing an old parser
model.

Keep the capsule faithful rather than exhaustive. Pull exact original passages only
when they support a consequential decision, expose a contradiction, or explain why the
user's thinking changed.

## Build the review

Use these lenses selectively:

- **Current work**: what the user has actually been trying to accomplish.
- **Workstreams**: distinct lines of work that are independent, related, or converging.
- **Question clusters**: repeated prompts that are different forms of one deeper issue.
- **Problem space**: dimensions, quadrants, sets, overlaps, dependencies, and exclusions.
- **Evolution**: earlier beliefs, later corrections, and why the mental model changed.
- **Intent coverage**: which original requirements survived, drifted, or disappeared.
- **Decisions**: accepted directions, rejected options, and choices still missing.
- **Artifacts**: documents, code, reports, and plans mentioned or produced recently.
- **AI replies**: prior conclusions and proposals worth retaining, challenging, or revisiting.
- **Insights**: connections and implications visible only across multiple conversations.
- **Open minds**: alternative frames, experiments, or questions that could unlock progress.

AI replies and AI-generated artifacts show what was proposed in the conversation. Use
them as reference, not as the only proof that a claim is correct. Mark consequential
conclusions as confirmed, inferred, proposed, contradicted, or unresolved when useful.

## Avoid low-value review patterns

- Do not narrate every chat chronologically unless the user asks for a timeline.
- Do not stop at conversation counts, file locations, schemas, or extraction mechanics.
- Do not produce a topic list without explaining the relationships between topics.
- Do not treat repeated wording as separate problems when one underlying question fits.
- Do not repeat prior AI summaries without evaluating what they add, miss, or contradict.
- Do not use compaction summaries or subagent prompts as replacements for original user
  text when the original records remain available.
- Do not overwhelm the user with every branch; preserve only information that changes
  understanding, decisions, risk, or next action.

## Reporting contract

For a substantial Chinese review, aim for roughly 3,000–5,000 Chinese characters; use
equivalent depth in another language. Be deep but concise. Prefer five or six coherent
sections rather than a large catalog.

Use Markdown box-line diagrams when they clarify relationships, question clusters,
problem dimensions, or evolution. Use compact pseudocode when it explains the review
logic more clearly than prose. For example:

```text
conversations
  -> group workstreams
  -> cluster recurring questions
  -> map dimensions and contradictions
  -> review decisions and artifacts
  -> derive insights and next questions
```

Lead with the conclusion. A useful default report is:

1. **Original intent and current focus**: what the user asked and the real work underway.
2. **Question clusters and problem map**: the few underlying problems and relationships.
3. **Lineage and drift**: material changes across forks, subagents, and compaction.
4. **Decisions and artifacts**: what changed and what should be retained.
5. **New insights**: cross-session implications and reframings.
6. **Next questions or actions**: the smallest set that could materially advance work.

When drift matters, quote the decisive original clause or identify its exact message
reference, then show the later interpretation beside it. Do not reproduce every prompt
when a compact request set preserves the meaning.

## Completion criterion

The review is complete when the user can see the core value of recent AI collaboration,
understand the shape and evolution of the problem space, distinguish resolved from open
questions, verify that the original request set was preserved or see exactly where it
drifted, and gain at least one useful insight or next question that was not obvious from
reading one conversation alone.
