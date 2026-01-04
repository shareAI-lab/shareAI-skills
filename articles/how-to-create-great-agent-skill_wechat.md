# 如何创建真正好的 Agent Skill

这篇文章不是泛泛而谈教你怎么给Agent创建Skill。

我们分析了 Anthropic 官方的 Skill 规范文档，逐行阅读了 17 个官方 Skill 示例的源码，提炼出判断 Skill 好坏的核心标准，并追溯每一条标准的来源和深层逻辑。

如果你想创建真正有价值的 Agent Skill，这篇文章会告诉你：什么是好的、什么是坏的、为什么，以及怎么做。

---

## 一、首先理解：Skill 到底是什么

### 1.1 一个根本性的误解

当大多数人听到"Agent Skill"时，脑子里想的是：**教 AI 如何做某件事**。

这是根本性的误解。

Claude 已经知道如何写代码。它知道如何调试。它知道如何设计系统架构。它知道什么是 PDF、什么是 Word 文档、什么是 API。

**这些，不需要你教。**

那 Skill 到底是什么？

### 1.2 Skill 是知识外化机制

传统 AI 的知识锁在模型参数里。想让模型学会新技能？

```
传统方式：
收集数据 → 设置 GPU 集群 → 参数训练 → 部署新版本
成本：$10,000 - $1,000,000+
周期：数周到数月
```

Skill 改变了这一切：

```
Skill 方式：
编辑 SKILL.md 文件 → 保存 → 下次触发时生效
成本：$0
周期：即时
```

这就像给 base model 外挂了一个可热插拔的 LoRA 适配器，但完全不需要训练。你用自然语言编辑一个 Markdown 文件，模型的行为就改变了。

**这是从"训练 AI"到"教育 AI"的范式转变。**

理解这一点，你才能理解为什么大多数 Skill 是垃圾——因为它们"教"的是 AI 已经知道的东西。

### 1.3 Tool vs Skill：一个关键区分

很多人把这两个概念混淆了。让我们澄清：

| 概念 | 本质 | 作用 | 例子 |
|------|------|------|------|
| **Tool（工具）** | 模型能**做**什么 | 执行动作 | bash、read_file、write_file、WebSearch |
| **Skill（技能）** | 模型**知道怎么做** | 指导决策 | PDF 处理、MCP 构建、前端设计、代码审查 |

工具是能力的边界——没有 bash 工具，模型无法执行命令。
技能是知识的注入——没有前端设计 Skill，模型写出的 UI 千篇一律。

**核心公式**：

```
通用 Agent + 优秀 Skill = 特定领域的专家 Agent
```

同一个 Claude 模型，加载不同的 Skill，就变成不同的专家。这就是 Skill 的价值所在。

换一种说法：

```
Agent 的能力上限 = 模型能力 + Skill 质量
```

模型能力是基座，Skill 质量决定了这个基座能发挥到什么程度。一个优秀的 Skill，能让通用 Agent 在特定领域的表现超越没有 Skill 加持的更强模型。

---

## 二、判断标准：从哪里来，为什么重要

我们提炼出 6 条判断 Skill 好坏的核心标准。每一条都有明确的来源，要么来自官方规范，要么来自对官方示例的系统分析，要么来自实践中发现的关键问题。

### 标准 1：Token 效率——每个段落是否值得它的开销

**来源**：Anthropic 官方 skill-creator 规范

官方原话：

> **Concise is Key.**
> The context window is a public good. Skills share the context window with everything else Claude needs: system prompt, conversation history, other Skills' metadata, and the actual user request.

> **Default assumption: Claude is already very smart.**
> Only add context Claude doesn't already have. Challenge each piece of information: "Does Claude really need this explanation?" and "Does this paragraph justify its token cost?"

**深层逻辑**：

Context window 是公共资源。一个 Skill 占用的 token，会挤压其他内容的空间——系统提示、对话历史、其他 Skill 的元数据、用户的实际请求。

当你写一段"什么是 PDF"的解释时，你在浪费这个公共资源。Claude 已经知道什么是 PDF。这 100 个 token 本可以用来存放更有价值的信息。

**如何判断**：

对 Skill 中的每个段落，问三个问题：
1. Claude 真的不知道这个吗？
2. 删掉它会影响任务完成吗？
3. 这 100 个 token 能换来什么价值？

如果答案是"Claude 已经知道"或"删掉无所谓"，删掉。

**核心公式**：

```
好 Skill = 专家独有的知识 - Claude 已有的知识
```

这个公式是判断 Skill 价值的根本标准。你可以把 Skill 理解为**专家大脑的压缩文件**——把一个设计师 10 年的审美积累压缩成 43 行，把一个文档专家的操作经验压缩成 200 行决策树。压缩的必须是 Claude 没有的东西，否则就是垃圾压缩。

---

### 标准 2：心智模型 vs 机械步骤——传递的是什么

**来源**：分析 17 个官方 Skill 示例，特别是 frontend-design、canvas-design

**发现**：

官方最精简的 Skill——frontend-design，只有 43 行。但它极其有效。

它没有教 Claude 如何写 CSS。它没有解释什么是 flexbox。它没有列出 Step 1、Step 2、Step 3。

它做的事情是：

```markdown
Before coding, understand the context and commit to a BOLD aesthetic direction:
- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic...
- **Differentiation**: What makes this UNFORGETTABLE?

NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto),
cliched color schemes (purple gradients on white backgrounds)...
```

它激活的是**设计师的思维方式**——在动手写代码之前，先想清楚几个关键问题。这是专家和新手的本质区别。

**深层逻辑**：

专家和新手的差异不在于"会不会操作"，而在于"如何思考问题"。一个资深设计师和一个初学者，都会写 CSS。但设计师在写第一行代码之前，脑子里已经有了清晰的审美方向、用户场景、差异化定位。

好的 Skill 传递的是这种思维方式，而不是机械的操作步骤。

**对比**：

| 维度 | 平庸 Skill | 优秀 Skill |
|------|-----------|-----------|
| 内容 | Step 1, Step 2, Step 3 | 思考框架、决策原则 |
| 假设 | Agent 不会做 | Agent 会做，但不知道怎么想 |
| 效果 | Agent 照本宣科 | Agent 像专家一样思考 |

---

### 标准 3：反模式清单——明确什么不能做

**来源**：分析官方 Skill 的普遍特征

**发现**：

几乎所有优秀的官方 Skill 都包含明确的"NEVER"清单。

frontend-design：
```markdown
NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial),
cliched color schemes (particularly purple gradients on white backgrounds),
predictable layouts and component patterns...
```

canvas-design：
```markdown
NEVER lose sight of the idea that this should be art, not something that's cartoony or amateur.
```

**深层逻辑**：

专家知识的一半是"知道什么能做"，另一半是"知道什么绝对不能做"。

一个资深设计师看到紫色渐变配白色背景，会本能地皱眉——"太 AI 感了"。这种"什么不能做"的直觉，是踩过无数坑之后形成的。

Claude 没有踩过这些坑。它不知道 Inter 字体已经被用滥了，不知道紫色渐变是 AI 生成内容的标志。

好的 Skill 要把这些"绝对不能做"的事情明确写出来。这比"应该做什么"更有价值，因为它划定了品质的底线。

**如何判断**：

你的 Skill 里有没有明确的"NEVER"清单？有没有告诉 Agent 什么是"垃圾做法"？

---

### 标准 4：Description 触发机制——何时被激活

**来源**：官方 skill-creator 规范

官方原话：

> This is the primary triggering mechanism for your skill, and helps Claude understand when to use the skill.
> Include both what the Skill does and specific triggers/contexts for when to use it.
> Include all "when to use" information here - Not in the body. The body is only loaded after triggering.

**深层逻辑**：

Skill 的加载分三层：

```
Layer 1: Metadata（始终在内存中）
         只有 name + description
         ~100 tokens / skill

Layer 2: SKILL.md Body（触发后才加载）
         详细指南、代码示例、决策树
         < 5000 tokens

Layer 3: Resources（按需加载）
         scripts/, references/, assets/
         无限制
```

关键点：**description 是唯一始终可见的部分**。Agent 根据 description 决定是否激活这个 Skill。如果 description 太模糊，Skill 就无法在正确的时机被触发。

**好的 description**：

```yaml
description: "Comprehensive document creation, editing, and analysis with support
for tracked changes, comments, formatting preservation, and text extraction.
When Claude needs to work with professional documents (.docx files) for:
(1) Creating new documents, (2) Modifying or editing content,
(3) Working with tracked changes, (4) Adding comments, or any other document tasks"
```

特点：
- 描述功能（what it does）
- 列出触发场景（when to use）
- 包含关键词（.docx files, tracked changes）

**差的 description**：

```yaml
description: "处理文档相关功能"
```

问题：太模糊，Agent 不知道什么时候该用它。

---

### 标准 5：自由度校准——与任务脆弱性匹配

**来源**：分析 docx（低自由度）vs frontend-design（高自由度）的设计差异

官方 skill-creator 规范：

> Match the level of specificity to the task's fragility and variability:
>
> **High freedom (text-based instructions)**: Use when multiple approaches are valid, decisions depend on context.
>
> **Medium freedom (pseudocode or scripts with parameters)**: Use when a preferred pattern exists, some variation is acceptable.
>
> **Low freedom (specific scripts, few parameters)**: Use when operations are fragile and error-prone, consistency is critical.

**深层逻辑**：

不同类型的任务需要不同程度的约束。

创意设计任务：需要高自由度。你给 Agent 一个审美方向，让它自己发挥。过度约束会扼杀创意。

文件格式操作任务：需要低自由度。Word 文档的 OOXML 格式有严格的规范，一个字符写错就会导致文件损坏。这种任务需要精确的脚本和详细的步骤。

**对应关系**：

| 任务类型 | 应有的自由度 | 原因 | 示例 Skill |
|----------|--------------|------|------------|
| 创意设计 | 高 | 多种方法有效，差异化是价值 | frontend-design |
| 代码审查 | 中 | 有原则但需要判断 | 代码审查 Skill |
| 文件格式操作 | 低 | 操作脆弱，一致性关键 | docx, xlsx |

**如何判断**：

问自己：这个任务容错率高还是低？如果 Agent 做错一步，后果是什么？

容错率高 → 给原则，不给步骤
容错率低 → 给脚本，少参数

---

### 标准 6：加载触发设计——Reference 能否被正确使用

**来源**：实践中发现的关键问题

**问题**：

很多 Skill 有详细的 reference 文档，但 Agent 不读。或者读太多。

这是一个光谱问题：

```
加载率太低 ◄─────────────────────────────────────────────► 过度加载

问题：                                              问题：
- Reference 形同虚设                                 - 浪费上下文空间
- 知识放了跟没放一样                                 - 无关信息稀释关键内容
- Agent 不知道何时该加载                             - Token 开销不必要增加
```

**深层原因**：

不同 Agent 对 Skill 机制的训练程度不同：
- Claude 对 Skill 机制有专门训练，会适度主动加载
- 大多数 Agent 没有专门训练，不会主动加载
- 有些 Agent 过于积极，一次性加载太多

你不能假设 Agent 会"聪明地"按需加载。你必须显式设计加载触发机制。

**解决方案**：

在工作流的关键节点嵌入强制加载指令。官方 docx Skill 的做法：

```markdown
### Creating New Document

**MANDATORY - READ ENTIRE FILE**: Before proceeding, you MUST read
[`docx-js.md`](docx-js.md) (~500 lines) completely from start to finish.
**NEVER set any range limits when reading this file.**
```

"MANDATORY"、"MUST"、"NEVER" 不是装饰词，是确保 Agent 执行的关键信号。

**注意**：这条标准只对有 reference 目录的中等/复杂 Skill 重要。简单型 Skill（如 frontend-design，43 行，无 reference）不需要考虑这个问题。

---

## 三、好 Skill vs 坏 Skill：深度对比

理论讲完了，让我们看具体例子。

### 3.1 坏 Skill 示例

> **# PDF 处理技能**
>
> **## 什么是 PDF**
>
> PDF（Portable Document Format，便携式文档格式）是由 Adobe 公司在 1993 年开发的一种文件格式。它可以在不同的操作系统和设备上保持文档的格式不变，包括字体、图像、排版等元素。PDF 文件可以包含文本、图像、超链接、表单字段、视频等多种元素。
>
> **## PDF 的特点**
>
> 1. 跨平台兼容性
> 2. 格式保持一致
> 3. 支持加密和权限控制
> 4. 文件大小相对较小
>
> **## 如何读取 PDF**
>
> 要读取 PDF 文件，你可以使用多种方法：
>
> **### 方法一：使用 PyPDF2**
>
> Step 1: 首先安装 PyPDF2 库
> `pip install PyPDF2`
>
> Step 2: 导入库
> `from PyPDF2 import PdfReader`
>
> Step 3: 打开 PDF 文件
> `reader = PdfReader("document.pdf")`
>
> Step 4: 读取页面内容
> `page = reader.pages[0]`
> `text = page.extract_text()`
>
> **### 方法二：使用 pdfplumber**
> ...

**问题分析**：

| 问题 | 具体表现 | 后果 |
|------|----------|------|
| 解释基础概念 | "什么是 PDF"、"PDF 的特点" | 浪费 200+ token，Claude 已经知道 |
| 机械步骤 | Step 1, 2, 3, 4 | Claude 已经会写代码，不需要手把手教 |
| 没有决策指导 | 列了两种方法但没说什么时候用哪种 | Agent 不知道如何选择 |
| 没有反模式 | 没有说什么情况会出错 | Agent 会踩坑 |
| 没有边缘情况 | 没有提到扫描件、加密 PDF 等 | 遇到特殊情况会失败 |

### 3.2 好 Skill 示例

```yaml
---
name: pdf-processing
description: 处理 PDF 文件。当用户需要读取 PDF 文本、提取表格数据、
             填写 PDF 表单、合并或拆分 PDF、将 PDF 转换为图片时使用。
---
```

> **# PDF 处理决策树**
>
> 根据任务类型选择工具：
>
> | 任务 | 首选工具 | 备选 | 何时用备选 |
> |------|----------|------|-----------|
> | 读取纯文本 | pdftotext | PyMuPDF | 需要保留布局信息 |
> | 提取表格 | camelot-py | tabula-py | camelot 失败时 |
> | 填写表单 | PyMuPDF | pdftk | PyMuPDF 不支持的表单类型 |
> | 合并/拆分 | PyMuPDF | pdftk | 批量处理大量文件 |
> | 转换为图片 | pdf2image | PyMuPDF | 需要更高分辨率控制 |
>
> **## 常见陷阱**
>
> 以下情况需要特殊处理：
>
> **扫描件 PDF**
> - 症状：pdftotext 返回空白或乱码
> - 原因：PDF 内容是图片，不是文本
> - 解决：先用 OCR（tesseract）处理，再提取文本
>
> **加密 PDF**
> - 症状：读取时报权限错误
> - 解决：PyMuPDF 的 `open(path, password=xxx)` 或先用 qpdf 解密
>
> **复杂嵌套表格**
> - 症状：camelot 提取结果混乱
> - 解决：考虑 LLM 辅助解析，或转成图片后用视觉模型
>
> **大文件性能**
> - 超过 100 页的 PDF，避免一次性加载全部页面
> - 使用分页处理：`for page in reader.pages[start:end]`
>
> **## 快速参考**

```bash
# 命令行快速提取文本
pdftotext input.pdf -  # 输出到 stdout

# 转换为图片（每页一张）
pdftoppm -jpeg -r 150 input.pdf output_prefix
```

**为什么好**：

| 维度 | 表现 | 价值 |
|------|------|------|
| 不解释基础 | 没有"什么是 PDF" | 节省 token |
| 决策导向 | 决策树告诉你什么情况用什么 | Agent 能做正确选择 |
| 常见陷阱 | 扫描件、加密、复杂表格 | 避免踩坑 |
| 边缘情况 | 大文件性能问题 | 处理特殊场景 |
| 可操作 | 直接给命令，不给教程 | 立即可用 |

---

### 3.3 另一个对比：创意型 Skill

**坏的创意型 Skill**：

```markdown
# 前端设计技能

## 设计原则

1. 保持一致性
2. 注重用户体验
3. 使用合适的颜色
4. 选择易读的字体
5. 做好响应式设计

## 设计流程

Step 1: 理解需求
Step 2: 制作线框图
Step 3: 选择配色方案
Step 4: 编写 HTML 结构
Step 5: 添加 CSS 样式
Step 6: 实现响应式
Step 7: 测试和优化

## 常用工具

- Figma
- Sketch
- Adobe XD
```

问题：全是废话。"保持一致性"、"注重用户体验"——这些 Claude 早就知道。这个 Skill 没有传递任何 Claude 没有的知识。

**好的创意型 Skill**（官方 frontend-design 风格）：

```markdown
---
name: frontend-design
description: 创建独特的、生产级的前端界面。当用户要求构建网页组件、页面、
应用程序、海报、仪表板时使用。生成有创意、有品味的代码和 UI 设计。
---

# 设计思维

在写任何代码之前，先回答这些问题：

**Purpose**：这个界面解决什么问题？谁在用它？
**Tone**：选择一个极端方向——极简主义、最大化混乱、复古未来、有机自然、奢华精致、玩具感、杂志感、粗野主义、装饰艺术...
**Differentiation**：什么让这个设计令人难忘？用户会记住什么？

**关键**：选择一个清晰的概念方向，然后精确执行。大胆的最大化和精致的极简都可以——关键是意图明确，而不是强度。

## 绝对不要做的事

以下是典型的"AI 生成感"设计，必须避免：

- 滥用 Inter、Roboto、Arial 字体
- 紫色渐变配白色背景
- 所有圆角都是 8px
- 千篇一律的卡片布局
- 没有个性的 cookie-cutter 风格

## 应该追求的

- **字体**：选择有个性的字体。把一个独特的展示字体和精致的正文字体搭配。
- **颜色**：承诺一个连贯的审美。主色调配锐利的强调色，胜过胆怯的平均分配。
- **动效**：聚焦高影响力时刻——一个精心编排的页面加载动画，胜过散落的微交互。
- **空间**：意外的布局。不对称。重叠。对角线流动。打破网格的元素。
- **背景**：创造氛围和深度，而不是默认纯色。渐变网格、噪点纹理、几何图案。

## 执行原则

**匹配复杂度和愿景**：
- 最大化设计 → 需要复杂代码、大量动画和效果
- 极简设计 → 需要克制、精确、细致的间距和字体处理

优雅来自于对愿景的良好执行，而不是堆砌效果。
```

**为什么好**：

| 维度 | 表现 |
|------|------|
| 思维框架 | Purpose/Tone/Differentiation 三个问题 |
| 明确反模式 | "绝对不要做的事"清单 |
| 具体方向 | 字体、颜色、动效、空间、背景各有指导 |
| 执行原则 | 复杂度匹配愿景 |
| 不教技术 | 没有解释 CSS，Claude 已经会 |

---

### 3.4 第三个对比：代码审查 Skill

这个例子展示如何把一个日常任务变成高质量 Skill。

**坏的代码审查 Skill**：

```markdown
# 代码审查技能

## 什么是代码审查
代码审查是软件开发过程中，由团队成员对代码变更进行检查和评估的活动。
它可以帮助发现 bug、提高代码质量、分享知识...

## 为什么要做代码审查
1. 发现潜在的 bug
2. 提高代码可读性
3. 促进团队知识共享
4. 确保代码符合规范

## 如何进行代码审查
Step 1: 阅读代码变更
Step 2: 理解代码的目的
Step 3: 检查是否有 bug
Step 4: 检查代码风格
Step 5: 写评论反馈
Step 6: 讨论和修改
```

问题：全是废话。Claude 知道什么是代码审查，知道为什么要做。Step 1-6 也是显而易见的流程。这个 Skill 没有传递任何专家独有的知识。

**好的代码审查 Skill**：

```yaml
---
name: code-review
description: 审查代码质量和正确性。当用户要求 review PR、检查代码、
             找 bug、评估代码质量时使用。
---
```

```markdown
# 审查优先级

不是所有问题都同等重要。按以下顺序审查：

1. **安全漏洞**（必须修复）
   - 注入攻击、权限泄露、敏感数据暴露
2. **逻辑错误**（必须修复）
   - 边界条件、空值处理、并发问题
3. **性能问题**（建议修复）
   - N+1 查询、内存泄漏、不必要的重复计算
4. **可维护性**（可选）
   - 代码风格、命名、注释

# 思维模式

审查每段代码时，问自己：

- **理解**：6 个月后的新人能看懂这段代码吗？
- **定位**：如果这里出 bug，能快速定位问题吗？
- **简化**：有没有更简单的写法实现同样功能？

# 绝对不要做

- 一次提 20 个问题（挑最重要的 3-5 个，其他放在"nit"里）
- 只说"这里有问题"不说怎么改（要给具体建议或代码示例）
- 吹毛求疵（专注真正影响的问题，不要纠结空格和换行）
- 用"我觉得"开头（用"建议"或直接说原因）

# 评论模板

**必须修复**：
> [MUST] 这里存在 SQL 注入风险。用户输入未经转义直接拼接到查询中。
> 建议使用参数化查询：`db.query("SELECT * FROM users WHERE id = ?", [userId])`

**建议修复**：
> [SUGGEST] 这个循环内有 N+1 查询问题，在数据量大时会很慢。
> 建议改用批量查询：`User.find({ id: { $in: userIds } })`

**小问题**：
> [NIT] 变量名 `d` 不够清晰，建议改为 `dateCreated`。
```

**区别总结**：

| 维度 | 坏 Skill | 好 Skill |
|------|----------|----------|
| 概念解释 | 解释什么是代码审查 | 直接跳过 |
| 流程 | Step 1-6 | 无（Claude 已知） |
| 优先级 | 无 | 明确的 4 级优先级 |
| 思维方式 | 无 | 3 个核心问题 |
| 反模式 | 无 | 4 条"绝对不要" |
| 可操作性 | 空泛建议 | 具体评论模板 |

这就是核心公式的体现：`好 Skill = 专家独有的知识 - Claude 已有的知识`。好的代码审查 Skill 传递的是资深工程师的审查直觉和经验，不是代码审查的定义和流程。

---

## 四、5 种 Skill 类型及其赋能

通过分析 17 个官方 Skill，我们识别出 5 种主要设计模式。每种模式有不同的结构、复杂度，以及它赋予 Agent 的能力。

### 类型 1：极简心智型

**代表**：frontend-design（43 行）

**结构特点**：
- 不教技术细节，传递思维方式
- 全部内容自包含在 SKILL.md 中
- 没有 references 目录
- 强调品味、差异化、反模式

**赋能**：

把一个通用的、写出千篇一律 UI 的 Agent，变成一个**有审美品味的设计师 Agent**。

这个 Agent 在写代码之前会先思考：这个界面要解决什么问题？用户是谁？什么能让它令人难忘？它会主动避免"AI 感"设计，追求独特性。

**适用场景**：
- 需要创意和品味的任务
- 差异化来自"怎么想"而非"知道什么"
- 不需要大量领域特定知识

**不需要加载触发机制**——43 行内容一次性加载，无需分层。

---

### 类型 2：工具操作型

**代表**：docx（197 行）、xlsx、pptx、pdf

**结构特点**：
- 决策树快速路由到正确工作流
- MANDATORY 强制加载指令
- 详细的代码示例
- 大量 reference 文档（每个 300-600 行）
- 低自由度，精确步骤

**赋能**：

把一个通用的、可能会把 Word 文档写坏的 Agent，变成一个**能精确操作复杂文件格式的专家 Agent**。

这个 Agent 知道：创建新文档用 docx-js，编辑现有文档用 OOXML 直接操作，处理修订痕迹用 redlining 工作流。它知道每种操作的具体步骤，不会犯破坏文件的错误。

**适用场景**：
- 文件格式操作
- 操作容易出错，需要精确指导
- 需要大量领域特定知识

**需要精心设计的加载触发**——决策树根据任务类型路由，每个工作流开始前强制加载对应文档。

---

### 类型 3：流程导向型

**代表**：mcp-builder（237 行）

**结构特点**：
- 清晰的多阶段工作流（如四阶段）
- 每个阶段有具体的产出和检查点
- reference 按阶段/按选择组织
- 中等自由度

**赋能**：

把一个通用的、可能遗漏关键步骤的 Agent，变成一个**能系统性构建复杂项目的工程师 Agent**。

这个 Agent 知道构建 MCP 服务器要经过：研究规划 → 实现 → 测试 → 评估四个阶段。每个阶段它知道要做什么、产出什么、什么时候可以进入下一阶段。

**适用场景**：
- 复杂的多步骤任务
- 需要阶段性检查点
- 有多种技术选择（如 TypeScript vs Python）

**需要阶段性加载触发**——进入每个阶段时加载对应的 reference 文档。

---

### 类型 4：哲学+执行型

**代表**：canvas-design（130 行）、algorithmic-art

**结构特点**：
- 两步流程：Philosophy（创建理念）→ Express（执行创作）
- 反复强调工艺品质和大师级执行
- 给予创意空间
- reference 是参考示例，非必需

**赋能**：

把一个通用的、输出平庸作品的 Agent，变成一个**有创作哲学的艺术家 Agent**。

这个 Agent 不会直接开始画画。它会先创建一个设计哲学——"Brutalist Joy"或"Chromatic Silence"——然后用这个哲学指导视觉表达。它追求的是"看起来像花了无数小时精心制作"的品质。

**适用场景**：
- 创意生成任务
- 需要独特性和原创性
- 品质比效率更重要

**加载触发可选**——核心工作流自包含在 SKILL.md，reference 只是参考示例。

---

### 类型 5：导航型

**代表**：internal-comms（33 行）

**结构特点**：
- SKILL.md 极简，只是路由器
- 详细内容在 examples/ 子目录中
- 快速识别场景，路由到对应文件

**结构示例**：

```markdown
## How to use this skill

1. **Identify the communication type** from the request
2. **Load the appropriate guideline file**:
   - `examples/3p-updates.md` - 进度/计划/问题更新
   - `examples/company-newsletter.md` - 公司通讯
   - `examples/faq-answers.md` - 常见问题回答
   - `examples/general-comms.md` - 其他类型
3. **Follow the specific instructions** in that file
```

**赋能**：

把一个通用的 Agent，变成一个**能处理多种场景的专业写手 Agent**。

这个 Agent 收到"帮我写周报"时，会识别这是 3P 更新，然后加载对应的指南，按照公司的格式和风格来写。

**适用场景**：
- 有多个明确的子场景
- 每个子场景有独立的详细指南
- 不需要同时加载所有场景

**需要简单路由触发**——识别场景类型，加载对应文件。

---

### 类型选择总结

| 你的任务特点 | 推荐类型 | 行数参考 | 需要加载触发 |
|--------------|----------|----------|--------------|
| 需要品味和创意 | 极简心智型 | 30-50 | 否 |
| 需要独特性和工艺品质 | 哲学+执行型 | 100-150 | 可选 |
| 有多个场景需要分发 | 导航型 | 20-50 | 是（简单） |
| 复杂多步骤项目 | 流程导向型 | 150-300 | 是 |
| 精确操作特定格式 | 工具操作型 | 200-500 | 是（精心） |

---

## 五、加载触发机制：最被忽视的设计

这一节只对**有 reference 目录的中等/复杂 Skill** 重要。如果你的 Skill 是简单的单文件（如 frontend-design），可以跳过。

### 5.1 问题

Skill 设计的核心理念是**按需加载上下文**——把详细知识存在 reference 文件里，需要时才加载，保持 context window 精简。

但现实是：Agent 经常不读该读的文档，或者读太多不该读的文档。

### 5.2 解决方案

**技巧 1：MANDATORY 语法**

在工作流步骤中嵌入强制加载指令：

```markdown
### 创建新文档

**MANDATORY - READ ENTIRE FILE**：在继续之前，你必须完整阅读
[`docx-js.md`](docx-js.md)（约 500 行）。
**绝对不要设置任何行数限制。**
```

关键词："MANDATORY"、"必须"、"绝对不要"——不留模糊空间。

**技巧 2：条件触发路由表**

```markdown
| 任务类型 | 必须加载 | 不要加载 |
|----------|----------|----------|
| 创建新文档 | `docx-js.md` | `ooxml.md`, `redlining.md` |
| 简单编辑 | `ooxml.md` | `docx-js.md`, `redlining.md` |
| 修订痕迹 | `redlining.md` | `docx-js.md` |
```

同时告诉 Agent 该读什么、不该读什么——解决"不读"和"读太多"两个问题。

**技巧 3：场景检测**

```markdown
**场景 A：新项目**
- 用户说："从头构建 X"、"创建一个新的..."
- **必须加载**：`references/greenfield.md`

**场景 B：修复 Bug**
- 用户说："X 坏了"、"修复这个 bug"
- **必须加载**：`references/bugfix.md`
```

基于用户输入的关键词自动路由。

---

## 六、设计检查清单

写完一个 Skill，过一遍这个清单：

```
基础规范
[ ] 有 YAML frontmatter，包含 name 和 description
[ ] description 包含"做什么"和"什么时候用"
[ ] SKILL.md < 500 行

内容质量
[ ] 没有解释 Claude 已知的基础概念
[ ] 没有机械的 Step 1, 2, 3
[ ] 有明确的反模式清单（NEVER list）
[ ] 有决策树或选择指导（如果有多种路径）
[ ] 有常见陷阱和边缘情况

加载机制（仅有 reference 的 Skill）
[ ] 每个 reference 有明确的加载触发条件
[ ] 触发条件嵌入在工作流步骤中
[ ] 有防止过度加载的机制

自由度
[ ] 创意任务 → 高自由度（原则而非步骤）
[ ] 脆弱操作 → 低自由度（精确脚本）
```

---

## 七、评估你的 Skill

怎么知道你写的 Skill 好不好？

我们在 [shareAI-skills](https://github.com/shareAI-lab/shareAI-skills) 仓库创建了一个 **skill-judge** Skill，专门用于多维度评估 Agent Skill 的设计质量。

### 评估维度

| 维度 | 分值 | 检查内容 |
|------|------|----------|
| 规范合规 | 20 | frontmatter 格式、description 完整性 |
| 渐进式披露 | 20 | 三层加载机制、MANDATORY 触发器 |
| 上下文效率 | 15 | 不解释基础概念、不过度冗长 |
| 自由度校准 | 15 | 创意任务高自由度、脆弱操作低自由度 |
| 模式识别 | 15 | 是否遵循 5 种官方模式之一 |
| 实用可用性 | 15 | 决策树、代码示例、边缘情况覆盖 |

### 评分标准

- **90-100**：优秀，生产就绪
- **80-89**：良好，需要小改进
- **70-79**：合格，需要改进
- **< 70**：需要重新设计

### 使用方法

把你的 SKILL.md 内容发给加载了 skill-judge 的 Agent，它会给你一份详细的评估报告，包括：
- 各维度得分
- 具体问题指出
- 改进建议

仓库地址：**https://github.com/shareAI-lab/shareAI-skills**

---

## 结语

好的 Agent Skill 不是教程。

**好的 Agent Skill 是专家知识的外化形式。**

它把一个领域专家的思维方式、决策原则、反模式直觉、边缘情况经验，压缩成一个可加载的 Markdown 文件。

当 Agent 加载这个文件时，它不是在"学习操作步骤"——它是在**继承一种专家思维**。

写 Skill 之前，问自己：
- 这个领域的顶级专家是如何思考的？
- 他们做决策的核心原则是什么？
- 他们踩过什么坑？
- 他们绝对不会做什么？
- 什么知识是模型不知道但必须知道的？

想清楚这些，再动手写。

记住那个核心公式：

```
好 Skill = 专家独有的知识 - Claude 已有的知识
```

**好 Skill = 高压缩比 + 高信息密度。**
**垃圾 Skill = 压缩了 Claude 已经知道的东西。**

---

**工具让模型能做事。技能让模型知道怎么做。**

这就是 Agent Skill 的全部奥秘——把专家大脑压缩成可加载的 Markdown 文件，让通用模型在需要时变成领域专家。不需要训练，不需要微调，编辑文本，即时生效。

---

**相关链接**：
- shareAI-skills 仓库：https://github.com/shareAI-lab/shareAI-skills
- skill-judge 评估工具：https://github.com/shareAI-lab/shareAI-skills/tree/main/skills/skill-judge
- Kode（开源 Claude Code）：https://github.com/shareAI-lab/Kode
