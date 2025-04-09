# file: lib/ansible/executor/stats.py:50-58
# asked: {"lines": [50, 51, 52, 53, 55, 56, 57, 58], "branches": [[53, 55], [53, 56]]}
# gained: {"lines": [50, 51, 52, 53, 55, 56, 57, 58], "branches": [[53, 55], [53, 56]]}

import pytest

from ansible.executor.stats import AggregateStats

@pytest.fixture
def stats():
    return AggregateStats()

def test_decrement_existing_host(stats):
    stats.ok['host1'] = 2
    stats.decrement('ok', 'host1')
    assert stats.ok['host1'] == 1

def test_decrement_non_existing_host(stats):
    stats.ok['host2'] = 0
    stats.decrement('ok', 'host2')
    assert stats.ok['host2'] == 0

def test_decrement_negative_value(stats):
    stats.ok['host3'] = 0
    stats.decrement('ok', 'host3')
    assert stats.ok['host3'] == 0
