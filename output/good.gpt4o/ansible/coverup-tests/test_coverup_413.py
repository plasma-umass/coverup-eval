# file lib/ansible/executor/stats.py:29-41
# lines [29, 31, 32, 33, 34, 35, 36, 37, 38, 41]
# branches []

import pytest
from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    return AggregateStats()

def test_aggregate_stats_initialization(aggregate_stats):
    assert aggregate_stats.processed == {}
    assert aggregate_stats.failures == {}
    assert aggregate_stats.ok == {}
    assert aggregate_stats.dark == {}
    assert aggregate_stats.changed == {}
    assert aggregate_stats.skipped == {}
    assert aggregate_stats.rescued == {}
    assert aggregate_stats.ignored == {}
    assert aggregate_stats.custom == {}

def test_aggregate_stats_custom(aggregate_stats):
    aggregate_stats.custom['test'] = 'value'
    assert aggregate_stats.custom['test'] == 'value'
    del aggregate_stats.custom['test']
    assert 'test' not in aggregate_stats.custom
