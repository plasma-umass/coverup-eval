# file httpie/output/processing.py:26-53
# lines [26, 27, 29, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 49, 50, 51, 52, 53]
# branches ['38->exit', '38->39', '39->38', '39->40', '41->39', '41->42', '45->46', '45->47', '50->51', '50->53', '51->52', '51->53']

import pytest
from unittest.mock import Mock, patch
from httpie.output.processing import Formatting
from httpie.context import Environment

@pytest.fixture
def mock_plugin_manager(mocker):
    mocker.patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={
        'group1': [MockPlugin],
        'group2': [MockPlugin]
    })

class MockPlugin:
    def __init__(self, env, **kwargs):
        self.env = env
        self.kwargs = kwargs
        self.enabled = True

    def format_headers(self, headers):
        return headers + ' formatted'

    def format_body(self, content, mime):
        return content + ' formatted'

def is_valid_mime(mime):
    return mime == 'application/json'

@patch('httpie.output.processing.is_valid_mime', side_effect=is_valid_mime)
def test_formatting_initialization(mock_is_valid_mime, mock_plugin_manager):
    env = Environment()
    formatting = Formatting(groups=['group1', 'group2'], env=env)
    assert len(formatting.enabled_plugins) == 2

@patch('httpie.output.processing.is_valid_mime', side_effect=is_valid_mime)
def test_format_headers(mock_is_valid_mime, mock_plugin_manager):
    env = Environment()
    formatting = Formatting(groups=['group1'], env=env)
    headers = 'Test Headers'
    formatted_headers = formatting.format_headers(headers)
    assert formatted_headers == 'Test Headers formatted'

@patch('httpie.output.processing.is_valid_mime', side_effect=is_valid_mime)
def test_format_body(mock_is_valid_mime, mock_plugin_manager):
    env = Environment()
    formatting = Formatting(groups=['group1'], env=env)
    content = 'Test Content'
    mime = 'application/json'
    formatted_content = formatting.format_body(content, mime)
    assert formatted_content == 'Test Content formatted'

@patch('httpie.output.processing.is_valid_mime', side_effect=is_valid_mime)
def test_format_body_invalid_mime(mock_is_valid_mime, mock_plugin_manager):
    env = Environment()
    formatting = Formatting(groups=['group1'], env=env)
    content = 'Test Content'
    mime = 'invalid/mime'
    formatted_content = formatting.format_body(content, mime)
    assert formatted_content == 'Test Content'
