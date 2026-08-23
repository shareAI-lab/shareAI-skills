# Cursor Conversations

Use this file only for Cursor composer or agent conversations.

## Typical locations

- Global state: Cursor `User/globalStorage/state.vscdb`
- Discovery index: `User/globalStorage/conversation-search.db`
- Optional agent transcript projection: `~/.cursor/projects/**/agent-transcripts/`

The application-support root is usually below `~/Library/Application Support/Cursor`
on macOS and `~/.config/Cursor` on Linux.

## Conversation reconstruction

Use `conversation-search.db` and `composerHeaders` to discover recent composers. Read
canonical bodies from `composerData:<id>` and `bubbleId:<composerId>:<bubbleId>`, or
from a non-empty `agent-transcripts/<id>/<id>.jsonl` projection when that is the only
complete visible channel.

Composer bubble type `1` is the human side; type `2` contains the assistant side when
text is present. Exclude tool payloads, internal reasoning, drafts, subagent composers,
empty sessions, and synthetic user rows such as automatic follow-up instructions or
MCP catalog injections.

Cursor can retain forks or duplicate composer roots. When two roots begin with the
same accepted human prompt, review the longer or newer continuation and mention that
a duplicate branch existed rather than counting both as separate workstreams.
