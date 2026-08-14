# Expectation and coaching guide

Use this reference only when the user asks for deeper coaching, repeated-pattern analysis, or employee feedback.

## The expected work chain

```text
understand the desired result
  -> identify the questions that matter
  -> verify evidence and numbers
  -> form a recommendation
  -> explain limits and next actions
```

The chain may be lightweight. Do not turn it into mandatory paperwork.

## Common bad cases and good cases

| Area | Bad case | Good case |
|---|---|---|
| Understanding | Say "understood" but start from a different question | Restate the desired result, output, and scope briefly |
| Focus | Produce a catalog of facts | Answer the decision and use facts as support |
| AI use | Attribute the result to AI | Verify and own the result |
| Evidence | Mix facts, guesses, and vendor claims | Mark what is confirmed, inferred, assumed, and unknown |
| Numbers | Give a total without source, unit, or formula | Make the number reproducible and compare it with a simple baseline |
| Experiments | Try a few examples and generalize | Define the question, sample, baseline, success rule, and limits |
| Unknowns | Reveal critical gaps in the final review | Surface them early with impact and a recovery plan |
| Reporting | Start with process and chronology | State conclusion, evidence, risk, and request first |
| Pressure | Agree or speculate | Protect the fact boundary and correct errors directly |
| Ownership | Define completion as "I researched it" | Define completion as "the decision can now be answered responsibly" |

## Evidence preference

Prefer, when applicable:

1. reproducible experiments;
2. source code and tests;
3. official documentation, specifications, pricing, or API behavior;
4. primary issues and pull requests;
5. reputable secondary analysis;
6. AI synthesis, recollection, or intuition as hypothesis sources only.

## Deep-review prompts

Ask the artifact, not just the author:

- What exact decision does this support?
- Which evidence is decisive?
- Which claim is weakest?
- Are the units, assumptions, and comparisons valid?
- Could the method produce the claimed conclusion?
- What important alternative was ignored?
- Which remaining unknown could reverse the recommendation?
- What will the manager most likely challenge?

## Feedback pattern

1. State the observable result.
2. Name the gap against the expected result.
3. Explain its impact.
4. Give the replacement behavior.
5. Define one clear check for the next cycle.

Example:

> The current cost conclusion is not reviewable because the unit conversion and workload assumption cannot be reproduced. In the next version, show the source price, one conversion formula, three workload scenarios, and a dedicated-server baseline. Send the calculation before writing the recommendation.

Avoid global labels about intelligence, attitude, or suitability based on one artifact. Consider role fit only after the same behavior repeats under clear expectations and reasonable support.
