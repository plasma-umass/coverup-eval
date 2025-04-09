# file dataclasses_json/undefined.py:269-273
# lines [269, 270, 273]
# branches []

import pytest
from dataclasses_json.undefined import UndefinedParameterError
from marshmallow import ValidationError

def test_UndefinedParameterError_is_instance_of_ValidationError():
    with pytest.raises(UndefinedParameterError) as exc_info:
        raise UndefinedParameterError("Undefined parameter encountered")
    
    assert isinstance(exc_info.value, ValidationError)
    assert str(exc_info.value) == "Undefined parameter encountered"
