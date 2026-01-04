# Phase: Design

Transform requirements into architecture.

---

## Architecture Proposal Pattern

```
"Based on discovery, here's my proposed architecture:

## System Overview

[ASCII diagram showing components and data flow]

## Key Technical Decisions

| Decision | Choice | Why | Trade-off |
|----------|--------|-----|-----------|
| [Area] | [Choice] | [Justification] | [What we give up] |

## What I'm NOT Recommending (and why)

- **[Alternative A]**: [Why not]
- **[Alternative B]**: [Why not]

## Data Model

[Key entities and relationships]

## API Design (if applicable)

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | /api/resource | Create |
| GET | /api/resource/:id | Read |

## Security Considerations

- [Security measure and why]

## Questions Before Proceeding

1. [Clarification needed]

If approved, I'll create implementation tasks."
```

---

## Architecture Decisions

### Technology Selection

Consider:
- Team familiarity
- Ecosystem maturity
- Long-term maintenance
- Performance requirements
- Integration needs

**Decision Format**:
```
**Decision**: [What]
**Options Considered**: [A, B, C]
**Selected**: [Choice]
**Rationale**: [Why]
**Trade-off Accepted**: [What we give up]
```

### Common Patterns

**Monolith vs Microservices**:
- Monolith: Faster to build, easier to deploy, sufficient for most projects
- Microservices: Only when scaling/team requires it

**SQL vs NoSQL**:
- SQL: Default for structured data, relationships
- NoSQL: When schema flexibility or specific access patterns required

**Server-rendered vs SPA**:
- Server: Simpler, better SEO, less JS
- SPA: Rich interactions, offline support

---

## Data Modeling

### Entity Relationship

```
User (1) ────────────── (N) Order
  │                           │
  │ has                       │ contains
  │                           │
  └──── Profile (1)     OrderItem (N)
```

### Schema Design Principles

- Normalize by default
- Denormalize for read performance when proven necessary
- Foreign keys for integrity
- Indexes on query patterns
- Soft deletes for audit trails

---

## API Design

### REST Principles

- Resources as nouns (`/users`, not `/getUsers`)
- HTTP verbs correctly (`GET` read, `POST` create, `PUT` update, `DELETE` delete)
- Consistent response format
- Meaningful status codes

### Error Response Format

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "field": "email"
  }
}
```

---

## Security by Default

- Input validation on all external data
- Parameterized queries (no SQL injection)
- Authentication on all protected routes
- Authorization checks per resource
- Secrets in environment variables
- HTTPS everywhere

---

## Design Checklist

Before proceeding to implementation:

- [ ] Architecture diagram clear
- [ ] Key decisions documented with rationale
- [ ] Alternatives considered and rejected with reasons
- [ ] Data model defined
- [ ] API contracts specified
- [ ] Security considerations addressed
- [ ] Human approves design

---

## Transition to Plan

Design complete when:
- [ ] Architecture approved
- [ ] Key decisions documented
- [ ] Trade-offs explicit
- [ ] Ready to break into tasks

**Transition**: "Design approved. Breaking into implementation tasks."
