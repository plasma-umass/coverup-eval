# file lib/ansible/inventory/helpers.py:29-40
# lines [36, 37, 38, 40]
# branches ['37->38', '37->40']

import pytest
from ansible.inventory.group import Group
from ansible.inventory.helpers import get_group_vars, sort_groups, combine_vars

# Mocking the sort_groups and combine_vars functions
@pytest.fixture
def mock_sort_groups(mocker):
    return mocker.patch('ansible.inventory.helpers.sort_groups', return_value=[])

@pytest.fixture
def mock_combine_vars(mocker):
    return mocker.patch('ansible.inventory.helpers.combine_vars', return_value={})

# Test function to cover lines 36-40
def test_get_group_vars_with_empty_groups(mock_sort_groups, mock_combine_vars):
    groups = []  # Empty list of groups
    result = get_group_vars(groups)
    assert result == {}  # Asserting that the result is an empty dictionary
    mock_sort_groups.assert_called_once_with(groups)  # Assert sort_groups was called
    mock_combine_vars.assert_not_called()  # Assert combine_vars was not called since there are no groups

# Test function to cover lines 36-40 with non-empty groups
def test_get_group_vars_with_non_empty_groups(mock_sort_groups, mock_combine_vars):
    # Creating mock Group objects
    group1 = Group(name='group1')
    group2 = Group(name='group2')
    groups = [group1, group2]

    # Setting up the return value for sort_groups
    mock_sort_groups.return_value = groups

    # Setting up the return value for combine_vars
    def combine_vars_side_effect(vars1, vars2):
        vars1.update(vars2)
        return vars1

    mock_combine_vars.side_effect = combine_vars_side_effect

    # Expected result after combining vars from both groups
    expected_vars = {'key1': 'value1', 'key2': 'value2'}
    group1.vars = {'key1': 'value1'}
    group2.vars = {'key2': 'value2'}

    result = get_group_vars(groups)
    assert result == expected_vars  # Asserting that the result matches the expected combined vars
    mock_sort_groups.assert_called_once_with(groups)  # Assert sort_groups was called
    assert mock_combine_vars.call_count == 2  # Assert combine_vars was called twice (once for each group)
