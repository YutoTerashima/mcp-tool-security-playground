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
## Publishable V2 Research Upgrade

This repository now includes a project-level V2 experiment suite:

- Reproducible matrix: `configs/experiment_matrix.yaml`
- Main runner: `scripts/run_matrix.py --device cuda --profile full`
- Failure analysis: `scripts/analyze_failures.py`
- Research report: `reports/mcp_tool_security_v2_research_report.md`
- Experiment index: `reports/results/experiment_index.json`

The V2 artifacts include multiple experiments, ablations, figures, failure cases, and a discussion section while keeping raw caches and large checkpoints out of Git.

