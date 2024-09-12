# file: lib/ansible/module_utils/facts/ansible_collector.py:103-118
# asked: {"lines": [103, 104, 106, 107, 109, 110, 111, 112, 114, 115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}
# gained: {"lines": [103, 104, 106, 107, 109, 110, 111, 112, 114, 115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector
from ansible.module_utils.facts.ansible_collector import CollectorMetaDataCollector

class TestCollectorMetaDataCollector:
    
    def test_init(self):
        gather_subset = ['all']
        module_setup = {'setup': 'value'}
        collector_instance = CollectorMetaDataCollector(gather_subset=gather_subset, module_setup=module_setup)
        
        assert collector_instance.gather_subset == gather_subset
        assert collector_instance.module_setup == module_setup

    def test_collect_without_module_setup(self):
        gather_subset = ['all']
        collector_instance = CollectorMetaDataCollector(gather_subset=gather_subset)
        
        result = collector_instance.collect()
        
        assert result == {'gather_subset': gather_subset}
    
    def test_collect_with_module_setup(self):
        gather_subset = ['all']
        module_setup = {'setup': 'value'}
        collector_instance = CollectorMetaDataCollector(gather_subset=gather_subset, module_setup=module_setup)
        
        result = collector_instance.collect()
        
        assert result == {'gather_subset': gather_subset, 'module_setup': module_setup}
