---
name: offensive-shellcode
description: "Shellcode concepts and defensive analysis for authorized isolated labs. Use for static triage, telemetry interpretation, and mitigation review; not for payload construction, deployment, or evasion."
---

## Shellcode Development Workflow

1. Confirm written authorization, scope, and isolated lab boundaries.
2. Identify the platform and analyze code statically first.
3. Use inert, non-networked test stubs for controlled validation.
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

## Windows API Resolution (PEB Walk)

Identifying `kernel32.dll` without imports:

1. Get `PEB` via `gs:[0x60]` (x64) or `fs:[0x30]` (x86)
2. Walk `PEB->Ldr.InMemoryOrderModuleList` — order: exe → ntdll → kernel32
3. Hash-compare module names to locate `kernel32`
4. Parse the Export Address Table (EAT)
5. Find `GetProcAddress` by name hash, then resolve `LoadLibraryA`
6. Use `LoadLibraryA` to load `WS2_32.dll`, resolve Winsock functions

**WinDbg helpers for debugging PEB walk:**
```bash
dt nt!_TEB -y ProcessEnvironmentBlock @$teb
dt nt!_PEB -y Ldr <peb_addr>
dt -r _PEB_LDR_DATA <ldr_addr>
dt _LDR_DATA_TABLE_ENTRY (<init_flink_addr> - 0x10)
lm m kernel32   # verify base address
r @r8           # check register
```

---

## Static artifact triage

- Compare PE sections, imports, resources, certificate metadata, and file overlays with a known-good build where available.
- Runtime API resolution or sparse imports can justify closer review, but neither proves maliciousness.
- Treat packed, encrypted, or high-entropy regions as triage indicators. Do not attempt to execute or unpack untrusted material outside an approved isolated lab.
- Do not infer that a PE remains validly signed after modification. Verify the signature and its coverage with trusted tooling.

## Detection engineering

Correlate executable private memory, cross-process access, permission changes, unusual thread starts, and process ancestry. Validate detections with benign telemetry or vendor test artifacts, not covert payloads. Preserve event logs and sample provenance.

---

## Platform-specific analysis notes

- **Windows:** interpret process environment and loader structures using symbols and documentation matching the exact OS build. Treat PEB inspection or dynamic export resolution as context, not a verdict.
- **Linux:** review executable mappings and process behavior with approved forensic telemetry; account for kernel version and security policy. Do not assume an eBPF feature is available or executable by unprivileged code.
- **macOS:** inspect code-signing state, entitlements, notarization, and launch behavior. Do not alter sealed system volumes or install persistence for a detection test.

---

## Safe Lab Validation and Defensive Review

Use this reference only for systems and experiments explicitly authorized in writing. Keep validation in an isolated, disposable lab with no route to production or third-party systems. Do not build or deploy covert loaders, callback payloads, credential theft, persistence, or evasion mechanisms from this document.

For learning and defensive validation:

- Review sample assembly and binaries statically; do not execute unknown shellcode on a host containing real data or credentials.
- Use inert, non-networked test stubs and synthetic input. Avoid real callbacks, process injection, or endpoint-security bypasses.
- If execution behavior must be studied, use a disposable VM snapshot with host-only networking, no shared folders or clipboard, and a documented rollback plan.
- Record hashes, process/memory events, and detections; preserve logs and artifacts for analysis rather than clearing them.
- For defensive testing, validate controls through benign telemetry or vendor-provided test artifacts, and coordinate scope and stop conditions with the system owner.
