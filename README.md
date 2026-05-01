# MCP Tool Security Playground

A compact playground for reasoning about Model Context Protocol style tool-use
security: tool permissions, prompt-injection pressure, safe wrappers, and risk logs.

## Research Question

When an agent can call tools, where should safety live: prompt, tool definition,
policy layer, or execution wrapper? This repo demonstrates a small policy-first
answer with mock tools.

## Quick Start

```bash
pip install -e ".[dev]"
python examples/run_policy_demo.py
pytest
```

## Example Output

```text
allow calculator.add
deny file.read: outside allowed path
deny network.post: tool requires human review
```

## Defensive Patterns

- Default-deny tool registry
- Human-review flags for high-impact tools
- Path allowlists for file operations
- Separate policy decision from tool execution

## Research Brief

See [`docs/research_brief.md`](docs/research_brief.md) for the threat model,
method, limitations, and next experiments.

## Portfolio Notes

This project demonstrates that tool safety needs explicit policy and execution boundaries, not only better prompts.

## Deeper Analysis

`examples/run_audit.py` adds an audit layer with impact scores, denial reasons,
max-risk analysis, and policy-decision summaries.

## Experiment Artifacts

- Scenario set: [`examples/injection_cases.json`](examples/injection_cases.json)
- Audit results: [`reports/tool_policy_audit.csv`](reports/tool_policy_audit.csv), [`reports/tool_policy_audit.json`](reports/tool_policy_audit.json)
- Analysis: [`reports/tool_policy_audit_report.md`](reports/tool_policy_audit_report.md)

## Capability Manifests

The project includes structured tool manifests and threat classification labels.
This mirrors how real agent platforms need machine-readable capability metadata
before policy decisions can be audited.

## Full Scenario Matrix

The project includes 28 policy scenarios in
[`examples/full_policy_scenarios.json`](examples/full_policy_scenarios.json) and
a generated analysis report in
[`reports/full_policy_scenarios_analysis.md`](reports/full_policy_scenarios_analysis.md).

## Audit Redaction

Audit logs include a redaction helper so sensitive tool arguments can be recorded
safely without leaking tokens or secrets into reports.

## Real Public Dataset Experiment

        The repository includes a 320-row sample from
        [S-Labs/prompt-injection-dataset](https://huggingface.co/datasets/S-Labs/prompt-injection-dataset)
        at `datasets/external/prompt_injection_sample.jsonl`. The accompanying report analyzes
        real prompt-injection labels and lexical attack patterns, then connects them to MCP-style
        permission boundaries.

## GPU-Backed Real Experiment

This repository now includes a reproducible GPU-backed experiment using `S-Labs/prompt-injection-dataset`.
The smoke path runs on the local RTX 5090 Laptop GPU through the `Transformers` conda
environment and writes metrics, figures, and a markdown report.

```powershell
conda run -n Transformers python scripts/download_data.py --smoke
conda run -n Transformers python scripts/preprocess_data.py --max-samples 384
conda run -n Transformers python scripts/run_experiment.py --device cuda --smoke
conda run -n Transformers python scripts/make_report.py
```

Main report: `reports/mcp_tool_security_gpu_report.md`.

<!-- V2_RESEARCH_UPGRADE -->
## Publishable V2 Research Results

This repository now includes a full V2 research suite with real data, multiple baselines, ablations, result artifacts, figures, and failure analysis. The README summarizes the measured run so the project can be judged from results, not just project intent.

### Dataset And Scale

S-Labs prompt-injection dataset using train, validation, and test splits; the full V2 run contains 15,291 tool-use security prompts.

- Full-profile result rows: `4`
- Experiment profile: `full`
- Experiment index: [`reports/results/experiment_index.json`](reports/results/experiment_index.json)
- Full report: [`reports/mcp_tool_security_v2_research_report.md`](reports/mcp_tool_security_v2_research_report.md)

### Main Results

| experiment_id | accuracy | macro_f1 | unsafe_recall | safe_recall | auroc | runtime_seconds |
| --- | --- | --- | --- | --- | --- | --- |
| static_policy | 0.6307 | 0.5542 | 0.2404 | 0.9505 | 0.5955 | 0.0250 |
| tfidf_detector | 0.9626 | 0.9622 | 0.9489 | 0.9738 | 0.9939 | 0.2010 |
| char_detector | 0.9639 | 0.9635 | 0.9588 | 0.9681 | 0.9922 | 0.7270 |
| hybrid_policy_detector | 0.9425 | 0.9422 | 0.9727 | 0.9177 | 0.9922 | 0.7260 |

### Analysis

- Detector-based routing substantially outperforms static policy: the best TF-IDF/char detectors reach roughly 0.962-0.964 macro-F1 on real prompt-injection data.
- The hybrid policy improves unsafe recall to about 0.973, but lowers benign pass rate compared with pure detectors, exposing the practical allow/deny/review tradeoff.
- Perturbation probes show hidden-instruction and tool-exfiltration wrappers push rule routing toward broad denial, which is useful for safety but creates overblocking pressure.
- The project now frames MCP security as an execution-policy problem: prompt text, tool risk, classifier confidence, and routing outcome are evaluated together.

### Failure Analysis

- `false_negative`: 78 records
- `false_positive`: 2 records

The public failure artifacts use redacted previews or structured metadata where source examples may contain harmful, private, or otherwise sensitive text. This keeps the analysis reproducible without turning the README into a prompt-injection or unsafe-content corpus.

### Key Artifacts

- [`reports/results/v2_main_results.csv`](reports/results/v2_main_results.csv)
- [`reports/results/v2_ablation_results.csv`](reports/results/v2_ablation_results.csv)
- [`reports/results/v2_failure_cases.json`](reports/results/v2_failure_cases.json)
- [`reports/figures/v2_ablation_macro_f1.png`](reports/figures/v2_ablation_macro_f1.png)
- [`reports/figures/v2_confusion_matrix.png`](reports/figures/v2_confusion_matrix.png)
- [`reports/figures/v2_model_macro_f1.png`](reports/figures/v2_model_macro_f1.png)

Figures:

- [`reports/figures/v2_ablation_macro_f1.png`](reports/figures/v2_ablation_macro_f1.png)
- [`reports/figures/v2_confusion_matrix.png`](reports/figures/v2_confusion_matrix.png)
- [`reports/figures/v2_model_macro_f1.png`](reports/figures/v2_model_macro_f1.png)

### Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```
