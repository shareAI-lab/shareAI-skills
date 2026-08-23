# Efficient Conversation Retrieval

Read this file only when local Agent Stores must be searched. Product adapters own
paths and fields; this file owns shared recovery behavior.

## Treat schemas as observed anchors

Client Stores are internal and may drift. Use the product adapter as a strong starting
point, not an immutable parser. When fields differ, inspect a few neighboring records
from one or two candidates. Infer the narrowest mapping from conversation identity,
record order, timestamps, parent relationships, human input, visible AI text, and turn
continuity; adapt once and apply it to the selected batch.

Never make a new schema fit by reclassifying tool output, reasoning, copied context,
or synthetic instructions as visible conversation. Ask only when competing mappings
would materially change the result.

## Use bounded passes

```text
one candidate query or index scan per Store
  -> one read per required conversation or lineage segment
  -> emit accepted turns directly
  -> perform the user's requested review
  -> reopen raw text for decisive evidence or requested exact/full recovery
```

Freeze one UTC `[start, end]` window only for relative or calendar-time requests.
Prefer accepted message clocks for activity; use a trustworthy session clock next and
file mtime only as fallback or candidate evidence.

Use the smallest sufficient recovered object:

```text
{
  source, conversation_id, activity_time, state,
  lineage_ref,
  turns[{message_ref, time, role, text_or_ref}]
}
```

For exact or full recovery, retain every persisted visible message verbatim. Otherwise,
short messages may remain verbatim; for unusually large messages, keep a stable exact
address plus only the clauses needed for the requested analysis. Advanced lenses may
add clusters, decisions, artifacts, or insights; retrieval should not precompute them.

## Read consistently

- For JSONL, stream once. If the source is actively writing, ignore one malformed or
  incomplete final line and retry that tail once; a malformed middle line is a gap.
- For SQLite, use one read-only transaction or snapshot for the batch. If snapshot
  reads are unavailable, compare a cheap row/version clock before and after once.
- Batch selected IDs. Avoid one query per session, message, part, or bubble.
- Do not reread a conversation separately for metadata, questions, replies, and
  artifacts when one pass can collect them.
- Choose one canonical body projection. Search indexes and derived caches shortlist
  candidates; they do not become transcript truth merely because they are convenient.

Recover accepted human messages and visible assistant replies in order. Exclude tool
calls, internal reasoning, system injection, synthetic input, and host-generated
command output or expansion unless requested. Preserve human-typed command invocations
and arguments when they carry intent. Do not discard a copied parent prefix until one
canonical ancestor copy has been retained and branch lineage has been resolved.
