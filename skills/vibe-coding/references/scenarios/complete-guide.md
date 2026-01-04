# Scenario Workflows: Complete Guide

All development scenarios with detailed workflows.

---

## Scenario Detection Matrix

| Human Says | Scenario | Jump To |
|------------|----------|---------|
| "Build X from scratch" | Greenfield | [Greenfield](#greenfield-new-project) |
| "I want to create a..." | Greenfield | [Greenfield](#greenfield-new-project) |
| "Add X to Y" | Feature Addition | [Feature](#feature-addition) |
| "Implement X in the existing..." | Feature Addition | [Feature](#feature-addition) |
| "X is broken" | Bug Fix | [Bug Fix](#bug-fix) |
| "When I do X, Y happens" | Bug Fix | [Bug Fix](#bug-fix) |
| "X is too slow" | Optimization | [Optimization](#performance-optimization) |
| "Make X faster" | Optimization | [Optimization](#performance-optimization) |
| "Clean up X" | Refactoring | [Refactoring](#refactoring) |
| "Improve code quality" | Refactoring | [Refactoring](#refactoring) |
| "Review this code" | Code Review | [Code Review](#code-review) |
| "Check this PR" | Code Review | [Code Review](#code-review) |
| "Migrate from X to Y" | Migration | [Migration](#migration) |
| "Upgrade X" | Migration | [Migration](#migration) |
| "Production is broken!" | Emergency | [Emergency Hotfix](#emergency-hotfix) |

---

## Greenfield (New Project)

**Use when**: Building something completely new from scratch.

### Phase 1: Discovery (5-15 min)

```
"Before I start building, I need to understand your vision:

1. **The Problem**: What pain point are we solving? Who has this problem?

2. **The User**: Who specifically will use this?
   - Role/job title?
   - Technical level?
   - Context of use?

3. **Success**: If this works perfectly, what changes?
   - What can they do that they couldn't before?
   - How will we measure success?

4. **Scope**: What's the minimum for v1?
   - Must have?
   - Nice to have (but can wait)?
   - Explicitly out of scope?

5. **Constraints**:
   - Tech stack requirements?
   - Existing systems to integrate?
   - Timeline/budget constraints?

Let's start with 1 and 3 - they reveal the core."
```

### Phase 2: Design (10-20 min)

```
"Based on our discovery, here's my proposed approach:

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

If this design is approved, I'll create the implementation plan."
```

### Phase 3: Plan (5-10 min)

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

### Phase 4: Implement

For each task:
1. State what you're building
2. Write test first (when applicable)
3. Implement
4. Show verification
5. Confirm before next task

### Phase 5: Ship

Run through pre-ship checklist, get final approval.

---

## Feature Addition

**Use when**: Adding new functionality to an existing codebase.

### Step 1: Understand Existing Code

```
"Before designing the feature, I need to understand the existing system:

1. **Codebase Structure**
   - Show me the root files (package.json, key configs)
   - What's the entry point?
   - What patterns are established?

2. **Integration Points**
   - Where will this feature attach?
   - What existing components does it touch?
   - Are there similar features I should reference?

3. **Constraints**
   - Tech debt or known issues?
   - Testing setup?
   - Performance requirements?

Let me read the relevant code first."
```

### Step 2: Design Integration

```
"After reading the code, here's how I'll integrate the feature:

## Integration Points
| Existing Component | Change Needed | Impact |
|--------------------|---------------|--------|

## New Components
| Component | Purpose | Touches |
|-----------|---------|---------|

## API Changes (if any)
[Breaking changes? Additions?]

## Database Changes (if any)
[Migrations needed?]

## Backward Compatibility
[How existing functionality is preserved]

Questions before I create the task plan?"
```

### Step 3: Implement

Same as greenfield Phase 4, but with extra attention to:
- Not breaking existing functionality
- Following existing patterns
- Adding tests for both new and affected existing code

---

## Bug Fix

**Use when**: Something isn't working correctly.

### RAPID Method

**R - Reproduce**
```
"Let me reproduce the bug first:

**Steps to Reproduce**:
1. [Step]
2. [Step]
3. [Step]

**Expected**: [What should happen]
**Actual**: [What happens]

Can you confirm these steps reproduce it consistently?"
```

**A - Analyze**
```
"Reproducing now...

**Reproduction Confirmed**: [Yes/No]
**Error Message**: [If any]
**Relevant Logs**: [If any]

Analyzing the code path..."
```

**P - Pinpoint**
```
"Found the issue:

**Root Cause**: [Exact problem]
**Location**: [File:line]
**Why It Happens**: [Explanation]

The bug occurs because [detailed explanation]."
```

**I - Implement**
```
"Proposed fix:

**Change**: [What I'll change]
**Why This Fixes It**: [Explanation]
**Risk**: [What could go wrong]

Implementing with regression test..."
```

**D - Deploy**
```
"Fix complete:

**Test Added**: [Test that fails without fix, passes with]
**Verification**:
```bash
[Command]
```
**Result**: [Output showing fix works]

**Regression Check**: [Confirming nothing else broke]

Ready to commit?"
```

---

## Performance Optimization

**Use when**: Something is too slow.

### Step 1: Profile First (ALWAYS)

```
"Before optimizing, I need to find the actual bottleneck:

**Current Performance**: [How slow?]
**Target Performance**: [How fast should it be?]

Let me profile to find where time is spent..."
```

### Step 2: Identify Bottleneck

```
"Profiling results:

| Area | Time % | Details |
|------|--------|---------|

**Actual Bottleneck**: [What's really slow]
**NOT the problem**: [What looked suspicious but isn't]

The [X] takes [Y]ms which is [Z]% of total time."
```

### Step 3: Propose Optimization

```
"Proposed optimization:

**Target**: [What we're optimizing]
**Approach**: [How]
**Expected Improvement**: [Quantified]
**Trade-off**: [What we give up]

Alternative approaches considered:
| Approach | Improvement | Trade-off | Why Not |
|----------|-------------|-----------|---------|

Proceed with recommended approach?"
```

### Step 4: Implement with Benchmarks

```
"Optimization complete:

**Before**: [Benchmark results]
**After**: [Benchmark results]
**Improvement**: [X% faster / Y ms saved]

Verification:
```bash
[Benchmark command]
```

**Regression Check**: [Confirming correctness unchanged]"
```

---

## Refactoring

**Use when**: Code works but needs improvement.

### Step 1: Understand Current State

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

### Step 2: Ensure Test Coverage

```
"Test coverage status:

**Current coverage**: [X%]
**Tests exist for**: [What's covered]
**Need tests for**: [What's not covered]

Before refactoring, I'll add tests for the gaps."
```

### Step 3: Plan Safe Transformations

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

### Step 3: Incremental Execution

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

## Code Review

**Use when**: Reviewing code for quality, security, or correctness.

### Review Protocol

```
"Reviewing the code now. I'll check:

1. **Correctness**: Does it do what it should?
2. **Security**: Any vulnerabilities?
3. **Performance**: Any obvious issues?
4. **Maintainability**: Is it readable and maintainable?
5. **Tests**: Are they adequate?

Reading..."
```

### Review Output Format

```
## Code Review: [Scope]

### Critical Issues (Must Fix)
| Issue | Location | Why Critical | Suggested Fix |
|-------|----------|--------------|---------------|

### Important Issues (Should Fix)
| Issue | Location | Impact | Suggested Fix |
|-------|----------|--------|---------------|

### Minor Issues (Nice to Fix)
| Issue | Location | Suggestion |
|-------|----------|------------|

### Positive Observations
- [What's done well]
- [Good patterns followed]

### Summary
**Recommendation**: [Approve / Request Changes / Block]
**Overall Quality**: [Assessment]
**Priority Fix**: [Most important thing to address]
```

---

## Migration

**Use when**: Moving from one technology/version to another.

### Step 1: Assess Current State

```
"Before planning the migration:

**Current**: [What exists now]
**Target**: [Where we're going]

Let me assess:
1. What needs to change?
2. What can stay the same?
3. What are the breaking changes?
4. What's the rollback plan?"
```

### Step 2: Migration Plan

```
## Migration Plan

### Phase 1: Preparation
- [ ] Add compatibility layer
- [ ] Write migration tests
- [ ] Document rollback procedure

### Phase 2: Gradual Migration
- [ ] Migrate component A
- [ ] Verify
- [ ] Migrate component B
- [ ] Verify
- [ ] ...

### Phase 3: Cleanup
- [ ] Remove old code
- [ ] Remove compatibility layer
- [ ] Update documentation

### Rollback Plan
If [failure condition]:
1. [Rollback step]
2. [Rollback step]

### Risk Assessment
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|

Approve this plan?
```

### Step 3: Execute with Checkpoints

Each migration step:
1. Make change
2. Run tests
3. Verify in staging (if applicable)
4. Confirm before continuing

---

## Emergency Hotfix

**Use when**: Critical production issue needs immediate fix.

### Expedited Protocol

```
"**HOTFIX MODE**

Understanding the issue:
- What's broken?
- What's the business impact?
- Who's affected?

Proceeding with expedited workflow:
1. Reproduce (minimal)
2. Fix (smallest possible change)
3. Test (critical path only)
4. Deploy (with rollback ready)

What's the issue?"
```

### Minimal Fix Approach

```
"Hotfix ready:

**Change**: [Minimal change - smallest possible]
**Risk**: [Assessment]
**Rollback**: [How to undo if it fails]

Verification:
```bash
[Quick test command]
```

**IMPORTANT**: This is a minimal fix. We should follow up with
[proper solution] after the emergency is resolved.

Deploy?"
```

### Post-Hotfix

```
"Hotfix deployed.

**Immediate Actions**:
- [ ] Monitor for [X minutes]
- [ ] Verify fix in production
- [ ] Notify stakeholders

**Follow-up Actions** (schedule these):
- [ ] Root cause analysis
- [ ] Proper fix with full testing
- [ ] Post-mortem if needed

Emergency resolved?"
```
