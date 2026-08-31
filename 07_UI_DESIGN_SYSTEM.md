# ENDLINE — UI Design System

## Design direction

**Reference aesthetic: technical registry + standards manual + infrastructure console.**

It should feel intentionally designed by a product designer, not generated from a generic “web3 AI SaaS” prompt.

## Visual personality

Keywords:

- archival
- engineered
- restrained
- legible
- versioned
- slightly industrial
- documentation-first
- trustworthy

## Explicit anti-pattern list

Do **not** use:

- purple/blue AI gradients;
- glowing blobs;
- aurora backgrounds;
- glassmorphism;
- frosted cards;
- excessive rounded corners;
- every section inside a card;
- giant hero headline occupying half the viewport;
- robot/brain/sparkle artwork;
- floating 3D icons;
- neon cyberpunk treatment;
- fake terminal typing animation;
- decorative blockchain hexagons;
- “Ask AI” chat box;
- generic dashboard metric cards across the top;
- excessive pill badges;
- gradients inside buttons;
- random icon next to every label.

## Palette

Use a small, print-inspired palette.

Suggested:

```text
Paper       #F2F0E8
Ink         #171715
Muted Ink   #67655E
Rule        #CBC7BA
Registry    #1F5A44
Warning     #A85D20
Critical    #9A3324
Panel       #E7E3D7
```

One accent at a time.

Status colours must never be the only way status is conveyed.

## Typography

Use one sans family plus one mono family at most.

Good direction:
- sans: a neutral grotesk/system sans;
- mono: system monospace for keys, versions, hashes and machine-readable values.

Do not use five font weights.

Suggested hierarchy:

```text
Page code/eyebrow    11–12px mono uppercase
Page title           30–40px sans medium
Section heading      14–16px sans semibold
Table                13–14px
Metadata             12px mono
Body                 15–16px
```

## Shape language

- 0–6px corner radius.
- Tables and rule lines should do most grouping.
- Use borders before shadows.
- Shadows only for overlays/dialogues.
- Buttons may be rectangular rather than pill-shaped.

## Core signature element: Lifecycle Stamp

Give Endline one ownable visual device.

Example:

```text
┌──────────────────────┐
│  STATUS / DEPRECATED │
│  SOURCE VERSION 03   │
│  ASSESSMENT 0007     │
└──────────────────────┘
```

This can appear on dependency detail pages and exported screenshots.

It should look like an archival inspection stamp, not a colourful badge.

## Core signature element: Endline Rule

At the top of key pages use a thin horizontal rule containing registry metadata:

```text
ENDLINE  /  REGISTRY  /  STUDIONET 61999  /  RECORD 0042
────────────────────────────────────────────────────────
```

This gives the product a recognisable identity without illustrations.

## Registry table

Table is the hero.

Use:
- sticky header on desktop;
- strong row hover;
- status word at left;
- dependency name as primary text;
- version and canonical key in mono;
- no card wrapper unless necessary.

## Status presentation

Use full words in important contexts.

Example:

```text
DEPRECATED
retirement announced
```

Do not reduce everything to tiny coloured chips.

## Buttons

Primary:

```text
RUN ASSESSMENT
REGISTER DEPENDENCY
```

Secondary:

```text
COPY JSON
EDIT SOURCES
```

Use text labels. Icons can support, not replace, important actions.

## Forms

Labels always above fields.

Source URL inputs should look like technical references:

```text
SOURCE / 01
https://...
```

Avoid floating labels.

## Motion

Motion should communicate state only.

Allowed:
- subtle row highlight;
- progress step transition;
- collapse/expand;
- 120–180ms hover/focus transitions.

Not allowed:
- continuous floating;
- parallax;
- background animation;
- glowing pulse around AI actions.

## Mobile

On mobile, transform registry rows into structured text blocks separated by rules, not big cards.

Example:

```text
DEPRECATED
Example API
v1 · API
assessed 2h ago
────────────────
```

## Accessibility

- visible keyboard focus;
- minimum 44px primary touch targets;
- labels not placeholders;
- status includes text;
- target WCAG AA contrast;
- respect reduced-motion preferences.

## Screenshot test

Before shipping, take screenshots of:
- registry desktop;
- dependency desktop;
- register desktop;
- registry mobile;
- dependency mobile.

Ask:

> If the GenLayer logo and product name were removed, would this still look like a deliberately designed registry rather than a generic AI dashboard?

If the answer is no, revise.
