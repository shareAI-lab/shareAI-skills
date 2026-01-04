# UI Aesthetics

Quick guidance for UI/frontend visual design.
Load when building: Web UI, mobile UI, any visual interface.

## The Anti-Slop Mandate

Avoid the telltale signs of generic AI-generated design:

```
BANNED FONTS:
- Inter, Roboto, Arial, Helvetica as primary
- system-ui without intention
- Comic Sans (obviously)

BANNED COLORS:
- Purple-to-blue gradients on white
- #007bff (Bootstrap blue)
- #6c757d (Bootstrap gray)
- Tailwind defaults unchanged

BANNED LAYOUTS:
- Everything perfectly centered
- Uniform card grids (same size, same spacing)
- Symmetric everything
- Three-column feature sections

BANNED PATTERNS:
- Hero + 3-col features + Pricing + CTA
- Identical border-radius on everything
- Generic gradient buttons
- Stock photo hero
```

## Design Decision First

Before writing ANY CSS, answer these:

```
1. VIBE (one word)
   What's the feeling?
   Examples: brutal, playful, luxurious, editorial, organic, technical

2. MEMORABLE
   What's the ONE thing users will remember?
   The bold typography? Unusual color? Unique interaction?

3. DIFFERENTIATION
   How is this different from competitors?
   What makes it recognizable?
```

## Style Starting Points

Pick a direction and commit:

### Editorial/Magazine
```
- Serif headlines, dramatic whitespace
- Large type scale contrast (48px+ headlines)
- Grid-breaking elements
- Black and white with one accent
- Fonts: Playfair Display, Cormorant, Lora
```

### Brutalist
```
- Monospace or bold sans-serif
- High contrast, harsh colors
- Exposed grid, visible borders
- No rounded corners
- Raw, unpolished intentionally
- Fonts: JetBrains Mono, Space Mono, IBM Plex Mono
```

### Luxury/Premium
```
- Thin font weights, generous letter-spacing
- Muted palette (cream, charcoal, gold accents)
- Ample margins, slow reveals
- Subtle animations, no flash
- Fonts: Cormorant Garamond, Tenor Sans
```

### Playful/Friendly
```
- Rounded shapes, bouncy animations
- Bright, saturated colors
- Oversized elements
- Personality in micro-interactions
- Fonts: Nunito, Quicksand, Poppins
```

### Technical/Developer
```
- Monospace for code, clean sans for UI
- Dark mode default
- Neon accents on dark
- Minimal decoration
- Fonts: JetBrains Mono, Inter for UI
```

## Typography Quick Guide

```
Type scale (use consistent ratio):
Display: 48-72px
H1: 36-48px
H2: 24-30px
H3: 20-24px
Body: 16-18px
Small: 14px
Caption: 12px

Line height:
Headlines: 1.1-1.2
Body: 1.5-1.6

Font pairing (safe combos):
- Playfair Display + Source Sans Pro
- Space Mono + Work Sans
- Cormorant + Montserrat
- JetBrains Mono + Inter
```

## Color Quick Guide

```
Color structure:
- 1 dominant color (60%)
- 1-2 supporting colors (30%)
- 1 accent for CTAs (10%)

Contrast requirements:
- Text on background: 4.5:1 minimum
- Large text: 3:1 minimum
- Important UI elements: 3:1 minimum

Build from:
- One main brand color
- Derive shades (lighten/darken)
- One contrasting accent
- Neutral grays from main color (not pure gray)
```

## Layout Principles

```
Create tension:
- Asymmetric balance
- One large + several small
- Break the grid intentionally

Whitespace:
- More than you think
- Consistent spacing scale (8px base)
- Let elements breathe

Hierarchy:
- One focal point per view
- Clear visual path
- Size and weight show importance
```

## Motion Guidelines

```
Micro-interactions: 150-300ms
Page transitions: 300-500ms

Timing functions:
- ease-out: entering elements
- ease-in: exiting elements
- ease-in-out: moving elements

Purpose:
- Provide feedback (button press)
- Show relationships (expand/collapse)
- Guide attention (new content)
- Add delight (sparingly)

Avoid:
- Motion for motion's sake
- Slow animations (> 500ms for simple actions)
- Animations that block interaction
```

## Quick Checks

```
Before shipping UI:
[ ] Font choice is INTENTIONAL (not default)
[ ] Color palette has ONE dominant color
[ ] Layout has some asymmetry or tension
[ ] Spacing is consistent (using scale)
[ ] Interactive elements look clickable
[ ] Would a designer be proud of this?
[ ] Passes squint test (hierarchy clear when blurred)
```

## Responsive Approach

```
Mobile-first:
- Design for 375px first
- Add complexity for larger screens
- Touch targets: 44px minimum

Breakpoints (typical):
- 640px: Large phones, small tablets
- 768px: Tablets
- 1024px: Small laptops
- 1280px: Desktops
- 1536px: Large desktops

Don't:
- Hide important content on mobile
- Make touch targets too small
- Use hover-only interactions
```
