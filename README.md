# ENDLINE

ENDLINE is a GenLayer-powered software dependency lifecycle registry. It turns live public evidence into consensus-backed lifecycle records for packages, APIs, SDKs, models, protocols, and services.

**Live app:** https://the-edl.vercel.app  
**Network:** GenLayer Studionet (`61999`)  
**Canonical contract:** `0x1C3B33d97096ED9DCBc91C6B7f321395507fC739`  
**Deployment transaction:** `0xaa37c9a7a98e74cf278b83a22c63279569182ef0ef4b5a8505ee0eda750ec4aa`

## The problem

Software dependencies change over time. A version can move from active support to deprecation, security-only maintenance, replacement, or end-of-life, but those facts are usually scattered across release notes, support pages, migration notices, and vendor documentation.

A normal database can store a lifecycle label, but it does not prove how that label was derived or whether multiple independent evaluators agreed on the evidence.

ENDLINE uses GenLayer to make that decision process part of the application itself.

## What ENDLINE does

A user registers a dependency together with one to three public HTTPS evidence sources. Anyone can then request a lifecycle assessment.

ENDLINE's Intelligent Contract:

1. reads the registered public web evidence,
2. treats page content and metadata as untrusted data,
3. classifies the tracked version using GenLayer nondeterministic execution,
4. has validators independently evaluate the same lifecycle question,
5. commits an assessment only when consensus succeeds, and
6. preserves the previous canonical state when consensus does not close.

Supported lifecycle statuses are:

- `ACTIVE`
- `DEPRECATED`
- `SECURITY_ONLY`
- `END_OF_LIFE`
- `REPLACED`
- `UNKNOWN`

Evidence quality is also recorded as `SUFFICIENT`, `AMBIGUOUS`, or `INSUFFICIENT`.

## Why GenLayer is necessary

Lifecycle classification is not always a deterministic lookup. Public sources can use different terminology, a retirement date may need to be interpreted in context, and evidence can conflict or be incomplete.

ENDLINE uses GenLayer for the parts that require live web access and subjective reasoning while keeping the accepted state transition deterministic and auditable.

Consensus-critical fields include:

- lifecycle `status`
- `reason_code`
- `evidence_state`
- `effective_date` when the lifecycle decision depends on a date
- `replacement` when the canonical status is `REPLACED`

Descriptive fields such as `summary`, `migration_required`, `breaking_change`, and supplementary replacement metadata do not unnecessarily block consensus when the core lifecycle conclusion agrees.

## Versioned evidence and stale assessments

Evidence is versioned rather than overwritten silently.

Each dependency begins with `SourceSet v1`. When the creator updates its evidence URLs, ENDLINE creates a new immutable source-set version and the previous assessment becomes stale.

The workflow is therefore:

`register -> assess -> update evidence -> stale -> reassess -> current`

An assessment records the source version it evaluated, so reviewers and applications can tell exactly which evidence set produced a lifecycle result.

## State model

ENDLINE stores three primary record types:

### Dependency

The current registry entry, including identity, creator, tracked version, current source version, current lifecycle state, assessment sequence, and freshness.

### SourceSet

An immutable snapshot of the one to three evidence URLs used for a particular source version.

### Assessment

A consensus-backed lifecycle decision tied to a dependency, assessment sequence, and source version.

Canonical keys are publisher-scoped. ENDLINE derives identity from `sender_address + canonical_key`, so two different publishers can register the same canonical key while one publisher cannot register the same key twice.

## Safety and trust boundaries

ENDLINE deliberately treats external evidence as untrusted input.

- sources must use public HTTPS URLs,
- localhost, `.local`, private, loopback, link-local, unspecified, multicast, and reserved literal IP destinations are rejected,
- credentials embedded in source URLs are rejected,
- rendered evidence is bounded before classification,
- prompts explicitly state that webpage text and dependency metadata are data rather than instructions,
- lifecycle output must satisfy deterministic compatibility invariants before storage,
- `UNKNOWN / AMBIGUOUS` and `UNKNOWN / INSUFFICIENT` cannot carry contradictory lifecycle metadata,
- state is written only after GenLayer consensus succeeds, and
- a failed or inconclusive assessment does not increment assessment history or replace the previous lifecycle state.

## Frontend transaction lifecycle

The frontend uses an injected EIP-1193 wallet and talks directly to GenLayer Studionet. There is no application backend, database, indexer, cron worker, or server-side adjudication service.

For writes, ENDLINE does not treat the first receipt object as the sole source of truth. After finality it performs bounded authoritative contract-state readback. This prevents temporary RPC/indexing lag from showing a successful registration or assessment as a false failure.

Registration, source updates, and assessments are reconciled against canonical onchain state before the UI reports success.

## Reviewer path

A reviewer can exercise the complete product flow from the live app:

1. Open https://the-edl.vercel.app and connect an injected wallet on GenLayer Studionet.
2. Open **Register** and enter a dependency, tracked version, canonical key, and one to three authoritative HTTPS sources.
3. Submit the registration and wait for ENDLINE to route to the new record after authoritative readback.
4. Click **Run fresh assessment** and wait for GenLayer consensus and contract-state reconciliation.
5. Confirm the lifecycle status, reason code, assessment sequence, source version, freshness state, and Assessment History entry.
6. Change one or more evidence URLs with **Update sources**. The dependency moves to a newer source version and its previous assessment becomes stale.
7. Run another assessment. The new assessment should bind to the latest source version and return the record to `Current` freshness.

For the cleanest lifecycle evidence, prefer authoritative pages that are specific to the tracked version. Broad aggregate release pages are valid evidence, but version-specific release/support pages reduce ambiguity between multiple lifecycle states shown on the same page.

## Development

```bash
cd frontend
npm install
npm run dev
```

Set the production or local contract address with:

```text
NEXT_PUBLIC_ENDLINE_CONTRACT=<deployed-contract-address>
```

The frontend uses GenLayer Studionet chain ID `61999` and `https://studio.genlayer.com/api` by default.

## Verification

Contract checks:

```bash
genvm-lint lint contracts/endline.py
genvm-lint validate contracts/endline.py
genvm-lint schema contracts/endline.py --output artifacts/endline.schema.json --json
genvm-lint typecheck contracts/endline.py
pytest tests/direct -v
```

Frontend checks:

```bash
npm ci --prefix frontend
npm run typecheck --prefix frontend
ESLINT_USE_FLAT_CONFIG=false npm run lint --prefix frontend
npm test --prefix frontend
npm run build --prefix frontend
```

The same contract and frontend gates run in GitHub Actions. Exact release hashes, lifecycle transactions, parity checks, audit disposition, and CI evidence are maintained in [`RELEASE_EVIDENCE.md`](./RELEASE_EVIDENCE.md).

## Release status

The current canonical Studionet contract is:

`0x1C3B33d97096ED9DCBc91C6B7f321395507fC739`

The deployed frontend is:

https://the-edl.vercel.app

The canonical release has verified source parity and a completed lifecycle proof covering registration, assessment, evidence-source update, reassessment, immutable SourceSet history, and stale-to-current freshness transitions. See [`RELEASE_EVIDENCE.md`](./RELEASE_EVIDENCE.md) for the detailed release record.
