# ENDLINE Release Evidence

Repository: https://github.com/Bibidee/endline

## Frozen canonical contract

- Contract-changing commit: `adfde5288f514f1288a1fcfe15cf74ef2bb60a1e`
- Final repository HEAD before this documentation closeout: `373ba892355302affe4d7d2e07be6e02074bc21c`
- Superseded historical SHA-256: `CFA705BF7FB8BB7E6512CC85FB15CEC2729C0E110B665FCD411B58C5CD605E0B`
- Current contract SHA-256: `F1584820F3B20E2DE1A1D6B495A8CADBA6B8D3D7BE46E12DC968B16E6209872F`
- Current Studionet contract: `0x1C3B33d97096ED9DCBc91C6B7f321395507fC739`
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
## Corrective liveness release

Canonical Studionet contract: `0x1C3B33d97096ED9DCBc91C6B7f321395507fC739`.

Contract SHA-256: `F1584820F3B20E2DE1A1D6B495A8CADBA6B8D3D7BE46E12DC968B16E6209872F`.

Deployment transaction: `0xaa37c9a7a98e74cf278b83a22c63279569182ef0ef4b5a8505ee0eda750ec4aa`.

Fresh lifecycle: registration `0x53c52d5d80d92e33ad213a0427211af9f53c0b159b58f17ab1f46f85efe4b8b6`; assessment 1 `0x148fb3e16be1f895c9a913cd2781e5a21d8ac97646c9b771cf6d44b9b0422deb`; source update `0xfe045b68a89cf8d74590deeaf3372c89ee16252f1715e0c736da27777aea51d7`; assessment 2 `0xda7ce09792723bf6824a39b472d4d581ec1637cf4aa2a0a9d59e958a3bba0198`.

Final authoritative state: source_version 2, assessment_count 2, current sequence 2, current assessment source version 2, is_stale false. Production frontend is `https://the-edl.vercel.app` and is rebound to the canonical contract.
## Final release hygiene

- Frozen contract SHA verified unchanged: `F1584820F3B20E2DE1A1D6B495A8CADBA6B8D3D7BE46E12DC968B16E6209872F`.
- Independent parity: PASS after normalizing CLI `Result:` wrapper and line endings; normalized deployed source content matched `contracts/endline.py` exactly.
- `npm audit --prefix frontend`: 7 vulnerabilities (4 moderate, 2 high, 1 critical). High/critical findings are PostCSS transitively bundled by Next.js and esbuild/Vite/Vitest development tooling; fixes require breaking Next.js 16/Vitest 4 upgrades, so no force upgrade was applied.
- `npm audit --omit=dev --prefix frontend`: 2 vulnerabilities (1 moderate, 1 high), both PostCSS through Next.js; remediation requires the breaking Next.js 16 upgrade.
- Final cleanup CI is run after this documentation commit.
