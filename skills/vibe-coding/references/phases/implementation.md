# Phase: Implementation

Systematic execution with test-first discipline.

---

## Task Granularity Standard

**The 2-5 Minute Rule**: Every task completable in 2-5 focused minutes.

| Estimate | Action |
|----------|--------|
| < 2 min | Combine with related work |
| 2-5 min | Perfect granularity |
| 5-10 min | Break into 2-3 subtasks |
| > 10 min | Mini-project, not a task |

---

## Task Template

```
## Task [N]: [Verb + Noun]

**Goal**: [Single sentence]
**Files**: [Exact paths to create/modify]
**Depends On**: [Previous task numbers, or "None"]

**Steps**:
1. [Specific action]
2. [Specific action]
3. [Specific action]

**Verification**:
```bash
[Exact command]
```
**Expected**: [What success looks like]

**NOT Doing**: [Explicit scope boundary]
```

---

## Implementation Protocol

For EACH task:

```
**Starting Task [N]: [Title]**

**Test First** (when applicable):
```typescript
describe('feature', () => {
  it('should do X', () => {
    expect(feature()).toBe(expected);
  });
});
```

**Implementation**:
[Show the actual code changes]

**Verification**:
```bash
[Exact command run]
```
**Result**: [Actual output]

**Task [N] Complete.**
- Tests: [Pass/Fail]
- Build: [Pass/Fail]
- Changes: [List of files]

Ready for next task?
```

---

## Task Plan Example

```
## Implementation Plan

### Phase A: Foundation (Tasks 1-3)

**Task 1: Initialize project structure**
Goal: Create project skeleton with correct dependencies
Files: package.json, tsconfig.json, src/index.ts
Depends On: None

Steps:
1. npm init -y
2. Install dependencies
3. Create tsconfig.json with strict mode
4. Create src/index.ts with basic server

Verification:
```bash
npm run build && npm start
```
Expected: Server starts on port 3000

NOT Doing: Database, auth, actual routes

---

**Task 2: Add database connection**
[...]

### Phase B: Core Features (Tasks 4-8)
[...]

### Phase C: Polish (Tasks 9-10)
[...]

---
Human approves? Then I'll begin.
```

---

## Test-First Discipline

For non-trivial code:

1. **Write failing test FIRST**
2. **Implement minimum to pass**
3. **Refactor while green**
4. **Commit**

Exceptions require EXPLICIT human approval:
- "Skip tests for this prototype" -> proceed without
- Otherwise -> tests mandatory

---

## When Blocked

```
**BLOCKED on Task [N]: [Title]**

**Issue**: [What's preventing progress]

**What I Tried**:
1. [Approach 1] - [Why didn't work]
2. [Approach 2] - [Why didn't work]

**Options**:
| Option | Pros | Cons | Recommend? |
|--------|------|------|------------|
| [A] | [Benefits] | [Drawbacks] | |
| [B] | [Benefits] | [Drawbacks] | <- This one |

**Recommendation**: [Option] because [reasoning]

**Need from you**: [Specific decision needed]
```

---

## Implementation Checklist

### Per-Task
- [ ] Test written first (when applicable)
- [ ] Implementation complete
- [ ] Verification passed
- [ ] Human confirmed

### Per-Phase
- [ ] All tasks in phase complete
- [ ] Integration tested
- [ ] No regressions

### Before Ship
- [ ] All tasks complete
- [ ] All tests pass
- [ ] Quality checklist passed
