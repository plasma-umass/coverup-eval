# file: typesystem/base.py:219-254
# asked: {"lines": [219, 220, 227, 228, 239, 240, 241, 243, 244, 245, 247, 248, 250, 251, 252, 253, 254], "branches": [[252, 253], [252, 254]]}
# gained: {"lines": [219, 220, 227, 228, 239, 240, 241, 243, 244, 245, 247, 248, 250, 251, 252, 253, 254], "branches": [[252, 253], [252, 254]]}

import pytest
from typesystem.base import ValidationResult, ValidationError

class MockValidationError(ValidationError):
    def __init__(self, message):
        self._messages = [message]

def test_validation_result_with_value():
    result = ValidationResult(value="valid_data")
    assert result.value == "valid_data"
    assert result.error is None
    assert bool(result) is True
    assert repr(result) == "ValidationResult(value='valid_data')"

def test_validation_result_with_error():
    error = MockValidationError("error_message")
    result = ValidationResult(error=error)
    assert result.value is None
    assert result.error == error
    assert bool(result) is False
    assert repr(result) == "ValidationResult(error=MockValidationError(['error_message']))"

def test_validation_result_assertion():
    with pytest.raises(AssertionError):
        ValidationResult(value="valid_data", error=MockValidationError("error_message"))

def test_validation_result_iteration():
    result = ValidationResult(value="valid_data")
    value, error = result
    assert value == "valid_data"
    assert error is None

    error_instance = MockValidationError("error_message")
    result = ValidationResult(error=error_instance)
    value, error = result
    assert value is None
    assert error == error_instance
