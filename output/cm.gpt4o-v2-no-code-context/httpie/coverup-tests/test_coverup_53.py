# file: httpie/plugins/manager.py:28-29
# asked: {"lines": [28, 29], "branches": []}
# gained: {"lines": [28, 29], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager, BasePlugin

class DummyPlugin(BasePlugin):
    pass

class AnotherPlugin(BasePlugin):
    pass

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_filter_with_matching_type(plugin_manager):
    plugin_manager.append(DummyPlugin)
    plugin_manager.append(AnotherPlugin)
    result = plugin_manager.filter(by_type=BasePlugin)
    assert result == [DummyPlugin, AnotherPlugin]

def test_filter_with_non_matching_type(plugin_manager):
    class NonMatchingPlugin:
        pass

    plugin_manager.append(DummyPlugin)
    plugin_manager.append(NonMatchingPlugin)
    result = plugin_manager.filter(by_type=BasePlugin)
    assert result == [DummyPlugin]

def test_filter_with_empty_manager(plugin_manager):
    result = plugin_manager.filter(by_type=BasePlugin)
    assert result == []
