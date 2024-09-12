# file: cookiecutter/exceptions.py:52-58
# asked: {"lines": [52, 53], "branches": []}
# gained: {"lines": [52, 53], "branches": []}

import pytest
from cookiecutter.exceptions import InvalidConfiguration, CookiecutterException

def test_invalid_configuration():
    with pytest.raises(InvalidConfiguration) as exc_info:
        raise InvalidConfiguration("Invalid configuration file")
    assert str(exc_info.value) == "Invalid configuration file"
    assert isinstance(exc_info.value, CookiecutterException)
