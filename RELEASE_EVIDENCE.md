# ENDLINE Release Evidence

Repository: https://github.com/Bibidee/endline

## Frozen canonical contract

- Contract-changing commit: `adfde5288f514f1288a1fcfe15cf74ef2bb60a1e`
- Final repository HEAD before this documentation closeout: `373ba892355302affe4d7d2e07be6e02074bc21c`
- Contract SHA-256: `CFA705BF7FB8BB7E6512CC85FB15CEC2729C0E110B665FCD411B58C5CD605E0B`
- Studionet contract: `0x05B8B436CdA0b32f56f2C7F2d57da224c374C7D3`
- Deployment transaction: unavailable from retained CLI output; deployed source was retrieved with `genlayer code` and matches repository source content.
- Network: GenLayer Studionet, chain ID `61999`, RPC `https://studio.genlayer.com/api`

The prior `0xAC619CE31aD990C77b988308Ab101282FE75A22E` and intermediate `0x5daDdb8AB4499d4E5a4a895a9a2202790ef9D3fb` deployments are superseded historical deployments.

## Lifecycle evidence

- Registration: `0x71a5d68c366f165e1f83dd8151f5a535344406a85a1dc0d033454ea4635a80fe`
- Assessment 1: `0x9b6c07ad756e56f13ffaffe5111782e34286145f9b737bdb0a83cd44d5d20439`
- Source update: `0x02ce8e4ba21ab9e884ea7b8fc4abed04b6059658d7c8f217cc7ab5fbc082fd30`
- Failed source-v2 assessment: `0xfd3a340184662a3cf56f0fec9122f197ebf8af6da2b4b5a809ab57efb6f32317` — FINALIZED / MAJORITY_DISAGREE; no state mutation.
- Successful source-v2 retry: `0xdae8d5b9cc2adb653e396d725405abf094c0f2be7c199509804e63697c5a0bdf` — FINALIZED / MAJORITY_AGREE / successful execution.

Final authoritative state: `source_version=2`, `assessment_count=2`, `current_assessment_sequence=2`, `current_assessment_source_version=2`, `is_stale=false`. Assessment 1 uses source version 1; Assessment 2 uses source version 2; SourceSets 1 and 2 are preserved.

## Verification

- GenVM lint, validate, schema, typecheck: PASS
- Python Direct Mode suite: 116/116 PASS (behavioural contract cases plus deterministic policy/helper cases)
- Frontend tests: 29/29 PASS
- Frontend typecheck, lint (zero warnings), production build: PASS
- CI before this closeout: [33456733686](https://github.com/Bibidee/endline/actions/runs/33456733686) — SUCCESS

## Live frontend

Production deployment: `dpl_DRRApkKpx4wsVkNmeKTh36v5XgnU`

Production alias: https://the-edl.vercel.app

Production is configured with `NEXT_PUBLIC_ENDLINE_CONTRACT=0x05B8B436CdA0b32f56f2C7F2d57da224c374C7D3`, chain ID `61999`, and the Studionet RPC. Unauthenticated smoke checks of `/`, `/about`, `/register`, and `/d/1` returned HTTP 200 and rendered ENDLINE.

## npm security disposition

`npm audit --omit=dev --prefix frontend`: 2 advisories (1 moderate, 1 high), both transitive PostCSS used by Next.js. The available fix requires the breaking Next.js 16 upgrade; no safe non-breaking patch is available in the current verified release.

Full audit: 7 advisories (4 moderate, 2 high, 1 critical). Additional esbuild/Vite/Vitest findings are dev-only tooling; ENDLINE does not ship or expose a Vite/Vitest server. Remediation requires a breaking Vitest upgrade and was not applied blindly.
