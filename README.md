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
