# Your first SOC project: investigate suspicious sign-ins

Update: a working AI-assisted analysis tool and reference report are now included. Start with LEARN_WITH_ME.md for the guided walkthrough, your personal tasks and accurate CV wording. Reference work is complete; your own analyst review is still pending.

**Time:** About 45-60 minutes. **Coding:** None. **Cost:** None.

This is a fictional training exercise using synthetic application logs. No real accounts, targets or credentials are involved. You can complete it by reading the log in a text editor and filling in the incident report below.

The goal is to practise the same investigation and documentation habits described in SOC placement adverts: review an alert, compare events, identify suspicious patterns, separate evidence from assumptions and recommend the next action.

## Scenario

You are a placement analyst helping a senior SOC analyst. An alert has flagged repeated failed logins to a fictional staff portal on 1 September 2026. Review `synthetic_authentication.log` and decide what should be escalated.

All times are UTC. Each line is an application event with a unique ID. `FAILURE` means a password was rejected; `SUCCESS` means the application accepted the sign-in. `MFA` describes whether the event recorded an additional authentication check. The IP ranges used are reserved for documentation. Do not look them up or treat them as real attackers.

## What to do

1. Read the log once to understand a normal sign-in.
2. Group events by source IP and then by account. Counting on paper is fine.
3. Identify a source trying multiple accounts, and a source repeatedly trying one account.
4. Find any successful sign-in after suspicious failures. Record the account, source, timestamp and event ID.
5. Check whether the successful sign-in shows MFA. Be clear about what this does and does not prove.
6. Fill in `incident_report_template.md`. Describe only what the log supports.
7. Compare your report with `review_notes.md` after finishing, then make corrections.

## What to save as your portfolio

- The synthetic log and your completed incident report.
- A short README explaining that you analysed a fictional dataset manually.
- Your own explanation of the suspicious sequence, including exact event references.
- A short reflection: what evidence was missing, what you would ask a senior analyst, and what you would investigate next.

If you later use this on your CV, describe it as a **self-directed simulated authentication-log investigation**. Do not claim real incident-response experience or use of Splunk, Sentinel or an EDR tool unless you actually used those tools.

Possible CV wording **only after you finish and can explain it**:

> Analysed 24 synthetic authentication events, distinguished repeated attempts against one account from attempts across multiple accounts, and documented a suspicious successful sign-in with evidence references and recommended follow-up checks.

Your placement CV currently does not claim this project is completed.
