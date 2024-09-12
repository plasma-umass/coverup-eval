# file: semantic_release/settings.py:20-32
# asked: {"lines": [20, 21, 22, 23, 24, 26, 28, 29, 32], "branches": []}
# gained: {"lines": [20, 21, 22, 23, 24, 26, 28, 29, 32], "branches": []}

import os
import pytest
from unittest.mock import patch, mock_open
from collections import UserDict
from semantic_release.settings import _config, _config_from_ini, _config_from_pyproject

@pytest.fixture
def mock_getcwd(monkeypatch):
    monkeypatch.setattr(os, "getcwd", lambda: "/mocked/path")

@pytest.fixture
def mock_isfile(monkeypatch):
    monkeypatch.setattr(os.path, "isfile", lambda path: True)

@pytest.fixture
def mock_open_file(monkeypatch):
    mocked_open = mock_open(read_data='[tool.semantic_release]\nkey="value"')
    monkeypatch.setattr("builtins.open", mocked_open)
    return mocked_open

@pytest.fixture
def mock_configparser(monkeypatch):
    class MockConfigParser:
        def read(self, paths):
            pass

        def items(self, section):
            return [("key", "value")]

        def getboolean(self, section, key):
            return True

        def get(self, section, key):
            return "value"

    monkeypatch.setattr("configparser.ConfigParser", MockConfigParser)

def test_config(mock_getcwd, mock_isfile, mock_open_file, mock_configparser):
    with patch("semantic_release.settings._config_from_ini", return_value={"ini_key": "ini_value"}):
        with patch("semantic_release.settings._config_from_pyproject", return_value={"toml_key": "toml_value"}):
            config = _config()
            assert isinstance(config, UserDict)
            assert config["ini_key"] == "ini_value"
            assert config["toml_key"] == "toml_value"
