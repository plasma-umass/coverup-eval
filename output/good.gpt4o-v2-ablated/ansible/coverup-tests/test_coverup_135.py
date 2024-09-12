# file: lib/ansible/vars/reserved.py:68-79
# asked: {"lines": [68, 71, 72, 74, 76, 77, 78, 79], "branches": [[71, 72], [71, 74], [78, 0], [78, 79]]}
# gained: {"lines": [68, 71, 72, 74, 76, 77, 78, 79], "branches": [[71, 72], [71, 74], [78, 0], [78, 79]]}

import pytest
from unittest.mock import patch

# Assuming _RESERVED_NAMES and display.warning are defined in the ansible.vars.reserved module
from ansible.vars.reserved import warn_if_reserved, _RESERVED_NAMES

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch('ansible.vars.reserved.display.warning')

def test_warn_if_reserved_no_additional(mock_display_warning):
    myvars = {'some_var', 'another_var', 'vars'}
    warn_if_reserved(myvars)
    mock_display_warning.assert_not_called()

def test_warn_if_reserved_with_reserved_name(mock_display_warning):
    myvars = {'some_var', 'another_var', 'vars'}
    reserved_name = next(iter(_RESERVED_NAMES))
    myvars.add(reserved_name)
    warn_if_reserved(myvars)
    mock_display_warning.assert_called_once_with(f'Found variable using reserved name: {reserved_name}')

def test_warn_if_reserved_with_additional(mock_display_warning):
    myvars = {'some_var', 'another_var', 'vars'}
    additional_reserved = {'additional_reserved_var'}
    myvars.add('additional_reserved_var')
    warn_if_reserved(myvars, additional_reserved)
    mock_display_warning.assert_called_once_with('Found variable using reserved name: additional_reserved_var')

def test_warn_if_reserved_with_additional_no_conflict(mock_display_warning):
    myvars = {'some_var', 'another_var', 'vars'}
    additional_reserved = {'additional_reserved_var'}
    warn_if_reserved(myvars, additional_reserved)
    mock_display_warning.assert_not_called()
