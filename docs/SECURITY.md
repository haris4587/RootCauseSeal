# Security and trust boundaries

## Binding and authorization

The constructor locks an approved GitHub owner/repository and the deployer. Only that deployer can register or spend inference on reviews. Cases commit incident ID, ordered source manifest, policy hash, publisher, owner, chain ID and contract address. Sources must be public raw GitHub URLs containing full lowercase 40-hex commits, with safe literal paths. Branches, tags, alternate hosts, queries, traversal and duplicate URLs are rejected. Every leader/validator fetch requires HTTP 200, exact SHA-256, exact bytes, UTF-8 and no NUL. Hashing is of raw bytes, not rendered/normalized text. SDK `Response.status` is used; prose docs currently show `status_code` in some examples, which is not the pinned SDK field.

The approved repository is a provenance boundary, not proof of publisher honesty. The owner chooses evidence and can omit adverse evidence. A third-party authoritative telemetry source must be independently obtained and preserved by the publisher; this version does not verify signatures, Git commit signatures or external issuer identities. Certificates are conditional on the locked package. The semantic incident check must connect evidence to the report's incident, service and times.

## Consensus and injection

Documents and incident strings are JSON-encoded under an explicit untrusted-data boundary. Prompts forbid following instructions in artifacts, browsing, tool requests and invented facts. The fixed policy cannot be edited by source text. Model-provided outcomes are forbidden; deterministic rules derive them. Supported/contradicted findings need bounded literal citations; cause support must cite non-report evidence. Independent validator assessments, exact check-state agreement, fresh leader citation checks and semantic source-grounded equivalence provide additional defenses. Prompt defenses reduce risk; they cannot mathematically guarantee LLM resistance. Offline injection tests verify boundaries and reject fabricated output, not universal model robustness.

## Failure and recovery

HTTP failures, changed fingerprints, decoding errors, malformed/oversized assessments and inference failures produce bounded INCONCLUSIVE error codes. Validators must independently reproduce an identical error to accept it. Divergent observations or semantic judgments reject consensus; a VM/network-undetermined transaction does not update state. No optimistic fallback marks a case COMPLETE. INCONCLUSIVE dominates contradictions conservatively; inspect all check details where available.

The owner may retry an inconclusive package three times total; history chains never overwrite earlier decisions. After exhaustion, the package remains INCONCLUSIVE. A changed report or evidence package can register a new case. There is no shared candidate slot for strangers to monopolize and no funds to trap. Availability depends on public GitHub and configured LLM providers.

Each independent semantic audit permits at most two model calls: the initial response and one correction on validation/provider failure. A correction receives the same authenticated artifacts and fixed checks, with bounded validation feedback. Exact quote matching and every schema bound remain mandatory; no fuzzy citation acceptance is used. Failure after both attempts remains INCONCLUSIVE. Bounded diagnostic traces identify validation errors; they do not alter verdicts.

## Bounds

Maximum 1000 cases per deployment, 3 accepted reviews per case, 2–5 files, 12000 bytes/file and 30000 bytes/package; manifest 6000 characters; URL 350; incident 120; six fixed checks; reason 500/check; summary 800; three citations/check, 350 characters/quote. Responses are downloaded by the host before local byte checking, so the contract bounds accepted data and model input, not the host's network buffering. Semantic equivalence adds one judge call per validator. No external wallet, secrets, payable methods, or cross-contract calls are required.

## Tests

`tests/test_contract.py` covers source substitution, unsafe URLs, duplicate/oversized manifests, citation forgery, report-only causal support, exact semantic check-state agreement, failed judge/VM output, provider/fetch failures, authorization, retry exhaustion, immutable history, and cross-deployment hash domains. These are mocked host tests; live consensus evidence is separate.
