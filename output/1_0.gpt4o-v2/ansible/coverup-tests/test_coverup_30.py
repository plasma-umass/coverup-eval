# file: lib/ansible/module_utils/facts/virtual/base.py:58-78
# asked: {"lines": [58, 59, 60, 61, 68, 69, 70, 71, 74, 76, 78], "branches": [[70, 71], [70, 74]]}
# gained: {"lines": [58, 59, 60, 61, 68, 69, 70, 71, 74, 76, 78], "branches": [[70, 71], [70, 74]]}

import pytest
from ansible.module_utils.facts.virtual.base import VirtualCollector, Virtual
from ansible.module_utils.facts.collector import BaseFactCollector

class MockModule:
    pass

class MockVirtual(Virtual):
    def populate(self, collected_facts=None):
        collected_facts = collected_facts or {}
        collected_facts.update({
            'virtualization_type': 'mock_type',
            'virtualization_role': 'mock_role',
            'virtualization_tech_guest': ['mock_guest'],
            'virtualization_tech_host': ['mock_host']
        })
        return collected_facts

@pytest.fixture
def mock_virtual(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.virtual.base.VirtualCollector._fact_class', MockVirtual)

def test_virtual_collector_collect_no_module(mock_virtual):
    collector = VirtualCollector()
    result = collector.collect(module=None)
    assert result == {}

def test_virtual_collector_collect_with_module(mock_virtual):
    collector = VirtualCollector()
    module = MockModule()
    collected_facts = {
        'existing_fact': 'existing_value'
    }
    result = collector.collect(module=module, collected_facts=collected_facts)
    assert result['virtualization_type'] == 'mock_type'
    assert result['virtualization_role'] == 'mock_role'
    assert result['virtualization_tech_guest'] == ['mock_guest']
    assert result['virtualization_tech_host'] == ['mock_host']
    assert result['existing_fact'] == 'existing_value'
