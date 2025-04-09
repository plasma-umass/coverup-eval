# file: dataclasses_json/undefined.py:269-273
# asked: {"lines": [269, 270, 273], "branches": []}
# gained: {"lines": [269, 270, 273], "branches": []}

import pytest
from dataclasses_json.undefined import UndefinedParameterError
from marshmallow import ValidationError

def test_UndefinedParameterError_is_instance_of_ValidationError():
    error = UndefinedParameterError("An error occurred")
    assert isinstance(error, ValidationError)
    assert str(error) == "An error occurred"
