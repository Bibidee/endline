# ENDLINE Release Evidence

Repository: https://github.com/Bibidee/endline
Branch: master
Source commit: e1b27ce5d7bd678127faccd161c7b635cd07c7cd
Contract SHA-256 at audit: F08218B647208EA2779CD8499D94A195097CA10CB1A56B1AC03A229C6C0FBBEC
GenLayer CLI: 0.39.2
genvm-linter: 0.11.0
Node: v22.22.2
Python: 3.12.10
genlayer-test: NOT AVAILABLE as standalone command
genlayer-js: 1.1.8 (frontend dependency)

Contract lint: PASS (warning: bare Exception remains)
Contract validate: BLOCKED — installed validator cannot import `genlayer.py`
Contract schema: BLOCKED — same SDK import failure
Contract typecheck: PASS (0 errors; SDK names reported as unresolved by Pyright)
Direct Mode tests: NOT RUN — no standalone genlayer-test command available
Frontend tests: BLOCKED — Vitest inherits inaccessible parent config path
Frontend typecheck: PASS
Frontend lint: PASS with `ESLINT_USE_FLAT_CONFIG=false`
Frontend production build: PASS
CI: CONFIGURED, not run remotely

Network attempted: GenLayer Studionet (chain ID 61999)
Canonical deployment network: NOT AVAILABLE
Canonical contract address: NOT AVAILABLE
Explorer: https://explorer-studio.genlayer.com
Deployment/registration/assessment/source-update transactions: NOT AVAILABLE
Frontend production URL: NOT AVAILABLE

Runtime diagnostics: official-template-shaped probes failed with `invalid_contract` on Studionet. Failed txs are recorded in HANDOFF.md and are not treated as deployments.
