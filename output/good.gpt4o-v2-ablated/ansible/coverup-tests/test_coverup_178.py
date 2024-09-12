# file: lib/ansible/module_utils/common/validation.py:468-484
# asked: {"lines": [468, 478, 479, 481, 482, 484], "branches": [[478, 479], [478, 481], [481, 482], [481, 484]]}
# gained: {"lines": [468, 478, 479, 481, 482, 484], "branches": [[478, 479], [478, 481], [481, 482], [481, 484]]}

import pytest
from ansible.module_utils.common.validation import check_type_bool
from ansible.module_utils._text import to_text

def boolean(value):
    """Convert a string, int, or float to a boolean."""
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        value = value.lower()
        if value in ('1', 'on', 't', 'true', 'y', 'yes'):
            return True
        if value in ('0', 'off', 'f', 'false', 'n', 'no'):
            return False
    raise TypeError('%s cannot be converted to a bool' % type(value))

def test_check_type_bool_with_bool():
    assert check_type_bool(True) is True
    assert check_type_bool(False) is False

def test_check_type_bool_with_string():
    assert check_type_bool('1') is True
    assert check_type_bool('on') is True
    assert check_type_bool('t') is True
    assert check_type_bool('true') is True
    assert check_type_bool('y') is True
    assert check_type_bool('yes') is True
    assert check_type_bool('0') is False
    assert check_type_bool('off') is False
    assert check_type_bool('f') is False
    assert check_type_bool('false') is False
    assert check_type_bool('n') is False
    assert check_type_bool('no') is False

def test_check_type_bool_with_int():
    assert check_type_bool(1) is True
    assert check_type_bool(0) is False

def test_check_type_bool_with_float():
    assert check_type_bool(1.0) is True
    assert check_type_bool(0.0) is False

def test_check_type_bool_with_invalid_type():
    with pytest.raises(TypeError):
        check_type_bool([1, 2, 3])
    with pytest.raises(TypeError):
        check_type_bool({'key': 'value'})
    with pytest.raises(TypeError):
        check_type_bool(None)
