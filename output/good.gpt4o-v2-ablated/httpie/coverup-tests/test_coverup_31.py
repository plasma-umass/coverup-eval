# file: httpie/config.py:61-62
# asked: {"lines": [61, 62], "branches": []}
# gained: {"lines": [61, 62], "branches": []}

import pytest
from httpie.config import ConfigFileError

def test_config_file_error_inheritance():
    assert issubclass(ConfigFileError, Exception)

def test_config_file_error_instance():
    error_message = "This is a config file error"
    error_instance = ConfigFileError(error_message)
    assert isinstance(error_instance, ConfigFileError)
    assert str(error_instance) == error_message
