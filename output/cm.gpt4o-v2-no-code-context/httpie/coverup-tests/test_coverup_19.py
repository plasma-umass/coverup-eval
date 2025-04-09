# file: httpie/config.py:131-144
# asked: {"lines": [131, 132, 133, 134, 137, 138, 139, 140, 142, 143, 144], "branches": []}
# gained: {"lines": [131, 132, 133, 134, 137, 138, 139, 140, 142, 143, 144], "branches": []}

import pytest
from pathlib import Path
from httpie.config import Config, DEFAULT_CONFIG_DIR

@pytest.fixture
def temp_config_dir(tmp_path, monkeypatch):
    temp_dir = tmp_path / "config"
    temp_dir.mkdir()
    monkeypatch.setattr('httpie.config.DEFAULT_CONFIG_DIR', str(temp_dir))
    yield temp_dir

def test_config_initialization(temp_config_dir):
    config = Config(directory=temp_config_dir)
    assert config.directory == temp_config_dir
    assert config['default_options'] == []

def test_config_default_options_property(temp_config_dir):
    config = Config(directory=temp_config_dir)
    assert config.default_options == []

def test_config_update_defaults(temp_config_dir):
    config = Config(directory=temp_config_dir)
    new_defaults = {'default_options': ['--verbose']}
    config.update(new_defaults)
    assert config['default_options'] == ['--verbose']
    assert config.default_options == ['--verbose']
