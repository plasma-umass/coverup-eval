# file lib/ansible/module_utils/facts/ansible_collector.py:49-54
# lines [49, 51, 52, 54]
# branches []

import pytest
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector
from ansible.module_utils.facts import collector

# Mocking the BaseFactCollector to avoid side effects
class MockBaseFactCollector(collector.BaseFactCollector):
    def __init__(self, collectors=None, namespace=None):
        self.collectors = collectors
        self.namespace = namespace

@pytest.fixture
def mock_base_fact_collector(mocker):
    mocker.patch('ansible.module_utils.facts.collector.BaseFactCollector', MockBaseFactCollector)

def test_ansible_fact_collector_initialization(mock_base_fact_collector):
    collectors = ['collector1', 'collector2']
    namespace = 'test_namespace'
    filter_spec = {'key': 'value'}

    fact_collector = AnsibleFactCollector(collectors=collectors, namespace=namespace, filter_spec=filter_spec)

    assert fact_collector.collectors == collectors
    assert fact_collector.namespace == namespace
    assert fact_collector.filter_spec == filter_spec
