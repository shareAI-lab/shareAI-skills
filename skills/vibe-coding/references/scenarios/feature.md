# Scenario: Feature Addition

Adding new functionality to an existing codebase.

---

## Workflow

```
UNDERSTAND EXISTING -> DESIGN INTEGRATION -> PLAN -> IMPLEMENT -> VERIFY
```

---

## Step 1: Understand Existing Code

```
"Before designing the feature, I need to understand the existing system:

1. Show me the files most relevant to where this feature will live
2. What's the current architecture pattern?
3. Are there similar features I should reference?
4. Any constraints from existing code I should know?

Let me read the relevant code first."
```

**Key**: Read and understand all related existing code before proposing changes.

---

## Step 2: Design Integration

```
"After reading the code, here's how I'll integrate the feature:

## Integration Points
| Existing Component | Change Needed | Impact |
|--------------------|---------------|--------|

## New Components
| Component | Purpose | Touches |

## API Changes (if any)
[Breaking changes? Additions?]

## Database Changes (if any)
[Migrations needed?]

## Backward Compatibility
[How existing functionality is preserved]

Questions before I create the task plan?"
```

---

## Step 3: Implement

Same as greenfield Phase 4, with extra attention to:
- Not breaking existing functionality
- Following existing patterns
- Adding tests for both new AND affected existing code

---

## Integration Checklist

- [ ] Existing patterns followed
- [ ] No breaking changes (or explicitly approved)
- [ ] Related tests updated
- [ ] Documentation updated
- [ ] Backward compatibility verified
