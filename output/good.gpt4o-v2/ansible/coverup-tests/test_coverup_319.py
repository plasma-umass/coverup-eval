# file: lib/ansible/module_utils/common/validation.py:509-527
# asked: {"lines": [509, 518, 519, 521, 522, 523, 524, 525, 527], "branches": [[518, 519], [518, 521], [521, 522], [521, 527]]}
# gained: {"lines": [509, 518, 519, 521, 522, 523, 524, 525, 527], "branches": [[518, 519], [518, 521], [521, 522], [521, 527]]}

import pytest
from ansible.module_utils.common.validation import check_type_float
from ansible.module_utils.six import binary_type, text_type

def test_check_type_float_with_float():
    assert check_type_float(1.23) == 1.23

def test_check_type_float_with_int():
    assert check_type_float(123) == 123.0

def test_check_type_float_with_text_type():
    assert check_type_float("123.45") == 123.45

def test_check_type_float_with_binary_type():
    assert check_type_float(b"123.45") == 123.45

def test_check_type_float_with_invalid_string():
    with pytest.raises(TypeError):
        check_type_float("abc")

def test_check_type_float_with_invalid_type():
    with pytest.raises(TypeError):
        check_type_float([1, 2, 3])
