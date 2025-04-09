# file lib/ansible/vars/reserved.py:68-79
# lines [68, 71, 72, 74, 76, 77, 78, 79]
# branches ['71->72', '71->74', '78->exit', '78->79']

import pytest
from unittest import mock
from ansible.vars.reserved import warn_if_reserved, _RESERVED_NAMES

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch('ansible.vars.reserved.display.warning')

def test_warn_if_reserved_no_additional(mock_display_warning):
    myvars = {next(iter(_RESERVED_NAMES)): '2.9', 'vars': 'some_value'}
    warn_if_reserved(myvars)
    mock_display_warning.assert_called_once_with(f'Found variable using reserved name: {next(iter(_RESERVED_NAMES))}')

def test_warn_if_reserved_with_additional(mock_display_warning):
    myvars = {'custom_var': 'value', 'vars': 'some_value'}
    additional_reserved = {'custom_var'}
    warn_if_reserved(myvars, additional_reserved)
    mock_display_warning.assert_called_once_with('Found variable using reserved name: custom_var')

def test_warn_if_reserved_no_conflict(mock_display_warning):
    myvars = {'non_reserved_var': 'value', 'vars': 'some_value'}
    warn_if_reserved(myvars)
    mock_display_warning.assert_not_called()
