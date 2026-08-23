# Optional Conversation Analysis Lenses

Read this file only when the user requests one or more deeper forms of synthesis. Use
the relevant lens, not a fixed pipeline.

## Question clusters and workstreams

Recover accepted human requests before trusting later summaries. Split a long prompt
into question atoms only when it reveals structure; retain the original reference.
Cluster by the underlying decision, unknown, or tension rather than keyword overlap.

For each useful cluster, identify:

- what the user is trying to understand, decide, or build;
- constraints, exclusions, examples, and assumptions that change the answer;
- which conversations extend, correct, fork, or repeat earlier work;
- what is resolved, contradicted, partial, or absent.

Prefer the fewest clusters that preserve meaningful differences.

## Problem-space map

Choose the smallest representation that exposes real relationships:

- dimensions for independent variables;
- quadrants only when two independent axes create four meaningful cases;
- sets for overlap, subset, exclusion, and uncovered cases;
- layers for abstraction or ownership;
- dependencies for order or prerequisite;
- tensions for needs that weaken one another.

Test whether dimensions are truly independent and whether missing regions matter. Do
not create a decorative ontology or a topic catalog.

## Documents, AI conclusions, and decisions

Collect mentioned documents, code, reports, plans, and decisions when relevant. Inspect
the artifact when available and attach it to the question it serves. Judge whether it
supports, extends, contradicts, supersedes, or leaves that question unresolved.

```text
user intent   -> original human messages outrank AI summaries
produced work -> actual document or code outranks a chat claim
external fact -> primary evidence outranks an AI report
```

## Insights, open questions, and brainstorming

Use this lens only when the user requests insights, open questions, reframing, or
brainstorming. A useful insight makes its derivation inspectable:

```text
cross-conversation observations
  -> relationship or contradiction
  -> why understanding changes
  -> decision, experiment, or next question enabled
```

Offer a small number of alternative frames or experiments. Do not generate an insight
or brainstorm section merely to satisfy a template.
