# ENDLINE — Product Brief

## One-line description

**Endline is a consensus-backed lifecycle registry that tells humans and agents whether a software dependency is still supported.**

## Problem

Modern applications and autonomous agents rely on external dependencies:

- APIs
- SDKs
- AI model versions
- package versions
- RPC services
- developer platforms
- protocol endpoints
- third-party integrations

The lifecycle of those dependencies changes constantly.

A provider may announce that:

- a version is deprecated;
- an API will stop accepting requests on a future date;
- a model has been replaced;
- a library enters security-only maintenance;
- an endpoint moves;
- a feature becomes unsupported;
- a migration is mandatory.

The evidence is normally fragmented across documentation, migration guides, release notes, status pages, repositories, and provider announcements.

Software can therefore keep relying on something that is technically still reachable but no longer safe to treat as supported.

## Product thesis

A dependency lifecycle should be representable as shared public state.

GenLayer can establish that state without one company maintaining a trusted lifecycle database.

Validators independently inspect the configured public sources and agree on a bounded result.

## Target users

### Human users

- developers
- engineering teams
- open-source maintainers
- DevOps teams
- security teams
- protocol teams
- DAO technical contributors

### Machine users

- autonomous coding agents
- procurement agents
- deployment agents
- monitoring agents
- migration agents
- application agents selecting tools dynamically

## MVP use case

A developer registers:

- dependency name: `Example API`
- type: `API`
- tracked version: `v1`
- official documentation URL
- changelog URL
- migration/support-policy URL

Anyone may trigger an assessment.

GenLayer validators independently fetch the allowed sources and return a structured conclusion.

Example:

```json
{
  "status": "DEPRECATED",
  "effective_date": "2026-10-31",
  "replacement": "v2",
  "migration_required": true,
  "breaking_change": true,
  "reason_code": "OFFICIAL_DEPRECATION_NOTICE"
}
```

The contract writes that canonical result to the dependency record and appends a lifecycle history entry.

## Why GenLayer is necessary

A deterministic smart contract cannot reliably decide that a natural-language release note means:

> “This version is deprecated now and will stop working on 31 October.”

A traditional off-chain service could make that decision, but then users must trust that service.

Endline instead makes the interpretation a validator-consensus problem.

## What Endline is not

Endline is not:

- uptime monitoring;
- SLA enforcement;
- escrow;
- a bounty system;
- milestone verification;
- code review;
- a vulnerability scanner;
- a package manager;
- a prediction market;
- a generic semantic search engine;
- a dispute court;
- a web scraper dashboard.

Its core primitive is:

> **Canonical lifecycle classification of a named dependency/version from configured public evidence.**

## Long-term expansion

After the MVP, Endline could add:

- dependency watchlists;
- machine-readable status attestations;
- migration recommendations;
- dependency graph impact analysis;
- “safe replacement” comparisons;
- agent policies such as “do not use deprecated dependencies”;
- cross-project exposure views;
- signed registry snapshots.

Do not build those before the MVP is complete and proven on-chain.
