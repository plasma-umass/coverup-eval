# file: lib/ansible/module_utils/common/validation.py:487-506
# asked: {"lines": [487, 497, 498, 500, 501, 502, 503, 504, 506], "branches": [[497, 498], [497, 500], [500, 501], [500, 506]]}
# gained: {"lines": [487, 497, 498, 500, 501, 502, 503, 504, 506], "branches": [[497, 498], [497, 500], [500, 501], [500, 506]]}

import pytest
from ansible.module_utils.common.validation import check_type_int
from ansible.module_utils.six import integer_types, string_types

def test_check_type_int_with_integer():
    assert check_type_int(10) == 10

def test_check_type_int_with_string_integer():
    assert check_type_int("10") == 10

def test_check_type_int_with_invalid_string():
    with pytest.raises(TypeError):
        check_type_int("invalid")

def test_check_type_int_with_float():
    with pytest.raises(TypeError):
        check_type_int(10.5)

def test_check_type_int_with_none():
    with pytest.raises(TypeError):
        check_type_int(None)
