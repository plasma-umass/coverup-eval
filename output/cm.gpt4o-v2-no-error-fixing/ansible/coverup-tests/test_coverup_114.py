# file: lib/ansible/executor/stats.py:83-99
# asked: {"lines": [83, 86, 87, 88, 89, 92, 93, 95, 96, 99], "branches": [[86, 87], [86, 88], [88, 89], [88, 92], [92, 93], [92, 95], [95, 96], [95, 99]]}
# gained: {"lines": [83, 86, 87, 88, 89, 92, 93, 95, 96, 99], "branches": [[86, 87], [86, 88], [88, 89], [88, 92], [92, 93], [92, 95], [95, 96], [95, 99]]}

import pytest
from ansible.executor.stats import AggregateStats
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.utils.vars import merge_hash

@pytest.fixture
def aggregate_stats():
    stats = AggregateStats()
    stats.custom = {}
    return stats

def test_update_custom_stats_no_host(aggregate_stats, mocker):
    mock_set_custom_stats = mocker.patch.object(aggregate_stats, 'set_custom_stats')
    aggregate_stats.update_custom_stats('stat1', 10)
    mock_set_custom_stats.assert_called_once_with('stat1', 10, '_run')

def test_update_custom_stats_with_host(aggregate_stats, mocker):
    mock_set_custom_stats = mocker.patch.object(aggregate_stats, 'set_custom_stats')
    aggregate_stats.update_custom_stats('stat1', 10, 'host1')
    mock_set_custom_stats.assert_called_once_with('stat1', 10, 'host1')

def test_update_custom_stats_mismatching_types(aggregate_stats):
    aggregate_stats.custom = {'_run': {'stat1': 10}}
    result = aggregate_stats.update_custom_stats('stat1', 'string_value')
    assert result is None

def test_update_custom_stats_mutable_mapping(aggregate_stats, mocker):
    aggregate_stats.custom = {'_run': {'stat1': {'key1': 'value1'}}}
    mock_merge_hash = mocker.patch('ansible.executor.stats.merge_hash', return_value={'key1': 'value1', 'key2': 'value2'})
    aggregate_stats.update_custom_stats('stat1', {'key2': 'value2'})
    assert aggregate_stats.custom['_run']['stat1'] == {'key1': 'value1', 'key2': 'value2'}
    mock_merge_hash.assert_called_once_with({'key1': 'value1'}, {'key2': 'value2'})

def test_update_custom_stats_other_types(aggregate_stats):
    aggregate_stats.custom = {'_run': {'stat1': 10}}
    aggregate_stats.update_custom_stats('stat1', 5)
    assert aggregate_stats.custom['_run']['stat1'] == 15
