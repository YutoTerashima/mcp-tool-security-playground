# Tool Audit Analysis

The audit layer assigns impact and risk scores after policy decisions. This makes
denied requests analyzable instead of merely blocked.

| Pattern | Interpretation |
| --- | --- |
| outside allowed path | likely path-confusion or prompt-injection pressure |
| human review | high-impact tool requires explicit approval |
| not allowlisted | unknown capability should default to deny |
