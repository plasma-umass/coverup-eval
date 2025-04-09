# file: lib/ansible/module_utils/facts/collector.py:89-96
# asked: {"lines": [89, 92, 93, 95, 96], "branches": [[92, 93], [92, 96]]}
# gained: {"lines": [89, 92, 93, 95, 96], "branches": [[92, 93], [92, 96]]}

import pytest
from unittest.mock import MagicMock

# Assuming the BaseFactCollector class is defined in ansible/module_utils/facts/collector.py
from ansible.module_utils.facts.collector import BaseFactCollector

class TestBaseFactCollector:
    @pytest.fixture
    def collector(self):
        class MockNamespace:
            def transform(self, key_name):
                return f"transformed_{key_name}"

        return BaseFactCollector(namespace=MockNamespace())

    def test_transform_dict_keys(self, collector):
        fact_dict = {'key1': 'value1', 'key2': 'value2'}
        transformed_dict = collector._transform_dict_keys(fact_dict)

        assert 'transformed_key1' in transformed_dict
        assert 'transformed_key2' in transformed_dict
        assert 'key1' not in transformed_dict
        assert 'key2' not in transformed_dict
        assert transformed_dict['transformed_key1'] == 'value1'
        assert transformed_dict['transformed_key2'] == 'value2'

    def test_transform_dict_keys_no_namespace(self):
        collector = BaseFactCollector()
        fact_dict = {'key1': 'value1', 'key2': 'value2'}
        transformed_dict = collector._transform_dict_keys(fact_dict)

        assert 'key1' in transformed_dict
        assert 'key2' in transformed_dict
        assert transformed_dict['key1'] == 'value1'
        assert transformed_dict['key2'] == 'value2'
