---
name: offensive-anti-forensics
description: "Detect forensic tampering and preserve evidence in authorized investigations."
---

# Forensic tampering: detection and preservation

This reference supports incident responders and authorized detection exercises. It describes adversary behavior at a high level and focuses on observable evidence. Never use it to disable telemetry, alter timestamps, clear logs, destroy artifacts, or evade analysis.

## Behaviors to recognize

- **Log tampering:** unexpected clearing, gaps, service restarts, policy changes, or collection-agent outages.
- **Timestamp manipulation:** file metadata that conflicts with journal, USN, filesystem, backup, or endpoint telemetry.
- **Artifact removal:** sudden history, audit, journal, or application-record changes inconsistent with normal retention.
- **Concealment:** unexpected alternate data streams, unusual archive/container contents, or files in atypical locations.
- **Analysis evasion:** processes that behave differently in monitored environments, unexplained delays, or conditional execution.
- **Network concealment:** unexpected encrypted DNS, unusual resolver use, or long-lived low-volume connections. These are leads, not proof of command-and-control.

## Investigation workflow

1. Confirm authority, incident scope, evidence owner, and retention requirements.
2. Preserve volatile and nonvolatile evidence before making changes. Record source, collection time, time zone, tool/version, and cryptographic hashes.
3. Acquire logs from independent sources: endpoint, identity, network, cloud control plane, and centralized collectors. Compare their time ranges and gaps.
4. Correlate file metadata with filesystem journals, backups, endpoint records, and application logs. Treat timestamps as claims, not standalone proof.
5. Document missing or altered evidence explicitly. Do not attempt to reconstruct or silently normalize it.
6. Contain through approved response procedures while preserving chain of custody; record every action and operator.

## ATT&CK references

MITRE ATT&CK T1070 covers Indicator Removal on Host. Use the current ATT&CK technique and sub-technique pages to map a specific observed behavior; do not infer a sub-technique from a tool name or artifact alone. In particular, verify exact identifiers before publishing a mapping.

## Safe validation

Use tabletop scenarios, vendor-provided benign test artifacts, or isolated disposable systems. Do not clear, modify, or delete logs or evidence during a detection exercise. Agree on scope, data handling, stop conditions, and restoration with the owner in advance.

## References

- [MITRE ATT&CK: Indicator Removal](https://attack.mitre.org/techniques/T1070/)
- [NIST SP 800-86: Guide to Integrating Forensic Techniques into Incident Response](https://csrc.nist.gov/pubs/sp/800/86/final)
