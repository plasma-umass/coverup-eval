# file lib/ansible/module_utils/facts/collector.py:266-280
# lines [272, 274, 275, 276, 277, 278, 280]
# branches ['274->275', '274->280', '276->274', '276->277', '277->276', '277->278']

import pytest
from ansible.module_utils.facts.collector import find_unresolved_requires

# Mock function to replace _get_requires_by_collector_name
def mock_get_requires_by_collector_name(collector_name, all_fact_subsets):
    return all_fact_subsets.get(collector_name, [])

@pytest.fixture
def mock_get_requires(mocker):
    # Use pytest-mock to patch the _get_requires_by_collector_name function
    mocker.patch('ansible.module_utils.facts.collector._get_requires_by_collector_name', side_effect=mock_get_requires_by_collector_name)

def test_find_unresolved_requires_with_unresolved(mock_get_requires):
    collector_names = {'network', 'virtual'}
    all_fact_subsets = {
        'network': ['interfaces'],
        'virtual': ['is_virtual'],
        'hardware': ['memory', 'cpu']
    }

    # Call the function under test
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)

    # Assert that the unresolved requirements are correctly identified
    assert unresolved == {'interfaces', 'is_virtual'}, "The unresolved requirements should be 'interfaces' and 'is_virtual'"

def test_find_unresolved_requires_with_no_unresolved(mock_get_requires):
    collector_names = {'network', 'virtual', 'interfaces', 'is_virtual'}
    all_fact_subsets = {
        'network': ['interfaces'],
        'virtual': ['is_virtual']
    }

    # Call the function under test
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)

    # Assert that there are no unresolved requirements
    assert not unresolved, "There should be no unresolved requirements"
