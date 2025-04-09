# file: lib/ansible/module_utils/facts/collector.py:239-251
# asked: {"lines": [239, 240, 242, 244, 245, 246, 247, 248, 249, 251], "branches": [[244, 245], [244, 251], [246, 244], [246, 247], [247, 246], [247, 248]]}
# gained: {"lines": [239, 240, 242, 244, 245, 246, 247, 248, 249, 251], "branches": [[244, 245], [244, 251], [246, 244], [246, 247], [247, 246], [247, 248]]}

import pytest
from ansible.module_utils.facts.collector import select_collector_classes

def test_select_collector_classes():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': ['classA', 'classB'],
        'collector2': ['classB', 'classC'],
        'collector3': ['classD']
    }
    
    expected_result = ['classA', 'classB', 'classC']
    result = select_collector_classes(collector_names, all_fact_subsets)
    
    assert result == expected_result

def test_select_collector_classes_empty():
    collector_names = []
    all_fact_subsets = {
        'collector1': ['classA', 'classB'],
        'collector2': ['classB', 'classC'],
        'collector3': ['classD']
    }
    
    expected_result = []
    result = select_collector_classes(collector_names, all_fact_subsets)
    
    assert result == expected_result

def test_select_collector_classes_no_matching_collectors():
    collector_names = ['collector4']
    all_fact_subsets = {
        'collector1': ['classA', 'classB'],
        'collector2': ['classB', 'classC'],
        'collector3': ['classD']
    }
    
    expected_result = []
    result = select_collector_classes(collector_names, all_fact_subsets)
    
    assert result == expected_result
