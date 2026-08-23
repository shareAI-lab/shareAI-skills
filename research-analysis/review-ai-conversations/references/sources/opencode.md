# opencode Conversations

Use this file only for opencode's relational store.

## Typical location

- Database: `${XDG_DATA_HOME:-~/.local/share}/opencode/opencode.db`

## Conversation reconstruction

The canonical relationship is:

```text
session -> message -> part
```

Root conversations normally have no `parent_id`; task-tool subagents have a parent.
Read messages and parts in stored order. Keep user and assistant text parts that are
not synthetic, ignored, compaction output, or tool data.

Respect session revert markers by excluding or clearly labeling reverted messages.
Use the session's update time for recency. Treat event or projection tables as derived
views when the canonical message and part rows already contain the visible text.
