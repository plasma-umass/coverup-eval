# file lib/ansible/inventory/helpers.py:29-40
# lines [29, 36, 37, 38, 40]
# branches ['37->38', '37->40']

import pytest
from unittest.mock import Mock, patch

# Assuming the following imports are correct based on the provided code snippet
from ansible.inventory.helpers import get_group_vars

# Mocking the sort_groups and combine_vars functions
@pytest.fixture
def mock_sort_groups(mocker):
    return mocker.patch('ansible.inventory.helpers.sort_groups')

@pytest.fixture
def mock_combine_vars(mocker):
    return mocker.patch('ansible.inventory.helpers.combine_vars')

def test_get_group_vars(mock_sort_groups, mock_combine_vars):
    # Mocking the group objects and their get_vars method
    group1 = Mock()
    group1.get_vars.return_value = {'var1': 'value1'}
    
    group2 = Mock()
    group2.get_vars.return_value = {'var2': 'value2'}
    
    groups = [group1, group2]
    
    # Mocking the sort_groups function to return the groups in a specific order
    mock_sort_groups.return_value = groups
    
    # Mocking the combine_vars function to combine dictionaries
    def combine_vars_side_effect(dict1, dict2):
        result = dict1.copy()
        result.update(dict2)
        return result
    
    mock_combine_vars.side_effect = combine_vars_side_effect
    
    # Calling the function under test
    result = get_group_vars(groups)
    
    # Asserting the expected result
    assert result == {'var1': 'value1', 'var2': 'value2'}
    
    # Asserting that sort_groups was called with the correct argument
    mock_sort_groups.assert_called_once_with(groups)
    
    # Asserting that combine_vars was called the correct number of times with the correct arguments
    assert mock_combine_vars.call_count == 2
    mock_combine_vars.assert_any_call({}, {'var1': 'value1'})
    mock_combine_vars.assert_any_call({'var1': 'value1'}, {'var2': 'value2'})
