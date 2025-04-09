# file: pymonet/validation.py:4-6
# asked: {"lines": [4, 5, 6], "branches": []}
# gained: {"lines": [4, 5, 6], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_initialization():
    value = "test_value"
    errors = ["error1", "error2"]
    
    validation = Validation(value, errors)
    
    assert validation.value == value
    assert validation.errors == errors
