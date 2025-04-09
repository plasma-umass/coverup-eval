# file: dataclasses_json/undefined.py:269-273
# asked: {"lines": [269, 270, 273], "branches": []}
# gained: {"lines": [269, 270, 273], "branches": []}

import pytest
from marshmallow import ValidationError
from dataclasses_json.undefined import UndefinedParameterError

def test_UndefinedParameterError_inheritance():
    # Test that UndefinedParameterError is a subclass of ValidationError
    assert issubclass(UndefinedParameterError, ValidationError)

def test_UndefinedParameterError_instance():
    # Test that an instance of UndefinedParameterError can be created
    error = UndefinedParameterError("An error occurred")
    assert isinstance(error, UndefinedParameterError)
    assert str(error) == "An error occurred"

def test_UndefinedParameterError_with_kwargs():
    # Test that UndefinedParameterError can be instantiated with additional keyword arguments
    error = UndefinedParameterError("An error occurred", field_name="test_field", data={"key": "value"})
    assert error.field_name == "test_field"
    assert error.data == {"key": "value"}
