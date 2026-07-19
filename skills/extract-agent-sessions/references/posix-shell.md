# Linux and macOS shell examples

Compose these Bash snippets only after probing the current schema. They are examples,
not a persistent parser. They use `jq` 1.6+ when available and avoid GNU-only
`date -d`, `find -printf`, and `stat -c` forms.

If `jq` is absent, use an already-installed streaming JSON parser. Do not print raw
JSONL or install software without permission.

## Contents

- [Safe setup](#safe-setup)
- [Discover candidates](#stream-a-history-index-into-a-private-candidate-file)
- [Resolve one session](#resolve-a-selected-id-without-wildcard-expansion)
- [Prove rollout identity](#prove-rollout-identity-without-exposing-values)
- [Fingerprint the schema](#fingerprint-structure-without-content)
- [Recover a tree branch](#build-a-tree-ancestry-without-bodies)
- [Project visible text](#project-visible-text-privately)
- [Detect concurrent writes](#detect-an-active-write)

## Safe setup

```bash
set -euo pipefail

agent_home=${AGENT_SESSION_HOME:-${HOME:-}}
case "$agent_home" in
  /*) ;;
  *) printf 'Set AGENT_SESSION_HOME to an existing absolute path\n' >&2; exit 2 ;;
esac
[ -d "$agent_home" ] || exit 2
agent_home=$(cd -P -- "$agent_home" 2>/dev/null && pwd -P) || exit 2

window_end_s=$(date -u +%s)
window_start_s=$((window_end_s - 48 * 60 * 60))
window_start_ms=$((window_start_s * 1000))
window_end_ms=$((window_end_s * 1000))

jq -nr --argjson start "$window_start_s" --argjson end "$window_end_s" '
  "UTC window: [\($start | todateiso8601), \($end | todateiso8601)]"
'
```

Create intermediates in a restrictive subshell and remove them on every exit:

```bash
(
  set -euo pipefail
  umask 077
  tmp_base=${TMPDIR:-/tmp}
  extract_dir=$(mktemp -d "$tmp_base/agent-session.XXXXXXXX")
  chmod 700 "$extract_dir"

  cleanup() {
    case ${extract_dir:-} in
      "$tmp_base"/agent-session.*) rm -rf -- "$extract_dir" ;;
    esac
  }
  trap cleanup EXIT
  trap 'exit 130' HUP INT TERM

  # Compose only the selected discovery and extraction commands here.
)
```

Keep raw transcripts outside the temporary directory. Store only private candidate
metadata, UUID relationships, fingerprints, and selected visible text.

## Stream a history index into a private candidate file

This parameterized reduction works for either observed history shape and retains
only the latest row per session. It does not output prompts or projects:

```bash
history="$agent_home/.codex/history.jsonl"
source_family=rollout
id_key=session_id
time_key=ts
window_start=$window_start_s
window_end=$window_end_s

# Tree-shaped history uses:
# history="$agent_home/.claude/history.jsonl"
# source_family=tree; id_key=sessionId; time_key=timestamp
# window_start=$window_start_ms; window_end=$window_end_ms

case "$source_family" in
  tree) data_root="$agent_home/.claude" ;;
  rollout) data_root="$agent_home/.codex" ;;
  *) printf 'Unsupported store family\n' >&2; exit 2 ;;
esac
[ -d "$data_root" ] && [ ! -L "$data_root" ] \
  && [ -f "$history" ] && [ ! -L "$history" ] || {
    printf 'History index is absent, linked, or unsupported\n' >&2
    exit 2
  }
case "$history" in
  "$data_root"/*) ;;
  *) printf 'History index escaped its data root\n' >&2; exit 2 ;;
esac

jq -nc \
  --arg source "$source_family" \
  --arg id_key "$id_key" \
  --arg time_key "$time_key" \
  --argjson start "$window_start" \
  --argjson end "$window_end" '
  reduce inputs as $row ({};
    ($row[$id_key] // null) as $id
    | ($row[$time_key] // null) as $time
    | if (
        ($id | type) == "string" and ($id | length) > 0
        and ($time | type) == "number"
        and $time >= $start and $time <= $end
      ) then
        if ((.[$id].recent_input // -1) < $time)
        then .[$id] = {
          source: $source,
          private_id: $id,
          recent_input: $time
        }
        else . end
      else . end
  )
  | .[]
' "$history" >"$extract_dir/${source_family}-candidates.jsonl"
```

Combine whichever compact JSONL candidate files exist, normalize milliseconds to
seconds, sort, and assign `S1`, `S2`, ... aliases. Keep the alias-to-ID map private:

```bash
candidate_files=()
for candidate_file in "$extract_dir"/tree-candidates.jsonl \
                      "$extract_dir"/rollout-candidates.jsonl; do
  [ -s "$candidate_file" ] && candidate_files+=("$candidate_file")
done
((${#candidate_files[@]} > 0)) || {
  printf 'No in-window candidates\n'
  exit 0
}

jq -sc '
  map(. + {
    recent_input_s: (
      if .source == "tree" then (.recent_input / 1000 | floor)
      else .recent_input end
    )
  })
  | sort_by(.recent_input_s) | reverse | to_entries[]
  | {
      alias: ("S" + ((.key + 1) | tostring)),
      source: .value.source,
      recent_input_s: .value.recent_input_s,
      private_id: .value.private_id
    }
' "${candidate_files[@]}" >"$extract_dir/candidate-map.jsonl"

jq -r '[.alias, .source, (.recent_input_s | todateiso8601)] | @tsv' \
  "$extract_dir/candidate-map.jsonl"
```

The private map remains one compact JSON object per line. Never print `private_id`,
history prompt text, `project`, or cwd.

## Resolve a selected ID without wildcard expansion

Read the private ID for one selected alias, then reject path separators, glob
characters, leading dots, and traversal markers:

```bash
case "$session_id" in
  ''|.*|*..*|*[!A-Za-z0-9._-]*)
    printf 'Unsafe or unsupported session ID\n' >&2
    exit 2
    ;;
esac
```

Resolve a tree root by direct path construction; do not recurse into `subagents`:

```bash
claude_root="$agent_home/.claude"
tree_root="$claude_root/projects"
[ -d "$claude_root" ] && [ ! -L "$claude_root" ] \
  && [ -d "$tree_root" ] && [ ! -L "$tree_root" ] || {
    printf 'Tree session root is absent, linked, or unsupported\n' >&2
    exit 2
  }

for project_dir in "$tree_root"/*; do
  [ -d "$project_dir" ] && [ ! -L "$project_dir" ] || continue
  candidate="$project_dir/$session_id.jsonl"
  [ -f "$candidate" ] && [ ! -L "$candidate" ] &&
    printf '%s\n' "$candidate" >>"$extract_dir/matches.txt"
done
```

For rollout files, walk only the known session root and compare the basename's
literal suffix after validating the ID:

```bash
codex_root="$agent_home/.codex"
rollout_root="$codex_root/sessions"
[ -d "$codex_root" ] && [ ! -L "$codex_root" ] \
  && [ -d "$rollout_root" ] && [ ! -L "$rollout_root" ] || {
  printf 'Rollout session root is absent or unsupported\n' >&2
  exit 2
}

while IFS= read -r candidate; do
  base=${candidate##*/}
  case "$base" in
    *-"$session_id".jsonl) printf '%s\n' "$candidate" >>"$extract_dir/matches.txt" ;;
  esac
done < <(find "$rollout_root" -type f -name '*.jsonl' -print)
```

Require exactly one match for the selected family. A missing tree transcript can be
command-only. A rollout match is not root until its first metadata record proves it.

## Prove rollout identity without exposing values

```bash
jq -nc --arg expected "$session_id" '
  (first(inputs | select(.type? == "session_meta"))
    // error("missing session_meta"))
  | .payload as $p
  | {
      id_matches: ($p.id? == $expected or $p.session_id? == $expected),
      explicit_subagent: (
        $p.thread_source? == "subagent"
        or (($p.source? | type) == "object" and $p.source.subagent? != null)
        or $p.agent_path? != null
      ),
      has_thread_id: ($p.id? != null),
      has_root_id: ($p.session_id? != null),
      has_parent: ($p.parent_thread_id? != null or $p.forked_from_id? != null),
      has_cwd: ($p.cwd? != null)
    }
' "$transcript" >"$extract_dir/identity.json"

jq -e '.id_matches == true and .explicit_subagent == false and .has_parent == false' \
  "$extract_dir/identity.json" >/dev/null
```

Keep actual metadata values private.

## Fingerprint structure without content

```bash
jq -c '
  def safe_enum($known):
    . as $value
    | if $value == null then null
      elif ($value | type) != "string" then ($value | type)
      elif ($known | index($value)) != null then $value
      else "unknown-string" end;
  {
    envelope: ((.type? // null) |
      safe_enum(["session_meta", "event_msg", "response_item", "user",
                 "assistant", "last-prompt"])),
    subtype_type: (.subtype? | type),
    payload_type: ((.payload.type? // null) |
      safe_enum(["user_message", "agent_message", "message", "reasoning",
                 "function_call", "function_call_output", "custom_tool_call",
                 "custom_tool_call_output", "task_started", "task_complete",
                 "turn_aborted"])),
    payload_role: ((.payload.role? // null) |
      safe_enum(["user", "assistant", "system", "tool"])),
    message_role: ((.message.role? // null) |
      safe_enum(["user", "assistant", "system", "tool"])),
    origin_kind: ((.origin.kind? // null) |
      safe_enum(["human", "system", "agent", "tool"])),
    prompt_source: ((.promptSource? // null) |
      safe_enum(["typed", "queued"])),
    message_content_type: (.message.content? | type),
    payload_content_type: (.payload.content? | type),
    message_blocks: (.message.content? |
      if type == "array" then map((.type? // null) |
        safe_enum(["text", "thinking", "redacted_thinking", "tool_use",
                   "tool_result", "image"])) else [] end),
    payload_blocks: (.payload.content? |
      if type == "array" then map((.type? // null) |
        safe_enum(["output_text", "input_text", "summary_text", "image"]))
      else [] end)
  }
' "$transcript" | sort | uniq -c | sort -nr | sed -n '1,100p'
```

Stop if the fingerprint does not support a known identity and message allow-list.

## Build a tree ancestry without bodies

After confirming the tree fields, write only UUID relationships to a private file:

```bash
jq -c '
  select(.uuid? != null and (.isSidechain // false) == false)
  | {uuid, parent: (.parentUuid // .logicalParentUuid // null)}
' "$transcript" >"$extract_dir/nodes.jsonl"
```

Use `jq -s` only on this minimal relationship file, never on the transcript:

```bash
jq -s '
  ([.[].parent | select(. != null)] | unique) as $parents
  | [.[] | .uuid as $id | select(($parents | index($id)) == null) | $id]
' "$extract_dir/nodes.jsonl" >"$extract_dir/leaves.json"

leaf_count=$(jq 'length' "$extract_dir/leaves.json")
[ "$leaf_count" -eq 1 ] || {
  printf 'Active branch is ambiguous; corroborate a leaf before continuing\n' >&2
  exit 2
}
active_leaf=$(jq -r '.[0]' "$extract_dir/leaves.json")

jq -s --arg leaf "$active_leaf" '
  . as $rows
  | ($rows | group_by(.uuid) | map(select(length > 1) | .[0].uuid)) as $duplicates
  | INDEX(.uuid) as $nodes
  | [$rows[]
      | .parent as $parent
      | select($parent != null and $nodes[$parent] == null)
      | .uuid
    ] as $broken
  | (($rows | length) + 1) as $limit
  | if ($duplicates | length) > 0
    then error("duplicate UUID in selected tree")
    elif ($broken | length) > 0
    then error("missing parent in selected tree")
    else [limit($limit; $leaf | recurse($nodes[.].parent; . != null))] as $ids
    | if ($ids | length) == $limit
    then error("cycle or invalid parent chain")
    else $ids | reverse end
    end
' "$extract_dir/nodes.jsonl" >"$extract_dir/active-ids.json"
```

Corroborate the selected ancestry with an explicit active marker or the latest
`last-prompt.leafUuid`. If multiple leaves remain plausible, stop rather than merge
branches. Selecting the newest leaf is a heuristic, not proof.

## Project visible text privately

Apply the exact predicates from `session-layouts.md` only after the fingerprint
matches. Keep the authoritative pattern visible in the command rather than hiding it
in a persistent helper. For example, a rollout projection has this shape:

```bash
jq -c '
  if .type? == "event_msg"
     and .payload.type? == "user_message"
     and (.payload.message? | type) == "string" then
    {
      role: "human",
      timestamp,
      text: .payload.message,
      attachment_summary: {
        images: ((.payload.images? // []) | length),
        local_images: ((.payload.local_images? // []) | length)
      }
    }
  elif .type? == "response_item"
       and .payload.type? == "message"
       and .payload.role? == "assistant" then
    [.payload.content[]?
      | select(.type? == "output_text" and (.text? | type) == "string")
      | .text
    ] as $text
    | select($text | length > 0)
    | {role: "assistant", timestamp, phase: (.payload.phase // null), text_blocks: $text}
  else empty end
' "$transcript" >"$extract_dir/visible.jsonl"
```

For a tree projection, first require membership in the private active-ID set, then
apply the human/assistant predicates. Bind the record UUID before searching the
active-ID array; otherwise `jq` changes the meaning of `.` inside `index(...)`:

```bash
jq -c --slurpfile active "$extract_dir/active-ids.json" '
  .uuid? as $id
  | select($id != null and ($active[0] | index($id)) != null)
  | if .type? == "user"
       and .message.role? == "user"
       and (.isSidechain // false) == false
       and (.origin.kind? == "human"
            or .promptSource? == "typed"
            or .promptSource? == "queued") then
      (if (.message.content? | type) == "string" then
         [.message.content]
       elif (.message.content? | type) == "array" then
         [.message.content[]?
           | select(.type? == "text" and (.text? | type) == "string")
           | .text]
       else [] end) as $text
      | select($text | length > 0)
      | {role: "human", text_blocks: $text}
    elif .type? == "assistant"
         and .message.role? == "assistant"
         and (.isSidechain // false) == false then
      [.message.content[]?
        | select(.type? == "text" and (.text? | type) == "string")
        | .text] as $text
      | select($text | length > 0)
      | {role: "assistant", text_blocks: $text}
    else empty end
' "$transcript" >"$extract_dir/visible.jsonl"
```

Do not write UUIDs, cwd, or local attachment paths to the visible artifact unless
private diagnosis explicitly requires them.

Print counts only during inventory:

```bash
jq -nc '
  reduce inputs as $message (
    {messages: 0, human: 0, assistant: 0, final_answers: 0};
    .messages += 1
    | if $message.role? == "human" then .human += 1 else . end
    | if $message.role? == "assistant" then .assistant += 1 else . end
    | if $message.phase? == "final_answer" then .final_answers += 1 else . end
  )
' "$extract_dir/visible.jsonl"
```

## Detect an active write

Capture evidence before extraction:

```bash
mtime_marker="$extract_dir/extraction-start"
: >"$mtime_marker"
before_inode=$(ls -di "$transcript" | awk '{print $1}')
before_size=$(wc -c <"$transcript")
```

After extraction, discard the artifact if identity, size, or mtime changed:

```bash
after_inode=$(ls -di "$transcript" | awk '{print $1}')
after_size=$(wc -c <"$transcript")

if [ "$before_inode" != "$after_inode" ] \
   || [ "$before_size" != "$after_size" ] \
   || [ "$transcript" -nt "$mtime_marker" ]; then
  printf 'Source changed; discard output and retry once\n' >&2
  exit 75
fi
```

Load selected message text only after the requested scope authorizes it. Otherwise
let the cleanup trap remove the private workspace.
