# file: httpie/output/processing.py:26-53
# asked: {"lines": [26, 27, 29, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 49, 50, 51, 52, 53], "branches": [[38, 0], [38, 39], [39, 38], [39, 40], [41, 39], [41, 42], [45, 46], [45, 47], [50, 51], [50, 53], [51, 52], [51, 53]]}
# gained: {"lines": [26, 27, 29, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 49, 50, 51, 52, 53], "branches": [[38, 0], [38, 39], [39, 38], [39, 40], [41, 42], [45, 46], [45, 47], [50, 51], [51, 52], [51, 53]]}

import pytest
from unittest.mock import Mock, patch
from httpie.output.processing import Formatting
from httpie.plugins.registry import plugin_manager
from httpie.context import Environment

class MockFormatterPlugin:
    def __init__(self, env, **kwargs):
        self.env = env
        self.kwargs = kwargs
        self.enabled = True

    def format_headers(self, headers: str) -> str:
        return headers + " formatted"

    def format_body(self, content: str, mime: str) -> str:
        return content + " formatted"

def test_formatting_initialization(monkeypatch):
    mock_get_formatters_grouped = Mock(return_value={'group1': [MockFormatterPlugin]})
    monkeypatch.setattr(plugin_manager, 'get_formatters_grouped', mock_get_formatters_grouped)

    env = Environment()
    formatting = Formatting(groups=['group1'], env=env, format_options={})

    assert len(formatting.enabled_plugins) == 1
    assert isinstance(formatting.enabled_plugins[0], MockFormatterPlugin)

def test_format_headers(monkeypatch):
    mock_get_formatters_grouped = Mock(return_value={'group1': [MockFormatterPlugin]})
    monkeypatch.setattr(plugin_manager, 'get_formatters_grouped', mock_get_formatters_grouped)

    env = Environment()
    formatting = Formatting(groups=['group1'], env=env, format_options={})
    headers = "headers"
    formatted_headers = formatting.format_headers(headers)

    assert formatted_headers == "headers formatted"

def test_format_body(monkeypatch):
    mock_get_formatters_grouped = Mock(return_value={'group1': [MockFormatterPlugin]})
    monkeypatch.setattr(plugin_manager, 'get_formatters_grouped', mock_get_formatters_grouped)

    def mock_is_valid_mime(mime):
        return True

    monkeypatch.setattr('httpie.output.processing.is_valid_mime', mock_is_valid_mime)

    env = Environment()
    formatting = Formatting(groups=['group1'], env=env, format_options={})
    content = "content"
    mime = "application/json"
    formatted_content = formatting.format_body(content, mime)

    assert formatted_content == "content formatted"
