# file: httpie/plugins/manager.py:51-52
# asked: {"lines": [51, 52], "branches": []}
# gained: {"lines": [51, 52], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins import FormatterPlugin

class DummyFormatterPlugin(FormatterPlugin):
    pass

class DummyNonFormatterPlugin:
    pass

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_get_formatters(plugin_manager, monkeypatch):
    # Add a dummy formatter plugin and a non-formatter plugin to the manager
    plugin_manager.append(DummyFormatterPlugin)
    plugin_manager.append(DummyNonFormatterPlugin)

    # Ensure that get_formatters only returns the formatter plugin
    formatters = plugin_manager.get_formatters()
    assert formatters == [DummyFormatterPlugin]

    # Clean up
    plugin_manager.clear()
