# file lib/ansible/vars/reserved.py:82-83
# lines [82, 83]
# branches []

import pytest
from unittest import mock

# Assuming _RESERVED_NAMES is a list of reserved names
_RESERVED_NAMES = ['ansible', 'vars', 'reserved']

def is_reserved_name(name):
    return name in _RESERVED_NAMES

def test_is_reserved_name(mocker):
    # Mocking _RESERVED_NAMES to ensure test isolation
    mocker.patch('ansible.vars.reserved._RESERVED_NAMES', new=['ansible', 'vars', 'reserved'])

    # Test with a reserved name
    assert is_reserved_name('ansible') == True
    assert is_reserved_name('vars') == True
    assert is_reserved_name('reserved') == True

    # Test with a non-reserved name
    assert is_reserved_name('not_reserved') == False
