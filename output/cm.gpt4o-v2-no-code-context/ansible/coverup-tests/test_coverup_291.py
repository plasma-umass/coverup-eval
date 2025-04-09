# file: lib/ansible/module_utils/common/validation.py:509-527
# asked: {"lines": [509, 518, 519, 521, 522, 523, 524, 525, 527], "branches": [[518, 519], [518, 521], [521, 522], [521, 527]]}
# gained: {"lines": [509, 518, 519, 521, 522, 523, 524, 525, 527], "branches": [[518, 519], [518, 521], [521, 522], [521, 527]]}

import pytest
from ansible.module_utils.common.validation import check_type_float

def test_check_type_float_with_float():
    assert check_type_float(3.14) == 3.14

def test_check_type_float_with_int():
    assert check_type_float(10) == 10.0

def test_check_type_float_with_str():
    assert check_type_float("2.718") == 2.718

def test_check_type_float_with_bytes():
    assert check_type_float(b"1.618") == 1.618

def test_check_type_float_with_invalid_str():
    with pytest.raises(TypeError):
        check_type_float("not_a_float")

def test_check_type_float_with_invalid_type():
    with pytest.raises(TypeError):
        check_type_float([1, 2, 3])
