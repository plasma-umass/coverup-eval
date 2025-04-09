# file: dataclasses_json/undefined.py:269-273
# asked: {"lines": [269, 270, 273], "branches": []}
# gained: {"lines": [269, 270, 273], "branches": []}

import pytest
from marshmallow import ValidationError
from dataclasses_json.undefined import UndefinedParameterError

def test_UndefinedParameterError_inheritance():
    with pytest.raises(UndefinedParameterError) as exc_info:
        raise UndefinedParameterError("Test error message")
    
    assert isinstance(exc_info.value, UndefinedParameterError)
    assert isinstance(exc_info.value, ValidationError)
    assert str(exc_info.value) == "Test error message"
