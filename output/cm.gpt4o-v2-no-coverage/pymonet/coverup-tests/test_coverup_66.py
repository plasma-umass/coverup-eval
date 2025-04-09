# file: pymonet/either.py:200-209
# asked: {"lines": [200, 207, 209], "branches": []}
# gained: {"lines": [200, 207, 209], "branches": []}

import pytest
from pymonet.either import Right
from pymonet.validation import Validation

def test_right_to_validation():
    # Create an instance of Right with a sample value
    value = 42
    right_instance = Right(value)
    
    # Convert to Validation
    validation_instance = right_instance.to_validation()
    
    # Assert that the validation_instance is a successful Validation with the correct value
    assert isinstance(validation_instance, Validation)
    assert validation_instance.value == value
    assert validation_instance.errors == []

    # Clean up
    del right_instance
    del validation_instance
