# file: pymonet/either.py:200-209
# asked: {"lines": [200, 207, 209], "branches": []}
# gained: {"lines": [200, 207, 209], "branches": []}

import pytest
from pymonet.either import Either, Right
from pymonet.validation import Validation

def test_right_to_validation():
    # Create an instance of Right
    right_instance = Right("test_value")
    
    # Convert to Validation
    validation_instance = right_instance.to_validation()
    
    # Assert that the validation instance is a success and holds the correct value
    assert validation_instance.is_success()
    assert validation_instance.value == "test_value"
