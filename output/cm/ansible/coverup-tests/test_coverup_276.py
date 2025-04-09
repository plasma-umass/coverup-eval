# file lib/ansible/module_utils/facts/ansible_collector.py:103-118
# lines [103, 104, 106, 107, 109, 110, 111, 112, 114, 115, 116, 117, 118]
# branches ['116->117', '116->118']

import pytest
from ansible.module_utils.facts.ansible_collector import CollectorMetaDataCollector
from ansible.module_utils.facts import collector

@pytest.fixture
def collector_metadata_collector():
    return CollectorMetaDataCollector(gather_subset=['all'], module_setup=True)

def test_collector_metadata_collector_collect_with_module_setup(collector_metadata_collector):
    collected_facts = collector_metadata_collector.collect()
    assert 'gather_subset' in collected_facts
    assert collected_facts['gather_subset'] == ['all']
    assert 'module_setup' in collected_facts
    assert collected_facts['module_setup'] is True

def test_collector_metadata_collector_collect_without_module_setup():
    collector_without_module_setup = CollectorMetaDataCollector(gather_subset=['network'], module_setup=False)
    collected_facts = collector_without_module_setup.collect()
    assert 'gather_subset' in collected_facts
    assert collected_facts['gather_subset'] == ['network']
    assert 'module_setup' not in collected_facts
