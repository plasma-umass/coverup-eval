# file lib/ansible/module_utils/common/validation.py:509-527
# lines [509, 518, 519, 521, 522, 523, 524, 525, 527]
# branches ['518->519', '518->521', '521->522', '521->527']

import pytest
from ansible.module_utils.common.validation import check_type_float

def test_check_type_float():
    # Test with a float value
    assert check_type_float(3.14) == 3.14

    # Test with an integer value
    assert check_type_float(10) == 10.0

    # Test with a string that can be converted to float
    assert check_type_float("2.718") == 2.718

    # Test with bytes that can be converted to float
    assert check_type_float(b"1.618") == 1.618

    # Test with a string that cannot be converted to float
    with pytest.raises(TypeError, match="cannot be converted to a float"):
        check_type_float("not_a_float")

    # Test with a type that cannot be converted to float
    with pytest.raises(TypeError, match="cannot be converted to a float"):
        check_type_float([1, 2, 3])
