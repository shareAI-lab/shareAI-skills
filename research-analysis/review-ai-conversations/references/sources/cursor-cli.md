# Cursor Agent CLI Conversations

Read only after `cursor.md` routes to Cursor Agent CLI.

## Body projections

Current transcripts use:

```text
$CURSOR_DATA_DIR/projects/<workspace>/agent-transcripts/
  <conversation>/<conversation>.jsonl
  <parent>/subagents/<child>.jsonl
```

Legacy flat `<conversation>.jsonl` files may remain. Resumable runtime state is stored
separately under `<config-root>/chats/<cwd-hash>/<session>/store.db`.

Stream each selected transcript once. Common visible shape:

```text
role == user | assistant
message.content[].type == text
```

Ignore metadata, `turn_ended`, tool use, and tool results for ordinary review. The
current transcript writer may merge assistant thinking with assistant text; when exact
visible-reply separation is required and an IDE bubble Store is available, prefer the
IDE body. Otherwise label this projection limitation.

## Lineage

Nested `<parent>/subagents/<child>.jsonl` is strong child evidence. Some Task children
may appear as sibling main transcripts; classify them only with parent metadata or one
unambiguous launch relationship.

CLI `/fork` can copy complete source history into a new `store.db` without a reliable
parent ID. A shared-prefix or root-fingerprint match is heuristic: count a confidently
matched prefix once, keep every relevant divergent suffix, and label uncertain
parentage.

The transcript writer may recover pre-compaction messages from retained summary
archives and filter derived summary messages. Preserve recovered original human turns;
never use a surviving summary to overwrite them.
