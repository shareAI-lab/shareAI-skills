# Cursor IDE Conversations

Read only after `cursor.md` routes to Cursor IDE.

## Discovery and time

Current global storage may contain `state.vscdb` and `conversation-search.db`. Older
bodies may remain in `User/workspaceStorage/<hash>/state.vscdb`.

Use `conversation-search.db.conversations` only as a candidate/FTS cache. Its ID,
title, archive state, and `updated_at` help shortlist; `source == cloud-cache` may have
no local body. FTS content is not exact transcript or lineage truth.

Prefer the typed `composerHeaders` table in `state.vscdb`. Fall back to
`ItemTable["composer.composerHeaders"]`, then legacy workspace
`composer.composerData.allComposers`.

Use activity clocks in this order, after verifying millisecond magnitude:

```text
maximum accepted bubble.createdAt
composerHeaders.lastUpdatedAt
composerHeaders.createdAt
conversation-search.updated_at
transcript file mtime
```

Do not assume `recency` or `checkpointAt` is an activity timestamp.

## Efficient body recovery

1. Query candidate IDs once from search or headers and read lineage metadata once.
2. Choose one body projection; never merge FTS, bubbles, and JSONL bodies.
3. Batch-read selected `composerData:<id>` rows.
4. Follow each `fullConversationHeadersOnly` ordered bubble list, then fetch required
   `bubbleId:<composerId>:<bubbleId>` rows with bounded `IN` queries.
5. Never query bubble by bubble. Use FTS directly only for search-only requests.

Current composer relationship:

```text
composerData.fullConversationHeadersOnly[]
  -> bubbleId:<composerId>:<bubbleId>

bubble.type == 1 -> human
bubble.type == 2 -> assistant
```

Prefer non-empty `bubble.text`. Decode `richText` only when its structured shape is
recognized; do not stringify it as user text. Exclude thinking blocks, tool payloads,
and context objects unless requested.

## Side Chats and incomplete caches

Prefer explicit Side Chat lineage:

```text
parentComposerId
subagentTypeName == side-chat
sideChatSeedTurnCount
```

Drop the copied seed prefix and retain the unique continuation. `isSubagent` is stronger
evidence than naming or ID patterns.

Across summarize/compress operations, preserve original human turns from retained
bubbles; summaries bridge missing history only. If a cloud-cache hit has no local
composer body, report an incomplete local cache rather than inventing a conversation.
