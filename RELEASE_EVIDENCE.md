# ENDLINE Release Evidence

Repository: https://github.com/Bibidee/endline

Frozen contract/code baseline: `26204f2c803f082f4b5ffac1a5b53dd356901426`.

Final repository release HEAD before this closure pass: `a0950e9cbabdcd32c010d039fb8cc9d9682a6bb0`.

Most recent fully verified CI before this closure pass: [run 33442725166](https://github.com/Bibidee/endline/actions/runs/33442725166) — completed / success.

## Frozen Studionet contract parity

- Contract source changed in the hardening pass: **NO**.
- SHA-256: `1BB6D7DBE96DD25B450F347BEAA67EA5BE08D8C9A298EA8B5F098A52CD89167B`.
- Runtime dependency: `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`.
- Studionet contract: `0xAC619CE31aD990C77b988308Ab101282FE75A22E`.
- Deployment transaction: `0xd4cd8cac1af337ea3aafc21d04b600dd48dce66d7fa1120353135e9cf3913b72`.

The final contract file remains byte-identical to the deployed source revision; no redeployment is required for this release-hygiene change.

## Verified lifecycle

All transactions finalized with majority agreement and successful execution.

- Registration: `0x3b9dac2cc9d81af034cbd35da31e2b016d9bcc2265c7eb15da217ffed0afa82f`
- Assessment 1: `0x9ab09a404536d88c5c43a13cd5a8fd82c33963d495a8a163f5d1e7ffb9621da0`
- Source update: `0x0495135638d84bf9251faeeb3f263d25988d6213049c42073c98447c0ca670bb`
- Assessment 2: `0xb8c2034bca0d9216837a380ee4836c2a32e58deb4f2ee6fc0f2c79838566ce31`

Authoritative readback: `source_version=2`, `assessment_count=2`, `current_assessment_sequence=2`, `current_assessment_source_version=2`, and `is_stale=false`.

## Verification baseline

GitHub Actions [run 33437277667](https://github.com/Bibidee/endline/actions/runs/33437277667) completed successfully:

- GenVM lint, validate, schema extraction (9 methods), and typecheck: PASS.
- Python/Direct Mode tests: 103/103 PASS.
- Frontend tests: 29/29 PASS.
- Frontend typecheck, lint, and production build: PASS.

Direct Mode covers lifecycle outcomes, invalid classifier output without state mutation, prompt injection, source-version rebinding, and consensus behavior where summary wording is non-critical but lifecycle-field disagreement is rejected.

Release-hygiene verification: GitHub Actions [run 33442376039](https://github.com/Bibidee/endline/actions/runs/33442376039) completed successfully for commit `ea18b0ca62c30e4b1ebc4f4310cd9d700d7cd22a`, including every contract and frontend release-gate step. The documentation-only follow-up run 33442725166 also passed for `a0950e9cbabdcd32c010d039fb8cc9d9682a6bb0`.

## Frontend release

Live production alias: https://the-edl.vercel.app

The Vercel deployment is built successfully and Vercel SSO Deployment Protection is disabled for the production project. Unauthenticated HTTP checks verified the homepage, `/about`, `/register`, and `/d/1` return the ENDLINE application without Vercel login or access-protection content.

## npm security disposition

After targeted upgrades, `sharp` is pinned at `^0.35.0` (resolved through Next.js to 0.35.4) and Vitest is updated to 2.1.9. `npm audit --omit=dev` has no critical findings and retains one high / one moderate advisory in Next.js's bundled PostCSS 8.4.31. The audit offers only Next 16.3.4, a major framework upgrade, as a fix; this release does not force that untested breaking change.

The full audit retains one critical and one high in dev-only Vitest/Vite tooling. The critical advisory requires a Vitest UI/API server; ENDLINE runs `vitest run` only and ships no Vitest/Vite code. Remediation requires Vitest 4, a major tooling upgrade, so it is documented rather than silently forced. No high or critical advisory is in the deployed application runtime apart from Next's transitive PostCSS path above.
