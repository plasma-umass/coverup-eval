# file cookiecutter/exceptions.py:52-58
# lines [52, 53]
# branches []

import pytest
from cookiecutter.exceptions import InvalidConfiguration

def test_invalid_configuration_exception():
    with pytest.raises(InvalidConfiguration) as exc_info:
        raise InvalidConfiguration("Invalid configuration")

    assert str(exc_info.value) == "Invalid configuration"
