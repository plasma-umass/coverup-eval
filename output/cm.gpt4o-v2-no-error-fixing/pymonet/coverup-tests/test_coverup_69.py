# file: pymonet/either.py:200-209
# asked: {"lines": [200, 207, 209], "branches": []}
# gained: {"lines": [200, 207, 209], "branches": []}

import pytest
from pymonet.either import Right
from pymonet.validation import Validation

def test_right_to_validation():
    # Create an instance of Right with a sample value
    right_instance = Right("test_value")
    
    # Convert the Right instance to a Validation instance
    validation_instance = right_instance.to_validation()
    
    # Assert that the validation_instance is an instance of Validation
    assert isinstance(validation_instance, Validation)
    
    # Assert that the value of the validation_instance is the same as the original Right instance
    assert validation_instance.value == "test_value"
    
    # Assert that the errors list in the validation_instance is empty
    assert validation_instance.errors == []
