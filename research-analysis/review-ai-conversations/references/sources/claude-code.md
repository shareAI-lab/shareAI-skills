# Claude Code Conversations

Use this file only for Claude Code stores.

## Typical locations

- Recent-input index: `~/.claude/history.jsonl`
- Root conversations: `~/.claude/projects/<encoded-workdir>/<session-id>.jsonl`
- Subagents: descendants below a root conversation's `subagents/` directory

## Conversation reconstruction

Claude transcripts form a tree. Use `uuid`, `parentUuid`, and when present
`logicalParentUuid` to reconstruct the active root conversation path. Do not flatten
sibling branches or count subagents as independent user conversations.

Keep human messages from user records whose source indicates typed or queued input.
Keep visible text blocks from assistant records. Exclude tool calls, tool results,
thinking, system records, progress machinery, and sidechain messages.

Compaction may reconnect history through logical parents. If the active path is
ambiguous, include the stable root portion and say that later branches diverged.
