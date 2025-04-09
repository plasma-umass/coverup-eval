# file lib/ansible/executor/stats.py:73-81
# lines [76, 77, 78, 79, 81]
# branches ['76->77', '76->78', '78->79', '78->81']

import pytest
from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    return AggregateStats()

def test_set_custom_stats_no_host(aggregate_stats):
    aggregate_stats.custom = {}
    aggregate_stats.set_custom_stats('stat1', 'value1')
    assert '_run' in aggregate_stats.custom
    assert aggregate_stats.custom['_run']['stat1'] == 'value1'

def test_set_custom_stats_with_host_new_entry(aggregate_stats):
    aggregate_stats.custom = {}
    aggregate_stats.set_custom_stats('stat2', 'value2', host='host1')
    assert 'host1' in aggregate_stats.custom
    assert aggregate_stats.custom['host1']['stat2'] == 'value2'

def test_set_custom_stats_with_host_existing_entry(aggregate_stats):
    aggregate_stats.custom = {'host2': {'stat3': 'value3'}}
    aggregate_stats.set_custom_stats('stat4', 'value4', host='host2')
    assert 'host2' in aggregate_stats.custom
    assert aggregate_stats.custom['host2']['stat3'] == 'value3'
    assert aggregate_stats.custom['host2']['stat4'] == 'value4'
