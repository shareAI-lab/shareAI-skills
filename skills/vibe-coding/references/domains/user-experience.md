# User Experience

Quick guidance for user-facing projects.
Load when building: Web apps, CLI tools, SDKs, mobile apps - anything with users.

## The 6 Essential States

Every feature needs all 6 states designed:

```
[ ] EMPTY    - No data yet
              What shows? How to start?
              "No messages yet. Start a conversation?"

[ ] LOADING  - Waiting for data
              Skeleton > spinner
              Show progress if known

[ ] SUCCESS  - Operation completed
              What happened? What's next?
              "Order placed! Track it here."

[ ] ERROR    - Something went wrong
              What failed? How to fix?
              "Payment failed. Try a different card."

[ ] PARTIAL  - Some succeeded, some failed
              Clear status for each item
              "3 of 5 files uploaded. 2 failed."

[ ] EDGE     - Unusual conditions
              Offline, timeout, no permission
              Graceful degradation
```

## First Experience

```
New user must:
[ ] Understand value in < 30 seconds
    - Clear headline, not jargon
    - Show, don't tell

[ ] Succeed at something in < 2 minutes
    - Immediate small win
    - Progress feedback

[ ] Not register before seeing value
    - Demo mode or limited access
    - Registration after value proven
```

## Onboarding Patterns

```
Good:
- Contextual hints when needed
- Progressive disclosure
- Skip option for power users
- Clear progress indicator
- Celebrate first success

Bad:
- Multi-step tutorial upfront
- Modal blocking content
- Force all features at once
- No way to skip
- Patronizing explanations
```

## Micro-copy Templates

### Empty States
```
"No [items] yet. [Action] to get started."
"Your [collection] is empty. [Create first]?"
"Nothing here! [What to do next]."
```

### Error States
```
"[What happened]. [How to fix]."
"Couldn't [action]: [reason]. Try [alternative]."
"[Problem]. [Specific solution] or [contact support]."
```

### Success States
```
"[Action] complete! [Next step]?"
"[Item] created. [View it] or [create another]?"
"Done! [What changed] and [what to do next]."
```

### Confirmation Dialogs
```
Good: "Delete 3 selected items?"
Bad:  "Are you sure?"

Good: "Cancel order #1234? This cannot be undone."
Bad:  "Confirm cancellation"
```

### Loading States
```
< 200ms:  No feedback needed
200ms-1s: Subtle indicator (opacity, skeleton)
1s-5s:    Clear progress (spinner with text)
> 5s:     Progress bar with estimate
```

## CLI User Experience

```
CLI users are power users, but still users.

Progress feedback:
$ mytool process data.csv
Processing... [████████░░] 80% (400/500 rows)

Multi-step:
Step 1/3: Downloading... done (2.3s)
Step 2/3: Processing... [████░░░░] 45%
Step 3/3: Uploading... waiting

Errors with solution:
Error: Config not found at ./config.json

To fix:
  1. Run 'mytool init' to create default, or
  2. Use --config /path/to/config.json

Checklist:
[ ] --help is complete and useful
[ ] Progress for operations > 1s
[ ] Errors explain how to fix
[ ] Exit codes are correct (0=success)
[ ] Supports --quiet and --verbose
[ ] Works with pipes (stdin/stdout)
```

## SDK/Library DX

```
Developer Experience = User Experience for developers

[ ] README example works by copy-paste
[ ] Error messages tell dev what to fix
[ ] Types are complete (TypeScript: .d.ts, Python: type hints)
[ ] Common patterns are one-liners
[ ] Edge cases documented

Error message example:
Bad:  "Invalid config"
Good: "Missing required field 'apiKey' in config. Get your API key at https://..."
```

## Edge Cases Checklist

```
For every feature, ask:
[ ] What if no data (empty)?
[ ] What if one item?
[ ] What if 10,000 items?
[ ] What if slow network?
[ ] What if offline?
[ ] What if user is new?
[ ] What if user is expert?
[ ] What if user makes mistake?
[ ] What if partial failure?
```

## Accessibility Basics

```
Must have:
[ ] Keyboard navigation works
[ ] Focus states visible
[ ] Color is not only indicator
[ ] Text has sufficient contrast (4.5:1)
[ ] Images have alt text
[ ] Form fields have labels

Test by:
- Tab through entire flow
- Use screen reader briefly
- Check with color blindness simulator
```

## Feedback Patterns

```
User action -> immediate feedback:
- Click button -> button state change
- Submit form -> loading indicator
- Complete action -> success message
- Error -> error message + solution

Timing:
< 100ms:  Feels instant
100-300ms: Acknowledged
300ms-1s: Noticeable wait
> 1s:     Needs progress indicator
```
