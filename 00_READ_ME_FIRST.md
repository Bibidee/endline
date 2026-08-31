# ENDLINE — Builder Pack

## What this is

Endline is a GenLayer-native lifecycle registry for APIs, SDKs, AI models, packages, protocols, and other software dependencies.

It answers one practical question:

> Is this dependency still active and supported, or has it been deprecated, replaced, restricted, or ended?

The product is deliberately scoped to **an Intelligent Contract + frontend only**.

There is **no application backend**, no database server, no cron worker, and no trusted off-chain adjudicator.

The Intelligent Contract:
- stores registered dependencies and lifecycle history;
- fetches approved public sources itself;
- asks validators to independently interpret those sources;
- reaches consensus on a small structured lifecycle result;
- writes the canonical result on-chain.

The frontend:
- connects through an injected EIP-1193 wallet;
- reads directly from the contract;
- submits contract writes;
- displays registry state and assessment history.

## Core MVP

A user can:

1. connect an injected wallet;
2. register a dependency;
3. provide up to 3 official/public lifecycle sources;
4. trigger an assessment;
5. wait for GenLayer finality;
6. view the canonical lifecycle status;
7. inspect the evidence URLs and assessment history;
8. copy an agent-readable status object.

### Canonical statuses

- `ACTIVE`
- `DEPRECATED`
- `SECURITY_ONLY`
- `END_OF_LIFE`
- `REPLACED`
- `UNKNOWN`

## Hard constraints

- GenLayer Intelligent Contract is the source of truth.
- Frontend + contract only.
- No Firebase, Supabase, Express, FastAPI, serverless API routes, cron jobs, or indexer required for the MVP.
- Public HTTPS sources only.
- The contract must fail safely when sources cannot be interpreted.
- Never turn a fetch/model failure into a confident lifecycle status.
- Keep consensus fields small and categorical.
- Do not compare raw HTML under strict equality.
- No MetaMask Snaps dependency.
- Injected wallet path first.
- Studionet target for collaborative testing: chain ID `61999`.
- Do not treat a submitted transaction as successful until final state is read back from the contract.

## Suggested build order

1. `01_PRODUCT_BRIEF.md`
2. `02_PRD.md`
3. `03_ARCHITECTURE.md`
4. `04_INTELLIGENT_CONTRACT_SPEC.md`
5. `05_CONSENSUS_EVIDENCE_SPEC.md`
6. `06_FRONTEND_UX_SPEC.md`
7. `07_UI_DESIGN_SYSTEM.md`
8. `08_TEST_PLAN.md`
9. `09_DEPLOYMENT_RELEASE.md`
10. `10_AGENT_BUILD_PROMPT.md`

## Official GenLayer references

- Web access: https://docs.genlayer.com/developers/intelligent-contracts/features/web-access
- Networks: https://docs.genlayer.com/developers/networks
- Tooling setup: https://docs.genlayer.com/developers/intelligent-contracts/tooling-setup
- Deploying: https://docs.genlayer.com/developers/intelligent-contracts/deploying

These docs were checked against the public GenLayer documentation on 30 August 2026.
