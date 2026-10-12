# Verified deployment and live test

Verified on 2026-10-12 with the built-in Studio account. This is the public **Studio sandbox**, chain ID 61999, GenVM v0.2.16; it is not a mainnet or funded production deployment. No external wallet connection was used.

| Item | Verified value |
|---|---|
| Contract | [0xf31106d0064d54F829fc4eBB377526C33c193A86](https://explorer-studio.genlayer.com/address/0xf31106d0064d54F829fc4eBB377526C33c193A86) |
| Owner | `0xabDa0405Bb3306647c4f03653017a3AD733FB9BC` |
| Deployment | [0x4761aa2787d59330eb7c784e59b8b76224fc6c19568f89494867669d0bbe2946](https://explorer-studio.genlayer.com/tx/0x4761aa2787d59330eb7c784e59b8b76224fc6c19568f89494867669d0bbe2946) — FINALIZED |
| Registration | [0xadb1ce3e983e3f3d70e9a2d6964850e376504ef2ac020c5acf5931e5ea6320bd](https://explorer-studio.genlayer.com/tx/0xadb1ce3e983e3f3d70e9a2d6964850e376504ef2ac020c5acf5931e5ea6320bd) — FINALIZED |
| Semantic review | [0x03207367aee7611f6190722234b4b7757a511bd5926a712fd347c92d75a6cce2](https://explorer-studio.genlayer.com/tx/0x03207367aee7611f6190722234b4b7757a511bd5926a712fd347c92d75a6cce2) — FINALIZED, SUCCESS, Accepted |
| Source commit | [`dd10cd393d2dab2167334ef3bd053768e67372cb`](https://github.com/haris4587/RootCauseSeal/commit/dd10cd393d2dab2167334ef3bd053768e67372cb) |
| Source SHA-256 | `19708247833015348587601964c2bd1ca8eac1e0d86ac259bf323575c349ba7d` |
| Case ID | `6a951f097b5d3d0b99d14a5db4ae5e7cdcee56357a78473a09de8a0d2af143c0` |
| Decision SHA-256 | `72ada20981677780cb9120a87d045cbf1686d8570eafcbf1a5eee0b6ac9c8306` |
| Policy SHA-256 | `93c38b22b9244566ce7e77cc89bef614f1aad8cbc3cc60c5055bea942353ca15` |

## Observed result

Full Consensus finalized **ACTION_REQUIRED**. Incident, timeline, cause, actions and verification were SUPPORTED; ownership was MISSING because named action owners and calendar due dates were TBD. The non-report telemetry supplied a causal reproduction distinguishing pool contention from database downtime. Both source artifacts are explicitly synthetic, not real incident telemetry.

Explorer showed Normal execution, five initially selected validators, zero rotations, three agree votes, one disagree and one idle. This is majority consensus, not unanimity. Finalized at 13:20:03 on 2026-10-12 in the browser's displayed Asia/Colombo time (07:50:03 UTC).

Read the FINALIZED state using `get_case(case_id)` and `get_decision(case_id, 1)`. Saved reads are [finalized-case.json](../evidence/finalized-case.json) and [finalized-decision.json](../evidence/finalized-decision.json). `python evidence/verify.py` independently verified the package ID, decision hash, fixture fingerprints, outcome and byte-for-byte deployed/source equality. [Verification output](../evidence/verification.json).

## Source and test validation

The exact final source was pushed before deployment in commit `dd10cd393d2dab2167334ef3bd053768e67372cb`. [final-deployed-source.py](../evidence/final-deployed-source.py) was read from Explorer's Code tab after final deployment. Its bytes exactly match `contracts/root_cause_seal.py`; SHA-256 is above. Later evidence-only commits preserve those source bytes. The fixture URLs remain pinned to the initial fixture commit, independently of later contract/evidence commits.

41 offline adversarial tests passed. Host web/LLM/consensus APIs are mocked in that suite; the real live test is the distinct transaction above. GenVM lint, SDK semantic validation and schema extraction all passed. The only linter notice is informational I200: a newer SDK runner exists. The deployed runner remains pinned to Studio's official dependency for reproducibility. See [unit output](../evidence/unit-tests.txt), [GenVM output](../evidence/genvm-check.json), and [schema](../evidence/schema.json).

## Failure investigation retained

The initial implementation at `0xCAAE117ebf0664e9Cd72cfc4b3BDcB0A5ff49780` finalized INCONCLUSIVE with INVALID_ASSESSMENT in [this review](https://explorer-studio.genlayer.com/tx/0xd661731aafaa87fa6ab0d33485e55d17998f63ef42464b9a055812f4eb363ccb). An intermediate diagnostic deployment at `0x12bB03C14748716CCe47fB9Cd8EE09535f730b66`, [review](https://explorer-studio.genlayer.com/tx/0xd7253c3c6469dea1427b0f49c4dc25c08399fdb5d94bb1151fba54a7d5991fdd), exposed shortened LLM quotes with ellipses, rejected as `Quote not found`. Its result is not used as final submission evidence. The final revision asks for short contiguous verbatim quotes and permits one bounded correction while retaining exact matching and every validation check. A regression test covers the correction path. Earlier inconclusive evidence is retained rather than relabeled as success.

[Finalized receipt snapshot](../evidence/full-consensus-finalized-observed.txt) · [Validator votes snapshot](../evidence/consensus-observed.txt) · [Deployment receipt snapshot](../evidence/deployment-observed.txt) · [Machine-readable record](../evidence/deployment.json)
