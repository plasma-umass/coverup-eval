# file: httpie/output/processing.py:26-53
# asked: {"lines": [], "branches": [[41, 39]]}
# gained: {"lines": [], "branches": [[41, 39]]}

import pytest
from unittest.mock import Mock, patch
from httpie.output.processing import Formatting
from httpie.context import Environment

class MockFormatter:
    def __init__(self, env, **kwargs):
        self.enabled = kwargs.get('enabled', True)
    
    def format_headers(self, headers):
        return headers
    
    def format_body(self, content, mime):
        return content

@pytest.fixture
def mock_plugin_manager(monkeypatch):
    mock_get_formatters_grouped = Mock(return_value={
        'group1': [MockFormatter],
        'group2': [MockFormatter]
    })
    monkeypatch.setattr('httpie.plugins.registry.plugin_manager.get_formatters_grouped', mock_get_formatters_grouped)
    return mock_get_formatters_grouped

def test_formatting_with_disabled_plugin(mock_plugin_manager):
    env = Environment()
    formatting = Formatting(groups=['group1', 'group2'], env=env, enabled=False)
    assert len(formatting.enabled_plugins) == 0

def test_formatting_with_enabled_plugin(mock_plugin_manager):
    env = Environment()
    formatting = Formatting(groups=['group1', 'group2'], env=env, enabled=True)
    assert len(formatting.enabled_plugins) == 2
