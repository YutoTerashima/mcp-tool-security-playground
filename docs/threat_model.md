# Threat Model

The mock client receives user-controlled text. The policy layer assumes prompts can
be hostile and only trusts structured tool requests after validation.
