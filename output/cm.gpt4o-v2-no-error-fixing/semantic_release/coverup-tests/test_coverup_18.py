# file: semantic_release/settings.py:80-94
# asked: {"lines": [80, 87, 89, 90, 92, 93, 94], "branches": []}
# gained: {"lines": [80, 87, 89, 90, 92, 93, 94], "branches": []}

import pytest
import importlib
from semantic_release.errors import ImproperConfigurationError

def test_current_commit_parser_valid(monkeypatch):
    # Mock the config.get to return a valid parser path
    def mock_get(key):
        return "os.path.join"
    
    monkeypatch.setattr("semantic_release.settings.config.get", mock_get)
    
    from semantic_release.settings import current_commit_parser
    
    parser = current_commit_parser()
    assert parser == importlib.import_module("os.path").join

def test_current_commit_parser_import_error(monkeypatch):
    # Mock the config.get to return an invalid module path
    def mock_get(key):
        return "nonexistent.module.parser"
    
    monkeypatch.setattr("semantic_release.settings.config.get", mock_get)
    
    from semantic_release.settings import current_commit_parser
    
    with pytest.raises(ImproperConfigurationError):
        current_commit_parser()

def test_current_commit_parser_attribute_error(monkeypatch):
    # Mock the config.get to return a valid module but invalid attribute
    def mock_get(key):
        return "os.path.nonexistent"
    
    monkeypatch.setattr("semantic_release.settings.config.get", mock_get)
    
    from semantic_release.settings import current_commit_parser
    
    with pytest.raises(ImproperConfigurationError):
        current_commit_parser()
