# Evidence and reproduction

The supplied `fixtures/postmortem.txt` and `fixtures/telemetry.txt` are explicitly synthetic. They model a pool-exhaustion incident with supporting causal reproduction, timeline and impact. The report has specific preventive actions and measurable tests but intentionally omits their owners and due dates. Expected semantic result: ACTION_REQUIRED, ownership MISSING, all other checks SUPPORTED. A live run must establish what validators actually concluded; expected results are not evidence of execution.

Each fixture is referenced through a full Git commit SHA, with raw byte length and SHA-256 committed to the manifest. `evidence/manifest.json` will record the live package; fixture commit and contract commit may differ because deployment records are committed afterward.

Local checks: `python -m unittest discover -s tests -v`; `genvm-lint check contracts/root_cause_seal.py --json`; schema extraction. Read [DEPLOYMENT.md](DEPLOYMENT.md) for verified live transaction and source comparisons.

Official references consulted on 2026-10-12:

- https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle
- https://docs.genlayer.com/developers/intelligent-contracts/features/web-access
- https://docs.genlayer.com/developers/intelligent-contracts/examples/storage
- https://docs.genlayer.com/api-references/genlayer-linter
- https://github.com/genlayerlabs/genvm (SDK implementation; pinned dependency validates actual API fields)

The runner hash is pinned to the official Studio v0.2.16 example dependency for compatibility. Linter 0.11.0 reports an informational newer-runner notice; upgrading the runner without checking Studio support would undermine reproducibility.
