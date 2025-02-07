# file: semantic_release/settings.py:64-74
# asked: {"lines": [], "branches": [[69, 74]]}
# gained: {"lines": [], "branches": [[69, 74]]}

import os
import pytest
import tomlkit
from tomlkit.exceptions import TOMLKitError
from semantic_release.settings import _config_from_pyproject
import logging

def test_config_from_pyproject_with_valid_file(monkeypatch):
    sample_toml = """
    [tool.semantic_release]
    version = "1.0.0"
    """
    def mock_isfile(path):
        return True

    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO(sample_toml)

    monkeypatch.setattr(os.path, "isfile", mock_isfile)
    monkeypatch.setattr("builtins.open", mock_open)

    result = _config_from_pyproject("pyproject.toml")
    assert result == {"version": "1.0.0"}

def test_config_from_pyproject_with_empty_toml(monkeypatch):
    sample_toml = ""
    def mock_isfile(path):
        return True

    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO(sample_toml)

    monkeypatch.setattr(os.path, "isfile", mock_isfile)
    monkeypatch.setattr("builtins.open", mock_open)

    result = _config_from_pyproject("pyproject.toml")
    assert result == {}

def test_config_from_pyproject_with_invalid_toml(monkeypatch, caplog):
    def mock_isfile(path):
        return True

    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO("invalid_toml")

    monkeypatch.setattr(os.path, "isfile", mock_isfile)
    monkeypatch.setattr("builtins.open", mock_open)

    with caplog.at_level(logging.DEBUG):
        result = _config_from_pyproject("pyproject.toml")
        assert result == {}
        assert any("Could not decode pyproject.toml" in message for message in caplog.messages)

def test_config_from_pyproject_with_no_file(monkeypatch):
    def mock_isfile(path):
        return False

    monkeypatch.setattr(os.path, "isfile", mock_isfile)

    result = _config_from_pyproject("pyproject.toml")
    assert result == {}
