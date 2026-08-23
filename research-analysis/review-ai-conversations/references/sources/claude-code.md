# Claude Code Conversations

Last verified: Claude Code `2.1.215`, 2026-08-23. Transcript entries are internal,
version-drifting data; validate a small local sample and adapt semantically.

## Locations

- Root: `${CLAUDE_CONFIG_DIR:-$HOME/.claude}`
- Prompt history: `<root>/history.jsonl`
- Root sessions: `<root>/projects/<encoded-project>/<session-id>.jsonl`
- Child Agents: `<root>/projects/<encoded-project>/<session-id>/subagents/**/agent-*.jsonl`
- Optional child metadata: matching `agent-*.meta.json`

## Discovery and time

`history.jsonl` commonly contains:

```text
sessionId
timestamp       Unix milliseconds
project
display
pastedContents
```

Scan it once for interactive prompt candidates, but do not treat it as exhaustive:
print-mode, SDK, disabled-persistence, or retained transcripts may be absent. Also stat
root-level session JSONLs and parse only relevant candidates. A supplied session ID or
file path skips discovery.

Transcript timestamps are normally RFC3339. Use the maximum accepted human or visible
assistant timestamp as activity time. File mtime is candidate evidence only.

`display` may contain paste placeholders. Prefer the expanded transcript user message;
use `pastedContents[*].content` only as fallback. A `contentHash` cannot reconstruct the
paste.

## One-read reconstruction

Stream each selected root transcript once and retain:

```text
uuid -> record
parentUuid -> children
last valid last-prompt.leafUuid
system/compact_boundary + logicalParentUuid
accepted human and visible assistant text
maximum accepted timestamp
```

Use `last-prompt.leafUuid` as the active user-branch anchor when present. Walk backward
through `parentUuid` and retain its relevant visible descendants. At
`system/subtype == compact_boundary`, bridge through `logicalParentUuid`; the following
`user/isCompactSummary` record is a derived context summary, not human testimony.

If links are missing, cyclic, or yield several plausible visible tails, preserve the
stable path and label divergent segments. Do not silently drop a sibling assistant
reply merely because retry or buffered-error records orphaned it.

## Human and assistant text

Strong human signals:

```text
type == user
message.role == user
origin.kind == human
  OR promptSource in {typed, queued, sdk}
```

Older or remote records may lack source fields. Accept their string or text-only input
only when it is not `isMeta` or `isCompactSummary`, has no tool-source/result fields,
is not task-notification/peer/system input, and is corroborated by prompt history or
turn continuity.

Visible AI text:

```text
type == assistant
message.role == assistant
message.content[].type == text
```

Preserve text-block order on the selected path. Exclude thinking, tool records, API
error placeholders, system records, and progress.

## Branches and child Agents

`/branch` or `--fork-session` creates another root transcript with copied ancestry.
Deduplicate copied ancestors by shared message UUID and preserve every selected branch
suffix; never fuzzy-deduplicate repeated human wording.

A normal or forked child Agent lives below `subagents/`; current records commonly carry
`agentId` and `isSidechain:true`. Metadata may carry `toolUseId`, `parentAgentId`,
`spawnDepth`, and `isFork`; `toolUseId` attaches the child to its parent turn. Fork
children may use `fork-context-ref` instead of copied messages. A child task prompt is
not direct human intent. Read child bodies only when requested or when their evidence
or artifact materially informs the parent review.
