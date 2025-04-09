# file sanic/exceptions.py:230-231
# lines [230, 231]
# branches []

import pytest
from sanic.exceptions import SanicException

class InvalidSignal(SanicException):
    pass

def test_invalid_signal_exception():
    with pytest.raises(InvalidSignal) as exc_info:
        raise InvalidSignal("This is an invalid signal error")
    
    assert str(exc_info.value) == "This is an invalid signal error"
