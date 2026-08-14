# Testing Strategy

Quick guidance for testing decisions. Applicable to all projects.

## What to Test - Decision Tree

```
This code...
|
+-- Is pure logic/calculation?
|   --> Unit test (required)
|
+-- Crosses a boundary (API/DB/file/external)?
|   --> Integration test (required for critical paths)
|
+-- Is a critical user journey?
|   --> E2E test (happy path only, keep minimal)
|
+-- Is UI appearance?
    --> Snapshot test (optional, high maintenance cost)
```

## Test Quality Checklist

```
Good test:
[ ] Name describes expected behavior
    "should return empty array when no items found"
[ ] One logical assertion per test
[ ] Independent (no shared mutable state)
[ ] Deterministic (same result every run)
[ ] Fast (unit < 10ms, integration < 100ms)
[ ] Readable (arrange-act-assert clear)
```

## Coverage Guidance

```
Don't chase 100%. Chase meaningful coverage.

Critical business logic: 90%+
API endpoints:          80%+
Utility functions:      80%+
Error paths:            70%+
UI components:          varies (snapshot optional)
Glue code:              can be low
```

## Test Patterns

```
Arrange-Act-Assert:
// Arrange
const user = createTestUser();

// Act
const result = service.process(user);

// Assert
expect(result.status).toBe('success');


Given-When-Then (BDD):
// Given a logged-in user
// When they submit an order
// Then order is created and email is sent
```

## Mocking Guidance

```
Mock at boundaries:
[YES] External APIs
[YES] Database (for unit tests)
[YES] File system
[YES] Time/dates
[YES] Random values

Don't mock:
[NO] The thing you're testing
[NO] Internal implementation details
[NO] Simple utilities
[NO] Everything (over-mocking = brittle tests)
```

## TDD Decision

```
Use TDD when:
- Logic is complex with many branches
- Requirements are clear upfront
- Building a library/SDK/API
- High-stakes code (payments, auth)

Skip TDD when:
- Exploring/prototyping
- UI layout work
- Requirements are fuzzy
- Throwaway code

If skipping TDD:
- Write tests BEFORE PR, not "later"
- "Later" means never
```

## Test Naming

```
Pattern: should_[expected]_when_[condition]

Good:
- should_return_null_when_user_not_found
- should_throw_error_when_email_invalid
- should_send_notification_when_order_placed

Bad:
- test1
- testUserFunction
- it_works
```

## Test Data

```
Use factories/builders for test data:

// Good
const user = createUser({ role: 'admin' });
const order = createOrder({ user, status: 'pending' });

// Bad - fragile, hard to maintain
const user = { id: 1, name: 'Test', email: 'test@test.com', role: 'admin', ... };
```

## Flaky Tests

```
If a test fails intermittently:
1. Fix it immediately (flaky = worthless)
2. Common causes:
   - Timing/async issues -> add proper waits
   - Shared state -> isolate tests
   - External dependencies -> mock them
   - Date/time -> use fixed test time
3. Never @skip without a ticket to fix
```
