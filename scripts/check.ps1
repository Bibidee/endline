$ErrorActionPreference = 'Stop'
$env:PYTHONIOENCODING = 'utf-8'
genvm-lint lint contracts/endline.py
genvm-lint validate contracts/endline.py
New-Item -ItemType Directory -Force artifacts | Out-Null
genvm-lint schema contracts/endline.py --output artifacts/endline.schema.json --json
genvm-lint typecheck contracts/endline.py
python -m pytest tests/direct -v
npm ci --prefix frontend
npm run typecheck --prefix frontend
$env:ESLINT_USE_FLAT_CONFIG = 'false'; npm run lint --prefix frontend
npm test --prefix frontend
npm run build --prefix frontend
