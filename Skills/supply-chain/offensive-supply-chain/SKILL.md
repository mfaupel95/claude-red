---
name: offensive-supply-chain
description: "Assess software supply-chain controls and provenance without modifying artifacts."
---

# Software supply chain: defensive assessment

This reference supports authorized, read-only review of source, build, dependency, signing, and release controls. Do not create, publish, inject, replace, or execute malicious packages, workflows, artifacts, or updates. Use synthetic fixtures and isolated test repositories for validation.


## Evidence-based release review

Review authorized, existing sanitized records only; cite evidence location, release/commit, digest, time window, owner and coverage. Missing evidence is unknown, not a passed control. Do not fetch or execute suspicious artifacts, run builds, access signing keys, change pipelines or publish anything.

| Question | Existing evidence | Expected control | Limitation |
|---|---|---|---|
| Are source and build boundaries controlled? | Protected-branch approvals, effective CI permissions/triggers, runner isolation records and pinned workflow/dependency references. | Reviewed source, least privilege, immutable inputs and separation of untrusted builds from signing/releases. | Configuration snapshots do not establish historical enforcement; compromised trusted builders remain a risk. |
| Is the registry explicitly approved? | Package/image source policies, fully qualified registry/namespace records, retained pull/push audit events, mirror configuration and existing manifests/build records identifying base-image publisher and platform. | Restrict approved registries and repositories; review source changes and reject unexpected routes at consumption. | A familiar registry hostname does not authenticate every publisher; mirrors and caches complicate attribution. |
| Is each base image bound to reviewed content? | Every Dockerfile stage, effective image arguments, retained build provenance and platform-specific resolved base-image digests, with existing tag-to-digest and manifest/index history. | Explicit approved registry/base-image repository and reviewed digest pins, with controlled updates. | Tags are mutable; index and platform-manifest digests differ. Pinning does not supply security updates automatically. |
| Do release and deployment digests agree? | Existing artifact checksum, registry manifest, provenance subject and deployment/admission records. | Bind the exact consumed digest to reviewed release inputs and verification results. | A matching digest proves identity, not benign code; SBOM/scanner presence is not a safety verdict. |
| Is the signer trusted for this artifact? | Retained signature-verification result, trusted key/identity policy, issuer, certificate identity, transparency evidence and signing audit metadata, including trusted-root/policy version and verification time. | Verify signature and artifact binding against an approved signer/key and issuer; constrain builder identity, source and build parameters, with revocation/rotation handling. | A cryptographically valid signature from an unexpected identity is insufficient; signatures/provenance do not prove harmlessness. Never expose key material. |
| Is independent rebuild evidence available? | Existing independent rebuilder identity, source revision, recorded environment/toolchain, input digests, build recipe, output hashes and comparison report/method. | Compare the specified release artifacts bit-for-bit using independently produced rebuild evidence with matching declared inputs. | A second job on the same compromised builder is not independent. Missing evidence is unverified; differences may be nondeterminism, not tampering. Do not claim reproducibility from provenance alone or rebuild here. |
| Are supply-chain alarms operating continuously? | Enabled registry/source-drift, digest/signer/provenance mismatch and dependency-advisory rules; recent alert delivery, triage tickets, freshness and ownership records. | Ongoing monitoring with accountable responders, defined response times, verified delivery and rollback/escalation procedures. | Rule existence or a quiet dashboard proves neither delivery nor coverage; cite gaps in retention, ingestion and external dependencies. |
| Which evidence is missing? | Evidence inventory linking each claim to retained reports, with missing inputs, inaccessible builder logs and verification failures marked explicitly | Record verified/contradicted/unknown per claim, owner and follow-up; gate release per policy | No rebuild or signer evidence means unknown, not trusted or compromised; this review does not perform builds or retrieve suspicious artifacts |

Report policy expectations separately from observed enforcement. Route suspected compromise to the incident owner and preserve minimal existing evidence; do not reproduce tampering or test production containment.

## References

- [SLSA v1.2: Verifying artifacts and provenance](https://slsa.dev/spec/v1.2/verifying-artifacts)
- [Sigstore: Signature, identity and digest verification](https://docs.sigstore.dev/cosign/verifying/verify/)
- [Docker: Base-image selection and digest pinning](https://docs.docker.com/build/building/best-practices/)
- [Reproducible Builds: Definition and bit-for-bit verification](https://reproducible-builds.org/docs/definition/)
