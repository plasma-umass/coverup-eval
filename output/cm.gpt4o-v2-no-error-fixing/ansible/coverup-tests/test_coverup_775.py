# file: lib/ansible/vars/reserved.py:68-79
# asked: {"lines": [71, 72, 74, 76, 77, 78, 79], "branches": [[71, 72], [71, 74], [78, 0], [78, 79]]}
# gained: {"lines": [71, 72, 74, 76, 77, 78, 79], "branches": [[71, 72], [71, 74], [78, 0], [78, 79]]}

import pytest
from unittest.mock import patch
from ansible.vars.reserved import warn_if_reserved, _RESERVED_NAMES

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch('ansible.vars.reserved.display.warning')

def test_warn_if_reserved_no_additional(mock_display_warning):
    myvars = {'reserved_var1': 'value1', 'vars': 'value2'}
    reserved_name = next(iter(_RESERVED_NAMES))
    myvars[reserved_name] = 'value3'
    
    warn_if_reserved(myvars)
    
    mock_display_warning.assert_called_once_with(f'Found variable using reserved name: {reserved_name}')

def test_warn_if_reserved_with_additional(mock_display_warning):
    myvars = {'reserved_var2': 'value1', 'vars': 'value2'}
    additional_reserved = {'additional_reserved_var'}
    myvars['additional_reserved_var'] = 'value3'
    
    warn_if_reserved(myvars, additional_reserved)
    
    mock_display_warning.assert_called_once_with('Found variable using reserved name: additional_reserved_var')
