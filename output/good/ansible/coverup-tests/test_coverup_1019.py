# file lib/ansible/vars/reserved.py:82-83
# lines [82, 83]
# branches []

import pytest
from ansible.vars.reserved import is_reserved_name, _RESERVED_NAMES

def test_is_reserved_name():
    # Test with a name that is known to be reserved
    reserved_name = next(iter(_RESERVED_NAMES))
    assert is_reserved_name(reserved_name) is True

    # Test with a name that is not reserved
    non_reserved_name = "not_reserved"
    assert is_reserved_name(non_reserved_name) is False

    # Clean up is not necessary as the test does not modify any state
