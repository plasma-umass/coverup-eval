# file lib/ansible/module_utils/facts/collector.py:99-104
# lines []
# branches ['102->104']

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

class MockFactCollector(BaseFactCollector):
    def collect(self, module=None, collected_facts=None):
        return {'key': 'value'}

    def _transform_dict_keys(self, facts_dict):
        return {'namespaced_key': 'value'}

@pytest.fixture
def mock_collector_with_namespace():
    collector = MockFactCollector()
    collector.namespace = True
    return collector

@pytest.fixture
def mock_collector_without_namespace():
    collector = MockFactCollector()
    collector.namespace = False
    return collector

def test_collect_with_namespace_transforms_keys(mock_collector_with_namespace):
    facts = mock_collector_with_namespace.collect_with_namespace()
    assert 'namespaced_key' in facts
    assert facts['namespaced_key'] == 'value'

def test_collect_without_namespace_does_not_transform_keys(mock_collector_without_namespace):
    facts = mock_collector_without_namespace.collect_with_namespace()
    assert 'key' in facts
    assert facts['key'] == 'value'
    assert 'namespaced_key' not in facts
