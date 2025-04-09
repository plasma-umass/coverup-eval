# file sanic/exceptions.py:230-231
# lines [230, 231]
# branches []

import pytest
from sanic.exceptions import InvalidSignal

def test_invalid_signal_exception():
    with pytest.raises(InvalidSignal) as exc_info:
        raise InvalidSignal("Invalid signal error")

    assert str(exc_info.value) == "Invalid signal error"
