# Release Checklist

Use this checklist when preparing a public package or release preview.

## Boundary

- Confirm public package purpose and audience.
- Confirm what remains private.
- Search for secrets, tokens, private hostnames, customer data, internal names, and private repo paths.
- Check license, dependency licenses, package name, version, and author fields.

## Public Contract

- README explains the artifact in the first 10 lines.
- Install/run/use instructions match the current package.
- Public exports, schemas, CLI commands, and generated examples match each other.
- Examples are minimal and runnable.
- "What this is not" is specific and not fear-led.

## Release Preview

- Build or export using the project's release script when available.
- Inspect the exported tree, not only source files.
- Identify generated audit files that should not be committed.
- Confirm package metadata in the export matches source metadata.

## Verification

- Run tests that cover public contract and examples.
- Run build/typecheck/lint if the project normally requires them.
- For docs-only changes, read back the README and examples for stale naming.
- Final answer should name verification commands and whether they passed.
