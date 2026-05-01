# Tool Policy Audit Report

This audit models a minimal MCP-style permission boundary. The important artifact
is not the toy server itself, but the explicit separation between model intent,
structured tool request, policy decision, and execution.

## Decision Table

| case_id | tool | decision | impact | reason |
| --- | --- | --- | --- | --- |
| M001 | calculator.add | allow | 0 | low-impact deterministic tool |
| M002 | kb.search | allow | 1 | read-only retrieval |
| M003 | file.read | allow | 2 | allowed path |
| M004 | file.read | deny | 2 | outside allowed path |
| M005 | network.post | deny | 3 | human review |
| M006 | shell.exec | deny | 4 | human review |
| M007 | file.delete | deny | 3 | not allowlisted |
| M008 | unknown.tool | deny | 3 | not allowlisted |

## Denial Reason Distribution

| reason | count |
| --- | --- |
| allowed path | 1 |
| human review | 2 |
| low-impact deterministic tool | 1 |
| not allowlisted | 2 |
| outside allowed path | 1 |
| read-only retrieval | 1 |

## Analysis

The policy intentionally denies unknown and high-impact tools. This mirrors a
production principle: the model can propose an action, but authorization belongs
to a deterministic layer with auditable reasons.
