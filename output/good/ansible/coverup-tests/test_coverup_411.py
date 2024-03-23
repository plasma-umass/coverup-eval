# file lib/ansible/executor/stats.py:29-41
# lines [29, 31, 32, 33, 34, 35, 36, 37, 38, 41]
# branches []

import pytest
from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    return AggregateStats()

def test_aggregate_stats_initialization(aggregate_stats):
    assert isinstance(aggregate_stats.processed, dict)
    assert isinstance(aggregate_stats.failures, dict)
    assert isinstance(aggregate_stats.ok, dict)
    assert isinstance(aggregate_stats.dark, dict)
    assert isinstance(aggregate_stats.changed, dict)
    assert isinstance(aggregate_stats.skipped, dict)
    assert isinstance(aggregate_stats.rescued, dict)
    assert isinstance(aggregate_stats.ignored, dict)
    assert isinstance(aggregate_stats.custom, dict)

    # Ensure that all dictionaries are empty upon initialization
    assert not aggregate_stats.processed
    assert not aggregate_stats.failures
    assert not aggregate_stats.ok
    assert not aggregate_stats.dark
    assert not aggregate_stats.changed
    assert not aggregate_stats.skipped
    assert not aggregate_stats.rescued
    assert not aggregate_stats.ignored
    assert not aggregate_stats.custom
