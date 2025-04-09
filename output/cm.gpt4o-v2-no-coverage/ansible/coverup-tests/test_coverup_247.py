# file: lib/ansible/executor/stats.py:83-99
# asked: {"lines": [83, 86, 87, 88, 89, 92, 93, 95, 96, 99], "branches": [[86, 87], [86, 88], [88, 89], [88, 92], [92, 93], [92, 95], [95, 96], [95, 99]]}
# gained: {"lines": [83, 86, 87, 88, 89, 92, 93, 95, 96, 99], "branches": [[86, 87], [86, 88], [88, 89], [88, 92], [92, 93], [92, 95], [95, 96], [95, 99]]}

import pytest
from unittest.mock import MagicMock
from ansible.executor.stats import AggregateStats
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.utils.vars import merge_hash

class TestAggregateStats:
    
    @pytest.fixture
    def aggregate_stats(self):
        return AggregateStats()

    def test_update_custom_stats_no_host(self, aggregate_stats):
        aggregate_stats.set_custom_stats = MagicMock()
        aggregate_stats.update_custom_stats('stat1', 10)
        aggregate_stats.set_custom_stats.assert_called_once_with('stat1', 10, '_run')

    def test_update_custom_stats_new_host(self, aggregate_stats):
        aggregate_stats.set_custom_stats = MagicMock()
        aggregate_stats.update_custom_stats('stat1', 10, 'host1')
        aggregate_stats.set_custom_stats.assert_called_once_with('stat1', 10, 'host1')

    def test_update_custom_stats_mismatched_types(self, aggregate_stats):
        aggregate_stats.custom['_run'] = {'stat1': 10}
        result = aggregate_stats.update_custom_stats('stat1', 'string_value')
        assert result is None

    def test_update_custom_stats_merge_hash(self, aggregate_stats):
        aggregate_stats.custom['_run'] = {'stat1': {'key1': 'value1'}}
        aggregate_stats.update_custom_stats('stat1', {'key2': 'value2'})
        assert aggregate_stats.custom['_run']['stat1'] == {'key1': 'value1', 'key2': 'value2'}

    def test_update_custom_stats_addition(self, aggregate_stats):
        aggregate_stats.custom['_run'] = {'stat1': 10}
        aggregate_stats.update_custom_stats('stat1', 5)
        assert aggregate_stats.custom['_run']['stat1'] == 15
