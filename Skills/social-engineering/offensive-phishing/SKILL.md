---
name: offensive-phishing
description: "Design safe, authorized phishing-awareness exercises without collecting credentials."
---

# Phishing awareness: safe simulation design

Use this reference for defensive evidence review and facilitator-led tabletop exercises only. It does not support real credential collection, session-token capture, executable payload delivery, filter bypass, or impersonation of third parties.


## Evidence-based defensive review

Use only authorized, existing, sanitized records. Record evidence location, time window, owner, and coverage; mark unavailable evidence as unknown, not passed. Never retrieve credential or token values.

| Question | Existing evidence | Expected control | Limitation |
|---|---|---|---|
| Does the apparent sender match the authenticated domain and delivery path? | Sanitized From/Reply-To, Return-Path, trusted Received hops, gateway Authentication-Results (SPF/DKIM/DMARC), message trace and verdicts. | Domain alignment, external labels, attachment/URL controls, and a reporting route. | Trust only headers added within the receiving trust boundary; forwarding can affect authentication. Authentication success does not prove benign intent. |
| Do message and identity signals agree? | Existing gateway detections, user reports, IdP sign-in risk, device/session metadata, MFA/reset and consent audit events (time, account, application, device, source, method and outcome) correlated by time. | Triage correlated anomalies and escalate through the incident owner; preserve minimal evidence; review conditional access, independent verification and session response by authorized responders. | Risk scores, IP changes, and unusual geography are signals, not proof; retention and licensing constrain coverage; session compromise may not produce a new login. |
| Is phishing-resistant MFA enforced? | Effective IdP authentication-strength policies, scoped users/apps, exclusions, enrollment and sanitized sign-in method results. | Require FIDO2/WebAuthn passkeys with verifier-name binding or other provider-supported phishing-resistant methods; review enrollment, recovery, legacy authentication and exceptions; verify effective policy enforcement. | SMS, OTP and push approval alone are not phishing-resistant; enrollment is not enforcement and MFA does not eliminate session compromise. |
| Can staff report safely and responders act? | Existing reporting tickets, response timestamps, escalation policy and approved aggregate training outcomes. | Known-good verification channels, non-punitive reporting, accessible guidance and an accountable responder. | Awareness metrics do not establish technical prevention or individual susceptibility. |

## Facilitator-only tabletop

With written owner approval, use fictional personas, inert mock message cards and synthetic mail-header/IdP event summaries. A moderator pauses at each decision: identify signals, verify through a known-good channel, report, then assign incident triage. Send nothing, open no links, and use no real accounts, QR codes, login fields, attachments or response tracking. Record aggregate decisions and control gaps, not participant rankings. Stop for distress, real personal data, credentials or operational impact; debrief and assign improvements.

## References

- [Microsoft: Anti-spam message headers](https://learn.microsoft.com/en-us/defender-office-365/message-headers-eop-mdo)
- [Microsoft: Authentication strengths](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths)
- [CISA: Recognize and Report Phishing (archived awareness guidance)](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing)
- [NIST SP 800-50 Rev. 1: Learning programs](https://csrc.nist.gov/pubs/sp/800/50/r1/final)

## Synthetic tabletop decision point

**Learning goal:** independently verify a request and report it without submitting credentials. **Inject:** a fictional employee receives a printed mock urgent account notice; no real address, link, QR code or login form exists. **Moderator question:** “The mock header says authentication passed but the request asks for an unexpected sign-in; what do you trust and what do you do?” **Expected reaction:** do not follow the request, open the known-good service independently, report through the established channel, and let authorized responders correlate sanitized mail/IdP records. Debrief aggregate reasoning and response time, not individual blame.

- [NIST SP 800-63B-4: phishing resistance](https://pages.nist.gov/800-63-4/sp800-63b.html)
