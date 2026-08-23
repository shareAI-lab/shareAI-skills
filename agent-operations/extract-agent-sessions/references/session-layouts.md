# Session store layouts

These are observed local implementation patterns, not vendor APIs. Probe every
installation before using them. Treat an unknown shape as unsupported rather than
loosening the human or assistant filters.

In this document, `<home>` means the explicitly resolved profile directory of the
account that ran the agent client. It is not a hard-coded username or the home of a
different account inferred from `sudo`, a service, or a scheduled task.

## Contents

- [Storage map](#storage-map)
- [Discovery indexes](#discovery-indexes)
- [Tree-shaped transcripts](#tree-shaped-transcripts)
- [Rollout-shaped transcripts](#rollout-shaped-transcripts)
- [Relational-shaped transcripts](#relational-shaped-transcripts)
- [ACP-stream-shaped transcripts](#acp-stream-shaped-transcripts)
- [Recency and low-context analysis](#recency-and-low-context-analysis)
- [Externalized content and corruption](#externalized-content-and-corruption)

## Storage map

| Purpose | Tree-shaped store | Rollout-shaped store | Relational-shaped store | ACP-stream-shaped store |
|---|---|---|---|---|
| Observed product family | Claude Code | Codex CLI/Desktop | opencode CLI/TUI (observed at 1.18.x) | Grok Build CLI/TUI (observed at `chat_format_version` 1) |
| Data root | `<home>/.claude` | `<home>/.codex` | `<home>/.local/share/opencode` (XDG data dir; honors `XDG_DATA_HOME`; dev channels suffix the name — probe `opencode*`) | `$GROK_HOME` when set and non-empty (used verbatim), otherwise `<home>/.grok` |
| Recent-input index | `history.jsonl` | `history.jsonl` | `session` table inside `opencode.db` | `summary.json` inside each session directory |
| Root transcript | `projects/<encoded-workdir>/<session-id>.jsonl` | `sessions/YYYY/MM/DD/rollout-...-<thread-id>.jsonl` | `message` + `part` rows for sessions with NULL `parent_id` | `sessions/<encoded-cwd>/<session-id>/updates.jsonl` |
| Child transcript | `<root-session>/subagents/**/*.jsonl` | Separate rollout whose first metadata record identifies a subagent | Sessions with non-NULL `parent_id` (task-tool subagents) | Sibling session directory whose `session_kind` starts with `subagent` |
| Optional path index | None required | `state_*.sqlite`, if present and opened read-only | `project` table; `<home>/.local/state/opencode/prompt-history.jsonl` is raw typed input — avoid by default | `sessions/session_search.sqlite` FTS (`title`/`content` are conversation text — never select them); per-cwd-group `prompt_history.jsonl` is raw typed input — avoid by default |

These relative layouts have been observed under Linux and macOS homes. Do not
assume that a desktop app, CLI, container, WSL distribution, or remote host shares
another environment's data root. Native Windows stores are outside this version's
supported scope.

## Discovery indexes

Observed tree-store history fields include:

```text
sessionId
timestamp       Unix milliseconds
project
display
```

Observed rollout-store history fields include:

```text
session_id
ts              Unix seconds
text
```

Observed relational-store `session` columns include:

```text
id, parent_id, project_id
title, directory                private, like display/project above
time_created, time_updated,
time_archived                   Unix milliseconds
revert                          JSON marker or NULL
share_url                       non-NULL when the session was shared
agent, model
```

Observed ACP-stream `summary.json` fields include:

```text
info.id, info.cwd               cwd is private, like project/directory above
created_at, updated_at,
last_active_at                  RFC3339 strings; last_active_at may be absent
session_kind                    absent on ordinary roots; "subagent*" on children
parent_session_id               set on forks; treat as an independent root
hidden                          optional visibility override
generated_title, session_summary,
last_turn_summary, last_recap   private display text
num_messages, num_chat_messages
chat_format_version             observed 1
```

Use these indexes only to obtain candidate IDs and recent human-input times. Keep
`project`, `display`, `text`, `title`, `directory`, `generated_title`,
`session_summary`, and `info.cwd` private; do not show them in the default
inventory. An entry with no transcript can be a command-only interaction. The
ACP-stream FTS file `session_search.sqlite` duplicates titles and prompt text;
do not use it as a discovery index.

Before relying on the field names or units, inspect key sets and numeric ranges.

## Tree-shaped transcripts

### Root and child identity

- Accept root files directly under `projects/<encoded-workdir>/`.
- Reject any path containing a `subagents` component.
- Do not group only by `sessionId`; child records can reuse a parent's ID.
- Treat `isSidechain=true`, `agentId`, peer origins, and task notifications as child
  or synthetic evidence, not user conversation.
- Use `cwd` or history `project` only for private local resolution. Do not expose it
  in inventories or shareable reports.

### The transcript is a tree

Observed nodes use `uuid` with `parentUuid`. Editing, retrying, or regenerating can
create sibling branches, so chronological filtering can include abandoned prompts
and replies.

Observed compact boundaries can reset `parentUuid` while retaining the prior link
in `logicalParentUuid`. Define the effective parent as:

```text
parentUuid if present, otherwise logicalParentUuid
```

To recover an active path:

1. Build a minimal UUID-to-parent map without message bodies.
2. Identify leaves as UUIDs that are not an effective parent of another main-path
   node.
3. Prefer an explicit active-leaf marker when the current schema provides one.
4. Use `last-prompt.leafUuid` only as corroboration or fallback; an active writer can
   leave it behind the newest assistant node.
5. If selecting the newest leaf by append order, mark that choice as a heuristic and
   verify that the last-prompt marker is on its ancestry.
6. Walk effective parents to the root, detect cycles or missing parents, then reverse
   the UUID list.
7. If multiple plausible active leaves remain, stop and report branch ambiguity.

### Human allow-list

For the currently observed shape, require all of:

```text
type == user
message.role == user
isSidechain != true
origin.kind == human OR promptSource in {typed, queued}
```

For string `message.content`, preserve the string. For an array, preserve only
ordered blocks whose `type` is `text`.

Exclude tool results, compact summaries, task notifications, peer messages, stop
hooks, local-command wrappers, system-origin user strings, and ambiguous strings
without evidence of human origin.

### Assistant allow-list

For the currently observed shape, require:

```text
type == assistant
message.role == assistant
isSidechain != true
message.content[].type == text
```

Preserve text blocks in active-path order. Exclude thinking, redacted thinking,
signatures, tool use, tool results, system records, summaries, and attachments.

Do not require `stop_reason=end_turn`; visible progress can accompany tool use. Do
not deduplicate by `message.id`; distinct nodes in one model message can carry
different visible blocks. Do not deduplicate repeated text content.

Start a logical round at each accepted human message and attach subsequent accepted
assistant text until the next human message. Synthetic records do not start rounds.

## Rollout-shaped transcripts

### Root and child identity

Use the first `session_meta` envelope as the rollout's identity. A child rollout can
copy later metadata and parent history, so using the last metadata record can count
one conversation multiple times.

Observed metadata fields include:

```text
payload.id
payload.session_id
payload.thread_source
payload.parent_thread_id
payload.forked_from_id
payload.agent_path
payload.source
payload.cwd
payload.timestamp
```

Treat `thread_source=subagent`, a structured `source.subagent`, an agent path, or a
parent-thread marker as child evidence. Do not rely on titles or first-user-message
fields because children can inherit them. Keep actual IDs and cwd private.

### Human allow-list

For the currently observed shape, use only:

```text
envelope type == event_msg
payload.type == user_message
payload.message
```

Do not use every `response_item` with `role=user`; that channel can carry agent
instructions, environment context, summaries, rollback notices, and child-agent
notifications.

Keep attachment presence and counts by default. In private-full mode, preserve
`text_elements`, `images`, and `local_images` only after warning that local paths,
URLs, or data URIs may be sensitive.

### Assistant allow-list

For the currently observed shape, use only:

```text
envelope type == response_item
payload.type == message
payload.role == assistant
payload.content[].type == output_text
```

Preserve content-block order and `payload.phase`, commonly `commentary` or
`final_answer`.

Do not additionally emit `event_msg/agent_message` when the authoritative response
item is present; it is an observed mirror and can be shorter. Recheck an actively
written file before using an unmatched mirror as a fallback. Treat an unknown pair
of canonical and mirror channels as schema ambiguity rather than silently dropping
one.

Exclude reasoning, agent-reasoning events, function calls and outputs, custom tool
calls and outputs, inter-agent messages, token counts, world state, and context
summaries.

### Turn state

Observed lifecycle evidence includes:

```text
task_started or turn_context.turn_id    turn begins
task_complete                           completed
turn_aborted                            aborted
EOF without a terminal event            open or stale-incomplete
```

A human can steer an active task without starting a new task. Preserve chronology
instead of inventing a strict one-question/one-answer mapping.

## Relational-shaped transcripts

Observed at opencode 1.18.x. The store is one SQLite database, `opencode.db`, in
WAL mode with foreign keys on. A running client commits continuously, and the
extracting agent may itself be that client, so open read-only and verify
settlement with row counts rather than file identity.

### Store access and safety

- Open read-only (`node:sqlite` `{ readOnly: true }`, or `sqlite3` with a
  `file:...?mode=ro` URI). Never attach, vacuum, checkpoint, or write.
- The bundled SQLite may reject double-quoted string literals; quote SQL string
  values with single quotes only.
- The same database contains credential-bearing tables (`account`,
  `account_state`, `control_account`, `credential`) and sits next to
  `auth.json`. Never open those tables or that file. Query only `session`,
  `message`, `part`, and, for structure alone, `migration`.
- Conversation content is duplicated into a durable `event` log
  (`aggregate_id` = session ID) and can also appear in projection tables such
  as `session_message`. Treat `message` + `part` as the canonical transcript
  and do not extract from the duplicates. If `session_message` is populated
  where `message` is empty, treat the layout as drifted and re-fingerprint.
- The database file has been observed world-readable. Keep extracted artifacts
  owner-restricted and do not copy the database elsewhere.

### Root and child identity

- Root: `parent_id IS NULL`. Subagent child: `parent_id` set (created by the
  task tool). Children can nest when the configured depth limit is raised, so
  resolve lineage recursively instead of checking one level.
- A task tool part on the parent side records the child session reference in
  its state metadata; use it only for private stitching when the user asks to
  include subagent transcripts.
- Forks deep-copy an ancestor's messages into a new session with fresh message
  and part IDs; `parent_id` stays NULL and lineage survives only in a title
  naming convention. Treat forked sessions as independent roots and report
  possible duplication instead of merging or deduplicating.
- `time_archived` marks archived sessions; report the state instead of
  silently skipping.

### Message and part model

Message rows carry role and turn metadata as JSON in a `data` column; visible
text lives in `part` rows joined by `message_id`. Observed part types:

```text
text          visible text; flags: synthetic, ignored
reasoning     model chain-of-thought, persisted as plaintext
tool          call state: status, input, output, metadata
step-start    model step boundary
step-finish   usage, cost, stop reason
file | patch | snapshot | agent | subtask | retry | compaction   auxiliary
```

Assistant `message.data.parentID` references the user message that opened the
turn; use it for turn grouping. Message IDs sort chronologically within a
session; order by `time_created`, then `id`. Timestamps are Unix milliseconds.

### Human allow-list

For the currently observed shape, require all of:

```text
message.data.role == user
part.data.type == text
part.data.synthetic != true
part.data.ignored != true
no sibling part of type compaction on the same message
```

A user message carrying a compaction part is a compaction trigger, machinery
rather than human input.

### Assistant allow-list

For the currently observed shape, require all of:

```text
message.data.role == assistant
message.data.summary != true      (summary rows are compaction output)
part.data.type == text
```

Exclude reasoning, tool, step, retry, file, patch, snapshot, and compaction
parts. Count excluded compaction summaries in the report.

### Revert, compaction, and externalized output

- `session.revert`, when non-NULL, holds a marker (`messageID`, optional
  `partID`). Rows at or beyond the marker are staged for deletion and vanish
  once the user continues; label them `reverted` in extractions instead of
  silently including or dropping them.
- Compaction appends: a trigger user message (compaction part) and a summary
  assistant message (`summary == true`). Older rows stay in the database and
  are merely hidden from model context. Pruned tool parts gain a compacted
  tombstone timestamp inside their state while keeping their text.
- Oversized tool output is truncated in the part (head and tail preserved,
  placeholder sentence in between) and externalized to `tool-output/tool_<id>`
  files under the data root. Those files expire on a short retention sweep;
  report missing externalized output as unavailable rather than lost data
  corruption.

### Turn state

Relational rows have no lifecycle envelope. Completion evidence comes from the
assistant message's finish metadata and its step-finish parts; an assistant
message without them is open or interrupted. Use accepted human and assistant
`time_created` for recency, and `session.time_updated` only as a fallback hint.

### Legacy JSON layout

Older installs used JSON files under `<data-root>/storage/` (per-project
`session/info`, `message`, and `part` directories, later flattened to
`storage/{session,message,part}/`). If `opencode.db` is absent but `storage/`
exists, fingerprint that layout before use and expect migration marker files
alongside it.

## ACP-stream-shaped transcripts

Observed in Grok Build (`grok`) under the grok home: `$GROK_HOME` when that
environment variable is set and non-empty (the binary uses the value verbatim),
otherwise `<home>/.grok`. Session directories live at:

```text
<grok-home>/sessions/<encoded-cwd>/<session-id>/
```

The cwd component is URL-encoded when the encoded name is at most 255 bytes.
Longer paths use `{slug}-{blake3-hex16}` and store the original path in a `.cwd`
file inside the group directory. Do not decode cwd names for inventory display.
Session IDs are UUIDs (commonly UUIDv7). Adjacent files such as
`auth.json`, `config.toml`, `system_prompt.txt`, and `rewind_points.jsonl`
are outside the conversation allow-list.

`updates.jsonl` is the authoritative conversation log (ACP session updates plus
xAI extension updates). `chat_history.jsonl` is the model-facing snapshot: it
is rewritten on compact and rewind, and it mixes real user turns with synthetic
rows (`synthetic_reason` values such as `system_reminder`,
`project_instructions`, `compaction_meta`). Extract visible text from
`updates.jsonl`. If that file is missing or empty, report the ACP stream as
unavailable rather than falling through to `chat_history.jsonl`.

### Store files

```text
summary.json              discovery index; one JSON object
updates.jsonl             canonical transcript; append-only JSONL
chat_history.jsonl        model context; rewritten; includes synthetics
events.jsonl              lifecycle telemetry (phase_changed, tool_started, ...)
prompt_context.json
system_prompt.txt         system injection — never extract as conversation
rewind_points.jsonl       file snapshots (source); never dump
signals.json, plan.json, announcement_state.json
compaction_checkpoints/   compacted model-view blobs, not the ACP stream
subagents/<child-id>/     metadata only (meta.json includes the child prompt)
terminal/, web_fetch/     tool sidecars
```

The cwd group may also contain `prompt_history.jsonl` (typed prompts, including
bash). Treat it like the relational family's prompt-history file: avoid by
default.

### Envelope

Each `updates.jsonl` line is:

```text
timestamp     Unix seconds (int)
method        "session/update" | "_x.ai/session/update"
params        { sessionId, update, _meta? }
```

Legacy lines without the envelope wrapper are raw ACP notifications. Fingerprint
`method` and `params.update.sessionUpdate` before reading text. Observed ACP
`sessionUpdate` values include `user_message_chunk`, `agent_message_chunk`,
`agent_thought_chunk`, `tool_call`, `tool_call_update`, `plan`. Observed xAI
extension values include `turn_completed`, `rewind_marker`, `retry_state`,
`session_recap`, `subagent_spawned`, `subagent_finished`,
`auto_compact_started`, `auto_compact_completed`, `compaction_checkpoint`.
Collapse any other discriminant to `unknown-string`.

### Root and child identity

- Accept a directory that contains `summary.json` whose `info.id` equals the
  directory basename.
- Reject any path whose components include `subagents`: that tree holds child
  metadata (`meta.json`, `output.json`), while the child transcript is a
  sibling session directory in the same cwd group.
- Child: `summary.session_kind` starts with `subagent` (observed
  `subagent`, `subagent_fork`, `subagent_resume`). `Summary::is_hidden`
  defaults to that prefix unless `hidden` is an explicit boolean.
- Ordinary roots omit `session_kind`. Forks of a parent conversation may set
  `session_kind` to `fork` and `parent_session_id`; treat them as independent
  roots and report possible duplication instead of merging.
- Worktree sessions may set `session_kind` to `worktree` and
  `source_workspace_dir`; they are roots.
- Keep `info.cwd`, titles, recaps, and `grok_home` private.

### Human allow-list

Require all of:

```text
method == "session/update"
params.update.sessionUpdate == "user_message_chunk"
params.update.content.type == "text"
params.update.content.text is a string
params.update._meta.hostTurn is not true
params.update.content._meta.bash_command is absent
```

Then reconstruct counted user runs, matching the store's resume collector:

1. Concatenate consecutive matching chunks until a non-user event or a
   `promptIndex` change opens a new run.
2. Until the first `_meta.promptIndex` appears, every user run counts. After
   that, drop unmarked runs (mid-turn phantoms omit the marker).
3. On `_x.ai/session/update` with `sessionUpdate == "rewind_marker"`, flush the
   current run, then truncate the surviving stream at the start of counted
   prompt `target_prompt_index` (keep the first N counted user runs and the
   non-user events that preceded the discarded runs). `updates.jsonl` is
   append-only; rewind records a branch rather than deleting earlier lines.
4. Skip empty trimmed runs.

`user_message_chunk` with a non-text content block (for example an image) ends
the current run; count it as an attachment rather than a human text message.

### Assistant allow-list

Require:

```text
method == "session/update"
params.update.sessionUpdate == "agent_message_chunk"
params.update.content.type == "text"
```

Concatenate consecutive matching chunks in order with no added separator (ACP
chunks are contiguous fragments). Flush the buffer on any other ACP update or
any `_x.ai/session/update`. Exclude `agent_thought_chunk`, tool calls, plan
entries, recaps, compaction machinery, retry state, and subagent spawn/finish
events.

### Turn state

```text
_x.ai/session/update + sessionUpdate == "turn_completed"
  stop_reason == "end_turn"     completed
  stop_reason == "cancelled"    aborted
EOF without turn_completed      open or stale-incomplete
```

Use `turn_completed` only for state. Compaction checkpoints rewrite
`chat_history.jsonl`; they leave historical `user_message_chunk` rows in
`updates.jsonl`.

### Recency

Prefer the last accepted human or visible-assistant envelope `timestamp` (Unix
seconds). Fall back to `summary.last_active_at`, then `summary.updated_at`
(RFC3339). Ignore `events.jsonl` and FTS `updated_at` as discussion recency.

## Recency and low-context analysis

Use the maximum accepted human or visible-assistant timestamp for transcript
activity. Ignore mtime, tool-result time, summaries, telemetry, and notification
time as discussion recency.

For topic analysis:

1. Read every selected human message.
2. Read final answers for completed turns.
3. Add visible progress when no final answer exists or the turn is open/aborted.
4. For tree-shaped, relational, and ACP-stream stores without phase labels, use
   the last assistant text before the next human message as a compact view while
   retaining the complete private artifact.

## Externalized content and corruption

- Preserve placeholders such as `[Pasted Content ...]` and `[Image #1]` in private
  full exports, but do not claim to recover content the store did not persist.
- Parse JSONL one record at a time. A record can itself be large, so streaming memory
  is bounded by the largest record, not zero. Read physical `\n`-delimited lines from
  the file object; `str.splitlines()` splits on Unicode separators that can appear
  inside JSON strings.
- Treat a malformed middle line as corruption.
- Retry a malformed final line only when file identity, size, or mtime shows an
  active write.
- If the schema fingerprint differs from every known allow-list, report unsupported
  schema and stop before reading content values.
