# file dataclasses_json/undefined.py:269-273
# lines [269, 270, 273]
# branches []

import pytest
from dataclasses_json.undefined import UndefinedParameterError

def test_undefined_parameter_error():
    with pytest.raises(UndefinedParameterError) as exc_info:
        raise UndefinedParameterError("Test error message")
    assert str(exc_info.value) == "Test error message"
