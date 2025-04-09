# file: lib/ansible/module_utils/facts/ansible_collector.py:103-118
# asked: {"lines": [103, 104, 106, 107, 109, 110, 111, 112, 114, 115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}
# gained: {"lines": [103, 104, 106, 107, 109, 110, 111, 112, 114, 115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector
from ansible.module_utils.facts.ansible_collector import CollectorMetaDataCollector

class MockModule:
    pass

@pytest.fixture
def mock_module():
    return MockModule()

def test_collector_metadata_collector_init():
    collectors = [BaseFactCollector()]
    namespace = 'test_namespace'
    gather_subset = 'test_subset'
    module_setup = 'test_setup'
    
    collector = CollectorMetaDataCollector(collectors, namespace, gather_subset, module_setup)
    
    assert collector.collectors == collectors
    assert collector.namespace == namespace
    assert collector.gather_subset == gather_subset
    assert collector.module_setup == module_setup

def test_collector_metadata_collector_collect(mock_module):
    gather_subset = 'test_subset'
    module_setup = 'test_setup'
    
    collector = CollectorMetaDataCollector(gather_subset=gather_subset, module_setup=module_setup)
    result = collector.collect(module=mock_module)
    
    assert result['gather_subset'] == gather_subset
    assert result['module_setup'] == module_setup

def test_collector_metadata_collector_collect_without_module_setup(mock_module):
    gather_subset = 'test_subset'
    
    collector = CollectorMetaDataCollector(gather_subset=gather_subset)
    result = collector.collect(module=mock_module)
    
    assert result['gather_subset'] == gather_subset
    assert 'module_setup' not in result
