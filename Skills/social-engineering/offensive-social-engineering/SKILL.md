---
name: offensive-social-engineering
description: "Run tabletop social-engineering awareness exercises without covert contact or access attempts."
---

# Social-engineering awareness: tabletop and prevention

This skill supports awareness planning and defensive control review. Do not impersonate staff or vendors, contact real employees with deceptive pretexts, attempt facility entry, clone badges, bypass locks, plant devices, or collect credentials.


## Evidence-based defensive review

Review authorized policies and existing sanitized records only. For each finding cite evidence location, time window, owner and coverage. Missing evidence is unknown, not a passed control.

| Question | Existing evidence | Expected control | Limitation |
|---|---|---|---|
| Are urgent phone requests independently verified? | Help-desk identity-check policy and existing sanitized reset/payment approval tickets. Approved help-desk verification procedure and synthetic call transcript | End suspicious calls; call back through a trusted directory, require independent approval, and report requests for passwords or MFA codes. End the request, call back via an independently known directory number, report; never share codes or approve unexpected prompts | Caller ID, familiar voices and claimed authority do not authenticate a caller; policy alone proves no compliance. Caller ID and familiar voices are not reliable identity evidence |
| Are SMS requests handled safely? | Existing reported-message metadata and mobile reporting guidance. Synthetic message card and existing reporting procedure | Do not follow unexpected links, reply or approve MFA prompts; use the known official app/contact and report. Do not reply or follow links; use the known-good app/contact and report | Familiar sender threads and polished wording can mislead; missing mobile telemetry limits assurance. Sender names and existing conversation threads can be misleading |
| Are unusual access requests escalated? | Visitor/escort policies, authorized badge-event summaries and facilities incident tickets. Existing visitor/escort policy and sanitized access-incident summaries | Verify visitors through reception, require escorts and report tailgating or lost badges without confrontation. Follow reception/escort procedure, contact security without confrontation | A badge event does not establish who crossed a door; no entry attempts or covert observation are authorized. Badge appearance and familiarity do not establish authorization; do not attempt entry tests |
| Are unexpected media/devices isolated? | Existing media policy, endpoint device-control events and inventory exceptions. Existing device-control policy and sanitized device-block records | Do not connect found USB media or unknown devices; notify IT/security and follow safe handover procedures. Do not connect it; hand it to the designated security process | Device-control coverage varies; no media planting, mounting or execution is permitted. Labels and packaging are not provenance; do not open contents to identify the owner |
| Are watering-hole warning signs recognized? | Existing browser/proxy/endpoint alerts and sanitized reports of unexpected login, update or download prompts on familiar sites. Existing sanitized web-proxy/browser alert and help-desk report, if available | Close the page, avoid downloads and credentials, report via a known channel, and let incident owners assess existing records. Stop interaction, use independently verified support/reporting; do not install prompted updates | A trusted site or TLS lock is not proof of safe content; do not revisit suspected pages to reproduce behavior. A familiar site may be compromised; TLS and reputation alone do not establish safe content; do not revisit it to reproduce |

## Fictional, moderated tabletop

Obtain security, privacy, HR and facilities approval. A facilitator presents fictional phone/SMS, visitor, found-media and familiar-site prompt cards, then pauses for the safe reaction, trusted verification route and escalation owner. No real calls/messages, impersonation, site visits, badge/lock interaction, recordings, planted devices or credential collection. Use synthetic records only; stop for distress, real personal data or operational impact. Debrief without blame, retain aggregate decisions only, and assign control improvements with owners.

## References

- [CISA: Recognize and Report Phishing (archived awareness guidance)](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing)
- [NIST SP 800-50 Rev. 1: Learning program design and evaluation](https://csrc.nist.gov/pubs/sp/800/50/r1/final)

## Fictional decision scenario

A fictional colleague receives an urgent SMS, then a purported support call asking them to open a familiar supplier site and attach a delivered USB device. No message is sent, call placed, website visited or device connected. **Learning goal:** verify each channel independently. **Moderator question:** “Which independent contact and reporting path do you use before acting?” **Expected reaction:** stop, use the known directory/support channel, leave media disconnected and involve facilities/security if access is requested. Record aggregate decisions and gaps in the written procedure, not personal susceptibility.
