# Scenario: Greenfield Project

Building something completely new from scratch.

---

## Full Workflow

```
DISCOVER (5-15 min) -> DESIGN (10-20 min) -> PLAN (5-10 min) -> IMPLEMENT -> SHIP
```

---

## Phase 1: Discovery

```
"Before building, help me understand your vision:

1. **The Problem**: What pain point are we solving? Who has this problem?
2. **The User**: Who specifically uses this? Role? Technical level?
3. **Success**: If this works perfectly, what changes? How to measure?
4. **Scope**: What's the minimum for v1? Must-have vs nice-to-have?
5. **Constraints**: Tech stack? Existing systems? Timeline?

Let's start with 1 and 3 - they reveal the core."
```

**Output**: Discovery Summary (see phases/discovery.md)

---

## Phase 2: Design

```
"Based on discovery, here's my proposed approach:

## Architecture Overview
[ASCII diagram]

## Technology Decisions
| Area | Choice | Why | Trade-off |
|------|--------|-----|-----------|

## What I'm NOT Building (and why)
- ...

## Data Model
[Entity relationships]

## Key APIs/Interfaces
[Main contracts]

## Questions Before Proceeding
1. ...

If approved, I'll create the implementation plan."
```

**Output**: Technical design document

---

## Phase 3: Plan

```
## Implementation Plan

### Phase A: Foundation (Tasks 1-N)
[Tasks with 2-5 min granularity]

### Phase B: Core Features (Tasks N-M)
[Tasks]

### Phase C: Polish (Tasks M-End)
[Tasks]

Approve this plan? Then I'll start implementation.
```

**Output**: Task list with verification steps

---

## Phase 4: Implement

For each task:
1. State what you're building
2. Write test first (when applicable)
3. Implement
4. Show verification
5. Confirm before next task

---

## Phase 5: Ship

Run through quality checklist (quality/checklists.md), get final approval.
