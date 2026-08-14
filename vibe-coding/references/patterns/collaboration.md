# Pattern: Human-AI Collaboration

Effective collaboration patterns between humans and AI agents.

---

## The Collaboration Model

### Division of Responsibilities

```
HUMAN (20% effort → 80% impact)       AI (80% effort → 20% impact)
─────────────────────────────────     ─────────────────────────────
Strategy & Direction                   Execution & Implementation
├── Define goals                       ├── Write code
├── Make decisions                     ├── Run tests
├── Resolve ambiguity                  ├── Debug issues
├── Set priorities                     └── Generate options

Quality Control                        Research & Analysis
├── Review outputs                     ├── Explore codebases
├── Validate results                   ├── Find patterns
├── Approve changes                    ├── Gather information
└── Catch errors                       └── Summarize findings

Domain Knowledge                       Documentation
├── Business context                   ├── Generate docs
├── User needs                         ├── Write specs
├── Organizational constraints         └── Create reports
└── Historical decisions
```

---

## Communication Protocols

### Information Flow: Human → AI

**Providing Context**
```
Good: "We're building a CLI tool for developers who need to manage
      multiple git repos. They currently use shell scripts but want
      something more robust. Must work on Mac and Linux."

Bad:  "Build a git tool"
```

**Providing Feedback**
```
Good: "Keep the API structure. Change the auth from session to JWT
      because we need stateless scaling."

Bad:  "This is wrong"
```

**Providing Direction**
```
Good: "Let's focus on the core CRUD operations first. We can add
      search and filtering in phase 2."

Bad:  "Build everything"
```

### Information Flow: AI → Human

**Asking Questions**
```
Good: "For the authentication system, I need to decide:
      1. Session-based (simpler) or JWT (stateless)?
      2. Where to store tokens - cookies or localStorage?

      For your use case (API + web client), I'd suggest JWT in
      httpOnly cookies. Thoughts?"

Bad:  "What auth do you want?"
```

**Reporting Progress**
```
Good: "Completed the user service (3/5 tasks done):
      ✓ Create user
      ✓ Get user by ID
      ✓ Update user
      → Delete user (current)
      ○ List users

      Found an edge case: what if user has active sessions when
      deleted? Options: invalidate all / keep until expiry"

Bad:  "Done with some stuff"
```

**Surfacing Decisions**
```
Good: "I need to decide how to handle pagination:

      Option A: Offset-based (page=2&limit=20)
      - Simpler to implement
      - Can miss items if data changes

      Option B: Cursor-based (after=xyz&limit=20)
      - More complex
      - Handles data changes correctly

      For an internal tool with moderate data, I'd suggest offset.
      For a public API with high volume, cursor is better.

      Which fits your case?"

Bad:  "Using offset pagination"
```

---

## Collaboration Patterns

### Pattern 1: Explore → Propose → Decide

When approaching something new:

```
1. AI EXPLORES
   "Let me look at the codebase to understand..."
   [Reads files, analyzes patterns]

2. AI PROPOSES
   "Based on what I found, here are options:
    - Option A: [approach] because [reason]
    - Option B: [approach] because [reason]
    I recommend A because..."

3. HUMAN DECIDES
   "Let's go with A, but also consider X"

4. AI EXECUTES
   "Proceeding with A, incorporating X..."
```

### Pattern 2: Draft → Review → Refine

When creating something:

```
1. AI DRAFTS
   "Here's a first pass at [thing]:
    [Draft content]
    Let me know what to adjust"

2. HUMAN REVIEWS
   "Good structure. Change X, add Y, remove Z"

3. AI REFINES
   "Updated version:
    - Changed X to [new]
    - Added Y
    - Removed Z
    [Refined content]"

4. HUMAN APPROVES
   "This works. Let's proceed."
```

### Pattern 3: Checkpoint → Validate → Continue

For longer work:

```
1. AI WORKS on chunk 1
   "Completed [chunk 1]. Key decisions:
    - [Decision made]
    Ready for review before continuing"

2. HUMAN VALIDATES
   "Looks good" OR "Change X before continuing"

3. AI CONTINUES to chunk 2
   "Starting [chunk 2]..."

[Repeat until done]
```

---

## Trust Calibration

### When to Trust AI Output

**High Trust** (minimal review):
- Boilerplate code
- Standard patterns (CRUD, auth setup)
- Code formatting/style
- Documentation generation

**Medium Trust** (careful review):
- Business logic implementation
- API design
- Database queries
- Error handling

**Low Trust** (thorough review):
- Security-sensitive code
- Performance-critical paths
- Complex algorithms
- Integration points with external systems

### Verification Strategies

**For High Trust**:
```
AI: "Created standard REST endpoints following project patterns"
Human: [Quick scan, accept]
```

**For Medium Trust**:
```
AI: "Implemented the discount calculation logic"
Human: [Test with edge cases, review formula]
```

**For Low Trust**:
```
AI: "Added authentication middleware"
Human: [Security review, penetration test, code audit]
```

---

## Handling Disagreements

### When AI Suggests Something Different

```
Human: "Use library X"
AI: "I can use X. I'd also suggest considering Y because:
     - [Reason 1]
     - [Reason 2]

     But X will work fine if you prefer it. Which one?"
```

### When Human Wants Something Risky

```
Human: "Store passwords in plain text"
AI: "I strongly advise against this because:
     - [Security risk 1]
     - [Security risk 2]

     If you have a specific reason for this requirement,
     I'd like to understand it. Otherwise, I recommend
     using bcrypt hashing which is industry standard."
```

### When Requirements Conflict

```
AI: "There's a conflict in the requirements:
     - Requirement A says [X]
     - Requirement B says [Y]

     These can't both be true. Options:
     1. Prioritize A (accept [consequence])
     2. Prioritize B (accept [consequence])
     3. Modify both to [compromise]

     Which direction?"
```

---

## Efficiency Maximizers

### Parallel Preparation

While AI executes Task A:
- Human prepares context for Task B
- Human reviews completed tasks
- Human plans next priorities

### Context Documents

Maintain persistent context:
- CLAUDE.md for project knowledge
- Architecture decision records
- Coding conventions document

### Batch Similar Work

Group related tasks:
```
Instead of:
  Task 1: Add user endpoint → Review
  Task 2: Add post endpoint → Review
  Task 3: Add comment endpoint → Review

Do:
  Task: Add all CRUD endpoints (user, post, comment)
  Single review
```

### Progressive Trust

Start with oversight, build autonomy:
```
Session 1: AI learns project structure
Session 2: AI handles simple tasks with review
Session 3: AI tackles complex features
Session 4: AI works semi-autonomously on known patterns
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Blind trust | Bugs slip through | Verify based on risk |
| Micro-management | Slow progress | Right-size tasks |
| Over-delegation | Wrong decisions | Human decides strategy |
| Under-specification | Wrong output | Provide full context |
| No checkpoints | Wasted work | Validate incrementally |
| Scope creep acceptance | Never done | Push back on additions |

---

## Collaboration Checklist

### Starting a Session
- [ ] Context is loaded (CLAUDE.md, relevant files)
- [ ] Goal is clear
- [ ] Priorities are set
- [ ] Constraints are known

### During Work
- [ ] Regular checkpoints
- [ ] Questions answered promptly
- [ ] Feedback is specific
- [ ] Decisions are documented

### Ending a Session
- [ ] Work is committed/saved
- [ ] State is documented
- [ ] Next steps are clear
- [ ] Handoff notes if needed
