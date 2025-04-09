# file: pymonet/either.py:138-147
# asked: {"lines": [138, 145, 147], "branches": []}
# gained: {"lines": [138, 145, 147], "branches": []}

import pytest
from pymonet.either import Left
from pymonet.validation import Validation

def test_left_to_validation():
    # Create an instance of Left with a specific value
    left_instance = Left("error_value")
    
    # Convert the Left instance to a Validation instance
    validation_instance = left_instance.to_validation()
    
    # Assert that the validation_instance is a failed Validation with the correct error value
    assert validation_instance.is_fail()
    assert validation_instance.errors == ["error_value"]
