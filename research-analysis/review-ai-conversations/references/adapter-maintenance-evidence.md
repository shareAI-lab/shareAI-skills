# Adapter Maintenance Evidence

Do not load this file during ordinary conversation review. Read it only when updating,
debugging, or re-verifying the product adapters.

Research date: 2026-08-23. Evidence order was current local Store shape and current
source/tests, then official documentation and history, then maintainer issues and
corroborating third-party implementations. Local inspection was read-only and recorded
schema, types, counts, and relationships rather than conversation bodies.

```text
local current Store
  + version-pinned source or package
  + official docs/history
  + issue or independent implementation when needed
  -> concise adapter contract
```

## Claude Code

Verified local target:

- Claude Code `2.1.215`; transcript sample versions `2.1.118-2.1.215`.
- 2,813 prompt-history rows, 190 history session IDs, 39 root transcripts, and
  1,011 child transcripts under the sampled home.
- Release tag `v2.1.215`, commit `015170d3fd84fb57ef4685a64b673fadd0690dc1`.

Decisive evidence:

- `[DOC]` [Session storage and internal-schema warning](https://code.claude.com/docs/en/sessions)
- `[DOC]` [Child Agent transcript behavior](https://code.claude.com/docs/en/subagents)
- `[HIST]` [Claude Code v2.1.215 release](https://github.com/anthropics/claude-code/releases/tag/v2.1.215)
- `[ISSUE]` [Compaction boundary and transcript-only summary evidence](https://github.com/anthropics/claude-code/issues/82509)
- `[ISSUE]` [Retry-created sibling branch boundary](https://github.com/anthropics/claude-code/issues/66824)

Findings that changed the adapter:

- `history.jsonl` is prompt history, not an exhaustive Session catalog.
- `origin:human` and `promptSource:typed|queued|sdk` are strong signals, not mandatory
  fields for every retained historical/remote human message.
- `last-prompt.leafUuid` is the best observed active-branch anchor.
- `logicalParentUuid` is used at `system/compact_boundary`; the following
  `isCompactSummary` user record is derived context.
- Root branches and forked child Agents are distinct mechanisms.

Confidence: strong for paths, time units, visible block types, and compaction record
pair; medium-strong for the active-leaf strategy; partial for automatically relating
independent branch roots when no explicit relation survives. Exact parser source is not
public, so runtime/package markers do not justify source-identical claims.

## Codex CLI and Desktop

Verified local target:

- `codex-cli 0.148.0`.
- Official tag `rust-v0.148.0`, commit
  `3ba0f711642a888aec92a611a3f3b2211157ff89`, 2026-08-18.
- Current source snapshot during audit: `c9b19deb09c1841ce7acc33ddb96276030936a29`.
- Local `history.jsonl` covered only 173 IDs while `state_5.sqlite.threads` covered
  roughly 1,780 threads; `thread_history_1.sqlite` was a partial projection.

Decisive source:

- `[CODE]` [Optional input-history contract](https://github.com/openai/codex/blob/rust-v0.148.0/codex-rs/message-history/src/lib.rs)
- `[CODE]` [Name-only session index](https://github.com/openai/codex/blob/rust-v0.148.0/codex-rs/rollout/src/session_index.rs)
- `[CODE]` [Legacy versus paginated persistence policy](https://github.com/openai/codex/blob/rust-v0.148.0/codex-rs/rollout/src/policy.rs)
- `[CODE]` [Rollout lineage reader](https://github.com/openai/codex/blob/rust-v0.148.0/codex-rs/thread-store/src/local/rollout_lineage.rs)
- `[CODE]` [SessionMeta history-base fields](https://github.com/openai/codex/blob/rust-v0.148.0/codex-rs/protocol/src/protocol.rs)
- `[CODE]` [Child history materialization boundary](https://github.com/openai/codex/blob/rust-v0.148.0/codex-rs/thread-store/src/local/thread_history_materialization.rs)
- `[ISSUE]` [Maintainer explanation of canonical paginated messages](https://github.com/openai/codex/issues/38169)
- `[ISSUE]` [Legacy fork copied-history behavior](https://github.com/openai/codex/issues/35647)
- `[DOC]` [Official Codex changelog](https://learn.chatgpt.com/docs/changelog)

Findings that changed the adapter:

- State DB discovery outranks `history.jsonl`; SQLite-selected `rollout_path` matters
  after revert because one stable thread can have multiple immutable rollouts.
- Paginated history uses `item_completed` UserMessage/AgentMessage; reading only legacy
  `event_msg.user_message` loses current Desktop prompts.
- `response_item.role=user` is model input and may contain injected context.
- A logical thread can span a recursively linked `history_base` rollout chain.
- The first physical `session_meta`, `thread_source`, structured `source.subagent`,
  parent/fork fields, and child ordinal boundary must be considered together.
- `compacted.replacement_history` is model context, not original testimony.

## opencode

Verified targets:

- Local `1.18.4`, tag commit `49c69c5ed3ccf706b61b3febb43c8aaff7f8325e`.
- Stable `1.18.21`, commit `826d9ad46a22bef0294998e08daa3c4904fea28f`.
- Upstream dev snapshot `9d466cd8497d02db40010077201e07bd10ac33b4`.
- Local DB used V1: 9,356 messages and 53,945 parts; V2 tables existed but were empty.

Decisive evidence:

- `[DOC]` [CLI database commands](https://dev.opencode.ai/docs/cli/)
- `[CODE/HIST]` [V1-to-V2 message conversion PR](https://github.com/anomalyco/opencode/pull/40723)
- `[ISSUE]` [Fork parent-ID gap signal](https://github.com/anomalyco/opencode/issues/16639)
- `[ISSUE]` [Ordering and assistant-sibling boundary](https://github.com/anomalyco/opencode/issues/30809)

Findings that changed the adapter:

- `opencode db path` is more accurate than assuming one XDG location.
- V1 and V2 may coexist during incremental migration; choose the populated projection
  per selected session and never merge both bodies for one session.
- V1 `parent_id` identifies child/task sessions, while V1 forks are new top-level
  sessions with cloned and re-IDed history.
- A user-message `summary` object is diff metadata; only assistant
  `summary === true` marks the derived compaction summary.
- V1 revert has message and optional part boundaries; V2 has an ordered `seq` contract.

## Grok Build

Verified targets:

- Local `grok 1.0.5 (5115b46bc9)`.
- Official source snapshot `07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8`,
  source version `1.0.8`, 2026-08-23.
- First public 1.0.5-era snapshot checked:
  `9fabadea800fa6e2ed8ec91c4f45f02b7e2504f4`.

Decisive source:

- `[CODE]` [Authoritative update Store and derived chat cache](https://github.com/xai-org/grok-build/blob/07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8/crates/codegen/xai-grok-shell/src/session/storage/mod.rs)
- `[CODE]` [Summary fields](https://github.com/xai-org/grok-build/blob/07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8/crates/codegen/xai-grok-shell/src/session/persistence.rs)
- `[CODE]` [Human-only prompt history](https://github.com/xai-org/grok-build/blob/07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8/crates/codegen/xai-grok-shell/src/session/prompt_history.rs)
- `[CODE]` [Rewind projection](https://github.com/xai-org/grok-build/blob/07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8/crates/codegen/xai-grok-shell/src/session/acp_session_impl/rewind.rs)
- `[CODE]` [Child Agent relation metadata](https://github.com/xai-org/grok-build/blob/07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8/crates/codegen/xai-grok-shell/src/agent/subagent/mod.rs)
- `[DOC]` [Bundled Session guide](https://github.com/xai-org/grok-build/blob/07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8/crates/codegen/xai-grok-pager/docs/user-guide/17-sessions.md)

Findings that changed the adapter:

- Per-cwd `prompt_history.jsonl` is the fastest authority signal for original human
  prompts; it must still be reconciled with the active rewind projection.
- `params._meta.agentTimestampMs` outranks envelope `timestamp`, which fork copying can
  rewrite.
- Display metadata can preserve the user's slash/skill-facing text when wire text is an
  expansion.
- Assistant chunks can be separated by tool/thought events; group by prompt ID and
  `turn_completed`, not adjacency.
- Root forks preserve the original event ID while rewriting the envelope time; use
  lineage plus event ID for copied-prefix deduplication.
- Child parentage normally comes from parent-side `subagents/<child>/meta.json`, not the
  child's summary.
- `chat_history.jsonl` and checkpoint summaries are derived model-context material.

## Cursor IDE and Agent CLI

Verified target and limitation:

- Local Cursor Agent CLI `2026.08.11-e8db854` package was inspected.
- No local Cursor GUI Store was present; IDE claims were cross-checked against current
  implementations, Cursor documentation/changelog, and Store-analysis projects.

Decisive evidence:

- `[DOC]` [Cursor local chat history](https://docs.cursor.com/en/agent/chat/history)
- `[HIST]` [Cursor 3.11 Side Chat and local search](https://cursor.com/changelog/side-chat)
- `[OBSERVED]` [Current IDE Store catalog](https://github.com/tony/agentgrep/blob/893905e6a12596cd4baf980903e338c9cd6f343b/src/agentgrep/store_catalog/cursor_ide.py)
- `[OBSERVED/HIST]` [Cursor Store migration notes](https://github.com/Callum-Ward/cursaves/blob/2919739d35a043f1f35979a758f87d4c936a42b7/docs/how-cursor-stores-chats.md)
- `[OBSERVED]` [Side Chat lineage fields](https://github.com/datadog-labs/trajectory/blob/ed6f7b655970e032f1a403234c282f2333087e0f/docs/SUPPORTED-CLIENTS.md)
- `[ISSUE]` [Maintainer statement that search DB cannot reconstruct state DB](https://forum.cursor.com/t/unable-to-restore-conversations-from-original-37-gb-state-vscdb-database-request-for-assistance/165794/6)
- `[DOC]` [Cursor CLI slash commands](https://cursor.com/docs/cli/reference/slash-commands)

Findings that changed the adapter:

- Cursor IDE and Cursor Agent CLI have separate state Stores, while either can write the
  shared `agent-transcripts` projection.
- `conversation-search.db` is a derived candidate/FTS cache, not body truth.
- Current IDE body ordering follows `fullConversationHeadersOnly` to batch-fetched
  bubble keys; bubble-by-bubble SQL is an avoidable N+1 path.
- `recency` and `checkpointAt` are not proven activity clocks.
- Current CLI transcript projection can combine assistant thinking and text.
- Side Chat copied-prefix length is explicit; CLI fork parentage may be heuristic.
- A cloud-cache search hit can legitimately lack a complete local conversation body.

## Refresh triggers

Re-run this audit when any of the following changes:

- Claude transcript version, compact-boundary shape, or Session picker behavior.
- Codex `state_*.sqlite` schema version, history mode, or rollout lineage protocol.
- opencode projection population switches from V1 to V2 or explicit fork metadata ships.
- Grok prompt-history/update metadata or rewind projection changes.
- Cursor IDE major Store migration or CLI transcript writer changes.

When refreshing, update the adapter's `Last verified` line and this evidence snapshot.
Do not copy evidence history into ordinary adapter context unless it changes extraction
decisions.
