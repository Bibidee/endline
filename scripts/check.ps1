$ErrorActionPreference = 'Stop'
$env:PYTHONIOENCODING = 'utf-8'
genvm-lint lint contracts/endline.py
genvm-lint typecheck contracts/endline.py
npm ci --prefix frontend
npm run typecheck --prefix frontend
$env:ESLINT_USE_FLAT_CONFIG = 'false'; npm run lint --prefix frontend
npm test --prefix frontend
npm run build --prefix frontend
