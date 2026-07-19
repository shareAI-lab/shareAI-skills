# shareAI Skills

Knowledge packages that extend AI agent capabilities.

[中文文档](./README_zh.md)

[![skills.sh](https://skills.sh/b/shareai-lab/shareai-skills)](https://skills.sh/shareai-lab/shareai-skills)

> Works with **[Kode CLI](https://github.com/shareAI-lab/Kode-CLI)**, **Claude Code**, **Codex**, **Cursor**, and any agent supporting the [Agent Skills specification](https://agentskills.io/specification).

## Installation

### skills CLI (Recommended)

Use Vercel's open-source [`skills` CLI](https://github.com/vercel-labs/skills) to
discover the collection, select skills, and install them for supported agents:

```bash
npx skills add shareai-lab/shareai-skills
```

In a regular terminal this starts the guided installation flow. In an
agent-controlled shell, the CLI may detect the current agent and select
non-interactive defaults; pass explicit `--skill` and `--agent` values for
predictable automation.

The current CLI release requires Node.js 22.20 or later. Project-local installation
is the default; add `--global` (`-g`) to make a skill available across projects.

### Common commands

```bash
# Preview the skills without installing
npx skills add shareai-lab/shareai-skills --list

# Install one skill globally for Codex
npx skills add shareai-lab/shareai-skills \
  --skill extract-agent-sessions --agent codex --global

# Install every skill into the current project for Kode and Claude Code
npx skills add shareai-lab/shareai-skills \
  --skill '*' --agent kode claude-code
```

Supported target names include `kode`, `claude-code`, `codex`, and `cursor`. Add
`--yes` for non-interactive installation or `--copy` when symlinks are unsuitable.

> `--all` means every skill for every agent known to the CLI. To install every
> skill for only selected agents, use `--skill '*' --agent ...` as shown above.

### Manage installed skills

```bash
# List project-local installations
npx skills list

# Update installed skills
npx skills update

# Remove one skill from Codex
npx skills remove extract-agent-sessions --agent codex
```

The CLI reports anonymous installation telemetry for the skills.sh leaderboard.
Set `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1` to opt out. See the
[official CLI reference](https://github.com/vercel-labs/skills#readme) for every
agent target and option, or browse this collection on
[skills.sh](https://skills.sh/shareai-lab/shareai-skills).

## Available Skills

| Skill | Description |
|-------|-------------|
| [skill-judge](./skills/skill-judge/) | Evaluate Agent Skill quality across 8 dimensions (120-point system) |
| [media-writer](./skills/media-writer/) | Adapt content for WeChat, HN, Reddit, Medium, Twitter, Dev.to, LinkedIn |
| [agent-builder](./skills/agent-builder/) | Design and build AI agents for any domain |
| [vibe-coding](./skills/vibe-coding/) | Vibe-driven development with minimal specs |
| [extract-agent-sessions](./skills/extract-agent-sessions/) | Recover recent local agent conversations on Linux/macOS without tool, reasoning, or subagent noise |

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
