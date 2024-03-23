# file httpie/config.py:131-144
# lines [131, 132, 133, 134, 137, 138, 139, 140, 142, 143, 144]
# branches []

import pytest
from pathlib import Path
from httpie.config import Config

def test_config_default_options(tmp_path):
    # Create a Config instance with the temporary directory
    config = Config(directory=tmp_path)

    # Assert that the directory is the temporary directory
    assert config.directory == tmp_path

    # Assert that the default options are an empty list
    assert config.default_options == []

    # Assert that the config file path is correct
    assert config.path == tmp_path / Config.FILENAME

    # No need to mock or cleanup since we're using the tmp_path fixture
