# Cursor Conversations

Last verified: Cursor Agent CLI `2026.08.11-e8db854`; Cursor IDE Store evidence through
3.15-era implementations, 2026-08-23. IDE and CLI state Stores are separate surfaces;
the `agent-transcripts` projection can be written by either.

## Detect and route

Cursor IDE global storage:

```text
Linux    ~/.config/Cursor/User/globalStorage/
macOS    ~/Library/Application Support/Cursor/User/globalStorage/
Windows  %APPDATA%\Cursor\User\globalStorage\
```

If `state.vscdb`, `conversation-search.db`, or IDE `workspaceStorage` is the selected
source, read [`cursor-ide.md`](cursor-ide.md) completely and do not load the CLI file.

Shared transcript projection:

```text
$CURSOR_DATA_DIR/projects/**/agent-transcripts/
default ~/.cursor/projects/**/agent-transcripts/
```

Read [`cursor-cli.md`](cursor-cli.md) for this JSONL body shape even when Cursor Desktop
created it. If adjacent IDE state exists and exact Side Chat lineage or copied-seed
deduplication matters, also read `cursor-ide.md`.

Cursor Agent CLI-exclusive signals:

```text
cursor-agent executable
resumable state:
  <config-root>/chats/<cwd-hash>/<session>/store.db
  config root = $CURSOR_CONFIG_DIR
             | $XDG_CONFIG_HOME/cursor
             | ~/.cursor
```

If `cursor-agent` or `chats/**/store.db` is selected, read
[`cursor-cli.md`](cursor-cli.md) completely and do not load the IDE file.

If the user says only "Cursor," cheaply probe both IDE and CLI roots. Load only the
subadapter whose Store has in-scope candidates; load both when both are relevant. When
both state surfaces are selected, recover them independently before deduplicating
proven relationships. Never choose only the longest or newest suspected fork: count a
proven shared prefix once and retain each relevant divergent continuation.
