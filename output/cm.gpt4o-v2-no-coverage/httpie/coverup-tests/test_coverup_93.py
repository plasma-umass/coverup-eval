# file: httpie/output/processing.py:26-53
# asked: {"lines": [], "branches": [[41, 39], [50, 53]]}
# gained: {"lines": [], "branches": [[50, 53]]}

import pytest
from unittest.mock import Mock, patch
from httpie.output.processing import Formatting
from httpie.context import Environment

class MockFormatter:
    def __init__(self, env, **kwargs):
        self.enabled = True

    def format_headers(self, headers):
        return headers.upper()

    def format_body(self, content, mime):
        return content.lower()

def mock_get_formatters_grouped():
    return {
        'group1': [MockFormatter],
        'group2': [MockFormatter]
    }

def mock_is_valid_mime(mime):
    return mime == 'application/json'

@pytest.fixture
def mock_environment():
    return Environment()

@pytest.fixture
def mock_plugin_manager(monkeypatch):
    monkeypatch.setattr('httpie.plugins.registry.plugin_manager.get_formatters_grouped', mock_get_formatters_grouped)

@pytest.fixture
def mock_valid_mime(monkeypatch):
    monkeypatch.setattr('httpie.output.processing.is_valid_mime', mock_is_valid_mime)

def test_formatting_initialization(mock_plugin_manager, mock_environment):
    formatting = Formatting(groups=['group1', 'group2'], env=mock_environment)
    assert len(formatting.enabled_plugins) == 2

def test_format_headers(mock_plugin_manager, mock_environment):
    formatting = Formatting(groups=['group1'], env=mock_environment)
    result = formatting.format_headers('test-header')
    assert result == 'TEST-HEADER'

def test_format_body_valid_mime(mock_plugin_manager, mock_valid_mime, mock_environment):
    formatting = Formatting(groups=['group1'], env=mock_environment)
    result = formatting.format_body('TEST-BODY', 'application/json')
    assert result == 'test-body'

def test_format_body_invalid_mime(mock_plugin_manager, mock_valid_mime, mock_environment):
    formatting = Formatting(groups=['group1'], env=mock_environment)
    result = formatting.format_body('TEST-BODY', 'text/plain')
    assert result == 'TEST-BODY'
