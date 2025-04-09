# file: lib/ansible/vars/reserved.py:68-79
# asked: {"lines": [71, 72, 74, 76, 77, 78, 79], "branches": [[71, 72], [71, 74], [78, 0], [78, 79]]}
# gained: {"lines": [71, 72, 74, 76, 77, 78, 79], "branches": [[71, 72], [71, 74], [78, 0], [78, 79]]}

import pytest
from unittest.mock import patch

# Assuming the function and _RESERVED_NAMES are imported from ansible/vars/reserved.py
from ansible.vars.reserved import warn_if_reserved, _RESERVED_NAMES

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch('ansible.vars.reserved.display.warning')

def test_warn_if_reserved_no_additional(mock_display_warning):
    myvars = {'foo': 'bar', 'ansible_version': '2.9'}
    with patch('ansible.vars.reserved._RESERVED_NAMES', {'ansible_version'}):
        warn_if_reserved(myvars)
    mock_display_warning.assert_called_once_with('Found variable using reserved name: ansible_version')

def test_warn_if_reserved_with_additional(mock_display_warning):
    myvars = {'foo': 'bar', 'custom_reserved': 'value'}
    additional_reserved = {'custom_reserved'}
    with patch('ansible.vars.reserved._RESERVED_NAMES', set()):
        warn_if_reserved(myvars, additional_reserved)
    mock_display_warning.assert_called_once_with('Found variable using reserved name: custom_reserved')

def test_warn_if_reserved_vars_discarded(mock_display_warning):
    myvars = {'vars': 'value', 'ansible_version': '2.9'}
    with patch('ansible.vars.reserved._RESERVED_NAMES', {'ansible_version'}):
        warn_if_reserved(myvars)
    mock_display_warning.assert_called_once_with('Found variable using reserved name: ansible_version')

def test_warn_if_reserved_no_conflict(mock_display_warning):
    myvars = {'foo': 'bar', 'baz': 'qux'}
    with patch('ansible.vars.reserved._RESERVED_NAMES', {'ansible_version'}):
        warn_if_reserved(myvars)
    mock_display_warning.assert_not_called()
