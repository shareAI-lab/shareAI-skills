# Linux and macOS shell examples

Compose these Bash snippets only after probing the current schema. They are examples,
not a persistent parser. They use `jq` 1.6+ when available and avoid GNU-only
`date -d`, `find -printf`, and `stat -c` forms.

If `jq` is absent, use an already-installed streaming JSON parser. Do not print raw
JSONL or install software without permission.

## Contents

- [Safe setup](#safe-setup)
- [Discover candidates](#stream-a-history-index-into-a-private-candidate-file)
- [Discover ACP-stream sessions](#discover-acp-stream-sessions-from-summaryjson)
- [Resolve one session](#resolve-a-selected-id-without-wildcard-expansion)
- [Prove rollout identity](#prove-rollout-identity-without-exposing-values)
- [Prove ACP-stream identity](#prove-acp-stream-identity-without-exposing-values)
- [Fingerprint the schema](#fingerprint-structure-without-content)
- [Recover a tree branch](#build-a-tree-ancestry-without-bodies)
- [Project visible text](#project-visible-text-privately)
- [Project an ACP stream](#project-an-acp-stream-privately)
- [Query a relational SQLite store](#query-a-relational-sqlite-store-read-only)
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
                      "$extract_dir"/rollout-candidates.jsonl \
                      "$extract_dir"/acp-stream-candidates.jsonl; do
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
      private_id: .value.private_id,
      child: (.value.child // false),
      has_updates: .value.has_updates
    }
' "${candidate_files[@]}" >"$extract_dir/candidate-map.jsonl"

jq -r '[.alias, .source, (.recent_input_s | todateiso8601),
        (if .child then "child" else "root" end),
        (if .has_updates == true then "transcript"
         elif .has_updates == false then "no-transcript"
         else "-" end)] | @tsv' \
  "$extract_dir/candidate-map.jsonl"
```

The private map remains one compact JSON object per line. Never print `private_id`,
history prompt text, `project`, or cwd.

## Discover ACP-stream sessions from summary.json

Grok Build has no `history.jsonl`. Walk `summary.json` files one level under each
cwd group. Resolve the grok home the same way the binary does: `$GROK_HOME`
verbatim when set and non-empty, otherwise `<home>/.grok`. Do not read
`prompt_history.jsonl`, `.cwd`, `session_search.sqlite` content columns, or
`auth.json`. Keep `info.cwd`, titles, and recaps private:

```bash
if [ -n "${GROK_HOME:-}" ]; then
  grok_home=$GROK_HOME
else
  grok_home="$agent_home/.grok"
fi
case "$grok_home" in
  /*) ;;
  *) printf 'GROK_HOME must be an absolute path\n' >&2; exit 2 ;;
esac
[ -d "$grok_home" ] && [ ! -L "$grok_home" ] || {
  printf 'Grok home is absent, linked, or unsupported\n' >&2
  exit 2
}
grok_home=$(cd -P -- "$grok_home" 2>/dev/null && pwd -P) || exit 2
sessions_root="$grok_home/sessions"
[ -d "$sessions_root" ] && [ ! -L "$sessions_root" ] || {
  printf 'ACP-stream session root is absent or unsupported\n' >&2
  exit 2
}

python3 - "$sessions_root" "$window_start_s" "$window_end_s" \
  "$extract_dir/acp-stream-candidates.jsonl" <<'EOF'
import json, sys
from datetime import datetime
from pathlib import Path

root = Path(sys.argv[1])
start_s, end_s = int(sys.argv[2]), int(sys.argv[3])
out_path = Path(sys.argv[4])


def parse_rfc3339(value):
    if not isinstance(value, str) or not value:
        return None
    text = value.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(text)
    except ValueError:
        if "." in text:
            head, rest = text.split(".", 1)
            frac = ""
            tz = rest
            for i, ch in enumerate(rest):
                if ch.isdigit():
                    frac += ch
                else:
                    tz = rest[i:]
                    break
            text = head + "." + frac[:6].ljust(6, "0") + tz
            try:
                return datetime.fromisoformat(text)
            except ValueError:
                return None
        return None


def is_child(summary):
    hidden = summary.get("hidden")
    if isinstance(hidden, bool):
        return hidden
    kind = summary.get("session_kind")
    return isinstance(kind, str) and kind.startswith("subagent")


with out_path.open("w", encoding="utf-8") as out:
    for group in sorted(root.iterdir()):
        if not group.is_dir() or group.is_symlink():
            continue
        for session_dir in sorted(group.iterdir()):
            if not session_dir.is_dir() or session_dir.is_symlink():
                continue
            summary_path = session_dir / "summary.json"
            if not summary_path.is_file() or summary_path.is_symlink():
                continue
            try:
                summary = json.loads(summary_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError, UnicodeError):
                continue
            info = summary.get("info") if isinstance(summary.get("info"), dict) else {}
            session_id = info.get("id")
            if not isinstance(session_id, str) or session_id != session_dir.name:
                continue
            stamp = parse_rfc3339(summary.get("last_active_at")) or parse_rfc3339(
                summary.get("updated_at")
            )
            if stamp is None:
                continue
            recent = int(stamp.timestamp())
            if recent < start_s or recent > end_s:
                continue
            updates = session_dir / "updates.jsonl"
            row = {
                "source": "acp-stream",
                "private_id": session_id,
                "recent_input": recent,
                "child": is_child(summary),
                "has_updates": updates.is_file() and (not updates.is_symlink()) and updates.stat().st_size > 0,
            }
            out.write(json.dumps(row, separators=(",", ":")) + "\n")
EOF
```

Inventory still prints only alias, source, and UTC time. Keep `child` and
`has_updates` on the private map so root filtering and transcript availability
can be reported without opening message bodies.

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

For ACP-stream sessions, walk cwd groups under the grok sessions root and match
the directory basename exactly. Skip `subagents` directories (metadata only):

```bash
while IFS= read -r candidate; do
  base=${candidate##*/}
  [ "$base" = "$session_id" ] || continue
  case "$candidate" in
    */subagents/*) continue ;;
  esac
  [ -f "$candidate/summary.json" ] && [ ! -L "$candidate/summary.json" ] &&
    printf '%s\n' "$candidate" >>"$extract_dir/matches.txt"
done < <(find "$sessions_root" -mindepth 2 -maxdepth 2 -type d -print)
```

Require exactly one match for the selected family. A missing tree transcript can be
command-only. A rollout match is not root until its first metadata record proves it.
An ACP-stream directory with `summary.json` but no `updates.jsonl` is a root
candidate whose transcript is unavailable.

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

## Prove ACP-stream identity without exposing values

```bash
python3 - "$session_dir" "$session_id" "$extract_dir/identity.json" <<'EOF'
import json, sys
from pathlib import Path

session_dir = Path(sys.argv[1])
expected = sys.argv[2]
out = Path(sys.argv[3])
summary = json.loads((session_dir / "summary.json").read_text(encoding="utf-8"))
info = summary.get("info") if isinstance(summary.get("info"), dict) else {}
kind = summary.get("session_kind")
hidden = summary.get("hidden")
if isinstance(hidden, bool):
    child = hidden
else:
    child = isinstance(kind, str) and kind.startswith("subagent")
updates = session_dir / "updates.jsonl"
identity = {
    "id_matches": info.get("id") == expected and session_dir.name == expected,
    "child": child,
    "has_parent_session_id": isinstance(summary.get("parent_session_id"), str)
        and len(summary.get("parent_session_id") or "") > 0,
    "has_cwd": isinstance(info.get("cwd"), str),
    "chat_format_version": summary.get("chat_format_version"),
    "has_updates": updates.is_file() and (not updates.is_symlink()) and updates.stat().st_size > 0,
}
out.write_text(json.dumps(identity) + "\n", encoding="utf-8")
EOF

jq -e '.id_matches == true and .child == false' \
  "$extract_dir/identity.json" >/dev/null
```

`has_parent_session_id` marks a fork, which remains a root. Stop if
`chat_format_version` is present and not `1` until the fingerprint of
`updates.jsonl` still matches the allow-list. Keep actual IDs and cwd private.

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

For an ACP-stream `updates.jsonl`, fingerprint method and `sessionUpdate`
discriminants instead of Codex/Claude envelopes:

```bash
jq -c '
  def safe_enum($known):
    . as $value
    | if $value == null then null
      elif ($value | type) != "string" then ($value | type)
      elif ($known | index($value)) != null then $value
      else "unknown-string" end;
  {
    method: ((.method? // null) |
      safe_enum(["session/update", "_x.ai/session/update"])),
    session_update: ((.params.update.sessionUpdate? // null) |
      safe_enum(["user_message_chunk", "agent_message_chunk",
                 "agent_thought_chunk", "tool_call", "tool_call_update",
                 "plan", "turn_completed", "rewind_marker", "retry_state",
                 "session_recap", "subagent_spawned", "subagent_finished",
                 "auto_compact_started", "auto_compact_completed",
                 "compaction_checkpoint"])),
    content_type: ((.params.update.content.type? // null) |
      safe_enum(["text", "image", "resource", "resource_link"])),
    has_prompt_index: ((.params.update._meta.promptIndex? | type) == "number"),
    has_host_turn: ((.params.update._meta.hostTurn? | type) == "boolean"),
    timestamp_type: (.timestamp? | type)
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

For an ACP-stream transcript, apply rewind truncation first, then coalesce
counted user runs and assistant chunks. The predicates match
`session-layouts.md`. Concatenate assistant fragments with no added separator.
Read with the file iterator (`for line in fh`); `str.splitlines()` splits on
Unicode line separators that can appear inside JSON strings:

```bash
python3 - "$transcript" "$extract_dir/visible.jsonl" <<'EOF'
import json, sys
from pathlib import Path

src, dest = Path(sys.argv[1]), Path(sys.argv[2])


def parse_line(line):
    obj = json.loads(line)
    method = obj.get("method")
    params = obj.get("params") if isinstance(obj.get("params"), dict) else obj
    update = params.get("update") if isinstance(params, dict) else None
    if not isinstance(update, dict):
        return obj.get("timestamp"), method, None, update
    return obj.get("timestamp"), method, update.get("sessionUpdate"), update


def prompt_index(update):
    meta = update.get("_meta") if isinstance(update, dict) else None
    if not isinstance(meta, dict):
        return None
    value = meta.get("promptIndex")
    return int(value) if isinstance(value, int) else None


def is_host_turn(update):
    meta = update.get("_meta") if isinstance(update, dict) else None
    return isinstance(meta, dict) and meta.get("hostTurn") is True


def is_bash_chunk(update):
    content = update.get("content") if isinstance(update, dict) else None
    if not isinstance(content, dict):
        return False
    meta = content.get("_meta")
    return isinstance(meta, dict) and meta.get("bash_command") is not None


def text_of(update):
    content = update.get("content") if isinstance(update, dict) else None
    if not isinstance(content, dict):
        return None, None
    if content.get("type") != "text":
        return content.get("type"), None
    text = content.get("text")
    return "text", text if isinstance(text, str) else None


lines = []
with src.open(encoding="utf-8") as fh:
    for raw in fh:
        line = raw.strip()
        if line:
            lines.append(line)

# Rewind: drop the branch after target_prompt_index counted user runs.
prompt_starts = []
seen_marker = False
in_user = False
current_pi = None
kept = []
for line in lines:
    try:
        ts, method, tag, update = parse_line(line)
    except json.JSONDecodeError:
        raise SystemExit("malformed middle record")
    if method == "_x.ai/session/update" and tag == "rewind_marker":
        target = update.get("target_prompt_index") if isinstance(update, dict) else None
        if isinstance(target, int):
            trunc = prompt_starts[target] if target < len(prompt_starts) else len(kept)
            kept = kept[:trunc]
            prompt_starts = prompt_starts[:target]
            in_user = False
            current_pi = None
            continue
    user = (
        method == "session/update"
        and tag == "user_message_chunk"
        and not is_host_turn(update)
        and not is_bash_chunk(update)
    )
    if user:
        pi = prompt_index(update)
        if pi is not None:
            seen_marker = True
        counts = (pi is not None) if seen_marker else True
        new_run = (not in_user) or (
            (seen_marker or pi is not None) and pi != current_pi
        )
        if new_run:
            in_user = True
            current_pi = pi
            if counts:
                prompt_starts.append(len(kept))
        else:
            if current_pi is None and pi is not None:
                current_pi = pi
    else:
        in_user = False
        current_pi = None
    kept.append(line)

# Coalesce visible text from the surviving stream.
visible = []
buf_role = None
buf_ts = None
buf_text = []
buf_pi = None
seen_marker = False
counted = True
attachments = 0


def flush():
    global buf_role, buf_ts, buf_text, buf_pi, counted, attachments
    if buf_role == "human" and not counted:
        buf_role = None
        buf_text = []
        attachments = 0
        return
    text = "".join(buf_text)
    if buf_role and text:
        row = {"role": buf_role, "timestamp": buf_ts, "text": text}
        if attachments:
            row["attachment_summary"] = {"non_text_blocks": attachments}
        visible.append(row)
    buf_role = None
    buf_ts = None
    buf_text = []
    buf_pi = None
    attachments = 0


in_user = False
current_pi = None
for line in kept:
    ts, method, tag, update = parse_line(line)
    if method == "session/update" and tag == "user_message_chunk":
        if is_host_turn(update) or is_bash_chunk(update):
            flush()
            continue
        ctype, text = text_of(update)
        pi = prompt_index(update)
        if pi is not None:
            seen_marker = True
        counts = (pi is not None) if seen_marker else True
        new_run = buf_role != "human" or (
            (seen_marker or pi is not None) and pi != buf_pi
        )
        if new_run:
            flush()
            buf_role = "human"
            buf_ts = ts
            buf_pi = pi
            counted = counts
        elif buf_pi is None and pi is not None:
            buf_pi = pi
            counted = True
        if ctype == "text" and text:
            buf_text.append(text)
        elif ctype not in (None, "text"):
            attachments += 1
            flush()
        continue
    if method == "session/update" and tag == "agent_message_chunk":
        ctype, text = text_of(update)
        if buf_role != "assistant":
            flush()
            buf_role = "assistant"
            buf_ts = ts
            counted = True
        if ctype == "text" and text:
            buf_text.append(text)
        continue
    flush()

flush()
with dest.open("w", encoding="utf-8") as out:
    for row in visible:
        out.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
EOF
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

## Query a relational SQLite store read-only

`jq` cannot read SQLite. Use an installed read-only client: `node:sqlite` on
Node 22+, or `sqlite3` with a `mode=ro` URI. Do not install software, attach
databases, write, or touch credential tables (`account`, `account_state`,
`control_account`, `credential`) or `auth.json`. The bundled SQLite may reject
double-quoted string literals, so quote SQL strings with single quotes; the
heredoc form below keeps that safe. Node prints an experimental-SQLite warning
on stderr; leave it visible rather than suppressing stderr wholesale.

Inventory candidates without exposing IDs or titles:

```bash
db="$agent_home/.local/share/opencode/opencode.db"
[ -f "$db" ] && [ ! -L "$db" ] || { printf 'No relational store\n' >&2; exit 2; }

node - "$db" "$window_start_ms" "$window_end_ms" \
  "$extract_dir/relational-map.jsonl" <<'EOF' \
  >"$extract_dir/relational-inventory.tsv"
const fs = require("node:fs");
const { DatabaseSync } = require("node:sqlite");
const [dbPath, startMs, endMs, mapPath] = process.argv.slice(2);
const db = new DatabaseSync(dbPath, { readOnly: true });
const rows = db.prepare(
  "SELECT id, parent_id, time_updated, time_archived FROM session " +
  "WHERE time_updated >= ? AND time_updated <= ? ORDER BY time_updated DESC"
).all(Number(startMs), Number(endMs));
let i = 0;
for (const r of rows) {
  i += 1;
  const alias = "S" + i;
  fs.appendFileSync(mapPath, JSON.stringify({
    alias, source: "relational", private_id: r.id,
    recent_input_s: Math.floor(r.time_updated / 1000),
  }) + "\n");
  console.log([
    alias,
    r.parent_id ? "child" : "root",
    new Date(r.time_updated).toISOString(),
    r.time_archived ? "archived" : "active",
  ].join("\t"));
}
db.close();
EOF

cat "$extract_dir/relational-inventory.tsv"
```

Fingerprint structure without content (key names and enums only):

```bash
node - "$db" <<'EOF'
const { DatabaseSync } = require("node:sqlite");
const db = new DatabaseSync(process.argv[2], { readOnly: true });
const roles = new Set(), keySets = new Set(), partTypes = new Set();
for (const r of db.prepare("SELECT data FROM message LIMIT 200").all()) {
  try {
    const d = JSON.parse(r.data);
    roles.add(typeof d.role === "string" ? d.role : "unknown");
    keySets.add(Object.keys(d).sort().join(","));
  } catch { keySets.add("unparsed"); }
}
for (const p of db.prepare("SELECT data FROM part LIMIT 500").all()) {
  try {
    const t = JSON.parse(p.data).type;
    partTypes.add(typeof t === "string" ? t : "unknown");
  } catch { partTypes.add("unparsed"); }
}
console.log("message roles:", [...roles].join("|"));
console.log("message key sets:", [...keySets].join("  "));
console.log("part types:", [...partTypes].join("|"));
db.close();
EOF
```

Stop unless roles stay within `user|assistant` and part types match the
documented set. After the user selects an alias, project the visible timeline
for that one session:

```bash
node - "$db" "$session_id" <<'EOF' >"$extract_dir/visible.jsonl"
const { DatabaseSync } = require("node:sqlite");
const db = new DatabaseSync(process.argv[2], { readOnly: true });
const ses = process.argv[3];
const marker = db.prepare("SELECT revert FROM session WHERE id = ?").get(ses);
let cut = null;
if (marker && marker.revert) {
  try { cut = JSON.parse(marker.revert).messageID ?? null; } catch {}
}
const rows = db.prepare(
  "SELECT m.id mid, m.time_created t, " +
  "json_extract(m.data, '$.role') role, " +
  "json_extract(m.data, '$.summary') summary, " +
  "json_extract(p.data, '$.type') ptype, " +
  "json_extract(p.data, '$.synthetic') synthetic, " +
  "json_extract(p.data, '$.ignored') ignored, " +
  "json_extract(p.data, '$.text') text " +
  "FROM message m JOIN part p ON p.message_id = m.id " +
  "WHERE m.session_id = ? " +
  "AND NOT EXISTS (SELECT 1 FROM part p2 WHERE p2.message_id = m.id " +
  "  AND json_extract(p2.data, '$.type') = 'compaction') " +
  "ORDER BY m.time_created, m.id, p.id"
).all(ses);
for (const r of rows) {
  if (r.ptype !== "text" || r.synthetic || r.ignored) continue;
  if (r.summary) continue; // compaction output
  if (typeof r.text !== "string" || r.text.length === 0) continue;
  console.log(JSON.stringify({
    role: r.role === "user" ? "human" : r.role,
    timestamp_ms: r.t,
    reverted: cut !== null && r.mid >= cut,
    text: r.text,
  }));
}
db.close();
EOF
```

Preserve truncation placeholders inside tool previews as-is; the externalized
`tool-output/` files they reference expire on a retention sweep. Detect
concurrent writes with row counts instead of file identity — WAL sidecars
change while any client runs, and the extracting agent may itself be writing
this store. Capture before extraction, re-run after, and retry once if it
moved:

```bash
node - "$db" "$session_id" <<'EOF'
const { DatabaseSync } = require("node:sqlite");
const db = new DatabaseSync(process.argv[2], { readOnly: true });
const r = db.prepare(
  "SELECT count(*) n, max(time_updated) t FROM message WHERE session_id = ?"
).get(process.argv[3]);
console.log(r.n + "\t" + (r.t ?? 0));
db.close();
EOF
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
