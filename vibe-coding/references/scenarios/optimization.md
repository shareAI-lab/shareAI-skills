# Scenario: Performance Optimization

Something is too slow. Measure first, optimize second.

---

## The Golden Rule

**NEVER optimize without data.** Profile first, identify bottleneck, then optimize.

---

## Workflow

```
PROFILE -> IDENTIFY BOTTLENECK -> PROPOSE FIX -> IMPLEMENT -> MEASURE AGAIN
```

---

## Step 1: Profile First

```
"Before optimizing, I need to find the actual bottleneck:

**Current Performance**: [How slow?]
**Target Performance**: [How fast should it be?]

Let me profile to find where time is spent..."
```

### Profiling Tools

| Environment | Tool |
|-------------|------|
| Node.js | `node --prof`, `clinic.js` |
| Python | `cProfile`, `py-spy` |
| Browser | DevTools Performance tab |
| Database | `EXPLAIN ANALYZE` |
| General | Timestamps around suspect code |

---

## Step 2: Identify Bottleneck

```
"Profiling results:

| Area | Time % | Details |
|------|--------|---------|
| [A] | 60% | [Description] |
| [B] | 25% | [Description] |
| [C] | 15% | [Description] |

**Actual Bottleneck**: [What's really slow]
**NOT the problem**: [What looked suspicious but isn't]

The [X] takes [Y]ms which is [Z]% of total time."
```

---

## Step 3: Propose Optimization

```
"Proposed optimization:

**Target**: [What we're optimizing]
**Approach**: [How]
**Expected Improvement**: [Quantified]
**Trade-off**: [What we give up]

Alternative approaches:
| Approach | Improvement | Trade-off | Why Not |
|----------|-------------|-----------|---------|

Proceed with recommended approach?"
```

---

## Step 4: Implement with Benchmarks

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

## Common Bottlenecks

| Bottleneck | Signs | Fixes |
|------------|-------|-------|
| N+1 queries | Many small DB calls | Batch/join queries |
| Missing index | Slow queries on large tables | Add appropriate index |
| Blocking I/O | Main thread stalls | Async/parallel |
| Memory churn | Frequent GC | Object pooling |
| Large payloads | Slow API responses | Pagination, compression |
| Unoptimized loops | Slow with large data | Algorithm improvement |

---

## Optimization Checklist

- [ ] Current performance measured
- [ ] Target performance defined
- [ ] Profiling completed
- [ ] Bottleneck identified (not guessed)
- [ ] Optimization implemented
- [ ] Improvement measured
- [ ] No regressions introduced
