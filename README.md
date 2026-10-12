# RootCauseSeal

A standalone GenLayer Intelligent Contract that checks whether an incident postmortem is supported by a locked evidence package and satisfies a fixed root-cause/corrective-action policy.

The report must identify incident/impact, establish a timeline, explain an evidence-supported causal mechanism, propose preventive actions, assign owners and calendar due dates, and provide measurable acceptance tests. A convincing narrative alone cannot qualify.

| Outcome | Deterministic rule |
|---|---|
| INCONCLUSIVE | Any check UNKNOWN, or evidence/model validation fails |
| INCONSISTENT | No UNKNOWN and at least one CONTRADICTED check |
| ACTION_REQUIRED | No UNKNOWN/CONTRADICTED and at least one MISSING check |
| COMPLETE | All six checks SUPPORTED |

## How consensus works

The leader fetches every commit-pinned artifact, authenticates raw SHA-256 and byte length, then performs a structured semantic audit. Each validator independently repeats the fetch and audit. All six check classifications and derived outcome must agree exactly. Validators reauthenticate and verify the leader's verbatim quotes, then judge semantic equivalence of the reasons, summary, causal conclusions and remediation gaps against the artifacts. Wording and quote selection may differ; material conclusions may not. This uses `gl.vm.run_nondet_unsafe`, not strict equality over LLM prose.

## Contract API

Deploy `contracts/root_cause_seal.py` with publisher `haris4587/RootCauseSeal` (or an organization's approved public evidence repository). The deploying account owns registration and review. Policy and publisher have no setters.

1. `register(incident, manifest_json)` locks 2–5 sources, exactly one report and at least one evidence artifact, and returns a content-addressed case ID. Manifest objects contain `url`, `sha256`, `bytes`, `role`.
2. `review(case_id)` produces a consensus decision hash. INCONCLUSIVE permits up to three total attempts against the exact same package; substantive decisions are terminal. Revised reports require a new package/case. No overwrite or delete API exists.
3. `get_policy()`, `get_case(case_id)`, `get_decision(case_id, attempt)` expose canonical JSON strings, including policy/package binding and a chained decision history.

Cases include chain ID, contract address and owner in their hash. Decision SHA-256 covers canonical compact sorted-key ASCII-escaped UTF-8 JSON of the stored `decision` object. Recompute using `digest()` in the contract. The `hash` wrapper field is excluded.

## Verification

```sh
python -m pip install genvm-linter==0.11.0
python -m unittest discover -s tests -v
genvm-lint check contracts/root_cause_seal.py --json
genvm-lint schema contracts/root_cause_seal.py --json
```

Offline tests use mocked GenLayer host APIs and synthetic artifacts. They check real contract functions and validator paths but do not prove live AI behavior. The separate live Full Consensus run is recorded in [deployment evidence](docs/DEPLOYMENT.md).

## Scope

This is a technical policy certificate, not a claim that supplied telemetry is truthful. The locked publisher repository provides provenance; commit pins and digests prevent substitution. An approved publisher can still publish fabricated evidence. Non-report artifacts are separate evidence, not automatically independent organizations. There are no tokens, funds, escrow or payouts.

See [security](docs/SECURITY.md), [deployment](docs/DEPLOYMENT.md), and [evidence/reproduction](docs/EVIDENCE.md).
