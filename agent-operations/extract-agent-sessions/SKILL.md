---
name: extract-agent-sessions
description: Recover, export, or summarize recent human and assistant conversations from local agent session stores while excluding tool calls, reasoning, system injection, copied parent history, and subagent noise. Use whenever the user wants to review, summarize, or extract insights from chats they had on Claude Code, Codex, opencode, Grok Build, or Cursor — including "what did we discuss", "回顾问题", "分析本地会话", and topic summaries. Also use for recent-session inventories and clean conversation recovery from tree-shaped `.claude` JSONL stores, rollout-shaped `.codex` JSONL stores, relational-shaped opencode SQLite stores, ACP-stream-shaped Grok Build `~/.grok/sessions` (or `$GROK_HOME/sessions`) stores, and Cursor-shaped composer/agent stores (`state.vscdb` + `conversation-search.db` + `agent-transcripts`) on Linux or macOS.
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
  session or the user selects an alias. Implicit scope counts: "analyze my
  local Cursor/Claude/Codex data", "回顾最近聊天", "总结 / insights", or
  "最近两天聊了什么" selects every in-window root for that family — do not
  wait for a second alias pick. If content would be sent to another service
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
- An ACP-stream home can mix transcripts with `auth.json` and an FTS index
  (`sessions/session_search.sqlite`) whose `title` and `content` columns are
  conversation text. Never open `auth.json`. Do not query those FTS columns.
  Skip `prompt_history.jsonl`, `system_prompt.txt`, and `rewind_points.jsonl`.
- A Cursor `state.vscdb` mixes composer transcripts with editor secrets in the
  same file. Query only `composerHeaders` and allow-listed `cursorDiskKV` key
  prefixes (`composerData:`, `bubbleId:`). Never read `ItemTable` (it holds
  `secret://`, `mcpOAuth.*`, and admin-auth keys), `agentKv:blob` values,
  `blobEncryptionKey`, or `speculativeSummarizationEncryptionKey`. Never open
  `Cookies`, `Local Storage`, `Session Storage`, or `mcp-oauth-attempts`.

## Output modes

Choose one mode before reading conversation bodies:

- **Inventory**: aliases, store family, UTC activity time, transcript availability,
  state, and warnings. Use this when the user is mapping a store, adding a
  family, or verifying a parser. Counts-only is a gate, not a deliverable.
- **Private full**: every persisted human message and visible assistant text block
  in order. Keep this owner-only and do not claim to redact it.
- **Shareable summary**: themes, outcomes, open questions, and insights, with
  paths, stable IDs, attachment references, secrets, and unnecessary verbatim
  text removed. This is the default when the user wants to review, summarize,
  or learn from chats.

If the user asked for review / 回顾 / 总结 / insights / "分析本地数据" and
did not ask to author or verify the extractor, run a short inventory then
**continue into Shareable summary**. Do not stop at schema fingerprints or
message counts.

“Lossless” means lossless relative to persisted visible text. Preserve a stored
placeholder such as `[Pasted Content ...]` or `[Image #1]` in private-full mode, but
state that the externalized body is unavailable.

## Select the shell guidance

Resolve the current user's home directory without guessing another user's account.
This version supports Linux and macOS hosts:

- Read [references/posix-shell.md](references/posix-shell.md) and compose commands
  for the shell and utilities actually present.
- JSONL families (tree, rollout, ACP-stream, and Cursor agent-transcripts) need
  a streaming JSON tool such as `jq`. The relational and Cursor composer
  families need a read-only SQLite client instead (`node:sqlite` on Node 22+,
  or `sqlite3` opened with a `mode=ro` URI); open read-only and expect WAL
  churn from a live client. ACP-stream rewind reconstruction also needs
  `python3` for the one-off coalescer in `posix-shell.md`.
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

For the ACP-stream family, each session directory's `summary.json` is the
discovery index: read identity, `session_kind`, `hidden`, and timestamp fields
only, and keep `info.cwd`, `generated_title`, `session_summary`, and recaps
private. Per-cwd-group `prompt_history.jsonl` holds prompt text; avoid it. Do
not use `session_search.sqlite` as a discovery index.

For the Cursor family, `conversation-search.db` is the discovery index and
`composerHeaders` is a recent-only overlay. Neither is a complete catalog.
When the user asks for **all** sessions in a window, also scan `composerData`
`createdAt` / `lastUpdatedAt` without reading message bodies. Keep `title`,
`name`, `subtitle`, `workspaceIdentifier`, composer-root `text` / `richText`
(the input draft), FTS `body`, and encoded project directory names private.
`source=cloud-cache` rows have no local composer blob; inventory them without
private-full extraction.

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

For ACP-stream stores, accept a directory whose basename equals
`summary.info.id`. Exclude sessions whose `session_kind` starts with
`subagent`, unless `hidden` is an explicit `false`. Reject any path containing
a `subagents` component (child metadata only; the child transcript is a sibling
directory). Forks may set `parent_session_id` while remaining roots; report
possible duplication instead of merging.

For Cursor stores, accept a composer as a root only when all of these are
absent: `composerHeaders.isSubagent=1`, `composerData.subagentInfo`,
`isBestOfNSubcomposer=true`, and any `agent-transcripts/**/subagents/` path.
Treat `empty-state-draft`, `isDraft=true` with no bubbles, `isEphemeral=true`,
and JSONL files that contain only `turn_ended` / error records as
command-only or failed-empty; exclude them from human-conversation summaries
and report the exclusion count. `subComposerIds` / `subagentComposerIds` on a
parent are child edges, not extra roots.

**Cursor synthetic humans** (observed 2026-08): the client injects
`role=user` rows that are not typed by the owner. Treat as machinery and
exclude from human-conversation summaries (count them):

- text that starts with `Perform any necessary follow-up actions in response
  to the subagent completion above`
- text whose first non-empty tag is `<mcp_server_catalog>`
- after these drops, a root with zero remaining human turns is
  machinery-only; exclude it and report the count

**Cursor fork clusters**: two in-window roots that share the same first
accepted human text (compare after stripping skill-attachment wrappers) are
a fork, not two independent discussions. Keep the longer or later root for
the summary and report the duplicate instead of merging.

### 4. Fingerprint the schema without content

Project only key names, column names, value types, role/type enums,
content-block or part type names, and counts. Do not print IDs, paths,
timestamps, or text values. Collapse unrecognized enum strings to an
`unknown-string` marker, then compare the fingerprint to the observed patterns
in the reference.

If required identity, parent-link, human, or assistant fields are absent or have an
unknown combination, stop content extraction and report schema drift. Do not guess
which channel contains human-visible text. For ACP-stream files, fingerprint
`method` and `params.update.sessionUpdate` plus `content.type`; stop if the
human/assistant pair is not `session/update` + `user_message_chunk` /
`agent_message_chunk` with `content.type == text`. For Cursor, fingerprint
composer `_v` / `conversation` / `fullConversationHeadersOnly` presence and
bubble `type` enums before choosing a channel. Stop if bubble types leave
`{1,2}` or if both the embedded array and the header+KV join are missing.

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

For an ACP-stream transcript, read `updates.jsonl` only. Apply `rewind_marker`
truncation, drop host-turn and bash-command user chunks, coalesce counted
`user_message_chunk` runs and `agent_message_chunk` fragments, and treat
`turn_completed` as lifecycle state. Do not extract `chat_history.jsonl`
(model-facing, rewritten on compact) or `events.jsonl`. If `updates.jsonl` is
missing, report the stream as unavailable.

For a Cursor transcript, choose one canonical channel after fingerprinting —
do not merge channels. Prefer `agent-transcripts/<id>/<id>.jsonl` when that
file exists, is not a failed-empty stub, and the user asked about a recent
agent-mode chat; also prefer it when `fullConversationHeadersOnly` and
`conversation` are empty and no `bubbleId:<id>:` rows exist (JSONL-only).
Otherwise use `composerData` (legacy `conversation[]`, or modern `_v` +
`fullConversationHeadersOnly` joined to `bubbleId:<composerId>:<bubbleId>`).
Keep only human `type==1` text and assistant `type==2` nonempty `text` from
bubbles, or JSONL `role==user|assistant` blocks whose `content[].type==text`,
after dropping Cursor synthetic humans (follow-up template and
`<mcp_server_catalog>` dumps). Exclude `tool_use`, `toolFormerData`, thinking,
composer-root draft `text`/`richText`, `latestConversationSummary`, and
`conversation_fts` body.
JSONL records have been observed without timestamps; use header/`updated_at`
for recency and label that limitation. Human counts should match across
channels when both exist; assistant counts may differ because JSONL keeps
in-progress text that composer stores as tool-only type-2 rows. Report the
mismatch and keep the selected channel.

Store attachment presence and counts by default. Preserve local attachment paths or
data only when the user explicitly requests a private full export.

### 6. Minimize model context

Inspect counts first. For a topic summary, load every selected **accepted**
human message (after synthetic-human filters) and the final answer for each
completed turn. Add visible progress only when a turn has no final answer, is
open/aborted, or the store does not label final answers. If a "13 human
turns" count collapses to three accepted prompts, say so — the raw count is
not the discussion.

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
writing the store, so re-check or exclude the currently active session. Cursor
`state.vscdb` and `conversation-search.db` are live while the desktop app is
open — verify `composerHeaders.lastUpdatedAt` or bubble counts for the
selected composer, not the WAL file mtime.

Report aliases, exact UTC window, root-session count, command-only exclusions,
subagent exclusions, synthetic-human exclusions, fork-cluster duplicates, state,
schema warnings, branch/compact ambiguity, and missing externalized content.
Keep original paths and stable IDs only in a private manifest when needed for
local traceability. A review request is unfinished if this report is all the
user received and no summary of accepted human turns exists.

Remove temporary artifacts unless the user explicitly chose a private export path.
