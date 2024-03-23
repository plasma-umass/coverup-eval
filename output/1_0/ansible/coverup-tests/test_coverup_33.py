# file lib/ansible/module_utils/facts/virtual/base.py:58-78
# lines [58, 59, 60, 61, 68, 69, 70, 71, 74, 76, 78]
# branches ['70->71', '70->74']

import pytest
from ansible.module_utils.facts.virtual.base import VirtualCollector

class MockModule:
    pass

class MockVirtual:
    def __init__(self, module):
        pass

    def populate(self, collected_facts=None):
        return {'virtualization_type': 'test_type', 'virtualization_role': 'test_role'}

@pytest.fixture
def mock_virtual(mocker):
    mocker.patch('ansible.module_utils.facts.virtual.base.VirtualCollector._fact_class', new=MockVirtual)

def test_virtual_collector_collect_with_module(mock_virtual):
    module = MockModule()
    virtual_collector = VirtualCollector()
    collected_facts = {'existing_fact': 'existing_value'}
    facts_dict = virtual_collector.collect(module=module, collected_facts=collected_facts)

    assert facts_dict == {'virtualization_type': 'test_type', 'virtualization_role': 'test_role'}
    assert 'existing_fact' not in facts_dict  # Ensure existing facts are not included

def test_virtual_collector_collect_without_module(mock_virtual):
    virtual_collector = VirtualCollector()
    facts_dict = virtual_collector.collect(module=None, collected_facts=None)

    assert facts_dict == {}
