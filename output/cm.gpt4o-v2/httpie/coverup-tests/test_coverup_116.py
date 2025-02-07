# file: httpie/output/processing.py:26-53
# asked: {"lines": [], "branches": [[41, 39], [50, 53]]}
# gained: {"lines": [], "branches": [[41, 39], [50, 53]]}

import pytest
from unittest.mock import Mock, patch
from httpie.output.processing import Formatting
from httpie.context import Environment

class MockFormatter:
    def __init__(self, env, **kwargs):
        self.enabled = True

    def format_headers(self, headers):
        return headers

    def format_body(self, content, mime):
        return content

class DisabledMockFormatter:
    def __init__(self, env, **kwargs):
        self.enabled = False

    def format_headers(self, headers):
        return headers

    def format_body(self, content, mime):
        return content

@pytest.fixture
def mock_plugin_manager(monkeypatch):
    mock_get_formatters_grouped = Mock(return_value={'group1': [MockFormatter, DisabledMockFormatter]})
    monkeypatch.setattr('httpie.plugins.registry.plugin_manager.get_formatters_grouped', mock_get_formatters_grouped)
    return mock_get_formatters_grouped

@pytest.fixture
def mock_is_valid_mime(monkeypatch):
    mock_is_valid_mime = Mock(return_value=True)
    monkeypatch.setattr('httpie.output.processing.is_valid_mime', mock_is_valid_mime)
    return mock_is_valid_mime

def test_formatting_initialization(mock_plugin_manager):
    env = Environment()
    formatting = Formatting(groups=['group1'], env=env)
    assert len(formatting.enabled_plugins) == 1
    assert isinstance(formatting.enabled_plugins[0], MockFormatter)

def test_format_body_with_valid_mime(mock_plugin_manager, mock_is_valid_mime):
    env = Environment()
    formatting = Formatting(groups=['group1'], env=env)
    result = formatting.format_body('content', 'application/json')
    assert result == 'content'
    mock_is_valid_mime.assert_called_once_with('application/json')

def test_format_body_with_invalid_mime(mock_plugin_manager, monkeypatch):
    mock_is_valid_mime = Mock(return_value=False)
    monkeypatch.setattr('httpie.output.processing.is_valid_mime', mock_is_valid_mime)
    env = Environment()
    formatting = Formatting(groups=['group1'], env=env)
    result = formatting.format_body('content', 'invalid/mime')
    assert result == 'content'
    mock_is_valid_mime.assert_called_once_with('invalid/mime')
