# opencode Conversations

Use this file only for opencode's relational store.

## Typical location

- Data root: `${XDG_DATA_HOME:-~/.local/share}/opencode`
- Database: `<data-root>/opencode.db`

## Time index

The `session` table is the discovery index. Important fields are:

```text
id, parent_id, project_id
time_created, time_updated, time_archived    Unix milliseconds
revert
```

Use `session.time_updated` to discover recent candidates. For a selected conversation,
prefer accepted `message.time_created` values as the discussion clock.

## Fast path

Use one read-only batch query to select in-window root sessions and fetch their ordered
message and part rows. Filter roles and part types while iterating the result, emitting
one capsule per root session. Avoid per-session and especially per-message SQL queries.
Inspect the schema once only if the observed database differs from the fields below.

## Conversation reconstruction

The canonical relationship is:

```text
session -> message -> part
```

Root conversations normally have no `parent_id`; task-tool subagents have a parent.
Read messages and parts in stored order. Keep user and assistant text parts that are
not synthetic, ignored, compaction output, or tool data.

Observed human relationship:

```text
message.data.role == user
part.data.type == text
part.data.synthetic != true
part.data.ignored != true
```

Observed visible AI relationship:

```text
message.data.role == assistant
message.data.summary != true
part.data.type == text
```

Respect session revert markers by excluding or clearly labeling reverted messages.
Use the session's update time for recency. Treat event or projection tables as derived
views when the canonical message and part rows already contain the visible text.
