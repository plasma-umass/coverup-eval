# file: httpie/config.py:131-144
# asked: {"lines": [144], "branches": []}
# gained: {"lines": [144], "branches": []}

import pytest
from pathlib import Path
from httpie.config import Config

@pytest.fixture
def temp_config_dir(tmp_path):
    return tmp_path / "config"

def test_default_options_property(temp_config_dir, monkeypatch):
    # Ensure the directory exists
    temp_config_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize Config with the temporary directory
    config = Config(directory=temp_config_dir)
    
    # Assert that the default_options property returns the expected default value
    assert config.default_options == []

    # Clean up by removing the created config file
    config_path = temp_config_dir / Config.FILENAME
    if config_path.exists():
        config_path.unlink()
