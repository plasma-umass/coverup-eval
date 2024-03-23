# file lib/ansible/module_utils/common/validation.py:367-388
# lines [367, 381, 382, 384, 385, 387, 388]
# branches ['381->382', '381->384', '384->385', '384->387']

import pytest
from ansible.module_utils.common.validation import check_type_str
from ansible.module_utils._text import to_native

# Define the test function
def test_check_type_str():
    # Test with a string value
    assert check_type_str("test_string") == "test_string"
    
    # Test with a non-string value and allow_conversion=True
    assert check_type_str(123, allow_conversion=True) == "123"
    
    # Test with a non-string value and allow_conversion=False
    with pytest.raises(TypeError) as excinfo:
        check_type_str(123, allow_conversion=False)
    assert "'123' is not a string and conversion is not allowed" in str(excinfo.value)

# There is no need for cleanup after the test, as the function does not modify any global state.
