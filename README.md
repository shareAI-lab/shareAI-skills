# shareAI Skills

Knowledge packages that extend AI agent capabilities.

[中文文档](./README_zh.md)

## What are Skills?

Skills are modular knowledge packages that give AI agents domain expertise on-demand. They follow the [Agent Skills Spec](https://github.com/anthropics/agent-skills) and work with Claude Code, Cursor, and other compatible agents.

## Installation

### Claude Code

```bash
claude plugins install https://github.com/shareAI-lab/shareAI-skills
```

### Cursor

Copy the `skills/` directory to your Cursor skills folder.

### Other Agents

Load `SKILL.md` files on-demand when the agent needs domain expertise.

## Available Skills

| Skill | Description |
|-------|-------------|
| [agent-builder](./skills/agent-builder/) | Design and build AI agents for any domain |

## Skill Structure

Each skill follows this structure:

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

- [mini-claude-code](https://github.com/shareAI-lab/mini-claude-code) - Learn how to build AI agents from scratch
- [Agent Skills Spec](https://github.com/anthropics/agent-skills) - Official specification

## License

Apache-2.0
