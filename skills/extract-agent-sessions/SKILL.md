---
name: extract-agent-sessions
description: Recover, export, or summarize recent human and assistant conversations from local agent session stores while excluding tool calls, reasoning, system injection, copied parent history, and subagent noise. Use for recent-session inventories, clean conversation recovery, or topic summaries from tree-shaped `.claude` JSONL stores, rollout-shaped `.codex` JSONL stores, and relational-shaped opencode SQLite stores on Linux or macOS.
---

# Extract Agent Sessions

Use this skill as a storage map and decision guide, not as a stable parser. Treat
all local session layouts as unversioned implementation details. Inspect the files
that exist now, adapt shell commands to their observed shape, and fail closed when
the shape is ambiguous.

Do not create or install a persistent extraction script. Compose one-off commands
from the current filesystem and shell capabilities.

## Safety defaults

- Treat every session log as sensitive. It may contain source code, personal data,
  secrets typed by the user, absolute paths, or credentials echoed by tools.
- Keep discovery local. Never upload a log or extracted artifact unless the user
  explicitly asks for that destination.
- List candidates as temporary aliases such as `S1` and `S2`. Do not display prompt
  previews, project names, working directories, complete IDs, or absolute paths by
  default. Truncation is not redaction.
- Read message bodies only after the requested scope identifies the relevant
  session or the user selects an alias. If content would be sent to another service
  or person, disclose that boundary and obtain confirmation.
- Write private intermediate artifacts only under an owner-restricted temporary
  directory. Remove them on normal exit and interruption unless the user explicitly
  requests a private export.
- Never inspect authentication files, credential stores, environment snapshots,
  shell history, debug logs, telemetry, crash dumps, clipboard data, or browser
  storage for this task.
- A relational store can mix conversations and credentials inside one database
  file. Query only the session, message, and part tables plus structural
  metadata; never read credential-bearing tables such as `account`,
  `account_state`, `control_account`, or `credential`, and never `SELECT *`
  from a table you have not fingerprinted.

## Output modes

Choose one mode before reading conversation bodies:

- **Inventory**: aliases, store family, UTC activity time, transcript availability,
  state, and warnings. This is the default discovery mode.
- **Private full**: every persisted human message and visible assistant text block
  in order. Keep this owner-only and do not claim to redact it.
- **Shareable summary**: themes and outcomes with paths, stable IDs, attachment
  references, secrets, and unnecessary verbatim text removed.

“Lossless” means lossless relative to persisted visible text. Preserve a stored
placeholder such as `[Pasted Content ...]` or `[Image #1]` in private-full mode, but
state that the externalized body is unavailable.

## Select the shell guidance

Resolve the current user's home directory without guessing another user's account.
This version supports Linux and macOS hosts:

- Read [references/posix-shell.md](references/posix-shell.md) and compose commands
  for the shell and utilities actually present.
- JSONL families need a streaming JSON tool such as `jq`. The relational family
  needs a read-only SQLite client instead (`node:sqlite` on Node 22+, or
  `sqlite3` opened with a `mode=ro` URI); open read-only and expect WAL churn
  from a live client.
- Under WSL, treat the Linux distribution as a separate environment and inspect it
  only when the agent client ran there. Native Windows session stores are outside
  this version's supported scope.

Read [references/session-layouts.md](references/session-layouts.md) for the relevant
store family before selecting identity or message fields.

## Workflow

### 1. Freeze a UTC window

Interpret “recent two days” as a rolling 48-hour interval unless the user asks for
calendar days. Capture one `[start, end]` snapshot and apply both bounds throughout
the scan so new writes do not move the reported window.

Use history or visible-message timestamps for discussion recency. Use file size and
mtime only to detect active writes or prioritize fallback inspection; never treat
mtime as the conversation time.

### 2. Discover from small indexes

Inspect keys and timestamp units before filtering the small history indexes. Keep
only the latest in-window entry per session ID in a private candidate map. Display
anonymous aliases and metadata only.

History is a discovery index, not canonical conversation text. It can contain slash
commands, local shell commands, or abbreviated pasted content.

For the relational family, the `session` table is the discovery index: select
identity, lineage, timestamp, and state columns only, and keep `title` and
`directory` private. Its state directory keeps a raw typed-input history file;
avoid it, because it holds prompt text without reliable session mapping.

### 3. Resolve and prove root identity

Resolve transcripts only for selected candidates. Constrain every path to an
approved data root, reject symlinks and unsafe IDs, and compare basenames exactly.

For tree-shaped stores, accept only root-level project transcripts and exclude
every `subagents/` descendant. For rollout-shaped stores, inspect the first
projected `session_meta` before reading later records; reject explicit subagents
before they can contribute copied parent history.

For relational stores, accept sessions whose parent link is NULL as roots and
exclude subagent sessions with a non-NULL parent link, resolving nesting
recursively. Forked sessions duplicate an ancestor's messages under fresh IDs
with lineage recorded only in a naming convention; treat them as independent
roots and report possible duplication instead of merging.

### 4. Fingerprint the schema without content

Project only key names, column names, value types, role/type enums,
content-block or part type names, and counts. Do not print IDs, paths,
timestamps, or text values. Collapse unrecognized enum strings to an
`unknown-string` marker, then compare the fingerprint to the observed patterns
in the reference.

If required identity, parent-link, human, or assistant fields are absent or have an
unknown combination, stop content extraction and report schema drift. Do not guess
which channel contains human-visible text.

### 5. Extract only the selected visible timeline

For a tree-shaped transcript, reconstruct the active UUID path before reading text.
Use both physical and logical parent links so compacted history remains connected.
If the active branch cannot be proven, report the ambiguity instead of merging
sibling branches.

For a rollout-shaped transcript, preserve canonical human messages and assistant
output text. Preserve visible progress and final text in private-full mode, but do
not duplicate mirror events. Use lifecycle records only for state.

For a relational transcript, join messages to parts in stored order and keep
only allow-listed visible text parts. Honor the revert marker by labeling rows
at or beyond it as reverted, and read only the canonical message and part
tables; event logs and projection tables duplicate the same content.

Store attachment presence and counts by default. Preserve local attachment paths or
data only when the user explicitly requests a private full export.

### 6. Minimize model context

Inspect counts first. For a topic summary, load every selected human message and
the final answer for each completed turn. Add visible progress only when a turn has
no final answer, is open/aborted, or the store does not label final answers.

Keep the complete filtered timeline on disk for private-full mode; do not load all
of it into model context merely to produce themes.

### 7. Verify, report, and clean up

Compare source identity, size, and modification time before and after extraction.
If the source changed, discard the artifact and retry once after it settles. Treat
a malformed middle record as corruption; retry an incomplete last line only when
the source was actively changing.

For a live SQLite store, compare the selected session's row count and maximum
update timestamp before and after extraction instead of file identity; WAL
sidecars change constantly, and the extraction may itself run inside the agent
writing the store, so re-check or exclude the currently active session.

Report aliases, exact UTC window, root-session count, command-only exclusions,
subagent exclusions, state, schema warnings, branch/compact ambiguity, and missing
externalized content. Keep original paths and stable IDs only in a private manifest
when needed for local traceability.

Remove temporary artifacts unless the user explicitly chose a private export path.
