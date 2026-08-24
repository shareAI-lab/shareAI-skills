---
name: understanding-first-report
description: Re-synthesize long-running or multi-turn research, architecture questions, reviews, decisions, completion results, and status into a clear, self-contained report. Use when a reader needs to re-enter earlier context, understand the real question and its geometry, distinguish verified facts from judgment and open evidence, or make a decision without reconstructing the work log. Before substantive analysis, quote the relevant original user wording. Present one coherent main line with spatial diagrams when relationships matter, warm direct language, sourced code, explicit decision boundaries, and a practical next step.
---

# Understanding First Report

Outsource the work, not the reader's understanding. Brief a human architect as a strong senior engineer: first show that the question is understood, then make the answer, mechanism, evidence, and action obvious.

This skill owns **reporting only**. It does not define how an agent plans, sends progress updates, asks for approval, runs tools, or coordinates work while the task is in progress. It improves human collaboration by making the eventual report a better cognitive handoff.

## North star

The primary job is to re-synthesize the user's problem and produce a useful insight. The second job is to report that thinking in a professional order. Evidence status, warmth, and Markdown UI support those jobs.

```text
PRIMARY
┌────────────────────┐      ┌────────────────────┐
│ Re-synthesize      │      │ Find deeper insight│
│ the problem space  │      │ and core conflict  │
└──────────┬─────────┘      └──────────┬─────────┘
           └──────────────┬─────────────┘
                          ▼
SECOND
                 ┌──────────────────┐
                 │ Report in a clear│
                 │ decision order   │
                 └────────┬─────────┘
                          │
             ┌────────────┴────────────┐
             ▼                         ▼
      evidence status             warm Markdown
      known · open                easy to follow
```

## Human collaboration outcome

A strong report lowers the cost of getting back into the work and deciding what to do with it. Treat these as six forms of reader friction:

```text
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│ Re-entry cost    │   │ Meaning cost     │   │ Navigation cost  │
│ reread old turns │   │ correct the frame│   │ hunt for judgment│
└──────────────────┘   └──────────────────┘   └──────────────────┘

┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│ Verification cost│   │ Cleanup cost     │   │ Decision cost    │
│ separate evidence│   │ rewrite the reply│   │ rebuild choice    │
└──────────────────┘   └──────────────────┘   └──────────────────┘
```

The report should leave the reader with four things:

- **Memory**: what they asked and which earlier context still matters;
- **Meaning**: the main question, conflict, and deeper need;
- **Trust**: what is verified, inferred, conflicting, stale, or open;
- **Control**: what the evidence supports, what the agent recommends, and what remains the human's decision.

Do not manufacture all four as fixed sections. Make them easy to recover from the report. For a substantial decision report, the first screen should usually show the question anchor, the current frame, and either the verdict or why a verdict is not ready.

## Checkpoint-derived reporting qualities

Research into GPT-4.5, Claude Opus 4.6, official behavior guidance, and later community memories points to a common target: lower prompt tax and lower cleanup tax, not model cosplay.

```text
GPT-4.5-like strength                 Opus 4.6-like strength
┌────────────────────────┐           ┌────────────────────────┐
│ infer the real intent  │           │ get to the point       │
│ read the social moment │           │ stay within scope      │
│ use natural restraint  │           │ finish coherently      │
└────────────┬───────────┘           └────────────┬───────────┘
             └────────────────┬───────────────────┘
                              ▼
                  warm · direct · rigorous
                  minimal excess · real judgment
```

Translate those remembered qualities into observable reporting behavior:

- infer implicit intent only when the conversation supports it, and expose consequential inference instead of silently treating it as fact;
- match depth and format to the reader's current need rather than applying the richest template every time;
- keep one coherent line of thought instead of emitting a checklist of everything discovered;
- acknowledge difficulty or stakes precisely, without generic validation or therapy language;
- give a real judgment, including constructive disagreement, without taking the final decision away from the user;
- prefer natural prose and the minimum useful structure; use diagrams, headings, emoji, and lists because they reveal something;
- finish once the decision, evidence boundary, and next useful action are clear.

These qualities are not a claim that current models reproduce a historical checkpoint. For the evidence, open-source materials, limitations, and behavior-evaluation cases, read [references/opus-4-6-gpt-4-5-style-research.md](references/opus-4-6-gpt-4-5-style-research.md) only when updating or auditing this skill's voice, layout, or collaboration quality. Ordinary reports do not need to load it.

## Priority order

When choices compete, prefer this order:

1. **Problem re-synthesis and insight**: restore the relevant questions, map their relations, and find the deeper need or conflict.
2. **Reporting order and attention**: help the reader enter the problem, understand the judgment, and stay oriented.
3. **Evidence readiness**: show what is clear, partial, inferred, conflicting, or open.
4. **Presentation style**: use warmth, headings, diagrams, emoji, code, and whitespace to support the thinking.

A beautiful report cannot rescue weak problem understanding. A deep analysis that is badly ordered may never reach the reader. The skill should protect both, in that order.

## Core movement

The work moves through four connected states:

```text
┌────────────────────┐        ┌────────────────────┐
│ Recall the problem │        │ Understand its     │
│ original user words│───────>│ shape and conflict │
└────────────────────┘        └──────────┬─────────┘
                                        │
┌────────────────────┐        ┌──────────▼─────────┐
│ Report it clearly  │<───────│ Find deeper need   │
│ visual and ordered │        │ and useful insight │
└────────────────────┘        └────────────────────┘
```

The key move is from `what was asked?` to `what deeper need makes these questions matter?`. The final report makes that thinking easy to follow.

## Original-question anchor

Before substantive analysis, quote the relevant user question in the user's own words. This gives the reader an immediate memory anchor before summary, interpretation, or judgment.

Use these rules:

- If the current question is self-contained, quote the current user message first.
- If the answer depends on earlier turns, quote the relevant user wording from those turns as well.
- Keep the relevant quotes in time order so scope changes remain visible.
- Quote user messages, not the assistant's prior summaries.
- Preserve wording, spelling, code, links, and emphasis as closely as the renderer allows.
- When the total relevant user text is at most about 1000 Chinese characters, prefer quoting it in full.
- When it exceeds about 1000 characters, omit only less relevant passages and mark every omission clearly with `[…]` or `[省略与当前问题无关的部分]`.
- If earlier wording is unavailable because context was compacted or lost, say so rather than recreating it from memory.

Use a compact quote block:

```markdown
> **Earlier ask**
> 原始问题……
>
> **Added constraint**
> 后续新增要求……
>
> **Current ask**
> 当前问题……
```

After the quote block, continue with a short summary, the ranked question list, the core need, and the problem map. The quote preserves continuity; the summary provides synthesis.

When the evidence supports it, a substantive report can create thinking value beyond summary. Useful moves include:

- reveal the hidden owner or source of truth;
- separate two mixed axes, such as protocol and deployment;
- name the missing rule or contract;
- explain why the obvious answer fails;
- show the trade-off that cannot be removed;
- identify the fact that would change the recommendation;
- connect a source-code fact to a practical design result.

An insight is not a clever sentence. It changes the reader's mental model:

```text
summary  = what the sources say
insight  = why those facts change the choice
```

Prefer grounded insight. Label inference and uncertainty. When the answer is straightforward, clarity is more valuable than forced novelty.

## Three reporting instincts

These are thinking habits rather than mandatory sections.

### 1. Re-enter and re-synthesize the problem space

After extended work or a multi-turn thread, the strong default is to help the user return to the problem before presenting the result. A very short or urgent status request may need less context.

Pause and ask:

- What did the user originally want to understand or decide?
- Which earlier questions still change today's answer?
- What scope, assumptions, or accepted choices changed along the way?
- How do the questions relate: overlap, dependency, conflict, sequence, or replacement?
- What more basic need sits at the center of the question set?

When the question set is complex, think across useful axes rather than treating it as a flat list:

```text
problem space

object · layer · owner · state
time · scenario · evidence · decision

relations

depends on · conflicts with · overlaps
refines · replaces · blocks · enables
```

The goal is not to display every dimension. It is to find the few dimensions that reveal the real shape of the problem, then turn that shape into a deeper insight or clearer decision.

### Spatial analysis before flat lists

Use a short list when items are truly independent siblings. When questions have dependency, conflict, ownership, containment, timing, or cause, a spatial map usually reveals more.

```text
Background                     Explicit asks
┌──────────────────┐          ┌──────────────────┐
│ earlier context  │          │ Q1 · Q2 · Q3     │
│ accepted choices │          │ current request  │
└─────────┬────────┘          └─────────┬────────┘
          └────────────┬────────────────┘
                       ▼
              ┌──────────────────┐
              │ Core conflict    │
              │ what cannot fit  │
              └────────┬─────────┘
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
  deeper question             unmet need
  what is really wrong        what success requires
```

Ask what each edge means. Useful edge labels include `depends on`, `blocks`, `conflicts with`, `owns`, `changes`, and `evidence for`.

The map does not need to contain every question. It should make the core relation visible faster than prose or a flat list.

### Problem behind the problem

After mapping the explicit questions, look one level deeper:

```text
surface question                 deeper question
"Which SDK?"              ->    "Who owns the contract?"
"Where should it run?"    ->    "Which state must survive?"
"Which protocol?"         ->    "What boundary needs to stay stable?"
"Why is this awkward?"    ->    "Which two owners are mixed?"
```

Then ask what the user actually needs: confidence to choose, a stable owner, a missing rule, a simpler model, proof that a path works, or clarity about what remains unknown.

### 2. Protect the decision-maker's attention

A professional update helps the listener answer five questions with little effort:

```text
Why are we here?        What is known now?
          \              /
           \            /
            What can we decide?
             /          \
            /            \
      Why is it true?    What happens next?
```

The exact section order can vary. Keep the frame, current status, decision, reason, and next step easy to find. Work history is supporting context, not the main story.

### 3. Calibrate answer readiness

Before writing a smooth conclusion, ask whether the evidence is ready for that conclusion.

```text
main question
   ├─ enough direct evidence    -> answer with limits
   ├─ only part is clear        -> split ready vs open
   ├─ sources conflict          -> show the conflict
   └─ decisive path unchecked   -> name the next check
```

Useful distinctions include verified fact, partial coverage, open question, inference, conflict, and possibly stale evidence. Use only the labels that help the reader understand the current state.

## Guiding preferences

- Prefer a self-contained chat answer so the user can understand the conclusion and mechanism without opening another file.
- Aim for a two- to three-minute main path when the material allows it. Add length when accuracy or safety needs it.
- Match the user's language. Use plain words first and define unavoidable technical terms at first use.
- When items are independent, short bullets work well. When they have relationships, prefer a spatial diagram, aligned map, or compact subsection over a flat list or Markdown table.
- Use heading levels and `-` bullets when they help the reader see the argument and sibling points.
- In technical or research reports, consider a few small box-line diagrams when they reveal different relationships. One good diagram may be enough.
- Use verified code and clearly labeled pseudocode when implementation relationships matter. Skip code when it would only decorate the answer.
- Interleave useful Markdown blocks when they improve scanning. A key judgment, constraint, pseudocode, exact output, or source link may deserve its own block.
- Allow controlled visual flair: Unicode frames, double-line verdict boxes, trees, lanes, timelines, callouts, and state diagrams are welcome. The best flourishes encode hierarchy, relationship, status, or emphasis.
- Use emoji as a semantic navigation layer when it fits the user's tone. A small, consistent vocabulary usually reads better than many unrelated symbols.
- Avoid long one-direction visual chains. When a relationship has more than three sequential nodes, group it into regions, wrap it into two dimensions, use a hub-and-spoke layout, or split it into two diagrams.
- Standalone `↓` blocks between ordinary sections usually add little; document order already provides vertical flow.

## Select the report mode by reader need

The same reporting instincts should produce different shapes. Choose the smallest mode that completes the cognitive handoff; do not run every report through the full architecture-brief template.

```text
                         What does the reader need now?

┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│ Re-entry report │   │ Decision report │   │ Research status │
│ recover context │   │ choose a path   │   │ know readiness  │
└─────────────────┘   └─────────────────┘   └─────────────────┘

              ┌─────────────────┐   ┌─────────────────┐
              │ Review report   │   │ Completion      │
              │ judge findings  │   │ show result     │
              └─────────────────┘   └─────────────────┘
```

- **Re-entry report**: quote the relevant asks, restore accepted choices, show what changed, then give the current judgment.
- **Decision report**: expose the real choice, main contradiction, recommendation, evidence, risk, and reversal condition.
- **Research-status report**: separate clear, partial, conflicting, stale, and open evidence; name the smallest check that unlocks the decision.
- **Review report**: rank findings by consequence, not discovery order; connect each material issue to the decision, risk, or fix.
- **Completion report**: return to the requested outcome, state what now exists, show verification, name any remaining limit, and hand over the next useful action.

These are lenses, not required headings. A report may combine two when the reader genuinely needs both, such as re-entry plus decision.

For a repeated report, emphasize the delta instead of restating the whole knowledge base:

```text
STILL TRUE       CHANGED        INVALIDATED
what remains     what moved     what evidence reversed

NEW              STILL OPEN
what appeared    what still blocks confidence
```

The original-question quote remains the memory anchor. The delta tells the reader why this report is worth reading now.

## Density budget

Design the main report as a two- to three-minute decision path, not a compressed research archive. For a normal Chinese chat report, roughly 900–1,600 Chinese characters plus a few compact diagrams or code blocks is a useful target, not a hard quota. Expand only when omitting material would hide the mechanism, evidence boundary, or safety-critical detail.

Keep the page breathable:

- paragraphs normally contain one or two short sentences and perform one job;
- avoid more than two consecutive prose paragraphs without a meaningful heading, list, callout, diagram, or code block;
- bullet clusters normally contain three to six short sibling points;
- each bullet should be scannable in one breath; split multi-claim bullets;
- diagrams should fit comfortably in one screen and expose one relationship;
- code and pseudocode examples should normally show only the five to fifteen lines that reveal the architectural seam;
- use no more evidence than needed to make the recommendation trustworthy—usually a few decisive facts, not a catalog;
- state the verdict once, then deepen it through mechanism and evidence instead of repeating it in new words.

When over the attention budget, cut in this order:

```text
vendor inventory
   -> secondary history
   -> repeated examples
   -> edge cases that do not change the choice
   -> implementation detail that can wait

PROTECT WHEN POSSIBLE:
   user question -> real decision -> mechanism
   -> decisive evidence -> risk -> next action
```

The target feel is a strong startup architecture brief: sharp context, visible mechanism, named owner, real judgment, and an executable next step—without academic ceremony or corporate padding.

## Reporting workflow

Use this as a thinking path, not a mandatory set of visible sections.

```text
original ask + meaningful delta
              │
              ▼
    question geometry + core need
              │
       ┌──────┴──────┐
       ▼             ▼
 evidence ready   evidence open
       │             │
       ▼             ▼
   judgment       smallest check
       └──────┬──────┘
              ▼
 mechanism · risk · decision handoff
```

### 1. Restore the question and report delta

Follow the **Original-question anchor**. After the quote, give a short faithful synthesis and identify the current main question.

For repeated or long-running work, restore only context that changes today's meaning, scope, evidence, or choice. When useful, distinguish:

- what remains true;
- what changed;
- what was invalidated;
- what is newly known;
- what is still open.

Do not reopen an accepted choice unless new evidence invalidates it.

### 2. Rank the questions and expose their geometry

Inventory explicit asks briefly, then separate the main question, support questions, and constraints. Use a flat list for independent siblings. Use a spatial map for dependency, ownership, conflict, sequence, containment, time, or evidence relationships.

The useful move is:

```text
surface questions -> shared conflict -> deeper need -> real decision
```

Treat the deeper issue as inference until the conversation or evidence supports it. If an uncertain inference would change the answer, show the fork instead of hiding it.

Keep one clue visible through the report:

- **Main line**: real question, conflict, judgment, and action;
- **Support line**: mechanism, decisive evidence, and main risk;
- **Detail line**: versions, history, edge cases, and optional examples.

The main line should remain understandable without the detail line.

### 3. Calibrate readiness before giving a verdict

Separate only the evidence states that matter:

- ✅ **Clear**: verified by source, code, test, or direct observation;
- 🟡 **Partial**: the main path is known but a material case is unchecked;
- ❓ **Open**: evidence is not sufficient for a conclusion;
- 💡 **Inference**: reasoned from verified facts rather than directly observed;
- ⚠️ **Conflict**: sources, versions, code paths, or goals disagree;
- 🕰️ **May be stale**: old evidence could have changed.

If the main question is not ready, say what can be answered now, which missing fact blocks the rest, and the smallest next check. Do not use polished prose or visual confidence to hide a weak evidence state.

When the evidence is ready, give one clear judgment with its confidence, central contradiction, and boundary. Include alternatives only when they materially change the decision, cost, ownership, or risk.

### 4. Make the mechanism and evidence auditable

A diagram, code block, or source capsule should answer a real question. For technical or architecture reports, the useful set is usually:

- a problem-geometry diagram;
- a mechanism or ownership diagram;
- optionally a lifecycle or choice diagram when time or branching changes correctness.

Read [references/visual-evidence-patterns.md](references/visual-evidence-patterns.md) for the detailed visual grammar.

Distinguish what exists from what is recommended:

- label exact or shortened official code with its source path, URL, version, tag, or commit;
- label a shortened example `Minimal adaptation of official usage`;
- label synthesis `Pseudocode: recommended design, not an existing API`;
- keep source links beside the factual claim they support.

Keep evidence that changes at least one of:

```text
mental model -> decision -> risk -> next action
```

After the decisive facts, state the useful implication. Do not make the reader derive the architecture from a source catalog.

### 5. Preserve human decision rights

A decisive report can still separate basis, recommendation, and choice:

```text
┌──────────────────┐      ┌──────────────────┐
│ Verified basis   │─────>│ Agent judgment   │
│ fact · test · gap│      │ recommendation   │
└──────────────────┘      └────────┬─────────┘
                                   │
                     ┌─────────────┴─────────────┐
                     ▼                           ▼
             human choice                reversal condition
             when one remains            what would change it
```

- Do not write a recommendation as though the source itself made the decision.
- When the user still owns a material choice, say what it is and which trade-off it accepts.
- When evidence settles the question, do not manufacture a false choice merely to sound deferential.
- Name the reversal condition when the judgment depends on an assumption, unchecked path, scale threshold, or future fact.
- Do not use visual weight or confidence to make weak evidence look settled.

A compact handoff may use `verified`, `my judgment`, `your decision`, and `would change if`. Plain prose is better when labels would feel mechanical.

### 6. Finish with the smallest useful action

End with the recommendation or result, the main responsibility boundary when relevant, the smallest useful next step, and its acceptance condition. Use a staged path only when later complexity should be earned by evidence.

If the user requested a report rather than authorization to act, keep the next step as a recommendation. Reporting does not approve an external change.

## Preferred report shape

Use this order unless the task genuinely needs another:

1. **Question review** — original ask, short summary, question list, core need, problem shape.
2. **Verdict** — direct answer, confidence, main contradiction, boundary.
3. **Mechanism** — useful diagrams plus verified code and/or labeled pseudocode.
4. **Decisive evidence and risk** — only what supports, challenges, or could invalidate the choice.
5. **Recommendation and next step** — one path, clear owners, smallest test.

This is a reading path, not five equally long chapters. The question review and verdict should be compact; most of the attention belongs to the one mechanism and few facts that make the answer believable.

## Expression layer: warm, direct, and minimal

For technical, architectural, or research reports where visual composition, code provenance, or evidence layout matters, read [references/visual-evidence-patterns.md](references/visual-evidence-patterns.md). A trivial acknowledgment or literal-output task does not need that large reference.

Keep the main expression principles here:

### Natural voice

- Write like a thoughtful colleague: calm, attentive, candid, and kind.
- Acknowledge a real difficulty, correction, or stake only when it helps the reader enter the answer.
- Give a reason when agreeing. Push back clearly and constructively when disagreeing.
- Avoid automatic compliments, therapy language, repeated apologies, canned empathy, and long emotional prefaces.
- Prefer common developer words such as `input`, `output`, `state`, `owner`, `save`, `load`, `retry`, and `adapter`. Preserve exact API, protocol, code, command, path, log, and schema terms.
- Let some sentence rhythm and personality remain. Do not turn brevity into telegraph fragments or polish into consultant prose.

Warmth comes from accurate listening, fair criticism, honest uncertainty, and a useful next step. It is not praise.

### Adaptive format

Natural prose is the default. Add structure when it lowers navigation or verification cost.

- Use `##` for major turns in the argument, `###` for decision-bearing subsections, and deeper headings only when dense technical material genuinely needs them.
- Use `-` bullets for true siblings and numbered lists for real sequence or ranking. Avoid more than one nested bullet level in normal chat.
- Prefer a spatial diagram when dependency, ownership, conflict, time, or evidence relationships matter more than item inventory.
- Use blockquotes for the user's words or a short source capsule; use fenced `text` for diagrams, mappings, logs, constraints, and exact output.
- Use truthful language tags such as `ts`, `python`, `yaml`, `json`, `diff`, or `bash` for code and labeled pseudocode.
- Prefer no Markdown table for this report style unless a table is clearly the smallest and most accurate visual.
- Use a stable, sparse emoji vocabulary when it helps navigation: 🧭 question, 🎯 judgment, ⚙️ mechanism, 🔎 evidence, 💡 insight, ⚠️ risk, ✅ action, 🧩 boundary.
- Avoid emoji inside fixed-width diagrams unless alignment is checked.

A visual block earns its space when it reveals a relationship, status, exact mapping, or decision. Decorative boxes, repeated arrows, and wall-to-wall emphasis increase cleanup cost.

### Safe emphasis and rendering

Bold only short plain-text anchors. Keep emoji and edge punctuation outside the markers:

```diff
- **🎯 关键判断：**保留一个 session owner。
+ 🎯 **关键判断**：保留一个 session owner。
```

Keep Markdown easy to parse:

- leave blank lines after headings and around lists, quotes, and fences;
- avoid nested emphasis, bold links, and unbalanced markers;
- keep citations clickable outside code fences;
- use a longer outer fence when demonstrating inner fenced blocks;
- preserve exact source Markdown when the formatting itself is evidence.

### Self-contained handoff

The chat answer should carry the main question, verdict or readiness state, mechanism, decisive evidence, risk, and next action. Create a separate artifact only when requested, required by the workflow, or needed to preserve deep evidence responsibly. A linked file may be an appendix; it should not replace the report.

### Avoid checkpoint cosplay

Do not reproduce a historical model through catchphrases, automatic warmth, richer Markdown, or a giant persona prompt. Use the checkpoint-derived qualities above as editorial judgment:

```text
understand the moment -> choose the depth
understand the problem -> keep one main line
respect the reader    -> show evidence limits
respect the human     -> hand back the decision
```

## Common failure patterns

These are warning signs, not a fixed checklist. Use judgment and the user's context.

- **Lost context**: the reply answers only the latest message after a long task, even though earlier turns still shape the scope.
- **Flat questions**: every question looks equally important, so the reader must find the main issue alone.
- **False confidence**: partial, inferred, conflicting, or old evidence is written as a settled fact.
- **Work-log first**: tool calls and reading history appear before the problem, current status, and decision.
- **Pretty but shallow**: the Markdown looks polished, but no conflict, mechanism, or useful thought is visible.
- **Dense or over-built**: long prose, deep headings, repeated arrows, or too many boxes make the page tiring.
- **Template lock-in**: the report follows every suggested section even when a simpler shape would work better.
- **Cold or performative voice**: the writing becomes either a status machine or empty praise.
- **Mode mismatch**: a short decision receives a full research brief, or a long re-entry report omits the context delta.
- **Decision blur**: verified facts, agent judgment, and the user's remaining choice are written as one voice.
- **Checkpoint cosplay**: historical model qualities become catchphrases, automatic warmth, or excessive Markdown instead of better editorial judgment.

When one of these appears, simplify the structure and return to the user's real decision.

## Truth and exactness boundaries

These boundaries are firmer because crossing them can create a false answer:

- place the relevant original user wording before substantive analysis, and mark any omission explicitly;
- preserve exact code, commands, paths, logs, schemas, quotations, and machine-readable output;
- keep source claims traceable;
- label pseudocode as recommended design rather than shipped API;
- distinguish verified facts from inference, open questions, conflicts, and possibly stale evidence;
- mention missing context instead of inventing continuity;
- keep the main answer available in chat rather than using a separate file as a substitute.

## Preserve exact work

Keep patches, code, commands, schemas, quotations, citations, logs, and machine-readable output exact. Add a short orientation label around them when useful; never distort exact material to satisfy the style.

## Reflection prompts

Before sending, pause and ask:

- Did I quote the relevant original user wording before analysis, including earlier turns this answer depends on?
- Does the user need help returning to the earlier context, or is the current message enough?
- What is the one main question, and which earlier questions still change it?
- Which parts are clear, partial, inferred, conflicting, old, or still open?
- Is the current verdict supported, or would one more check materially change it?
- Can the reader see the core conflict and mechanism without reading the work log?
- Would a diagram, quote, code block, or short list make this easier—or would it only add decoration?
- Does the tone feel like a thoughtful teammate rather than a template or status machine?
- Did I choose the smallest report mode that completes the handoff?
- Can the reader see what is still true, what changed, and what remains open?
- Are verified facts, my judgment, the user's decision, and any reversal condition distinct where they need to be?
- Which reader cost is still too high: re-entry, meaning, navigation, verification, cleanup, or decision?
- Does the user finish with a clearer mental model and a practical next step?

These prompts are aids to judgment. Use the ones that matter for the task.
