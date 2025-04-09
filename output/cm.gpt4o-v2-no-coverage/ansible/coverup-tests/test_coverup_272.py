# file: lib/ansible/module_utils/facts/collector.py:239-251
# asked: {"lines": [239, 240, 242, 244, 245, 246, 247, 248, 249, 251], "branches": [[244, 245], [244, 251], [246, 244], [246, 247], [247, 246], [247, 248]]}
# gained: {"lines": [239, 240, 242, 244, 245, 246, 247, 248, 249, 251], "branches": [[244, 245], [244, 251], [246, 244], [246, 247], [247, 246], [247, 248]]}

import pytest

from ansible.module_utils.facts.collector import select_collector_classes

def test_select_collector_classes_empty():
    result = select_collector_classes([], {})
    assert result == []

def test_select_collector_classes_no_duplicates():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': ['class1', 'class2'],
        'collector2': ['class3']
    }
    result = select_collector_classes(collector_names, all_fact_subsets)
    assert result == ['class1', 'class2', 'class3']

def test_select_collector_classes_with_duplicates():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': ['class1', 'class2'],
        'collector2': ['class2', 'class3']
    }
    result = select_collector_classes(collector_names, all_fact_subsets)
    assert result == ['class1', 'class2', 'class3']

def test_select_collector_classes_partial_match():
    collector_names = ['collector1', 'collector3']
    all_fact_subsets = {
        'collector1': ['class1', 'class2'],
        'collector2': ['class3'],
        'collector3': ['class4']
    }
    result = select_collector_classes(collector_names, all_fact_subsets)
    assert result == ['class1', 'class2', 'class4']
