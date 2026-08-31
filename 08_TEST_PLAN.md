# ENDLINE — Test Plan

## Principle

Test state transitions and failure behaviour, not just happy-path rendering.

## 1. Contract deterministic tests

### Registration

- valid registration succeeds;
- zero sources rejected;
- more than 3 sources rejected;
- non-HTTPS source rejected;
- malformed URL rejected;
- obvious localhost/private targets rejected;
- oversized name rejected;
- oversized version rejected;
- oversized URL rejected;
- invalid kind rejected;
- duplicate canonical key rejected;
- IDs increment correctly.

### Source updates

- creator can update;
- non-creator cannot update;
- update increments source version exactly once;
- previous assessments remain readable;
- old assessment keeps old source version;
- invalid replacement source set rejected.

### Pagination

- dependency pagination bounded;
- assessment pagination bounded;
- empty ranges safe;
- out-of-range IDs handled clearly.

## 2. Nondeterministic/consensus tests

Create controlled fixtures representing:

### ACTIVE
Docs explicitly state supported/current.

### DEPRECATED
Official text says deprecated but retirement not yet effective.

### SECURITY_ONLY
Maintenance policy states only security fixes.

### END_OF_LIFE
Retirement date has passed or support ended.

### REPLACED
Old version superseded and replacement clearly named.

### UNKNOWN
Accessible evidence is insufficient.

### CONFLICT
Two configured sources materially disagree.

### PROMPT INJECTION
Evidence page contains malicious instructions.

Expected:
- source instructions do not change schema/policy.

## 3. Equivalence tests

Validators agree on:
- same status;
- same effective date;
- same replacement;
- same booleans;
- same reason code;
- different summary wording.

Expected:
- assessment can still converge if summary is explicitly non-critical.

Validators disagree on:
- status;
- effective date;
- replacement;
- migration requirement.

Expected:
- no unsafe canonical mutation.

## 4. Retry tests

Simulate:
- 500;
- timeout;
- empty render;
- model unavailable;
- malformed model output.

Verify:
- no assessment appended;
- count unchanged;
- canonical lifecycle unchanged;
- retry remains possible.

## 5. Frontend unit/component tests

- disconnected wallet state;
- wrong network;
- register form validation;
- source add/remove controls;
- transaction progress;
- error rendering;
- registry filtering;
- dependency detail rendering;
- history rendering;
- JSON copy formatting.

## 6. Frontend integration tests

Mock SDK boundary, not product data.

Verify:

### Register flow
form → write → finality → readback → route.

### Assessment flow
click → write → finality → readback → newest status.

### Failed readback
Finalised transaction but expected state not observed:
- show reconciliation error;
- do not show false success.

## 7. Real Studionet smoke test

Use real deployed contract.

Minimum proof:

1. register one dependency;
2. verify readback;
3. run one assessment against stable public evidence;
4. confirm terminal result;
5. inspect Explorer transaction;
6. verify history;
7. update source set;
8. confirm source version increments;
9. run second assessment;
10. confirm old history still references previous source version.

## 8. UI review

Check at:
- 1440px desktop;
- 1024px;
- 768px;
- 390px;
- 360px.

Verify:
- no horizontal overflow;
- registry remains readable;
- wallet/network controls usable;
- full keyboard path works;
- no colour-only status;
- no generic AI visual motifs.

## 9. Release gate

Do not release until:

- contract lint passes;
- schema extraction passes;
- direct tests pass;
- frontend tests pass;
- TypeScript passes;
- lint passes;
- production build passes;
- final deployed source matches repository source;
- at least one real Studionet lifecycle is documented.
