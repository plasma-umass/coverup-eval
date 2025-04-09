# file: semantic_release/settings.py:80-94
# asked: {"lines": [80, 87, 89, 90, 92, 93, 94], "branches": []}
# gained: {"lines": [80, 87, 89, 90, 92, 93, 94], "branches": []}

import pytest
import importlib
from unittest.mock import patch, Mock
from semantic_release.settings import current_commit_parser
from semantic_release.errors import ImproperConfigurationError

@pytest.fixture
def mock_config(monkeypatch):
    config = {
        "commit_parser": "some_module.some_parser"
    }
    monkeypatch.setattr('semantic_release.settings.config', config)
    return config

def test_current_commit_parser_success(mock_config):
    mock_module = Mock()
    mock_parser = Mock()
    mock_module.some_parser = mock_parser

    with patch('importlib.import_module', return_value=mock_module):
        parser = current_commit_parser()
        assert parser == mock_parser

def test_current_commit_parser_import_error(mock_config):
    with patch('importlib.import_module', side_effect=ImportError):
        with pytest.raises(ImproperConfigurationError, match='Unable to import parser'):
            current_commit_parser()

def test_current_commit_parser_attribute_error(mock_config):
    mock_module = Mock()
    del mock_module.some_parser

    with patch('importlib.import_module', return_value=mock_module):
        with pytest.raises(ImproperConfigurationError, match='Unable to import parser'):
            current_commit_parser()
