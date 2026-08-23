# Lab Skills

[English](./README.md) | 简体中文 | [日本語](./README.ja.md)

这些 Skill 来自 Lab 在工程研发、技术调研、内容发布与团队协作中的真实实践。

仓库将其中可复用的工作方法整理出来，供参考、讨论、调整与持续改进。

适用于 AI 编程 Agent，以及其他支持 [Agent Skills 规范](https://agentskills.io/specification)的系统。

## 范围

这是一个只包含 Skill 的仓库，不提供插件、通用教程或无关文章。

每个 Skill 都应当能够独立理解和使用。部分目录可能包含可选的 Agent 元数据，但核心指令不依赖某一种产品运行时。

这些 Skill 来源于实践，而不是通用标准。使用前请阅读各 Skill 的 description，并根据自己的工具、组织和工作环境调整不适用的假设。

## 安装

查看仓库中可用的 Skill：

```bash
npx skills add shareai-lab/lab-skills --list
```

为自动识别出的 Agent 环境安装全部 Skill：

```bash
npx skills add shareai-lab/lab-skills --skill '*' -y
```

安装单个 Skill：

```bash
npx skills add shareai-lab/lab-skills --skill deep-architecture-research
```

不安装 Skill，仅生成一次使用提示：

```bash
npx skills use shareai-lab/lab-skills@understanding-first-report
```

## 同步上游更新

从记录的上游来源更新当前范围内的全部已安装 Skill：

```bash
npx skills update
```

只更新一个 Skill：

```bash
npx skills update deep-architecture-research
```

无交互更新项目级 Skill：

```bash
npx skills update --project -y
```

无交互更新全局 Skill：

```bash
npx skills update --global -y
```

如果曾安装改名前的 Skill，请执行一次迁移：

```bash
npx skills remove boss-meet meet-work extract-agent-sessions -y
npx skills add shareai-lab/lab-skills \
  --skill meeting-coach-leader meeting-coach-worker \
          review-ai-conversations -y
```

## Skill 目录

### 调研与分析

#### [review-ai-conversations](./research-analysis/review-ai-conversations/)

回顾不同 AI Worker 上的近期对话，将信息压缩到核心价值，梳理问题空间，并产生跨 Session 的新洞察。

**推荐场景**

- 回顾最近在 Claude Code、Codex、opencode、Grok Build 或 Cursor 中推进的工作。
- 聚类反复出现的问题，并梳理维度、交集、依赖关系与未解决缺口。
- 将近期文档、代码产物和 AI 结论作为参考资料，而不是未经验证的唯一事实。
- 产生新的洞察、问题重构、头脑风暴方向和高价值下一步问题。

**使用示例**

```text
/review-ai-conversations 回顾我最近和 AI Worker 的聊天，
聚类核心问题，梳理问题空间，并产生新的洞察和下一步问题。
```

#### [deep-architecture-research](./research-analysis/deep-architecture-research/)

先澄清宽泛的系统问题，再结合源码、历史、官方文档和经过校准的社区证据进行深入研究。

**推荐场景**

- 从源码层面对比框架、Runtime、SDK 或技术项目。
- 追踪重要架构变化、破坏性更新、困难边界和争议场景。
- 在设计新系统或选择实现路径前收集可靠证据。

**使用示例**

```text
/deep-architecture-research 澄清并比较这些 Agent Runtime
如何管理 Session、Memory、Workspace 和 Deployment。
```

#### [understanding-first-report](./research-analysis/understanding-first-report/)

将长时间、多轮的技术工作重新梳理为清晰的问题空间、更深的洞见和专业汇报。恢复相关上下文，说明哪些已查清、哪些仍待确认，再按容易进入状态的顺序给出判断。

**推荐场景**

- 在 Agent 长时间工作后，重新连接前面的问题、范围变化和已经接受的选择。
- 梳理问题集，找到更本质的需求或矛盾，判断答案是否成熟，再按清楚的决策顺序汇报。

**使用示例**

```text
/understanding-first-report 重新连接前面多轮问题，画出问题空间，
说明哪些已查清、哪些仍待确认，再给出洞见和下一步。
```

两个 Skill 适合组合使用，但也可以各自独立使用。

### 软件工程

#### [vibe-coding](./software-engineering/vibe-coding/)

将 AI Agent 变成能够透明决策、适度验证并保持工程品位的开发伙伴。

**推荐场景**

- 在尊重现有代码规范的前提下增加功能。
- 沿真实失败路径诊断和修复 Bug。
- 以适当验证完成重构、性能优化或迁移。

**使用示例**

```text
/vibe-coding 在现有服务中增加这个功能，遵循已有规范，
并验证真实的集成路径。
```

### 团队协作与沟通

#### [meeting-coach-leader](./team-collaboration/meeting-coach-leader/)

帮助负责人和管理者准备、主持和复盘能够推动真实工作与决策的高带宽会议。

**推荐场景**

- 准备或复盘员工工作评审会议。
- 诊断反复出现的低价值讨论和缺失的决策前提。
- 给出直接具体的反馈，同时不接管工作者的责任。

**使用示例**

```text
/meeting-coach-leader 复盘这份会议记录，设计一个更短、
能够真正形成决策的后续会议。
```

#### [meeting-coach-worker](./team-collaboration/meeting-coach-worker/)

帮助工作者把会议、反馈和工作笔记转化为更好的执行和更清晰的汇报。

**推荐场景**

- 从近期会议证据中理解负责人真正期待的结果。
- 判断当前工作是否适合汇报，以及还缺少什么。
- 找出最高价值的下一步，并准备简洁的工作更新。

**使用示例**

```text
/meeting-coach-worker 告诉我负责人真正期待什么、
当前工作缺少什么，以及下次应该如何汇报。
```

### Agent 开发

#### [agent-builder](./agent-development/agent-builder/)

设计和构建 AI Agent。附带的启动代码目前使用 Anthropic Python SDK，但架构指导尽量保持 Provider 无关。

**推荐场景**

- 定义 Agent 的目标、能力、知识、上下文与信任边界。
- 判断是否真的需要规划、Subagent、Skill 或额外工具。

**使用示例**

```text
/agent-builder 设计一个客服 Agent，能够搜索政策、
检查订单，并升级处理退款请求。
```

#### [skill-judge](./agent-development/skill-judge/)

使用源于实践的诊断标准评估和改进 Agent Skill。

**推荐场景**

- 检查 `SKILL.md` 是否能正确触发并提供真正的专家知识。
- 诊断指令膨胀、引用不清、自由度失衡或完成条件模糊。

**使用示例**

```text
/skill-judge 评审这个 Skill，并给出三个影响最大的改进建议。
```

### 内容与发布

#### [media-writer](./content-publishing/media-writer/)

根据不同社区的文化和表达习惯改写技术内容。

**推荐场景**

- 将同一个技术主题改写为微信公众号、Hacker News、Reddit、Medium、X/Twitter、Dev.to 或 LinkedIn 内容。
- 保留目标社区的真实语气，而不是套用统一的社交媒体模板。

**使用示例**

```text
/media-writer 将这篇架构笔记改写成 Hacker News 发布帖，
不要使用营销语言。
```

## 团队协作说明

两个 meeting-coach Skill 强调真实工作、清晰决策、交付准备度、高带宽沟通和明确责任。

它们用于通过会议改进工作，而不是规定一套通用管理文化。

应用到其他组织时，请重新考虑其中关于层级、反馈方式、会议节奏、决策权和交付标准的假设。

## 维护

Skill 是持续维护的工作资产，而不是冻结的快照：

- 当真实使用暴露出缺口、歧义或低效行为时进行改进。
- 保持指令与当前工具、工作流和质量标准一致。
- 当更简单的边界更有效时，合并重叠 Skill。
- 当 Skill 不再符合所属场景时重新分类。
- 替换或停用已经无法稳定提供价值的 Skill。

## 贡献

贡献可以增加、改进、移动、合并或停用 Skill。

1. 从真实使用场景或已经观察到的失败开始。
2. 根据工作场景选择目录，而不是根据作者或实现技术分类。
3. 添加包含有效 `name` 和 `description` frontmatter 的独立 Skill 目录。
4. 只加入 Skill 实际需要的 references、scripts、assets 或 Agent 元数据。
5. 同时验证单个 Skill 结构和仓库默认发现行为。
6. 在 Pull Request 中解释实践证据、适用范围和非目标。

## 许可证

Apache-2.0
