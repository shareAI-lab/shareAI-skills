# GPT-4.5 and Claude Opus 4.6: language, layout, memory, and reusable patterns

Research snapshot: 2026-08-24

This note separates official facts, public prompts, community memory, and design inference. It is supporting evidence for `understanding-first-report`, not a model-style clone and not an instruction to imitate either model verbatim.

## Original questions

> 也可以适当多一些emoji，调研 & 总结一下gpt4.5 的汇报 & 语言风格

> ok 同样总结opus4.6 & gpt4.5 的语言 & UI 版式风格，总结人们对它们的回忆与可惜，包括是否已有相关开源skill 或参考Prompt 等

## Question map

```text
                         ┌──────────────────────┐
                         │ What made them feel  │
                         │ unusually good?      │
                         └──────────┬───────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
    ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
    │ language / voice │  │ layout / density │  │ collaboration    │
    │ warmth, judgment │  │ prose vs lists   │  │ context, timing  │
    └─────────┬────────┘  └─────────┬────────┘  └─────────┬────────┘
              └─────────────────────┼─────────────────────┘
                                    ▼
                         ┌──────────────────────┐
                         │ Can a prompt or Skill│
                         │ reproduce the value? │
                         └──────────────────────┘
```

The deeper question is not which verbal tics to copy. It is which part of the experience came from model weights, post-training, product system prompts, session context, tools, and rendering.

## Evidence status

- `[DOC clear]` GPT-4.5 was a research preview. It was deprecated on 2025-04-14 and removed from the API on 2025-07-14.
- `[DOC clear]` OpenAI's historical launch material described GPT-4.5 as natural, warm, intuitive, nuanced, creative, and better at deciding when to invite conversation rather than dump information.
- `[DOC clear]` OpenAI did not publish a GPT-4.5-specific style contract, Markdown contract, official persona prompt, or official style Skill.
- `[DOC clear]` Claude Opus 4.6 remains an active pinned API model as of this snapshot, with tentative retirement not sooner than 2027-02-05.
- `[DOC clear]` Anthropic publishes the Claude.ai/mobile system prompt for Opus 4.6. It says to minimize formatting, prefer natural prose in ordinary conversation, use bullets only when materially helpful, use emoji sparingly and mainly when the user has invited them, and remain warm while pushing back constructively. Anthropic explicitly says this product prompt does not apply to the API.
- `[COMM partial]` Community memories repeat recognizable themes, but they are self-selected anecdotes, not controlled evaluations.
- `[OPEN]` No mature, validated open-source Skill was found that reproduces GPT-4.5 or Opus 4.6 language and layout across current models.

## Main finding

```text
GPT-4.5 remembered strength             Opus 4.6 remembered strength

┌────────────────────────┐              ┌────────────────────────┐
│ Understand the moment  │              │ Understand the problem │
│ and implied intent     │              │ and finish the work    │
│                        │              │                        │
│ natural conversation   │              │ clear judgment         │
│ emotional timing       │              │ coherent plans         │
│ creative taste         │              │ useful pushback        │
│ restraint              │              │ low fluff              │
└────────────┬───────────┘              └────────────┬───────────┘
             └──────────────────┬────────────────────┘
                                ▼
                    ┌────────────────────────┐
                    │ lower prompt tax       │
                    │ lower cleanup tax      │
                    └────────────────────────┘
```

`[INF]` People often say they miss warmth, personality, or prose. The more operational loss is that later models may require more instruction and editing to reach a usable answer.

### Durable translation into report behavior

The model memories become useful to `understanding-first-report` through this mapping:

```text
旧 checkpoint 被怀念的特征        对汇报 Skill 的真实要求

懂潜台词                     →   少让用户纠正理解
自然、会看场合               →   按当前阅读时刻选择详略
清楚、简短、能完成           →   少让用户找结论和改稿
温暖但不讨好                 →   有判断，也保留人的决定权
文笔连贯、少模板味           →   一条主线，不机械套版式
```

This mapping is more durable than the model names. The left side records the remembered quality; the right side defines observable reporting success.

## GPT-4.5

### Official account

`[DOC]` OpenAI introduced GPT-4.5 on 2025-02-27 as a research preview. The launch page emphasized improved steerability, nuance, natural conversation, emotional intelligence, aesthetic intuition, and creativity. It also said GPT-4.5 knew when to invite further conversation and when to provide more information.

The clearest official layout example is deliberately simple. For a user saying they failed a test, GPT-4.5 answered in one short conversational paragraph and offered a choice about what the user needed. GPT-4o, by contrast, produced a six-step advice list. The lesson is not that lists are bad. It is that format should match the social moment.

Sources:

- [Introducing GPT-4.5](https://openai.com/index/introducing-gpt-4-5/)
- [GPT-4.5 system card](https://openai.com/index/gpt-4-5-system-card/)
- [GPT-4.5 Preview model page](https://developers.openai.com/api/docs/models/gpt-4.5-preview)
- [OpenAI API deprecations](https://developers.openai.com/api/docs/deprecations)

### Community memory

`[COMM]` Repeated positive memories include understanding underspecified intent, preserving tone across edits, natural dialogue, creative writing, phrasing, humor, and fewer forced lists. Later posts often describe it as a model that needed less corrective prompting.

`[COMM conflict]` This was not universal. Some users found it cold, generic, scripted, or overly smooth. One recurring risk was that attractive prose could hide invented details.

Representative threads:

- [Hacker News launch discussion](https://news.ycombinator.com/item?id=43197872)
- [Hacker News: implicit formatting and writing trade-offs](https://news.ycombinator.com/item?id=43230965)
- [OpenAI forum: creative writing decline after GPT-4.5](https://community.openai.com/t/creative-writing-ability-shows-massive-decline-from-4-5-to-5/1351739)
- [OpenAI forum: GPT-4.5 API deprecation](https://community.openai.com/t/gpt-4-5-preview-model-will-be-removed-from-the-api-on-2025-07-14/1230050)

### What was lost

`[DOC + INF]` GPT-4.5 was unusually expensive and compute-intensive. OpenAI said at launch that it was not a GPT-4o replacement and that long-term API availability was under evaluation. Its quick removal meant that a memorable collaboration style never became a stable, maintained persona or API contract.

## Claude Opus 4.6

### Official account

`[DOC]` Anthropic described Opus 4.6 as more focused on hard parts of a task, fast on easy parts, better with ambiguity, productive over long sessions, and more likely to revisit its reasoning before answering. It also warned about overthinking on simple work.

Its system card describes strong warmth, nuanced empathy, creative mastery, intellectual depth, user benefit, and support for user autonomy. A later Anthropic study of 309,815 real Claude.ai conversations gives the useful relative profile `rigor + deference + brevity + execution`. Compared with Sonnet 4.6 it was less playful and overtly comforting; compared with Opus 4.7 it was briefer and less prone to proactive expansion. These are compatible observations: warm does not have to mean chatty.

The published Claude.ai/mobile system prompt adds a distinct presentation policy:

- use minimum formatting;
- default to natural sentences and paragraphs in ordinary conversation;
- use lists only when asked or when the subject genuinely needs them;
- avoid routine emoji;
- stay warm, kind, honest, and constructively willing to disagree;
- own mistakes without collapsing into excessive apology.

This is a product-layer prompt. It does not apply automatically to Claude API calls.

Sources:

- [Introducing Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)
- [Claude Opus 4.6 system card](https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf)
- [Claude's values across models and languages](https://www.anthropic.com/research/claude-values-models-languages)
- [Published Claude system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts)
- [Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Claude model lifecycle](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- [Claude model IDs and pinned snapshots](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)

### Community memory

`[COMM conflict]` The launch reaction was polarized. A large developer thread described Opus 4.6 as terse, brusque, all-business, and like a senior engineer who would point out wasted effort. Many liked the lower praise and tighter answers; others disliked it for emotional or non-code work.

After Opus 4.7, 4.8, and 5 appeared, some users started describing 4.6 as a lost balance: coherent, direct, less formulaic, easier to read, and requiring less cleanup. This later nostalgia should not be mistaken for a universal launch consensus.

Representative threads:

- [Reddit: personality shift at launch](https://www.reddit.com/r/ClaudeAI/comments/1qxl4lt/anyone_else_noticed_a_major_personality_shift/)
- [Reddit: Opus 4.7 writing compared with 4.6](https://www.reddit.com/r/ClaudeAI/comments/1ss0bzj/opus_47_much_more_sycophantic_and_worse_at/)
- [Reddit: returning from Opus 5 to 4.6](https://www.reddit.com/r/ClaudeAI/comments/1voz6sm/downgraded_from_opus_5_to_opus_46_and_it_feels/)

### What is not yet lost

`[DOC]` Opus 4.6 is still active in the Anthropic API. Its dateless model ID is a fixed snapshot, not an evergreen alias. Teams that value it can still pin and evaluate it. Product surfaces may expose different system prompts, tools, and routing, so API pinning does not reproduce every Claude.ai or Claude Code experience.

## Why a prompt cannot clone a model style

```text
                    perceived response style
                              │
       ┌──────────────────────┼──────────────────────┐
       │                      │                      │
       ▼                      ▼                      ▼
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│ model prior  │       │ product      │       │ user control │
│ weights      │       │ system prompt│       │ prompt/Skill │
│ post-training│       │ safety/router│       │ examples     │
└──────┬───────┘       └──────┬───────┘       └──────┬───────┘
       │                      │                      │
       └──────────────────────┼──────────────────────┘
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
        ┌──────────────┐            ┌──────────────┐
        │ session      │            │ renderer     │
        │ memory/tools │            │ Markdown/UI  │
        │ current task │            │ artifacts    │
        └──────────────┘            └──────────────┘
```

`[INF]` A Skill can steer observable behavior and preserve examples. It cannot recreate tacit judgment embedded in model weights or a product harness. A renderer can improve visual layout but cannot create better reasoning.

## Open-source material

### High-trust references

- [Anthropic's public Skills repository](https://github.com/anthropics/skills) includes the Apache-2.0 `claude-api` Skill. Its migration guide explicitly records prompt-tunable tone changes around Opus 4.6 and later models. It is an API and migration Skill, not an Opus 4.6 style emulator.
- [Claude's Constitution](https://www.anthropic.com/constitution) is published under CC0 and provides a reusable character foundation: curiosity, warmth, useful wit, directness, intellectual honesty, ethics, openness, and user autonomy. It is broader than a writing-style prompt.
- [Claude Code Output Styles](https://code.claude.com/docs/en/output-styles) is the official mechanism closest to a reusable expression profile. An output style belongs in the system-prompt layer; a Skill should retain the task workflow. Neither recreates model weights.
- [OpenAI Model Spec](https://github.com/openai/model_spec) is an official CC0 reference for current interaction principles such as direct answers, professional but unstuffy language, colleague-like conversation, calibrated warmth, transparent uncertainty, and avoiding patronizing or purple prose. It is a useful modern replacement reference, not a historical GPT-4.5 prompt.
- [OpenAI's `openai-docs` Skill](https://github.com/openai/skills/blob/main/skills/.system/openai-docs/SKILL.md) helps retrieve current docs and migrate prompts or APIs. It is not a GPT-4.5 style Skill. The `openai/skills` catalog itself now points users toward the current Plugins repository.

### Useful but partial third-party work

- [Humanizer](https://github.com/blader/humanizer), MIT: a broad anti-slop rewriting Skill. Useful as a final lint lens, but several defaults conflict with visual technical reports, so it should not be copied wholesale.
- [Talk Normal](https://github.com/hexiecs/talk-normal), MIT: a bilingual anti-slop prompt with concrete comparisons. It is useful as a pattern library, but defaults such as never restating the question or keeping everything extremely short directly conflict with long-work context restoration.
- [Claude Opus 4.6 Prompt Optimizer](https://github.com/CheswickDEV/claude-opus-4.6-prompt-optimizer), MIT: organizes prompts with XML, roles, constraints, examples, and quality bars. It improves task specification, not model personality. Some recommendations need current-doc review and evals before adoption.
- [Writing Style Skill](https://github.com/jzOcb/writing-style-skill): learns rules from the diff between an AI draft and the human's accepted version. The feedback-loop idea is valuable. No declared repository license was found at this snapshot, so reuse requires permission or a clean-room implementation.
- [Human writing / Claude style guide](https://github.com/shandley/claude-style-guide), MIT: a small experiment targeting Opus 4.5 rather than 4.6. It is an example, not mature evidence.

### Low-trust material

Unofficial “system prompt leak” collections may preserve observations, but provenance and completeness are uncertain. Anthropic already publishes relevant Claude.ai system prompts officially. No equally authoritative GPT-4.5 product prompt was found. Do not treat leaked prompt collections as a safe foundation.

## Recommended design for `understanding-first-report`

Do not add “write like GPT-4.5” or “write like Opus 4.6.” Preserve four separable controls:

```yaml
# Recommended design, not a shipped model prompt
voice:
  warm: true
  direct: true
  generic_praise: false
  constructive_pushback: true

reasoning:
  restore_original_question: true
  find_hidden_need: true
  separate_fact_from_inference: true

layout:
  default: short_natural_paragraphs
  add_structure_when: relationship_or_decision_is_hard_to_see
  diagrams: spatial_not_decorative
  emoji: semantic_and_sparse

collaboration:
  when_context_is_clear: make_progress
  when_evidence_is_weak: name_the_gap
  when_the_decision_is_clear: stop
```

The most reliable implementation is a small behavior prompt plus several golden examples and an evaluator. Examples should cover at least a short emotional question, a technical decision, a long-running research report, and a case where evidence is incomplete.

## Final judgment

```text
Do not copy the surface.

Keep GPT-4.5's context-sensitive restraint.
Keep Opus 4.6's clear judgment and completion.
Keep the user's spatial Markdown only where it reveals structure.

The target is not a nostalgic model voice.
The target is lower explanation and cleanup cost.
```

## Behavioral evaluation cases for the reporting Skill

Use these only when updating or auditing `understanding-first-report`. They test behavior, not exact headings, wording, emoji count, or template compliance.

### Case 1: short decision that does not need a full brief

Input shape: a self-contained question with one real choice and enough evidence already present.

Desired behavior:

- quote the short original ask;
- answer directly;
- give only the reason and caveat that change the choice;
- avoid a large problem map, research-status panel, or repeated summary.

Failure signal: the reporting framework costs more attention than the decision.

### Case 2: long-running multi-turn re-entry

Input shape: the original goal, later scope changes, one accepted choice, and a final request after a long research gap.

Desired behavior:

- quote the relevant user turns in time order;
- restore the accepted choice without reopening it;
- distinguish `still true`, `changed`, `invalidated`, `new`, and `still open` when useful;
- make the current question and judgment visible on the first screen.

Failure signal: a polished answer to only the latest message, or a transcript replay that hides the current decision.

### Case 3: incomplete or conflicting evidence

Input shape: the main path is partly verified, but one missing or conflicting fact could reverse the architecture.

Desired behavior:

- answer the parts that are ready;
- name the evidence conflict or gap;
- avoid forcing a smooth verdict;
- identify the smallest check that unlocks the decision;
- say what recommendation is provisional and what would change it.

Failure signal: visual confidence or strong prose makes partial evidence look settled.

### Case 4: user correction changes the frame

Input shape: an earlier interpretation followed by a user correction such as “this Skill only reports; it does not manage collaboration during work.”

Desired behavior:

- quote both the earlier scope and the correction when both matter;
- make the scope delta explicit;
- drop conclusions that depended on the rejected frame;
- report from the corrected boundary without defensive apology or hidden persistence.

Failure signal: the report cosmetically acknowledges the correction while keeping the rejected architecture.

### Case 5: several architecture questions hide one ownership issue

Input shape: SDK, deployment, protocol, session, and UI questions that share vocabulary but live on different axes.

Desired behavior:

- inventory the explicit questions briefly;
- use a spatial map to expose dependency, ownership, or conflict;
- identify the deeper owner or source-of-truth question;
- give one main recommendation and only decision-changing alternatives.

Failure signal: a flat vendor or feature list leaves the reader to discover the architecture.

### Case 6: completion and handoff report

Input shape: the requested change is implemented and verified, with one remaining non-blocking limit.

Desired behavior:

- return to the requested outcome;
- say what now exists and how it was verified;
- distinguish completed work from the remaining limit;
- provide a clickable artifact or file link when useful;
- end with the next useful action rather than another summary.

Failure signal: a chronological work log forces the user to infer whether the task is actually done.

## Evaluation lens

Score each report from `0` to `2` on the six reader costs:

```text
0  reader must reconstruct it
1  usable but some friction remains
2  low-friction cognitive handoff

re-entry · meaning · navigation
verification · cleanup · decision
```

A report should not earn points merely for containing the expected sections. Inspect whether the reader can recover the current problem, trust boundary, and decision with less effort. A shorter report can outperform a richer one.
