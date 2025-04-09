# file httpie/plugins/manager.py:51-52
# lines [51, 52]
# branches []

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import FormatterPlugin

# Mock plugin classes
class MockFormatterPlugin(FormatterPlugin):
    def __init__(self, **kwargs):
        kwargs.setdefault('format_options', {})
        super().__init__(**kwargs)

class MockNonFormatterPlugin:
    pass

@pytest.fixture
def plugin_manager():
    manager = PluginManager()
    yield manager
    manager.clear()

def test_get_formatters(plugin_manager):
    # Add a formatter plugin and a non-formatter plugin to the manager
    formatter_plugin = MockFormatterPlugin()
    non_formatter_plugin = MockNonFormatterPlugin()
    plugin_manager.append(MockFormatterPlugin)
    plugin_manager.append(MockNonFormatterPlugin)

    # Get formatters from the plugin manager
    formatters = plugin_manager.get_formatters()

    # Assert that only the formatter plugin is returned
    assert len(formatters) == 1
    assert issubclass(formatters[0], FormatterPlugin)

    # Clean up is handled by the plugin_manager fixture
