# file lib/ansible/module_utils/facts/collector.py:239-251
# lines [239, 240, 242, 244, 245, 246, 247, 248, 249, 251]
# branches ['244->245', '244->251', '246->244', '246->247', '247->246', '247->248']

import pytest
from ansible.module_utils.facts.collector import select_collector_classes

class MockCollector1:
    pass

class MockCollector2:
    pass

@pytest.fixture
def all_fact_subsets():
    return {
        'subset1': [MockCollector1],
        'subset2': [MockCollector2],
        'subset3': [MockCollector1, MockCollector2],
    }

def test_select_collector_classes(all_fact_subsets):
    collector_names = ['subset1', 'subset2', 'subset3']
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    
    assert MockCollector1 in selected_classes
    assert MockCollector2 in selected_classes
    assert len(selected_classes) == 2  # Ensure no duplicates

def test_select_collector_classes_empty(all_fact_subsets):
    collector_names = []
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    
    assert len(selected_classes) == 0  # Ensure it works with empty input

def test_select_collector_classes_non_existent(all_fact_subsets):
    collector_names = ['non_existent_subset']
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    
    assert len(selected_classes) == 0  # Ensure it works with non-existent keys
