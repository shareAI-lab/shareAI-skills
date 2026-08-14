# Error Handling

Quick guidance for error handling decisions. Applicable to all projects.

## Error Handling Decision Tree

```
This error...
|
+-- Caller can handle it?
|   --> Throw/raise - let caller decide
|
+-- Can recover automatically?
|   --> Retry with backoff, log warning
|
+-- Unrecoverable but expected?
|   --> Fail gracefully, clear message to user
|
+-- Unexpected/bug?
    --> Fail fast, log full context, alert if critical
```

## Error Message Quality

```
Good error = What + Why + How to fix

BAD:
"Invalid input"
"Error occurred"
"Something went wrong"
"Failed"

GOOD:
"Invalid email format: 'abc'. Expected: user@domain.com"
"Connection timeout after 30s to api.example.com. Check network or increase timeout."
"File not found: config.json. Run 'init' to create, or use --config to specify path."
"Payment failed: Card declined. Try a different card or contact your bank."
```

## Logging Levels

```
ERROR: Something failed, needs attention
       - Exceptions that affect functionality
       - Failed operations that can't retry

WARN:  Unexpected but handled, might need attention
       - Retries succeeded after failures
       - Deprecated usage detected
       - Performance thresholds exceeded

INFO:  Significant business events
       - User actions (login, purchase)
       - Process milestones
       - Config changes

DEBUG: Development troubleshooting
       - Function entry/exit
       - Variable values
       - Decision points

Production: ERROR + WARN + INFO
Development: All levels
```

## What to Log

```
Always log:
- Error message and stack trace
- Request/transaction ID for correlation
- User/session context (NOT credentials)
- Timestamp
- What was being attempted

Never log:
- Passwords, tokens, API keys
- Credit card numbers
- Personal data (SSN, etc.)
- Full request bodies with sensitive data
```

## Error Categories

```
User Error (4xx):
- Invalid input -> 400 Bad Request
- Not authenticated -> 401 Unauthorized
- Not authorized -> 403 Forbidden
- Not found -> 404 Not Found
- Conflict -> 409 Conflict

System Error (5xx):
- Bug/unexpected -> 500 Internal Server Error
- External service down -> 502 Bad Gateway
- Overloaded -> 503 Service Unavailable
- Timeout -> 504 Gateway Timeout
```

## Anti-Patterns

```
Never:
- Swallow exceptions silently: catch (e) { }
- Log and rethrow same error (double logging)
- Expose internal details to users (stack traces)
- Use exceptions for control flow
- Catch generic Exception when specific available

Avoid:
- Nested try-catch (refactor to functions)
- Error codes when exceptions available
- Returning null to indicate error
```

## Retry Pattern

```
When to retry:
- Network timeouts
- Rate limiting (429)
- Temporary failures (503)

When NOT to retry:
- Validation errors (400) - won't change
- Auth failures (401, 403) - won't change
- Not found (404) - won't appear
- Business logic errors

Exponential backoff:
Attempt 1: immediate
Attempt 2: wait 1s
Attempt 3: wait 2s
Attempt 4: wait 4s
Attempt 5: give up

With jitter: add random 0-500ms to prevent thundering herd
```

## Error Boundaries

```
Where to catch:
- API layer: Convert to HTTP response
- Service layer: Log and wrap with context
- Repository layer: Wrap DB errors

Pattern:
try {
  return await operation();
} catch (error) {
  logger.error('Operation failed', { error, context });
  throw new ServiceError('Friendly message', { cause: error });
}
```

## Graceful Degradation

```
When dependency fails, consider:

1. Return cached data (stale but available)
2. Return partial data (what you have)
3. Return default/fallback value
4. Disable feature gracefully
5. Queue for retry later

Always:
- Log the degradation
- Monitor degradation frequency
- Alert if prolonged
```
