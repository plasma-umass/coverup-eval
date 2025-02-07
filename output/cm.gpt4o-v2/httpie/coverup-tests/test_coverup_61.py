# file: httpie/config.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
from pathlib import Path
from httpie.config import BaseConfigDict

def test_base_config_dict_init():
    # Create a Path object
    test_path = Path('/tmp/test_config')

    # Initialize BaseConfigDict with the test path
    config_dict = BaseConfigDict(test_path)

    # Assert that the path attribute is set correctly
    assert config_dict.path == test_path

    # Assert that the object is an instance of BaseConfigDict and dict
    assert isinstance(config_dict, BaseConfigDict)
    assert isinstance(config_dict, dict)
