# Start here: your guided SOC project

## What has actually been built

An AI-assisted reference project now exists: a fictional 24-event dataset, an offline Python analysis tool, CSV evidence, three simple detection rules, automated checks and a worked incident report. Codex wrote and ran the tool and drafted the report. You have not yet completed the analyst review. This distinction matters when explaining your contribution in an interview.

You can do the analyst work without coding. Open results/events.csv in a spreadsheet or read synthetic_authentication.log. The Python is optional and readable if you later want to understand automation.

## First lesson: read one event

E017 means: at 09:02:30 UTC, the portal accepted a sign-in for ellis from 203.0.113.44, and its MFA field says NOT_REQUIRED. It does not tell us who was using the account. It also does not show what they did after signing in.

Look at E011-E016 immediately before it: six failed attempts from the same source against ellis. The sequence makes E017 worth escalating. A single success alone would give much less reason for concern.

## Your 30-minute walkthrough

1. **5 minutes:** Read the six column definitions in START_HERE.md. Find E003, E004 and E017 in the raw log
2. **5 minutes:** Filter the CSV to source 203.0.113.44. Count failures and successes yourself; compare with results/evidence_summary.md
3. **5 minutes:** Filter 198.51.100.23. Count accounts, not just events. Explain why ten failures across five accounts differs from six against ellis
4. **10 minutes:** Fill incident_report_template.md in your own words before reading WORKED_REPORT.md. Include event IDs, your escalation decision and two missing pieces of evidence
5. **5 minutes:** Compare with the worked report, correct mistakes and write a short reflection explaining one thing you initially misunderstood

Save your own report as MY_REPORT.md and reflection as MY_REFLECTION.md. These files do not yet exist; creating them is your part of the project.

## How the optional code works

- parse() splits each line into six fields, checks event IDs and sorts by time
- detect() looks back five minutes from each event, grouping by source IP and account
- Five different accounts with failed attempts produces a multi-account alert
- Five failures for one account produces a repeated-failure alert
- A success following five failures for the same account and source produces a success-after-failures alert
- main() writes CSV and JSON plus a readable evidence summary

With Python installed, open a terminal in this folder and run `python analyse.py`, then `python -m unittest -v test_analyse.py`. Standard library only; no package installation is needed. Pre-generated results are included so this is optional.

## Explain it back to me

1. Which event deserves the most urgent review, and why?
2. Does MFA NOT_REQUIRED prove MFA was bypassed?
3. Why can we not say password spraying was definitely used?
4. What harmless situation could trigger the same rules?
5. What did you personally check, change or write, and what did AI help with?

## CV wording

For now: **Guided authentication-log investigation - in progress**. AI-assisted lab prepared; personal analysis pending. Do not use completed-project bullets yet.

After you complete the walkthrough and can explain your report, a supportable bullet is: **Reviewed 24 synthetic authentication events using an AI-assisted analysis tool, investigated repeated and multi-account sign-in failures, and wrote an evidence-based incident report with escalation recommendations**.

Only use that wording after you actually perform those tasks. Do not claim you independently built the Python tool, handled real incidents, or used Splunk/Sentinel.

## Virtual work experience alongside this project

Deloitte Australia Cyber on Forage is free, introductory and about 30-60 minutes. Use the Start Free Simulation button and sign in or register yourself. Complete its tasks yourself; ask for explanations if stuck. Save your certificate and a brief account of what you did. List it as a job simulation or virtual experience, never employment at Deloitte.

https://www.theforage.com/simulations/Deloitte%20Australia/cyber-c1e3
