# file pymonet/validation.py:21-31
# lines [21, 22, 31]
# branches []

import pytest
from pymonet.validation import Validation

def test_validation_success():
    # Test with no value
    validation = Validation.success()
    assert validation.value is None
    assert validation.errors == []

    # Test with a specific value
    value = "test_value"
    validation = Validation.success(value)
    assert validation.value == value
    assert validation.errors == []

    # Test with a complex value
    value = {"key": "value"}
    validation = Validation.success(value)
    assert validation.value == value
    assert validation.errors == []
