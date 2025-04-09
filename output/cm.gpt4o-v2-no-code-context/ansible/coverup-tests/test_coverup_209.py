# file: lib/ansible/module_utils/facts/collector.py:239-251
# asked: {"lines": [239, 240, 242, 244, 245, 246, 247, 248, 249, 251], "branches": [[244, 245], [244, 251], [246, 244], [246, 247], [247, 246], [247, 248]]}
# gained: {"lines": [239, 240, 242, 244, 245, 246, 247, 248, 249, 251], "branches": [[244, 245], [244, 251], [246, 244], [246, 247], [247, 246], [247, 248]]}

import pytest
from ansible.module_utils.facts.collector import select_collector_classes

def test_select_collector_classes_empty():
    result = select_collector_classes([], {})
    assert result == []

def test_select_collector_classes_no_duplicates():
    class CollectorA:
        pass

    class CollectorB:
        pass

    all_fact_subsets = {
        'subset1': [CollectorA, CollectorB],
        'subset2': [CollectorA]
    }
    result = select_collector_classes(['subset1', 'subset2'], all_fact_subsets)
    assert result == [CollectorA, CollectorB]

def test_select_collector_classes_with_duplicates():
    class CollectorA:
        pass

    class CollectorB:
        pass

    all_fact_subsets = {
        'subset1': [CollectorA, CollectorB],
        'subset2': [CollectorA, CollectorB]
    }
    result = select_collector_classes(['subset1', 'subset2'], all_fact_subsets)
    assert result == [CollectorA, CollectorB]

def test_select_collector_classes_partial_match():
    class CollectorA:
        pass

    class CollectorB:
        pass

    all_fact_subsets = {
        'subset1': [CollectorA],
        'subset2': [CollectorB]
    }
    result = select_collector_classes(['subset1', 'subset2'], all_fact_subsets)
    assert result == [CollectorA, CollectorB]

def test_select_collector_classes_nonexistent_subset():
    class CollectorA:
        pass

    all_fact_subsets = {
        'subset1': [CollectorA]
    }
    result = select_collector_classes(['subset1', 'subset2'], all_fact_subsets)
    assert result == [CollectorA]

def test_select_collector_classes_empty_subset():
    class CollectorA:
        pass

    all_fact_subsets = {
        'subset1': [CollectorA],
        'subset2': []
    }
    result = select_collector_classes(['subset1', 'subset2'], all_fact_subsets)
    assert result == [CollectorA]
