# Data Engineering

Quick guidance for data/ML projects.
Load when building: Data pipelines, ETL, ML workflows, analytics, data processing.

## Pipeline Design Principles

```
Every pipeline should be:
[ ] Idempotent  - Same input = same output, safe to re-run
[ ] Observable  - Can see what's happening (logs, metrics)
[ ] Recoverable - Can resume from failure
[ ] Testable    - Can validate with sample data
```

## Idempotency Patterns

```
Make operations safe to retry:

Database:
- Use UPSERT instead of INSERT
- Check before write if already processed
- Use transaction IDs for deduplication

Files:
- Write to temp, then atomic rename
- Include run ID in output path
- Clean up before re-run or append safely

Processing:
- Track watermarks (last processed ID/timestamp)
- Use batch IDs for deduplication
- Store processing state externally
```

## Data Validation

```
Validate at boundaries:

INPUT VALIDATION:
[ ] Schema matches expectation
[ ] Required fields present
[ ] Types are correct
[ ] Values in valid ranges
[ ] No unexpected nulls in required fields
[ ] Referential integrity (foreign keys exist)

Fail fast:
def validate_input(df):
    errors = []
    if df.empty:
        errors.append("Empty dataframe")
    if 'id' not in df.columns:
        errors.append("Missing required column: id")
    if df['id'].duplicated().any():
        errors.append(f"Duplicate IDs found")
    if errors:
        raise ValidationError("\n".join(errors))

OUTPUT VALIDATION:
[ ] Row counts match expectation
[ ] No unexpected nulls introduced
[ ] Aggregations make sense
[ ] No data loss
```

## Error Handling in Pipelines

```
Pipeline failed...
|
+-- Transient error (network, temp file)?
|   --> Retry with exponential backoff
|       Log warning, continue
|
+-- Data quality issue (bad records)?
|   --> Options:
|       - Skip and log (for non-critical)
|       - Quarantine to dead-letter
|       - Fail entire batch (for critical)
|
+-- Schema change upstream?
|   --> Fail loudly, alert, needs investigation
|
+-- Unknown error?
    --> Fail fast, log everything, alert
```

## Batch Processing Patterns

```
Large datasets:
- Process in chunks (1000-10000 records)
- Checkpoint progress after each chunk
- Support resume from last checkpoint

Pattern:
def process_in_batches(data, batch_size=1000):
    last_checkpoint = load_checkpoint()

    for batch_start in range(last_checkpoint, len(data), batch_size):
        batch = data[batch_start:batch_start + batch_size]
        process_batch(batch)
        save_checkpoint(batch_start + batch_size)
```

## Incremental Processing

```
Don't reprocess everything:

Watermark pattern:
- Track last processed timestamp/ID
- Query only new/changed records
- Update watermark after success

Change detection:
- Compare checksums
- Use updated_at timestamps
- Database change data capture (CDC)

Late arrivals:
- Allow lookback window
- Reprocess recent partitions
- Track data completeness
```

## Data Quality Checks

```
Automated checks:

Freshness:
- Data arrived on time?
- Latest timestamp within SLA?

Completeness:
- Expected row count?
- All required fields populated?

Accuracy:
- Values in valid ranges?
- Aggregates match source?
- Cross-field consistency?

Uniqueness:
- Primary keys unique?
- No duplicate records?

Run checks:
- After each pipeline stage
- Alert on failures
- Block downstream if critical
```

## Performance Patterns

```
Common optimizations:

N+1 queries:
BAD:  for user in users: get_orders(user.id)
GOOD: get_orders_for_users([u.id for u in users])

Memory explosion:
BAD:  df = pd.read_csv('huge.csv')
GOOD: for chunk in pd.read_csv('huge.csv', chunksize=10000):

Slow joins:
- Index join columns
- Pre-filter before join
- Consider denormalization for read-heavy

Parallel processing:
- Partition data for parallel workers
- Use appropriate parallelism (CPU-bound vs I/O-bound)
- Manage memory per worker
```

## Monitoring & Alerting

```
Track:
- Pipeline run duration (trend)
- Records processed
- Error counts
- Data freshness (time since last update)
- Data quality scores

Alert on:
- Pipeline failure
- Duration > 2x normal
- Zero records processed
- Quality checks failed
- Data stale > SLA
```

## Pipeline Checklist

```
Before shipping pipeline:
[ ] Tested with production-like data volume
[ ] Handles empty input gracefully
[ ] Handles malformed records (skip/log/fail)
[ ] Idempotent (safe to re-run)
[ ] Has checkpointing for long runs
[ ] Logs useful information
[ ] Has monitoring/alerting
[ ] Documented expected runtime
[ ] Has runbook for common failures
[ ] Tested failure and recovery
```

## SQL Quality

```
Query best practices:
- Explicit column names (not SELECT *)
- WHERE clause before JOIN when possible
- Use EXPLAIN to check query plan
- Index columns in WHERE and JOIN
- Avoid functions on indexed columns
- LIMIT in dev queries

Readable SQL:
- One clause per line
- Consistent capitalization
- Meaningful table aliases
- Comments for complex logic
```
