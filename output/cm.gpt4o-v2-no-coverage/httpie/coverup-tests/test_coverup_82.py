# file: httpie/plugins/manager.py:51-52
# asked: {"lines": [51, 52], "branches": []}
# gained: {"lines": [51, 52], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins import FormatterPlugin

class MockFormatterPlugin(FormatterPlugin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

def test_get_formatters(monkeypatch):
    # Create a mock filter method
    def mock_filter(self, plugin_type):
        assert plugin_type == FormatterPlugin
        return [MockFormatterPlugin(format_options={})]

    # Patch the filter method in PluginManager
    monkeypatch.setattr(PluginManager, 'filter', mock_filter)

    # Create an instance of PluginManager and call get_formatters
    manager = PluginManager()
    formatters = manager.get_formatters()

    # Assertions to verify the behavior
    assert len(formatters) == 1
    assert isinstance(formatters[0], MockFormatterPlugin)
    assert formatters[0].enabled
    assert formatters[0].format_options == {}
