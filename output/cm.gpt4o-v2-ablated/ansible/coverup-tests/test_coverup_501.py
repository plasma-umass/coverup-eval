# file: lib/ansible/module_utils/facts/ansible_collector.py:103-118
# asked: {"lines": [110, 111, 112, 115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}
# gained: {"lines": [110, 111, 112, 115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}

import pytest
from ansible.module_utils.facts import collector
from ansible.module_utils.facts.ansible_collector import CollectorMetaDataCollector

class MockBaseFactCollector:
    def __init__(self, collectors=None, namespace=None):
        self.collectors = collectors
        self.namespace = namespace

@pytest.fixture
def mock_base_fact_collector(monkeypatch):
    monkeypatch.setattr(collector, 'BaseFactCollector', MockBaseFactCollector)

def test_collector_metadata_collector_init(mock_base_fact_collector):
    gather_subset = ['all']
    module_setup = {'key': 'value'}
    collector_instance = CollectorMetaDataCollector(gather_subset=gather_subset, module_setup=module_setup)
    
    assert collector_instance.gather_subset == gather_subset
    assert collector_instance.module_setup == module_setup

def test_collector_metadata_collector_collect_with_module_setup(mock_base_fact_collector):
    gather_subset = ['all']
    module_setup = {'key': 'value'}
    collector_instance = CollectorMetaDataCollector(gather_subset=gather_subset, module_setup=module_setup)
    
    result = collector_instance.collect()
    
    assert result == {'gather_subset': gather_subset, 'module_setup': module_setup}

def test_collector_metadata_collector_collect_without_module_setup(mock_base_fact_collector):
    gather_subset = ['all']
    collector_instance = CollectorMetaDataCollector(gather_subset=gather_subset)
    
    result = collector_instance.collect()
    
    assert result == {'gather_subset': gather_subset}
