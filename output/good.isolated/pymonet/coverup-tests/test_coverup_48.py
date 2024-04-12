# file pymonet/validation.py:21-31
# lines [21, 22, 31]
# branches []

import pytest
from pymonet.validation import Validation

def test_validation_success():
    # Test the success class method
    value = "test_value"
    result = Validation.success(value)
    
    # Assertions to verify the postconditions
    assert result.value == value
    assert result.errors == []
    assert isinstance(result, Validation)
