# file: lib/ansible/executor/stats.py:43-48
# asked: {"lines": [46, 47, 48], "branches": []}
# gained: {"lines": [46, 47, 48], "branches": []}

import pytest

from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    stats = AggregateStats()
    stats.processed = {}
    stats.ok = {}
    stats.failures = {}
    return stats

def test_increment_ok(aggregate_stats):
    aggregate_stats.increment('ok', 'host1')
    assert aggregate_stats.processed['host1'] == 1
    assert aggregate_stats.ok['host1'] == 1

def test_increment_failures(aggregate_stats):
    aggregate_stats.increment('failures', 'host2')
    assert aggregate_stats.processed['host2'] == 1
    assert aggregate_stats.failures['host2'] == 1

def test_increment_existing_ok(aggregate_stats):
    aggregate_stats.ok['host1'] = 1
    aggregate_stats.increment('ok', 'host1')
    assert aggregate_stats.processed['host1'] == 1
    assert aggregate_stats.ok['host1'] == 2

def test_increment_existing_failures(aggregate_stats):
    aggregate_stats.failures['host2'] = 2
    aggregate_stats.increment('failures', 'host2')
    assert aggregate_stats.processed['host2'] == 1
    assert aggregate_stats.failures['host2'] == 3
