# file lib/ansible/module_utils/common/validation.py:538-540
# lines [538, 540]
# branches []

import pytest
from ansible.module_utils.common.validation import check_type_raw

def test_check_type_raw():
    # Test with different types of values to ensure the function returns the raw value
    assert check_type_raw(10) == 10
    assert check_type_raw("string") == "string"
    assert check_type_raw([1, 2, 3]) == [1, 2, 3]
    assert check_type_raw({"key": "value"}) == {"key": "value"}
    assert check_type_raw(None) is None
