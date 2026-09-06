# Review notes - read after completing the investigation

This is an answer guide to the fictional exercise, not a report of real activity.

- `198.51.100.23`: 10 failed sign-ins, zero successes, five distinct accounts. E005-E009 and E019-E023 show two rounds of attempts across those accounts. This is consistent with a password-spraying pattern, but the log does not show the attempted passwords; you cannot prove that the same password was reused.
- `203.0.113.44`: six failures followed by one success against `ellis`, E011-E017. The rapid repeated attempts are suspicious. E017 at 09:02:30 UTC should be prioritised for review because authentication succeeded and MFA was not required.
- A successful login is not proof of account compromise. Check whether the user recognises it, the device and session context, the identity provider's records and any actions after the login. The log does not show access to files or data exfiltration.
- E003-E004 show one failed attempt followed by a successful MFA-protected sign-in from the same source. This could be a normal mistyped password. It is less concerning than the repeated sequences, but is not automatically guaranteed benign.
- Preserve the evidence, record the event IDs and escalate the suspicious success to the senior analyst. Propose validation of the session and MFA policy, and containment according to the organisation's approved procedures if compromise is suspected. Do not say you blocked an IP or reset an account in this exercise.

There are 24 events in total: 17 failures and seven successes. The counts and a clear, cautious assessment matter more than dramatic language.
