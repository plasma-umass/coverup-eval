# file lib/ansible/executor/stats.py:60-71
# lines [60, 63, 64, 65, 66, 67, 68, 69, 70]
# branches []

import pytest
from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    stats = AggregateStats()
    stats.ok = {'host1': 1}
    stats.failures = {'host1': 2}
    stats.dark = {'host1': 3}
    stats.changed = {'host1': 4}
    stats.skipped = {'host1': 5}
    stats.rescued = {'host1': 6}
    stats.ignored = {'host1': 7}
    return stats

def test_summarize_existing_host(aggregate_stats):
    summary = aggregate_stats.summarize('host1')
    assert summary == {
        'ok': 1,
        'failures': 2,
        'unreachable': 3,
        'changed': 4,
        'skipped': 5,
        'rescued': 6,
        'ignored': 7,
    }

def test_summarize_non_existing_host(aggregate_stats):
    summary = aggregate_stats.summarize('host2')
    assert summary == {
        'ok': 0,
        'failures': 0,
        'unreachable': 0,
        'changed': 0,
        'skipped': 0,
        'rescued': 0,
        'ignored': 0,
    }
