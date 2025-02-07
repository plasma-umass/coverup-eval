# file: pymonet/validation.py:8-14
# asked: {"lines": [8, 12, 13, 14], "branches": []}
# gained: {"lines": [8, 12, 13, 14], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_equality():
    # Create two Validation objects with the same value and errors
    val1 = Validation(value=10, errors=['error1'])
    val2 = Validation(value=10, errors=['error1'])
    
    # Create a Validation object with different value
    val3 = Validation(value=20, errors=['error1'])
    
    # Create a Validation object with different errors
    val4 = Validation(value=10, errors=['error2'])
    
    # Create an object of a different type
    class NotValidation:
        def __init__(self, value, errors):
            self.value = value
            self.errors = errors
    
    not_val = NotValidation(value=10, errors=['error1'])
    
    # Test equality
    assert val1 == val2  # Should be True
    assert val1 != val3  # Should be True
    assert val1 != val4  # Should be True
    assert val1 != not_val  # Should be True
