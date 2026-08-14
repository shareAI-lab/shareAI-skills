# API & Interface Design

Quick guidance for API/library/CLI interface design.
Load when building: REST APIs, libraries, SDKs, CLI tools, any module interfaces.

## The Golden Rule

**Consistency is king.** Users hate surprises.

```
Consistency checklist:
[ ] Similar operations have similar names
[ ] Similar inputs have similar formats
[ ] Similar outputs have similar structures
[ ] Error formats are uniform
[ ] Naming convention is uniform (camelCase OR snake_case, not mixed)
```

## REST API Patterns

### URL Structure
```
/api/v1/{resources}           - collection (plural noun)
/api/v1/{resources}/{id}      - single item
/api/v1/{resources}/{id}/{sub} - nested resource

Good: /api/v1/users/123/orders
Bad:  /api/v1/getUser?id=123
Bad:  /api/v1/user/123 (singular)
```

### HTTP Methods
```
GET    - read (idempotent, no body)
POST   - create new resource
PUT    - replace entire resource (idempotent)
PATCH  - partial update
DELETE - remove resource (idempotent)

Idempotent = same request multiple times = same result
```

### Response Format (pick one, use everywhere)
```json
// Success
{
  "data": { ... },
  "meta": {
    "total": 100,
    "page": 1,
    "limit": 20,
    "hasMore": true
  }
}

// Error
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human readable description",
    "details": [
      { "field": "email", "issue": "required" }
    ]
  }
}

// Never mix: sometimes { data } sometimes raw object
```

### Status Codes
```
Success:
200 OK           - General success
201 Created      - Resource created (return the resource)
204 No Content   - Success, nothing to return (DELETE)

Client Error:
400 Bad Request  - Invalid input
401 Unauthorized - Not authenticated
403 Forbidden    - Authenticated but not allowed
404 Not Found    - Resource doesn't exist
409 Conflict     - Duplicate or state conflict
422 Unprocessable - Valid format, invalid semantics

Server Error:
500 Internal     - Bug, unexpected error
502 Bad Gateway  - Upstream service failed
503 Unavailable  - Overloaded or maintenance
```

## Pagination

```
Any list that could return > 50 items needs pagination.

Request:
GET /api/users?page=2&limit=20
GET /api/users?cursor=abc123&limit=20

Response:
{
  "data": [...],
  "meta": {
    "total": 150,       // if known
    "page": 2,          // or cursor
    "limit": 20,
    "hasMore": true,
    "nextCursor": "xyz" // for cursor-based
  }
}

Cursor-based is better for:
- Large datasets
- Real-time data (items added/removed)
- Consistent pagination
```

## Library/SDK Design

### The 5-Minute Rule
```
New user must be able to:
1. Install       (< 1 min)
2. Write code    (< 3 min)
3. See result    (< 1 min)

If your README example doesn't work by copy-paste, you've failed.
```

### API Surface
```
Good: Small, obvious
import { Client } from 'mylib';
const client = new Client({ apiKey: '...' });
const result = await client.doThing(input);

Bad: Large, confusing
import { ClientFactory, ConfigBuilder, AuthProvider } from 'mylib';
const config = new ConfigBuilder()
  .withAuth(new AuthProvider(...))
  .build();
const client = ClientFactory.create(config);
```

### Defaults
```
- Sensible defaults for everything
- Zero-config should work for common case
- Advanced config available but not required

// Good: works immediately
const client = new Client({ apiKey });

// Also good: can customize
const client = new Client({
  apiKey,
  timeout: 30000,
  retries: 3,
});
```

## CLI Design

### Basic Structure
```
mytool <command> [options] [arguments]

Required:
mytool --help          # Global help
mytool command --help  # Command help
mytool --version       # Version

Standard options:
--verbose, -v    More output
--quiet, -q      Less output
--config, -c     Config file path
--output, -o     Output file/format
```

### Exit Codes
```
0   - Success
1   - General error
2   - Misuse (wrong arguments)
126 - Permission denied
127 - Command not found
```

### Output Design
```
Good:
$ mytool build
Building project...
  Compiling 42 files... done
  Generating types... done
  Output: dist/

Build completed in 2.3s

Bad (too verbose):
$ mytool build
[2024-01-15 10:23:45] INFO Starting build
[2024-01-15 10:23:45] DEBUG Loading config
[2024-01-15 10:23:45] DEBUG Found 42 files
... (100 more lines)

Bad (too quiet):
$ mytool build
Done.
```

### Progress Feedback
```
# Known progress
Processing... [████████░░] 80% (40/50)

# Unknown progress
Processing... ⠋ (elapsed: 5s)

# Multi-step
Step 1/3: Downloading... done
Step 2/3: Processing... [████░░░░] 45%
Step 3/3: Uploading... waiting
```

## Versioning

```
API: URL versioning (clearest)
/api/v1/users
/api/v2/users

Library: Semver
MAJOR.MINOR.PATCH
- MAJOR: Breaking changes
- MINOR: New features, backward compatible
- PATCH: Bug fixes

Breaking change = increment MAJOR
```

## Documentation

```
Every public interface needs:
[ ] What it does (one line)
[ ] Parameters with types
[ ] Return value
[ ] Example usage
[ ] Error cases

Example:
/**
 * Creates a new user account.
 *
 * @param email - User's email address
 * @param name - User's display name
 * @returns The created user object
 * @throws ValidationError if email is invalid
 * @throws ConflictError if email already exists
 *
 * @example
 * const user = await createUser('alice@example.com', 'Alice');
 * console.log(user.id);
 */
```
