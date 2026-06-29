---
name: oss-release-packager
description: >
  Prepare an internal project, package, CLI, standard, SDK, or documentation set for open-source/public release, or audit a closed-source implementation against its public package for drift. Use when asked to publish, open source, package, release-preview, write a public README, create examples, define public/private repo boundaries, verify package metadata, or compare a private/internal version against the public artifact.
---

# OSS Release Packager

## Overview

Use this skill to turn an internal artifact into a publishable public package without leaking private implementation details, and to keep the closed-source/internal version aligned with the public contract after release.

Default to a conservative release posture: make the public artifact useful, runnable, and honest; keep private code, customer data, secrets, internal roadmaps, and unsupported claims out of the public surface.

## Choose A Mode

- **Public release package**: use when preparing or updating an open-source repository, npm/PyPI package, CLI, schema, SDK, standard, examples, launch README, or release preview.
- **Closed-source drift audit**: use when the public package already exists and the user wants to know whether the private/internal implementation, docs, generated outputs, or tests have drifted away from the public artifact.

For public release packaging, read `references/release-checklist.md`.

For drift audits, read `references/drift-audit.md`.

## Public Release Workflow

1. **Establish the release boundary**
   - Identify what is public source, public contract, generated artifact, example, documentation, and internal-only implementation.
   - Look for secrets, private URLs, real customer/user data, internal roadmaps, license-incompatible dependencies, and proprietary implementation details.
   - If the boundary is ambiguous, propose a narrower public package and name what remains private.

2. **Inspect the actual repo state**
   - Read package metadata, schemas, CLI entrypoints, public exports, examples, tests, README/docs, license, and release scripts.
   - Use `git status --short` before editing. Preserve unrelated user changes.
   - Prefer the project's own export/build/test scripts over hand-building a preview.

3. **Make the public contract legible**
   - Ensure the README states: what this is, who it is for, what the package contains, how to install/run/use it, what is stable, what is experimental, and what it is not.
   - Make examples minimal, runnable, and aligned with the current API/schema.
   - Keep limitation language plain and specific; avoid defensive walls of disclaimers at the top.

4. **Align all public surfaces**
   - Check package metadata, schema descriptions, generated output copy, docs, examples, CLI help, tests, and README for consistent naming and claims.
   - When phrasing changes, propagate it across surfaces rather than leaving stale language behind.

5. **Generate a release preview**
   - Create a tree or exported folder that reflects what would actually publish.
   - Include package name/version/license and the top README opening in the final summary.
   - Call out generated files or local audit metadata that should not be committed.

6. **Verify**
   - Run the narrowest meaningful tests first, then broader package verification if available.
   - For docs-only changes, still read back rendered/previewed docs when practical.
   - If verification cannot run, say exactly why and what risk remains.

## Drift Audit Workflow

1. **Define the pair**
   - Public side: package, standard, SDK, CLI, README, schema, examples, or exported artifact.
   - Closed-source side: internal implementation, hosted product, generation route, private docs, private tests, or release/export pipeline.

2. **Map comparable surfaces**
   - Public contract/API/schema.
   - Generated outputs and examples.
   - User-facing copy and docs.
   - Package metadata/versioning.
   - Tests/fixtures that describe expected behavior.

3. **Classify each difference**
   - `in_sync`: same behavior or same claim.
   - `intentional_private`: closed-source-only behavior that should not be public.
   - `public_missing`: public package lacks behavior/docs needed for users to succeed.
   - `closed_source_drift`: internal behavior no longer matches the public contract.
   - `risky_leakage`: public artifact exposes private, unsupported, or confusing internal detail.

4. **Patch or report**
   - If the user's request implies implementation, patch the smallest safe set of files.
   - If the audit reveals product decisions, report options and recommend the default path.
   - Never copy private implementation wholesale into public code unless the user explicitly approves that boundary.

## Output Shape

For a release package, end with:

- Public artifact path or repo/package location.
- Package tree or changed public surfaces.
- Verification run and result.
- Remaining release blockers, if any.

For a drift audit, end with:

- Drift table grouped by surface.
- Recommended patches or decisions.
- Any public/private boundary risks.
- Verification needed after fixes.
