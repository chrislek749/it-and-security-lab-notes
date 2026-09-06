"""Offline teaching tool for the supplied fictional authentication log.

Written with AI assistance. No network connections or third-party dependencies.
Run: python analyse.py
"""
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import csv
import json

ROOT = Path(__file__).resolve().parent

def parse(text):
    events = []
    for line in text.splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        fields = [part.strip() for part in line.split('|')]
        if len(fields) != 6:
            raise ValueError('Expected six fields: ' + line)
        event_id, timestamp, user, source_ip, result, mfa = fields
        if result not in ('SUCCESS', 'FAILURE'):
            raise ValueError('Unexpected result: ' + result)
        events.append(dict(event_id=event_id, timestamp=timestamp,
                           user=user, source_ip=source_ip, result=result, mfa=mfa))
    if len({e['event_id'] for e in events}) != len(events):
        raise ValueError('Duplicate event IDs')
    return sorted(events, key=lambda e: e['timestamp'])

def time(event):
    return datetime.fromisoformat(event['timestamp'].replace('Z', '+00:00'))

def detect(events):
    """Teaching thresholds, not production detections; inclusive 5-minute window."""
    alerts, seen = [], set()
    for current in events:
        recent = [e for e in events if e['source_ip'] == current['source_ip']
                  and timedelta(0) <= time(current) - time(e) <= timedelta(minutes=5)]
        failures = [e for e in recent if e['result'] == 'FAILURE']
        checks = []
        if len({e['user'] for e in failures}) >= 5:
            checks.append(('MULTI_ACCOUNT_FAILURES', failures))
        same = [e for e in failures if e['user'] == current['user']]
        if len(same) >= 5:
            checks.append(('REPEATED_ACCOUNT_FAILURES', same))
        if current['result'] == 'SUCCESS' and len(same) >= 5:
            checks.append(('SUCCESS_AFTER_FAILURES', same + [current]))
        for rule, evidence in checks:
            # One first-trigger alert per rule/source/account in this small dataset.
            key = (rule, current['source_ip'], '' if rule == 'MULTI_ACCOUNT_FAILURES' else current['user'])
            if key in seen:
                continue
            seen.add(key)
            alerts.append(dict(rule=rule, trigger=current['event_id'],
                               source_ip=current['source_ip'],
                               evidence=[e['event_id'] for e in evidence]))
    return alerts

def main():
    events = parse((ROOT/'synthetic_authentication.log').read_text())
    alerts = detect(events)
    target = ROOT/'results'
    target.mkdir(exist_ok=True)
    with (target/'events.csv').open('w', newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(events[0]))
        writer.writeheader(); writer.writerows(events)
    counts = Counter(e['result'] for e in events)
    summary = dict(total=len(events), results=dict(counts), alerts=alerts)
    (target/'findings.json').write_text(json.dumps(summary, indent=2))
    rows = ['# Generated evidence summary', '', 'Synthetic training data only. AI-assisted analysis tool.', '',
            f"Events: {len(events)}; failures: {counts['FAILURE']}; successes: {counts['SUCCESS']}", '',
            '| Source IP | Failures | Successes | Distinct accounts |', '|---|---:|---:|---:|']
    groups=defaultdict(list)
    for event in events: groups[event['source_ip']].append(event)
    for ip, group in sorted(groups.items()):
        rows.append(f"| {ip} | {sum(e['result']=='FAILURE' for e in group)} | {sum(e['result']=='SUCCESS' for e in group)} | {len({e['user'] for e in group})} |")
    rows += ['', '## First rule triggers', '']
    for alert in alerts:
        rows.append(f"- {alert['rule']}: {alert['trigger']}; evidence {', '.join(alert['evidence'])}")
    rows += ['', 'Rules identify patterns requiring review, not confirmed attacks. Passwords are not logged, so the multi-account pattern cannot establish password spraying specifically.',
             'This small demonstrator emits only the first alert per rule/source/account for the entire file. Production logic needs episode resets, larger-scale processing, identity context and validation.']
    (target/'evidence_summary.md').write_text('\n'.join(rows))
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main()
