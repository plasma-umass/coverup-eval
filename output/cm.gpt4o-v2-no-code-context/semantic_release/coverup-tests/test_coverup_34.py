# file: semantic_release/settings.py:64-74
# asked: {"lines": [64, 65, 66, 67, 68, 69, 70, 71, 72, 74], "branches": [[65, 66], [65, 74], [69, 70], [69, 74]]}
# gained: {"lines": [64, 65, 66, 67, 68, 69, 70, 71, 72, 74], "branches": [[65, 66], [65, 74], [69, 70]]}

import os
import pytest
import tomlkit
from tomlkit.exceptions import TOMLKitError
from unittest.mock import mock_open, patch
import logging

# Assuming the function _config_from_pyproject is imported from semantic_release.settings
from semantic_release.settings import _config_from_pyproject

logger = logging.getLogger('semantic_release.settings')

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch.object(logger, 'debug')

def test_config_from_pyproject_file_exists_valid_toml(monkeypatch):
    mock_toml_content = """
    [tool.semantic_release]
    version = "1.0.0"
    """
    monkeypatch.setattr(os.path, 'isfile', lambda x: True)
    with patch("builtins.open", mock_open(read_data=mock_toml_content)):
        result = _config_from_pyproject("pyproject.toml")
        assert result == {"version": "1.0.0"}

def test_config_from_pyproject_file_exists_invalid_toml(monkeypatch, mock_logger):
    monkeypatch.setattr(os.path, 'isfile', lambda x: True)
    with patch("builtins.open", mock_open(read_data="invalid_toml")):
        result = _config_from_pyproject("pyproject.toml")
        assert result == {}
        assert mock_logger.call_count == 1
        assert "Could not decode pyproject.toml: " in mock_logger.call_args[0][0]

def test_config_from_pyproject_file_does_not_exist(monkeypatch):
    monkeypatch.setattr(os.path, 'isfile', lambda x: False)
    result = _config_from_pyproject("pyproject.toml")
    assert result == {}
