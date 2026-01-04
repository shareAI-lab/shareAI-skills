# How to Create Great Agent Skills

This guide distills lessons from analyzing 17 official Anthropic skills and the skill-creator specification. It covers what makes a skill good or bad, why, and how to design effective skills.

## What is a Skill?

### The Common Misconception

Most people think skills are about **teaching AI how to do something**.

This is wrong.

Claude already knows how to write code, debug, design systems, and work with PDFs. You don't need to teach it these things.

### Skills are Knowledge Externalization

Traditional AI knowledge is locked in model weights:

```
Traditional approach:
Collect data -> GPU cluster -> Parameter training -> Deploy new version
Cost: $10,000 - $1,000,000+
Timeline: Weeks to months
```

Skills change this:

```
Skill approach:
Edit SKILL.md -> Save -> Takes effect on next trigger
Cost: $0
Timeline: Instant
```

Think of it as a hot-swappable LoRA adapter that requires no training. You edit a Markdown file in natural language, and the model's behavior changes.

**This is a paradigm shift from "training AI" to "educating AI."**

### Tool vs Skill

| Concept | Essence | Function | Examples |
|---------|---------|----------|----------|
| **Tool** | What model **can do** | Execute actions | bash, read_file, write_file |
| **Skill** | What model **knows how to do** | Guide decisions | PDF processing, frontend design |

Tools define capability boundaries. Skills inject knowledge.

**Core Formula:**

```
Generic Agent + Excellent Skill = Domain Expert Agent
```

Or:

```
Agent Capability Ceiling = Model Capability + Skill Quality
```

---

## 6 Judgment Standards

### Standard 1: Token Efficiency

**Source:** Anthropic skill-creator specification

> **Concise is Key.** The context window is a public good. Skills share the context window with everything else Claude needs.

> **Default assumption: Claude is already very smart.** Only add context Claude doesn't already have.

**The Core Formula:**

```
Good Skill = Expert-only Knowledge - What Claude Already Knows
```

For every paragraph, ask:
1. Does Claude really not know this?
2. Would removing it affect task completion?
3. Is this 100 tokens worth the value?

If Claude already knows it or it doesn't matter, delete it.

---

### Standard 2: Mental Models vs Mechanical Steps

**Source:** Analysis of frontend-design and canvas-design skills

The official frontend-design skill is only 43 lines, yet highly effective:

```markdown
Before coding, commit to a BOLD aesthetic direction:
- **Purpose**: What problem does this interface solve?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos...
- **Differentiation**: What makes this UNFORGETTABLE?

NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto)...
```

It doesn't teach CSS. It activates **designer thinking** - asking key questions before writing code.

| Dimension | Mediocre Skill | Excellent Skill |
|-----------|---------------|-----------------|
| Content | Step 1, Step 2, Step 3 | Thinking frameworks, decision principles |
| Assumption | Agent can't do it | Agent can do it but doesn't know how to think |
| Effect | Agent follows script | Agent thinks like an expert |

---

### Standard 3: Anti-Pattern Lists

**Source:** Common pattern across official skills

Almost all excellent official skills include explicit "NEVER" lists:

```markdown
NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial),
cliched color schemes (particularly purple gradients on white backgrounds)...
```

Expert knowledge is half "what to do" and half "what never to do." A senior designer instinctively frowns at purple gradients on white - "too AI-looking." Claude hasn't developed this instinct.

Good skills explicitly state what not to do. This is more valuable than "what to do" because it sets quality floors.

---

### Standard 4: Description Trigger Mechanism

**Source:** Skill-creator specification

> This is the primary triggering mechanism for your skill. Include both what the Skill does and specific triggers/contexts for when to use it.

Skills load in three layers:

```
Layer 1: Metadata (always in memory)
         Only name + description
         ~100 tokens/skill

Layer 2: SKILL.md Body (loaded after trigger)
         Detailed guides, code examples
         < 5000 tokens

Layer 3: Resources (loaded on demand)
         scripts/, references/, assets/
         Unlimited
```

**Good description:**

```yaml
description: "Comprehensive document creation, editing, and analysis with support
for tracked changes, comments, formatting preservation, and text extraction.
When Claude needs to work with professional documents (.docx files) for:
(1) Creating new documents, (2) Modifying content, (3) Working with tracked changes..."
```

**Bad description:**

```yaml
description: "Handles document-related functions"
```

Too vague - agent doesn't know when to use it.

---

### Standard 5: Freedom Calibration

**Source:** Analysis of docx (low freedom) vs frontend-design (high freedom)

> Match the level of specificity to the task's fragility and variability:
>
> **High freedom**: When multiple approaches are valid, decisions depend on context.
> **Low freedom**: When operations are fragile and error-prone, consistency is critical.

| Task Type | Freedom Level | Reason | Example Skill |
|-----------|--------------|--------|---------------|
| Creative design | High | Multiple valid approaches | frontend-design |
| Code review | Medium | Has principles but needs judgment | code-review |
| File format ops | Low | Fragile operations, consistency critical | docx, xlsx |

Ask: What's the error tolerance? If agent makes one wrong step, what's the consequence?

High tolerance -> Give principles, not steps
Low tolerance -> Give scripts, few parameters

---

### Standard 6: Loading Trigger Design

**Source:** Practical experience

Many skills have detailed reference docs, but agents don't read them. Or read too much.

**Solution: MANDATORY syntax**

```markdown
### Creating New Document

**MANDATORY - READ ENTIRE FILE**: Before proceeding, you MUST read
[`docx-js.md`](docx-js.md) completely from start to finish.
**NEVER set any range limits when reading this file.**
```

"MANDATORY", "MUST", "NEVER" - these aren't decoration. They're critical signals.

**Solution: Conditional routing table**

```markdown
| Task Type | MUST Load | Do NOT Load |
|-----------|-----------|-------------|
| Create new | `docx-js.md` | `ooxml.md`, `redlining.md` |
| Simple edit | `ooxml.md` | `docx-js.md`, `redlining.md` |
```

Tells agent both what to read AND what not to read.

---

## Good vs Bad Skills: Examples

### Bad Skill Example

```markdown
# PDF Processing Skill

## What is PDF
PDF (Portable Document Format) is a file format developed by Adobe in 1993...

## How to Read PDF
Step 1: Install PyPDF2 library
Step 2: Import library
Step 3: Open PDF file
Step 4: Read page content
```

**Problems:**
- Explains basic concepts (Claude already knows)
- Mechanical steps (Claude already writes code)
- No decision guidance
- No anti-patterns
- No edge cases

### Good Skill Example

```yaml
---
name: pdf-processing
description: Process PDF files. Use when user needs to extract text, tables,
             fill forms, merge/split PDFs, or convert to images.
---
```

```markdown
# PDF Processing Decision Tree

| Task | Primary Tool | Fallback | When to Use Fallback |
|------|-------------|----------|---------------------|
| Extract text | pdftotext | PyMuPDF | Need layout preservation |
| Extract tables | camelot-py | tabula-py | When camelot fails |
| Fill forms | PyMuPDF | pdftk | Unsupported form types |

## Common Pitfalls

**Scanned PDFs**
- Symptom: pdftotext returns blank or garbage
- Cause: PDF content is images, not text
- Solution: OCR with tesseract first

**Encrypted PDFs**
- Symptom: Permission error on read
- Solution: PyMuPDF's `open(path, password=xxx)` or decrypt with qpdf first
```

**Why it's good:**
- No basic explanations
- Decision-oriented routing
- Common pitfalls documented
- Edge cases covered
- Immediately actionable

---

## 5 Skill Types

### Type 1: Minimal Mindset

**Example:** frontend-design (43 lines)

- Transfers thinking patterns, not technical details
- Self-contained in SKILL.md
- No references directory
- Emphasizes taste and anti-patterns

**Empowerment:** Transforms generic agent into **designer agent with aesthetic taste**.

**Use when:** Creative tasks where differentiation comes from "how to think"

---

### Type 2: Tool Operation

**Example:** docx (197 lines), xlsx, pptx, pdf

- Decision tree routing to correct workflow
- MANDATORY loading directives
- Detailed code examples
- Large reference docs (300-600 lines each)
- Low freedom, precise steps

**Empowerment:** Transforms generic agent into **expert at precise file format operations**.

**Use when:** File format operations that are error-prone

---

### Type 3: Process-Oriented

**Example:** mcp-builder (237 lines)

- Clear multi-phase workflow
- Each phase has outputs and checkpoints
- References organized by phase
- Medium freedom

**Empowerment:** Transforms generic agent into **systematic project builder**.

**Use when:** Complex multi-step tasks with checkpoints

---

### Type 4: Philosophy + Execution

**Example:** canvas-design (130 lines), algorithmic-art

- Two-step flow: Philosophy -> Express
- Emphasizes craft quality
- Creative space
- References are optional examples

**Empowerment:** Transforms generic agent into **artist with creative philosophy**.

**Use when:** Creative generation requiring originality

---

### Type 5: Navigation

**Example:** internal-comms (33 lines)

- SKILL.md is just a router
- Detailed content in examples/ subdirectory
- Quick scenario identification and routing

**Empowerment:** Transforms generic agent into **multi-scenario specialist**.

**Use when:** Multiple distinct sub-scenarios with independent guidelines

---

### Type Selection Summary

| Task Characteristics | Recommended Type | Line Count | Needs Loading Triggers |
|---------------------|------------------|------------|----------------------|
| Needs taste/creativity | Minimal Mindset | 30-50 | No |
| Needs originality/craft | Philosophy+Execution | 100-150 | Optional |
| Multiple scenarios | Navigation | 20-50 | Yes (simple) |
| Complex multi-step | Process-Oriented | 150-300 | Yes |
| Precise format operations | Tool Operation | 200-500 | Yes (careful) |

---

## Design Checklist

```
Basic Requirements
[ ] Has YAML frontmatter with name and description
[ ] Description includes "what it does" and "when to use"
[ ] SKILL.md < 500 lines

Content Quality
[ ] Doesn't explain concepts Claude already knows
[ ] No mechanical Step 1, 2, 3
[ ] Has explicit anti-pattern list (NEVER list)
[ ] Has decision tree or selection guidance (if multiple paths)
[ ] Has common pitfalls and edge cases

Loading Mechanism (only for skills with references)
[ ] Each reference has clear loading trigger conditions
[ ] Triggers embedded in workflow steps
[ ] Has mechanism to prevent over-loading

Freedom Calibration
[ ] Creative tasks -> High freedom (principles not steps)
[ ] Fragile operations -> Low freedom (precise scripts)
```

---

## Evaluate Your Skill

Use the [skill-judge](../skills/skill-judge/) skill to evaluate your skill across 6 dimensions:

| Dimension | Points | Checks |
|-----------|--------|--------|
| Spec Compliance | 20 | Frontmatter, description completeness |
| Progressive Disclosure | 20 | Three-layer loading, MANDATORY triggers |
| Context Efficiency | 15 | No basic explanations, not verbose |
| Freedom Calibration | 15 | Creative=high freedom, fragile=low freedom |
| Pattern Recognition | 15 | Follows one of 5 official patterns |
| Practical Usability | 15 | Decision trees, code examples, edge cases |

**Scoring:**
- 90-100: Excellent, production-ready
- 80-89: Good, minor improvements needed
- 70-79: Acceptable, needs improvement
- <70: Needs redesign

---

## Summary

Good skills are not tutorials.

**Good skills are externalized expert knowledge.**

They compress an expert's thinking patterns, decision principles, anti-pattern instincts, and edge case experience into a loadable Markdown file.

When an agent loads this file, it's not "learning steps" - it's **inheriting expert thinking**.

Before writing a skill, ask:
- How do top experts in this domain think?
- What are their core decision principles?
- What pitfalls have they encountered?
- What do they absolutely never do?
- What knowledge does the model lack but need?

Remember:

```
Good Skill = Expert-only Knowledge - What Claude Already Knows
```

**Tools let models do things. Skills let models know how.**

---

**Related:**
- [shareAI-skills repository](https://github.com/shareAI-lab/shareAI-skills)
- [skill-judge evaluation tool](../skills/skill-judge/)
- [Kode CLI](https://github.com/shareAI-lab/Kode)
