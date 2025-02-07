# file: httpie/config.py:99-121
# asked: {"lines": [], "branches": [[103, 106], [106, 109]]}
# gained: {"lines": [], "branches": [[103, 106], [106, 109]]}

import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch
from httpie.config import BaseConfigDict

@pytest.fixture
def config_dict(tmp_path):
    path = tmp_path / "config.json"
    return BaseConfigDict(path=path)

def test_save_with_helpurl_and_about(config_dict, monkeypatch):
    config_dict.helpurl = "http://example.com/help"
    config_dict.about = "About information"
    
    mock_ensure_directory = MagicMock()
    monkeypatch.setattr(config_dict, "ensure_directory", mock_ensure_directory)
    
    with patch("pathlib.Path.write_text", return_value=None) as mock_write_text:
        config_dict.save()
    
    assert config_dict["__meta__"]["help"] == "http://example.com/help"
    assert config_dict["__meta__"]["about"] == "About information"
    mock_ensure_directory.assert_called_once()
    mock_write_text.assert_called_once()

def test_save_without_helpurl_and_about(config_dict, monkeypatch):
    config_dict.helpurl = None
    config_dict.about = None
    
    mock_ensure_directory = MagicMock()
    monkeypatch.setattr(config_dict, "ensure_directory", mock_ensure_directory)
    
    with patch("pathlib.Path.write_text", return_value=None) as mock_write_text:
        config_dict.save()
    
    assert "help" not in config_dict["__meta__"]
    assert "about" not in config_dict["__meta__"]
    mock_ensure_directory.assert_called_once()
    mock_write_text.assert_called_once()
