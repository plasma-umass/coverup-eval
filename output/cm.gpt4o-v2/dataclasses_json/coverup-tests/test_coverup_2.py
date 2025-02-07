# file: dataclasses_json/undefined.py:269-273
# asked: {"lines": [269, 270, 273], "branches": []}
# gained: {"lines": [269, 270, 273], "branches": []}

import pytest
from marshmallow import ValidationError
from dataclasses_json.undefined import UndefinedParameterError

def test_UndefinedParameterError_is_instance_of_ValidationError():
    error_instance = UndefinedParameterError("Test error")
    assert isinstance(error_instance, ValidationError)
    assert str(error_instance) == "Test error"
