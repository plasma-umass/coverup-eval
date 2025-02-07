# file: lib/ansible/module_utils/facts/collector.py:239-251
# asked: {"lines": [239, 240, 242, 244, 245, 246, 247, 248, 249, 251], "branches": [[244, 245], [244, 251], [246, 244], [246, 247], [247, 246], [247, 248]]}
# gained: {"lines": [239, 240, 242, 244, 245, 246, 247, 248, 249, 251], "branches": [[244, 245], [244, 251], [246, 244], [246, 247], [247, 246], [247, 248]]}

import pytest
from ansible.module_utils.facts.collector import select_collector_classes

def test_select_collector_classes():
    collector_names = ['network', 'hardware']
    all_fact_subsets = {
        'network': ['NetworkCollector'],
        'hardware': ['HardwareCollector', 'NetworkCollector']
    }
    
    result = select_collector_classes(collector_names, all_fact_subsets)
    
    assert result == ['NetworkCollector', 'HardwareCollector']

def test_select_collector_classes_empty():
    collector_names = []
    all_fact_subsets = {
        'network': ['NetworkCollector'],
        'hardware': ['HardwareCollector']
    }
    
    result = select_collector_classes(collector_names, all_fact_subsets)
    
    assert result == []

def test_select_collector_classes_no_duplicates():
    collector_names = ['network', 'network']
    all_fact_subsets = {
        'network': ['NetworkCollector'],
    }
    
    result = select_collector_classes(collector_names, all_fact_subsets)
    
    assert result == ['NetworkCollector']
