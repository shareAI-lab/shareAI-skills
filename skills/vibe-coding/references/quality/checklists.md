# Quality Checklists

Ready-to-use checklists for different development scenarios.

---

## Pre-Ship Checklist (Universal)

### Code Quality
- [ ] All tests pass
- [ ] No lint errors
- [ ] Type check passes (if applicable)
- [ ] No console.log or debug statements
- [ ] Error handling is comprehensive
- [ ] No hardcoded values that should be configurable

### Security
- [ ] No secrets in code
- [ ] Input validation on all external data
- [ ] SQL injection prevention verified
- [ ] XSS prevention verified
- [ ] Authentication/authorization correct

### Performance
- [ ] No N+1 query problems
- [ ] No blocking operations in hot paths
- [ ] Reasonable response times

### Documentation
- [ ] README explains how to run
- [ ] Complex logic is commented
- [ ] API endpoints documented (if applicable)

### Final Check
- [ ] Works on clean install
- [ ] Human has tested core flows

---

## Feature Checklist

### Before Starting
- [ ] Requirements understood
- [ ] Design approach approved
- [ ] Dependencies identified

### During Development
- [ ] Following design specs
- [ ] Writing tests alongside code
- [ ] Regular commits

### Before Review
- [ ] Acceptance criteria met
- [ ] Tests pass locally
- [ ] No debug code
- [ ] Self-reviewed

---

## Bug Fix Checklist

### Investigation
- [ ] Bug reproduced reliably
- [ ] Root cause identified
- [ ] Scope of impact understood

### Fix
- [ ] Minimal change to fix issue
- [ ] No side effects
- [ ] Regression test added

### Verification
- [ ] Bug no longer reproduces
- [ ] All tests pass
- [ ] Related functionality works

---

## API Endpoint Checklist

- [ ] RESTful URL structure
- [ ] Appropriate HTTP method
- [ ] Input validation
- [ ] Authentication check
- [ ] Authorization check
- [ ] Proper status codes
- [ ] Tests for happy path
- [ ] Tests for error cases

---

## Frontend Component Checklist

- [ ] Accessible (keyboard, screen reader)
- [ ] Responsive (mobile to desktop)
- [ ] Loading states handled
- [ ] Error states handled
- [ ] Focus management correct
- [ ] Cross-browser tested

---

## Database Change Checklist

- [ ] Migration scripts prepared
- [ ] Rollback plan documented
- [ ] Index strategy considered
- [ ] Migration tested locally
- [ ] Data preservation verified

---

## Quick Quality Check

```
5-Second Check:
[ ] Does it compile?
[ ] Do tests pass?
[ ] Would I understand this in 6 months?
[ ] Is it secure?
[ ] Is it fast enough?
```

---

## Commit Message Template

```
type(scope): subject

[optional body]

Types: feat, fix, docs, style, refactor, test, chore
Scope: component, module, or area affected
Subject: imperative mood, < 50 chars
```

---

## PR Description Template

```md
## What
[Brief description]

## Why
[Reason for the change]

## How
[Key implementation details]

## Testing
- [ ] Manual testing done
- [ ] Unit tests added/updated
```
