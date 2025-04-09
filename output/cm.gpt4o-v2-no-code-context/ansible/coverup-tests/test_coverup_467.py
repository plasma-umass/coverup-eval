# file: lib/ansible/inventory/helpers.py:29-40
# asked: {"lines": [29, 36, 37, 38, 40], "branches": [[37, 38], [37, 40]]}
# gained: {"lines": [29, 36, 37, 38, 40], "branches": [[37, 38], [37, 40]]}

import pytest
from unittest.mock import MagicMock

# Assuming the functions sort_groups and combine_vars are imported from the same module
from ansible.inventory.helpers import get_group_vars, sort_groups, combine_vars

@pytest.fixture
def mock_sort_groups(mocker):
    return mocker.patch('ansible.inventory.helpers.sort_groups')

@pytest.fixture
def mock_combine_vars(mocker):
    return mocker.patch('ansible.inventory.helpers.combine_vars')

def test_get_group_vars_empty(mock_sort_groups, mock_combine_vars):
    mock_sort_groups.return_value = []
    mock_combine_vars.side_effect = lambda x, y: {**x, **y}

    result = get_group_vars([])

    assert result == {}
    mock_sort_groups.assert_called_once_with([])
    mock_combine_vars.assert_not_called()

def test_get_group_vars_non_empty(mock_sort_groups, mock_combine_vars):
    group1 = MagicMock()
    group1.get_vars.return_value = {'var1': 'value1'}
    group2 = MagicMock()
    group2.get_vars.return_value = {'var2': 'value2'}

    mock_sort_groups.return_value = [group1, group2]
    mock_combine_vars.side_effect = lambda x, y: {**x, **y}

    result = get_group_vars([group1, group2])

    assert result == {'var1': 'value1', 'var2': 'value2'}
    mock_sort_groups.assert_called_once_with([group1, group2])
    assert mock_combine_vars.call_count == 2
    mock_combine_vars.assert_any_call({}, {'var1': 'value1'})
    mock_combine_vars.assert_any_call({'var1': 'value1'}, {'var2': 'value2'})
