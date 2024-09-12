# file: httpie/config.py:131-144
# asked: {"lines": [131, 132, 133, 134, 137, 138, 139, 140, 142, 143, 144], "branches": []}
# gained: {"lines": [131, 132, 133, 134, 137, 138, 139, 140, 142, 143, 144], "branches": []}

import pytest
from pathlib import Path
from httpie.config import Config, DEFAULT_CONFIG_DIR

class MockBaseConfigDict(dict):
    def __init__(self, path: Path):
        super().__init__()
        self.path = path

@pytest.fixture
def mock_base_config_dict(monkeypatch):
    monkeypatch.setattr('httpie.config.BaseConfigDict', MockBaseConfigDict)

def test_config_initialization(mock_base_config_dict):
    config = Config(directory=DEFAULT_CONFIG_DIR)
    assert config.directory == Path(DEFAULT_CONFIG_DIR)
    assert config['default_options'] == []

def test_config_default_options_property(mock_base_config_dict):
    config = Config(directory=DEFAULT_CONFIG_DIR)
    assert config.default_options == []
