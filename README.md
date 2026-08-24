# Lab Skills

English | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md)

Skills distilled from the Lab's real engineering, research, publishing, and collaboration work.

The reusable parts are shared for reference, discussion, adaptation, and continued improvement.

The repository is designed for AI coding agents and other systems that support the [Agent Skills specification](https://agentskills.io/specification).

## Scope

This is a skills-only repository. It does not ship plugins, general tutorials, or unrelated articles.

Every Skill is intended to remain understandable and useful on its own. Some packages may include optional agent-facing metadata, but the core instructions do not depend on one specific product runtime.

The collection is practice-derived, not a universal standard. Read each Skill's description and adapt assumptions that do not fit your tools, organization, or working context.

## Installation

Preview the available Skills without installing them:

```bash
npx skills add shareai-lab/lab-skills --list
```

Install all Skills non-interactively for the detected agent environment:

```bash
npx skills add shareai-lab/lab-skills --skill '*' -y
```

Install one Skill:

```bash
npx skills add shareai-lab/lab-skills --skill deep-architecture-research
```

Generate a prompt for one Skill without installing it:

```bash
npx skills use shareai-lab/lab-skills@understanding-first-report
```

## Keeping Skills Updated

Update every installed Skill in the current scope from its recorded upstream source:

```bash
npx skills update
```

Update one Skill only:

```bash
npx skills update deep-architecture-research
```

Update project-level Skills without prompting:

```bash
npx skills update --project -y
```

Update global Skills without prompting:

```bash
npx skills update --global -y
```

If you installed Skills before they were renamed, remove the old names and install the replacements once:

```bash
npx skills remove boss-meet meet-work extract-agent-sessions -y
npx skills add shareai-lab/lab-skills \
  --skill meeting-coach-leader meeting-coach-worker \
          review-ai-conversations -y
```

## Skill Catalog

### Research and analysis

#### [review-ai-conversations](./research-analysis/review-ai-conversations/)

Review recent conversations across AI workers, compress them to their core value, map the problem space, and surface new cross-session insights.

**Recommended scenarios**

- Review what you have been working on across Claude Code, Codex, opencode, Grok Build, or Cursor.
- Cluster recurring questions and map their dimensions, overlaps, dependencies, and unresolved gaps.
- Revisit recent documents, code artifacts, and AI conclusions as reference material rather than unquestioned truth.
- Generate new insights, reframings, brainstorming directions, and high-value next questions.

**Example**

```text
/review-ai-conversations review my recent AI worker chats,
cluster the core problems, map the problem space, and surface
new insights and next questions.
```

#### [deep-architecture-research](./research-analysis/deep-architecture-research/)

Clarify broad system questions before investigating architecture through source, history, official documentation, and calibrated community evidence.

**Recommended scenarios**

- Compare frameworks, runtimes, SDKs, or technical projects at source level.
- Trace important architectural changes, breaking updates, hard boundaries, and disputed scenarios.
- Gather evidence before designing a new system or selecting an implementation path.

**Example**

```text
/deep-architecture-research clarify and compare how these agent
runtimes own sessions, memory, workspaces, and deployment.
```

#### [understanding-first-report](./research-analysis/understanding-first-report/)

Re-synthesize long-running or multi-turn technical work into a clear problem space, deeper insight, and professional update. Restore relevant context, show what is known or still open, then present the decision in an attention-friendly order.

**Recommended scenarios**

- Reconnect earlier questions, scope changes, and accepted choices after extended agent work.
- Quote the relevant original user wording before analysis; include dependent earlier turns and mark omissions only when the combined text is long.
- Use spatial Markdown diagrams during analysis to show dependencies, conflicts, ownership, and the problem behind the problem instead of leaving questions in a flat list.
- Map the question set, find the deeper need or conflict, calibrate answer readiness, and report the result in a clear decision order.

**Example**

```text
/understanding-first-report quote the relevant original questions, reconnect
the problem space, show what is known or open, then give the insight and next step.
```

The two Skills work well together, but each remains independently usable.

### Software engineering

#### [vibe-coding](./software-engineering/vibe-coding/)

Turn an AI agent into a disciplined software development partner with transparent decisions and proportionate verification.

**Recommended scenarios**

- Add a feature to an existing codebase without ignoring its conventions.
- Diagnose and fix a bug from the real failure path.
- Refactor, optimize, or migrate software with proportionate verification.

**Example**

```text
/vibe-coding add this feature to the existing service, follow
its conventions, and verify the real integration path.
```

### Team collaboration and communication

#### [meeting-coach-leader](./team-collaboration/meeting-coach-leader/)

Help leaders and managers prepare, run, and review high-bandwidth meetings that advance real work and decisions.

**Recommended scenarios**

- Prepare or review an employee work-review meeting.
- Diagnose repeated low-value discussions and missing decision prerequisites.
- Give direct, specific feedback without taking over the worker's responsibility.

**Example**

```text
/meeting-coach-leader review this meeting transcript and design
a shorter follow-up that reaches a decision.
```

#### [meeting-coach-worker](./team-collaboration/meeting-coach-worker/)

Help workers turn meetings, feedback, and work notes into better execution and stronger updates.

**Recommended scenarios**

- Infer what a leader actually expects from recent meeting evidence.
- Review whether current work is ready to report and what is still missing.
- Identify the highest-value next action and prepare a concise update.

**Example**

```text
/meeting-coach-worker tell me what my manager expects, what is
missing from my work, and how to report it next time.
```

### Agent development

#### [agent-builder](./agent-development/agent-builder/)

Design and build AI agents. The bundled starter code currently uses the Anthropic Python SDK, while the architectural guidance is intended to remain provider-neutral.

**Recommended scenarios**

- Define an agent's purpose, capabilities, knowledge, context, and trust boundary.
- Decide whether planning, subagents, skills, or additional tools are actually needed.

**Example**

```text
/agent-builder design a customer-support agent that can search
policy, inspect orders, and escalate refunds.
```

#### [skill-judge](./agent-development/skill-judge/)

Evaluate and improve Agent Skill packages with a practice-derived diagnostic rubric.

**Recommended scenarios**

- Check whether a `SKILL.md` triggers at the right time and adds real expert knowledge.
- Diagnose instruction sprawl, weak references, poor freedom calibration, or unclear completion criteria.

**Example**

```text
/skill-judge review this Skill package and give me the three
highest-impact improvements.
```

### Content and publishing

#### [media-writer](./content-publishing/media-writer/)

Adapt technical content to the culture and expectations of supported publishing platforms.

**Recommended scenarios**

- Rewrite one technical idea for WeChat, Hacker News, Reddit, Medium, X/Twitter, Dev.to, or LinkedIn.
- Preserve the community's tone instead of applying one generic social-media format.

**Example**

```text
/media-writer turn this architecture note into a Hacker News
launch post without marketing language.
```

## Team Collaboration Guidance

The meeting-coach Skills emphasize substantive work, clear decisions, delivery readiness, high-bandwidth communication, and explicit ownership.

They are intended to improve work through meetings, not to prescribe a universal management culture.

When applying them elsewhere, reconsider assumptions about hierarchy, feedback style, meeting cadence, decision rights, and what counts as a ready deliverable.

## Maintenance

Skills are maintained working assets, not frozen snapshots:

- Improve them when real usage exposes gaps, ambiguity, or inefficient behavior.
- Keep guidance aligned with current tools, workflows, and quality standards.
- Consolidate overlapping Skills when a simpler boundary serves users better.
- Reclassify a Skill when its actual use no longer matches its scenario.
- Replace or retire Skills that no longer provide reliable value.

## Contributing

Contributions may add, improve, move, consolidate, or retire Skills.

1. Start from a concrete use case or observed failure.
2. Select the scenario that matches the work context rather than the author or implementation technology.
3. Add a self-contained Skill directory with valid `name` and `description` frontmatter.
4. Include only the references, scripts, assets, or agent metadata required by the Skill.
5. Validate both individual Skill structure and default repository discovery.
6. Explain the practical evidence, intended applicability, and non-goals in the pull request.

## License

Apache-2.0
