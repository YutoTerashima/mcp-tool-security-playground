from __future__ import annotations


SENSITIVE_KEYS = {"token", "secret", "password", "api_key"}


def redact(value: object) -> object:
    if isinstance(value, dict):
        return {key: ("<redacted>" if key.lower() in SENSITIVE_KEYS else redact(val)) for key, val in value.items()}
    if isinstance(value, list):
        return [redact(item) for item in value]
    return value
