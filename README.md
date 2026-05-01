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
