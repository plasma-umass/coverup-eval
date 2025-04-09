# file: lib/ansible/executor/stats.py:60-71
# asked: {"lines": [60, 63, 64, 65, 66, 67, 68, 69, 70], "branches": []}
# gained: {"lines": [60, 63, 64, 65, 66, 67, 68, 69, 70], "branches": []}

import pytest
from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    return AggregateStats()

def test_summarize_all_zeroes(aggregate_stats):
    host = 'test_host'
    summary = aggregate_stats.summarize(host)
    assert summary == {
        'ok': 0,
        'failures': 0,
        'unreachable': 0,
        'changed': 0,
        'skipped': 0,
        'rescued': 0,
        'ignored': 0
    }

def test_summarize_with_values(aggregate_stats):
    host = 'test_host'
    aggregate_stats.ok[host] = 1
    aggregate_stats.failures[host] = 2
    aggregate_stats.dark[host] = 3
    aggregate_stats.changed[host] = 4
    aggregate_stats.skipped[host] = 5
    aggregate_stats.rescued[host] = 6
    aggregate_stats.ignored[host] = 7

    summary = aggregate_stats.summarize(host)
    assert summary == {
        'ok': 1,
        'failures': 2,
        'unreachable': 3,
        'changed': 4,
        'skipped': 5,
        'rescued': 6,
        'ignored': 7
    }
