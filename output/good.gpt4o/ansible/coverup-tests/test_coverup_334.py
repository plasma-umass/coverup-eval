# file lib/ansible/module_utils/facts/collector.py:330-342
# lines [330, 331, 332, 334, 335, 336, 337, 339, 340, 342]
# branches ['334->335', '336->337', '336->339']

import pytest
from unittest.mock import patch

# Assuming the functions find_unresolved_requires and resolve_requires are imported from the same module
from ansible.module_utils.facts.collector import _solve_deps

def test_solve_deps(mocker):
    # Mocking the find_unresolved_requires and resolve_requires functions
    mock_find_unresolved_requires = mocker.patch('ansible.module_utils.facts.collector.find_unresolved_requires')
    mock_resolve_requires = mocker.patch('ansible.module_utils.facts.collector.resolve_requires')

    # Setting up the mock return values
    mock_find_unresolved_requires.side_effect = [
        {'dep1', 'dep2'},  # First call returns unresolved dependencies
        set()              # Second call returns an empty set, indicating all dependencies are resolved
    ]
    mock_resolve_requires.return_value = {'dep3'}

    collector_names = {'collector1', 'collector2'}
    all_fact_subsets = {
        'collector1': {'requires': []},
        'collector2': {'requires': []},
        'dep1': {'requires': []},
        'dep2': {'requires': []},
        'dep3': {'requires': []}
    }

    result = _solve_deps(collector_names, all_fact_subsets)

    # Assertions to verify the correct behavior
    assert result == {'collector1', 'collector2', 'dep3'}
    mock_find_unresolved_requires.assert_called_with({'collector1', 'collector2', 'dep3'}, all_fact_subsets)
    mock_resolve_requires.assert_called_with({'dep1', 'dep2'}, all_fact_subsets)
