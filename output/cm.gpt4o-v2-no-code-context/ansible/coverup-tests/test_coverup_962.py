# file: lib/ansible/executor/stats.py:83-99
# asked: {"lines": [86, 87, 88, 89, 92, 93, 95, 96, 99], "branches": [[86, 87], [86, 88], [88, 89], [88, 92], [92, 93], [92, 95], [95, 96], [95, 99]]}
# gained: {"lines": [86, 87, 88, 89, 92, 93, 95, 96, 99], "branches": [[86, 87], [86, 88], [88, 89], [88, 92], [92, 93], [92, 95], [95, 96], [95, 99]]}

import pytest
from collections.abc import MutableMapping
from ansible.executor.stats import AggregateStats

class TestAggregateStats:
    @pytest.fixture
    def stats(self):
        return AggregateStats()

    def test_update_custom_stats_no_host(self, stats, mocker):
        mocker.patch.object(stats, 'set_custom_stats')
        stats.custom = {}
        stats.update_custom_stats('stat1', 10)
        stats.set_custom_stats.assert_called_once_with('stat1', 10, '_run')

    def test_update_custom_stats_new_host(self, stats, mocker):
        mocker.patch.object(stats, 'set_custom_stats')
        stats.custom = {}
        stats.update_custom_stats('stat1', 10, 'host1')
        stats.set_custom_stats.assert_called_once_with('stat1', 10, 'host1')

    def test_update_custom_stats_mismatching_types(self, stats):
        stats.custom = {'host1': {'stat1': 10}}
        result = stats.update_custom_stats('stat1', 'string', 'host1')
        assert result is None

    def test_update_custom_stats_merge_hash(self, stats, mocker):
        mocker.patch('ansible.executor.stats.merge_hash', return_value={'key': 'value'})
        stats.custom = {'host1': {'stat1': {}}}
        stats.update_custom_stats('stat1', {'key': 'value'}, 'host1')
        assert stats.custom['host1']['stat1'] == {'key': 'value'}

    def test_update_custom_stats_addition(self, stats):
        stats.custom = {'host1': {'stat1': 10}}
        stats.update_custom_stats('stat1', 5, 'host1')
        assert stats.custom['host1']['stat1'] == 15
