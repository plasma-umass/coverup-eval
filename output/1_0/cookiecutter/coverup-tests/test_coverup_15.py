# file cookiecutter/exceptions.py:43-49
# lines [43, 44]
# branches []

import pytest
from cookiecutter.exceptions import ConfigDoesNotExistException

def test_config_does_not_exist_exception():
    with pytest.raises(ConfigDoesNotExistException) as exc_info:
        raise ConfigDoesNotExistException("Test config does not exist.")

    assert str(exc_info.value) == "Test config does not exist."
