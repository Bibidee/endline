# ENDLINE — Frontend & UX Specification

## Frontend goal

Make Endline feel like a serious infrastructure registry, not an AI demo.

The product should communicate:

- precision;
- provenance;
- versioning;
- status;
- history;
- machine readability.

It should not lead with “AI”.

## Stack

Suggested:

- Next.js
- TypeScript
- CSS modules, Tailwind, or plain CSS
- `genlayer-js`
- injected EIP-1193 wallet

Avoid adding UI libraries solely to imitate a generic SaaS template.

## Navigation

Desktop:

```text
ENDLINE
Registry
Register
About

                         network · wallet
```

Mobile:
- compact top bar;
- no hidden critical actions behind multiple menus.

## Page: Registry `/`

Primary structure:

```text
ENDLINE / DEPENDENCY REGISTRY

[ search/filter ]          [ Register dependency ]

STATUS     DEPENDENCY        TYPE       VERSION      ASSESSED
ACTIVE     Example API       API        v2           2h ago
DEPR.      Example SDK       SDK        4.x          1d ago
EOL        Example Model     MODEL      2025-11      3d ago
```

Do not use a grid of giant rounded cards.

The registry should be a dense table/list with strong information hierarchy.

Filters:
- status;
- kind.

Search:
- name;
- canonical key;
- version.

## Page: Register `/register`

Fields:

- Name
- Kind
- Tracked version
- Canonical key
- Source URL 1
- Source URL 2
- Source URL 3

UX:
- explain canonical key with one example;
- validate URL format before submit;
- show transaction state;
- after finality, read the new dependency from chain;
- route to detail page.

## Page: Dependency `/d/[id]`

Header:

```text
EXAMPLE API / v1
DEPRECATED
canonical key: example-api:v1
```

Main zones:

### Current lifecycle

A compact status panel containing:

- status;
- effective date;
- replacement;
- migration required;
- breaking change;
- reason code;
- last assessed;
- source version.

### Sources

List each configured source as a numbered reference.

Do not hide URLs behind vague text like “Evidence 1”.

### Assessment action

Primary button:

`RUN FRESH ASSESSMENT`

Transaction feedback:

```text
Submitting
→ Pending consensus
→ Finalised
→ Reading canonical state
→ Updated
```

Never show “Updated” before readback.

### History

Use an audit ledger/table:

```text
#04  DEPRECATED   2026-08-30  source v2
#03  ACTIVE       2026-08-21  source v1
#02  UNKNOWN      2026-08-10  source v1
```

Click/expand reveals structured fields and summary.

### Agent-readable view

A copy button produces a JSON object from current on-chain state.

Example:

```json
{
  "canonical_key": "example-api:v1",
  "status": "DEPRECATED",
  "effective_date": "2026-10-31",
  "replacement": "v2",
  "migration_required": true,
  "breaking_change": true,
  "source_version": 2,
  "assessment_sequence": 4
}
```

Do not call this an API endpoint. It is a copyable representation of contract state.

## Page: About `/about`

Keep it brief.

Explain:

- what is being classified;
- that validators independently inspect configured public sources;
- that the creator selects source URLs;
- that Endline does not certify source ownership;
- that results can become stale until reassessed.

## Empty state

Good:

```text
No dependencies registered yet.
Create the first registry entry.
```

Bad:

- AI-generated illustration;
- robot mascot;
- sparkles;
- huge gradient CTA.

## Loading states

Use restrained skeleton lines or textual progress.

Do not use “thinking…” bubbles.

## Error language

Prefer precise states:

- `Wallet rejected transaction`
- `Source assessment did not converge`
- `Assessment failed before canonical state changed`
- `Network mismatch`
- `Finalised transaction did not produce expected readback`

Avoid vague:
- `Oops! Something went wrong 🤖`
