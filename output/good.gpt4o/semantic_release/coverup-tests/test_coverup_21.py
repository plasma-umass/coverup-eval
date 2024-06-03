# file semantic_release/settings.py:64-74
# lines [64, 65, 66, 67, 68, 69, 70, 71, 72, 74]
# branches ['65->66', '65->74', '69->70', '69->74']

import os
import pytest
import tomlkit
from unittest import mock
from semantic_release.settings import _config_from_pyproject
from tomlkit.exceptions import TOMLKitError

def test_config_from_pyproject_file_exists(mocker):
    mocker.patch("os.path.isfile", return_value=True)
    mock_open = mocker.patch("builtins.open", mock.mock_open(read_data='[tool.semantic_release]\nversion="1.0.0"'))
    result = _config_from_pyproject("pyproject.toml")
    mock_open.assert_called_once_with("pyproject.toml", "r")
    assert result == {"version": "1.0.0"}

def test_config_from_pyproject_file_not_exists(mocker):
    mocker.patch("os.path.isfile", return_value=False)
    result = _config_from_pyproject("pyproject.toml")
    assert result == {}

def test_config_from_pyproject_tomlkit_error(mocker):
    mocker.patch("os.path.isfile", return_value=True)
    mock_open = mocker.patch("builtins.open", mock.mock_open(read_data='invalid toml'))
    mocker.patch("tomlkit.loads", side_effect=TOMLKitError("Invalid TOML"))
    mock_logger = mocker.patch("semantic_release.settings.logger")
    result = _config_from_pyproject("pyproject.toml")
    mock_open.assert_called_once_with("pyproject.toml", "r")
    mock_logger.debug.assert_called_once_with("Could not decode pyproject.toml: Invalid TOML")
    assert result == {}
