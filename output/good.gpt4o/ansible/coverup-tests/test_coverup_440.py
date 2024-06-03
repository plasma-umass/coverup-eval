# file lib/ansible/module_utils/common/validation.py:468-484
# lines [468, 478, 479, 481, 482, 484]
# branches ['478->479', '478->481', '481->482', '481->484']

import pytest
from ansible.module_utils.common.validation import check_type_bool
from ansible.module_utils._text import to_text

def test_check_type_bool():
    # Test with a boolean value
    assert check_type_bool(True) is True
    assert check_type_bool(False) is False

    # Test with string values
    assert check_type_bool('1') is True
    assert check_type_bool('0') is False
    assert check_type_bool('true') is True
    assert check_type_bool('false') is False
    assert check_type_bool('yes') is True
    assert check_type_bool('no') is False
    assert check_type_bool('on') is True
    assert check_type_bool('off') is False

    # Test with integer values
    assert check_type_bool(1) is True
    assert check_type_bool(0) is False

    # Test with float values
    assert check_type_bool(1.0) is True
    assert check_type_bool(0.0) is False

    # Test with invalid type
    with pytest.raises(TypeError):
        check_type_bool(['invalid'])

    with pytest.raises(TypeError):
        check_type_bool({'invalid': 'dict'})

    with pytest.raises(TypeError):
        check_type_bool(None)
