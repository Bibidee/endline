# ENDLINE — Deployment & Release

## Target progression

Recommended:

```text
local development
→ Studionet
→ production-like GenLayer testnet validation
```

Studionet values checked from current GenLayer docs:

```text
GenLayer RPC: https://studio.genlayer.com/api
Chain ID:     61999
Currency:     GEN
Explorer:     https://explorer-studio.genlayer.com
```

## Environment

Example frontend env:

```bash
NEXT_PUBLIC_GENLAYER_RPC=https://studio.genlayer.com/api
NEXT_PUBLIC_GENLAYER_CHAIN_ID=61999
NEXT_PUBLIC_ENDLINE_CONTRACT=0x...
```

Do not commit secrets.

The injected-wallet browser path should not require a private key.

## Contract verification sequence

Before deployment:

1. lint exact contract source;
2. generate/check schema;
3. run direct tests;
4. confirm only intended deployable contract exists in submission path;
5. record source commit hash.

After deployment:

1. record contract address;
2. open Explorer;
3. compare deployed source with final local source where tooling supports it;
4. execute real registration;
5. execute real assessment;
6. record transaction hashes in `HANDOFF.md`.

## Frontend deployment

Vercel is fine for the static/server-rendered frontend surface, but do not add server-side adjudication routes.

If Next.js is used:
- keep chain access in client modules where injected wallet is required;
- avoid API routes for evidence;
- environment variable for contract address;
- production build must pass before deployment.

Current release alias: https://the-edl.vercel.app. Vercel Deployment Protection / SSO has been disabled for the production project; unauthenticated checks of `/`, `/about`, `/register`, and `/d/1` passed.

## Wallet flow

Expected browser flow:

```text
detect injected provider
→ request accounts
→ inspect chain
→ switch/add GenLayer network if required
→ create GenLayer client/provider integration
→ submit write
→ wait for finality
→ authoritative readback
```

No Snap-specific RPC should be required for the normal injected-wallet path.

## Release evidence

Create `HANDOFF.md` containing:

```text
Repository:
Commit:
Frontend:
Network:
Chain ID:
Contract:
Explorer:
Registration tx:
Assessment tx:
Source-update tx:
Second assessment tx:
Tests:
Known limitations:
```

## Known limitations to disclose

- configured sources are selected by registrants;
- source ownership is not cryptographically certified in MVP;
- webpages can change or become inaccessible;
- the canonical status becomes stale until a new assessment is run;
- validator consensus reduces unilateral interpretation but does not make web evidence infallible;
- Studionet is a development environment and should not be represented as production mainnet.

## Official references

- https://docs.genlayer.com/developers/networks
- https://docs.genlayer.com/developers/intelligent-contracts/tooling-setup
- https://docs.genlayer.com/developers/intelligent-contracts/deploying
- https://docs.genlayer.com/developers/intelligent-contracts/features/web-access
