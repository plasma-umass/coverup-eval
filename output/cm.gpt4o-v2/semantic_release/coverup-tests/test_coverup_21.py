# file: semantic_release/settings.py:64-74
# asked: {"lines": [64, 65, 66, 67, 68, 69, 70, 71, 72, 74], "branches": [[65, 66], [65, 74], [69, 70], [69, 74]]}
# gained: {"lines": [64, 65, 66, 67, 68, 69, 70, 71, 72, 74], "branches": [[65, 66], [65, 74], [69, 70]]}

import os
import pytest
import tomlkit
from tomlkit.exceptions import TOMLKitError
from unittest.mock import mock_open, patch

from semantic_release.settings import _config_from_pyproject

def test_config_from_pyproject_file_exists_with_valid_toml(monkeypatch):
    mock_toml_content = """
    [tool.semantic_release]
    version = "1.0.0"
    """
    monkeypatch.setattr(os.path, "isfile", lambda x: True)
    with patch("builtins.open", mock_open(read_data=mock_toml_content)):
        result = _config_from_pyproject("pyproject.toml")
        assert result == {"version": "1.0.0"}

def test_config_from_pyproject_file_exists_with_invalid_toml(monkeypatch, caplog):
    monkeypatch.setattr(os.path, "isfile", lambda x: True)
    with patch("builtins.open", mock_open(read_data="invalid_toml")):
        with patch("semantic_release.settings.logger.debug") as mock_debug:
            result = _config_from_pyproject("pyproject.toml")
            assert result == {}
            mock_debug.assert_called_once()
            assert "Could not decode pyproject.toml" in mock_debug.call_args[0][0]

def test_config_from_pyproject_file_does_not_exist(monkeypatch):
    monkeypatch.setattr(os.path, "isfile", lambda x: False)
    result = _config_from_pyproject("pyproject.toml")
    assert result == {}
