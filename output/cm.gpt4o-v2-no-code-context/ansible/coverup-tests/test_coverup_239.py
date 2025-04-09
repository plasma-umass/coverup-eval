# file: lib/ansible/module_utils/facts/ansible_collector.py:103-118
# asked: {"lines": [103, 104, 106, 107, 109, 110, 111, 112, 114, 115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}
# gained: {"lines": [103, 104, 106, 107, 109, 110, 111, 112, 114, 115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}

import pytest
from ansible.module_utils.facts.ansible_collector import CollectorMetaDataCollector
from ansible.module_utils.facts.collector import BaseFactCollector

class MockBaseFactCollector(BaseFactCollector):
    def __init__(self, collectors=None, namespace=None):
        self.collectors = collectors
        self.namespace = namespace

@pytest.fixture
def mock_base_fact_collector(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.ansible_collector.collector.BaseFactCollector', MockBaseFactCollector)

def test_collector_metadata_collector_init(mock_base_fact_collector):
    collector = CollectorMetaDataCollector(collectors=['test_collector'], namespace='test_namespace', gather_subset=['test_subset'], module_setup={'key': 'value'})
    assert collector.collectors == ['test_collector']
    assert collector.namespace == 'test_namespace'
    assert collector.gather_subset == ['test_subset']
    assert collector.module_setup == {'key': 'value'}

def test_collector_metadata_collector_collect_without_module_setup(mock_base_fact_collector):
    collector = CollectorMetaDataCollector(gather_subset=['test_subset'])
    result = collector.collect()
    assert result == {'gather_subset': ['test_subset']}

def test_collector_metadata_collector_collect_with_module_setup(mock_base_fact_collector):
    collector = CollectorMetaDataCollector(gather_subset=['test_subset'], module_setup={'key': 'value'})
    result = collector.collect()
    assert result == {'gather_subset': ['test_subset'], 'module_setup': {'key': 'value'}}
