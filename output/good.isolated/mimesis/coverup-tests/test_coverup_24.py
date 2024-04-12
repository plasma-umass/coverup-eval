# file mimesis/providers/base.py:105-118
# lines [105, 112, 113, 114, 115, 117, 118]
# branches ['112->113', '112->118', '113->114', '113->117']

import pytest
from mimesis.providers.base import BaseDataProvider
from collections.abc import Mapping

class TestBaseDataProvider:
    @pytest.fixture
    def base_data_provider(self):
        return BaseDataProvider()

    def test_update_dict_recursive(self, base_data_provider):
        initial = {'level1': {'level2': 'value1'}}
        other = {'level1': {'level2': 'value2', 'level3': 'value3'}}
        expected = {'level1': {'level2': 'value2', 'level3': 'value3'}}
        result = base_data_provider._update_dict(initial, other)
        assert result == expected, "The dictionary was not updated correctly"

    def test_update_dict_with_non_mapping(self, base_data_provider):
        initial = {'key1': 'value1'}
        other = {'key2': 'value2'}
        expected = {'key1': 'value1', 'key2': 'value2'}
        result = base_data_provider._update_dict(initial, other)
        assert result == expected, "The dictionary was not updated correctly"

    def test_update_dict_with_empty_other(self, base_data_provider):
        initial = {'key1': 'value1'}
        other = {}
        expected = {'key1': 'value1'}
        result = base_data_provider._update_dict(initial, other)
        assert result == expected, "The dictionary should not change when 'other' is empty"

    def test_update_dict_with_empty_initial(self, base_data_provider):
        initial = {}
        other = {'key1': 'value1'}
        expected = {'key1': 'value1'}
        result = base_data_provider._update_dict(initial, other)
        assert result == expected, "The dictionary should be updated with 'other' when 'initial' is empty"

    def test_update_dict_with_nested_empty_dict(self, base_data_provider):
        initial = {'level1': {}}
        other = {'level1': {'level2': 'value2'}}
        expected = {'level1': {'level2': 'value2'}}
        result = base_data_provider._update_dict(initial, other)
        assert result == expected, "The nested dictionary should be updated correctly"
