# file lib/ansible/executor/stats.py:50-58
# lines [51, 52, 53, 55, 56, 57, 58]
# branches ['53->55', '53->56']

import pytest
from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    stats = AggregateStats()
    stats.ok = {'host1': 1}
    stats.failures = {'host1': 1}
    stats.dark = {'host1': 1}
    stats.changed = {'host1': 1}
    stats.skipped = {'host1': 1}
    stats.rescued = {'host1': 1}
    stats.ignored = {'host1': 1}
    yield stats

def test_decrement_existing_host(aggregate_stats):
    aggregate_stats.decrement('ok', 'host1')
    assert aggregate_stats.ok['host1'] == 0

def test_decrement_non_existing_host(aggregate_stats):
    aggregate_stats.decrement('ok', 'host2')
    assert aggregate_stats.ok['host2'] == 0

def test_decrement_negative_value(aggregate_stats):
    aggregate_stats.ok['host1'] = 2
    aggregate_stats.decrement('ok', 'host1')
    assert aggregate_stats.ok['host1'] == 1
    aggregate_stats.decrement('ok', 'host1')
    assert aggregate_stats.ok['host1'] == 0
