# file lib/ansible/module_utils/facts/collector.py:99-104
# lines [99, 101, 102, 103, 104]
# branches ['102->103', '102->104']

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

class MockFactCollector(BaseFactCollector):
    def __init__(self):
        self.namespace = 'test_namespace'

    def collect(self, module=None, collected_facts=None):
        return {'key1': 'value1', 'key2': 'value2'}

    def _transform_dict_keys(self, facts_dict):
        return {'transformed_' + k: v for k, v in facts_dict.items()}

@pytest.fixture
def mock_collector():
    collector = MockFactCollector()
    return collector

def test_collect_with_namespace(mock_collector):
    facts = mock_collector.collect_with_namespace()
    assert 'transformed_key1' in facts
    assert 'transformed_key2' in facts
    assert facts['transformed_key1'] == 'value1'
    assert facts['transformed_key2'] == 'value2'
