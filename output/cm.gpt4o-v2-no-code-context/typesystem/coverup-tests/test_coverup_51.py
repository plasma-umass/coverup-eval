# file: typesystem/base.py:213-216
# asked: {"lines": [213, 214], "branches": []}
# gained: {"lines": [213, 214], "branches": []}

import pytest
from typesystem.base import BaseError

def test_validation_error_inheritance():
    class ValidationError(BaseError):
        """
        Raised by `.validate()` or returned by `.validate_or_error()`.
        """
        pass

    # Ensure that ValidationError is a subclass of BaseError
    assert issubclass(ValidationError, BaseError)

    # Ensure that an instance of ValidationError can be created with required parameters
    error_instance = ValidationError(text="Test error")
    assert isinstance(error_instance, ValidationError)
    assert str(error_instance) == "Test error"
