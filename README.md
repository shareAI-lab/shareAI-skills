# Lab Skills

Skills distilled from the Lab's real work and collaboration practices. The parts that may generalize beyond our context are shared for reference, discussion, and continued improvement.

[中文文档](./README_zh.md)

[![skills.sh](https://skills.sh/b/shareai-lab/lab-skills)](https://skills.sh/shareai-lab/lab-skills)

> Works with **[Kode CLI](https://github.com/shareAI-lab/Kode-CLI)**, **Claude Code**, **Codex**, **Cursor**, and any agent supporting the [Agent Skills specification](https://agentskills.io/specification).

## Installation

```bash
npx skills add shareai-lab/lab-skills
```

Install one skill:

```bash
npx skills add shareai-lab/lab-skills --skill extract-agent-sessions
```

Browse the collection on [skills.sh](https://skills.sh/shareai-lab/lab-skills).

## Available Skills

| Skill | Description |
|-------|-------------|
| [skill-judge](./skills/skill-judge/) | Evaluate Agent Skill quality across 8 dimensions (120-point system) |
| [media-writer](./skills/media-writer/) | Adapt content for WeChat, HN, Reddit, Medium, Twitter, Dev.to, LinkedIn |
| [agent-builder](./skills/agent-builder/) | Design and build AI agents for any domain |
| [vibe-coding](./skills/vibe-coding/) | Vibe-driven development with minimal specs |
| [extract-agent-sessions](./skills/extract-agent-sessions/) | Recover recent local agent conversations on Linux/macOS without tool, reasoning, or subagent noise |
| [meet-work](./skills/team-meet/meet-work/) | Turn recent meetings into better work, delivery reviews, and high-bandwidth employee reports |
| [boss-meet](./skills/team-meet/boss-meet/) | Help managers run decision-oriented meetings and give direct, constructive feedback |

## Repository Scope and Maintenance

This is a skills-only repository. It does not ship product-specific plugin manifests or runtime integration metadata.

Skills here are maintained working assets, not frozen snapshots:

- Real usage, failure cases, and changing workflows should drive improvements.
- Existing skills should be refined when their guidance becomes ambiguous, incomplete, or outdated.
- Skills that no longer provide reliable value or meet the current quality bar should be replaced or removed.
- Contributions may add, improve, consolidate, or retire skills as the collection evolves.

## How to Create Great Skills

Creating a truly effective skill is an art. We've analyzed 17 official Anthropic skills and distilled the core principles:

**Core Formula:**
```
Good Skill = Expert-only Knowledge - What Claude Already Knows
```

Read the full guide: **[How to Create Great Agent Skills](./docs/how-to-create-great-agent-skill.md)**

Use the [skill-judge](./skills/skill-judge/) skill to evaluate your skill's quality with structured scoring across 8 dimensions:

| Dimension | Points | Focus |
|-----------|--------|-------|
| Knowledge Delta | 20 | Expert-only knowledge vs. what Claude already knows |
| Mindset + Procedures | 15 | Thinking patterns + domain-specific workflows |
| Anti-Pattern Quality | 15 | Specific NEVER lists with non-obvious reasons |
| Specification (esp. Description) | 15 | Description with WHAT, WHEN, and KEYWORDS |
| Progressive Disclosure | 15 | Content layering, loading triggers |
| Freedom Calibration | 15 | Specificity matched to task fragility |
| Pattern Recognition | 10 | Follows established skill patterns |
| Practical Usability | 15 | Decision trees, working examples, edge cases |

## What are Skills?

Skills are modular knowledge packages that give AI agents domain expertise on-demand. They follow the [Agent Skills specification](https://agentskills.io/specification).

## Skill Structure

```
skill-name/
├── SKILL.md              # Core instructions (required)
├── references/           # Detailed documentation (optional)
├── scripts/              # Executable code (optional)
└── assets/               # Templates and resources (optional)
```

## Philosophy

> **Skills are knowledge, not code.**

A skill doesn't tell the agent what to do step-by-step. It gives the agent the knowledge to figure out what to do. The model is smart - your job is to inform it, not constrain it.

## Contributing

We welcome contributions! To add a new skill:

1. Create a directory under `skills/`
2. Add a `SKILL.md` with YAML frontmatter (name, description)
3. Include any necessary references, scripts, or assets
4. Submit a PR

## Related

| Repository | Purpose |
|------------|---------|
| [Kode](https://github.com/shareAI-lab/Kode-CLI) | Full-featured open source agent CLI |
| [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | Learn how to build AI agents from scratch |
| [Agent Skills specification](https://agentskills.io/specification) | Open specification |

## License

Apache-2.0
