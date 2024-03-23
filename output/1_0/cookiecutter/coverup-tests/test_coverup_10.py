# file cookiecutter/exceptions.py:133-138
# lines [133, 134]
# branches []

import pytest
from cookiecutter.exceptions import UnknownExtension

def test_unknown_extension_exception():
    with pytest.raises(UnknownExtension) as exc_info:
        raise UnknownExtension("Test extension cannot be imported")

    assert str(exc_info.value) == "Test extension cannot be imported"
