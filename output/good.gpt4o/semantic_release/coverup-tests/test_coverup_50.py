# file semantic_release/settings.py:64-74
# lines []
# branches ['69->74']

import os
import pytest
import tomlkit
from unittest import mock
from semantic_release.settings import _config_from_pyproject

def test_config_from_pyproject_with_valid_pyproject(mocker):
    mocker.patch("os.path.isfile", return_value=True)
    mock_open = mocker.patch("builtins.open", mock.mock_open(read_data='[tool.semantic_release]\nversion="1.0.0"'))
    mocker.patch("tomlkit.loads", return_value={"tool": {"semantic_release": {"version": "1.0.0"}}})

    result = _config_from_pyproject("pyproject.toml")
    assert result == {"version": "1.0.0"}

    mock_open.assert_called_once_with("pyproject.toml", "r")

def test_config_from_pyproject_with_empty_pyproject(mocker):
    mocker.patch("os.path.isfile", return_value=True)
    mock_open = mocker.patch("builtins.open", mock.mock_open(read_data=''))
    mocker.patch("tomlkit.loads", return_value={})

    result = _config_from_pyproject("pyproject.toml")
    assert result == {}

    mock_open.assert_called_once_with("pyproject.toml", "r")

def test_config_from_pyproject_with_invalid_toml(mocker):
    mocker.patch("os.path.isfile", return_value=True)
    mock_open = mocker.patch("builtins.open", mock.mock_open(read_data='invalid_toml'))
    mocker.patch("tomlkit.loads", side_effect=tomlkit.exceptions.TOMLKitError("Error"))

    result = _config_from_pyproject("pyproject.toml")
    assert result == {}

    mock_open.assert_called_once_with("pyproject.toml", "r")
