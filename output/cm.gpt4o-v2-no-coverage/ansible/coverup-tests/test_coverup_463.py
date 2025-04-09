# file: lib/ansible/executor/stats.py:73-81
# asked: {"lines": [73, 76, 77, 78, 79, 81], "branches": [[76, 77], [76, 78], [78, 79], [78, 81]]}
# gained: {"lines": [73, 76, 77, 78, 79, 81], "branches": [[76, 77], [76, 78], [78, 79], [78, 81]]}

import pytest
from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    return AggregateStats()

def test_set_custom_stats_no_host(aggregate_stats):
    aggregate_stats.set_custom_stats('stat1', 'value1')
    assert '_run' in aggregate_stats.custom
    assert aggregate_stats.custom['_run']['stat1'] == 'value1'

def test_set_custom_stats_with_host(aggregate_stats):
    aggregate_stats.set_custom_stats('stat2', 'value2', host='host1')
    assert 'host1' in aggregate_stats.custom
    assert aggregate_stats.custom['host1']['stat2'] == 'value2'

def test_set_custom_stats_update_existing(aggregate_stats):
    aggregate_stats.set_custom_stats('stat3', 'value3', host='host2')
    aggregate_stats.set_custom_stats('stat3', 'new_value3', host='host2')
    assert aggregate_stats.custom['host2']['stat3'] == 'new_value3'
