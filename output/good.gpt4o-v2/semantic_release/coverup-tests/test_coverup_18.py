# file: semantic_release/settings.py:80-94
# asked: {"lines": [80, 87, 89, 90, 92, 93, 94], "branches": []}
# gained: {"lines": [80, 87, 89, 90, 92, 93, 94], "branches": []}

import pytest
import importlib
from unittest.mock import patch, Mock
from semantic_release.settings import current_commit_parser
from semantic_release.errors import ImproperConfigurationError

@pytest.fixture
def mock_config():
    with patch('semantic_release.settings.config') as mock_config:
        yield mock_config

def test_current_commit_parser_success(mock_config):
    mock_config.get.return_value = 'os.path.join'
    parser = current_commit_parser()
    assert parser == importlib.import_module('os.path').join

def test_current_commit_parser_import_error(mock_config):
    mock_config.get.return_value = 'nonexistent.module.parser'
    with pytest.raises(ImproperConfigurationError) as excinfo:
        current_commit_parser()
    assert 'Unable to import parser' in str(excinfo.value)

def test_current_commit_parser_attribute_error(mock_config):
    mock_config.get.return_value = 'os.path.nonexistent'
    with pytest.raises(ImproperConfigurationError) as excinfo:
        current_commit_parser()
    assert 'Unable to import parser' in str(excinfo.value)
