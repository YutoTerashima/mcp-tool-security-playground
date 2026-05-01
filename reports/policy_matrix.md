# Policy Matrix

| Tool | Default | Reason |
| --- | --- | --- |
| `calculator.add` | allow | deterministic low-impact tool |
| `kb.search` | allow | read-only retrieval |
| `file.read` | conditional | path allowlist required |
| `network.post` | deny | requires human review |
| `shell.exec` | deny | high-impact execution surface |
