# Grok Build Conversations

Use this file only for Grok Build's ACP-style stream store.

## Typical locations

- Root: `$GROK_HOME` when set, otherwise `~/.grok`
- Conversation stream: `sessions/<encoded-cwd>/<session-id>/updates.jsonl`
- Metadata: `summary.json` in the same session directory

## Conversation reconstruction

Accept visible user text from `session/update` records tagged
`user_message_chunk`. Accept visible AI text from `agent_message_chunk` records.
Coalesce adjacent fragments into conversational turns.

Exclude host turns, shell-command injections, tools, internal reasoning, and sessions
whose kind identifies a subagent. Apply `rewind_marker` before summarizing so abandoned
branches do not survive into the review.

Use `turn_completed` as lifecycle state. If visible assistant text was emitted in
chunks, concatenate it in stored order without inventing separators.
