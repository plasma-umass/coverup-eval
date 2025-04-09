# file: lib/ansible/module_utils/common/validation.py:468-484
# asked: {"lines": [468, 478, 479, 481, 482, 484], "branches": [[478, 479], [478, 481], [481, 482], [481, 484]]}
# gained: {"lines": [468, 478, 479, 481, 482, 484], "branches": [[478, 479], [478, 481], [481, 482], [481, 484]]}

import pytest
from ansible.module_utils.common.validation import check_type_bool
from ansible.module_utils.six import string_types

def test_check_type_bool_with_boolean():
    assert check_type_bool(True) is True
    assert check_type_bool(False) is False

def test_check_type_bool_with_string():
    assert check_type_bool('true') is True
    assert check_type_bool('false') is False
    assert check_type_bool('yes') is True
    assert check_type_bool('no') is False
    assert check_type_bool('1') is True
    assert check_type_bool('0') is False

def test_check_type_bool_with_int():
    assert check_type_bool(1) is True
    assert check_type_bool(0) is False

def test_check_type_bool_with_float():
    assert check_type_bool(1.0) is True
    assert check_type_bool(0.0) is False

def test_check_type_bool_with_invalid_type():
    with pytest.raises(TypeError):
        check_type_bool([])

def test_check_type_bool_with_invalid_string():
    with pytest.raises(TypeError):
        check_type_bool('invalid')

