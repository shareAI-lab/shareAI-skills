# Codex Conversations

Use this file only for Codex CLI or Desktop rollout stores.

## Typical locations

- Data root: `~/.codex`
- Recent-input index: `~/.codex/history.jsonl`
- Rollouts: `~/.codex/sessions/YYYY/MM/DD/rollout-...-<thread-id>.jsonl`

## Time index

Observed history fields are:

```text
session_id
ts              Unix seconds
text
```

Use `history.jsonl` to discover recent IDs. For a selected rollout, prefer accepted
human or visible assistant record timestamps. Use the dated directory only to narrow
the file search, not as the final conversation clock.

## Fast path

Scan `history.jsonl` once, resolve the selected rollout paths, then stream each rollout
once. Read `session_meta` as it appears and extract visible human/assistant turns into
the capsule in the same pass. Do not run separate scans for identity, timestamps,
questions, and replies.

## Conversation reconstruction

Read the first `session_meta` record to identify the root conversation and reject
explicit subagent rollouts. A fork can contain copied ancestor messages; keep its own
new human turns and avoid counting copied history twice.

Keep canonical human messages from `event_msg` records whose payload type is
`user_message`. Keep visible assistant `output_text` blocks from assistant message
`response_item` records. Exclude tool calls, reasoning, system injection, mirror
events, and copied parent history.

Observed human fields:

```text
type == event_msg
payload.type == user_message
payload.message
```

Observed visible AI fields:

```text
type == response_item
payload.type == message
payload.role == assistant
payload.content[].type == output_text
```

Use lifecycle records only to understand whether a turn completed, stopped, or remains
open. For review, prioritize the user's accepted prompts and the final visible answer
for each completed turn.
