# file lib/ansible/module_utils/common/validation.py:414-465
# lines [434, 442, 443, 445, 447, 449]
# branches ['432->434', '441->442', '444->445', '446->447', '448->449', '459->461']

import pytest
from ansible.module_utils.common.validation import check_type_dict

def test_check_type_dict():
    # Test case to cover line 434
    assert check_type_dict('{"key": "value"}') == {"key": "value"}

    # Test case to cover lines 442-443, 445, 447, 449
    assert check_type_dict('key1=value1, key2="value2", key3=\'value3\'') == {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
    }

    # Test case to cover branch 459->461
    assert check_type_dict('key1=value1, key2=value2') == {
        "key1": "value1",
        "key2": "value2",
    }

    # Test case to cover TypeError for invalid string
    with pytest.raises(TypeError, match="dictionary requested, could not parse JSON or key=value"):
        check_type_dict("invalid_string")

    # Test case to cover TypeError for non-dict, non-string input
    with pytest.raises(TypeError, match="cannot be converted to a dict"):
        check_type_dict(12345)
