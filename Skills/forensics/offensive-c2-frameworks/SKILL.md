---
name: offensive-c2-frameworks
description: "Review command-and-control indicators and defensive controls in authorized environments."
---

# Command-and-control: defensive review

Use this reference to assess detection coverage and investigate suspected C2 activity. It does not provide implant, redirector, listener, credential-access, or evasion instructions. Do not deploy C2 software or contact infrastructure unless a separate written authorization explicitly permits it; prefer telemetry-only simulations.

## Behavior patterns

- Repeated outbound connections with unusual timing or process lineage.
- DNS requests with atypical volume, response sizes, entropy, or resolver paths.
- Rare destinations, newly observed domains, or network traffic inconsistent with the initiating process.
- Long-lived encrypted sessions or unusual protocol use. Encryption and periodicity alone do not establish maliciousness.
- Unexpected proxy, certificate, or DNS configuration changes.
- Endpoint processes that initiate network activity after suspicious memory or child-process behavior.

## Defensive review workflow

1. Establish written scope, approved telemetry sources, retention, and incident contacts.
2. Review egress policy, DNS resolver configuration, proxy logs, endpoint process lineage, and identity events using read-only access.
3. Correlate network metadata with process, user, device, and cloud records. Preserve packet captures and relevant logs under the incident evidence process.
4. Treat JA3/JA4, TLS certificates, domain age, and beacon-like timing as non-unique signals. Correlate multiple independent indicators before attribution.
5. Validate detection logic with synthetic events or vendor-provided benign test data. Do not create implants, redirectors, callbacks, or covert channels for a routine validation.
6. Document false positives, telemetry gaps, data limitations, and response actions.

## Controls to assess

- Restrict outbound traffic to documented business needs; monitor direct-to-internet access and unapproved DNS resolvers.
- Centralize DNS, proxy, endpoint, identity, and cloud audit telemetry with synchronized clocks and protected retention.
- Alert on anomalous process-to-network relationships and unexpected changes to proxy, resolver, or certificate settings.
- Use allowlists and application controls where practical, with reviewed exceptions and rollback procedures.
- Preserve evidence before containment actions that could terminate processes or remove network state.

## Safe exercise boundary

Prefer tabletop injects, replay of sanitized historical telemetry, and harmless detection test records. Do not use real credentials, external callbacks, live implants, persistence, traffic disguise, or log deletion. Stop if activity reaches an out-of-scope system.

## References

- [MITRE ATT&CK: Command and Control](https://attack.mitre.org/tactics/TA0011/)
- [MITRE ATT&CK: Application Layer Protocol](https://attack.mitre.org/techniques/T1071/)

## Local process and lateral-channel coverage matrix

Only inspect existing sanitized telemetry or synthetic records; do not generate traffic, open pipes, start processes or deploy frameworks. Fix an incident window (UTC start/end) and compare a documented baseline; the example windows below are correlation hypotheses, not universal detection thresholds. Verify deployed sensor/version/configuration and field availability before using a join.

| Review question | Existing evidence (source, fields, window) | Expected control | Limitation / false positive |
|---|---|---|---|
| Can process relationships be reconstructed? | Existing Sysmon process events: UtcTime, host, ProcessGuid, ParentProcessGuid, Image, User; incident window plus 15 minutes on either side | Join by host/process GUID, preserve ancestry and application-control outcome | Retention or sensor gaps break ancestry; installers and management agents spawn unusual children |
| Is IPC/Named Pipe activity attributable? | Existing Sysmon pipe-created/connected records, if enabled: UtcTime, host, ProcessGuid/ProcessId, Image, PipeName; correlate within 5 minutes of process event | Identify expected pipe owners/consumers and flag new process/pipe pairings for review | Named pipes cover only part of IPC; RPC, sockets and shared memory need separate documented sources; legitimate services use pipes |
| Is SMB access tied to identity and endpoint? | Existing Windows share-audit records, if enabled: time, server, account/logon ID, client address, share/relative target, requested access and outcome; correlate within 15 minutes with endpoint/network records | Approved shares, least privilege and cross-host identity correlation | Audit settings determine available fields; backups/admin tools are common false positives; NAT/clock skew and PID reuse weaken joins |
| Can cross-source gaps be distinguished from absence? | Collector health, enabled audit configuration and retention metadata over the full incident/baseline window | Coverage map by host/channel/time and explicit unknown cells | A pipe/SMB event is not a C2 verdict; missing telemetry is not evidence that communication did not occur |

- [Microsoft Sysmon event coverage](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon): process and pipe event availability depends on installed version and filtering; do not assume all events are enabled.
