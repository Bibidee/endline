# ENDLINE Release Evidence

Repository: https://github.com/Bibidee/endline

## Frozen contract baseline

- Contract baseline: `26204f2c803f082f4b5ffac1a5b53dd356901426`
- Contract SHA-256: `1BB6D7DBE96DD25B450F347BEAA67EA5BE08D8C9A298EA8B5F098A52CD89167B`
- Studionet contract: `0xAC619CE31aD990C77b988308Ab101282FE75A22E`
- Deployment transaction: `0xd4cd8cac1af337ea3aafc21d04b600dd48dce66d7fa1120353135e9cf3913b72`

The deployed contract source remains byte-identical to this frozen baseline. No frontend release documented here changes or redeploys it.

## Verified lifecycle evidence

- Registration: `0x3b9dac2cc9d81af034cbd35da31e2b016d9bcc2265c7eb15da217ffed0afa82f`
- Assessment 1: `0x9ab09a404536d88c5c43a13cd5a8fd82c33963d495a8a163f5d1e7ffb9621da0`
- Source update: `0x0495135638d84bf9251faeeb3f263d25988d6213049c42073c98447c0ca670bb`
- Assessment 2: `0xb8c2034bca0d9216837a380ee4836c2a32e58deb4f2ee6fc0f2c79838566ce31`

Authoritative readback recorded `source_version=2`, `assessment_count=2`, `current_assessment_sequence=2`, `current_assessment_source_version=2`, and `is_stale=false`.

## Latest code-changing frontend release

- Frontend reconstruction commit: `022ee49c1393eceeedb1830e7fc98defc1a98d75`
- Verification: [GitHub Actions run 33449232518](https://github.com/Bibidee/endline/actions/runs/33449232518) — completed / success.

This release reconstructed the frontend interface only. It did not modify the deployed contract, did not require contract redeployment, and preserved the existing GenLayer transaction finality and authoritative-readback semantics.

That run verified GenVM lint, validate, schema extraction, contract typecheck, the pinned GenLayer testing suite, 103/103 Direct Mode tests, frontend typecheck, frontend lint, 29/29 frontend tests, and the production build.

## Live frontend

Production alias: https://the-edl.vercel.app

The Vercel production environment centrally configures `NEXT_PUBLIC_GENLAYER_RPC`, `NEXT_PUBLIC_GENLAYER_CHAIN_ID=61999`, and `NEXT_PUBLIC_ENDLINE_CONTRACT=0xAC619CE31aD990C77b988308Ab101282FE75A22E`. Vercel Deployment Protection is disabled for production. Unauthenticated checks of `/`, `/about`, `/register`, and `/d/1` load the ENDLINE application without a Vercel login prompt.

## npm security disposition

`npm audit --omit=dev` has no critical finding. One high and one moderate advisory remain in Next.js's bundled PostCSS 8.4.31; the offered remediation is a major Next 16 upgrade, which is not forced into this verified release.

The full audit retains one critical and one high advisory in dev-only Vitest/Vite tooling. ENDLINE runs `vitest run` only and ships no Vitest/Vite server or UI. The available remediation requires a major Vitest upgrade, so it is explicitly deferred rather than applied as an unverified breaking change.
