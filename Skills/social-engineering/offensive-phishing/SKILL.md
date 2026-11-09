---
name: offensive-phishing
description: "Design safe, authorized phishing-awareness exercises without collecting credentials."
---

# Phishing awareness: safe simulation design

Use this reference for tabletop exercises or approved click-only awareness simulations. It does not support real credential collection, session-token capture, executable payload delivery, filter bypass, or impersonation of third parties.

## Exercise prerequisites

1. Obtain written approval from the organization's security, legal, privacy, and communications owners.
2. Define the recipient group, schedule, data collected, retention period, notification plan, and stop conditions.
3. Use an organization-controlled training domain and landing page. Do not register lookalike third-party domains or use external redirection services.
4. Make the exercise inert: no login fields, password prompts, cookies, tokens, attachments, macros, downloads, QR redirects, or code execution.
5. Collect only the minimum aggregate outcome needed, such as click/no-click counts. Avoid recording message contents, personal browsing data, or sensitive identifiers.
6. Provide a clear debrief and a non-punitive reporting path. Delete or aggregate exercise data under the approved retention plan.

## Tabletop alternative

Use synthetic personas, mock messages, and facilitator-led decision points. Discuss reporting, verification, and escalation without sending messages to real recipients or collecting responses from real accounts.

## Defensive review checklist

- Confirm external sender labeling, domain authentication, attachment controls, URL inspection, and reporting workflows.
- Review training materials for accessibility, privacy, and non-punitive language.
- Measure aggregate reporting and response time, not credential entry or individual susceptibility.
- Coordinate with help desk and incident response so the exercise does not trigger unplanned containment actions.

## Stop conditions

Stop immediately if the exercise reaches an unintended recipient, requests or receives credentials, causes operational disruption, or collects data outside the approved plan. Notify the owner and preserve only the minimum evidence required for the incident review.

## References

- [CISA: Recognize and Report Phishing](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing)
- [NIST SP 800-50 Rev. 1: Building a Cybersecurity and Privacy Learning Program](https://csrc.nist.gov/pubs/sp/800/50/r1/final)
