# Pattern: Systematic Debugging

Approach debugging methodically for efficient problem resolution.

---

## The RAPID Framework

```
R - REPRODUCE  : Confirm and isolate the bug
A - ANALYZE    : Understand what's happening
P - PINPOINT   : Find the exact cause
I - IMPLEMENT  : Fix the issue
D - DEPLOY     : Verify and deploy the fix
```

For detailed RAPID workflow, see [scenarios/bugfix.md](../scenarios/bugfix.md).

---

## Debugging Strategies

### Binary Search (Git Bisect)

For "it worked before" bugs:

```
Commits: A -> B -> C -> D -> E -> F (current, broken)

Test C... Works
Test E... Broken
Test D... Works

Bug introduced in commit E: "Refactor data handling"
```

### Divide and Conquer

For complex systems:

```
Testing each in isolation:
- Database layer: Works
- API layer: Works
- Business logic: Fails  <- Found it
- Frontend: Works

Testing business logic functions:
- validateInput(): Works
- processData(): Fails  <- Found it
- formatOutput(): Works
```

### Print Debugging

When flow is unclear:

```javascript
console.log('1. Input:', JSON.stringify(input));
console.log('2. After validation:', validated);
console.log('3. Before transform');
// ... crash happens here
console.log('4. After transform');  // Never reached
```

### Rubber Duck Debugging

Explain the code step by step:

```
"Let me walk through this logic:

1. User submits form with email
2. We check if email exists... wait
3. We're checking email exists AFTER creating the user
4. That's the bug - order is wrong

The check should come BEFORE creation."
```

---

## Common Bug Categories

### Logic Errors

```javascript
// Off-by-one
for (let i = 0; i <= array.length; i++)  // Should be <

// Wrong operator
if (user.role = 'admin')  // Should be ===

// Missing case
switch (type) {
  case 'a': return handleA();
  case 'b': return handleB();
  // Missing: case 'c'
}
```

### Async Issues

```javascript
// Not awaiting
const user = getUser(id);  // Missing await
console.log(user.name);    // user is a Promise

// Race condition
let data;
fetchData().then(d => data = d);
process(data);  // data is still undefined
```

### Null/Undefined

```javascript
// Optional property
const name = user.profile.name;  // profile might be undefined

// Fix:
const name = user.profile?.name ?? 'Unknown';
```

### State Issues

```javascript
// Stale closure in React
const [count, setCount] = useState(0);
const handleClick = () => {
  setCount(count + 1);  // Uses stale count
  setCount(count + 1);  // Same stale value
};

// Fix:
setCount(c => c + 1);
```

---

## When Stuck

1. **Take a break** - Fresh eyes find bugs
2. **Explain it** - Describe to someone (or rubber duck)
3. **Check assumptions** - Verify what you "know" is true
4. **Search for similar** - Others may have hit this
5. **Simplify** - Remove code until bug disappears
6. **Add logging** - More visibility into execution

---

## Debugging Checklist

### Before Starting
- [ ] Can reproduce the bug
- [ ] Understand expected behavior
- [ ] Have access to logs/errors

### During Investigation
- [ ] Isolated the conditions
- [ ] Traced execution path
- [ ] Formed hypothesis
- [ ] Verified hypothesis

### After Fixing
- [ ] Bug no longer reproduces
- [ ] Tests added/updated
- [ ] No regressions
- [ ] Root cause addressed
