# file: cookiecutter/exceptions.py:4-9
# asked: {"lines": [4, 5], "branches": []}
# gained: {"lines": [4, 5], "branches": []}

import pytest
from cookiecutter.exceptions import CookiecutterException

def test_cookiecutter_exception():
    with pytest.raises(CookiecutterException):
        raise CookiecutterException("This is a test exception")

    # Ensure the exception message is correct
    try:
        raise CookiecutterException("This is a test exception")
    except CookiecutterException as e:
        assert str(e) == "This is a test exception"
