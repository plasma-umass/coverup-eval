# file pymonet/either.py:200-209
# lines [200, 207, 209]
# branches []

import pytest
from pymonet.either import Right
from pymonet.validation import Validation

def test_right_to_validation():
    # Create a Right instance
    right_value = Right(10)
    
    # Convert to Validation
    validation_result = right_value.to_validation()
    
    # Assert that the result is a Validation instance
    assert isinstance(validation_result, Validation)
    
    # Assert that the result is a success
    assert validation_result.is_success() is True
    
    # Assert that the value is the same as the original Right value
    assert validation_result.value == right_value.value
