# file lib/ansible/module_utils/facts/collector.py:65-76
# lines [65, 69, 73, 75, 76]
# branches []

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

class MockNamespace:
    def transform(self, name):
        return f"mock_{name}"

class MockFactCollector(BaseFactCollector):
    name = "mock_collector"
    _fact_ids = set(["mock_id_1", "mock_id_2"])

@pytest.fixture
def mock_namespace():
    return MockNamespace()

def test_base_fact_collector_with_namespace(mock_namespace):
    collector = MockFactCollector(namespace=mock_namespace)
    assert collector.namespace is mock_namespace
    assert collector.fact_ids == {"mock_collector", "mock_id_1", "mock_id_2"}

def test_base_fact_collector_without_namespace():
    collector = MockFactCollector()
    assert collector.namespace is None
    assert collector.fact_ids == {"mock_collector", "mock_id_1", "mock_id_2"}
