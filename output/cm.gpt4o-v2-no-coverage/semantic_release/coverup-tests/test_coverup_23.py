# file: semantic_release/settings.py:64-74
# asked: {"lines": [64, 65, 66, 67, 68, 69, 70, 71, 72, 74], "branches": [[65, 66], [65, 74], [69, 70], [69, 74]]}
# gained: {"lines": [64, 65, 66, 67, 68, 69, 70, 71, 72, 74], "branches": [[65, 66], [65, 74], [69, 70]]}

import os
import pytest
import tomlkit
from tomlkit.exceptions import TOMLKitError
from unittest import mock
from semantic_release.settings import _config_from_pyproject

@pytest.fixture
def mock_isfile():
    with mock.patch("os.path.isfile") as mock_isfile:
        yield mock_isfile

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open(read_data="[tool.semantic_release]\nkey = 'value'")) as mock_open:
        yield mock_open

@pytest.fixture
def mock_tomlkit_loads():
    with mock.patch("tomlkit.loads", side_effect=tomlkit.loads) as mock_loads:
        yield mock_loads

@pytest.fixture
def mock_logger():
    with mock.patch("semantic_release.settings.logger") as mock_logger:
        yield mock_logger

def test_config_from_pyproject_file_exists(mock_isfile, mock_open, mock_tomlkit_loads):
    mock_isfile.return_value = True
    result = _config_from_pyproject("pyproject.toml")
    assert result == {"key": "value"}
    mock_isfile.assert_called_once_with("pyproject.toml")
    mock_open.assert_called_once_with("pyproject.toml", "r")
    mock_tomlkit_loads.assert_called_once()

def test_config_from_pyproject_file_not_exists(mock_isfile):
    mock_isfile.return_value = False
    result = _config_from_pyproject("pyproject.toml")
    assert result == {}
    mock_isfile.assert_called_once_with("pyproject.toml")

def test_config_from_pyproject_tomlkit_error(mock_isfile, mock_open, mock_tomlkit_loads, mock_logger):
    mock_isfile.return_value = True
    mock_tomlkit_loads.side_effect = TOMLKitError("Mock TOMLKitError")
    result = _config_from_pyproject("pyproject.toml")
    assert result == {}
    mock_isfile.assert_called_once_with("pyproject.toml")
    mock_open.assert_called_once_with("pyproject.toml", "r")
    mock_tomlkit_loads.assert_called_once()
    mock_logger.debug.assert_called_once_with("Could not decode pyproject.toml: Mock TOMLKitError")
