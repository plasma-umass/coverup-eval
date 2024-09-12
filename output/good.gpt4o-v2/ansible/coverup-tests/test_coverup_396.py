# file: lib/ansible/executor/stats.py:29-41
# asked: {"lines": [29, 31, 32, 33, 34, 35, 36, 37, 38, 41], "branches": []}
# gained: {"lines": [29, 31, 32, 33, 34, 35, 36, 37, 38, 41], "branches": []}

import pytest
from ansible.executor.stats import AggregateStats

def test_aggregate_stats_init():
    stats = AggregateStats()
    
    assert stats.processed == {}
    assert stats.failures == {}
    assert stats.ok == {}
    assert stats.dark == {}
    assert stats.changed == {}
    assert stats.skipped == {}
    assert stats.rescued == {}
    assert stats.ignored == {}
    assert stats.custom == {}
