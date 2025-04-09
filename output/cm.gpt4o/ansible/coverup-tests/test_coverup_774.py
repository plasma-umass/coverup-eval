# file lib/ansible/executor/stats.py:26-28
# lines [26, 27]
# branches []

import pytest
from ansible.executor.stats import AggregateStats

def test_aggregate_stats_initialization():
    # Test the initialization of AggregateStats
    stats = AggregateStats()
    assert isinstance(stats, AggregateStats)
