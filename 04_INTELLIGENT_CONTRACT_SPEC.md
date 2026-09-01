# ENDLINE — Intelligent Contract Specification

## Contract name

`EndlineRegistry`

Suggested source:

`contracts/endline.py`

## Design principle

Use nondeterminism only to observe and interpret external evidence.

Everything that can be deterministic should remain deterministic:

- admission rules;
- state transitions;
- enums;
- string bounds;
- counters;
- IDs;
- permissions;
- source-version logic;
- history ordering;
- derivation rules where possible.

## Storage

Suggested conceptual structures:

### Dependency

```text
id: uint
creator: address
name: string
kind: string enum
tracked_version: string
canonical_key: string
source_urls: bounded list[string]
source_version: uint
created_at: uint
current_status: string enum
current_effective_date: string
current_replacement: string
current_migration_required: bool
current_breaking_change: bool
current_reason_code: string enum
assessment_count: uint
```

### Assessment

```text
dependency_id: uint
sequence: uint
requested_by: address
requested_at: uint
source_version: uint
status: enum
effective_date: string
replacement: string
migration_required: bool
breaking_change: bool
reason_code: enum
evidence_state: enum
summary: bounded diagnostic string
```

## Suggested hard bounds

- dependencies per deployment: 512
- assessments per dependency: 32
- source URLs per dependency: 3
- name: 120 chars
- tracked version: 80 chars
- canonical key: 180 chars
- URL: 500 chars
- replacement: 160 chars
- diagnostic summary: 320 chars

If GenVM/runtime constraints require smaller values, prefer lowering them.

## Public write methods

### `register_dependency(...)`

Arguments:

```text
name
kind
tracked_version
canonical_key
source_urls
```

Requirements:

- caller is captured as creator;
- `kind` is valid enum;
- canonical key normalisation policy is deterministic;
- canonical key is unique;
- 1–3 sources;
- sources are HTTPS;
- reject credentials in URL;
- reject obvious local/private hosts;
- strings within bounds.

Effects:

- allocate ID;
- set `source_version = 1`;
- set current lifecycle to `UNKNOWN`;
- assessment count zero.

### `update_sources(dependency_id, source_urls)`

Authority:
- creator only for MVP.

Effects:
- validate full replacement set;
- increment source version;
- do not delete history;
- do not silently reclassify lifecycle status.

Optional policy:
- mark the current result as “based on previous source version” in view data rather than erasing it.

### `assess_dependency(dependency_id)`

Authority:
- permissionless.

Rules:
- dependency exists;
- source list non-empty;
- no canonical state mutation before agreed nondeterministic result exists.

Nondeterministic work:
- independently fetch configured sources;
- extract stable lifecycle facts;
- classify into exact schema;
- return a bounded envelope.

Consensus:
- compare only state-relevant structured fields.

Post-consensus:
- append assessment;
- update canonical status;
- increment assessment count.

### `get_dependency(id)`

Pure/view.

### `get_assessment(dependency_id, sequence)`

Pure/view.

### `get_assessments(dependency_id, offset, limit)`

Bounded pagination.

### `get_dependency_count()`

Pure/view.

### `get_dependencies(offset, limit)`

Bounded pagination.

## Lifecycle reason codes

Suggested fixed enum:

- `NO_CHANGE_NOTICE`
- `OFFICIAL_DEPRECATION_NOTICE`
- `SECURITY_MAINTENANCE_ONLY`
- `RETIREMENT_ANNOUNCED`
- `RETIREMENT_EFFECTIVE`
- `SUCCESSOR_IDENTIFIED`
- `CONFLICTING_EVIDENCE`
- `INSUFFICIENT_EVIDENCE`
- `UNCLASSIFIED`

Do not let free-form model prose control state.

## Assessment output schema

The model-facing result should collapse into something close to:

```json
{
  "status": "DEPRECATED",
  "effective_date": "2026-10-31",
  "replacement": "v2",
  "migration_required": true,
  "breaking_change": true,
  "reason_code": "OFFICIAL_DEPRECATION_NOTICE",
  "evidence_state": "SUFFICIENT",
  "summary": "Provider documentation states that v1 is deprecated and names v2 as the migration target."
}
```

## Equivalence fields

State-relevant fields:

- `status`
- `effective_date`
- `replacement`
- `migration_required`
- `breaking_change`
- `reason_code`
- `evidence_state`

`summary` is diagnostic only and should not cause disagreement if all state-relevant fields agree.

### Compatibility matrix

- `ACTIVE` requires `NO_CHANGE_NOTICE`, no date/replacement, and both booleans false.
- `DEPRECATED` requires an official deprecation or retirement announcement; retirement announcements may include an effective date and successor/migration metadata.
- `SECURITY_ONLY` requires `SECURITY_MAINTENANCE_ONLY` and no retirement date or replacement.
- `END_OF_LIFE` requires `RETIREMENT_EFFECTIVE` and a valid effective date; successor and migration metadata are allowed.
- `REPLACED` requires `SUCCESSOR_IDENTIFIED` and a non-empty replacement identity.
- `UNKNOWN` is reserved for unclassified, insufficient, or conflicting evidence and cannot carry lifecycle metadata.

Validator equivalence compares status, reason code, evidence state, effective date, and boolean migration/breaking semantics. Replacement text is compared after trimming, collapsing whitespace, and lowercasing; summaries are excluded.

## Failure policy

### Fetch failure
Prefer retryable failure with no mutation.

### Model/parse failure
Prefer retryable failure with no mutation.

### Validators materially disagree
Transaction may become undetermined according to GenLayer consensus behaviour; state must remain safe/retryable.

### Sources are accessible but genuinely ambiguous
Allow:

```text
status = UNKNOWN
evidence_state = AMBIGUOUS
reason_code = CONFLICTING_EVIDENCE or INSUFFICIENT_EVIDENCE
```

That is a valid assessment, not a technical error.

## Time handling

The model may extract an effective date from evidence.

The contract should not let the model invent transaction time.

If the classification depends on whether an announced retirement date has already passed, give the nondeterministic classifier an authoritative/bounded time context from the contract/runtime and make the derived policy explicit.

## Source-update race

Every assessment must store the exact `source_version`.

This prevents a later source edit from making old history appear to have been based on current sources.

## Duplicate identity

Use `canonical_key` to stop obvious duplicates.

Example canonical keys:

```text
openai-api:assistants:v2
example-sdk:python:4.x
some-model:model-name:2026-01
```

The canonical key is supplied by the registrant and enforced unique. Do not attempt universal dependency naming in MVP.
### Liveness equivalence policy

Consensus-critical fields are status, reason_code, evidence_state, lifecycle-critical effective_date, and replacement for REPLACED. Summary, migration_required, breaking_change, and supplementary replacement metadata are advisory and excluded from equivalence. UNKNOWN AMBIGUOUS/INSUFFICIENT results require empty lifecycle metadata.
