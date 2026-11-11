---
name: offensive-cicd-secrets
description: "Audit CI/CD secret exposure without revealing or transmitting secret values."
---

# CI/CD secret exposure: defensive audit

This skill is for authorized, read-only review of pipeline configuration and controls. Never print, copy, transmit, decode, or validate a real secret value. Do not add a workflow that exfiltrates credentials or runs untrusted code with production secrets.

## Review workflow

1. Confirm repository, runner, environment, and identity scope in writing. Use a non-production project and synthetic credentials for any approved validation.
2. Inventory which workflows can access secrets, environment-scoped variables, deployment credentials, cloud identity, signing keys, and runner-local credentials.
3. Trace trust boundaries: pull requests from forks, reusable workflows, untrusted branch refs, artifacts, caches, package scripts, and privileged event triggers.
4. Verify least privilege, environment approvals, short-lived identity federation, and runner isolation through configuration review.
5. Check whether logs, artifacts, caches, test reports, and debug output could expose values. Verify masking configuration without rendering any value.
6. Review outbound network policy and retention controls. Use metadata-only evidence; do not send test secrets to an external receiver.
7. Record findings with file/setting references, impact, uncertainty, and remediation. If exposure is suspected, follow the owner's rotation and incident process.

## Safer validation

- Use synthetic, uniquely labeled dummy values in a disposable test project, with no production permissions and no external network route.
- Validate that policy blocks access or redacts output by checking a pass/fail result—not by printing or collecting the dummy value.
- Prefer static policy checks and platform audit logs. Do not enable debug logging in a production workflow to inspect secret handling.

## Common controls

- Scope secrets to the smallest repository, environment, and workflow that needs them.
- Prefer short-lived, audience- and subject-bound OIDC credentials over long-lived cloud keys where supported.
- Require approvals for protected environments and restrict privileged workflow triggers.
- Use isolated ephemeral runners for untrusted jobs; prevent unsafe cache or artifact sharing across trust boundaries.
- Rotate credentials after suspected exposure and preserve relevant audit evidence.

## Scope and safety

Testing is limited to explicitly authorized repositories and disposable test credentials. Never access or disclose secret values, disable masking, bypass approval gates, alter production workflows, or attempt to assume cloud roles as part of this review.

## References

- [GitHub: Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
- [GitLab: CI/CD variable security](https://docs.gitlab.com/ci/variables/)
- [OWASP: Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/)

## Metadata-only evidence review matrix

Use owner-provided sanitized metadata exports only. Never read credential stores, variable values, Vault secret responses, helper output, tokens or raw logs that may contain them. Evidence records contain object IDs, scopes, timestamps and access outcomes, not secret values. Check installed version, edition, plugins and enabled auditing before claiming coverage.

| Review question | Existing evidence | Expected control | Limitation |
|---|---|---|---|
| Which GitLab jobs can reach protected material? | Sanitized variable protection/environment metadata, pipeline refs, job-token permission settings and available audit events | Protected refs/environments, narrow job-token access, approvals and isolated runners | Masking does not stop malicious job code; protected/masked availability depends on configuration and version |
| Which Jenkins jobs/agents can use credentials? | Credential ID/scope only, folder/job ACL exports, pipeline references, agent labels and existing access/change audit metadata | Least privilege by folder/job, trusted pipeline changes, agent isolation | Plugin/version and configured audit support determine visibility; masking is not an access boundary |
| Are Vault requests consistent with policy? | Sanitized audit request time, identity/entity reference, operation/path, result and policy metadata | Narrow policies, short-lived identities and reviewed unusual reads/denials or new source/job combinations | Audit availability and exemptions must be checked; raw audit requests/responses can be sensitive and are not review inputs |
| Is registry authentication isolated? | Sanitized helper-name/registry mapping, credential-store ACL attestation and registry access metadata: principal, repository, action, time, outcome | Approved credential helpers, minimal repository rights, no shared runner credential context | Do not invoke helpers or inspect auth fields; helper configuration alone does not prove secure storage or correct runtime use |
| Are runner identities overprivileged or anomalous? | Existing runner/service-account/OIDC subject-audience mappings, role grants, job IDs and sanitized identity-provider/registry access events | Per-job short-lived identity, narrow audience/subject binding and cross-job isolation | Shared hosts, incomplete audit retention and legitimate release bursts complicate attribution; unusual access needs corroboration |

### Additional official references

- [Jenkins credential scope](https://www.jenkins.io/doc/book/using/using-credentials/)
- [Vault audit logging and exceptions](https://developer.hashicorp.com/vault/docs/audit)
- [Docker credential stores and helpers](https://docs.docker.com/reference/cli/docker/login/)
