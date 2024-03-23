# file cookiecutter/exceptions.py:4-9
# lines [4, 5]
# branches []

import pytest
from cookiecutter.exceptions import CookiecutterException

def test_cookiecutter_exception():
    with pytest.raises(CookiecutterException) as exc_info:
        raise CookiecutterException("An error occurred")

    assert str(exc_info.value) == "An error occurred"
