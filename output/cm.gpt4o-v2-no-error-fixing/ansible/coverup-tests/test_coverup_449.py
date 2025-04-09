# file: lib/ansible/executor/stats.py:43-48
# asked: {"lines": [43, 46, 47, 48], "branches": []}
# gained: {"lines": [43, 46, 47, 48], "branches": []}

import pytest
from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    return AggregateStats()

def test_increment_new_host(aggregate_stats):
    aggregate_stats.increment('ok', 'host1')
    assert aggregate_stats.processed['host1'] == 1
    assert aggregate_stats.ok['host1'] == 1

def test_increment_existing_host(aggregate_stats):
    aggregate_stats.ok['host1'] = 1
    aggregate_stats.increment('ok', 'host1')
    assert aggregate_stats.processed['host1'] == 1
    assert aggregate_stats.ok['host1'] == 2
