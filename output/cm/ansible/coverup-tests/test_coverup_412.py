# file lib/ansible/executor/stats.py:73-81
# lines [73, 76, 77, 78, 79, 81]
# branches ['76->77', '76->78', '78->79', '78->81']

import pytest
from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    stats = AggregateStats()
    stats.custom = {}
    return stats

def test_set_custom_stats_without_host(aggregate_stats):
    aggregate_stats.set_custom_stats('test_stat', 42)
    assert '_run' in aggregate_stats.custom
    assert 'test_stat' in aggregate_stats.custom['_run']
    assert aggregate_stats.custom['_run']['test_stat'] == 42

def test_set_custom_stats_with_host(aggregate_stats):
    aggregate_stats.set_custom_stats('test_stat', 42, host='test_host')
    assert 'test_host' in aggregate_stats.custom
    assert 'test_stat' in aggregate_stats.custom['test_host']
    assert aggregate_stats.custom['test_host']['test_stat'] == 42

def test_set_custom_stats_update_existing(aggregate_stats):
    aggregate_stats.custom['_run'] = {'existing_stat': 1}
    aggregate_stats.set_custom_stats('updated_stat', 99)
    assert 'updated_stat' in aggregate_stats.custom['_run']
    assert aggregate_stats.custom['_run']['updated_stat'] == 99
    # Ensure existing stat is not removed
    assert 'existing_stat' in aggregate_stats.custom['_run']
    assert aggregate_stats.custom['_run']['existing_stat'] == 1
