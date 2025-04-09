# file httpie/config.py:70-72
# lines [70, 71, 72]
# branches []

import pytest
from httpie.config import BaseConfigDict
from pathlib import Path
import os

def test_base_config_dict_initialization(tmp_path):
    # Create a temporary file to represent the config path
    temp_config_path = tmp_path / "config.json"
    temp_config_path.touch()

    # Initialize the BaseConfigDict with the temporary path
    config_dict = BaseConfigDict(path=temp_config_path)

    # Assert that the path attribute is set correctly
    assert config_dict.path == temp_config_path

    # Clean up is handled by pytest's tmp_path fixture
