# Visual and Evidence Patterns

Load this file for technical, architectural, or research reporting.

## What the visuals serve

Visual style is not the main product. It supports a clear line of thought.

```text
1. re-synthesize the problem space
2. find the core conflict and useful insight
3. choose a professional report order
4. calibrate evidence and uncertainty
5. use Markdown UI to make the thinking easy to follow
```

When a visual choice competes with problem clarity or report order, prefer clarity and order. A plain diagram that reveals the real relation is more valuable than a beautiful diagram around weak thinking.

## Problem-analysis canvas

Use diagrams during analysis, not only after the answer is known. A useful canvas places the main conflict in the center and keeps context, questions, evidence, and need around it.

```text
Earlier context                  Current questions
┌──────────────────┐           ┌──────────────────┐
│ old asks         │           │ explicit asks    │
│ accepted choices │           │ new constraints  │
└─────────┬────────┘           └─────────┬────────┘
          └────────────┬─────────────────┘
                       ▼
              ┌──────────────────┐
              │ Main conflict    │
              │ the key tension  │
              └──────┬─────┬─────┘
                     │     │
                     ▼     ▼
              deeper ask   unmet need
                     │     │
          ┌──────────┘     └──────────┐
          ▼                           ▼
   evidence ready                evidence missing
```

Use a flat list mainly as an inventory. Move to a spatial map when any of these relations matter:

- one question depends on another;
- two goals conflict;
- one layer owns another object's state;
- an earlier decision changes the current ask;
- evidence supports or weakens a claim;
- several surface questions point to one deeper need.

The center of the canvas should answer `what is the key tension?`. The lower part should answer `what deeper problem or need does this tension reveal?`.

## Problem-behind-the-problem pattern

```text
What the user asks              What may sit underneath

┌──────────────────┐           ┌──────────────────┐
│ choose SDK       │──────────>│ stable contract  │
│ choose hosting   │──────────>│ state ownership  │
│ compare protocol │──────────>│ durable boundary │
│ fix awkward flow │──────────>│ mixed owners     │
└──────────────────┘           └──────────────────┘

                        ▼

               What the user needs

          confidence · proof · simpler model
          clear owner · safe next decision
```

Treat the deeper issue as an inference until evidence supports it. The point is to help the user see a useful possibility, not to claim hidden intent with certainty.

## Use several small visuals, not one overloaded picture

For a substantive report, prefer two or three compact diagrams that answer different questions:

- **Problem geometry**: What objects, questions, axes, and conflicts make up the ask?
- **Ownership or mechanism**: Who owns identity, state, lifecycle, authority, and effects? How does the main path run?
- **Lifecycle or choice**: Where does the system pause, retry, resume, fail, migrate, or branch into alternatives?

Use only one when another diagram would repeat the same edge. One visual should answer one question. Keep labels short, arrows directional, and width suitable for an ordinary code block.

Avoid more than three consecutive nodes on one axis. For larger relationships, use a two-dimensional map, grouped regions, hub-and-spoke layout, parallel lanes, or multiple diagrams.

Separate fenced `↓` blocks between ordinary report sections are usually unnecessary. Markdown already reads downward; arrows work best inside one semantic diagram.

This style usually reads better without Markdown tables. For exact mappings, consider an aligned text block, paired bullets, or a mapping diagram.

## Markdown block palette

Treat Markdown blocks as a small visual language. Interleave them with short prose instead of reserving blocks only for executable code.

### Original-question block

> **User's original ask**
> Preserve the relevant user wording here before analysis.

When analysis depends on several turns, quote the related user messages in time order:

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

Prefer the full relevant wording when the combined quote is at most about 1000 Chinese characters. For longer material, keep the decision-bearing passages and mark omitted text explicitly:

```markdown
> 原始问题的关键部分……
>
> […]（省略与当前分析无关的中间描述）
>
> 后续改变范围的原话……
```

Preserve the user's exact wording, code, links, and emphasis where practical. If an earlier turn is unavailable, say so rather than recreating it.

### Key-judgment callout

> **Key judgment**
> State the choice in one sentence. Follow with the boundary or reason that makes it true.

Use a more visually emphatic fenced block when the verdict is the report's anchor:

```text
╔═══════════════ VERDICT ═══════════════╗
║ Keep the runtime as source of truth. ║
║ Add the protocol as a thin adapter.  ║
╚═══════════════════════════════════════╝
```

### Constraint or invariant block

```text
INVARIANT
  one thread  -> one authoritative session
  one action  -> one idempotency key
  one diagram -> one relationship
```

### Source capsule

Keep links clickable by using a blockquote rather than a code fence:

> **Verified source**
> [Official specification](https://example.com/spec) · `path/to/source.ts` · tag or commit when known

### Exact-output block

Use a fence when spacing, bytes, commands, logs, schemas, or machine-readable output must remain literal:

```text
RUN_STARTED -> MESSAGE_DELTA* -> RUN_FINISHED
```

### Code and pseudocode pair

Use neighboring blocks to distinguish present fact from proposed design. Keep provenance labels directly above both blocks.

Visual variety works best when block semantics stay stable. Reusing one callout style for one kind of claim is often clearer than inventing many styles.

## Syntax-highlighted pseudocode palette

Pseudocode should usually use a real language tag for color and structure. The provenance label must still say that it is pseudocode.

Use TypeScript for interfaces, adapters, event flows, and async relationships.

`Pseudocode: recommended interface, not an existing API`

```ts
// PSEUDOCODE
type SessionBinding = {
  threadId: string;
  nativeSessionId: string;
};

for await (const event of nativeRun) {
  yield projectToProtocol(event, binding);
}
```

Use Python for short algorithms, branching, retries, and orchestration.

`Pseudocode: recommended control flow, not executable framework code`

```python
# PSEUDOCODE
if output.is_valid:
    commit(output)
elif retry_budget > 0:
    retry(with_feedback=output.errors)
else:
    fall_back_to_text()
```

Use YAML for declarative ownership, policy, rollout stages, and configuration-shaped thinking.

`Pseudocode: recommended ownership model`

```yaml
# PSEUDOCODE
ownership:
  runtime: [loop, session, checkpoint]
  adapter: [translation, correlation]
  product_ui: [renderer, interaction]
  business_system: [authority, durable_facts]
```

Use JSON for payloads and schemas. Use `diff` for a visual before/after. Use `bash` for commands. Keep `text` for diagrams, mappings, logs, constraints, and exact output.

Choose a language because its grammar helps explain the construct, not only because its colors look attractive.

## Emoji as semantic navigation

Use emoji to help the eye locate a section's purpose before reading it. A stable heading sequence might be:

````markdown
## 🧭 Question review

## 🎯 Verdict

## ⚙️ Mechanism

## 🔎 Decisive evidence

### ⚠️ Main risk

## ✅ Recommendation and next step
```

Useful recurring meanings include:

- 🧭 orientation and problem framing;
- 🎯 judgment and decision;
- ⚙️ mechanism and execution;
- 🔎 evidence and source inspection;
- 💡 insight and implication;
- ⚠️ contradiction, uncertainty, or risk;
- ✅ action, acceptance, or completion;
- 🧩 ownership boundary or composition.

The symbol and nearby words should agree. A stable meaning for each emoji usually makes the report easier to scan.

Emoji also works in scannable bullets:

- 🎯 **Decision**: Keep the existing session owner.
- ⚙️ **Mechanism**: Translate native events at the adapter boundary.
- ⚠️ **Risk**: Replaying full history can duplicate context.
- ✅ **Next step**: Verify two turns on one thread.

Keep emoji outside exact source material. Do not insert it into code, commands, paths, schemas, logs, quotations, or machine-readable output.

Avoid emoji inside fixed-width diagrams unless the final rendering has been checked. Display widths differ across fonts and platforms:

```text
Safe:   🎯 Verdict
        ┌───────────────┐
        │ Clear borders │
        └───────────────┘

Risky:  ┌─🎯────────────┐  <- emoji width may shift the border
        │ Verdict       │
        └───────────────┘
```

Emoji is a navigation accent, not a substitute for words. Accessibility, exactness, and seriousness still come first.

## Heading and `-` list palette

Headings provide the report's visible skeleton:

- `##` marks a major turn in the argument: question, verdict, mechanism, evidence, action.
- `###` names a local decision, owner, contradiction, risk, or scenario inside that section.
- `####` is reserved for dense technical detail that cannot be expressed more clearly with a short list or diagram.
- Deeper levels usually signal that the report should be simplified.

Hyphen bullets provide the local anatomy:

- use `-` for sibling claims, facts, constraints, consequences, owners, and actions;
- use a bold lead-in when the reader should be able to scan the list without reading every sentence;
- keep normal lists to one level and use at most one nested level;
- turn a third nesting level into a `###` subsection, a tree diagram, or a separate block;
- use numbers only when order or rank is real;
- keep a blank line before every list and after headings so CommonMark renders predictably.

```markdown
## Verdict

The protocol belongs at the interaction boundary.

### Why

- **Runtime**: Owns the loop and durable session.
- **Adapter**: Owns translation and correlation.
- **Product UI**: Owns rendering and interaction.
- **Business system**: Owns authoritative facts.

### Main risk

- Duplicating history creates two conflicting sources of truth.
  - Prevent it by selecting one canonical session owner.
```

The report should be understandable from its heading outline and bold bullet leads, while the surrounding prose supplies reasoning and nuance.

When relationships become more important than prose nesting, switch to a tree:

```text
## Mechanism
   ├─ ### Input
   │     ├─ identity
   │     └─ context
   ├─ ### Runtime
   │     ├─ session
   │     └─ effects
   └─ ### Output
         ├─ events
         └─ UI projection
```

## Simple developer-word palette

Use the smallest English word that preserves the technical meaning.

Prefer:

- `owner`, not `authority holder`;
- `main`, not `canonical`, unless the source uses that term;
- `input` and `output`, not `ingress` and `egress`;
- `flow` or `steps`, not `orchestration`, unless naming a real framework feature;
- `map`, not `projection`, when simple data conversion is meant;
- `save`, `load`, `retry`, `fail`, and `fix`, not abstract process nouns;
- `temp`, not `ephemeral`, unless lifecycle precision matters;
- `file`, `report`, or `output`, not `artifact`, when one of those is exact.

Use a color-rich `diff` block to clean up language during editing:

```diff
- The adapter performs semantic projection across the ingress boundary.
+ The adapter maps input events at the API boundary.

- The orchestration layer materializes a canonical state artifact.
+ The run flow saves the main state file.

- Idempotency guarantees effect-level deduplication.
+ Safe retry prevents the same effect from running twice.
```

Preserve exact source terms:

- code symbol: `RunAgentInput`;
- API field: `previous_response_id`;
- protocol event: `RUN_FINISHED`;
- official concept: `idempotency key`;
- command, path, log, schema, and quotation text.

Explain the exact term with simple words beside its first use:

> **`idempotency key`**
> A request ID used to stop the same write from running twice.

The goal is not childish English. The goal is low-cost English that a working developer reads without translation.

## Warm microcopy patterns

Warmth should appear in transitions, judgments, caveats, and next steps. It should not be limited to a friendly first sentence.

### Acknowledge the real tension

```diff
- There are two conflicting owners.
+ 你觉得这里拧巴是对的：现在确实有两个模块在争同一份 state。
```

### Give a firm choice without sounding harsh

```diff
- Do not do this. It is wrong.
+ 我不建议走这条路。它会产生两份 history，恢复时很难保证一致。
```

### State uncertainty with a useful path

```diff
- Unresolved. More research required.
+ 这里还没有足够证据。
+ 先跑一次断线恢复测试，就能判断是否需要新的 store。
```

### Turn status into help

```diff
- Update complete. Validation passed.
+ 已经改好，并通过校验。下一次技术汇报会直接使用这套规则。
```

### Keep short prose connected

Avoid telegraph fragments:

```text
问题存在。
原因明确。
建议修改。
```

Prefer one warm, compact paragraph:

```text
这里的问题已经比较清楚：两个模块同时拥有 session。
建议先收回到一个 owner，再让 adapter 只负责事件映射。
```

Useful transition phrases include:

- `这里的关键是……`
- `你担心的点是成立的……`
- `好消息是……`
- `真正需要小心的是……`
- `更稳的做法是……`
- `我们先把这两个问题拆开……`
- `这一步做完后，后面的选择会简单很多。`

Use them sparingly. Repetition turns natural warmth into a template.

Warmth is not praise. It comes from accurate listening, fair criticism, honest uncertainty, and a useful next step.

## Parser-safe emphasis rhythm

Use bold as a light reading cue. Bold plain words only. Keep punctuation and emoji outside.

```diff
- **🎯 Decision:** Keep one owner.
- **Decision:** Keep one owner.
- **:**

+ 🎯 **Decision**: Keep one owner.
+ **Main owner**: Native runtime.
+ **主要风险**：重复写入 history。
```

Mix forms instead of bolding every line:

```markdown
这里的关键是先选出一个 session owner。

> 两份 history 看起来更安全，实际会让恢复更难。

- 🎯 **选择**：保留 runtime 作为 owner。
- ⚠️ **风险**：adapter 再存一份 history。

这样做后，恢复路径会简单很多。
```

Keep the syntax simple:

- bold short plain-text phrases only;
- put punctuation after the closing `**`;
- keep emoji before the opening `**`;
- keep code spans and links outside bold;
- avoid bold plus italic plus links in one phrase;
- close markers on the same line;
- add blank lines around quotes, lists, and fenced blocks;
- use a longer outer fence when demonstrating inner fences.

Quotes add warmth and voice. They work well for the user's words, one short source statement, or a key human observation; ordinary prose should still carry most of the report.

## Problem-geometry pattern

Use this before the verdict when several surface questions point to one underlying decision:

```text
┌────────────────┐       ┌────────────────┐
│ Objects        │──────>│ Relationships  │
│ runtime, UI    │       │ carries, owns  │
└───────┬────────┘       └───────┬────────┘
        │                        │
        ▼                        ▼
┌────────────────┐       ┌────────────────┐
│ Mixed axes     │──────>│ Real decision  │
│ protocol/deploy│       │ where boundary?│
└────────────────┘       └────────────────┘
```

Replace every label with the user's actual objects and axes. The geometry should show which questions are siblings, which are dependencies, and which only look related because two layers share vocabulary.

## Clue hierarchy pattern

Before adding evidence, make the question order visible.

```text
User's words

┌────────────────┐      ┌────────────────┐
│ Explicit ask A │      │ Explicit ask B │
└────────┬───────┘      └────────┬───────┘
         └───────────┬───────────┘
                     ▼
            ┌────────────────┐
            │ Main question  │
            │ core need      │
            └───────┬────────┘
                    │
       ┌────────────┴────────────┐
       ▼                         ▼
┌──────────────┐          ┌──────────────┐
│ Support      │          │ Constraints  │
│ how / why    │          │ limits / risk│
└──────────────┘          └──────────────┘
```

Use three content lanes:

- **Main line**: what must be decided and why it matters;
- **Support line**: mechanism, facts, and main risk;
- **Detail line**: versions, edge cases, extra examples, and secondary sources.

The main line should be readable on its own. Support should explain it. Detail should never interrupt it.

Use this short opening pattern:

```markdown
## 🧭 问题回顾

> 当前用户原话；如果分析依赖前文，也在这里引用相关多轮原话。
>
> 相关原文总量超过约 1000 字时，可对非关键部分做明确标记的省略。

### 用户的问题

- 🎯 **主问题**：最终需要做什么选择？
- ⚙️ **支撑问题**：系统实际怎样运行？
- ⚠️ **约束**：哪些风险和边界不能忽略？

### 核心需求

这几个问题最终指向同一个需求：……
```

After this opening, reveal information by importance:

```text
FIRST SCREEN                     SUPPORT
┌────────────────────┐          ┌────────────────────┐
│ ask · core need    │          │ mechanism · facts  │
│ conflict · verdict │          │ risk · insight     │
└──────────┬─────────┘          └──────────┬─────────┘
           └─────────────┬────────────────┘
                         ▼
                  ┌────────────┐
                  │ next action│
                  └────────────┘

DETAIL LANE
versions · history · extra examples
only when they change the choice
```

State the main question early when possible, so the reader does not have to discover it by reading every section. Return to it through new evidence rather than repeated wording.

## High-dimensional question-space projection

Complex multi-turn questions often live on several axes at once. The useful work is to project that space into a small map the reader can hold.

```text
Questions                         Axes

Q1 hosting ───────────────┐       layer
Q2 session owner ─────────┼────>  owner
Q3 protocol support ──────┤       state
Q4 current vs planned ────┘       time

Relations

Q2 blocks Q1
Q3 supports Q1
Q4 changes how Q3 should be read
```

A useful synthesis often does three things:

- **Cluster** questions that share one axis or decision;
- **Connect** questions that depend on or block each other;
- **Distill** the central need that explains why the cluster matters.

The displayed map can be much smaller than the internal analysis. Show the axes and edges that change understanding or action.

Use a simple center map when many questions point to one deeper need:

```text
┌──────────────┐      ┌──────────────┐
│ Deployment   │      │ SDK support  │
└──────┬───────┘      └──────┬───────┘
       │                     │
       └──────────┬──────────┘
                  ▼
          ┌──────────────┐
          │ Deeper need  │
          │ clear owner  │
          └──────┬───────┘
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
┌──────────────┐    ┌──────────────┐
│ Session      │    │ Business fact│
└──────────────┘    └──────────────┘
```

## Long-run context re-entry pattern

Use this after long research, background work, many tool calls, or a large time gap.

```text
Earlier turns                     Current turn
┌────────────────────┐          ┌────────────────────┐
│ original goal      │          │ latest request     │
│ added questions    │          │ current constraint │
│ accepted choices   │          │ needed decision    │
└──────────┬─────────┘          └──────────┬─────────┘
           └─────────────┬─────────────────┘
                         ▼
                ┌──────────────────┐
                │ Current problem  │
                │ scope that matters│
                └────────┬─────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       what is known          what remains open
```

Open with a short human reminder:

> **Where we left off**
> You first asked …
> Later, we added …
> This update focuses on …

Keep earlier turns that change the current meaning, scope, owner, or success check. A short decision record is usually more useful than replaying the transcript.

### Report-delta board

When this is not the first report, show why the new report changes the reader's mental model. Use only the states that contain real information.

```text
┌─ STILL TRUE ─────────┐     ┌─ CHANGED ───────────┐
│ accepted boundary   │     │ scope or mechanism  │
│ verified fact       │     │ current judgment    │
└─────────────────────┘     └─────────────────────┘

┌─ INVALIDATED ───────┐     ┌─ NEW / STILL OPEN ──┐
│ old assumption      │     │ decisive evidence   │
│ rejected direction │     │ remaining blocker   │
└─────────────────────┘     └─────────────────────┘
```

This board is not a changelog. Include a delta only when it changes context, confidence, choice, risk, or action. Keep the original user quote above it as the stable memory anchor.

## Research-status panel

Stable status words can make different levels of certainty visible without making every item look equally complete.

```markdown
### 🔎 当前调研状态

- ✅ **已查清**：有源码、官方资料、测试或直接观察支持。
- 🟡 **部分清楚**：主路径已知，但关键场景还没验证。
- ❓ **仍待确认**：证据不足，暂时不能下结论。
- 💡 **当前推断**：由已验证事实推导，不是直接实现事实。
- ⚠️ **存在冲突**：来源、版本或目标之间不一致。
- 🕰️ **可能过期**：旧资料可能已经变化。
```

Connect status to the decision:

```text
✅ Clear facts             🟡 Partial / ❓ Open
┌──────────────────┐      ┌──────────────────┐
│ safe to decide   │      │ blocks decision │
└────────┬─────────┘      └────────┬─────────┘
         │                         │
         ▼                         ▼
  current verdict            smallest next check
```

When evidence is weak, use warm but firm language:

> 目前还不能可靠下结论。缺的是多实例恢复路径的验证。
>
> 先补这一项，拆不拆新服务就会清楚很多。

## Leader-update board

A boss or decision group should see the state of the decision, not the diary of the work.

```text
┌──────────────────────┐      ┌──────────────────────┐
│ 🧭 Context           │      │ 🔎 Current status    │
│ goal · scope · asks  │      │ clear · open · risk  │
└──────────┬───────────┘      └──────────┬───────────┘
           └──────────────┬──────────────┘
                          ▼
                 ┌──────────────────┐
                 │ 🎯 Decision      │
                 │ what can be done │
                 └────────┬─────────┘
                          │
             ┌────────────┴────────────┐
             ▼                         ▼
      ⚙ Why it works             ✅ Next action
      mechanism · facts          owner · check · result
```

For leader updates, starting with the problem and current decision state is usually stronger than starting with `I searched`, `I read`, or a tool timeline. Mention the work process when it affects trust, coverage, or a blocker.

### Decision-handoff panel

Use this when a report recommends a path but the human still owns a material trade-off.

```text
🔎 VERIFIED BASIS                 🎯 MY JUDGMENT
┌────────────────────┐          ┌────────────────────┐
│ source · code      │─────────>│ recommended path   │
│ test · evidence gap│          │ reason + limit     │
└────────────────────┘          └──────────┬─────────┘
                                          │
                           ┌──────────────┴──────────────┐
                           ▼                             ▼
                    YOUR DECISION                 WOULD CHANGE IF
                    trade-off owned               reversal condition
```

Do not add `YOUR DECISION` when the evidence already settles the question or the user already authorized the choice. Do not add `WOULD CHANGE IF` when there is no material contingency. The panel exists to preserve decision clarity, not to weaken a supported recommendation.

The same geometry may use richer framing when the extra structure improves scanning:

```text
╔════════════ WHAT WAS ASKED ════════════╗
║ SDKs · hosting · protocol · sessions  ║
╚══════════════════╤═════════════════════╝
                   │ appears as one topic
                   ▼
┌────────────────────────────────────────┐
│ Actually four axes                    │
│                                        │
│ transport ─ deployment ─ state ─ UI   │
└──────────────────┬─────────────────────┘
                   │ split these axes
                   ▼
╔════════════ REAL DECISION ═════════════╗
║ Which layer owns each responsibility? ║
╚════════════════════════════════════════╝
```

For a deeper ownership question, expose the hidden center:

```text
surface questions
   ├─ How is it called?
   ├─ Where is it hosted?
   └─ Which SDK exists?
             │
             ▼
      deeper question
   Who owns identity, state,
   lifecycle, and effects?
```

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

Use this when the main question is “which layer owns what?” Replace labels with verified project objects. Mark synthesized ownership as `recommended` or `application-owned`.

Use parallel lanes when several owners act at the same time:

```text
┌─ Product UI ───────┐   renders / collects input
├─ Protocol adapter ─┤   translates / correlates
├─ Agent runtime ────┤   reasons / checkpoints
└─ Business system ──┘   authorizes / records truth
```

## Spatial composition and breathing room

Use whitespace to make ownership and direction visible. Separated nodes are often easier to read than tightly packed ones.

Prefer separated blocks:

```text
┌──────────────────┐          ┌──────────────────┐
│ Product UI       │          │ Agent Runtime    │
│ renders          │          │ reasons          │
└────────┬─────────┘          └────────▲─────────┘
         │                             │
         │ user action                 │ native run
         ▼                             │
┌───────────────────────────────────────────────┐
│ Protocol Adapter                              │
│                                               │
│ identity mapping  ·  event projection         │
└──────────────────────┬────────────────────────┘
                       │ authorized effect
                       ▼
              ┌──────────────────┐
              │ Business System  │
              │ records truth    │
              └──────────────────┘
```

Avoid cramped blocks:

```text
┌UI┐->┌Adapter┐->┌Runtime┐->┌DB┐
```

Use vertical space between phases. Use horizontal space between peers. Use nesting only for real containment. Use arrows only for a named relationship.

Use two-dimensional composition when several report elements relate to one center:

```text
🧭 Question                          🎯 Verdict
┌──────────────────┐                ┌──────────────────┐
│ What is mixed?   │                │ Choose boundary. │
└────────┬─────────┘                └────────┬─────────┘
         │                                   │
         └──────────────┬────────────────────┘
                        ▼
              ┌──────────────────┐
              │ Mechanism        │
              └───────┬──────────┘
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
  🔎 Evidence                 ⚠ Risk
  ┌──────────────┐            ┌──────────────┐
  │ What proves? │            │ What breaks? │
  └──────┬───────┘            └──────┬───────┘
         └────────────┬───────────────┘
                      ▼
               ✅ Next action
```

A block-heavy report still needs short prose between blocks. One or two sentences should explain why the next visual matters.

The page itself may interleave blocks. Headings and whitespace usually carry reading order better than arrows between every section.

## Mechanism-flow pattern

```text
input -> verify -> persist -> execute -> record -> deliver
```

Expand only the stages that affect the decision. When translation is the key seam, show both vocabularies:

```text
client input
    │
    ▼
protocol adapter
    │ maps identity + events
    ▼
native runtime
```

## Lifecycle pattern

Use a lifecycle diagram only when time changes ownership or correctness:

```text
receive -> run -> pause
                   │ human decision
                   ▼
             persist -> resume -> effect
```

Show retry or failure branches only when they change the recommendation:

```text
execute -> success -> record
   │
   ├-> retryable failure -> replay-safe retry
   └-> terminal failure  -> explicit error
```

## Choice pattern

Use a small branching diagram instead of a comparison table:

```text
Existing system?
   ├─ yes -> embedded adapter
   └─ no  -> standalone service

Independent scale or security boundary later?
   ├─ yes -> extract the same adapter boundary
   └─ no  -> keep one deployment
```

Alternatives belong here only when they materially change cost, ownership, or risk.

## Exact mappings without tables

Use aligned text for protocol or event mappings:

```text
Native event                 Protocol projection
message.delta             -> TEXT_MESSAGE_CONTENT
tool.started              -> TOOL_CALL_START
tool.completed            -> TOOL_CALL_RESULT
approval.requested        -> RUN_FINISHED(interrupt)
```

Keep this for exact repeated mappings. If the list does not change the decision, move it out of the main report.

## Fact versus inference

A diagram edge is a claim. Keep factual edges traceable to citations near the visual. Mark synthesized edges as `recommended`, `inferred`, or `application-owned` when the project does not ship them.

Label current implementation, roadmap, and recommendation when they appear in the same flow.

## Insight block

Use an insight block when the report has enough evidence to teach one non-obvious relationship.

```text
🔎 Verified fact                    ⚠ Conflict
┌────────────────────┐            ┌────────────────────┐
│ Runtime saves state│            │ Adapter saves it too│
└─────────┬──────────┘            └─────────┬──────────┘
          └──────────────┬──────────────────┘
                         │
                  💡 Insight
          ┌──────────────────────────┐
          │ Two recovery truths exist│
          └────────────┬─────────────┘
                       │
                  🎯 Decision
          Keep one main state owner.
```

Write the surrounding prose in four short moves:

- **Observation**: What did the source or code prove?
- **Conflict**: Which facts, goals, or owners do not fit together?
- 💡 **Insight**: What does that reveal about the real problem?
- 🎯 **Decision**: What changes because of that insight?

Good insight types include:

- hidden owner;
- mixed layers;
- missing rule;
- false symmetry;
- impossible trade-off;
- failure trigger;
- condition that would reverse the recommendation.

Avoid forcing a surprising claim. A simple, well-supported answer is better than fake depth.

## Code provenance

Use one of these labels immediately above a code block:

- `Official usage (version/tag, source URL or path)`
- `Minimal adaptation of official usage (source URL or path)`
- `Source relationship excerpt (commit + path)`
- `Pseudocode: recommended design, not an existing API`

For exact official code, preserve names and call relationships. Elide unrelated setup with comments rather than silently changing semantics.

When architecture depends on both present fact and proposed seam, show them separately:

`Minimal adaptation of official usage (source URL/path)`

```ts
const result = Runner.run_streamed(agent, input, { session });
for await (const event of result.stream_events()) {
  // Native events exposed by the official SDK.
}
```

`Pseudocode: recommended design, not an existing API`

```ts
for await (const nativeEvent of nativeRun) {
  yield mapNativeEventToProtocol(nativeEvent, sessionBinding);
}
```

The first block establishes what exists. The second makes the recommended adapter boundary explicit. Never merge them into a fictional official API.

## Attention sequence

Reveal complexity in this order:

```text
┌─────────────────┐      ┌─────────────────┐
│ Original ask    │      │ Real decision   │
└────────┬────────┘      └────────┬────────┘
         └────────────┬───────────┘
                      ▼
             ┌─────────────────┐
             │ Problem geometry│
             └────────┬────────┘
                      ▼
             ┌─────────────────┐
             │ Verdict + seam  │
             └──────┬────┬─────┘
                    │    │
                    ▼    ▼
               evidence  risk
                    └─┬──┘
                      ▼
                    action
```

Methodology, glossaries, and vendor catalogs are usually better after the reader knows the real question. Define a new term near the first claim that depends on it.

## Density and rhythm gate

The report should feel like a sequence of decisions, not a page of compressed prose.

Avoid this shape:

```text
long paragraph
long paragraph
long paragraph
long seven-item bullet list
large diagram explaining everything
repeated conclusion
```

Prefer a compact composition instead of a long vertical chain:

```text
🧭 Question         🎯 Judgment
     └──────┬──────┘
            ▼
       ⚙ Mechanism
        ┌───┴───┐
        ▼       ▼
   🔎 Evidence  ⚠ Risk
        └───┬───┘
            ▼
        ✅ Action
```

Use these editing heuristics:

- split a paragraph when its second idea could have its own heading, bullet, or edge;
- split a bullet when it contains more than one independent claim;
- split a diagram when it answers both “who owns this?” and “what happens next?”;
- shorten code to the call relationship that proves the point;
- remove an example if the previous block already made the mechanism clear;
- remove a source if it adds prestige but no new evidence;
- remove the closing summary when it merely repeats the verdict—finish with action instead.

Whitespace is part of the explanation. Leave visible breathing room around headings, lists, callouts, diagrams, and code.

## Two-minute architecture-brief pattern

```markdown
## 🧭 Question review

> Original ask or faithful compression.

- **Real decision**: One sentence.
- **Hidden geometry**: One sentence or small diagram.

## 🎯 Verdict

```text
╔══ DECISION ══╗
║ One choice.  ║
╚══════════════╝
```

## ⚙️ Mechanism

One diagram, followed by the minimum verified code and recommended pseudocode.

## 🔎 Evidence and risk

- **Verified**: Decisive fact.
- **Inference**: What it means.
- ⚠️ **Risk**: What could invalidate the choice.

## ✅ Next step

- One owner.
- One test.
- One acceptance condition.
````

When embedding fenced blocks inside this Markdown example, use a longer outer fence in the actual source so rendering remains valid.

## Clean Markdown rules

- Use short headings and generous blank lines.
- Use `##` for the main report path, `###` for decision-bearing subsections, and `####` sparingly.
- Use CommonMark `-` bullets actively for parallel information, with no more than one nested bullet level in normal chat.
- Prefer other visual forms over Markdown tables for this reporting style.
- Avoid deeply nested bullets and wall-to-wall bold text.
- Keep diagrams in fenced `text` blocks and code in language-tagged fences.
- Use syntax-highlighted `ts`, `python`, `yaml`, `json`, `diff`, or `bash` fences for pseudocode whenever the grammar truthfully fits; reserve `text` for visual and literal material.
- Keep citations beside the exact factual claim they support.
- Let the answer be readable without opening linked artifacts.
- Actively alternate prose, callouts, diagrams, exact blocks, and code when each form improves comprehension.
- Unicode single-line, double-line, rounded, and tree characters are allowed. Keep alignment correct in a monospace fence.
- Use a small, consistent emoji vocabulary in headings and bullet leads when it improves navigation or warmth.
- A visually elaborate frame works best with a short interior. Dense prose inside a fancy box is harder to read than ordinary prose.
- Give peer blocks horizontal space, phases vertical space, and the whole diagram enough room to breathe.
- Keep one visual axis to roughly three sequential nodes; recompose longer structures into regions or another diagram.
- Standalone arrow fences between normal headings, prose, lists, and code blocks usually add little.
- Keep useful citations clickable in normal Markdown or blockquotes rather than hiding them in code fences.
- Keep paragraphs short, lists clustered, and sections visibly separated; the main path should fit a two- to three-minute read.
- Prefer simple English from common code, issue, PR, log, and API vocabulary. Use plain Chinese around exact project terms.
- Keep the voice calm and warm across the whole report. Connect short sentences into small natural paragraphs instead of writing in telegram fragments.
- Bold only short plain-text phrases. Keep punctuation, emoji, links, and code outside the emphasis markers.
- Use normal prose, intermittent bold, and occasional blockquotes together so the page feels human rather than mechanically highlighted.
- Make the core conflict visible and add one grounded insight when it changes how the reader should think or act.
- Quote the relevant original user wording before analysis, then summarize, list, and rank the questions while keeping one main clue visible through verdict, evidence, and action.
- Use lists to collect questions, then use spatial diagrams to show dependency, conflict, ownership, time, evidence, and the problem behind the problem.
- After long-running work, restore the relevant multi-turn context and show research status before asking the reader to accept a verdict.

## Visual failure checks

- A decorative box around prose adds weight without understanding.
- A decorative box around a one-line verdict can improve scanning; the failure is boxing content without giving the box a semantic role.
- A diagram with unrelated flows should be split or reduced.
- Repeating the same ownership edge in three diagrams wastes attention.
- A dense ontology is not a senior brief; show only objects that change the choice.
- A code block without provenance can turn plausible synthesis into false API evidence.
- Plain gray pseudocode wastes a useful visual channel when an honest language tag could expose types, control flow, or declarative structure.
- A cramped one-line architecture chain hides ownership and should be expanded into spatial blocks.
- A long downward staircase of report elements wastes vertical space and repeats Markdown's natural reading direction.
- Repeated standalone `↓` blocks are visual filler unless they are part of one modeled flow.
- A flat wall under one heading hides the argument; a six-level outline hides it differently.
- A bullet list where every item contains several unrelated claims should be split by headings or diagrams.
- Emoji on every line, or the same emoji with shifting meanings, creates visual noise rather than hierarchy.
- Three dense paragraphs in a row usually mean the content needs a heading, bullets, or a diagram.
- Repeating the verdict as a final summary wastes the last screen; end with the next action when possible.
- Academic or consultant English that can be replaced by a common developer word adds needless reading cost.
- Cold commands, empty praise, and scripted empathy all weaken trust; use direct but kind engineering language.
- Bold punctuation, emoji inside emphasis, unbalanced markers, and deep Markdown nesting can render differently across clients.
- Attractive Markdown without a clear conflict, mechanism, or useful insight is decoration rather than a report.
- A flat question list with no main question forces the reader to do the prioritization work.
- A flat question list with hidden dependencies forces the reader to reconstruct the geometry alone.
- Secondary detail that appears before the core need breaks the progressive reading path.
- A long-running report that remembers only the latest message can answer the wrong scope with perfect confidence.
- A smooth answer that hides open or stale evidence is less useful than a clear partial result.
- A chronological work diary makes leaders spend attention before they know what decision is needed.
- A long mapping inventory belongs outside the three-minute path unless it decides the architecture.
