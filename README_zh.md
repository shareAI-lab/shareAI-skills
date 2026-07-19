# shareAI Skills

扩展 AI Agent 能力的知识包。

[English](./README.md)

[![skills.sh](https://skills.sh/b/shareai-lab/shareai-skills)](https://skills.sh/shareai-lab/shareai-skills)

> 兼容 **[Kode CLI](https://github.com/shareAI-lab/Kode-CLI)**、**Claude Code**、**Codex**、**Cursor**，以及任何支持 [Agent Skills 规范](https://agentskills.io/specification) 的 Agent。

## 安装

### skills CLI（推荐）

使用 Vercel 开源的 [`skills` CLI](https://github.com/vercel-labs/skills) 浏览本仓库、选择 Skill，并安装到受支持的 Agent：

```bash
npx skills add shareai-lab/shareai-skills
```

在普通终端中，这会进入引导式安装流程。在 Agent 控制的 Shell 中，CLI 可能检测到
当前 Agent 并改用非交互默认值；自动化场景应显式传入 `--skill` 和 `--agent`，
避免安装范围不明确。

当前 CLI 版本要求 Node.js 22.20 或更高版本。默认安装到当前项目；添加
`--global`（`-g`）可让 Skill 在所有项目中使用。

### 常用命令

```bash
# 只查看可用 Skill，不安装
npx skills add shareai-lab/shareai-skills --list

# 将一个 Skill 全局安装到 Codex
npx skills add shareai-lab/shareai-skills \
  --skill extract-agent-sessions --agent codex --global

# 将本仓库全部 Skill 安装到当前项目的 Kode 与 Claude Code
npx skills add shareai-lab/shareai-skills \
  --skill '*' --agent kode claude-code
```

支持的目标名称包括 `kode`、`claude-code`、`codex` 和 `cursor`。自动化安装可添加
`--yes` 跳过确认；无法使用符号链接时可添加 `--copy`。

> `--all` 表示把所有 Skill 安装到 CLI 已知的所有 Agent。只想安装到指定 Agent
> 时，应使用上面展示的 `--skill '*' --agent ...`。

### 管理已安装的 Skill

```bash
# 查看当前项目安装的 Skill
npx skills list

# 更新已安装的 Skill
npx skills update

# 从 Codex 中卸载一个 Skill
npx skills remove extract-agent-sessions --agent codex
```

CLI 会上报匿名安装遥测，用于 skills.sh 排行榜。设置 `DISABLE_TELEMETRY=1` 或
`DO_NOT_TRACK=1` 可以关闭。所有 Agent 目标与参数参见
[官方 CLI 文档](https://github.com/vercel-labs/skills#readme)，也可以在
[skills.sh](https://skills.sh/shareai-lab/shareai-skills) 浏览本合集。

## 可用 Skills

| Skill | 描述 |
|-------|------|
| [skill-judge](./skills/skill-judge/) | 8维度评估 Agent Skill 设计质量（120分制） |
| [media-writer](./skills/media-writer/) | 适配各平台内容：微信、HN、Reddit、Medium、Twitter、Dev.to、LinkedIn |
| [agent-builder](./skills/agent-builder/) | 为任何领域设计和构建 AI Agent |
| [vibe-coding](./skills/vibe-coding/) | 氛围驱动开发，极简规格 |
| [extract-agent-sessions](./skills/extract-agent-sessions/) | 在 Linux/macOS 恢复近期本地 Agent 对话，排除工具、推理和子代理噪声 |

## 如何创建好的 Skill

创建真正有效的 Skill 是一门艺术。我们分析了 17 个 Anthropic 官方 Skill，提炼出核心原则：

**核心公式：**
```
好 Skill = 专家独有的知识 - Claude 已有的知识
```

阅读完整指南：**[How to Create Great Agent Skills](./docs/how-to-create-great-agent-skill.md)**（英文教学文档）

使用 [skill-judge](./skills/skill-judge/) 对你的 Skill 进行 8 维度结构化评分：

| 维度 | 分值 | 关注点 |
|------|------|--------|
| 知识增量 | 20 | 专家独有知识 vs Claude 已知内容 |
| 思维方式 + 领域流程 | 15 | 思考框架 + Claude 不知道的领域特定流程 |
| 反模式质量 | 15 | 具体的 NEVER 清单及非显而易见的原因 |
| 规范合规（尤其是 description） | 15 | description 必须包含 WHAT、WHEN、KEYWORDS |
| 渐进式披露 | 15 | 内容分层，加载触发机制 |
| 自由度校准 | 15 | 具体程度与任务脆弱性匹配 |
| 模式识别 | 10 | 遵循已验证的 Skill 设计模式 |
| 实用性 | 15 | 决策树、可运行示例、边缘情况覆盖 |

## 什么是 Skills？

Skills 是模块化的知识包，为 AI Agent 按需提供领域专业知识。它们遵循 [Agent Skills 规范](https://agentskills.io/specification)。

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
| [Kode](https://github.com/shareAI-lab/Kode-CLI) | 全功能开源 Agent CLI |
| [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | 从零学习如何构建 AI Agent |
| [Agent Skills 规范](https://agentskills.io/specification) | 开放规范 |

## License

Apache-2.0
