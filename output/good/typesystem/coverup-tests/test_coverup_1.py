# file typesystem/base.py:219-254
# lines [219, 220, 227, 228, 239, 240, 241, 243, 244, 245, 247, 248, 250, 251, 252, 253, 254]
# branches ['252->253', '252->254']

import pytest
from typesystem.base import ValidationResult
from typesystem import ValidationError

def test_validation_result():
    # Test with value
    result_with_value = ValidationResult(value="valid_data")
    value, error = result_with_value
    assert value == "valid_data"
    assert error is None
    assert bool(result_with_value) is True
    assert repr(result_with_value) == "ValidationResult(value='valid_data')"

    # Test with error
    validation_error = ValidationError(text="error_message")
    result_with_error = ValidationResult(error=validation_error)
    value, error = result_with_error
    assert value is None
    assert error == validation_error
    assert bool(result_with_error) is False
    assert repr(result_with_error) == f"ValidationResult(error={validation_error!r})"

    # Test assertion for both value and error
    with pytest.raises(AssertionError):
        ValidationResult(value="valid_data", error=validation_error)
