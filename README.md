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

`npm run typecheck`, `npm run lint`, `npm test`, `npm run build`, and from the repository root `python -m unittest discover -s tests/direct`.

## Status

Deployment requires a configured GenLayer CLI account and injected wallet. No deployment address or transaction hashes are claimed until a real Studionet lifecycle is executed.
