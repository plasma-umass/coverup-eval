# file: httpie/config.py:131-144
# asked: {"lines": [131, 132, 133, 134, 137, 138, 139, 140, 142, 143, 144], "branches": []}
# gained: {"lines": [131, 132, 133, 134, 137, 138, 139, 140, 142, 143, 144], "branches": []}

import pytest
from pathlib import Path
from httpie.config import Config

@pytest.fixture
def temp_config_dir(tmp_path):
    return tmp_path / "config"

def test_config_initialization(temp_config_dir):
    # Ensure the directory exists
    temp_config_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize Config with the temporary directory
    config = Config(directory=temp_config_dir)
    
    # Assertions to verify initialization
    assert config.directory == temp_config_dir
    assert config['default_options'] == []

def test_config_default_options(temp_config_dir):
    # Ensure the directory exists
    temp_config_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize Config with the temporary directory
    config = Config(directory=temp_config_dir)
    
    # Assertions to verify default options property
    assert config.default_options == []
