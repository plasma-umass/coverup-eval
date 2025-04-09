# file lib/ansible/module_utils/common/validation.py:509-527
# lines [509, 518, 519, 521, 522, 523, 524, 525, 527]
# branches ['518->519', '518->521', '521->522', '521->527']

import pytest
from ansible.module_utils.common.validation import check_type_float

def test_check_type_float_with_float():
    assert check_type_float(1.0) == 1.0

def test_check_type_float_with_int():
    assert check_type_float(1) == 1.0

def test_check_type_float_with_str():
    assert check_type_float("1.23") == 1.23

def test_check_type_float_with_bytes():
    assert check_type_float(b"1.23") == 1.23

def test_check_type_float_with_invalid_str():
    with pytest.raises(TypeError):
        check_type_float("invalid")

def test_check_type_float_with_invalid_type():
    with pytest.raises(TypeError):
        check_type_float([])

# Assuming binary_type and text_type are defined in the module or imported from six
# If not, they need to be defined or imported for the tests to work
