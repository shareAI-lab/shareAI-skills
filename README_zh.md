# shareAI Skills

扩展 AI Agent 能力的知识包。

[English](./README.md)

> 兼容 **[Kode CLI](https://github.com/shareAI-lab/Kode)**、**Claude Code**、**Cursor**，以及任何支持 [Agent Skills Spec](https://github.com/anthropics/agent-skills) 的 Agent。

## 安装

### Kode CLI（推荐）

```bash
kode plugins install https://github.com/shareAI-lab/shareAI-skills
```

### Claude Code

```bash
claude plugins install https://github.com/shareAI-lab/shareAI-skills
```

### Cursor

将 `skills/` 目录复制到你的 Cursor skills 文件夹。

### 其他 Agent

当 Agent 需要领域专业知识时，按需加载 `SKILL.md` 文件。

## 可用 Skills

| Skill | 描述 |
|-------|------|
| [agent-builder](./skills/agent-builder/) | 为任何领域设计和构建 AI Agent |

## 什么是 Skills？

Skills 是模块化的知识包，为 AI Agent 按需提供领域专业知识。它们遵循 [Agent Skills Spec](https://github.com/anthropics/agent-skills)。

## Skill 结构

```
skill-name/
├── SKILL.md              # 核心指令 (必需)
├── references/           # 详细文档 (可选)
├── scripts/              # 可执行代码 (可选)
└── assets/               # 模板和资源 (可选)
```

## 理念

> **Skills 是知识，不是代码。**

Skill 不是告诉 Agent 按步骤做什么，而是给 Agent 知识让它自己想出该做什么。模型很聪明——你的工作是为它提供信息，而不是限制它。

## 贡献

欢迎贡献！添加新 skill：

1. 在 `skills/` 下创建目录
2. 添加带 YAML frontmatter（name, description）的 `SKILL.md`
3. 包含必要的 references、scripts 或 assets
4. 提交 PR

## 相关

| 仓库 | 用途 |
|------|------|
| [Kode](https://github.com/shareAI-lab/Kode) | 全功能开源 Agent CLI |
| [mini-claude-code](https://github.com/shareAI-lab/mini-claude-code) | 从零学习如何构建 AI Agent |
| [Agent Skills Spec](https://github.com/anthropics/agent-skills) | 官方规范 |

## License

Apache-2.0
