# ENDLINE — Product Requirements Document

## 1. Objective

Ship a working GenLayer dApp where users can register a software dependency, trigger a validator-consensus lifecycle assessment using public web evidence, and read the canonical result and history.

## 2. Success criteria

The MVP is successful when all of the following work end-to-end:

- injected wallet connects;
- frontend recognises/switches to the configured GenLayer network;
- user registers a dependency;
- dependency becomes readable from contract state;
- assessment triggers real GenLayer nondeterministic web access;
- validators return a bounded structured result;
- result is written only after consensus;
- failures remain retryable or resolve to `UNKNOWN` according to policy;
- history is append-only;
- frontend reads final authoritative state after transaction finalisation;
- production frontend contains no mock registry rows.

## 3. Personas

### Maintainer
Registers dependencies and official evidence sources.

### Consumer
Looks up the current status before integrating a dependency.

### Agent
Reads the canonical structured lifecycle state before choosing a tool/version.

### Independent caller
Triggers a fresh assessment when the stored result may be stale.

## 4. Core entities

### Dependency

Required fields:

- `id`
- `creator`
- `name`
- `kind`
- `tracked_version`
- `canonical_key`
- `source_urls`
- `created_at`
- `current_status`
- `current_effective_date`
- `current_replacement`
- `current_migration_required`
- `current_breaking_change`
- `current_reason_code`
- `assessment_count`
- `source_version`

### Assessment

Required fields:

- `dependency_id`
- `sequence`
- `requested_by`
- `requested_at`
- `source_version`
- `status`
- `effective_date`
- `replacement`
- `migration_required`
- `breaking_change`
- `reason_code`
- `evidence_state`

## 5. Dependency kinds

MVP enum:

- `API`
- `SDK`
- `MODEL`
- `PACKAGE`
- `PROTOCOL`
- `SERVICE`
- `OTHER`

Do not let the model invent kinds.

## 6. Lifecycle statuses

MVP enum:

### ACTIVE
The tracked dependency/version remains supported according to available configured evidence.

### DEPRECATED
Use is discouraged or retirement has been announced, but it is not yet clearly end-of-life.

### SECURITY_ONLY
The dependency remains maintained only for security/critical fixes or equivalent restricted support.

### END_OF_LIFE
The tracked version/service is no longer supported or its official retirement date has passed.

### REPLACED
The configured evidence clearly identifies another version/product/API as the intended replacement.

### UNKNOWN
The evidence is accessible but does not support a safe classification.

Technical fetch/model failures should be distinguished from a legitimate `UNKNOWN` assessment whenever the runtime permits a retryable failure without state mutation.

## 7. Core user stories

### Register

As a maintainer, I can register a dependency with 1–3 HTTPS evidence sources.

Acceptance:
- duplicate canonical keys rejected;
- invalid/unsafe URL forms rejected;
- bounded strings;
- source list immutable for that version.

### Update sources

As the dependency creator, I can replace the evidence source set.

Acceptance:
- increments `source_version`;
- previous assessment history remains intact;
- future assessments reference the new source version.

### Assess

As any wallet, I can request lifecycle assessment.

Acceptance:
- validators independently fetch sources;
- output follows exact schema;
- consensus comparison uses settlement/state-relevant fields;
- no pre-consensus mutation of canonical lifecycle state.

### View status

As any user or agent, I can read the canonical current record without triggering a model call.

### View history

As any user, I can inspect prior assessments in order.

## 8. Pages

### `/`
Registry dashboard.

### `/register`
Dependency registration form.

### `/d/[id]`
Dependency detail and assessment history.

### `/about`
Short explanation of what Endline proves and what it does not prove.

No additional pages required for MVP.

## 9. Non-functional requirements

### Correctness
State changes must never rely on frontend assumptions.

### Boundedness
All arrays and strings need hard caps.

### Retry safety
A failed or undetermined assessment must not corrupt the last canonical result.

### Source transparency
Every lifecycle record must expose the URLs used for its source version.

### No fake authority
The MVP does not cryptographically prove that a URL belongs to an official vendor. The UI must say “configured sources”, not “verified official sources”, unless such verification is actually implemented.

### Accessibility
Keyboard navigation, visible focus states, semantic labels, sufficient contrast.

### Responsive behaviour
Desktop-first registry UI, fully usable on mobile.

## 10. Explicit non-goals

Do not add:

- escrow or token rewards;
- subscriptions;
- user profiles;
- social feeds;
- chat assistant;
- AI chatbot;
- arbitrary URL crawling;
- backend database;
- email alerts;
- browser extension;
- complex DAO governance;
- token economics;
- vector search.

Those can distract from demonstrating the core GenLayer primitive.
