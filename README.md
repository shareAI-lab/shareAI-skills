# Lab Skills

Skills distilled from the Lab's real work and collaboration practices. Potentially generalizable parts are shared for reference, discussion, and continued improvement.

[![skills.sh](https://skills.sh/b/shareai-lab/lab-skills)](https://skills.sh/shareai-lab/lab-skills)

> Compatible with **[Kode CLI](https://github.com/shareAI-lab/Kode-CLI)**, **Claude Code**, **Codex**, **Cursor**, and any agent that supports the [Agent Skills specification](https://agentskills.io/specification).

## Purpose

This is a skills-only repository. It does not ship product-specific plugin manifests or runtime integration metadata.

These skills come from practice, not from a claim of universal correctness. Use them as working references, adapt them to local context, and improve them when real usage reveals better approaches.

## Installation

Install the collection:

```bash
npx skills add shareai-lab/lab-skills
```

Install one skill:

```bash
npx skills add shareai-lab/lab-skills --skill extract-agent-sessions
```

Browse the collection on [skills.sh](https://skills.sh/shareai-lab/lab-skills).

## Available Skills

| Skill | Purpose |
|-------|---------|
| [agent-builder](./agent-builder/) | Design and build AI agents for a specific domain or workflow |
| [extract-agent-sessions](./extract-agent-sessions/) | Recover clean recent conversations from local agent session stores |
| [media-writer](./media-writer/) | Adapt content to the culture and expectations of each publishing platform |
| [skill-judge](./skill-judge/) | Evaluate and improve Agent Skill design quality |
| [boss-meet](./boss-meet/) | Help managers run decision-oriented meetings and give direct, constructive feedback |
| [meet-work](./meet-work/) | Turn recent meetings into better work, delivery reviews, and high-bandwidth updates |
| [vibe-coding](./vibe-coding/) | Turn an AI agent into a disciplined software development partner |

## Repository Layout

Every skill directory lives at the repository root so standard installers can discover the complete collection without special flags.

```text
lab-skills/
├── agent-builder/
├── boss-meet/
├── extract-agent-sessions/
├── media-writer/
├── meet-work/
├── skill-judge/
└── vibe-coding/
```

Each skill is self-contained:

```text
skill-name/
├── SKILL.md              # Required instructions and trigger metadata
├── references/           # Optional detailed knowledge
├── scripts/              # Optional deterministic helpers
├── assets/               # Optional output resources
└── agents/               # Optional agent-facing metadata
```

## Maintenance

Skills are maintained working assets, not frozen snapshots:

- Improve them when real usage exposes gaps, ambiguity, or inefficient behavior.
- Keep guidance aligned with current tools, workflows, and quality standards.
- Consolidate overlapping skills when a simpler structure serves users better.
- Replace or remove skills that no longer provide reliable value.

## Contributing

Contributions may add, improve, consolidate, or retire skills.

1. Start from a concrete use case or observed failure.
2. Add a self-contained skill directory at the repository root.
3. Include a valid `SKILL.md` with `name` and `description` frontmatter.
4. Add only the references, scripts, assets, or agent metadata required by the skill.
5. Validate the skill and submit a pull request that explains the practical evidence behind the change.

## Related Projects

| Project | Purpose |
|---------|---------|
| [Kode](https://github.com/shareAI-lab/Kode-CLI) | Open-source agent CLI |
| [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | Learn how to build an agent from first principles |
| [Agent Skills specification](https://agentskills.io/specification) | Open skill format specification |

## License

Apache-2.0
