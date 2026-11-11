---
name: offensive-dependency-confusion
description: "Review dependency source policy and prevent package-confusion risks."
---

# Dependency source confusion: defensive review

Use this skill to assess package-source configuration, namespace ownership, and lockfile integrity in authorized repositories. Do not publish lookalike packages, trigger installs, register public placeholders, or collect callbacks. A package being absent from a public registry is not proof of a vulnerability.


## Evidence-based source review

Use authorized, existing configuration and sanitized telemetry only. Record tool version, operation, overrides, evidence location, time window and coverage. Missing telemetry is unknown; public-name availability is not proof of exposure. Never install, resolve, publish packages or execute hooks to demonstrate a finding.

| Question | Existing evidence | Expected control | Limitation |
|---|---|---|---|
| Are npm sources constrained? | Effective sanitized .npmrc scope/default registry mappings, lockfile resolved URLs/integrities and existing build/registry request logs. | Map private scopes to approved registries and review lockfile/source changes. | Scope mappings, overrides and operation matter; a missing mapping alone does not prove fallback. |
| Are pip candidates constrained? | Existing index/extra-index/find-links settings, environment override names, pinned hashes and build/registry logs. | Restrict all candidate locations to approved sources and review pinned artifacts. | An index URL alone does not exclude other sources; version priority is not a universal source policy. |
| Are NuGet and JVM sources constrained? | NuGet.Config mappings; Maven mirrors/settings; Gradle content filters; lock/dependency verification files and retained restore logs. | Explicit package-source mapping or repository content rules, approved immutable versions and reviewed changes. | Source order is not universally authoritative; behavior depends on manager, version and operation. |
| Are Go module routes and private paths controlled? | go.mod, go.sum, go.work/vendor metadata where present; sanitized GOPROXY, GOPRIVATE, GONOPROXY, GONOSUMDB settings; existing CI module-download and proxy/registry logs. | Match module paths to approved proxy/VCS routes; review replace/workspace overrides and deliberate private-path checksum policy. | GOPROXY comma fallback normally follows 404/410; pipe fallback follows any error. GOPRIVATE supplies defaults for GONOPROXY/GONOSUMDB, not an allowlist. go.sum is an integrity record, not a source lockfile or safety verdict. |
| Are Ruby gem sources explicit? | Gemfile source blocks/:source/git/path declarations, Gemfile.lock remotes/revisions, Bundler version/config and retained build/registry logs. | One approved global source; explicitly bind private gems and review transitive dependencies and lockfile source changes. | Multiple global sources are deprecated; source blocks can affect available sources for other gems. A lockfile alone does not prove approved origin or harmless install behavior. |
| Are container dependency sources explicit? | Dockerfiles for every stage, build argument values, image lock metadata if used, retained build/pull and registry audit logs with resolved digests/platforms. | Fully qualify approved registry/namespace and base images, pin reviewed digests, and constrain mirrors/proxies. | Short names, mutable tags and cache hits obscure origin; an image digest proves content identity, not publisher trust or safety. |

Use existing build-to-lockfile-to-registry correlations to distinguish intended policy from observed resolution. Do not fetch missing artifacts, enumerate public names or run builds. Report unresolved routes with an owner rather than asserting exploitation.

## References

- [Go: Module reference, proxies and private modules](https://go.dev/ref/mod)
- [RubyGems/Bundler: Gemfile sources and source priority](https://guides.rubygems.org/gemfile/)
- [Docker: Base-image selection and digest pinning](https://docs.docker.com/build/building/best-practices/)
