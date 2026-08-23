# Claude Code Conversations

Use this file only for Claude Code stores.

## Typical locations

- Data root: `~/.claude`
- Recent-input index: `~/.claude/history.jsonl`
- Root conversations: `~/.claude/projects/<encoded-workdir>/<session-id>.jsonl`
- Subagents: descendants below a root conversation's `subagents/` directory

## Time index

Observed history fields are:

```text
sessionId
timestamp       Unix milliseconds
project
display
```

Use `history.jsonl` to discover in-window session IDs. Inside a selected transcript,
prefer the maximum accepted human or visible assistant timestamp. Do not use the
date of the containing directory as conversation time.

## Conversation reconstruction

Claude transcripts form a tree. Use `uuid`, `parentUuid`, and when present
`logicalParentUuid` to reconstruct the active root conversation path. Do not flatten
sibling branches or count subagents as independent user conversations.

Keep human messages from user records whose source indicates typed or queued input.
Keep visible text blocks from assistant records. Exclude tool calls, tool results,
thinking, system records, progress machinery, and sidechain messages.

Observed human fields:

```text
type == user
message.role == user
origin.kind == human OR promptSource in {typed, queued}
message.content string OR ordered text blocks
```

Observed visible AI fields:

```text
type == assistant
message.role == assistant
message.content[].type == text
```

Compaction may reconnect history through logical parents. If the active path is
ambiguous, include the stable root portion and say that later branches diverged.
