# file: httpie/plugins/manager.py:54-59
# asked: {"lines": [54, 55, 56, 57, 58], "branches": []}
# gained: {"lines": [54, 55, 56, 57, 58], "branches": []}

import pytest
from unittest.mock import Mock, patch
from httpie.plugins.manager import PluginManager, FormatterPlugin

class MockFormatterPlugin(FormatterPlugin):
    group_name = 'test_group'
    def __init__(self, **kwargs):
        self.enabled = True
        self.kwargs = kwargs
        self.format_options = kwargs.get('format_options', {})

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_get_formatters_grouped(plugin_manager, monkeypatch):
    mock_formatter = MockFormatterPlugin(format_options={})
    mock_get_formatters = Mock(return_value=[mock_formatter])

    monkeypatch.setattr(plugin_manager, 'get_formatters', mock_get_formatters)

    grouped_formatters = plugin_manager.get_formatters_grouped()

    assert 'test_group' in grouped_formatters
    assert grouped_formatters['test_group'] == [mock_formatter]

    mock_get_formatters.assert_called_once()

def test_get_formatters(plugin_manager, monkeypatch):
    mock_filter = Mock(return_value=['formatter1', 'formatter2'])
    monkeypatch.setattr(plugin_manager, 'filter', mock_filter)

    formatters = plugin_manager.get_formatters()

    assert formatters == ['formatter1', 'formatter2']
    mock_filter.assert_called_once_with(FormatterPlugin)
