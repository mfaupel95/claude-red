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
| Are urgent phone requests independently verified? | Help-desk identity-check policy and existing sanitized reset/payment approval tickets. | End suspicious calls; call back through a trusted directory, require independent approval, and report requests for passwords or MFA codes. | Caller ID, familiar voices and claimed authority do not authenticate a caller; policy alone proves no compliance; never share MFA codes or approve unexpected prompts. |
| Are SMS requests handled safely? | Existing reported-message metadata and mobile reporting guidance. | Do not follow unexpected links, reply or approve MFA prompts; use the known official app/contact and report. | Familiar sender threads and polished wording can mislead; missing mobile telemetry limits assurance. |
| Are unusual access requests escalated? | Visitor/escort policies, authorized badge-event summaries and facilities incident tickets. | Verify visitors through reception, require escorts and report tailgating or lost badges without confrontation. | A badge event does not establish who crossed a door; no entry attempts or covert observation are authorized. |
| Are unexpected media/devices isolated? | Existing media policy, endpoint device-control events and inventory exceptions. | Do not connect found USB media or unknown devices; notify IT/security and follow safe handover procedures. | Device-control coverage varies; no media planting, mounting or execution is permitted; labels are not provenance and opening contents to identify the owner is out of scope. |
| Are watering-hole warning signs recognized? | Existing browser/proxy/endpoint alerts and sanitized reports of unexpected login, update or download prompts on familiar sites. | Close the page, avoid downloads and credentials, report via a known channel, and let incident owners assess existing records. | A trusted site or TLS lock is not proof of safe content; do not revisit suspected pages to reproduce behavior. |

## Fictional, moderated tabletop

Obtain security, privacy, HR and facilities approval. A facilitator presents fictional phone/SMS, visitor, found-media and familiar-site prompt cards, then pauses for the safe reaction, trusted verification route and escalation owner. No real calls/messages, impersonation, site visits, badge/lock interaction, recordings, planted devices or credential collection. Use synthetic records only; stop for distress, real personal data or operational impact. Debrief without blame, retain aggregate decisions only, and assign control improvements with owners.

## References

- [CISA: Recognize and Report Phishing (archived awareness guidance)](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing)
- [NIST SP 800-50 Rev. 1: Learning program design and evaluation](https://csrc.nist.gov/pubs/sp/800/50/r1/final)

## Fictional decision scenario

A fictional colleague receives an urgent SMS, then a purported support call asking them to open a familiar supplier site and attach a delivered USB device. No message is sent, call placed, website visited or device connected. **Learning goal:** verify each channel independently. **Moderator question:** “Which independent contact and reporting path do you use before acting?” **Expected reaction:** stop, use the known directory/support channel, leave media disconnected and involve facilities/security if access is requested. Record aggregate decisions and gaps in the written procedure, not personal susceptibility.
