---
name: review-ai-conversations
description: Review and synthesize recent human-AI conversations across Claude Code, Codex, opencode, Grok Build, and Cursor. Use when the user wants to revisit work done with AI workers, summarize and cluster recurring questions, map the problem space, review prior AI replies and generated artifacts as reference material, compress long-running work across sessions, deepen understanding, brainstorm, or surface new insights and next questions. The user may specify agents, locations, time ranges, topics, analysis types, content to extract, or content to find.
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

Each source reference defines four required facts: the storage root, the recent/time
index and its units, root/child or fork identity, and the fields that contain the
user's question and visible AI reply. Preserve those facts when adapting to schema
changes.

For a request spanning several products, process each source independently, then merge
the clean human/assistant conversations at the analysis stage.

Freeze one UTC `[start, end]` window for the review. Use the product's documented
recent index to find candidates, then prefer the maximum accepted human-message or
visible AI-message timestamp as the conversation's real activity time. File mtime is
only a fallback when the store has no message or session clock.

## Read the conversation body

Recover the user's actual messages and the visible AI replies in conversational order.
Exclude tool calls, internal reasoning, system injection, copied parent history,
subagent chatter, host commands, and synthetic messages that were not typed by the
user or shown as an AI reply.

Prefer complete root conversations. Avoid counting forks, retries, copied context, or
subagents as independent lines of human thought. If a store has changed shape, inspect
the current fields and adapt instead of forcing an old parser model.

## Build the review

Use these lenses selectively:

- **Current work**: what the user has actually been trying to accomplish.
- **Workstreams**: distinct lines of work that are independent, related, or converging.
- **Question clusters**: repeated prompts that are different forms of one deeper issue.
- **Problem space**: dimensions, quadrants, sets, overlaps, dependencies, and exclusions.
- **Evolution**: earlier beliefs, later corrections, and why the mental model changed.
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

1. **Current focus**: the real work underway.
2. **Question clusters**: the few underlying problems behind many conversations.
3. **Problem map**: relationships, tensions, missing dimensions, and dependencies.
4. **Decisions and artifacts**: what changed and what should be retained.
5. **New insights**: cross-session implications and reframings.
6. **Next questions or actions**: the smallest set that could materially advance work.

## Completion criterion

The review is complete when the user can see the core value of recent AI collaboration,
understand the shape and evolution of the problem space, distinguish resolved from open
questions, and gain at least one useful insight or next question that was not obvious
from reading one conversation alone.
