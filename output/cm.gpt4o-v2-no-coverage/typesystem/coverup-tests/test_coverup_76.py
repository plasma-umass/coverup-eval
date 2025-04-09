# file: typesystem/base.py:187-188
# asked: {"lines": [187, 188], "branches": []}
# gained: {"lines": [187, 188], "branches": []}

import pytest
from typesystem.base import BaseError, ValidationError
from typesystem.base import Message

def test_base_error_eq_with_validation_error():
    message1 = Message(text="Error 1")
    message2 = Message(text="Error 2")
    error1 = ValidationError(messages=[message1])
    error2 = ValidationError(messages=[message1])
    error3 = ValidationError(messages=[message2])
    
    assert error1 == error2
    assert error1 != error3

def test_base_error_eq_with_non_validation_error():
    message = Message(text="Error")
    error = ValidationError(messages=[message])
    non_error = "Not an error"
    
    assert error != non_error
