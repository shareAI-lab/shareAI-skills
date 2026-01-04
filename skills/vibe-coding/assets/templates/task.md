# Task Specification Template

Use this template when delegating implementation tasks.

---

## Task: [Verb + Object]

**ID**: TASK-XXX
**Status**: Not Started | In Progress | Blocked | Complete
**Assignee**: [AI Agent / Human]
**Estimated Effort**: [Small/Medium/Large]

---

## Goal

[Single sentence: What this task accomplishes]

---

## Context

**Background**:
[Why this task exists, what led to it]

**Related Work**:
- [Related task or document]
- [Dependency]

**Current State**:
[What exists now that this task builds on]

---

## Requirements

### Functional Requirements

1. [Specific, testable requirement]
2. [Specific, testable requirement]
3. [Specific, testable requirement]

### Technical Requirements

- [Technical constraint or requirement]
- [Technical constraint or requirement]

---

## Constraints

### MUST

- [Non-negotiable requirement]
- [Non-negotiable requirement]

### MUST NOT

- [Explicit prohibition]
- [Explicit prohibition]

### SHOULD

- [Preference if possible]
- [Preference if possible]

---

## Acceptance Criteria

- [ ] [Observable, testable criterion]
- [ ] [Observable, testable criterion]
- [ ] [Observable, testable criterion]
- [ ] Tests pass
- [ ] No regressions

---

## Implementation Guidance

### Files to Touch

| File | Action | Description |
|------|--------|-------------|
| [path/file.ts] | Create/Modify | [What to do] |
| [path/file.ts] | Create/Modify | [What to do] |

### Suggested Approach

1. [Step 1]
2. [Step 2]
3. [Step 3]

### Patterns to Follow

- [Reference existing pattern in codebase]
- [Reference documentation]

### Edge Cases to Handle

- [Edge case 1]: [Expected behavior]
- [Edge case 2]: [Expected behavior]

---

## NOT Doing

- [Explicit exclusion 1]
- [Explicit exclusion 2]
- [Future enhancement - not now]

---

## Verification

### How to Test

```sh
# Command to run tests
npm test path/to/test

# Manual verification
curl -X POST /api/endpoint -d '{"data": "test"}'
```

### Expected Outcome

[What success looks like]

---

## Dependencies

### Blocked By

- [ ] [Task that must complete first]

### Blocks

- [ ] [Task waiting on this one]

---

## Notes

[Additional context, gotchas, or reminders]

---

## Completion Checklist

- [ ] Code implemented
- [ ] Tests written
- [ ] Tests pass
- [ ] No regressions
- [ ] Code reviewed (if applicable)
- [ ] Documentation updated (if applicable)
- [ ] Acceptance criteria met
