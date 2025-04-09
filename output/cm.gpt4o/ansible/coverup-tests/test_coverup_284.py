# file lib/ansible/module_utils/facts/ansible_collector.py:103-118
# lines [103, 104, 106, 107, 109, 110, 111, 112, 114, 115, 116, 117, 118]
# branches ['116->117', '116->118']

import pytest
from ansible.module_utils.facts.ansible_collector import CollectorMetaDataCollector
from ansible.module_utils.facts.collector import BaseFactCollector

def test_collector_metadata_collector(mocker):
    # Mocking the BaseFactCollector to avoid any side effects
    mocker.patch('ansible.module_utils.facts.collector.BaseFactCollector.__init__', return_value=None)

    # Test case 1: Only gather_subset is provided
    gather_subset = ['all']
    collector = CollectorMetaDataCollector(gather_subset=gather_subset)
    result = collector.collect()
    assert result == {'gather_subset': gather_subset}

    # Test case 2: Both gather_subset and module_setup are provided
    module_setup = {'some_key': 'some_value'}
    collector = CollectorMetaDataCollector(gather_subset=gather_subset, module_setup=module_setup)
    result = collector.collect()
    assert result == {'gather_subset': gather_subset, 'module_setup': module_setup}

    # Test case 3: Neither gather_subset nor module_setup is provided
    collector = CollectorMetaDataCollector()
    result = collector.collect()
    assert result == {'gather_subset': None}
