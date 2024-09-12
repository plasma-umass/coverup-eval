# file: lib/ansible/module_utils/common/validation.py:487-506
# asked: {"lines": [487, 497, 498, 500, 501, 502, 503, 504, 506], "branches": [[497, 498], [497, 500], [500, 501], [500, 506]]}
# gained: {"lines": [487, 497, 498, 500, 501, 502, 503, 504, 506], "branches": [[497, 498], [497, 500], [500, 501], [500, 506]]}

import pytest
from ansible.module_utils.common.validation import check_type_int

def test_check_type_int_with_int():
    assert check_type_int(5) == 5

def test_check_type_int_with_valid_string():
    assert check_type_int("10") == 10

def test_check_type_int_with_invalid_string():
    with pytest.raises(TypeError, match=r"<class 'str'> cannot be converted to an int"):
        check_type_int("invalid")

def test_check_type_int_with_float():
    with pytest.raises(TypeError, match=r"<class 'float'> cannot be converted to an int"):
        check_type_int(10.5)

def test_check_type_int_with_none():
    with pytest.raises(TypeError, match=r"<class 'NoneType'> cannot be converted to an int"):
        check_type_int(None)
