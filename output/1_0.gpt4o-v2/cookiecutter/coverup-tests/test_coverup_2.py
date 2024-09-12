# file: cookiecutter/exceptions.py:43-49
# asked: {"lines": [43, 44], "branches": []}
# gained: {"lines": [43, 44], "branches": []}

import pytest
from cookiecutter.exceptions import ConfigDoesNotExistException

def test_config_does_not_exist_exception():
    with pytest.raises(ConfigDoesNotExistException) as exc_info:
        raise ConfigDoesNotExistException("Config file not found.")
    
    assert str(exc_info.value) == "Config file not found."
