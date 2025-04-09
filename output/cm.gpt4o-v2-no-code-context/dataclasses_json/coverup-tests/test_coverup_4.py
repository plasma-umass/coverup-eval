# file: dataclasses_json/undefined.py:269-273
# asked: {"lines": [269, 270, 273], "branches": []}
# gained: {"lines": [269, 270, 273], "branches": []}

import pytest
from dataclasses_json.undefined import UndefinedParameterError
from marshmallow import ValidationError

def test_UndefinedParameterError_is_subclass_of_ValidationError():
    assert issubclass(UndefinedParameterError, ValidationError)

def test_UndefinedParameterError_instance():
    error_instance = UndefinedParameterError("Undefined parameter error occurred")
    assert isinstance(error_instance, UndefinedParameterError)
    assert str(error_instance) == "Undefined parameter error occurred"
