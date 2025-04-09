# file lib/ansible/module_utils/facts/ansible_collector.py:121-156
# lines [128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 140, 141, 142, 143, 146, 147, 148, 149, 151, 152, 153, 154, 156]
# branches ['141->142', '141->146']

import pytest
from ansible.module_utils.facts import timeout
from ansible.module_utils.facts.ansible_collector import get_ansible_collector
from ansible.module_utils.facts.collector import BaseFactCollector

# Mock classes to simulate collector behavior
class MockCollector(BaseFactCollector):
    name = 'mock_collector'
    _fact_ids = set()

    def collect(self, module=None, collected_facts=None):
        return {}

class CollectorMetaDataCollector(BaseFactCollector):
    name = 'collector_meta_data_collector'
    _fact_ids = set()

    def collect(self, module=None, collected_facts=None):
        return {}

# Test function to cover lines 128-156
def test_get_ansible_collector(mocker):
    # Mock the collector_classes_from_gather_subset function
    mocker.patch('ansible.module_utils.facts.ansible_collector.collector.collector_classes_from_gather_subset',
                 return_value=[MockCollector])

    # Mock the CollectorMetaDataCollector class
    mocker.patch('ansible.module_utils.facts.ansible_collector.CollectorMetaDataCollector',
                 return_value=CollectorMetaDataCollector())

    # Call the function with default parameters to cover lines 128-156
    fact_collector = get_ansible_collector(all_collector_classes=[MockCollector])

    # Assertions to verify postconditions
    assert 'mock_collector' in [collector.name for collector in fact_collector.collectors]
    assert 'collector_meta_data_collector' in [collector.name for collector in fact_collector.collectors]
    assert fact_collector.filter_spec == []
    assert fact_collector.namespace is None

    # Clean up after the test
    mocker.stopall()
