---
name: offensive-shellcode
description: "Shellcode concepts and defensive analysis for authorized isolated labs. Use for static triage, telemetry interpretation, and mitigation review; not for payload construction, deployment, or evasion."
---

## Shellcode Analysis and Triage Workflow

1. Confirm written authorization, scope, and approved existing evidence sources.
2. Identify the platform and analyze code statically first.
3. Use existing analysis reports or synthetic telemetry for validation; do not execute samples or test stubs.
4. Record hashes, telemetry, and results; preserve evidence and logs.
5. Stop if validation could affect production or third-party systems.

---

## Basic Concepts

### Memory-permission changes

A sample may move memory from writable to executable before transferring control. This can be a useful detection signal when correlated with process lineage and behavior, but it is not inherently malicious. Prefer platform memory protections and application-control policies; review unexpected private executable regions in context.

### Position-Independent Code (PIC) Techniques

| Method | Platform | Notes |
|--------|----------|-------|
| Call/Pop | Windows | Push next addr, pop into register |
| FPU state | Windows | `fstenv` saves instruction pointer |
| SEH | Windows | Exception handler stores EIP |
| GOT | Linux | Global Offset Table |
| VDSO | Linux | Kernel-provided shared object |

---

## Static API-resolution indicators

Review only existing disassembly or analyst reports for process-environment/loader-list references, module-name comparisons or hashes, export-table parsing, and dynamically resolved APIs. Record file hash, offsets, architecture and uncertainty; do not turn these observations into an implementation sequence. Sparse imports and dynamic resolution also occur in benign software.

There is no fixed loader-module order to rely on. Internal Windows structures and offsets are build/architecture dependent; use matching symbols and authoritative documentation rather than an assumed executable/ntdll/kernel32 ordering. No debugger commands, loader construction or sample execution are required here.

---

## Static artifact triage

- Compare PE sections, imports, resources, certificate metadata, and file overlays with a known-good build where available.
- Runtime API resolution or sparse imports can justify closer review, but neither proves maliciousness.
- Treat packed, encrypted, or high-entropy regions as triage indicators. Do not execute or unpack untrusted material as part of this review.
- Do not infer that a PE remains validly signed after modification. Verify the signature and its coverage with trusted tooling.

## Detection engineering

Correlate executable private memory, cross-process access, permission changes, unusual thread starts, and process ancestry. Validate detection logic against existing sanitized telemetry or synthetic records, not executable artifacts or payloads. Preserve event logs and sample provenance.

---

## Platform-specific analysis notes

- **Windows:** interpret process environment and loader structures using symbols and documentation matching the exact OS build. Treat PEB inspection or dynamic export resolution as context, not a verdict.
- **Linux:** review executable mappings and process behavior with approved forensic telemetry; account for kernel version and security policy. Do not assume an eBPF feature is available or executable by unprivileged code.
- **macOS:** inspect code-signing state, entitlements, notarization, and launch behavior. Do not alter sealed system volumes or install persistence for a detection test.

---

## Safe Lab Validation and Defensive Review

Use this reference only for systems and experiments explicitly authorized in writing. Limit validation to existing analysis reports and synthetic telemetry; lab isolation or separate authorization does not permit sample execution under this skill. Do not build or deploy covert loaders, callback payloads, credential theft, persistence, or evasion mechanisms from this document.

For learning and defensive validation:

- Review existing disassembly and analyst reports statically; do not execute shellcode or other samples.
- Use synthetic event records, not executable test stubs. No callbacks, process injection, or endpoint-security bypasses.
- Assess execution behavior only through existing analysis reports or synthetic telemetry; record provenance, collection context and uncertainty without executing the artifact.
- Record hashes, process/memory events, and detections; preserve logs and artifacts for analysis rather than clearing them.
- For defensive testing, review controls against existing sanitized telemetry or synthetic records, and coordinate scope and stop conditions with the system owner.

## Evidence review matrix

| Review question | Existing evidence | Expected control | Limitation |
|---|---|---|---|
| Are executable mappings unexpected? | Approved existing memory-map export: process identity, region type, permissions, capture time; compare known-good JIT activity | Memory protections (DEP/NX, W^X where supported), reviewed exceptions | Snapshot coverage is partial; JIT/private executable memory is not proof of shellcode; do not change permissions or execute samples |
| Is application control enforced? | Existing policy export and allow/block/audit events correlated to image identity and signer | Application Control policy with reviewed trust rules and enforcement evidence | Audit mode is not enforcement; a trusted signer is not proof of safety; platform/build support differs |
| Can the behavior actually be observed? | Existing EDR/process/memory events, enabled sensor configuration, retention window and dropped-event counters | Document coverage, correlation keys and collection health | API calls and memory transitions may not be collected; no event is not evidence of absence |

## Official platform reference

- [Microsoft: PEB_LDR_DATA](https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb_ldr_data): internal structure may change; use build-matched symbols. No fixed module ordering is assumed.
