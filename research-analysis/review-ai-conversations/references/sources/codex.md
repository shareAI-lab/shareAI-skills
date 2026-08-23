# Codex Conversations

Use this file only for Codex CLI or Desktop rollout stores.

## Typical locations

- Recent-input index: `~/.codex/history.jsonl`
- Rollouts: `~/.codex/sessions/YYYY/MM/DD/rollout-...-<thread-id>.jsonl`

## Conversation reconstruction

Read the first `session_meta` record to identify the root conversation and reject
explicit subagent rollouts. A fork can contain copied ancestor messages; keep its own
new human turns and avoid counting copied history twice.

Keep canonical human messages from `event_msg` records whose payload type is
`user_message`. Keep visible assistant `output_text` blocks from assistant message
`response_item` records. Exclude tool calls, reasoning, system injection, mirror
events, and copied parent history.

Use lifecycle records only to understand whether a turn completed, stopped, or remains
open. For review, prioritize the user's accepted prompts and the final visible answer
for each completed turn.
