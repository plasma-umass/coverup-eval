# file: semantic_release/settings.py:64-74
# asked: {"lines": [], "branches": [[69, 74]]}
# gained: {"lines": [], "branches": [[69, 74]]}

import os
import pytest
import tomlkit
from unittest.mock import mock_open, patch
from semantic_release.settings import _config_from_pyproject

def test_config_from_pyproject_file_exists_with_content(monkeypatch):
    mock_toml_content = """
    [tool.semantic_release]
    version = "1.0.0"
    """
    mock_path = "pyproject.toml"

    monkeypatch.setattr(os.path, "isfile", lambda x: True)
    monkeypatch.setattr("builtins.open", mock_open(read_data=mock_toml_content))

    result = _config_from_pyproject(mock_path)
    assert result == {"version": "1.0.0"}

def test_config_from_pyproject_file_exists_empty_content(monkeypatch):
    mock_toml_content = ""
    mock_path = "pyproject.toml"

    monkeypatch.setattr(os.path, "isfile", lambda x: True)
    monkeypatch.setattr("builtins.open", mock_open(read_data=mock_toml_content))

    result = _config_from_pyproject(mock_path)
    assert result == {}

def test_config_from_pyproject_file_not_exists(monkeypatch):
    mock_path = "pyproject.toml"

    monkeypatch.setattr(os.path, "isfile", lambda x: False)

    result = _config_from_pyproject(mock_path)
    assert result == {}

def test_config_from_pyproject_tomlkit_error(monkeypatch):
    mock_path = "pyproject.toml"

    monkeypatch.setattr(os.path, "isfile", lambda x: True)
    monkeypatch.setattr("builtins.open", mock_open(read_data="invalid toml content"))

    with patch("tomlkit.loads", side_effect=tomlkit.exceptions.TOMLKitError):
        result = _config_from_pyproject(mock_path)
        assert result == {}
