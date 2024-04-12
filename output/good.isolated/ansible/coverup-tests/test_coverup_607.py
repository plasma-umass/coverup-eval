# file lib/ansible/module_utils/facts/collector.py:84-87
# lines [84, 85, 86, 87]
# branches ['85->86', '85->87']

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

class MockNamespace:
    def transform(self, key_name):
        return "transformed_" + key_name

@pytest.fixture
def base_fact_collector():
    return BaseFactCollector()

@pytest.fixture
def base_fact_collector_with_namespace():
    collector = BaseFactCollector()
    collector.namespace = MockNamespace()
    return collector

def test_transform_name_without_namespace(base_fact_collector):
    key_name = "test_key"
    transformed_name = base_fact_collector._transform_name(key_name)
    assert transformed_name == key_name

def test_transform_name_with_namespace(base_fact_collector_with_namespace):
    key_name = "test_key"
    transformed_name = base_fact_collector_with_namespace._transform_name(key_name)
    assert transformed_name == "transformed_test_key"
