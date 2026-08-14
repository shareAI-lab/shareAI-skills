# Scenario: Refactoring

Code works but needs improvement. Change structure without changing behavior.

---

## The Safety Rule

**NEVER refactor without tests.** If tests don't exist, write them first.

---

## Workflow

```
UNDERSTAND CURRENT -> ENSURE TESTS -> PLAN SAFE TRANSFORMS -> EXECUTE INCREMENTALLY
```

---

## Step 1: Understand Current State

```
"Before refactoring, let me understand the current state:

**What exists**: [Summary of current code]
**What's problematic**: [Specific issues]
**What works fine**: [Don't touch these]

What specifically do you want improved?
- Readability?
- Performance?
- Testability?
- Maintainability?
- All of the above?"
```

---

## Step 2: Ensure Test Coverage

```
"Test coverage status:

**Current coverage**: [X%]
**Tests exist for**: [What's covered]
**Need tests for**: [What's not covered]

Before refactoring, I'll add tests for [gaps]."
```

**Critical**: Each test must pass BEFORE and AFTER the refactor.

---

## Step 3: Plan Safe Transformations

```
"Refactoring plan:

## Step 1: [Safe transformation]
- Current: [What exists]
- After: [What it becomes]
- Risk: Low - [Why safe]

## Step 2: [Safe transformation]
...

**Important**: Each step will be verified before the next.

Proceed with this plan?"
```

---

## Step 4: Incremental Execution

For each step:
1. Run tests (should pass)
2. Make transformation
3. Run tests (should still pass)
4. Commit
5. Repeat

```
"Step [N] complete:

**Changed**: [What changed]
**Tests**: All pass
**Behavior**: Unchanged

Ready for next step?"
```

---

## Safe Refactoring Patterns

| Pattern | When | Risk Level |
|---------|------|------------|
| Rename | Unclear naming | Very Low |
| Extract function | Code duplication | Low |
| Extract variable | Complex expression | Very Low |
| Inline | Over-abstraction | Low |
| Move | Wrong location | Low |
| Change signature | API improvement | Medium |

---

## Refactoring Checklist

- [ ] Tests exist and pass before starting
- [ ] Each step independently verifiable
- [ ] Behavior unchanged after each step
- [ ] No side effects introduced
- [ ] Final tests all pass
- [ ] Code quality improved (measurable)
