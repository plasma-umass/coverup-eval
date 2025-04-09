# file: httpie/plugins/manager.py:51-52
# asked: {"lines": [51, 52], "branches": []}
# gained: {"lines": [51, 52], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager, FormatterPlugin

class DummyFormatter(FormatterPlugin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.format_options = kwargs.get('format_options', {})

@pytest.fixture
def plugin_manager():
    class TestPluginManager(PluginManager):
        def filter(self, by_type):
            return [plugin for plugin in self if isinstance(plugin, by_type)]
    return TestPluginManager()

def test_get_formatters_with_formatter_plugin(plugin_manager):
    formatter = DummyFormatter(format_options={})
    plugin_manager.append(formatter)
    formatters = plugin_manager.get_formatters()
    assert len(formatters) == 1
    assert formatters[0] is formatter

def test_get_formatters_without_formatter_plugin(plugin_manager):
    formatters = plugin_manager.get_formatters()
    assert len(formatters) == 0
