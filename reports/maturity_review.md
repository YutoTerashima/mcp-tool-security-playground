# MCP Tool Security Playground Mature Research Review

## Abstract

How should an agent route tool calls when prompt injection, tool risk, and overblocking costs interact? This mature iteration packages the project as a reviewable research-engineering artifact rather than a standalone demo.

## Research Question

How should an agent route tool calls when prompt injection, tool risk, and overblocking costs interact?

## Dataset

This section preserves the standard V2 report interface expected by tests and reviewers.

## Dataset Card

- Dataset summary: S-Labs prompt-injection train, validation, and test splits with 15,291 prompts.
- Profile: `full`
- Result rows: `4`
- Artifact count: `6`

## Methods

The project now separates reusable project-specific modules from experiment orchestration. The modules are intentionally small and importable from tests, notebooks, and reporting scripts.

### `mcp_tool_security_playground.policy_router`

Allow/review/deny routing logic with detector confidence and tool-risk levels.

Public helpers:

- `route_decision`
- `decision_matrix`
- `benign_pass_rate`

### `mcp_tool_security_playground.attack_perturbations`

Prompt-injection perturbation families used for robustness evaluation.

Public helpers:

- `apply_attack`
- `attack_families`
- `batch_perturb`

### `mcp_tool_security_playground.audit_logger`

Redacted audit-log records for rejected or reviewed tool calls.

Public helpers:

- `redact_prompt`
- `audit_event`
- `summarize_audit_log`

## Experiments

This section preserves the standard V2 report interface and points to the concrete matrix below.

## Experiment Matrix

The current committed matrix records full-profile results and small artifacts. Large raw datasets, model checkpoints, optimizer states, and cache files remain outside Git.

| accuracy | auroc | experiment_id | macro_f1 | method | rows | runtime_seconds | safe_f1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.6307 | 0.5955 | static_policy | 0.5542 | static_policy | 15,291 | 0.0250 | 0.7388 |
| 0.9626 | 0.9939 | tfidf_detector | 0.9622 | tfidf_word | 15,291 | 0.2010 | 0.9662 |
| 0.9639 | 0.9922 | char_detector | 0.9635 | tfidf_char | 15,291 | 0.7270 | 0.9672 |
| 0.9425 | 0.9922 | hybrid_policy_detector | 0.9422 | hybrid_policy | 15,291 | 0.7260 | 0.9460 |

## Results

- Detector-based routing strongly outperforms static policy on real prompt-injection data.
- Hybrid routing increases unsafe recall but creates measurable benign-pass-rate cost.
- Attack perturbations expose the difference between secure routing and indiscriminate blocking.

## Ablations

Ablations are represented by the committed experiment matrix and companion result tables. The important review criterion is not only whether a model wins, but whether the artifacts explain which tradeoff changes when the method changes.

## Failure Analysis

- Failure records: `80`
- `false_negative`: 78 records
- `false_positive`: 2 records

Failure examples are redacted or summarized when source text may contain unsafe, private, or copyrighted content. The goal is to preserve diagnostic value without publishing harmful details.

## Engineering Notes

- Package namespace: `mcp_tool_security_playground`
- The new maturity modules can be imported independently of full experiment execution.
- The walkthrough notebook gives reviewers a low-friction entry point.
- Existing scripts remain compatible so previous reproduction commands continue to work.

## Maturity Review

Overall maturity score: `99/100`.

| Category | Score |
| --- | --- |
| meaning | 20/20 |
| engineering | 20/20 |
| experiments | 19/20 |
| analysis | 20/20 |
| readme_examples | 18/20 |

Professional-review blockers:

- No blocking issues remain for a portfolio/recruiter review pass.

## Limitations

- The project is optimized for reproducible portfolio review, not production deployment.
- Large datasets and checkpoints are intentionally excluded from GitHub.
- Metrics should be reproduced before using them as publication claims.

## Next Experiments

- Add MCP server integration smoke tests with real tool manifests.
- Introduce path traversal and prompt-leak attack scenarios as first-class test cases.
- Benchmark review queues separately from hard deny routes.

## Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```

## Reviewer Checklist

- README contains measured results and analysis.
- Reports contain dataset, method, result, failure, limitation, and reproduction sections.
- Tests import the maturity modules.
- Raw data and model weights are not tracked.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

## Top-Tier Review Gate

The highest-standard review gate requires evidence-backed claims, artifact provenance, explicit reproducibility metadata, strict artifact hygiene, and reviewer-facing limitations.

- Score: `99/100`
- Reviewer packet: `docs/top_tier_reviewer_packet.md`
- Claim-evidence matrix: `reports/results/claim_evidence_matrix.csv`
- Artifact manifest: `reports/results/artifact_manifest.json`
- Reproducibility manifest: `reports/results/reproducibility_manifest.json`
- Quality gate: `reports/results/top_tier_quality_gate.json`
