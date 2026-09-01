# ENDLINE

ENDLINE is a GenLayer Intelligent Contract plus injected-wallet frontend for consensus-backed software dependency lifecycle records.

## Development

```text
cd frontend
npm install
npm run dev
```

Set `NEXT_PUBLIC_ENDLINE_CONTRACT` from a deployed Studionet contract. The frontend uses chain ID `61999` and `https://studio.genlayer.com/api` by default. It does not include a backend, database, indexer, cron worker, or server-side adjudication route.

## Checks

Run `scripts/check.ps1` on Windows, or run `pytest tests/direct -v` plus the frontend npm scripts. The contract gate includes lint, validation, schema extraction, and typecheck.

Canonical keys are unique per publisher: ENDLINE derives identity from `sender_address + canonical_key`, so separate publishers may register the same canonical key.

## Status

The verified Studionet contract is `0x05B8B436CdA0b32f56f2C7F2d57da224c374C7D3`. See `RELEASE_EVIDENCE.md` for finalized lifecycle receipts.

The deployed frontend is https://the-edl.vercel.app. It is built against Studionet and the canonical contract, and public unauthenticated access to the production alias has been verified.

The frozen deployed contract baseline is distinct from the repository release history; the latest verified release evidence and CI links are maintained in `RELEASE_EVIDENCE.md`.
