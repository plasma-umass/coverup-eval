# file: lib/ansible/inventory/helpers.py:29-40
# asked: {"lines": [29, 36, 37, 38, 40], "branches": [[37, 38], [37, 40]]}
# gained: {"lines": [29, 36, 37, 38, 40], "branches": [[37, 38], [37, 40]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.helpers import get_group_vars
from ansible.inventory.group import Group

@pytest.fixture
def mock_group():
    group = MagicMock(spec=Group)
    group.get_vars.return_value = {'var1': 'value1'}
    return group

@pytest.fixture
def mock_groups(mock_group):
    return [mock_group]

@patch('ansible.inventory.helpers.sort_groups')
@patch('ansible.inventory.helpers.combine_vars')
def test_get_group_vars(mock_combine_vars, mock_sort_groups, mock_groups):
    mock_sort_groups.return_value = mock_groups
    mock_combine_vars.side_effect = lambda a, b: {**a, **b}

    result = get_group_vars(mock_groups)

    mock_sort_groups.assert_called_once_with(mock_groups)
    assert mock_combine_vars.call_count == len(mock_groups)
    assert result == {'var1': 'value1'}
