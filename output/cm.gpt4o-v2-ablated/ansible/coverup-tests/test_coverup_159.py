# file: lib/ansible/executor/stats.py:50-58
# asked: {"lines": [50, 51, 52, 53, 55, 56, 57, 58], "branches": [[53, 55], [53, 56]]}
# gained: {"lines": [50, 51, 52, 53, 55, 56, 57, 58], "branches": [[53, 55], [53, 56]]}

import pytest

from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    class MockAggregateStats(AggregateStats):
        def __init__(self):
            self.some_stat = {}
    return MockAggregateStats()

def test_decrement_existing_host_positive_value(aggregate_stats):
    aggregate_stats.some_stat['host1'] = 2
    aggregate_stats.decrement('some_stat', 'host1')
    assert aggregate_stats.some_stat['host1'] == 1

def test_decrement_existing_host_zero_value(aggregate_stats):
    aggregate_stats.some_stat['host1'] = 0
    aggregate_stats.decrement('some_stat', 'host1')
    assert aggregate_stats.some_stat['host1'] == 0

def test_decrement_non_existing_host(aggregate_stats):
    aggregate_stats.decrement('some_stat', 'host2')
    assert aggregate_stats.some_stat['host2'] == 0
