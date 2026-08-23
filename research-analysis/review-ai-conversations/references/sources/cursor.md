# Cursor Conversations

Use this file only for Cursor composer or agent conversations.

## Typical locations

- Global state: Cursor `User/globalStorage/state.vscdb`
- Discovery index: `User/globalStorage/conversation-search.db`
- Optional agent transcript projection: `~/.cursor/projects/**/agent-transcripts/`

The application-support root is usually below `~/Library/Application Support/Cursor`
on macOS and `~/.config/Cursor` on Linux.

## Time index

The `conversations` table in `conversation-search.db` provides candidate IDs and
`updated_at` in Unix milliseconds. `composerHeaders` provides `createdAt`,
`lastUpdatedAt`, `recency`, and `checkpointAt`, also in Unix milliseconds.

For a selected composer, prefer the maximum accepted bubble `createdAt`; otherwise
fall back to `composerData.lastUpdatedAt`, `composerHeaders.lastUpdatedAt` or
`recency`, then search-index `updated_at`. JSONL-only transcripts may have no message
timestamp, so report that fallback explicitly.

## Conversation reconstruction

Use `conversation-search.db` and `composerHeaders` to discover recent composers. Read
canonical bodies from `composerData:<id>` and `bubbleId:<composerId>:<bubbleId>`, or
from a non-empty `agent-transcripts/<id>/<id>.jsonl` projection when that is the only
complete visible channel.

Composer bubble type `1` is the human side; type `2` contains the assistant side when
text is present. Exclude tool payloads, internal reasoning, drafts, subagent composers,
empty sessions, and synthetic user rows such as automatic follow-up instructions or
MCP catalog injections.

Observed composer human fields:

```text
bubble.type == 1
bubble.text OR bubble.richText
```

Observed composer visible AI fields:

```text
bubble.type == 2
bubble.text is nonempty
```

For `agent-transcripts`, keep `role == user|assistant` and ordered content blocks whose
`type == text`. Do not merge composer and JSONL channels; choose the more complete
canonical conversation after comparing accepted human-turn counts.

Cursor can retain forks or duplicate composer roots. When two roots begin with the
same accepted human prompt, review the longer or newer continuation and mention that
a duplicate branch existed rather than counting both as separate workstreams.
