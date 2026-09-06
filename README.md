# IT and Security Lab Notes

Small practical labs covering sign-in investigations, phishing triage, IT support and a home media-server plan.

## Start here

- [Authentication investigation walkthrough](LEARN_WITH_ME.md)
- [Worked incident report](WORKED_REPORT.md)
- [Home media-server plan](MEDIA_SERVER.md)
- [Download all project workbooks](project-workbooks.zip), including phishing cases, support tickets, CSV templates and generated reference results

## What is finished?

| Project | Status |
|---|---|
| Personal PC build | Owner confirms assembling the CPU, GPU, RAM and PSU; component records pending |
| Authentication lab | Working reference tool, 24 synthetic events, generated evidence and four passing tests; learner investigation pending |
| Phishing triage | Three fictional cases and worked answers prepared; learner responses pending |
| IT support | Three fictional cases and tracker prepared; learner responses pending |
| Home media server | Jellyfin design and test plan prepared; not installed |

## Run the authentication lab

Python 3.10 or newer; no extra packages needed. Run these commands from the repository folder:

```text
python analyse.py
python -m unittest -v test_analyse.py
```

The tool writes `results/events.csv`, `results/findings.json` and `results/evidence_summary.md`. Expected totals: 24 events, 17 failures and 7 successes. First rule triggers: E009, E015 and E017. The tests also check benign retries, events outside the time window and separation between accounts.

No coding is needed to complete the learner investigation: read the log or generated CSV and fill in the report template. The complete workbooks archive includes pre-generated results.

## Contributions and limitations

The teaching materials, Python tool and worked reference answers were prepared with OpenAI Codex. They are not a claim that the owner independently wrote the tool or completed the investigations. Personal reports and reflections will be added as the exercises are completed.

The logs, email messages and support tickets are fictional. The rules are teaching examples, not production detections: alerts require review and do not prove compromise. No real accounts were investigated, and no media server was installed by creating this repository.
