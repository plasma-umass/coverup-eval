# file lib/ansible/executor/stats.py:43-48
# lines [43, 46, 47, 48]
# branches []

import pytest
from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    stats = AggregateStats()
    stats.processed = {}
    stats.ok = {}
    stats.changed = {}
    stats.skipped = {}
    stats.failures = {}
    stats.rescued = {}
    stats.ignored = {}
    return stats

def test_increment(aggregate_stats):
    host = 'localhost'
    
    # Test incrementing 'ok' stat
    aggregate_stats.increment('ok', host)
    assert aggregate_stats.ok[host] == 1
    assert aggregate_stats.processed[host] == 1

    # Test incrementing 'ok' stat again
    aggregate_stats.increment('ok', host)
    assert aggregate_stats.ok[host] == 2

    # Test incrementing 'changed' stat
    aggregate_stats.increment('changed', host)
    assert aggregate_stats.changed[host] == 1

    # Test incrementing 'skipped' stat
    aggregate_stats.increment('skipped', host)
    assert aggregate_stats.skipped[host] == 1

    # Test incrementing 'failures' stat
    aggregate_stats.increment('failures', host)
    assert aggregate_stats.failures[host] == 1

    # Test incrementing 'rescued' stat
    aggregate_stats.increment('rescued', host)
    assert aggregate_stats.rescued[host] == 1

    # Test incrementing 'ignored' stat
    aggregate_stats.increment('ignored', host)
    assert aggregate_stats.ignored[host] == 1
