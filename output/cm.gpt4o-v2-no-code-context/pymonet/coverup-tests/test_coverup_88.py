# file: pymonet/either.py:200-209
# asked: {"lines": [200, 207, 209], "branches": []}
# gained: {"lines": [200, 207, 209], "branches": []}

import pytest
from pymonet.either import Right
from pymonet.validation import Validation

def test_right_to_validation():
    right_value = Right(42)
    validation = right_value.to_validation()
    
    assert isinstance(validation, Validation)
    assert validation.is_success()
    assert validation.value == 42
