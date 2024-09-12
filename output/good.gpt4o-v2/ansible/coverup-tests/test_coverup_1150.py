# file: lib/ansible/executor/stats.py:83-99
# asked: {"lines": [86, 87, 88, 89, 92, 93, 95, 96, 99], "branches": [[86, 87], [86, 88], [88, 89], [88, 92], [92, 93], [92, 95], [95, 96], [95, 99]]}
# gained: {"lines": [86, 87, 88, 89, 92, 93, 95, 96, 99], "branches": [[86, 87], [86, 88], [88, 89], [88, 92], [92, 93], [92, 95], [95, 96], [95, 99]]}

import pytest
from unittest.mock import MagicMock
from ansible.executor.stats import AggregateStats
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.utils.vars import merge_hash

@pytest.fixture
def aggregate_stats():
    stats = AggregateStats()
    stats.custom = {}
    stats.set_custom_stats = MagicMock()
    return stats

def test_update_custom_stats_no_host(aggregate_stats):
    aggregate_stats.update_custom_stats('stat1', 1)
    aggregate_stats.set_custom_stats.assert_called_once_with('stat1', 1, '_run')

def test_update_custom_stats_new_host(aggregate_stats):
    aggregate_stats.update_custom_stats('stat1', 1, 'host1')
    aggregate_stats.set_custom_stats.assert_called_once_with('stat1', 1, 'host1')

def test_update_custom_stats_mismatching_types(aggregate_stats):
    aggregate_stats.custom = {'host1': {'stat1': 1}}
    result = aggregate_stats.update_custom_stats('stat1', 'string', 'host1')
    assert result is None

def test_update_custom_stats_mutable_mapping(aggregate_stats, monkeypatch):
    aggregate_stats.custom = {'host1': {'stat1': {'key1': 'value1'}}}
    new_data = {'key2': 'value2'}
    merged_data = {'key1': 'value1', 'key2': 'value2'}
    
    def mock_merge_hash(a, b):
        return {**a, **b}
    
    monkeypatch.setattr('ansible.utils.vars.merge_hash', mock_merge_hash)
    
    aggregate_stats.update_custom_stats('stat1', new_data, 'host1')
    assert aggregate_stats.custom['host1']['stat1'] == merged_data

def test_update_custom_stats_other_types(aggregate_stats):
    aggregate_stats.custom = {'host1': {'stat1': 1}}
    aggregate_stats.update_custom_stats('stat1', 2, 'host1')
    assert aggregate_stats.custom['host1']['stat1'] == 3
