# Completed desktop casework

6 September 2026

The offline analysis and written assessments below are complete. These are fictional exercises, with no live account investigation, repaired client machine or installed media server. The supplied Python tool and case assessments were produced on request; they do not establish independent programming or hands-on investigation by the portfolio owner.

## Authentication investigation

The analyser processed all 24 events: 17 failures and 7 successes. Four unit tests passed, covering the supplied dataset, benign retries, failures outside the five-minute window and separation between accounts.

The highest-priority review sequence is E011-E017: six failed attempts followed by a successful sign-in for ellis from 203.0.113.44. E017 records MFA NOT_REQUIRED. This calls for account-owner verification, device/session context and a review of the applicable MFA policy. It does not prove compromise or MFA bypass.

E005-E009 and E019-E023 show ten failures across five accounts from 198.51.100.23. This supports investigation of multi-account guessing. Without attempted passwords, password spraying cannot be established. The three first-trigger alerts (E009, E015, E017) overlap; they are not three confirmed incidents. No accounts were blocked or reset.

Evidence: authentication-lab/results/findings.json, authentication-lab/results/events.csv and WORKED_REPORT.md.

## Phishing triage

P01 is suspicious because it requests a password under time pressure and uses unapproved and mismatched domains. Passing SPF, DKIM and DMARC for a sender domain does not establish that the sender is the employer. P02 remains uncertain: an expected bank change and passing authentication do not independently validate new payment details. P03 has lower concern because the workshop is expected and there is no link or attachment; the existing portal bookmark provides a separate check.

User response for P01:

Please do not open the link or reply with your password. The message uses a domain that is not listed as an approved company service, and its reply address is different. Report it through the usual security reporting route, using contact details you already know. If you entered your password, contact IT straight away so they can review the account and guide the next steps. Keep the email available for investigation. A message passing email authentication can still come from an unapproved sender, so that result does not make this password request safe.

False-positive consideration: an approved external helpdesk may use another domain. Confirm that through existing internal records, not through contact details supplied in the suspicious message. No links or attachments were opened.

Evidence: phishing-triage/triage.csv and messages.txt.

## IT support handover

T01: One desktop shows No Signal. Begin with the selected monitor input and external cable, then compare with an approved spare. A graphics-card fault is only one possible explanation. Record the actual result before escalating. No internal repair or powered component work is proposed.

T02: One new starter is denied a project share while another user can access it. A general network outage is less likely; check the exact path, identity and authorised access group. Obtain access-owner approval before any permission change. Do not use Everyone permissions as a workaround.

T03: The snapshot shows memory at 91% and storage 98% full, with CPU at 12%. Preserve unsaved work and agree a suitable time to inspect application memory and storage use. Those figures are clues, not a diagnosis. No deletion, restart or security-tool change has been performed. Any future improvement must be measured with the same operation before and after.

All cases need urgency and business-impact confirmation before assigning a priority. The written triage is finished; proposed device checks remain unperformed.

Evidence: it-support/tickets.csv and cases.txt.

## PC build and media server

The owner confirmed assembling the CPU, GPU, RAM and PSU of their personal PC. No component models or benchmark results are claimed. The media-server design remains a plan: installation and playback/access testing require the actual OS, hardware and available storage.
