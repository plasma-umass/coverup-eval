# file: httpie/plugins/manager.py:28-29
# asked: {"lines": [28, 29], "branches": []}
# gained: {"lines": [28, 29], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

class DummyPlugin(BasePlugin):
    pass

class AnotherPlugin(BasePlugin):
    pass

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_filter_with_no_plugins(plugin_manager):
    assert plugin_manager.filter(by_type=BasePlugin) == []

def test_filter_with_matching_plugin(plugin_manager):
    plugin_manager.append(DummyPlugin)
    result = plugin_manager.filter(by_type=BasePlugin)
    assert result == [DummyPlugin]

def test_filter_with_non_matching_plugin(plugin_manager):
    plugin_manager.append(str)  # str is not a subclass of BasePlugin
    result = plugin_manager.filter(by_type=BasePlugin)
    assert result == []

def test_filter_with_multiple_plugins(plugin_manager):
    plugin_manager.append(DummyPlugin)
    plugin_manager.append(AnotherPlugin)
    plugin_manager.append(str)  # str is not a subclass of BasePlugin
    result = plugin_manager.filter(by_type=BasePlugin)
    assert DummyPlugin in result
    assert AnotherPlugin in result
    assert str not in result
