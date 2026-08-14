# Skill Evaluation Rubric

Use this rubric for a full, scored audit. It is an opinionated diagnostic model, not official certification.

## Scoring overview

| Dimension | Maximum |
|-----------|---------|
| D1. Knowledge delta | 20 |
| D2. Thinking patterns and domain procedures | 15 |
| D3. Anti-pattern quality | 15 |
| D4. Specification and trigger quality | 15 |
| D5. Progressive disclosure | 15 |
| D6. Freedom calibration | 15 |
| D7. Structural pattern fit | 10 |
| D8. Practical usability | 15 |
| **Total** | **120** |

Score each dimension from evidence. Use intermediate scores when the package falls between anchors.

## D1. Knowledge delta — 20 points

Judge whether the Skill contributes knowledge the AI model is unlikely to supply reliably without the package.

| Score | Anchor |
|------:|--------|
| 0–5 | Mostly definitions, generic advice, or standard operations |
| 6–10 | Some useful insight diluted by substantial obvious content |
| 11–15 | Mostly non-obvious decisions, trade-offs, or domain knowledge |
| 16–20 | Dense expert value; nearly every section changes behavior or judgment |

Strong evidence:

- non-obvious decision criteria;
- trade-offs tied to conditions;
- failure modes learned from practice;
- domain-specific procedures whose ordering matters;
- local policies, schemas, or operating constraints.

Weak evidence:

- explaining basic concepts;
- tutorials for standard file or language operations;
- generic reminders such as "write clean code";
- repeated motivational framing.

## D2. Thinking patterns and domain procedures — 15 points

Judge whether the Skill transfers both how an expert reasons and any procedures the agent would not reliably infer.

| Score | Anchor |
|------:|--------|
| 0–3 | Generic steps without domain judgment |
| 4–7 | Useful procedures but weak decision framing |
| 8–11 | Good balance of reasoning patterns and necessary procedures |
| 12–15 | Expert reasoning and non-obvious procedures reinforce each other |

Ask:

- Does the package explain what changes the choice between paths?
- Are mandatory sequences justified by risk or domain behavior?
- Could a generic checklist be replaced by a smaller decision rule?

## D3. Anti-pattern quality — 15 points

Judge whether warnings capture specific mistakes and explain their consequences.

| Score | Anchor |
|------:|--------|
| 0–3 | No meaningful anti-patterns |
| 4–7 | Mostly vague cautions without reasons |
| 8–11 | Specific failure patterns with useful explanations |
| 12–15 | High-value experiential warnings, consequences, and alternatives |

Do not reward a long `NEVER` list by itself. A prohibition should identify the condition, the failure it prevents, and a better action.

## D4. Specification and trigger quality — 15 points

Judge package validity and whether the description activates the Skill in the right situations.

| Score | Anchor |
|------:|--------|
| 0–5 | Invalid frontmatter, naming mismatch, or unusably vague description |
| 6–10 | Valid package with incomplete or over-broad trigger guidance |
| 11–13 | Clear function and use cases with minor overlap or wording gaps |
| 14–15 | Precise activation surface, useful trigger detail, and clear boundaries |

Check:

- required `name` and `description` fields;
- folder and Skill name alignment;
- explicit function and use context;
- concrete artifacts, actions, tools, or phrases where relevant;
- overlap with neighboring Skills;
- claims of universality, official status, or compatibility.

Treat missing files or advertised-but-unimplemented capabilities as hard-gate findings even when frontmatter is valid.

## D5. Progressive disclosure — 15 points

Judge whether the package loads the right amount of context for each request.

| Score | Anchor |
|------:|--------|
| 0–5 | Large undifferentiated body, broken routing, or unusable fragmentation |
| 6–10 | Some separation, but loading rules are incomplete or inconsistent |
| 11–13 | Core guidance and detailed resources are separated and routed well |
| 14–15 | Minimal core context with precise conditional loading and no orphan content |

Check:

- whether `SKILL.md` contains only always-needed guidance;
- whether long details live in appropriate resources;
- whether every resource has a clear loading condition;
- whether instructions prevent unnecessary loading;
- whether references duplicate the core body;
- whether a simple task requires opening too many files.

Line count is a signal, not the decision. A short but fragmented package can be worse than a coherent longer one.

## D6. Freedom calibration — 15 points

Judge whether instruction specificity matches task fragility.

| Score | Anchor |
|------:|--------|
| 0–5 | Rigid for variable work or vague for high-risk operations |
| 6–10 | Mixed calibration with noticeable over- or under-constraint |
| 11–13 | Appropriate freedom for most decisions and operations |
| 14–15 | Constraints, judgment, scripts, and fallbacks match risk throughout |

General guidance:

- Creative work usually needs principles and examples, not a fixed script.
- Review and design work usually need decision criteria with moderate freedom.
- Fragile file, security, migration, or external-write operations need explicit sequencing and verification.

## D7. Structural pattern fit — 10 points

Judge whether the package structure fits the work rather than imitating a fashionable template.

| Score | Anchor |
|------:|--------|
| 0–3 | Chaotic or internally contradictory structure |
| 4–6 | Recognizable approach with significant friction |
| 7–8 | Coherent structure with minor routing or organization issues |
| 9–10 | Structure closely matches task variability, risk, and resource needs |

Common useful patterns include:

- **Mindset**: concise principles and anti-patterns for high-judgment work.
- **Navigation**: a small router for several independent scenarios.
- **Process**: a phased workflow for complex multi-step work.
- **Tool**: explicit decision and verification guidance for fragile operations.
- **Hybrid**: a justified combination with clear boundaries.

Do not deduct points merely because a package does not match a named pattern.

## D8. Practical usability — 15 points

Judge whether another agent can use the package successfully in realistic conditions.

| Score | Anchor |
|------:|--------|
| 0–5 | Contradictory, incomplete, unsafe, or not executable |
| 6–10 | Useful for common cases but missing important paths or fallbacks |
| 11–13 | Clear and actionable with realistic edge-case coverage |
| 14–15 | Strong routing, verified examples, fallbacks, and operational clarity |

Check:

- decision routes for common task variants;
- existence and plausibility of referenced resources;
- script interfaces versus implemented behavior;
- error handling and recovery;
- safety around external writes or sensitive data;
- environment and tool assumptions;
- whether the output contract is clear.

## Grade bands

| Grade | Score | Interpretation |
|-------|------:|----------------|
| A | 108–120 | Strong and ready for its stated scope |
| B | 96–107 | Good; targeted improvements remain |
| C | 84–95 | Usable with a clear improvement path |
| D | 72–83 | Significant issues limit reliability |
| F | 0–71 | Fundamental redesign or repair needed |

A grade never overrides a hard-gate failure. Report the blocker first.

## Evidence discipline

For every score:

1. cite a concrete file and location;
2. describe the behavioral consequence;
3. distinguish facts from predictions;
4. state the highest-value improvement;
5. preserve strong content that should not be lost during revision.

Avoid false precision. When evidence supports a range rather than an exact point, explain the uncertainty and choose the conservative score.
