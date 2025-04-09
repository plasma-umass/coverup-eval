# file: httpie/output/processing.py:26-53
# asked: {"lines": [26, 27, 29, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 49, 50, 51, 52, 53], "branches": [[38, 0], [38, 39], [39, 38], [39, 40], [41, 39], [41, 42], [45, 46], [45, 47], [50, 51], [50, 53], [51, 52], [51, 53]]}
# gained: {"lines": [26, 27, 29, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 49, 50, 51, 52, 53], "branches": [[38, 0], [38, 39], [39, 38], [39, 40], [41, 39], [41, 42], [45, 46], [45, 47], [50, 51], [50, 53], [51, 52], [51, 53]]}

import pytest
from unittest.mock import MagicMock, patch
from httpie.output.processing import Formatting

@pytest.fixture
def mock_environment():
    return MagicMock()

@pytest.fixture
def mock_plugin_manager():
    with patch('httpie.output.processing.plugin_manager') as mock:
        yield mock

@pytest.fixture
def mock_is_valid_mime():
    with patch('httpie.output.processing.is_valid_mime') as mock:
        yield mock

def test_formatting_initialization(mock_plugin_manager, mock_environment):
    mock_plugin = MagicMock()
    mock_plugin.enabled = True
    mock_plugin_manager.get_formatters_grouped.return_value = {
        'group1': [lambda env, **kwargs: mock_plugin]
    }

    formatting = Formatting(groups=['group1'], env=mock_environment)
    assert len(formatting.enabled_plugins) == 1
    assert formatting.enabled_plugins[0] == mock_plugin

def test_formatting_initialization_no_enabled_plugins(mock_plugin_manager, mock_environment):
    mock_plugin = MagicMock()
    mock_plugin.enabled = False
    mock_plugin_manager.get_formatters_grouped.return_value = {
        'group1': [lambda env, **kwargs: mock_plugin]
    }

    formatting = Formatting(groups=['group1'], env=mock_environment)
    assert len(formatting.enabled_plugins) == 0

def test_format_headers(mock_plugin_manager, mock_environment):
    mock_plugin = MagicMock()
    mock_plugin.enabled = True
    mock_plugin.format_headers.return_value = 'formatted headers'
    mock_plugin_manager.get_formatters_grouped.return_value = {
        'group1': [lambda env, **kwargs: mock_plugin]
    }

    formatting = Formatting(groups=['group1'], env=mock_environment)
    result = formatting.format_headers('headers')
    assert result == 'formatted headers'
    mock_plugin.format_headers.assert_called_once_with('headers')

def test_format_body_valid_mime(mock_plugin_manager, mock_environment, mock_is_valid_mime):
    mock_plugin = MagicMock()
    mock_plugin.enabled = True
    mock_plugin.format_body.return_value = 'formatted body'
    mock_plugin_manager.get_formatters_grouped.return_value = {
        'group1': [lambda env, **kwargs: mock_plugin]
    }
    mock_is_valid_mime.return_value = True

    formatting = Formatting(groups=['group1'], env=mock_environment)
    result = formatting.format_body('content', 'mime/type')
    assert result == 'formatted body'
    mock_plugin.format_body.assert_called_once_with('content', 'mime/type')

def test_format_body_invalid_mime(mock_plugin_manager, mock_environment, mock_is_valid_mime):
    mock_plugin = MagicMock()
    mock_plugin.enabled = True
    mock_plugin_manager.get_formatters_grouped.return_value = {
        'group1': [lambda env, **kwargs: mock_plugin]
    }
    mock_is_valid_mime.return_value = False

    formatting = Formatting(groups=['group1'], env=mock_environment)
    result = formatting.format_body('content', 'mime/type')
    assert result == 'content'
    mock_plugin.format_body.assert_not_called()
