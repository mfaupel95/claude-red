---
name: offensive-dependency-confusion
description: "Review dependency source policy and prevent package-confusion risks."
---

# Dependency source confusion: defensive review

Use this skill to assess package-source configuration, namespace ownership, and lockfile integrity in authorized repositories. Do not publish lookalike packages, trigger installs, register public placeholders, or collect callbacks. A package being absent from a public registry is not proof of a vulnerability.

## Review workflow

1. Confirm repository and package-manager scope. Work from a local copy and use read-only configuration review first.
2. Inventory manifests, lockfiles, repository configuration, environment overrides, mirrors, and package-source mappings.
3. Determine the effective registry/source for each dependency using the exact package manager, version, project format, and operation. Do not generalize from source order or version numbers alone.
4. Check whether private package names are scoped or mapped exclusively to approved sources. Review how unscoped names resolve and whether extra indexes, mirrors, `find-links`, or local sources add candidates.
5. Verify lockfile URLs, hashes, provenance metadata, and review controls. Do not install an untrusted candidate to “prove” exposure.
6. Record source-selection uncertainty and recommend namespace controls, explicit source mapping, pinned versions, hashes, and trusted mirrors.

## Package-manager cautions

- **npm:** registry selection depends on package scope mapping and the configured default registry. Review effective `.npmrc` settings and lockfile resolved URLs; a missing scope mapping does not itself prove fallback or exposure.
- **pip:** candidate selection can involve all configured locations. Check index settings, extra indexes, `find-links`, trusted-host entries, environment variables, and configuration files. `--index-url` alone does not prove that no other source is active.
- **NuGet:** behavior depends on project format and operation. For `PackageReference` restore, source order is not a universal priority rule. Use Package Source Mapping to constrain package IDs to approved sources and verify the effective configuration.
- **Maven and Gradle:** resolution depends on mirrors, repository declarations, fixed versus dynamic versions, and tool version. Review effective settings and repository content filters; do not infer exposure from “highest version wins.”

## Safe validation

Use offline fixtures or a private disposable registry with synthetic package names and no install hooks. Do not publish to public registries or trigger package resolution in other consumers. If a controlled registry test is necessary, require written approval from its owner, isolate it from production, and define cleanup and rollback beforehand.

## References

- [npm: Registry scopes](https://docs.npmjs.com/cli/v10/using-npm/scope)
- [pip: Finding and choosing packages](https://pip.pypa.io/en/stable/cli/pip_install/#finding-packages)
- [NuGet: Package Source Mapping](https://learn.microsoft.com/en-us/nuget/consume-packages/package-source-mapping)
- [Gradle: Repository content filtering](https://docs.gradle.org/current/userguide/filtering_repository_content.html)
