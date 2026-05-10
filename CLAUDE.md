# Agent Instructions

This repository packages the GTM Brain Builder plugin for public use.

## Public Packaging Rules

- Keep the repo generic and reusable.
- Do not add private GTM data, customer evidence, transcripts, credentials, local `.env` files, or company-specific exports.
- If adding examples, use fictional company names.
- Keep plugin content scoped to agents, skills, references, and scripts that help someone build their own GTM Brain.

## Validation

Before publishing changes:

```bash
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 scripts/init_gtm_brain.py "Test GTM Brain" --path /tmp/Test-GTM-Brain --force
```

Also check for accidental private data:

```bash
rg -n "api[_-]?key|secret|password|token|/Users/|\\.env|customer export|transcript" .
```
