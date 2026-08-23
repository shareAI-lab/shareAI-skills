# Grok Build Conversations

Last verified: local Grok Build `1.0.5` and official source `1.0.8`, 2026-08-23.

## Locations and authority

- Root: `$GROK_HOME`, otherwise `~/.grok`
- Session: `<root>/sessions/<cwd-group>/<session-id>/`
- Metadata: `summary.json`
- Authoritative conversation: `updates.jsonl`
- Human prompt index: `<root>/sessions/<cwd-group>/prompt_history.jsonl`
- Child relation: `<parent-session>/subagents/<child-id>/meta.json`

The cwd group is normally URL-encoded; long paths may use a slug/hash plus `.cwd`.
`chat_history.jsonl` is derived model context and may be rewritten by compaction, so it
cannot replace the original update stream.

## Discovery and activity time

Read matching `summary.json` files once. Observed fields include:

```text
info.id
created_at, updated_at, last_active_at       RFC3339
session_kind, hidden
parent_session_id, fork_parent_prompt_id, inherited_prefix_len  when present
```

Treat a summary as hidden when `hidden == true`, or when `hidden` is absent and
`session_kind` starts with `subagent`; explicit `hidden == false` overrides the kind.

For accepted human and visible AI events prefer
`params._meta.agentTimestampMs` (Unix milliseconds), then envelope `timestamp` (Unix
seconds). Fork copying can rewrite the envelope time while retaining the event clock.
Fall back to `last_active_at`, then `updated_at`.

## Preserve human prompts

Read each selected cwd group's `prompt_history.jsonl` once and filter by `session_id`:

```text
{timestamp, session_id, prompt, is_bash}
```

It records human-authority prompts and excludes child/synthetic turns, but is capped and
may retain a partial live tail. Exclude `is_bash == true` unless requested. Reconcile it
with the rewind-aware update stream rather than forcing history-only rows into the
active timeline.

Accept update text only when:

```text
method == session/update
params.update.sessionUpdate == user_message_chunk
params.update.content.type == text
```

Prefer the user-facing text in this order:

```text
content._meta.combinedDisplayTexts[]
content._meta.displayText
content.text
```

Exclude `update._meta.hostTurn`, `update._meta.hideFromScrollback`, and
`content._meta.bash_command`. Group fragments by `update._meta.promptIndex`.

## Visible AI replies and turns

Accept `agent_message_chunk` text from the same `session/update` shape. Exclude
`agent_thought_chunk`, tools, results, and control updates. Group message chunks by
`params._meta.promptId`; when absent, use the current user turn until:

```text
method == _x.ai/session/update
params.update.sessionUpdate == turn_completed
params.update.prompt_id
```

Tool or thought records may appear between visible chunks, so adjacency is not a turn
boundary.

## Forks, child Agents, rewind, and compaction

Use summary fork fields when present. Root forks may copy ancestor updates while
rewriting session and envelope time; deduplicate a proven copied prefix by lineage plus
the retained `params._meta.eventId`. `inherited_prefix_len` counts derived chat items,
not update turns, so it is not a direct prompt cutoff. For a child Agent, prefer the parent's
`subagents/<child-id>/meta.json`, which can contain `parent_session_id`,
`child_session_id`, `prompt`, `resumed_from`, and context-source fields. Fall back to
the parent's `subagent_spawned` update. The child prompt is delegated work.

Apply every append-only `_x.ai/session/update` `rewind_marker` by truncating accumulated
live turns to the state before its target prompt index, then append the later branch.
Do not derive chronology from `rewind_points.jsonl`.

Only a committed `compaction_checkpoint` proves a new context epoch.
`auto_compact_started/failed/cancelled` are lifecycle signals; `session_recap` and
stored recap summaries are UI-derived reference material. None replaces earlier raw
updates, which remain the canonical original conversation.

## Fast path

```text
summary scan + one prompt-history scan per cwd group
  -> root/child/fork classification
  -> one forward, rewind-aware updates stream per selected session
  -> prompt-index human turns + prompt-ID assistant turns
```
