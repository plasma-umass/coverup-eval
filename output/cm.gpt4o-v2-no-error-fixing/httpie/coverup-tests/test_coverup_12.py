# file: httpie/output/processing.py:26-53
# asked: {"lines": [26, 27, 29, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 49, 50, 51, 52, 53], "branches": [[38, 0], [38, 39], [39, 38], [39, 40], [41, 39], [41, 42], [45, 46], [45, 47], [50, 51], [50, 53], [51, 52], [51, 53]]}
# gained: {"lines": [26, 27, 29, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 49, 50, 51, 52, 53], "branches": [[38, 0], [38, 39], [39, 38], [39, 40], [41, 42], [45, 46], [45, 47], [50, 51], [50, 53], [51, 52], [51, 53]]}

import pytest
from unittest.mock import Mock, patch
from httpie.output.processing import Formatting
from httpie.context import Environment

@pytest.fixture
def mock_plugin_manager():
    with patch('httpie.plugins.registry.plugin_manager.get_formatters_grouped') as mock:
        yield mock

@pytest.fixture
def mock_is_valid_mime():
    with patch('httpie.output.processing.is_valid_mime') as mock:
        yield mock

def test_formatting_initialization(mock_plugin_manager):
    mock_plugin = Mock()
    mock_plugin.enabled = True
    mock_plugin_manager.return_value = {'group1': [lambda env, **kwargs: mock_plugin]}
    
    fmt = Formatting(groups=['group1'], env=Environment())
    
    assert len(fmt.enabled_plugins) == 1
    assert fmt.enabled_plugins[0] == mock_plugin

def test_format_headers(mock_plugin_manager):
    mock_plugin = Mock()
    mock_plugin.enabled = True
    mock_plugin.format_headers.return_value = 'formatted headers'
    mock_plugin_manager.return_value = {'group1': [lambda env, **kwargs: mock_plugin]}
    
    fmt = Formatting(groups=['group1'], env=Environment())
    result = fmt.format_headers('headers')
    
    assert result == 'formatted headers'
    mock_plugin.format_headers.assert_called_once_with('headers')

def test_format_body(mock_plugin_manager, mock_is_valid_mime):
    mock_plugin = Mock()
    mock_plugin.enabled = True
    mock_plugin.format_body.return_value = 'formatted body'
    mock_plugin_manager.return_value = {'group1': [lambda env, **kwargs: mock_plugin]}
    mock_is_valid_mime.return_value = True
    
    fmt = Formatting(groups=['group1'], env=Environment())
    result = fmt.format_body('body', 'mime/type')
    
    assert result == 'formatted body'
    mock_plugin.format_body.assert_called_once_with('body', 'mime/type')
    mock_is_valid_mime.assert_called_once_with('mime/type')

def test_format_body_invalid_mime(mock_plugin_manager, mock_is_valid_mime):
    mock_plugin = Mock()
    mock_plugin.enabled = True
    mock_plugin_manager.return_value = {'group1': [lambda env, **kwargs: mock_plugin]}
    mock_is_valid_mime.return_value = False
    
    fmt = Formatting(groups=['group1'], env=Environment())
    result = fmt.format_body('body', 'invalid/mime')
    
    assert result == 'body'
    mock_plugin.format_body.assert_not_called()
    mock_is_valid_mime.assert_called_once_with('invalid/mime')
