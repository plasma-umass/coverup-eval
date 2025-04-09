# file: lib/ansible/vars/reserved.py:68-79
# asked: {"lines": [68, 71, 72, 74, 76, 77, 78, 79], "branches": [[71, 72], [71, 74], [78, 0], [78, 79]]}
# gained: {"lines": [68, 71, 72, 74, 76, 77, 78, 79], "branches": [[71, 72], [71, 74], [78, 0], [78, 79]]}

import pytest
from unittest.mock import patch

# Assuming _RESERVED_NAMES and display.warning are imported from ansible.vars.reserved
from ansible.vars.reserved import warn_if_reserved, _RESERVED_NAMES

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch('ansible.vars.reserved.display.warning')

def test_warn_if_reserved_no_additional(mock_display_warning):
    myvars = ['foo', 'bar', 'baz']
    reserved_names = _RESERVED_NAMES

    warn_if_reserved(myvars)

    for var in myvars:
        if var in reserved_names:
            mock_display_warning.assert_any_call(f'Found variable using reserved name: {var}')
    assert mock_display_warning.call_count == len([var for var in myvars if var in reserved_names])

def test_warn_if_reserved_with_additional(mock_display_warning):
    myvars = ['foo', 'bar', 'baz']
    additional_reserved = {'bar', 'qux'}
    reserved_names = _RESERVED_NAMES.union(additional_reserved)

    warn_if_reserved(myvars, additional_reserved)

    for var in myvars:
        if var in reserved_names:
            mock_display_warning.assert_any_call(f'Found variable using reserved name: {var}')
    assert mock_display_warning.call_count == len([var for var in myvars if var in reserved_names])

def test_warn_if_reserved_ignore_vars(mock_display_warning):
    myvars = ['vars', 'foo', 'bar']
    reserved_names = _RESERVED_NAMES

    warn_if_reserved(myvars)

    assert mock_display_warning.call_count == len([var for var in myvars if var in reserved_names and var != 'vars'])
