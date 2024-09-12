# file: lib/ansible/vars/reserved.py:82-83
# asked: {"lines": [82, 83], "branches": []}
# gained: {"lines": [82, 83], "branches": []}

import pytest
from ansible.vars.reserved import is_reserved_name, _RESERVED_NAMES

def test_is_reserved_name():
    # Test with a reserved name
    reserved_name = next(iter(_RESERVED_NAMES))
    assert is_reserved_name(reserved_name) == True

    # Test with a non-reserved name
    non_reserved_name = "non_reserved_name"
    assert is_reserved_name(non_reserved_name) == False
