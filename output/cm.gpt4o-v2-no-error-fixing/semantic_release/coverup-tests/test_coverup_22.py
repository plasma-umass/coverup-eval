# file: semantic_release/settings.py:20-32
# asked: {"lines": [20, 21, 22, 23, 24, 26, 28, 29, 32], "branches": []}
# gained: {"lines": [20, 21, 22, 23, 24, 26, 28, 29, 32], "branches": []}

import os
import pytest
from unittest.mock import patch, mock_open
from collections import UserDict
from semantic_release.settings import _config

@pytest.fixture
def mock_getcwd(monkeypatch):
    monkeypatch.setattr(os, 'getcwd', lambda: '/mocked/path')

@pytest.fixture
def mock_isfile(monkeypatch):
    monkeypatch.setattr(os.path, 'isfile', lambda path: True)

@pytest.fixture
def mock_open_ini(monkeypatch):
    ini_content = """
    [semantic_release]
    changelog_capitalize = true
    """
    monkeypatch.setattr('builtins.open', mock_open(read_data=ini_content))

@pytest.fixture
def mock_open_toml(monkeypatch):
    toml_content = """
    [tool.semantic_release]
    changelog_capitalize = true
    """
    monkeypatch.setattr('builtins.open', mock_open(read_data=toml_content))

def test_config(mock_getcwd, mock_isfile, mock_open_ini, mock_open_toml):
    with patch('semantic_release.settings._config_from_ini', return_value={'changelog_capitalize': True}) as mock_ini, \
         patch('semantic_release.settings._config_from_pyproject', return_value={'changelog_capitalize': True}) as mock_toml:
        config = _config()
        assert isinstance(config, UserDict)
        assert config['changelog_capitalize'] == True
        mock_ini.assert_called_once()
        mock_toml.assert_called_once()
