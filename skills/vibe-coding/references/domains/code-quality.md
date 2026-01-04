# Code Quality

Quick guidance for code quality decisions. Applicable to all projects.

## Function Design

Before writing a function, ask:
```
- Does it do ONE thing?
- Is the name self-explanatory?
- Are input/output types clear?
- Is it testable in isolation?
```

**Size guidance**:
- 5-20 lines ideal
- Max 50 lines (beyond = split it)
- 0-3 parameters ideal, max 5

## Naming Quick Reference

```
Verbs:
get/fetch   - retrieve existing
create/make - create new
update      - modify existing
delete      - remove
is/has/can  - returns boolean
to/as       - convert format
find/search - lookup with criteria
validate    - check correctness
parse       - extract structure
build       - construct complex object

Avoid:
process, handle, manage, do  - too vague
data, info, item, object     - add specifics
temp, tmp, x, foo            - meaningless
```

## Structure Principles

```
Good function:
- Single responsibility
- Single return type
- Side effects documented (or none)
- Handles edge cases explicitly

Good file/module:
- Single responsibility
- < 300 lines ideal
- Related code grouped
- Clear public interface
- Internal helpers hidden
```

## Code Smells - Fix Immediately

```
Must fix:
- Duplicated code blocks (3+ times)
- Deep nesting (> 3 levels)
- Magic numbers/strings
- Giant functions (> 100 lines)
- Commented-out code
- Empty catch blocks

Consider fixing:
- Too many parameters (> 5)
- Mixed abstraction levels
- Boolean parameters changing behavior
- Long parameter lists
```

## Refactor Decision

```
Refactor NOW if:
- About to copy code 3rd time -> extract
- Can't explain function in one sentence -> split
- Tests are hard to write -> simplify

Don't refactor NOW if:
- Code works and isn't changing
- No tests exist (add tests first)
- Under time pressure (note for later)
```

## Comments Guidance

```
Comment WHAT code does:     NO  (code should be self-explanatory)
Comment WHY code exists:    YES (intent, business reason)
Comment edge cases:         YES (non-obvious behavior)
Comment workarounds:        YES (with link to issue/reason)

Good: // Skip validation for admin users per security audit 2024-01
Bad:  // Loop through users
```

## Dependencies

```
Before adding a dependency:
1. Do we really need it? (vs writing 20 lines)
2. Is it maintained? (last commit, open issues)
3. What's the size impact?
4. Are there security concerns?

Prefer:
- Fewer, well-established deps
- deps with good TypeScript/types
- deps with minimal transitive deps
```
