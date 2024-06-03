# file lib/ansible/vars/reserved.py:82-83
# lines [83]
# branches []

import pytest
from ansible.vars.reserved import is_reserved_name

def test_is_reserved_name(mocker):
    # Mock the _RESERVED_NAMES to ensure the test is isolated
    mock_reserved_names = mocker.patch('ansible.vars.reserved._RESERVED_NAMES', new_callable=set)
    
    # Add a reserved name to the mock set
    mock_reserved_names.add('reserved_name')
    
    # Test that the function returns True for a reserved name
    assert is_reserved_name('reserved_name') is True
    
    # Test that the function returns False for a non-reserved name
    assert is_reserved_name('non_reserved_name') is False
