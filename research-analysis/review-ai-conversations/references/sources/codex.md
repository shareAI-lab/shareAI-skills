# Codex Conversations

Last verified: Codex CLI/Desktop `0.148.0`, 2026-08-23. This version supports both
legacy and paginated rollout history; choose the protocol from the first physical
`session_meta`.

## Locations and discovery

- Codex home: `${CODEX_HOME:-$HOME/.codex}`
- Active rollouts: `<home>/sessions/YYYY/MM/DD/rollout-*.jsonl[.zst]`
- Archived rollouts: `<home>/archived_sessions/`
- Current metadata DB: `state_5.sqlite` in the resolved SQLite home
- Optional prompt log: `<home>/history.jsonl`
- Name-update sidecar: `<home>/session_index.jsonl`

Prefer a read-only query of the current state DB:

```sql
SELECT id, rollout_path, recency_at_ms, updated_at_ms,
       source, thread_source, history_mode, archived
FROM threads
WHERE recency_at_ms >= ?
ORDER BY recency_at_ms DESC;
```

The versioned DB filename and schema may drift; inspect available `state_*.sqlite`
tables when `state_5.sqlite` is absent. Validate every candidate from its first physical
`session_meta`. Prefer `thread_source == user`; exclude structured subagent/internal
sources unless requested.

If no usable state row exists, shortlist active and archived rollouts by mtime and read
only their first `session_meta`. Several rollouts may share one stable thread after a
revert; without SQLite's selected path, do not merge them and label current-branch
selection ambiguous.

`history.jsonl` is optional input history `{session_id, ts, text}`, where `ts` is Unix
seconds. It may be disabled, trimmed, or miss Desktop activity, so use it only as a
text-to-thread hint. `session_index.jsonl` indexes names, not conversation activity.

## Identity and rollout lineage

Use the first physical `session_meta` in a rollout:

```text
payload.id                             stable thread ID
payload.session_id                     session lineage; may remain the root ID
payload.thread_source                  user | subagent | internal variants
payload.source                         client source or structured subagent source
payload.forked_from_id                 fork origin
payload.parent_thread_id               direct parent
payload.history_mode                   legacy | paginated
payload.history_base                   inherited paginated prefix
payload.subagent_history_start_ordinal child-local boundary
```

Do not classify from `session_id` or `forked_from_id` alone. A user fork normally keeps
`thread_source == user`; a child uses `thread_source == subagent`, structured
`source.subagent`, or an explicit parent.

Start from SQLite's selected `rollout_path`. For paginated history, follow
`history_base` recursively, reverse the segments into time order, and read each only to
its exclusive ordinal/byte cutoff. Despite its field name, `history_base.thread_id`
identifies a rollout. Never glob every file containing the stable thread ID and merge
them. For child-local work, ignore inherited ordinals before
`subagent_history_start_ordinal`.

## Canonical visible conversation

Branch on `history_mode`:

```text
legacy human:
  event_msg / payload.type == user_message / payload.message
legacy assistant:
  event_msg / payload.type == agent_message / payload.message

paginated human:
  event_msg / payload.type == item_completed
  payload.item.type ~= UserMessage
  payload.item.content[].text
paginated assistant:
  event_msg / payload.type == item_completed
  payload.item.type ~= AgentMessage
  payload.item.content[].text
```

Normalize harmless item-type casing changes and preserve assistant phase when present.
Use `response_item` user/assistant messages only as a compatibility fallback: user-role
model input can contain injected context. Deduplicate fallbacks against canonical item
IDs.

Never recurse into `compacted.payload.replacement_history`; it is a model-context
checkpoint and may repeat roles and summaries. Preserve top-level original messages
across rollout ancestors. Apply `thread_rolled_back` and selected revert lineage to
derive current state. `turn_aborted` marks an incomplete turn but does not remove its
accepted user message. Include an abandoned branch only when relevant and label it.

## Fast path

```text
state DB candidate query
  -> first session_meta validation
  -> required history_base segments only
  -> one forward stream per segment
  -> canonical human/assistant items
  -> fork-prefix alignment from lineage + ordered canonical events
```

For legacy forks, use `forked_from_id`, align the copied canonical-event prefix with the
parent, and use response-item IDs only when available; legacy event messages do not
always carry stable item IDs. Stream `.jsonl.zst` through one decompression pass rather
than materializing and rescanning an intermediate JSONL copy.

Use accepted line RFC3339 timestamps for message activity. Use `recency_at_ms` for
discovery and `updated_at_ms` when completion activity matters. Filename and directory
dates are creation hints. `thread_history_1.sqlite` is an incremental UI projection;
do not use it as the default body unless completeness against the selected rollout and
its full lineage has already been proven.
