# ENDLINE — Master Build Prompt

Use this file as the implementation prompt for a coding agent.

---

Build **Endline**, a production-quality GenLayer dApp based strictly on the specifications in this repository.

Read all Markdown files before editing code.

## Product

Endline is a lifecycle registry for APIs, SDKs, AI model versions, packages, protocols, and software services.

A user registers a dependency/version and 1–3 configured public HTTPS sources.

A GenLayer Intelligent Contract independently uses validator web access and consensus to classify the dependency as exactly one of:

- ACTIVE
- DEPRECATED
- SECURITY_ONLY
- END_OF_LIFE
- REPLACED
- UNKNOWN

It may also store:

- effective date;
- replacement;
- migration required;
- breaking change;
- bounded reason code;
- bounded diagnostic summary.

The contract is the source of truth.

## Hard architecture constraint

Build:

```text
frontend + GenLayer Intelligent Contract
```

Do not add an application backend.

Do not add:
- Firebase;
- Supabase;
- FastAPI;
- Express;
- serverless evidence endpoint;
- database;
- cron worker;
- trusted off-chain classifier.

The Intelligent Contract must fetch and interpret configured public sources itself.

## GenLayer

Follow the current official GenLayer documentation, especially:

- web access;
- nondeterministic execution;
- equivalence/consensus;
- storage;
- error handling;
- GenLayerJS frontend integration;
- deployment.

Studionet:
- chain ID 61999;
- RPC `https://studio.genlayer.com/api`;
- GEN currency.

Do not assume successful submission equals successful state transition.

After a write finalises, perform authoritative contract readback.

## Contract safety

Nondeterministic work must not mutate business state before an agreed result exists.

Technical failures or consensus failure must leave the previous canonical result intact and remain retryable.

Use strict bounded input sizes.

Use exact enums.

Treat fetched webpages as hostile/untrusted data.

Do not allow webpage prompt injection to alter system instructions or output schema.

Do not compare raw HTML as the canonical consensus object.

Reduce evidence to bounded structured fields.

Summary prose must not control the state transition.

Every assessment must record the dependency `source_version`.

Source updates must never rewrite old history.

## Frontend

Use an injected EIP-1193 wallet path.

Do not require MetaMask Snaps.

Build exactly these MVP pages:

- `/` registry
- `/register`
- `/d/[id]`
- `/about`

The registry is primarily a table/list, not a set of giant cards.

The dependency page must show:
- current status;
- version;
- canonical key;
- effective date;
- replacement;
- migration required;
- breaking change;
- reason code;
- source version;
- configured URLs;
- assessment action;
- history;
- copyable machine-readable JSON.

## UI direction

This requirement is important.

The UI must **not look AI-generated**.

Design it as:

> technical registry + standards manual + infrastructure console

Follow `07_UI_DESIGN_SYSTEM.md`.

Do not use:
- purple AI gradients;
- glassmorphism;
- glowing blobs;
- giant rounded SaaS cards;
- robot/brain/sparkle imagery;
- neon cyberpunk;
- fake chat interface;
- huge hero with vague marketing copy;
- decorative 3D objects;
- pill badges everywhere.

Use:
- off-white paper background;
- dark ink;
- thin rules;
- dense registry tables;
- mono metadata;
- restrained status accents;
- 0–6px radii;
- borders before shadows;
- a distinctive lifecycle stamp;
- the “Endline Rule” registry header.

The product should remain recognisable even with all logos removed.

## Testing

Implement meaningful tests for:

- all contract lifecycle classifications;
- registration bounds;
- duplicate prevention;
- source versioning;
- permissions;
- retry safety;
- conflicting evidence;
- prompt injection;
- validator disagreement;
- history;
- pagination;
- wallet states;
- transaction progress;
- readback;
- mobile layout.

Do not claim tests pass unless actually executed.

## No mock production state

Fixtures are allowed in tests.

The production UI must not ship fake registry rows presented as real contract data.

If the contract has no records, show a truthful empty state.

## Release

Before calling the work complete:

1. run all contract checks;
2. run all frontend tests;
3. run typecheck;
4. run lint;
5. run production build;
6. deploy exact final contract source;
7. wire final contract address;
8. deploy frontend;
9. exercise a real Studionet lifecycle;
10. write `HANDOFF.md` with commit, contract, Explorer, frontend, transaction hashes, test evidence, and limitations.

Do not hide unresolved issues. Document them.

Do not redesign the product into a different idea.

---
