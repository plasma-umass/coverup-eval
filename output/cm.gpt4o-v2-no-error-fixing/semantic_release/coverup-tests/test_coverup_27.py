# file: semantic_release/settings.py:64-74
# asked: {"lines": [66, 67, 68, 69, 70, 71, 72], "branches": [[65, 66], [69, 70], [69, 74]]}
# gained: {"lines": [66, 67, 68, 69, 70, 71, 72], "branches": [[65, 66], [69, 70]]}

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
    mock_open_func = mock_open(read_data=mock_toml_content)
    
    with patch("builtins.open", mock_open_func):
        with patch("os.path.isfile", return_value=True):
            result = _config_from_pyproject("pyproject.toml")
            assert result == {"version": "1.0.0"}

def test_config_from_pyproject_file_exists_with_invalid_toml(monkeypatch, caplog):
    mock_open_func = mock_open(read_data="invalid_toml_content")
    
    with patch("builtins.open", mock_open_func):
        with patch("os.path.isfile", return_value=True):
            with patch("semantic_release.settings.logger.debug") as mock_logger:
                result = _config_from_pyproject("pyproject.toml")
                assert result == {}
                mock_logger.assert_called_once()
                assert "Could not decode pyproject.toml" in mock_logger.call_args[0][0]

def test_config_from_pyproject_file_does_not_exist(monkeypatch):
    with patch("os.path.isfile", return_value=False):
        result = _config_from_pyproject("pyproject.toml")
        assert result == {}
