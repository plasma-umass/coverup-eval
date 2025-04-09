# file: lib/ansible/module_utils/facts/collector.py:65-76
# asked: {"lines": [65, 69, 73, 75, 76], "branches": []}
# gained: {"lines": [65, 69, 73, 75, 76], "branches": []}

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

class MockNamespace:
    def transform(self, name):
        return f"namespace_{name}"

@pytest.fixture
def mock_namespace():
    return MockNamespace()

def test_base_fact_collector_init_with_collectors(mock_namespace):
    collectors = [BaseFactCollector(), BaseFactCollector()]
    collector = BaseFactCollector(collectors=collectors, namespace=mock_namespace)
    
    assert collector.collectors == collectors
    assert collector.namespace == mock_namespace
    assert collector.fact_ids == {collector.name} | BaseFactCollector._fact_ids

def test_base_fact_collector_init_without_collectors(mock_namespace):
    collector = BaseFactCollector(namespace=mock_namespace)
    
    assert collector.collectors == []
    assert collector.namespace == mock_namespace
    assert collector.fact_ids == {collector.name} | BaseFactCollector._fact_ids
