# Real Dataset Analysis: Prompt Injection Samples

Source: [S-Labs/prompt-injection-dataset](https://huggingface.co/datasets/S-Labs/prompt-injection-dataset)

The analysis uses 320 real rows and tracks label balance plus lexical attack
indicators that matter for MCP/tool-use policy design.

- Label counts: {'0': 189, '1': 131}
- Most common injection-related tokens: [('instruction', 23), ('system', 20), ('ignore', 14), ('secret', 4), ('tool', 3), ('previous', 3)]

Design implication: policy checks should not rely only on keyword spotting. The dataset
contains normal programming/help questions alongside adversarial instructions, so the
playground uses policy context, allowed roots, and human-review boundaries in addition
to lexical signals.
