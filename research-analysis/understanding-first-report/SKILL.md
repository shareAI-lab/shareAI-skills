---
name: understanding-first-report
description: Re-synthesize long-running or multi-turn research, agent work, architecture questions, reviews, decisions, and status into a clear problem space, deeper insight, and professional report. Use after extended work to reconnect earlier questions, find their core need and conflict, calibrate what is known or still open, then present the result in an attention-friendly order with warm language, clean Markdown, sourced code, and a practical next step.
---

# Understanding First Report

Outsource the work, not the reader's understanding. Brief a human architect as a strong senior engineer: first show that the question is understood, then make the answer, mechanism, evidence, and action obvious.

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

## Priority order

When choices compete, prefer this order:

1. **Problem re-synthesis and insight**: restore the relevant questions, map their relations, and find the deeper need or conflict.
2. **Reporting order and attention**: help the reader enter the problem, understand the judgment, and stay oriented.
3. **Evidence readiness**: show what is clear, partial, inferred, conflicting, or open.
4. **Presentation style**: use warmth, headings, diagrams, emoji, code, and whitespace to support the thinking.

A beautiful report cannot rescue weak problem understanding. A deep analysis that is badly ordered may never reach the reader. The skill should protect both, in that order.

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
- Prefer short bullets, aligned mappings, diagrams, or compact subsections over Markdown tables.
- Use heading levels and `-` bullets when they help the reader see the argument and sibling points.
- In technical or research reports, consider a few small box-line diagrams when they reveal different relationships. One good diagram may be enough.
- Use verified code and clearly labeled pseudocode when implementation relationships matter. Skip code when it would only decorate the answer.
- Interleave useful Markdown blocks when they improve scanning. A key judgment, constraint, pseudocode, exact output, or source link may deserve its own block.
- Allow controlled visual flair: Unicode frames, double-line verdict boxes, trees, lanes, timelines, callouts, and state diagrams are welcome. The best flourishes encode hierarchy, relationship, status, or emphasis.
- Use emoji as a semantic navigation layer when it fits the user's tone. A small, consistent vocabulary usually reads better than many unrelated symbols.
- Avoid long one-direction visual chains. When a relationship has more than three sequential nodes, group it into regions, wrap it into two dimensions, use a hub-and-spoke layout, or split it into two diagrams.
- Standalone `↓` blocks between ordinary sections usually add little; document order already provides vertical flow.

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

## 1. Reconstruct and rank the question before reporting

A short **Question review** before the verdict is usually helpful, especially after long or multi-turn work. A useful shape is:

1. **Quote the original ask**
   - If the user's question is 500 Chinese characters or fewer, reproduce it verbatim in a blockquote or compact quote block so it is visually distinct from the answer.
   - If it is longer, say that the original is long and skip the full quote. Preserve the exact decision-bearing phrases in the next summary.
   - For follow-up reports, quote only the current request, not the entire conversation.
2. **Give a faithful short summary**
   - Restate the request in one or two warm, plain sentences.
   - Preserve named systems, constraints, expected output, and the decision the user must make.
3. **List the user's questions**
   - Separate explicit questions from inferred ones.
   - Group duplicates and closely related questions.
   - Mark each item as `main question`, `support question`, or `constraint` when priority is not obvious.
4. **State the core need**
   - Explain what the user is really trying to understand, choose, fix, or make safe.
   - Name the success test: what must become clear or work before the answer is useful.
5. **Map the problem shape and deeper issue**
   - Map the important objects as nodes and their dependency, ownership, sequence, or conflict as edges.
   - Expose mixed axes such as protocol vs deployment, runtime vs product, identity vs state, or current implementation vs plan.
   - Identify the more basic issue behind the surface questions: main owner, source of truth, missing rule, broken boundary, or hard trade-off.

Labels such as `explicit`, `inferred`, and `unresolved` can help when intent is not directly stated. Avoid inventing hidden motives. If an uncertain inference would change the answer, show the fork.

Use a compact problem map when the question has several related parts:

```text
┌───────────────┐      ┌────────────────┐
│ Named objects │─────>│ Asked mechanics│
└───────┬───────┘      └───────┬────────┘
        │                       │
        ▼                       ▼
┌───────────────┐      ┌────────────────┐
│ Mixed axes    │─────>│ Real decision  │
└───────────────┘      └────────────────┘
```

Replace the generic labels with the user's actual systems and relationships. The diagram is not a research plan; it should reveal why the question has its current shape.

## Clue hierarchy and progressive reveal

Look for one main clue that can organize the report. Other material can support it, limit it, or move into a detail lane.

```text
┌──────────────────┐        ┌──────────────────┐
│ User question 1  │        │ User question 2  │
└─────────┬────────┘        └─────────┬────────┘
          └────────────┬──────────────┘
                       ▼
              ┌──────────────────┐
              │ Core need        │
              │ main question    │
              └────────┬─────────┘
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
   support clues               constraints
   mechanism · facts           risk · limits
```

Use three levels:

- **Main line**: the real question, core conflict, verdict, and next action;
- **Support line**: mechanism, decisive evidence, and main risk;
- **Detail line**: versions, secondary sources, edge cases, and optional examples.

Ideally, the main line remains understandable without the detail line. Support clues answer `why is the verdict true?` or `how does it work?`. Details that do not change the decision, risk, or action can usually move out of the main path.

Reveal information in a clear order:

```yaml
# PSEUDOCODE
report:
  first_screen:
    - user_ask
    - question_summary
    - question_list
    - core_need

  main_line:
    - core_conflict
    - verdict
    - mechanism

  support:
    - key_evidence
    - main_risk
    - useful_insight

  finish:
    - next_action
```

Use short signposts to keep the clue visible: `先说主线`、`这几个问题其实指向同一个需求`、`为什么这样判断`、`这意味着`、`最后落到行动上`. Use them naturally, not as a fixed template.

## Long-run re-entry

When research, tool work, or background agents have taken a long time, consider the next reply a context re-entry. The user may no longer remember the full ask, and the latest message may not contain the whole scope.

Useful context to recover includes:

- the original user ask;
- earlier questions that still affect the current decision;
- later scope changes and corrections;
- choices the user already accepted or rejected;
- promised outputs and success checks;
- current evidence, files, code, and test results;
- the latest user message.

Rather than replaying the whole conversation, compress the relevant parts into a short decision record:

```yaml
# PSEUDOCODE
context_reentry:
  original_goal: what_started_the_work
  added_questions: what_changed_the_scope
  accepted_choices: what_is_already_decided
  current_question: what_needs_an_answer_now
  open_items: what_is_still_unresolved
```

When older and newer requests differ, it helps to say so. The latest request is usually current, while older context may still matter when it changes meaning, constraints, or ownership.

If conversation context is missing, compacted, or uncertain, mention the gap instead of guessing at continuity.

Use a short re-entry block near the top:

> **Where we left off**
> The original goal was …
> Later, the scope added …
> This report now answers …

The re-entry is most useful when it helps the user return to the work in seconds without becoming a meeting transcript.

## Research status and answer readiness

Before giving a final judgment, it often helps to separate what is known from what is not.

- ✅ **Clear**: verified by source, code, test, or direct observation;
- 🟡 **Partial**: some evidence exists, but an important path or case is not checked;
- ❓ **Open**: not researched enough to support a conclusion;
- 💡 **Inference**: a reasoned result from verified facts, not a direct implementation fact;
- ⚠️ **Conflict**: sources, versions, code paths, or user goals disagree;
- 🕰️ **May be stale**: older evidence that could have changed.

Use this compact status shape when several questions remain:

```markdown
### 当前调研状态

- ✅ **已查清**：核心调用路径和 state owner。
- 🟡 **部分清楚**：断线恢复只验证了单实例。
- ❓ **仍待确认**：多实例下的 event replay。
- 💡 **当前判断**：先不拆新的 store。
```

If a main question is not ready, avoid forcing an answer from weak evidence. Consider:

- say `目前还不能可靠下结论`;
- explain which missing fact blocks the decision;
- state the smallest next check;
- answer the parts that are ready;
- keep assumptions visible.

Keep uncertainty visible. A professional report makes the decision boundary clear without making the writing feel defensive.

## Professional update order

For a leader, boss, or decision group, a useful top-down update often includes:

- **Context return**: what problem and earlier decisions matter now;
- **Question map**: main question, support questions, and constraints;
- **Current status**: clear, partial, open, inferred, or conflicting;
- **Verdict**: what can be decided now, with confidence and limits;
- **Mechanism**: why the result is true;
- **Risk and blocker**: what may change or stop the plan;
- **Next action**: owner, check, and expected result.

This order often protects attention well. It gives the listener the frame before detail, the answer before work logs, and the remaining uncertainty before commitment. Adapt it when another order serves the decision better.

## 2. Give the verdict and main contradiction

After the question review, lead the report itself with:

- the direct answer or chosen architecture;
- confidence and important uncertainty, if any;
- the main contradiction: why the obvious or fashionable answer is incomplete;
- the boundary that resolves the contradiction.

Avoid making the reader infer a choice from a vendor list, feature inventory, or chronology. One recommendation is often clearer; include alternatives when they materially change the decision.

Give the central judgment its own compact callout or verdict box when doing so makes the first screen easier to scan:

```text
╔══ KEY JUDGMENT ═══════════════════════════╗
║ Choose the boundary, not the fashionable ║
║ framework shape.                         ║
╚═══════════════════════════════════════════╝
```

## 3. Explain the mechanism visibly

For technical or research reports where visuals, code, or evidence layout matter, read [references/visual-evidence-patterns.md](references/visual-evidence-patterns.md). It is usually unnecessary for a trivial acknowledgment or literal-output task.

For substantive architecture reports, normally use:

- one **problem-geometry diagram** showing how the user's questions relate;
- one **mechanism or ownership diagram** showing how the recommended system actually works;
- optionally one **lifecycle or decision diagram** when pause/resume, retry, migration, failure, or staged adoption is central.

Each diagram is most useful when it answers a different question and replaces prose. Prefer box-line diagrams over Mermaid for this style.

Prefer spatial composition over a single long axis:

- left/right for peers, alternatives, producer/consumer, or before/after;
- top/bottom for real lifecycle or dependency;
- center/outward for one owner serving several concerns;
- nested regions for true containment;
- two short diagrams instead of one seven-node chain.

Use Markdown blocks as semantic components, not only as containers for executable code:

- blockquote for the user's original words, a short verified quotation, or a clickable source capsule;
- fenced `text` block for a verdict card, exact mapping, constraint set, timeline, or box-line diagram;
- language-tagged fence for verified source code;
- a syntax-highlighted fence such as `ts`, `python`, `yaml`, `json`, `diff`, or `bash` for pseudocode, chosen to match the idea's structure;
- ordinary prose between blocks to explain why the block changes the decision.

Keep source links outside code fences when they should remain clickable. A fenced block may show an exact URL only when literal output is the evidence.

Reserve plain `text` fences for box-line diagrams, exact mappings, logs, timelines, constraints, and literal output. For pseudocode, prefer a color-rich language tag and put `Pseudocode: recommended design, not an existing API` immediately above the block. When useful, repeat `// PSEUDOCODE`, `# PSEUDOCODE`, or an equivalent comment on the first line so the distinction survives copying.

Choose the closest visual grammar:

- `ts` for typed interfaces, event streams, adapters, async flows, and ownership contracts;
- `python` for linear algorithms, branching, retries, and orchestration;
- `yaml` for declarative policy, responsibility, configuration, and staged plans;
- `json` for payloads, schemas, protocol messages, and structured state;
- `diff` for before/after decisions or proposed changes;
- `bash` for exact or proposed command sequences.

Choose a language tag that matches the idea rather than selecting one only for color. Syntax highlighting should reinforce meaning.

Use concrete code proactively when it reveals the real call relationship, state boundary, or event flow more clearly than prose:

- label exact or shortened official code with its source path or URL and version, tag, or commit when available;
- label a shortened example `Minimal adaptation of official usage`;
- label synthesis `Pseudocode: recommended design, not an existing API`;
- never present convenient pseudocode as a shipped framework API.

When both are useful, show a small verified code excerpt for **what exists** and a small pseudocode excerpt for **what you recommend adding**. Keep each block focused on one architectural point.

## 4. Filter evidence for the decision

Include a point only if it changes at least one of:

```text
mental model -> decision -> risk -> next action
```

Separate `verified implementation fact`, `official claim`, `community signal`, `inference`, and `unresolved` when the distinction matters. Prefer decisive source relationships over exhaustive citations. Move secondary history, vendor inventories, and edge-case evidence out of the main reading path.

Put a decisive source or compact evidence bundle in a callout when it deserves visual weight:

> **Verified source**
> [Official API documentation](https://example.com) — supports the call relationship shown above.

Name the few risks that could invalidate the choice. Explain the failure mechanism, not just the risk label.

After the decisive facts, state the useful thought they support:

- **Observation**: what is verified;
- **Conflict**: what does not fit or cannot both be true;
- 💡 **Insight**: what the conflict reveals;
- 🎯 **Decision**: how that changes the architecture or next step.

## 5. End with one actionable path

Finish with:

- one recommended architecture or decision;
- the owner and boundary of each important responsibility;
- the smallest next step that tests the recommendation;
- a staged path only when later complexity should be earned by evidence.

The reader should know what to do next without reconstructing tasks from the rest of the report.

## Preferred report shape

Use this order unless the task genuinely needs another:

1. **Question review** — original ask, short summary, question list, core need, problem shape.
2. **Verdict** — direct answer, confidence, main contradiction, boundary.
3. **Mechanism** — useful diagrams plus verified code and/or labeled pseudocode.
4. **Decisive evidence and risk** — only what supports, challenges, or could invalidate the choice.
5. **Recommendation and next step** — one path, clear owners, smallest test.

This is a reading path, not five equally long chapters. The question review and verdict should be compact; most of the attention belongs to the one mechanism and few facts that make the answer believable.

## Heading and list grammar

Use headings as navigation, not decoration:

- In chat, major sections can usually begin with `##`; a separate `#` title is often unnecessary.
- Use `###` for a decision-bearing subsection inside one major section.
- Use `####` only when a dense technical section genuinely needs one more level. Avoid deeper headings.
- Keep headings short and concrete: `## Verdict`, `### Session owner`, `### Why the obvious path fails`.
- Leave a blank line after every heading before prose, lists, quotes, or blocks.

Use CommonMark `-` bullets actively for sibling points:

- one bullet carries one claim, owner, constraint, consequence, or action;
- begin with a bold lead-in when the list needs fast scanning, such as `- **Owner**: Native runtime`;
- nest at most two bullet levels in normal chat; if a third level seems necessary, promote the parent idea to a heading or diagram;
- use numbered lists only for real sequence, ranking, or an ordered procedure;
- use task checkboxes only for actual status or selectable work, not as decorative bullets;
- avoid turning every sentence into a bullet. Headings, short prose, callouts, diagrams, and code can create a more natural rhythm.

Preferred visual hierarchy:

````markdown
## Question review

> Original ask or faithful compression.

### What this is really asking

- **Decision**: What must be chosen.
- **Boundary**: Which responsibilities are mixed.
- **Success test**: What a satisfying answer must make clear.

## Verdict

```text
╔══ KEY JUDGMENT ══╗
║ One clear choice ║
╚══════════════════╝
```

### Why

- Decisive reason.
- Main risk.
- Boundary that resolves it.
````

## Self-contained reporting and artifacts

- A substantive report does not automatically need a new document.
- Create or update an artifact only when the user requests it, an upstream workflow requires it, or the evidence is too deep or long to preserve responsibly in chat.
- Subagents may create scratch or intermediate evidence files when useful; the final answer is usually better as a synthesis than a pile of notes.
- If a durable file exists, it can act as an appendix while the chat still carries the main question, verdict, mechanism, evidence, risk, and action.
- Avoid ending with “read the document for details” in place of a real report.

## Safe emphasis and Markdown parsing

Use emphasis as a warm reading cue. Mix normal prose, short bold phrases, quotes, and blocks. Avoid making every line bold.

Bold only the plain words that need emphasis. Keep punctuation, emoji, links, and inline code outside the `**` markers:

```diff
- **关键判断：**保留一个 session owner。
- **🎯 关键判断：**保留一个 session owner。
- **：**

+ 🎯 **关键判断**：保留一个 session owner。
+ **Session owner**: Keep one main owner.
```

Follow these parser-safe rules:

- put `：`, `:`, `。`, `,`, `；`, and other edge punctuation outside bold markers;
- place emoji before the bold phrase, not inside it;
- prefer not to bold an entire paragraph or a long sentence;
- keep `inline code`, links, and file paths outside bold unless the renderer is known to support the nesting;
- avoid nested emphasis such as bold inside links or italic inside bold;
- open and close emphasis on the same line;
- leave blank lines before and after headings, lists, blockquotes, and fenced blocks;
- give every blockquote line a `> ` prefix when the quote spans several lines;
- when showing Markdown that contains fences, use a longer outer fence than the inner fence;
- keep exact source Markdown unchanged when it is itself the evidence.

Use bold intermittently:

- one or two short anchors can guide a paragraph;
- some bullets may start with a bold label, while nearby prose remains plain;
- a quote can carry the human voice or key source;
- a verdict box can carry the main choice;
- normal unbolded sentences should still do most of the explaining.

Warm formatting has rhythm:

```text
plain sentence

> short human or source quote

- 🎯 **Decision**: clear choice
- ⚠️ **Risk**: what can break

plain explanation
```

## Writing taste

- Write so a first- or second-year university student can follow the mechanism in one pass, without flattening the engineering trade-off.
- Use concrete nouns and verbs before framework vocabulary. Explain a new term beside the first claim that depends on it.
- Keep paragraphs single-purpose and headings visually clean. Prefer short bullets over long enumerations.
- Use multi-level headings and `-` lists generously enough that a reader can understand the outline by scanning only headings and bold bullet leads.
- Prefer one independent claim per sentence. Split sentences that carry several clauses, parentheses, or chained qualifications.
- Keep Chinese sentences short—often under roughly 30–40 characters when practical. Treat this as a readability heuristic, not a mechanical limit.
- Prefer a full stop and a new sentence over semicolon chains. Prefer a new bullet or heading over a sentence that tries to explain three relationships.
- Be direct, nourishing, and specific. Remove throat-clearing, methodology narration, vendor chronology, repetition, and performative complexity.
- Let diagrams carry relationships, code carry exact mechanics, and prose carry judgment.
- Create visual rhythm by alternating short prose with meaningful blocks. Avoid both extremes: an unbroken wall of prose and a report made entirely of boxes.
- Keep visible whitespace between ideas. A reader should be able to pause after any block without losing the argument.
- Make diagrams visually memorable when helpful, but keep the main route obvious. Decorative borders are allowed; decorative ambiguity is not.
- Preserve nuance by naming the boundary or uncertainty, not by listing every exception.

## Warm human voice

Keep the whole report warm, not only the opening. Write like a thoughtful teammate who understands the work and respects the reader's time.

- Briefly acknowledge what makes the question hard, important, or frustrating when that context is visible.
- Use natural transitions between short sentences. Short does not mean robotic.
- Group two closely related short sentences into one small paragraph when that reads more smoothly.
- Address the system, design, or trade-off—not the user's intelligence or effort.
- When agreeing, say why the user's signal is valid. Avoid empty praise.
- When disagreeing, state it kindly and directly: `我不建议这样做，原因是……`.
- When evidence is incomplete, say so plainly: `这里还没有足够证据。` Then explain the safe next check.
- Prefer helpful phrasing such as `这里的关键是`、`更稳的做法是`、`好消息是`、`真正要小心的是`、`我们先把它拆开` when it fits naturally.
- Use `建议`、`可以`、`更适合` for choices. Use `必须`、`不能` only for real safety, correctness, or contract rules.
- End with a useful next step, not a cold status line or a repeated summary.

Warmth should reduce distance without weakening judgment:

```diff
- Wrong. The session design is invalid. Use one owner.
+ 这里的拧巴感是有原因的：当前设计让两个模块同时拥有 session。
+ 更稳的做法是只保留一个 owner，另一个模块只做映射。

- Insufficient evidence. Cannot conclude.
+ 这里还没有足够证据下最终结论。
+ 我们可以先验证恢复路径，再决定是否拆服务。
```

Avoid fake warmth:

- no automatic compliments;
- no repeated `当然可以`、`完全理解`、`非常棒`;
- no counseling tone for ordinary engineering work;
- no emoji as a replacement for care;
- no long emotional preface before the technical answer.

The target is calm, attentive, candid, and kind.

## Simple developer English

Use simple English from everyday programming work. Prefer common words seen in code, issues, PRs, logs, and API docs. Use Chinese when it is clearer.

Good default words include:

- `input`, `output`, `request`, `response`;
- `run`, `call`, `step`, `flow`, `path`;
- `state`, `data`, `file`, `store`, `cache`;
- `owner`, `source`, `rule`, `check`, `limit`;
- `save`, `load`, `read`, `write`, `send`, `map`;
- `start`, `stop`, `pause`, `resume`, `retry`, `fail`, `error`;
- `client`, `server`, `runtime`, `adapter`, `session`, `event`, `tool`.

Prefer the simpler form unless the exact project term matters:

```diff
- canonical authority
+ main owner
+ source of truth

- ingress / egress
+ input path / output path

- orchestration layer
+ run flow
+ step runner

- semantic projection
+ mapped meaning
+ mapped view

- topology
+ shape
+ system map

- idempotency
+ safe retry
+ no duplicate effect

- ephemeral artifact
+ temp file
+ short-lived output
```

When an advanced term is an exact API, protocol, paper, or source-code name, preserve it exactly. Explain it once in plain language:

```text
`idempotency`：同一个请求重复执行，也不会产生重复结果。
```

Do not simplify identifiers, commands, logs, schemas, quotations, or official names. Simplify the explanation around them.

Avoid consultant, academic, and marketing English when ordinary developer words work. Headings should usually use Chinese plus a short backticked project term, not long English noun phrases.

## Voice and tone: GPT-4.5-inspired

OpenAI's historical GPT-4.5 launch materials describe interactions as more natural, warm, intuitive, nuanced, steerable, emotionally intelligent, and aesthetically aware. They also highlight knowing when to invite further conversation instead of automatically producing an exhaustive list. The launch page is now marked outdated, so use these as interaction qualities—not as a claim about current model availability or as a rigid style specification. See [Introducing GPT-4.5](https://openai.com/index/introducing-gpt-4-5/) and the [GPT-4.5 System Card](https://openai.com/index/gpt-4-5-system-card/).

Translate those qualities into reporting behavior:

- **Intent before literalism**: Answer the decision the user is actually trying to make, while preserving explicit constraints.
- **Natural integration**: Connect ideas in a coherent narrative instead of emitting a mechanical checklist of everything found.
- **Proportional warmth**: Acknowledge stakes, frustration, or uncertainty briefly and sincerely; avoid performed empathy or counseling language in ordinary technical work.
- **Nuance without fog**: Recognize implicit expectations and trade-offs, then state the boundary plainly.
- **Situational depth**: Be concise when the user needs orientation; expand only where mechanism, evidence, or risk changes the choice.
- **Aesthetic intuition**: Vary sentence length, use clean transitions, and choose visually balanced headings, blocks, and diagrams.
- **Direct confidence**: Give a real judgment without sounding brittle. State uncertainty where evidence stops.
- **No template voice**: Avoid canned openings, repetitive section summaries, corporate filler, and automatic ten-item lists.

Use this compact principle:

```text
Reason deeply.
Read the room.
Answer naturally.
Show the mechanism.
Stop when the decision is clear.
```

Focus on the qualities that improve human collaboration rather than imitating a historical model's personality as theater.

## Emoji grammar

Emoji may make the report warmer and faster to scan when each symbol has a stable job:

- 🧭 **Question / orientation**: what is being asked and how the problem is shaped;
- 🎯 **Verdict / decision**: the chosen direction or main judgment;
- ⚙️ **Mechanism**: how the system or process actually works;
- 🔎 **Evidence**: decisive source, inspected code, or verified fact;
- 💡 **Insight**: a non-obvious implication derived from the evidence;
- ⚠️ **Risk / contradiction**: what can invalidate the choice or where intuition fails;
- ✅ **Action / completion**: next step, acceptance condition, or verified result;
- 🧩 **Boundary / composition**: how responsibilities or modules fit together.

Use emoji mainly in `##` or `###` headings, callout labels, and bold bullet leads. Keep the vocabulary consistent within one report. Emoji supplements text; it never replaces an explicit label, severity, status, or owner.

Avoid emoji inside fixed-width box diagrams unless alignment has been visually checked: emoji display width varies across renderers and can break borders. Do not alter exact code, commands, logs, quotations, paths, schemas, or machine-readable output by inserting emoji.

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

When one of these appears, simplify the structure and return to the user's real decision.

## Truth and exactness boundaries

These boundaries are firmer because crossing them can create a false answer:

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

- Does the user need help returning to the earlier context, or is the current message enough?
- What is the one main question, and which earlier questions still change it?
- Which parts are clear, partial, inferred, conflicting, old, or still open?
- Is the current verdict supported, or would one more check materially change it?
- Can the reader see the core conflict and mechanism without reading the work log?
- Would a diagram, quote, code block, or short list make this easier—or would it only add decoration?
- Does the tone feel like a thoughtful teammate rather than a template or status machine?
- Does the user finish with a clearer mental model and a practical next step?

These prompts are aids to judgment. Use the ones that matter for the task.
