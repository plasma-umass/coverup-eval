# file lib/ansible/module_utils/common/validation.py:538-540
# lines [538, 540]
# branches []

import pytest
from ansible.module_utils.common.validation import check_type_raw

def test_check_type_raw():
    # Test with an integer
    value = 42
    assert check_type_raw(value) == value

    # Test with a string
    value = "test"
    assert check_type_raw(value) == value

    # Test with a list
    value = [1, 2, 3]
    assert check_type_raw(value) == value

    # Test with a dictionary
    value = {"key": "value"}
    assert check_type_raw(value) == value

    # Test with a None value
    value = None
    assert check_type_raw(value) == value

    # Test with a boolean
    value = True
    assert check_type_raw(value) == value
