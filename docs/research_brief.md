# Research Brief

## Problem

Tool-using agents inherit the risk of every connected capability. Prompt-level safety is
not enough when a model can request file access, network calls, shell execution, or
private data retrieval.

## Method

This playground uses a default-deny tool policy with:

- explicit tool allowlists
- human-review lists for high-impact tools
- path allowlists for file access
- structured policy decisions before execution

## What the Mock Demo Proves

The same natural-language pressure can be ignored because authorization is enforced at
the tool boundary. The model can ask, but the policy decides.

## Limitations

- This is a local simulation, not a full MCP runtime.
- The policy is static.
- The examples are mild and defensive by design.

## Next Experiments

- Add signed tool manifests.
- Add per-session permission scopes.
- Add audit logs with redaction for sensitive arguments.
