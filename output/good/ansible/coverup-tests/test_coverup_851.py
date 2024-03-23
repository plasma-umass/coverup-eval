# file lib/ansible/executor/stats.py:26-28
# lines [26, 27]
# branches []

import pytest
from ansible.executor.stats import AggregateStats

# Since the original code snippet does not provide any methods or attributes,
# we will create a test that simply instantiates the AggregateStats class
# to ensure that the class can be instantiated without errors.

def test_aggregate_stats_instantiation():
    # Instantiate AggregateStats
    stats = AggregateStats()

    # Assert that the instance is of type AggregateStats
    assert isinstance(stats, AggregateStats), "stats should be an instance of AggregateStats"
