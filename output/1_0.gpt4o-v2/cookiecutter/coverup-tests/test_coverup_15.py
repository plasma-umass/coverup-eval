# file: cookiecutter/exceptions.py:133-138
# asked: {"lines": [133, 134], "branches": []}
# gained: {"lines": [133, 134], "branches": []}

import pytest
from cookiecutter.exceptions import UnknownExtension, CookiecutterException

def test_unknown_extension():
    with pytest.raises(UnknownExtension) as exc_info:
        raise UnknownExtension("Unable to import extension")
    assert str(exc_info.value) == "Unable to import extension"
    assert isinstance(exc_info.value, CookiecutterException)
