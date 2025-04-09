# file lib/ansible/module_utils/facts/collector.py:239-251
# lines [239, 240, 242, 244, 245, 246, 247, 248, 249, 251]
# branches ['244->245', '244->251', '246->244', '246->247', '247->246', '247->248']

import pytest
from ansible.module_utils.facts.collector import select_collector_classes

def test_select_collector_classes():
    collector_names = ['network', 'hardware', 'software']
    all_fact_subsets = {
        'network': ['NetworkCollector'],
        'hardware': ['HardwareCollector'],
        'software': ['SoftwareCollector', 'AdvancedSoftwareCollector'],
        'unused': ['UnusedCollector']
    }

    result = select_collector_classes(collector_names, all_fact_subsets)
    
    assert result == ['NetworkCollector', 'HardwareCollector', 'SoftwareCollector', 'AdvancedSoftwareCollector']

    # Test with duplicate collector names
    collector_names = ['network', 'network', 'hardware']
    result = select_collector_classes(collector_names, all_fact_subsets)
    
    assert result == ['NetworkCollector', 'HardwareCollector']

    # Test with no matching collector names
    collector_names = ['nonexistent']
    result = select_collector_classes(collector_names, all_fact_subsets)
    
    assert result == []

    # Test with empty collector names
    collector_names = []
    result = select_collector_classes(collector_names, all_fact_subsets)
    
    assert result == []
