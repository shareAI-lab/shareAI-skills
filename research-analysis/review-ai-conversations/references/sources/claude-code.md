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

## Fast path

Scan `history.jsonl` once to select in-window root session IDs. Stream each selected
root transcript once: build the parent map, identify the accepted branch, extract
visible turns, record the activity clock, and emit the conversation capsule during
that same pass. Do not first export the tree and then rescan it for messages.

## Conversation reconstruction

Claude transcripts form a tree. Use `uuid`, `parentUuid`, and when present
`logicalParentUuid` to reconstruct the active root conversation path. Do not flatten
sibling branches or count subagents as independent user conversations.

Treat descendants in `subagents/` and sidechain records as derived work attached to
the parent turn. For a fork, keep the shared ancestor once and preserve only the new
human-authored continuation on each relevant branch. Across repeated compaction,
follow logical parents back to original user records; use compaction summaries only to
bridge context epochs when raw ancestors are unavailable.

Keep human messages from user records whose source indicates typed or queued input.
Keep visible text blocks from assistant records. Exclude tool calls, tool results,
thinking, system records, and progress machinery from the visible root timeline.
Read sidechains or subagent transcripts only to attach relevant evidence or artifacts;
never reinterpret their delegated prompts as direct human input.

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

If the active path is ambiguous, include the stable root portion and say that later
branches diverged.
