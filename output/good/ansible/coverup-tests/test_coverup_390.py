# file lib/ansible/vars/reserved.py:68-79
# lines [68, 71, 72, 74, 76, 77, 78, 79]
# branches ['71->72', '71->74', '78->exit', '78->79']

import pytest
from ansible.vars.reserved import warn_if_reserved, _RESERVED_NAMES
from ansible.utils.display import Display

# Mock the global display object used by the warn_if_reserved function
@pytest.fixture
def mock_display(mocker):
    mock = mocker.patch('ansible.vars.reserved.display', spec=Display)
    return mock

# Test function to cover the missing lines/branches in warn_if_reserved
def test_warn_if_reserved_with_additional(mock_display):
    test_vars = {'ansible_var': 1, 'custom_var': 2}
    additional_reserved = {'custom_var'}
    warn_if_reserved(test_vars, additional=additional_reserved)
    mock_display.warning.assert_called_once_with('Found variable using reserved name: custom_var')

def test_warn_if_reserved_without_additional(mock_display):
    test_vars = {'ansible_var': 1, 'vars': 2}
    warn_if_reserved(test_vars)
    reserved_without_vars = _RESERVED_NAMES - {'vars'}
    intersected_vars = reserved_without_vars.intersection(test_vars)
    if intersected_vars:
        expected_call = 'Found variable using reserved name: ' + next(iter(intersected_vars))
        mock_display.warning.assert_called_once_with(expected_call)
    else:
        mock_display.warning.assert_not_called()
