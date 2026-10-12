# GenLayer Intelligent Contracts submission

**Contribution date:** 10/12/2026

**Title:** RootCauseSeal — Evidence-Bound Incident Postmortem Verification

**One-line description:** GenLayer consensus verifies evidence-bound incident postmortems against a locked root-cause and corrective-action policy.

**Notes / Description (967 characters):**

RootCauseSeal audits incident postmortems against a locked root-cause and corrective-action policy. Cases bind incident identity and 2–5 commit-pinned artifacts with SHA-256 and byte lengths. GenLayer validators independently fetch and authenticate sources, then assess impact, timeline, causal support, preventive actions, owners/due dates and measurable verification.
Exact check-state agreement and source-grounded semantic equivalence protect decisions. Verbatim citations, input bounds, injection defenses and one bounded correction reject unsupported outputs. Deterministic rules derive COMPLETE, ACTION_REQUIRED, INCONSISTENT or INCONCLUSIVE. Owner authorization, bounded retries and chained decision hashes protect the lifecycle.
41 adversarial offline tests, GenVM lint and SDK validation pass. A real Studio Full Consensus test finalized ACTION_REQUIRED for missing owners/dates. Deployed source bytes and decision hash verified. Demo evidence is synthetic.

## Evidence links

- Repository: https://github.com/haris4587/RootCauseSeal
- Contract: https://explorer-studio.genlayer.com/address/0xf31106d0064d54F829fc4eBB377526C33c193A86
- Deployment: https://explorer-studio.genlayer.com/tx/0x4761aa2787d59330eb7c784e59b8b76224fc6c19568f89494867669d0bbe2946
- Full Consensus: https://explorer-studio.genlayer.com/tx/0x03207367aee7611f6190722234b4b7757a511bd5926a712fd347c92d75a6cce2
- Registration: https://explorer-studio.genlayer.com/tx/0xadb1ce3e983e3f3d70e9a2d6964850e376504ef2ac020c5acf5931e5ea6320bd
- Source commit: https://github.com/haris4587/RootCauseSeal/commit/dd10cd393d2dab2167334ef3bd053768e67372cb
- Final source: https://github.com/haris4587/RootCauseSeal/blob/main/contracts/root_cause_seal.py
- Deployment record: https://github.com/haris4587/RootCauseSeal/blob/main/docs/DEPLOYMENT.md
- Security: https://github.com/haris4587/RootCauseSeal/blob/main/docs/SECURITY.md
- Evidence guide: https://github.com/haris4587/RootCauseSeal/blob/main/docs/EVIDENCE.md
- Tests: https://github.com/haris4587/RootCauseSeal/blob/main/tests/test_contract.py
- Test output: https://github.com/haris4587/RootCauseSeal/blob/main/evidence/unit-tests.txt
- GenVM output: https://github.com/haris4587/RootCauseSeal/blob/main/evidence/genvm-check.json
- Schema: https://github.com/haris4587/RootCauseSeal/blob/main/evidence/schema.json
- Finalized state: https://github.com/haris4587/RootCauseSeal/blob/main/evidence/finalized-case.json
- Finalized decision: https://github.com/haris4587/RootCauseSeal/blob/main/evidence/finalized-decision.json
- Verification: https://github.com/haris4587/RootCauseSeal/blob/main/evidence/verification.json
- Manifest: https://github.com/haris4587/RootCauseSeal/blob/main/evidence/manifest.json
- Verifier: https://github.com/haris4587/RootCauseSeal/blob/main/evidence/verify.py
- Receipt observation: https://github.com/haris4587/RootCauseSeal/blob/main/evidence/full-consensus-finalized-observed.txt
- Consensus votes: https://github.com/haris4587/RootCauseSeal/blob/main/evidence/consensus-observed.txt
- Deployed source snapshot: https://github.com/haris4587/RootCauseSeal/blob/main/evidence/final-deployed-source.py
- Finalized screenshot: https://github.com/haris4587/RootCauseSeal/blob/main/evidence/full-consensus-finalized.jpg
- Pinned report: https://raw.githubusercontent.com/haris4587/RootCauseSeal/60d3cb3d0657c110779ac4aa6207e37f5124bd09/fixtures/postmortem.txt
- Pinned evidence: https://raw.githubusercontent.com/haris4587/RootCauseSeal/60d3cb3d0657c110779ac4aa6207e37f5124bd09/fixtures/telemetry.txt

Source SHA-256: `19708247833015348587601964c2bd1ca8eac1e0d86ac259bf323575c349ba7d`

Decision SHA-256: `72ada20981677780cb9120a87d045cbf1686d8570eafcbf1a5eee0b6ac9c8306`

The final evidence commit is the commit containing this file; the source commit identifies the exact deployed implementation. No code changes were made when appending deployment evidence.
