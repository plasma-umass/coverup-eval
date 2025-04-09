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

@pytest.fixture
def collector_instance():
    return CollectorMetaDataCollector(gather_subset='test_subset', module_setup='test_setup')

def test_collector_metadata_collector_init(collector_instance):
    assert collector_instance.gather_subset == 'test_subset'
    assert collector_instance.module_setup == 'test_setup'
    assert collector_instance.name == 'gather_subset'
    assert collector_instance._fact_ids == set([])

def test_collect_with_module_setup(collector_instance, mock_module):
    result = collector_instance.collect(module=mock_module)
    assert result == {'gather_subset': 'test_subset', 'module_setup': 'test_setup'}

def test_collect_without_module_setup():
    collector = CollectorMetaDataCollector(gather_subset='test_subset')
    result = collector.collect()
    assert result == {'gather_subset': 'test_subset'}
