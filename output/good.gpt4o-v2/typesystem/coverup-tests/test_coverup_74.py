# file: typesystem/base.py:213-216
# asked: {"lines": [213, 214], "branches": []}
# gained: {"lines": [213, 214], "branches": []}

import pytest
from typesystem.base import ValidationError, BaseError, Message, Position

def test_validation_error_inheritance():
    # Ensure ValidationError is a subclass of BaseError
    assert issubclass(ValidationError, BaseError)

def test_validation_error_instance():
    # Ensure an instance of ValidationError can be created with the correct parameters
    error = ValidationError(text="An error occurred")
    assert isinstance(error, ValidationError)
    assert str(error) == "An error occurred"
