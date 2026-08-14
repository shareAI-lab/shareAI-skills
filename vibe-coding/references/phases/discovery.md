# Phase: Discovery

Transform vague ideas into clear, actionable requirements.

---

## The Discovery Protocol

Start with fundamental questions:

```
"Before I propose solutions, help me understand:

**The Problem**
1. What's painful about the current situation?
2. What triggers this need? (specific scenario)

**The Users**
3. Who will use this? (be specific: "marketing lead" not "users")
4. What do they need to accomplish?

**The Vision**
5. If this worked perfectly, what's different?
6. How will we know it succeeded? (measurable)

**The Constraints**
7. Must integrate with existing systems?
8. Tech stack requirements?
9. Timeline or resource constraints?

Let's start with #1 and #5 - they reveal the core."
```

---

## Question Patterns

### For New Projects

```
1. What are you building? (elevator pitch)
2. Who is this for? What do they need?
3. What's the core workflow/use case?
4. What existing systems must this work with?
5. Tech preference? (or should I recommend?)
6. Timeline pressure? (MVP fast vs build right)
```

### For Feature Requests

```
1. What should the feature do? (specific behavior)
2. Where does it fit in the existing system?
3. Who will use it? How often?
4. What triggers this feature? What's the output?
5. Edge cases to handle?
6. How does this interact with existing features?
```

### For Vague Ideas

```
1. What prompted this idea? (the trigger)
2. What would be different if this existed?
3. Can you give an example scenario?
4. What's the simplest version that's useful?
5. Similar things you've seen and liked?
```

---

## Explore Solution Space

**Divergent Thinking**:
- 3 different ways to solve this?
- Simplest version that delivers value?
- Dream version with no constraints?

**Convergent Thinking**:
- Given constraints, which approach fits?
- What trade-offs are acceptable?
- MVP vs nice-to-have?

**Proposal Pattern**:
```
"I see a few approaches:

**Option A: [Simple]**
- Pros: Fast to build, easy to maintain
- Cons: Limited features
- Best if: Need something working quickly

**Option B: [Comprehensive]**
- Pros: Full-featured, scalable
- Cons: More complex, longer
- Best if: Long-term use

**Option C: [Hybrid]**
- Start simple, designed to extend
- Pros: Quick start with growth path
- Cons: Needs upfront architecture thought

Which resonates?"
```

---

## Discovery Output

Before leaving discovery, produce:

```
## Discovery Summary

**Building**: [One sentence]
**For**: [Specific user type]
**Solving**: [Core problem]
**Success metric**: [How we know it works]

**Core Features (v1)**:
1. [Feature] - [Why essential]
2. [Feature] - [Why essential]
3. [Feature] - [Why essential]

**NOT Building (v1)**:
- [Exclusion] - [Why excluded]

**Constraints**:
- [Constraint]

**Approach Options Explored**:
1. [Option A]: [Trade-off]
2. [Option B]: [Trade-off]
3. [Option C]: [Trade-off]

**Selected**: [Option] because [reasoning]

Human confirms? Then I'll move to design.
```

---

## Red Flags

| Signal | Risk | Response |
|--------|------|----------|
| "Just build X like Y" | Copying without understanding | "What specifically about Y? What would you change?" |
| Everything is P0 | No prioritization | "If only ONE feature, which?" |
| Scope keeps expanding | Never-ending discovery | "Let's lock v1. Add more in v2." |
| "Make it flexible" | Over-engineering | "Flexible for what scenarios?" |
| No user mentioned | Building for nobody | "Who specifically will use this?" |

---

## Transition to Design

Discovery complete when:
- [ ] Core problem and solution clear
- [ ] Scope bounded (in/out explicit)
- [ ] Human confirms requirements
- [ ] Ready to discuss HOW to build

**Transition**: "Requirements solid. Ready to talk technical approach?"
