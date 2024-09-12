# file: lib/ansible/module_utils/common/validation.py:538-540
# asked: {"lines": [538, 540], "branches": []}
# gained: {"lines": [538, 540], "branches": []}

import pytest

from ansible.module_utils.common.validation import check_type_raw

def test_check_type_raw():
    # Test with an integer
    assert check_type_raw(10) == 10

    # Test with a string
    assert check_type_raw("test") == "test"

    # Test with a list
    assert check_type_raw([1, 2, 3]) == [1, 2, 3]

    # Test with a dictionary
    assert check_type_raw({"key": "value"}) == {"key": "value"}

    # Test with None
    assert check_type_raw(None) == None

    # Test with a boolean
    assert check_type_raw(True) == True
