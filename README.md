# Lab Skills

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

## Skill Catalog

### Agent development

- **[agent-builder](./agent-development/agent-builder/)**
  - Design and build AI agents. The bundled starter code currently uses the Anthropic Python SDK, while the architectural guidance is intended to remain provider-neutral.
  - **Typical use:** Define an agent's purpose, tools, knowledge, context, trust boundary, and subagent structure.
  - **Example:** `Use $agent-builder to design a customer-support agent that can search policy, inspect orders, and escalate refunds.`

- **[skill-judge](./agent-development/skill-judge/)**
  - Evaluate and improve Agent Skill packages with a practice-derived diagnostic rubric.
  - **Typical use:** Review whether a `SKILL.md` triggers correctly, adds real expert knowledge, loads references predictably, and avoids instruction sprawl.
  - **Example:** `Use $skill-judge to review this Skill package and give me the three highest-impact improvements.`

### Agent operations

- **[extract-agent-sessions](./agent-operations/extract-agent-sessions/)**
  - Recover clean human-visible conversations from supported Claude Code, Codex, opencode, and Grok Build session stores.
  - **Typical use:** Reconstruct recent user/assistant conversations while excluding tool calls, reasoning, system injection, copied history, and subagent noise.
  - **Example:** `Use $extract-agent-sessions to summarize my root Codex and Claude Code conversations from the last three days.`

### Content and publishing

- **[media-writer](./content-publishing/media-writer/)**
  - Adapt technical content to the culture and expectations of supported publishing platforms.
  - **Typical use:** Turn one technical idea into a platform-native WeChat, Hacker News, Reddit, Medium, X/Twitter, Dev.to, or LinkedIn post.
  - **Example:** `Use $media-writer to turn this architecture note into a Hacker News launch post without marketing language.`

### Research and analysis

```text
Broad question
      │
      ▼
deep-architecture-research
      │ clarify → confirm → investigate
      ▼
understanding-first-report
      │ verdict → mechanism → action
      ▼
Clear human understanding
```

- **[deep-architecture-research](./research-analysis/deep-architecture-research/)**
  - Clarify broad system questions before investigating architecture through source, history, official documentation, and calibrated community evidence.
  - **Typical use:** Compare frameworks or SDKs, understand a source-level mechanism, trace breaking architectural changes, or gather evidence before designing a system.
  - **Example:** `Use $deep-architecture-research to clarify and compare how these agent runtimes own sessions, memory, workspaces, and deployment.`

- **[understanding-first-report](./research-analysis/understanding-first-report/)**
  - Turn complex technical work into a verdict-first brief with truthful diagrams, code provenance, and low cognitive load.
  - **Typical use:** Compress a large research artifact, architecture review, decision, or status update into the main contradiction, decisive evidence, and one recommendation.
  - **Example:** `Use $understanding-first-report to explain this research to a human architect in under 3,000 Chinese characters.`

The two Skills work well together, but each remains independently usable.

### Software engineering

- **[vibe-coding](./software-engineering/vibe-coding/)**
  - Turn an AI agent into a disciplined software development partner with transparent decisions and proportionate verification.
  - **Typical use:** Build a feature, fix a bug, refactor code, improve performance, or perform a migration while respecting the existing codebase.
  - **Example:** `Use $vibe-coding to add this feature to the existing service, follow its conventions, and verify the real integration path.`

### Team collaboration and communication

- **[meeting-coach-leader](./team-collaboration/meeting-coach-leader/)**
  - Help leaders and managers prepare, run, and review high-bandwidth meetings that advance real work and decisions.
  - **Typical use:** Prepare a work review, diagnose repeated low-value meetings, give direct feedback, or close a decision with clear ownership.
  - **Example:** `Use $meeting-coach-leader to review this meeting transcript and design a shorter follow-up that reaches a decision.`

- **[meeting-coach-worker](./team-collaboration/meeting-coach-worker/)**
  - Help workers turn meetings, feedback, and work notes into better execution and stronger updates.
  - **Typical use:** Infer leader expectations, review whether current work is ready, identify the highest-value next action, and prepare for the next meeting.
  - **Example:** `Use $meeting-coach-worker to tell me what my manager expects, what is missing from my work, and how to report it next time.`

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
