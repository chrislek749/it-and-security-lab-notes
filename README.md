# IT and Security Lab Notes

Practical case studies covering sign-in analysis, phishing triage, IT support and a home media-server design.

## Finished casework

Read the [completed assessments and support handover](COMPLETED_CASEWORK.md).

- Authentication: 24 fictional sign-ins analysed, with 17 failures, 7 successes and three overlapping rule alerts; all four automated tests pass
- Phishing: [three completed email assessments](phishing-triage/triage.csv), with evidence, missing context and next steps
- IT support: [three completed ticket assessments](it-support/tickets.csv), with diagnostic plans and escalation criteria
- Personal PC: CPU, GPU, RAM and power supply assembled by the owner
- Home media server: [Jellyfin design and test plan](MEDIA_SERVER.md); installation and device testing remain outstanding

The written casework is complete. Physical checks in the support cases are proposed, not recorded as repairs. The portfolio includes supplied code and reference analysis; it does not claim independent programming or personal investigation of live systems.

## Run the log analysis

Python 3.10 or newer; standard library only. From the repository folder:

```text
python analyse.py
python -m unittest -v test_analyse.py
```

The tool creates `results/events.csv`, `results/findings.json` and `results/evidence_summary.md`. The checked-in [findings](authentication-lab/results/findings.json) and [event table](authentication-lab/results/events.csv) record the completed run.

## Guides and source cases

- [Authentication walkthrough](LEARN_WITH_ME.md)
- [Worked incident report](WORKED_REPORT.md)
- [Fictional email cases](phishing-triage/messages.txt)
- [Fictional support cases](it-support/cases.txt)
- [Original exercise workbook bundle](project-workbooks.zip)

The original guides and workbook templates remain available for practice. The completed assessments above contain the latest results.

## Limits

All sign-ins, emails and tickets are fictional. Alerts are review signals, not confirmed attacks. The small dataset does not establish production detection accuracy. No live accounts were changed, no client devices were repaired in these exercises, and no media server has been installed.
