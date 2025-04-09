# file: lib/ansible/module_utils/facts/collector.py:84-87
# asked: {"lines": [84, 85, 86, 87], "branches": [[85, 86], [85, 87]]}
# gained: {"lines": [84, 85, 86, 87], "branches": [[85, 86], [85, 87]]}

import pytest

class MockNamespace:
    def transform(self, key_name):
        return f"transformed_{key_name}"

class TestBaseFactCollector:
    @pytest.fixture
    def base_fact_collector(self):
        from ansible.module_utils.facts.collector import BaseFactCollector
        return BaseFactCollector()

    def test_transform_name_with_namespace(self, base_fact_collector):
        base_fact_collector.namespace = MockNamespace()
        transformed_name = base_fact_collector._transform_name("test_key")
        assert transformed_name == "transformed_test_key"

    def test_transform_name_without_namespace(self, base_fact_collector):
        base_fact_collector.namespace = None
        transformed_name = base_fact_collector._transform_name("test_key")
        assert transformed_name == "test_key"
