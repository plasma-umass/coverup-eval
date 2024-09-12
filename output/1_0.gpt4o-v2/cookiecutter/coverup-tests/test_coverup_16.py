# file: cookiecutter/exceptions.py:93-99
# asked: {"lines": [93, 94], "branches": []}
# gained: {"lines": [93, 94], "branches": []}

import pytest
from cookiecutter.exceptions import InvalidModeException, CookiecutterException

def test_invalid_mode_exception():
    with pytest.raises(InvalidModeException) as exc_info:
        raise InvalidModeException("Incompatible modes: no_input and replay both set to True")
    
    assert str(exc_info.value) == "Incompatible modes: no_input and replay both set to True"
    assert isinstance(exc_info.value, CookiecutterException)
    assert isinstance(exc_info.value, InvalidModeException)
