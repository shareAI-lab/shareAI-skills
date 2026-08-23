# opencode Conversations

Last verified: local `1.18.4`, stable `1.18.21`, and upstream dev on 2026-08-23.
Detect the populated projection before reading; migration-era databases may contain
both V1 and V2 tables.

## Locate the database

Prefer `opencode db path`; it resolves XDG, `OPENCODE_DB`, and channel-specific policy.
If the command is unavailable, try:

```text
${XDG_DATA_HOME:-$HOME/.local/share}/opencode/opencode.db
```

## Choose one projection

Classify all selected session IDs in one batch:

- For each session, use V2 when `session_message` has rows for that session.
- Otherwise use V1 when `message` and `part` have rows for that session.
- Never merge V1 and V2 bodies for the same session; migration may be incremental.

Observed SQL time columns are Unix milliseconds. Use `session.time_updated` to discover
recent sessions; use message clocks for ordering accepted turns.

## Session lineage

`session.parent_id IS NULL` identifies a top-level session; non-null proves a child
relationship. The built-in task tool uses children, but the public creation surface can
also set a parent. Do not presume a child's user-role prompt is human-authored or
delegated without task/subagent evidence. Read child bodies only when requested or when
the parent result is missing or insufficient.

V1 forks are also top-level: the fork implementation clones and re-IDs history without
recording its source in `parent_id`. A `(fork #N)` title plus a matching visible prefix
is only a heuristic. Prefer explicit fork metadata if a later schema provides it.

## V1: message and part

```text
session -> message -> part
```

Human text:

```text
message.data.role == user
part.data.type == text
part.data.synthetic != true
part.data.ignored != true
part.data.text is non-empty
```

Visible assistant text:

```text
message.data.role == assistant
message.data.summary != true
part.data.type == text
part.data.synthetic != true
part.data.text is non-empty
```

Order messages by `(message.time_created, message.id)` and parts by `part.id`. A user
`summary` object is ordinary diff metadata; only assistant `summary === true` marks a
derived compaction summary. A `compaction` part marks a context boundary, not a human
request; original non-synthetic user rows remain primary.

If `session.revert` exists, its `messageID` and optional `partID` start the inactive
branch. Exclude that range by default; include it only for discarded-history review.

## V2: session_message

Order strictly by `seq`:

```text
human:     type == user      -> data.text
assistant: type == assistant -> data.content[type == text].text
```

Skip synthetic, system, shell, compaction, reasoning, and tool records unless asked.
Do not merge `session_input`, `session_context_epoch`, or event rows into the visible
transcript; they are inbox, runner-context, or event representations.

## Fast path

Select in-window root IDs once, then batch-fetch only accepted V1 text/compaction parts
or accepted V2 message types in indexed order. Emit each conversation while streaming;
avoid per-session and per-message queries.

If neither projection matches, sample a few rows. If still ambiguous, use the supported
`opencode export <sessionID>` interface rather than scanning the entire Store.
