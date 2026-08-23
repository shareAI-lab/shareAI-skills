# Lab Skills

Skills distilled from the Lab's real work and collaboration practices. Potentially reusable parts are shared for reference, discussion, adaptation, and continued improvement.

Designed for AI coding agents and other systems that support the [Agent Skills specification](https://agentskills.io/specification).

## Scope

This is a skills-only repository. It does not ship product-specific plugin manifests, runtime integration metadata, tutorials, or general articles.

The collection is practice-derived, not a universal standard. Each skill has a different portability boundary:

- **Opinionated**: broadly reusable while encoding strong assumptions about quality or method.
- **Tool-specific**: reusable only where the named tools, storage formats, or platforms apply.
- **Lab-oriented**: shaped by the Lab's work, collaboration style, and outcome-driven goals; adapt before using it as guidance for another organization.

## Installation

Preview the available skills without installing them:

```bash
npx skills add shareai-lab/lab-skills --list
```

Install all skills non-interactively for the detected agent environment:

```bash
npx skills add shareai-lab/lab-skills --skill '*' -y
```

Install one skill:

```bash
npx skills add shareai-lab/lab-skills --skill meet-work
```

## Skill Catalog

| Scenario | Skill | Applicability | Purpose |
|----------|-------|---------------|---------|
| Agent development | [agent-builder](./agent-development/agent-builder/) | Opinionated | Design and build AI agents; bundled starter code currently uses the Anthropic Python SDK |
| Agent development | [skill-judge](./agent-development/skill-judge/) | Opinionated | Evaluate and improve Agent Skill design quality with a practice-derived rubric |
| Agent operations | [extract-agent-sessions](./agent-operations/extract-agent-sessions/) | Tool-specific | Recover clean conversations from supported local agent session stores |
| Content and publishing | [media-writer](./content-publishing/media-writer/) | Tool-specific | Adapt content to the culture and expectations of supported publishing platforms |
| Research and analysis | [deep-architecture-research](./research-analysis/deep-architecture-research/) | Opinionated | Clarify broad system questions, then investigate architecture through source, history, official docs, and calibrated community evidence |
| Research and analysis | [understanding-first-report](./research-analysis/understanding-first-report/) | Opinionated | Turn deep technical work into a verdict-first brief with truthful diagrams, code provenance, and low cognitive load |
| Software engineering | [vibe-coding](./software-engineering/vibe-coding/) | Opinionated | Turn an AI agent into a disciplined software development partner |
| Team collaboration and communication | [boss-meet](./team-collaboration/boss-meet/) | Lab-oriented | Help managers run decision-oriented meetings and give direct, constructive feedback |
| Team collaboration and communication | [meet-work](./team-collaboration/meet-work/) | Lab-oriented | Turn recent meetings into better work, delivery reviews, decisions, and high-bandwidth updates |

## Repository Structure

Scenario directories form the first level. Self-contained skill directories form the second level.

```text
lab-skills/
├── agent-development/
│   ├── agent-builder/
│   └── skill-judge/
├── agent-operations/
│   └── extract-agent-sessions/
├── content-publishing/
│   └── media-writer/
├── research-analysis/
│   ├── deep-architecture-research/
│   └── understanding-first-report/
├── software-engineering/
│   └── vibe-coding/
└── team-collaboration/
    ├── boss-meet/
    └── meet-work/
```

Scenario directories are navigation boundaries only and do not contain a `SKILL.md`. Every actual skill remains self-contained:

```text
scenario/skill-name/
├── SKILL.md              # Required instructions and trigger metadata
├── references/           # Optional detailed knowledge
├── scripts/              # Optional deterministic helpers
├── assets/               # Optional output resources
└── agents/               # Optional agent-facing metadata
```

Use an existing scenario when its work context genuinely fits. Create a new scenario only when it represents a stable, reusable area of work rather than a temporary topic or ownership label.

## Lab-Oriented Guidance

The skills under `team-collaboration/` reflect the Lab's emphasis on substantive work, clear decisions, delivery readiness, high-bandwidth communication, and explicit ownership. They are intended to improve work through meetings, not to prescribe a universal management culture.

When applying them elsewhere, preserve the reasoning but reconsider assumptions about hierarchy, feedback style, meeting cadence, decision rights, and what counts as a ready deliverable.

## Maintenance

Skills are maintained working assets, not frozen snapshots:

- Improve them when real usage exposes gaps, ambiguity, or inefficient behavior.
- Keep guidance aligned with current tools, workflows, and quality standards.
- Consolidate overlapping skills when a simpler boundary serves users better.
- Reclassify a skill when its actual use no longer matches its scenario.
- Replace or remove skills that no longer provide reliable value.

## Contributing

Contributions may add, improve, move, consolidate, or retire skills.

1. Start from a concrete use case or observed failure.
2. Select the scenario that matches the work context rather than the author or implementation technology.
3. Add a self-contained skill directory with a valid `SKILL.md` containing `name` and `description` frontmatter.
4. Include only the references, scripts, assets, or agent metadata required by the skill.
5. Validate default repository discovery as well as the individual skill.
6. Explain the practical evidence, intended applicability, and non-goals in the pull request.

## License

Apache-2.0
