# file lib/ansible/executor/stats.py:83-99
# lines [87, 89]
# branches ['86->87', '88->89']

import pytest
from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    return AggregateStats()

def test_update_custom_stats_with_none_host(aggregate_stats, mocker):
    mocker.patch.object(aggregate_stats, 'set_custom_stats')
    aggregate_stats.custom = {'_run': {}}
    aggregate_stats.update_custom_stats('test_stat', 1)
    aggregate_stats.set_custom_stats.assert_called_once_with('test_stat', 1, '_run')

def test_update_custom_stats_with_new_host_and_stat(aggregate_stats, mocker):
    mocker.patch.object(aggregate_stats, 'set_custom_stats')
    aggregate_stats.custom = {}
    aggregate_stats.update_custom_stats('test_stat', 1, 'new_host')
    aggregate_stats.set_custom_stats.assert_called_once_with('test_stat', 1, 'new_host')
