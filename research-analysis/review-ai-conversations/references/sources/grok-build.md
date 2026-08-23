# Grok Build Conversations

Use this file only for Grok Build's ACP-style stream store.

## Typical locations

- Root: `$GROK_HOME` when set, otherwise `~/.grok`
- Conversation stream: `sessions/<encoded-cwd>/<session-id>/updates.jsonl`
- Metadata: `summary.json` in the same session directory

## Time index

`summary.json` is the discovery index. Relevant fields include:

```text
info.id
created_at, updated_at, last_active_at    RFC3339
session_kind, parent_session_id, hidden
```

Each `updates.jsonl` envelope has a Unix-seconds `timestamp`. Prefer the last accepted
human or visible AI envelope timestamp. Fall back to `last_active_at`, then
`updated_at` when the stream has no usable message time.

## Fast path

Read the relevant `summary.json` files once to select root sessions. Stream each
selected `updates.jsonl` once, applying rewind state, coalescing adjacent visible
chunks, recording activity time, and building the capsule together. Do not create an
intermediate concatenated transcript.

## Conversation reconstruction

Accept visible user text from `session/update` records tagged
`user_message_chunk`. Accept visible AI text from `agent_message_chunk` records.
Coalesce adjacent fragments into conversational turns.

Observed human fields:

```text
method == session/update
params.update.sessionUpdate == user_message_chunk
params.update.content.type == text
params.update.content.text
```

Observed visible AI fields:

```text
method == session/update
params.update.sessionUpdate == agent_message_chunk
params.update.content.type == text
params.update.content.text
```

Exclude host turns, shell-command injections, tools, and internal reasoning from the
visible timeline. Do not count sessions whose kind identifies a subagent as new human
conversations; read them only for derived results relevant to the parent. Apply
`rewind_marker` before summarizing so abandoned branches do not survive into the review.

Use `parent_session_id` and `session_kind` to attach forks and subagents to the root
conversation. A child session's prompt is a derived task unless direct human origin is
shown. When rollover or summary updates bridge context epochs, keep earlier raw
`user_message_chunk` text as canonical and treat the bridge summary as derived.

Use `turn_completed` as lifecycle state. If visible assistant text was emitted in
chunks, concatenate it in stored order without inventing separators.
