# ENDLINE — Architecture

## System boundary

```text
┌──────────────────────────────────────────────┐
│                  FRONTEND                    │
│                                              │
│  Next.js / TypeScript                       │
│  injected EIP-1193 wallet                   │
│  genlayer-js                                │
│                                              │
│  reads contract state                       │
│  writes registration / assessment txs       │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│        GENLAYER INTELLIGENT CONTRACT         │
│                                              │
│ deterministic state                         │
│ dependency registry                         │
│ source versions                             │
│ assessment history                          │
│ lifecycle policy                            │
│                                              │
│ nondeterministic assessment block           │
└──────────────────────┬───────────────────────┘
                       │
             independent validator reads
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      source 1      source 2      source 3
     docs page      changelog     policy page
```

There is no application backend in the MVP.

## Frontend responsibilities

The frontend may:

- connect injected wallets;
- request chain switching;
- validate forms for user experience;
- submit writes;
- wait for final transaction status;
- perform authoritative contract readback;
- render registry data;
- generate a copyable JSON view from on-chain state.

The frontend must not:

- decide lifecycle status;
- fetch evidence and claim that it represents validator evidence;
- persist canonical registry state in local storage;
- treat optimistic form state as final;
- secretly proxy evidence through API routes.

## Contract responsibilities

The Intelligent Contract owns:

- ID assignment;
- duplicate prevention;
- dependency data;
- URL bounds and coarse validation;
- source ownership/update policy;
- assessment sequencing;
- web retrieval;
- model interpretation;
- consensus equivalence;
- canonical lifecycle result;
- history;
- failure invariants.

## Data flow: registration

```text
form
  ↓
client-side validation
  ↓
writeContract(register_dependency)
  ↓
GenLayer finality
  ↓
readContract(get_dependency)
  ↓
render authoritative state
```

## Data flow: assessment

```text
user clicks "Run assessment"
  ↓
writeContract(assess_dependency)
  ↓
each validator independently:
    fetches configured sources
    extracts bounded lifecycle facts
    classifies into allowed enum
  ↓
equivalence/consensus
  ↓
only agreed structured result reaches mutation path
  ↓
contract updates current state + appends history
  ↓
frontend reads final dependency + newest assessment
```

## Network

For collaborative hosted development:

- network: GenLayer Studionet
- chain ID: `61999`
- currency: `GEN`
- explorer: `https://explorer-studio.genlayer.com`
- GenLayer RPC: `https://studio.genlayer.com/api`

Keep all network values in a single frontend config module.

## Repository shape

```text
endline/
├─ contracts/
│  └─ endline.py
├─ frontend/
│  ├─ app/
│  ├─ components/
│  ├─ lib/
│  ├─ styles/
│  └─ tests/
├─ tests/
│  ├─ direct/
│  └─ integration/
├─ scripts/
├─ docs/
├─ .env.example
├─ README.md
└─ HANDOFF.md
```

## State-authority rule

The frontend may cache data for rendering convenience, but **contract state is always authoritative**.

After every successful-looking write:

1. wait for finality;
2. read the affected object from chain;
3. verify expected transition;
4. only then display success.

## Availability caveat

Public webpages can change, block automated rendering, return regional variants, or become temporarily unavailable.

Endline should therefore distinguish:

- valid `UNKNOWN` evidence outcome;
- retryable technical failure;
- non-convergent validator outcome.

Do not collapse all three into one generic status.
