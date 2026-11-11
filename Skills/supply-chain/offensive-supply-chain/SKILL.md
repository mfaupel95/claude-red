---
name: offensive-supply-chain
description: "Assess software supply-chain controls and provenance without modifying artifacts."
---

# Software supply chain: defensive assessment

This reference supports authorized, read-only review of source, build, dependency, signing, and release controls. Do not create, publish, inject, replace, or execute malicious packages, workflows, artifacts, or updates. Use synthetic fixtures and isolated test repositories for validation.

## Assessment workflow

1. Define repositories, build systems, registries, signing identities, release channels, and third-party boundaries in the written scope.
2. Map source-to-build-to-release provenance: commits, approvals, dependencies, build runners, artifacts, signatures, and deployment records.
3. Review workflow permissions, trusted triggers, runner isolation, reusable-workflow pinning, artifact provenance, and secret exposure boundaries.
4. Inspect dependency sources, lockfiles, checksums, SBOMs, and policy enforcement. Treat scanners as partial controls: known-vulnerability results do not establish that code is benign.
5. Verify signature and provenance policy independently. A valid signature identifies a signing key or publisher; it does not prove the artifact is safe.
6. Examine release and update controls, including key custody, approval separation, rollback, and audit retention.
7. Record evidence and gaps without downloading or executing suspicious artifacts. Escalate suspected compromise through the owner's incident process.

## Controls to assess

- Require reviewed changes, protected branches, least-privilege CI identities, and approval for release-affecting workflows.
- Pin third-party actions and build dependencies to immutable references where supported; review updates before adoption.
- Use explicit package-source mapping, lockfiles, hashes, and trusted registries.
- Isolate ephemeral runners and separate untrusted builds from signing/release environments.
- Protect signing keys with hardware-backed or managed controls, narrow authorization, and auditable rotation.
- Generate and retain provenance and SBOMs; verify them at deployment rather than treating their presence as proof of safety.
- Maintain a tested rollback and incident-response path for compromised dependencies or releases.

## Safe validation

Prefer configuration review, policy tests, and vendor-provided benign fixtures. Use dummy secrets and synthetic artifacts in a private disposable repository. Do not access real signing keys, transmit secrets, publish test packages publicly, tamper with production artifacts, or install untrusted dependencies.

## References

- [SLSA: Supply-chain Levels for Software Artifacts](https://slsa.dev/)
- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
- [OpenSSF Scorecard](https://scorecard.dev/)

## Artifact trust evidence review matrix

| Review question | Existing evidence | Expected control | Limitation |
|---|---|---|---|
| Is the registry and base-image origin explicit? | Existing Dockerfile/build/deployment manifests and sanitized build records naming registry, repository, base-image publisher and platform | Fully qualified approved registries and reviewed base-image provenance | Familiar names, mirrors and “official” labels do not independently prove origin or safety |
| Can mutable tags change the artifact? | Existing tag-to-digest history, manifest/index and platform-specific digest records | Reviewed digest pinning and recorded update approval; compare build and deployed digests | Tags are mutable; a digest fixes content identity, not trust; a multi-platform index differs from a platform manifest |
| Is the signer the expected one for this release? | Existing signature/provenance verification report: artifact digest, signer key/identity, issuer, trusted-root/policy version and verification time | Explicit expected signer/issuer and source/build identity policy, with revocation/rotation handling | A valid signature from an unexpected identity is insufficient; expected signing does not prove benign code |
| Is there independent rebuild evidence? | Already available independent builder report: source commit, materials/base digests, toolchain, build recipe/environment, output digests and comparison method | Independently controlled rebuild with matching declared inputs and documented byte/semantic comparison | Same pipeline repeating a build is not independent; nondeterminism can explain differences; do not claim reproducibility from a provenance document alone |
| Which evidence is missing? | Evidence inventory linking each claim to retained reports, with missing inputs, inaccessible builder logs and verification failures marked explicitly | Record verified/contradicted/unknown per claim, owner and follow-up; gate release per policy | No rebuild or signer evidence means unknown, not trusted or compromised; this review does not perform builds or retrieve suspicious artifacts |

- [Docker: base-image selection and digest pinning](https://docs.docker.com/build/building/best-practices/)
