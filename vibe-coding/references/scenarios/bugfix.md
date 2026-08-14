# Scenario: Bug Fix

Something isn't working correctly. Use the RAPID method.

---

## RAPID Method

```
R - REPRODUCE  : Confirm and isolate the bug
A - ANALYZE    : Understand what's happening
P - PINPOINT   : Find the exact cause
I - IMPLEMENT  : Fix the issue
D - DEPLOY     : Verify and deploy the fix
```

---

## R - Reproduce

```
"Let me reproduce the issue:

**Reported**: [What was reported]
**Steps**:
1. [Step 1]
2. [Step 2]
3. [Expected vs Actual]

**Reproduced**: Yes/No

[If no] I couldn't reproduce. Can you provide:
- Environment details?
- Exact input data?
- Screenshots/logs?"
```

### Isolate Conditions

```
"Investigating when this occurs:

Works: [Condition A]
Fails: [Condition B]
Works: [Condition C]

The bug appears specifically when: [Isolated condition]"
```

---

## A - Analyze

```
"Tracing execution:

1. Request hits [entry point]
2. -> [function A]
3. -> [function B]
4. -> [function C] <- Error occurs here
5. -> (never reached)

The failure is in [location]"
```

---

## P - Pinpoint

```
"Found the issue:

**Root Cause**: [Exact problem]
**Location**: [File:line]
**Why It Happens**: [Explanation]

The bug occurs because [detailed explanation]."
```

### Root vs Symptom

```
**Symptom**: [What user sees]
**Immediate cause**: [Direct trigger]
**Root cause**: [Underlying issue]

Fix options:
1. Treat symptom only (quick, may recur)
2. Fix root cause (thorough)
3. Both (defense in depth)

Recommendation: [Choice] because [reason]
```

---

## I - Implement

```
"Proposed fix:

**Change**: [What I'll change]
**Why This Fixes It**: [Explanation]
**Risk**: [What could go wrong]

Implementing with regression test..."
```

---

## D - Deploy

```
"Fix complete:

**Original bug**: No longer reproduces
**Regression tests**: All passing
**New test**: Added and passes

**Verification**:
```bash
[Command]
```

Ready to commit?"
```

---

## Debugging Strategies

**Binary Search**: For "it worked before" bugs
```
Commits: A -> B -> C -> D -> E -> F (broken)
Test C... Works
Test E... Broken
Test D... Works
Bug introduced in commit E
```

**Divide and Conquer**: For complex systems
```
Testing in isolation:
- Database layer: Works
- API layer: Works
- Business logic: Fails  <- Found it
- Frontend: Works
```

---

## Common Bug Categories

| Category | Example | Fix Pattern |
|----------|---------|-------------|
| Logic | Off-by-one, wrong operator | Trace execution |
| Async | Missing await, race condition | Check timing |
| Null/Undefined | Optional property access | Add guards |
| State | Stale closure, mutation | Check lifecycle |
