---
name: review-ai-conversations
description: Review recent human-AI conversations across Claude Code, Codex, opencode, Grok Build, and Cursor according to the user's requested locations, time range, focus, extraction targets, and report type. Use when the user wants to revisit, recover, search, summarize, compare, or understand work spread across AI workers and sessions. Can optionally cluster questions, map the problem space, review documents and AI conclusions, detect intent drift, or derive insights; handles forks, subagents, compaction, and Store drift as extraction concerns.
---

# Review AI Conversations

Help the user review the actual conversation bodies from long-running work with AI
workers. Follow what the user asked to analyze, extract, find, or report. Deeper
synthesis—question clustering, problem-space mapping, drift review, or new insights—is
available when requested or clearly useful, but is not a mandatory pipeline.

## Accept natural-language scope

The user may freely specify any combination of:

- **Agents or locations**: one client, several clients, a project, or explicit paths.
- **Time range**: recent hours, days, weeks, calendar dates, or named conversations.
- **Analysis focus**: architecture, progress, decisions, recurring problems, or one topic.
- **Analysis type**: review, summary, comparison, clustering, problem map, or insights.
- **Content to extract**: prompts, replies, conclusions, artifacts, or open questions.
- **Content to find**: a phrase, proposal, changed belief, missing answer, or document.

Do not require store schemas, session IDs, or a rigid command format. Infer reasonable
scope from ordinary language. Ask only when two interpretations would materially
change the conversations or conclusions included.

## Start with the requested review

```text
conversation bodies
        │
        ▼
faithful review, extraction, search, or summary requested by the user
        │
        ├─ optionally cluster questions and workstreams
        ├─ optionally map dimensions, sets, dependencies, or tensions
        ├─ optionally review documents, AI conclusions, decisions, or drift
        └─ optionally derive insights, open questions, or alternative frames
```

The user's original messages are the authority for intent. AI replies, compaction
summaries, and AI-generated reports are useful evidence of what was understood or
proposed, but they are not independent proof that the interpretation or conclusion is
correct.

## Load only the extraction guidance needed

When the user supplies conversation text directly, analyze it without loading Store
references.

When reading local stores:

1. Read [`references/retrieval.md`](references/retrieval.md) for the shared efficient
   retrieval and schema-drift rules.
2. Read only the matching product reference:
   - Claude Code: `references/sources/claude-code.md`
   - Codex: `references/sources/codex.md`
   - opencode: `references/sources/opencode.md`
   - Grok Build: `references/sources/grok-build.md`
   - Cursor: `references/sources/cursor.md`
3. If parent/fork/subagent/summary markers, copied prefixes, multiple context epochs,
   or suspected intent drift appear, also read
   [`references/lineage-and-intent.md`](references/lineage-and-intent.md).

Do not load unrelated product references. For several products, recover each Store
family independently and combine their conversation capsules only at analysis time.

## Optionally cluster the user's real questions

Use this lens when the user requests clustering, recurring themes, a synthesis of
long-running work, or when repeated questions obscure the main concerns. Recover each
accepted human-authored request before trusting later summaries. Split a long prompt
into question atoms only when that helps reveal structure. Preserve the original text
or an exact message reference beside the normalized form.

Cluster by the underlying decision, unknown, or tension—not merely repeated words.
Two differently worded prompts may be one problem; two prompts sharing vocabulary may
belong to different workstreams. For each cluster, identify:

- what the user is ultimately trying to understand, decide, or build;
- the constraints, exclusions, assumptions, and examples that shape the answer;
- which conversations extend, correct, fork, or repeat earlier work;
- what is resolved, contradicted, partly answered, or still absent.

Prefer the fewest clusters that preserve meaningful differences. Do not compress away
a detail merely because later AI summaries ignored it.

## Optionally map the problem space

Use this lens when the user asks how questions relate, wants dimensions or quadrants,
or needs a clearer system model. Make relationships explicit rather than producing a
topic catalog. Choose the smallest useful representation:

- **Dimensions** for independent variables along which answers change.
- **Quadrants** only when two genuinely independent axes create four meaningful cases.
- **Sets** for membership, overlap, subset, exclusion, and uncovered cases.
- **Layers** for abstraction, ownership, or implementation boundaries.
- **Dependencies or sequence** when one question must be answered before another.
- **Tensions** when satisfying one need weakens another.

Ask whether the chosen dimensions are independent, whether cases are missing, and
whether two apparent dimensions are actually the same concern at different layers.
The goal is a compact problem model the user can think with, not a decorative diagram.

## Optionally review documents, AI replies, and decisions

Use this lens when artifacts, prior conclusions, or work progress matter. Collect recent
documents, code, reports, plans, and decisions mentioned or produced in the selected
conversations. Inspect the actual artifact when available instead of relying only on
an AI statement that it exists or says something.

Attach each artifact or consequential AI conclusion to the question cluster it serves.
Judge whether it supports, extends, contradicts, supersedes, or leaves the question
unresolved. Distinguish clearly:

```text
truth about user intent   -> original human messages outrank AI summaries
truth about produced work -> actual document or code outranks a chat claim
truth about external facts -> primary evidence outranks an AI report
```

Treat AI replies as proposals and prior reasoning worth reviewing. Repetition across
AI workers is not independent confirmation when they inherited the same summary or
copied context.

## Optionally derive insights and open minds

Use this lens only when the user asks for insights, brainstorming, reframing, open
questions, or a deeper synthesis—or when one genuinely decision-relevant connection is
worth surfacing briefly. An insight should expose a useful relationship not obvious
from one conversation: two clusters may share a hidden constraint, a rejected idea may
solve a different quadrant, or repeated trouble may reveal a misplaced boundary.

For each important insight, make the derivation inspectable:

```text
observations across conversations
  -> relationship or contradiction
  -> why it changes understanding
  -> decision, experiment, or next question it enables
```

Use **open minds** to offer a small number of alternative frames, counterexamples, or
experiments that could unlock the work. Do not generate a brainstorm dump disconnected
from the recovered question space. Do not add this section merely to satisfy a template.

## Avoid low-value review

- Do not narrate every conversation chronologically unless a timeline is requested.
- Do not stop at session counts, filenames, extraction mechanics, or a topic list.
- Do not treat AI summaries or generated documents as the only trusted source.
- Do not invent quadrants whose axes are not independent or whose cells add no value.
- Do not flatten forks, subagents, and repeated compaction into duplicate human intent.
- Do not repeat old AI conclusions without testing what they add, miss, or contradict.
- Do not force clustering, diagrams, insights, open minds, or next actions when the user
  requested a simpler recovery, extraction, search, or summary.
- Unless exact recovery was requested, do not preserve every detail equally; retain
  what changes understanding, decisions, risk, or the user's stated purpose.

## Reporting contract

Follow the user's requested output and level of depth first. For a substantial
synthesis, lead with the conclusion and keep reading pressure low. Roughly 3,000–5,000
Chinese characters is usually enough; use equivalent depth in another language.
Prefer five or six coherent sections when that structure fits.

Use Markdown box-line diagrams for problem relationships and compact pseudocode for
review logic. Avoid Markdown tables unless exact repeated-field comparison genuinely
needs one.

A substantial synthesis may use the following structure, but include only sections
that serve the user's request:

1. **Original intent and current focus**
2. **Question clusters and workstreams**
3. **Problem-space map**
4. **Documents, conclusions, decisions, and drift**
5. **New insights and open minds**
6. **The few next questions or actions that matter**

The review is complete when it faithfully satisfies the requested scope and gives the
user a clearer, evidence-aware account of the selected conversations. Question maps,
drift analysis, insights, and next actions are completion criteria only when the user
requested them or they are necessary to answer the stated purpose.
