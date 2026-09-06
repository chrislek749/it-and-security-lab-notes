# Worked incident report: suspicious authentication

Status: AI-prepared reference analysis, not yet independently reviewed by Olamilekan.
Environment: fictional staff portal; 24 synthetic events on 1 September 2026, all times UTC. No live systems investigated.

## Decision

Escalate the ellis sign-in sequence for prompt senior-analyst review. E011-E016 show six rejected attempts from 203.0.113.44 between 09:02:00 and 09:02:25. E017 records a successful sign-in for the same account and source at 09:02:30 with MFA NOT_REQUIRED. This is a suspicious sequence, not proof that an attacker gained access or that data was stolen.

## Evidence

| Finding | Evidence | Interpretation |
|---|---|---|
| Ten failures across five accounts from 198.51.100.23 | E005-E009 and E019-E023, 09:00:00-09:04:40 | Multi-account guessing pattern; consistent with spraying, but passwords are unavailable so the exact technique is unproven |
| Six failures followed by success for ellis from 203.0.113.44 | E011-E017, 09:02:00-09:02:30 | Possible successful guessing; legitimate retries are an alternative |
| One failure followed by success and MFA for chen | E003-E004, 08:57:00-08:57:30 | Lower-priority comparison; compatible with a typo but not verified as benign |

The dataset contains 17 failures and 7 successes. Ten failures belong to the multi-account source, six to the ellis source, and one to chen's ordinary-looking sequence. The rules generate three first-trigger alerts at E009, E015 and E017; these are overlapping detections, not three proven incidents.

## Recommended next checks

1. Preserve relevant authentication and session logs and ask the senior analyst to validate the account and source against normal activity
2. Contact the account owner through an established channel to verify the sign-in
3. Review session activity, device context and identity-provider MFA policy; NOT_REQUIRED records an outcome, not the reason for it
4. If unauthorised access is confirmed or strongly suspected, follow the organisation's approved process for session revocation, credential reset and MFA remediation
5. Investigate the multi-account source separately; do not assume it is the same actor as the ellis source

No containment was performed in this exercise. IPs use documentation ranges and must not be treated as real indicators to block.

## Limitations

No user-agent, location, device, password, session activity, asset criticality or business context is available. Shared gateways can make distinct users appear under one IP. A five-failure threshold is a teaching choice, not a validated production rule. The small file cannot establish detection accuracy or false-positive rates.
